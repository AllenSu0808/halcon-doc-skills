"""HALCON 參考資料的讀取與名稱比對（halcon_doc.py 與 halcon_check.py 共用）。"""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from pathlib import Path

LANGS = ("hdevelop", "dotnet", "python")
REFERENCES = Path(__file__).resolve().parent.parent / "references"
VALUE_SEP = " | "

# 語言推斷時略過的資料夾
_SKIP_DIRS = {".git", ".claude", ".venv", "venv", "node_modules", "bin", "obj"}
_SECTION_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
_PARAM_HEADER_RE = re.compile(r"^\*\*`(\w+)`\*\*", re.MULTILINE)


class DocError(Exception):
    """查詢失敗（語言未安裝、查無運算子等），訊息直接給使用者看。"""


@dataclass(frozen=True)
class Signature:
    """SIGNATURES.tsv 的一列。"""

    name: str
    kind: str
    owner: str
    signature: str
    summary: str
    page: str


@dataclass(frozen=True)
class Param:
    """PARAMS.tsv 的一列。"""

    page: str
    param: str
    direction: str
    type: str
    default: str
    list_of_values: str
    suggested_values: str

    def values(self) -> list[str]:
        """合法值清單（去掉引號）；沒有嚴格列舉時為空。"""
        if not self.list_of_values:
            return []
        return [v.strip("'\"") for v in self.list_of_values.split(VALUE_SEP)]


def key(name: str) -> str:
    """名稱比對鍵：去掉前綴、底線並轉小寫，讓各語言寫法對應到同一運算子。"""
    return name.rsplit(".", 1)[-1].replace("_", "").lower()


def _read_tsv(path: Path) -> list[list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.split("\t") for line in lines[1:] if line]


class Reference:
    """單一語言的參考資料。"""

    def __init__(self, root: Path, lang: str) -> None:
        self.lang = lang
        self.dir = root / lang
        sig_path = self.dir / "SIGNATURES.tsv"
        param_path = self.dir / "PARAMS.tsv"
        if not sig_path.is_file() or not param_path.is_file():
            installed = ", ".join(available_langs(root)) or "無"
            raise DocError(f"{lang} 文件未安裝（已安裝：{installed}）")
        self.signatures = [Signature(*row) for row in _read_tsv(sig_path)]
        self.params = [Param(*row) for row in _read_tsv(param_path)]

    def pages(self, name: str) -> list[str]:
        """由任意寫法的名稱找出頁面檔名；查無時拋出含相近名稱的 DocError。"""
        wanted = key(name)
        found = {
            s.page
            for s in self.signatures
            if key(s.name) == wanted or key(Path(s.page).stem) == wanted
        }
        if found:
            return sorted(found)
        raise DocError(f"查無「{name}」。{self.suggest(name)}")

    def suggest(self, name: str) -> str:
        """回傳相近名稱提示字串。"""
        names = sorted({s.name for s in self.signatures})
        lowered = {n.lower(): n for n in names}
        close = difflib.get_close_matches(
            name.rsplit(".", 1)[-1].lower(), list(lowered), n=5, cutoff=0.6
        )
        if not close:
            return "請改用 search 以關鍵字查詢。"
        return "相近名稱：" + ", ".join(lowered[c] for c in close)

    def rows_for(self, page: str) -> list[Signature]:
        """該頁的所有簽章列（不含類別列）。"""
        return [s for s in self.signatures if s.page == page and s.kind != "class"]

    def params_for(self, page: str) -> list[Param]:
        """該頁的所有參數（依頁面順序）。"""
        return [p for p in self.params if p.page == page]

    def read_page(self, page: str) -> str:
        """讀取頁面 Markdown。"""
        return (self.dir / page).read_text(encoding="utf-8")


def available_langs(root: Path = REFERENCES) -> list[str]:
    """已安裝的語言。"""
    return [lang for lang in LANGS if (root / lang / "SIGNATURES.tsv").is_file()]


def detect_lang(start: Path) -> str:
    """由專案檔案推斷語言（只看起點與往下兩層）。

    :raises DocError: 無法判斷或同時符合多種語言時。
    """
    found: set[str] = set()
    for path in _walk(start, depth=2):
        name = path.name.lower()
        if name.endswith(".csproj"):
            found.add("dotnet")
        elif name == "pyproject.toml" or name.endswith(".py"):
            found.add("python")
        elif name.endswith((".hdev", ".hdvp")):
            found.add("hdevelop")
    if len(found) == 1:
        return found.pop()
    hint = "、".join(sorted(found)) if found else "找不到 .csproj / .py / .hdev"
    raise DocError(f"無法判斷語言（{hint}），請加上 --lang {{{','.join(LANGS)}}}")


def _walk(root: Path, depth: int) -> list[Path]:
    result: list[Path] = []
    try:
        entries = list(root.iterdir())
    except OSError:
        return result
    for entry in entries:
        if entry.is_dir():
            if depth > 0 and entry.name not in _SKIP_DIRS:
                result += _walk(entry, depth - 1)
        else:
            result.append(entry)
    return result


def sections(md: str) -> dict[str, str]:
    """把頁面切成 ``{段落標題: 內文}``。"""
    matches = list(_SECTION_RE.finditer(md))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(md)
        result[match.group(1)] = md[match.end() : end].strip("\n")
    return result


def param_blocks(parameters: str) -> dict[str, str]:
    """把 ``## Parameters`` 段落切成 ``{參數名: 原文}``。"""
    matches = list(_PARAM_HEADER_RE.finditer(parameters))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(parameters)
        )
        result[match.group(1)] = parameters[match.start() : end].strip()
    return result
