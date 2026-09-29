"""輸出品質檢查：連結與圖片路徑、重複文字、各語言檔案數。"""

from __future__ import annotations

import os
import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

from . import config

_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)[^)]*\)")
_LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
_REPEAT_RE = re.compile(r"\b([A-Za-z_]{4,})\1\b")
_ESCAPED_DOLLAR_RE = re.compile(r"\\\$")
_EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "#")


@dataclass
class VerifyReport:
    """檢查結果。"""

    problems: list[str] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """沒有任何問題時為 True。"""
        return not self.problems


def verify_output(
    output_dir: Path, langs: Sequence[str] = config.LANGS
) -> VerifyReport:
    """檢查輸出資料夾。

    :param output_dir: 輸出根目錄。
    :param langs: 要檢查的語言資料夾。
    :return: 問題清單與各語言 .md 檔案數。
    """
    output_dir = Path(output_dir)
    report = VerifyReport()
    for lang in langs:
        lang_dir = output_dir / lang
        if not lang_dir.is_dir():
            report.problems.append(f"缺少語言資料夾：{lang}")
            continue
        if not (lang_dir / "INDEX.md").exists():
            report.problems.append(f"缺少 INDEX.md：{lang}")
        files = sorted(p for p in lang_dir.rglob("*.md") if p.name != "INDEX.md")
        report.counts[lang] = len(files)
        for md_file in sorted(lang_dir.rglob("*.md")):
            _check_file(md_file, output_dir, report)
    return report


def _check_file(md_file: Path, root: Path, report: VerifyReport) -> None:
    rel = md_file.relative_to(root).as_posix()
    text = md_file.read_text(encoding="utf-8")
    text = _FENCE_RE.sub("", text)
    scan = _INLINE_CODE_RE.sub("", text)
    for target in _LINK_RE.findall(scan):
        if target.startswith(_EXTERNAL_PREFIXES):
            continue
        path = Path(os.path.normpath(md_file.parent / unquote(target.split("#")[0])))
        if not path.exists():
            report.problems.append(f"{rel}：連結目標不存在 {target}")
    plain = _ESCAPED_DOLLAR_RE.sub("", scan)
    if plain.count("$$") % 2 or plain.replace("$$", "").count("$") % 2:
        report.problems.append(f"{rel}：公式定界符 $ 不成對")
    if "@@FORMULA:" in text:
        report.problems.append(f"{rel}：殘留公式標記 @@FORMULA:")
    repeated = _REPEAT_RE.search(_LINK_TARGET_RE.sub("]", text))
    if repeated:
        report.problems.append(f"{rel}：疑似語言重複文字 {repeated.group(0)}")
