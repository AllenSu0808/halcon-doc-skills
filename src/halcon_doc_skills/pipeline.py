"""爬取（crawl）與離線轉換（convert_all）流程。"""

from __future__ import annotations

import asyncio
import logging
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin

from playwright.async_api import Browser, BrowserContext, Page, async_playwright
from playwright.async_api import Error as PlaywrightError

from . import config
from .assets import image_asset_name
from .cache import PageCache
from .converter import convert_page, is_stub_page
from .crawler import Frontier, md_name, normalize_url, page_name
from .extractor import PageExtract, PageFetchError, extract_page
from .formulas import FormulaResult, FormulaStore, scan_and_decode
from .indexer import (
    IndexEntry,
    build_index,
    category_from_breadcrumb,
    read_title_and_summary,
)
from .ocr import OcrOptions, ocr_pending

log = logging.getLogger(__name__)


@dataclass
class CrawlReport:
    """爬取統計。"""

    fetched: int = 0
    skipped: int = 0
    failed: list[str] = field(default_factory=list)


@dataclass
class ConvertReport:
    """轉換統計（以語言為鍵）。"""

    converted: dict[str, int] = field(default_factory=dict)
    skipped_stubs: dict[str, int] = field(default_factory=dict)


@dataclass
class FormulaReport:
    """公式處理統計。"""

    total: int = 0
    decoded: int = 0
    ocr: int = 0
    unresolved: int = 0
    rejected: Counter[str] = field(default_factory=Counter)


@dataclass(frozen=True)
class _Options:
    force: bool
    delay: float
    retries: int


async def crawl(
    cache: PageCache,
    output_dir: Path,
    *,
    concurrency: int = config.DEFAULT_CONCURRENCY,
    limit: int | None = None,
    force: bool = False,
    delay: float = config.DEFAULT_DELAY,
    retries: int = config.DEFAULT_RETRIES,
    entries: Sequence[str] | None = None,
    headless: bool = True,
) -> CrawlReport:
    """以廣度優先爬取文件頁並寫入快取與圖片資產。

    :param cache: 頁面快取。
    :param output_dir: 輸出根目錄（圖片放在其下的 ``assets/``）。
    :param concurrency: 同時開啟的分頁（worker）數。
    :param limit: 最多處理的不同網址數（試跑用）。
    :param force: True 時忽略已完成的快取，重新擷取。
    :param delay: 每次成功擷取後的等待秒數。
    :param retries: 每頁最多嘗試次數。
    :param entries: 入口頁（相對於 ``config.BASE_URL``），預設用設定值。
    :param headless: 是否以無頭模式啟動瀏覽器。
    :return: 爬取統計。
    """
    frontier = Frontier(limit)
    queue: asyncio.Queue[str] = asyncio.Queue()
    report = CrawlReport()
    options = _Options(force=force, delay=delay, retries=retries)
    for entry in entries if entries is not None else config.ENTRY_PAGES:
        url = urljoin(config.BASE_URL, entry)
        if frontier.add(url):
            queue.put_nowait(url)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=headless)
        try:
            workers = [
                asyncio.create_task(
                    _worker(
                        browser,
                        queue,
                        frontier,
                        cache,
                        Path(output_dir) / "assets",
                        report,
                        options,
                    )
                )
                for _ in range(concurrency)
            ]
            join = asyncio.create_task(queue.join())
            finished, _ = await asyncio.wait(
                {join, *workers}, return_when=asyncio.FIRST_COMPLETED
            )
            for task in finished:
                if task is not join:
                    task.result()  # worker 意外結束時重新拋出例外，避免卡住
            for task in (join, *workers):
                task.cancel()
            await asyncio.gather(join, *workers, return_exceptions=True)
        finally:
            await browser.close()
    log.info(
        "爬取完成：新增 %d、略過 %d、失敗 %d",
        report.fetched,
        report.skipped,
        len(report.failed),
    )
    return report


async def _worker(
    browser: Browser,
    queue: asyncio.Queue[str],
    frontier: Frontier,
    cache: PageCache,
    assets_dir: Path,
    report: CrawlReport,
    options: _Options,
) -> None:
    """從佇列取網址處理；每個 worker 使用獨立的 browser context。"""
    context = await browser.new_context()
    page = await context.new_page()
    try:
        while True:
            url = await queue.get()
            try:
                links = await _handle_url(page, url, cache, assets_dir, report, options)
            except (PageFetchError, PlaywrightError) as exc:
                log.error("失敗：%s（%s）", url, exc)
                cache.record_failure(url, str(exc).splitlines()[0])
                report.failed.append(url)
            else:
                for link in links:
                    normalized = normalize_url(link, url)
                    if normalized and frontier.add(normalized):
                        queue.put_nowait(normalized)
            finally:
                queue.task_done()
    finally:
        await context.close()


