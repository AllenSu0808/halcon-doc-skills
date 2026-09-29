"""公式處理：由 MetaPost SVG 的字形還原 LaTeX，並管理結果快取。

站上的公式是 MetaPost 排版後的行內 SVG，每個字元都是
``<use xlink:href="#GLYPH<字型>_<字碼>">``。只要字型與字碼對照表齊全、
版面單純（單一基線，最多一層上下標），就能不靠 OCR 精確還原。
其餘情況一律拋出 ``Reject``，交給備援（OCR）或保留原圖。
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cache import PageCache

# 公式容器：span.math（行內）或 span.displaymath（獨立），內含註解與 <svg>
FORMULA_RE = re.compile(
    r'<span\b[^>]*\bclass="(?P<cls>displaymath|math)"[^>]*>'
    r"(?:\s*<!--.*?-->)?\s*(?P<svg><svg\b.*?</svg>)\s*</span>",
    re.DOTALL,
)
# converter 在 Markdown 產生後才把此標記換成 LaTeX，避免被 markdownify 跳脫
TOKEN_RE = re.compile(r"@@FORMULA:([0-9a-f]{16}):([di]):([^@\s]+)@@")

_GREEK_UPPER = [
    r"\Gamma", r"\Delta", r"\Theta", r"\Lambda", r"\Xi", r"\Pi",
    r"\Sigma", r"\Upsilon", r"\Phi", r"\Psi", r"\Omega",
]  # fmt: skip
_GREEK_LOWER = [
    r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", r"\zeta",
    r"\eta", r"\theta", r"\iota", r"\kappa", r"\lambda", r"\mu", r"\nu",
    r"\xi", r"\pi", r"\rho", r"\sigma", r"\tau", r"\upsilon", r"\phi",
    r"\chi", r"\psi", r"\omega", r"\varepsilon", r"\vartheta", r"\varpi",
    r"\varrho", r"\varsigma", r"\varphi",
]  # fmt: skip


def _ascii(codes: Iterable[int]) -> dict[int, str]:
    return {code: chr(code) for code in codes}


# cmr10：羅馬字型。數字、標點、字母沿用 ASCII 位置
_CMR = _ascii(range(33, 127))
for _code in (34, 92, 94, 95, 96, 123, 124, 125, 126):
    _CMR.pop(_code, None)
_CMR.update(dict(enumerate(_GREEK_UPPER)))
_CMR.update({123: "-", 124: "--"})

# cmmi10：數學斜體。字母沿用 ASCII 位置，另有希臘字母
_CMMI = dict(enumerate(_GREEK_UPPER))
_CMMI.update({11 + i: name for i, name in enumerate(_GREEK_LOWER)})
_CMMI.update({58: ".", 59: ",", 60: "<", 61: "/", 62: ">", 64: r"\partial"})
_CMMI.update(_ascii(list(range(65, 91)) + list(range(97, 123))))

# cmsy10：數學符號（只收錄常見者；查不到的字碼會退回備援）
_CMSY = {
    0: "-", 1: r"\cdot", 2: r"\times", 3: r"\ast", 4: r"\div", 6: r"\pm",
    7: r"\mp", 14: r"\circ", 15: r"\bullet", 17: r"\equiv", 18: r"\subseteq",
    19: r"\supseteq", 20: r"\le", 21: r"\ge", 24: r"\sim", 25: r"\approx",
    26: r"\subset", 27: r"\supset", 28: r"\ll", 29: r"\gg",
    32: r"\leftarrow", 33: r"\rightarrow", 36: r"\leftrightarrow",
    40: r"\Leftarrow", 41: r"\Rightarrow", 44: r"\Leftrightarrow",
    47: r"\propto", 48: r"\prime", 49: r"\infty", 50: r"\in", 51: r"\ni",
    56: r"\forall", 57: r"\exists", 58: r"\neg", 59: r"\emptyset",
    62: r"\top", 63: r"\bot", 91: r"\cup", 92: r"\cap", 94: r"\wedge",
    95: r"\vee", 102: r"\{", 103: r"\}", 106: "|", 107: r"\|",
    110: r"\setminus", 114: r"\nabla",
}  # fmt: skip
_CMSY.update({code: rf"\mathcal{{{chr(code)}}}" for code in range(65, 91)})

_ASCII_TEXT = _ascii(range(33, 127))
_ASCII_TEXT[34] = '"'

# 字型家族 → (種類, 字碼對照表)
_FAMILY = {
    "cmr": ("rm", _CMR),
    "cmmi": ("math", _CMMI),
    "cmsy": ("sym", _CMSY),
    "pcrr": ("tt", _ASCII_TEXT),
    "ptmr": ("text", _ASCII_TEXT),
    "ptmri": ("textit", _ASCII_TEXT),
    "cmti": ("textit", _ASCII_TEXT),
    "cmbx": ("bf", _CMR),
}
_FONT_RE = re.compile(r"^(?:(cmr|cmmi|cmsy|cmex|cmti|cmbx)(\d+)|(pcrr|ptmr|ptmri)8r)$")
_WRAP = {
    "tt": r"\texttt",
    "text": r"\text",
    "textit": r"\textit",
    "bf": r"\mathbf",
}
_FUNCTIONS = {
    "sin", "cos", "tan", "cot", "sec", "csc", "exp", "log", "ln", "min",
    "max", "det", "arg", "lim", "sup", "inf", "deg", "gcd", "sinh", "cosh",
    "tanh",
}  # fmt: skip
_TEXT_ESCAPES = {
    "#": r"\#", "$": r"\$", "%": r"\%", "&": r"\&", "_": r"\_",
    "{": r"\{", "}": r"\}", "^": r"\^{}", "~": r"\~{}",
}  # fmt: skip
# 同一條基線的容許誤差；超過視為多基線（分數、矩陣、多行）
_BASELINE_TOLERANCE = 1.0
_SCRIPT_OFFSET = 0.5


class Reject(Exception):
    """無法可靠解碼；訊息是簡短的原因代碼（用於統計）。"""


@dataclass(frozen=True)
class FormulaResult:
    """公式的 LaTeX 結果。``source`` 為 ``decode`` 或 ``ocr``。"""

    latex: str
    source: str


@dataclass(frozen=True)
class _Glyph:
    x: float
    y: float
    family: str
    size: int
    code: int
    group: int


def formula_key(svg: str) -> str:
    """公式 SVG（原始字串）的快取鍵。"""
    return hashlib.sha1(svg.encode("utf-8")).hexdigest()[:16]


def collect_formula_svgs(html: str) -> list[tuple[str, bool]]:
    """取出 HTML 內所有公式，回傳 ``(svg, 是否為獨立公式)`` 清單。"""
    return [
        (m.group("svg"), m.group("cls") == "displaymath")
        for m in FORMULA_RE.finditer(html)
    ]


def _split_font(name: str) -> tuple[str, int]:
    """``cmmi7`` → ``("cmmi", 7)``；``pcrr8r`` → ``("pcrr", 10)``。"""
    match = _FONT_RE.match(name)
    if not match:
        raise Reject(f"font:{name}")
    if match.group(1):
        return match.group(1), int(match.group(2))
    return match.group(3), 10


def _parse_glyphs(svg: str) -> list[_Glyph]:
    """依 x 座標排序取出所有字形；有任何無法處理的元素就拒絕。"""
    start = svg.find("</defs>")
    if start < 0:
        raise Reject("no-defs")
    body = svg[start:]
    if re.search(r"<(path|rect|line|polygon|circle|ellipse)\b", body):
        raise Reject("rule")  # 分數線、根號橫線等
    glyphs: list[_Glyph] = []
    groups = re.finditer(
        r'<g transform="matrix\(([^)]*)\)"[^>]*>(.*?)</g>', body, re.DOTALL
    )
    for index, group in enumerate(groups):
        matrix = [float(v) for v in re.split(r"[,\s]+", group.group(1).strip())]
        uses = re.finditer(
            r'<use xlink:href="#GLYPH([a-z0-9]+)_(\d+)"(?: x="([-\d.]+)")?',
            group.group(2),
        )
        for use in uses:
            family, size = _split_font(use.group(1))
            offset = float(use.group(3) or 0)
            glyphs.append(
                _Glyph(
                    x=matrix[4] + matrix[0] * offset,
                    y=matrix[5],
                    family=family,
                    size=size,
                    code=int(use.group(2)),
                    group=index,
                )
            )
    if not glyphs:
        raise Reject("empty")
    # 完整性檢查：解析到的字形數必須等於 <use> 數，避免靜默漏字
    if len(glyphs) != len(re.findall(r"<use\b", body)):
        raise Reject("unparsed-use")
    return sorted(glyphs, key=lambda g: g.x)


def _emit_run(kind: str, chars: list[str]) -> str:
    """把同種類的連續字元轉成 LaTeX 片段。"""
    if kind == "rm":  # 數字與標點直接輸出，連續字母包成 \mathrm 或函數名
        parts: list[str] = []
        i = 0
        while i < len(chars):
            if not chars[i].isalpha():
                parts.append(chars[i])
                i += 1
                continue
            j = i
            while j < len(chars) and chars[j].isalpha():
                j += 1
            word = "".join(chars[i:j])
            if word in _FUNCTIONS:
                parts.append(f"\\{word} ")
            else:
                parts.append(rf"\mathrm{{{word}}}")
            i = j
        return "".join(parts)
    if kind in _WRAP:
        text = "".join(chars)
        if not any(c.isalnum() for c in text):  # 純標點（如括號）不需要包 \text
            return "".join(_TEXT_ESCAPES.get(c, c) for c in text)
        escaped = "".join(_TEXT_ESCAPES.get(c, c) for c in chars)
        return f"{_WRAP[kind]}{{{escaped}}}"
    return _join(chars)  # math、sym：指令後接字母要補空白


def _render(items: list[tuple[str, str, int]]) -> str:
    """``(種類, 字元, 群組)`` 序列 → LaTeX。文字字型在群組邊界補空白。"""
    tokens: list[str] = []
    i = 0
    while i < len(items):
        kind = items[i][0]
        chars: list[str] = []
        j = i
        while j < len(items) and items[j][0] == kind:
            if j > i and kind in ("text", "textit", "tt"):
                if items[j][2] != items[j - 1][2]:
                    chars.append(" ")
            chars.append(items[j][1])
            j += 1
            if kind == "sym":  # 符號逐個輸出，避免相鄰指令黏在一起
                break
        tokens.append(_emit_run(kind, chars))
        i = j
    return _join(tokens)


def _join(tokens: list[str]) -> str:
    """串接片段；指令（如 ``\\le``）後面接字母時補一個空白。"""
    result = ""
    for token in tokens:
        if result and re.search(r"\\[A-Za-z]+$", result) and token[:1].isalpha():
            result += " "
        result += token
    return result.strip()


def decode_svg(svg: str) -> str:
    """由字形還原 LaTeX。

    :param svg: 公式的行內 SVG 字串。
    :return: LaTeX 字串（不含 ``$`` 定界符）。
    :raises Reject: 版面或字型超出可可靠解碼的範圍。
    """
    glyphs = _parse_glyphs(svg)
    for glyph in glyphs:
        if glyph.family == "cmex":  # 大括號、矩陣括號、根號、求和積分
            raise Reject("cmex")
        if glyph.code not in _FAMILY[glyph.family][1]:
            raise Reject(f"code:{glyph.family}{glyph.size}_{glyph.code}")
    mains = [g for g in glyphs if g.size >= 10]
    if not mains:
        raise Reject("no-main")
    base = collections.Counter(round(g.y, 1) for g in mains).most_common(1)[0][0]
    if any(abs(g.y - base) > _BASELINE_TOLERANCE for g in mains):
        raise Reject("multi-baseline")
    if any(g.size < 7 for g in glyphs):
        raise Reject("nested-script")

    atoms: list[dict] = []  # 每個主字形一個 atom，附帶它的上下標
    for glyph in glyphs:
        kind, table = _FAMILY[glyph.family]
        item = (kind, table[glyph.code], glyph.group)
        if glyph.size >= 10:
            atoms.append({"main": item, "sup": [], "sub": []})
            continue
        if not atoms:
            raise Reject("script-first")
        if glyph.y < base - _SCRIPT_OFFSET:
            atoms[-1]["sup"].append(item)
        elif glyph.y > base + _SCRIPT_OFFSET:
            atoms[-1]["sub"].append(item)
        else:
            raise Reject("script-on-baseline")

    segments: list[str] = []
    pending: list[tuple[str, str, int]] = []  # 尚未輸出的相鄰主字形
    for atom in atoms:
        pending.append(atom["main"])
        if not atom["sup"] and not atom["sub"]:
            continue
        segments.append(_render(pending))
        pending = []
        if atom["sub"]:
            segments[-1] += f"_{{{_render(atom['sub'])}}}"
        if atom["sup"]:
            segments[-1] += f"^{{{_render(atom['sup'])}}}"
    if pending:
        segments.append(_render(pending))
    return _join(segments)


def make_token(key: str, display: bool, asset: str | None) -> str:
    """產生給 converter 的公式標記；``asset`` 為 None 表示不附圖。"""
    return f"@@FORMULA:{key}:{'d' if display else 'i'}:{asset or '-'}@@"


def render_tokens(
    markdown: str, formulas: Mapping[str, FormulaResult], rel_assets: str
) -> str:
    """把 Markdown 中的公式標記換成 ``$…$`` / ``$$…$$``（OCR 結果另附圖檔）。"""

    def _replace(match: re.Match[str]) -> str:
        key, mode, asset = match.groups()
        result = formulas.get(key)
        if result is None:  # 標記沒有對應結果（不應發生）：保留提示便於 verify 抓到
            return match.group(0)
        latex = " ".join(result.latex.split())
        text = f"$${latex}$$" if mode == "d" else f"${latex}$"
        if asset != "-":
            text += f" ![figure]({rel_assets}/{asset})"
        return text

    return TOKEN_RE.sub(_replace, markdown)


@dataclass
class FormulaStore:
    """``cache/latex/<key>.json``：每個不同的公式一個檔。

    欄位：``svg``（原始 SVG）、``latex``（可為 None）、``source``、
    ``reject``（解碼被拒的原因）、``ocr_attempts``（OCR 已嘗試次數）。
    """

    root: Path

    def path(self, key: str) -> Path:
        return self.root / f"{key}.json"

    def has(self, key: str) -> bool:
        return self.path(key).exists()

    def load(self, key: str) -> dict:
        return json.loads(self.path(key).read_text(encoding="utf-8"))

    def save(self, key: str, data: dict) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        text = json.dumps(data, ensure_ascii=False, indent=1)
        self.path(key).write_text(text, encoding="utf-8")

    def keys(self) -> list[str]:
        if not self.root.exists():
            return []
        return sorted(p.stem for p in self.root.glob("*.json"))

    def results(self) -> dict[str, FormulaResult]:
        """所有已有 LaTeX 的公式。"""
        found: dict[str, FormulaResult] = {}
        for key in self.keys():
            data = self.load(key)
            if data.get("latex"):
                found[key] = FormulaResult(data["latex"], data["source"])
        return found

    def pending_ocr(self, max_attempts: int = 2) -> list[tuple[str, str]]:
        """尚無 LaTeX、且 OCR 嘗試次數未達上限的 ``(key, svg)``。"""
        pending: list[tuple[str, str]] = []
        for key in self.keys():
            data = self.load(key)
            if not data.get("latex") and data.get("ocr_attempts", 0) < max_attempts:
                pending.append((key, data["svg"]))
        return pending


@dataclass
class DecodeReport:
    """解碼統計。"""

    total: int = 0
    decoded: int = 0
    rejected: collections.Counter = field(default_factory=collections.Counter)
    keys: set[str] = field(default_factory=set)


def scan_and_decode(cache: PageCache, store: FormulaStore) -> DecodeReport:
    """掃描快取內所有公式，以字形解碼並存入 store。

    尚無 LaTeX 的舊公式也會重試解碼（字形對照表補齊後即可救回）。

    :param cache: 頁面快取。
    :param store: 公式結果快取。
    :return: 解碼統計（``rejected`` 依原因代碼分類）。
    """
    report = DecodeReport()
    seen: set[str] = set()
    for page in cache.pages():
        for lang in cache.langs:
            for svg, _display in collect_formula_svgs(cache.load_html(lang, page)):
                key = formula_key(svg)
                if key in seen:
                    continue
                seen.add(key)
                report.keys.add(key)
                report.total += 1
                data = store.load(key) if store.has(key) else _new_entry(svg)
                if data["latex"] is None:
                    try:
                        data.update(latex=decode_svg(svg), source="decode", reject=None)
                    except Reject as exc:
                        data["reject"] = str(exc)
                    store.save(key, data)
                if data["source"] == "decode":
                    report.decoded += 1
                elif data["latex"] is None:
                    report.rejected[data["reject"].split(":")[0]] += 1
    return report


def _new_entry(svg: str) -> dict:
    return {
        "svg": svg,
        "latex": None,
        "source": None,
        "reject": None,
        "ocr_attempts": 0,
    }
