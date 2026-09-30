"""由轉換後的 Markdown 頁面解析簽章與參數，產生 skill 用的 TSV。"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import astuple, dataclass, fields
from pathlib import Path

from .indexer import read_title_and_summary

# 標題尾端的頁面種類，例如 ``# find_shape_model (Operator)``
_KIND_RE = re.compile(r"^# .+ \((Operator|Class)\)\s*$", re.MULTILINE)
_SECTION_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
_HDEVELOP_SIG_RE = re.compile(r"^([a-z][a-z0-9_]*) ?\((.*)\)$")
_PYTHON_SIG_RE = re.compile(r"^def ([a-z][a-z0-9_]*)\((.*)\) -> .+$")
_DOTNET_MEMBER_RE = re.compile(r"^(?:static )?\S+ (\w+)\.(\w+)\((.*)\)$")
_DOTNET_CTOR_RE = re.compile(r"^public (\w+)\((.*)\)$")
_PARAM_RE = re.compile(r"^\*\*`(\w+)`\*\* \((\w+)\)\s+.*?`→`\s*(.*)$")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_VALUE_RE = re.compile(r"'[^']*'|\"[^\"]*\"|[^,]+")

# 參數屬性標籤 → ParamRow 欄位
_ATTR_FIELDS = {
    "Default:": "default",
    "List of values:": "list_of_values",
    "Suggested values:": "suggested_values",
}

VALUE_SEP = " | "


@dataclass(frozen=True)
class SignatureRow:
    """SIGNATURES.tsv 的一列。"""

    name: str
    kind: str  # operator / method / constructor / class
    owner: str
    signature: str
    summary: str
    page: str


@dataclass(frozen=True)
class ParamRow:
    """PARAMS.tsv 的一列。"""

    page: str
    param: str
    direction: str
    type: str
    default: str
    list_of_values: str
    suggested_values: str


@dataclass(frozen=True)
class ParsedPage:
    """單一頁面的解析結果。"""

    kind: str  # operator / class
    signatures: list[SignatureRow]
    params: list[ParamRow]


def clean(text: str) -> str:
    """把不換行空白、tab 與換行換成一般空白，並去掉頭尾空白。"""
    return re.sub(r"[\s ]+", " ", text).strip()


def sections(md: str) -> dict[str, str]:
    """把頁面切成 ``{段落標題: 內文}``。"""
    matches = list(_SECTION_RE.finditer(md))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(md)
        result[match.group(1)] = md[match.end() : end]
    return result


def _signature_row(
    lang: str, text: str, summary: str, page: str
) -> SignatureRow | None:
    if lang in ("hdevelop", "python"):
        pattern = _HDEVELOP_SIG_RE if lang == "hdevelop" else _PYTHON_SIG_RE
        match = pattern.match(text)
        if not match:
            return None
        return SignatureRow(match[1], "operator", "", text, summary, page)
    ctor = _DOTNET_CTOR_RE.match(text)
    if ctor:
        return SignatureRow(ctor[1], "constructor", ctor[1], text, summary, page)
    member = _DOTNET_MEMBER_RE.match(text)
    if not member:
        return None
    kind = "operator" if member[1] == "HOperatorSet" else "method"
    return SignatureRow(member[2], kind, member[1], text, summary, page)


def _parse_signatures(
    lang: str, body: str, summary: str, page: str
) -> list[SignatureRow]:
    rows: list[SignatureRow] = []
    for line in body.splitlines():
        line = clean(line)
        if not (line.startswith("`") and line.endswith("`") and len(line) > 2):
            continue
        row = _signature_row(lang, line[1:-1], summary, page)
        if row:
            rows.append(row)
    return rows


def split_values(text: str) -> str:
    """把 ``'a', 'b', 1`` 這類清單轉成以 `` | `` 分隔的字串。"""
    values = (clean(v) for v in _VALUE_RE.findall(text))
    return VALUE_SEP.join(v for v in values if v)


def _parse_params(body: str, page: str) -> list[ParamRow]:
    rows: list[ParamRow] = []
    current: dict[str, str] | None = None
    pending: str | None = None  # 等待值的屬性欄位
    collected: list[str] = []

    def flush_attr() -> None:
        nonlocal pending
        if current is not None and pending and collected:
            raw = " ".join(collected)
            current[pending] = raw if pending == "default" else split_values(raw)
        pending = None
        collected.clear()

    def flush_param() -> None:
        flush_attr()
        if current is not None:
            rows.append(ParamRow(page=page, **current))

    for raw_line in body.splitlines():
        line = clean(raw_line)
        header = _PARAM_RE.match(line)
        if header:
            flush_param()
            current = {
                "param": header[1],
                "direction": header[2],
                "type": clean(_LINK_RE.sub(r"\1", header[3]).replace("*", "")),
                "default": "",
                "list_of_values": "",
                "suggested_values": "",
            }
            continue
        if line in _ATTR_FIELDS:
            flush_attr()
            pending = _ATTR_FIELDS[line]
        elif pending and line:
            collected.append(line)
        elif pending:
            flush_attr()
    flush_param()
    return rows


def parse_page(md: str, page: str, lang: str) -> ParsedPage | None:
    """解析一頁運算子或類別頁；其他頁面（目錄、索引）回傳 ``None``。

    :param md: 頁面 Markdown。
    :param page: 頁面檔名，例如 ``find_shape_model.md``。
    :param lang: ``hdevelop`` / ``dotnet`` / ``python``。
    :return: 解析結果；運算子頁沒有任何簽章時 ``signatures`` 為空。
    """
    kind_match = _KIND_RE.search(md)
    if not kind_match:
        return None
    title, summary = read_title_and_summary(md, page)
    summary = clean(summary)
    body = sections(md)
    if kind_match[1] == "Class":
        row = SignatureRow(clean(title), "class", "", "", summary, page)
        return ParsedPage("class", [row], [])
    signatures = _parse_signatures(lang, body.get("Signature", ""), summary, page)
    params = _parse_params(body.get("Parameters", ""), page)
    return ParsedPage("operator", signatures, params)


def write_tsv(path: Path, rows: Iterable[SignatureRow | ParamRow], cls: type) -> None:
    """寫出 tab 分隔檔，首行為欄名；欄位內的空白已先以 ``clean`` 正規化。"""
    header = "\t".join(f.name for f in fields(cls))
    lines = [header] + ["\t".join(clean(v) for v in astuple(r)) for r in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
