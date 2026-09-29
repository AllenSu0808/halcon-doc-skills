"""命令列介面：crawl / convert / verify。"""

from __future__ import annotations

import argparse
import asyncio
import logging
from collections.abc import Sequence
from pathlib import Path

from . import config
from .cache import PageCache
from .formulas import FormulaStore
from .ocr import OcrOptions
from .pipeline import convert_all, crawl, resolve_formulas
from .verify import verify_output

log = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """建立命令列解析器。"""
    parser = argparse.ArgumentParser(
        prog="halcon-doc-skills",
        description="爬取 HALCON 文件並轉成各語言的 Markdown。",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    crawl_p = sub.add_parser("crawl", help="爬取並轉換")
    _add_paths(crawl_p, cache=True)
    crawl_p.add_argument("--concurrency", type=int, default=config.DEFAULT_CONCURRENCY)
    crawl_p.add_argument("--limit", type=int, default=None, help="最多處理頁數（試跑）")
    crawl_p.add_argument(
        "--entry",
        action="append",
        dest="entries",
        default=None,
        help="覆寫入口頁（相對於文件根目錄，可重複）",
    )
    crawl_p.add_argument("--force", action="store_true", help="忽略快取重新擷取")
    crawl_p.add_argument("--delay", type=float, default=config.DEFAULT_DELAY)
    _add_ocr_options(crawl_p)

    convert_p = sub.add_parser("convert", help="僅以快取重新轉換")
    _add_paths(convert_p, cache=True)
    _add_ocr_options(convert_p)

    verify_p = sub.add_parser("verify", help="檢查輸出品質")
    _add_paths(verify_p, cache=False)
    return parser


def _add_paths(parser: argparse.ArgumentParser, cache: bool) -> None:
    if cache:
        parser.add_argument("--cache-dir", type=Path, default=Path("cache"))
    parser.add_argument("--output", type=Path, default=Path("output"))


def _add_ocr_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--ocr-fallback",
        action="store_true",
        help="字形解碼被拒的公式改用 latexconvert.com 做 OCR（會上傳圖片到第三方）",
    )
    parser.add_argument("--ocr-delay", type=float, default=5.0, help="OCR 請求間隔秒數")
    parser.add_argument("--ocr-max", type=int, default=500, help="單次最多 OCR 筆數")


def _convert(cache: PageCache, args: argparse.Namespace) -> None:
    """解碼公式（可選 OCR 備援）後轉換全部頁面。"""
    store = FormulaStore(cache.root / "latex")
    ocr_options = (
        OcrOptions(delay=args.ocr_delay, max_count=args.ocr_max)
        if args.ocr_fallback
        else None
    )
    resolve_formulas(cache, store, ocr_options)
    convert_all(cache, args.output, formulas=store.results())


def main(argv: Sequence[str] | None = None) -> int:
    """程式進入點。

    :return: 結束碼；``verify`` 發現問題時為 1，其餘為 0。
    """
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    if args.command == "verify":
        report = verify_output(args.output)
        for problem in report.problems:
            log.error(problem)
        log.info("各語言 .md 檔案數：%s", report.counts)
        return 0 if report.ok else 1

    cache = PageCache(args.cache_dir)
    if args.command == "crawl":
        asyncio.run(
            crawl(
                cache,
                args.output,
                concurrency=args.concurrency,
                limit=args.limit,
                force=args.force,
                delay=args.delay,
                entries=args.entries,
            )
        )
    _convert(cache, args)
    return 0
