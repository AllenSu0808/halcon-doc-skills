"""產生各語言資料夾的 INDEX.md。"""

from __future__ import annotations

import posixpath
import re
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass

from .crawler import md_name

_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
_SUFFIX_RE = re.compile(r"\s*\((?:Operator|Class)\)\s*$")
_SUMMARY_RE = re.compile(r"^## Name\s*\n+[^\n]*?—\s*([^\n]+)", re.MULTILINE)

# 麵包屑前兩層是「HALCON 版本」與「HALCON Operator Reference」，不屬於分類
_BREADCRUMB_SKIP = 2


@dataclass(frozen=True)
class IndexEntry:
    """索引中的一筆頁面。"""

    name: str
    title: str
    summary: str
    category: str


def category_from_breadcrumb(breadcrumb: Sequence[Sequence[str]]) -> str:
    """由麵包屑取得分類路徑，例如 ``Filters / Arithmetic``。"""
    texts = [item[0] for item in breadcrumb][_BREADCRUMB_SKIP:]
    return " / ".join(texts) or "Other"


def read_title_and_summary(md: str, page: str) -> tuple[str, str]:
    """從轉換後的 Markdown 取出標題與一句話摘要。"""
    match = _HEADING_RE.search(md)
    if match:
        title = _SUFFIX_RE.sub("", match.group(1))
    else:
        title = posixpath.splitext(posixpath.basename(page))[0]
    summary_match = _SUMMARY_RE.search(md)
    summary = summary_match.group(1).strip() if summary_match else ""
    return title, summary


def _line(entry: IndexEntry) -> str:
    link = f"[{entry.title}]({md_name(entry.name)})"
    return f"- {link} — {entry.summary}" if entry.summary else f"- {link}"


def build_index(lang: str, entries: Sequence[IndexEntry]) -> str:
    """產生索引 Markdown：先列目錄頁，再依分類列出其餘頁面。"""
    lines = [f"# HALCON 26.05 Reference Index ({lang})", ""]
    toc = sorted(
        (e for e in entries if e.name.startswith("toc_")), key=lambda e: e.name
    )
    if toc:
        lines += ["## Table of Contents", ""]
        lines += [_line(e) for e in toc] + [""]
    by_category: dict[str, list[IndexEntry]] = defaultdict(list)
    for entry in entries:
        if not entry.name.startswith("toc_"):
            by_category[entry.category].append(entry)
    for category in sorted(by_category):
        lines += [f"## {category}", ""]
        ordered = sorted(by_category[category], key=lambda e: (e.title.lower(), e.name))
        lines += [_line(e) for e in ordered] + [""]
    return "\n".join(lines).rstrip() + "\n"