async def _handle_url(
    page: Page,
    url: str,
    cache: PageCache,
    assets_dir: Path,
    report: CrawlReport,
    options: _Options,
) -> list[str]:
    """處理單一網址，回傳該頁連結供後續入列。"""
    name = page_name(url)
    if not options.force and cache.is_complete(name):
        report.skipped += 1
        return cache.load_meta(name)["links"]
    extract = await _fetch_with_retry(page, url, options.retries)
    cache.save(name, extract)
    await _download_images(page.context, extract.image_urls, assets_dir)
    report.fetched += 1
    done = report.fetched + report.skipped + len(report.failed)
    log.info("[%d] %s", done, name)
    await asyncio.sleep(options.delay)
    return extract.links


async def _fetch_with_retry(page: Page, url: str, retries: int) -> PageExtract:
    """擷取頁面；可重試的錯誤以指數退避重試，不可重試（如 404）立即放棄。"""
    attempt = 0
    while True:
        attempt += 1
        try:
            return await extract_page(page, url)
        except PageFetchError as exc:
            if not exc.retryable or attempt >= retries:
                raise
            log.warning("重試 %d/%d：%s（%s）", attempt, retries, url, exc)
        except PlaywrightError as exc:
            if attempt >= retries:
                raise
            log.warning("重試 %d/%d：%s（%s）", attempt, retries, url, exc)
        await asyncio.sleep(2 ** (attempt - 1))


async def _download_images(
    context: BrowserContext, urls: Sequence[str], assets_dir: Path
) -> None:
    """下載內容中的 ``<img>`` 到共用資產資料夾；失敗只記警告。"""
    for url in urls:
        path = assets_dir / image_asset_name(url)
        if path.exists():
            continue
        try:
            response = await context.request.get(url)
        except PlaywrightError as exc:
            log.warning("圖片下載失敗：%s（%s）", url, exc)
            continue
        if not response.ok:
            log.warning("圖片下載失敗：%s（HTTP %d）", url, response.status)
            continue
        assets_dir.mkdir(parents=True, exist_ok=True)
        path.write_bytes(await response.body())


def resolve_formulas(
    cache: PageCache,
    store: FormulaStore,
    ocr_options: OcrOptions | None = None,
) -> FormulaReport:
    """字形解碼快取內所有公式；給了 ``ocr_options`` 時對被拒者做 OCR 備援。

    :param cache: 頁面快取。
    :param store: 公式結果快取（``cache/latex``）。
    :param ocr_options: None 表示不啟用 OCR（預設）。
    :return: 公式統計（只計目前快取內出現的公式）。
    """
    decode_report = scan_and_decode(cache, store)
    if ocr_options is not None:
        ocr_report = asyncio.run(ocr_pending(store, ocr_options))
        log.info("OCR 完成：成功 %d、失敗 %d", ocr_report.done, ocr_report.failed)
    results = {
        key: result
        for key, result in store.results().items()
        if key in decode_report.keys
    }
    report = FormulaReport(total=decode_report.total, rejected=decode_report.rejected)
    report.decoded = sum(r.source == "decode" for r in results.values())
    report.ocr = sum(r.source == "ocr" for r in results.values())
    report.unresolved = report.total - len(results)
    log.info(
        "公式：共 %d 個，字形解碼 %d、OCR %d、保留圖檔 %d；被拒原因：%s",
        report.total,
        report.decoded,
        report.ocr,
        report.unresolved,
        dict(report.rejected),
    )
    return report


def convert_all(
    cache: PageCache,
    output_dir: Path,
    langs: Sequence[str] = config.LANGS,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> ConvertReport:
    """離線將快取轉成 Markdown，略過空殼頁並產生各語言 INDEX.md。

    :param cache: 頁面快取。
    :param output_dir: 輸出根目錄。
    :param langs: 要轉換的語言。
    :param formulas: 公式鍵 → LaTeX 結果（通常是 ``store.results()``）。
    :return: 各語言的轉換與略過數量。
    """
    output_dir = Path(output_dir)
    assets_dir = output_dir / "assets"
    pages = cache.pages()
    report = ConvertReport()
    for lang in langs:
        real = {p for p in pages if not is_stub_page(cache.load_html(lang, p))}
        index_entries: list[IndexEntry] = []
        for number, page in enumerate(sorted(real), start=1):
            meta = cache.load_meta(page)
            markdown = convert_page(
                cache.load_html(lang, page),
                meta["url"],
                lang,
                real,
                assets_dir,
                formulas,
            )
            target = output_dir / lang / md_name(page)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
            title, summary = read_title_and_summary(markdown, page)
            category = category_from_breadcrumb(meta["breadcrumb"])
            index_entries.append(IndexEntry(page, title, summary, category))
            if number % 200 == 0:
                log.info("[%s] 已轉換 %d / %d", lang, number, len(real))
        index_path = output_dir / lang / "INDEX.md"
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(build_index(lang, index_entries), encoding="utf-8")
        report.converted[lang] = len(real)
        report.skipped_stubs[lang] = len(pages) - len(real)
        log.info(
            "[%s] 轉換 %d 頁，略過空殼頁 %d",
            lang,
            len(real),
            len(pages) - len(real),
        )
    return report
