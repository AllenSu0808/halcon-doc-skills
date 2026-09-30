"""組出可直接複製到專案的 HALCON skill 資料夾。"""

from __future__ import annotations

import logging
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from . import config
from .signatures import ParamRow, SignatureRow, parse_page, write_tsv

log = logging.getLogger(__name__)

# 解析失敗率超過此值時 build-skill 視為失敗
MAX_FAILURE_RATE = 0.01


@dataclass
class LangStats:
    """單一語言的產生統計。"""

    pages: int = 0
    operators: int = 0
    classes: int = 0
    signatures: int = 0
    params: int = 0
    failed: list[str] = field(default_factory=list)

    @property
    def failure_rate(self) -> float:
        """解析失敗頁數 / 運算子頁數。"""
        return len(self.failed) / self.operators if self.operators else 0.0


@dataclass
class BuildReport:
    """build_skill 的結果。"""

    stats: dict[str, LangStats] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """至少產生一種語言，且每種語言失敗率都不超過門檻。"""
        return bool(self.stats) and all(
            s.failure_rate <= MAX_FAILURE_RATE for s in self.stats.values()
        )


def _build_lang(source: Path, dest: Path, lang: str) -> LangStats:
    stats = LangStats()
    signatures: list[SignatureRow] = []
    params: list[ParamRow] = []
    dest.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.glob("*.md")):
        # 不換行空白會讓 grep 找不到簽章，複製時一併換成一般空白
        text = path.read_text(encoding="utf-8").replace(" ", " ")
        (dest / path.name).write_text(text, encoding="utf-8")
        stats.pages += 1
        page = parse_page(text, path.name, lang)
        if page is None:
            continue
        if page.kind == "class":
            stats.classes += 1
        else:
            stats.operators += 1
            if not page.signatures:
                stats.failed.append(path.name)
        signatures += page.signatures
        params += page.params
    write_tsv(dest / "SIGNATURES.tsv", signatures, SignatureRow)
    write_tsv(dest / "PARAMS.tsv", params, ParamRow)
    stats.signatures = len(signatures)
    stats.params = len(params)
    return stats


def build_skill(output: Path, template: Path, dest: Path) -> BuildReport:
    """以 ``template`` 為基礎、``output`` 的文件為參考資料產生 skill。

    :param output: crawl/convert 產出的資料夾（含各語言子資料夾）。
    :param template: 手寫的 skill 範本資料夾（SKILL.md、scripts/、pitfalls/）。
    :param dest: 產出位置；若是先前產生的 skill（含 SKILL.md）會先整個刪除。
    :return: 各語言統計；缺少的語言不會出現在 ``stats``。
    :raises FileExistsError: ``dest`` 已存在但不是先前產生的 skill。
    """
    if dest.exists():
        # 避免 --out 指錯位置（例如 output/）時把資料整個刪掉
        if not (dest / "SKILL.md").is_file():
            raise FileExistsError(f"{dest} 已存在且不是先前產生的 skill，拒絕覆寫")
        shutil.rmtree(dest)
    shutil.copytree(template, dest, ignore=shutil.ignore_patterns("__pycache__"))
    report = BuildReport()
    for lang in config.LANGS:
        source = output / lang
        if not source.is_dir():
            log.warning("略過 %s：找不到 %s", lang, source)
            continue
        report.stats[lang] = _build_lang(source, dest / "references" / lang, lang)
    return report
