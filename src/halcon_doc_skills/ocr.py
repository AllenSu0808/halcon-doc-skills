"""備援：以 latexconvert.com 的網頁介面對 SVG 公式做 OCR。

只驅動網頁介面，不直接呼叫該站的 ``/convert`` 端點（robots.txt 對該路徑
為 Disallow）。循序執行、請求間隔至少數秒、有筆數上限，連續失敗即停止。
"""

from __future__ import annotations

import asyncio
import logging
import tempfile
from dataclasses import dataclass
from pathlib import Path

from playwright.async_api import Error as PlaywrightError
from playwright.async_api import Page, async_playwright, expect

from .assets import normalize_svg
from .formulas import FormulaStore

log = logging.getLogger(__name__)

LATEXCONVERT_URL = "https://latexconvert.com/zh/"
# 上傳後，LaTeX 結果會出現在這個 textarea（2026/09/30 實測）
_OUTPUT_SELECTOR = "textarea.latex-output"
_MAX_CONSECUTIVE_FAILURES = 3


class OcrError(Exception):
    """OCR 沒有產生結果。"""


@dataclass(frozen=True)
class OcrOptions:
    """OCR 備援的節流與上限。"""

    delay: float = 5.0
    max_count: int = 500
    timeout_ms: int = 60_000
    headless: bool = True


@dataclass
class OcrReport:
    """OCR 統計。"""

    done: int = 0
    failed: int = 0


async def render_png(page: Page, svg: str, path: Path) -> None:
    """把公式 SVG 轉成白底 PNG（該網站只接受 JPEG/PNG/GIF/WebP）。"""
    await page.set_content(
        f'<body style="margin:12px;background:#fff;font-size:20px">{svg}</body>'
    )
    await page.locator("svg").first.screenshot(path=str(path))


async def ocr_png(page: Page, png: Path, timeout_ms: int) -> str:
    """上傳 PNG 並讀取 LaTeX 結果。

    :raises OcrError: 逾時內沒有出現結果。
    """
    await page.goto(LATEXCONVERT_URL, wait_until="load", timeout=timeout_ms)
    await page.locator('input[type="file"]').first.set_input_files(str(png))
    output = page.locator(_OUTPUT_SELECTOR)
    try:
        await expect(output).not_to_have_value("", timeout=timeout_ms)
    except AssertionError as exc:
        raise OcrError("等不到 OCR 結果") from exc
    return (await output.input_value()).strip()


async def ocr_pending(
    store: FormulaStore, options: OcrOptions | None = None
) -> OcrReport:
    """對 store 中尚無 LaTeX 的公式逐一 OCR，結果寫回 store。"""
    options = options or OcrOptions()
    todo = store.pending_ocr()[: options.max_count]
    report = OcrReport()
    if not todo:
        return report
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=options.headless)
        try:
            render_ctx = await browser.new_context(device_scale_factor=3)
            ocr_ctx = await browser.new_context()
            render_page = await render_ctx.new_page()
            ocr_page = await ocr_ctx.new_page()
            failures = 0
            with tempfile.TemporaryDirectory() as tmp:
                for number, (key, svg) in enumerate(todo, start=1):
                    data = store.load(key)
                    data["ocr_attempts"] = data.get("ocr_attempts", 0) + 1
                    png = Path(tmp) / f"{key}.png"
                    try:
                        await render_png(render_page, normalize_svg(svg), png)
                        latex = await ocr_png(ocr_page, png, options.timeout_ms)
                    except (OcrError, PlaywrightError) as exc:
                        failures += 1
                        report.failed += 1
                        data["ocr_error"] = str(exc).splitlines()[0]
                        log.warning("OCR 失敗 [%d/%d]：%s", number, len(todo), exc)
                    else:
                        failures = 0
                        if latex:
                            data.update(latex=latex, source="ocr")
                            report.done += 1
                        else:
                            report.failed += 1
                        log.info("OCR [%d/%d] %s", number, len(todo), key)
                    store.save(key, data)
                    if failures >= _MAX_CONSECUTIVE_FAILURES:
                        log.error("連續失敗 %d 次，停止 OCR", failures)
                        break
                    await asyncio.sleep(options.delay)
        finally:
            await browser.close()
    return report
