"""圖片資產：行內 SVG 存檔與資產檔名規則。"""
from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from .formulas import FORMULA_RE, FormulaResult, formula_key, make_token

_SVG_RE = re.compile(r"<svg\b.*?</svg>", re.DOTALL | re.IGNORECASE)
_SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'
_XLINK_NS = 'xmlns:xlink="http://www.w3.org/1999/xlink"'


def _digest(data: str) -> str:
    """回傳字串 SHA-1 的前 16 碼，用作檔名。"""
    return hashlib.sha1(data.encode("utf-8")).hexdigest()[:16]


def normalize_svg(svg: str) -> str:
    """補上獨立 SVG 檔所需的命名空間宣告。

    行內 SVG 在 HTML 中可省略 ``xmlns``，但存成 .svg 檔時必須有。
    """
    head = svg[: svg.index(">")]
    additions: list[str] = []
    if "xmlns=" not in head:
        additions.append(_SVG_NS)
    if "xlink:" in svg and "xmlns:xlink=" not in head:
        additions.append(_XLINK_NS)
    if not additions:
        return svg
    return svg.replace("<svg", "<svg " + " ".join(additions), 1)


def svg_asset_name(svg: str) -> str:
    """SVG 內容對應的資產檔名（相同內容得到相同檔名）。"""
    return f"{_digest(svg)}.svg"


def image_asset_name(url: str) -> str:
    """圖片網址對應的資產檔名，保留原副檔名。"""
    suffix = PurePosixPath(urlsplit(url).path).suffix.lower() or ".bin"
    return f"{_digest(url)}{suffix}"


def extract_inline_svgs(
    html: str,
    assets_dir: Path,
    rel_prefix: str,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> str:
    """把 HTML 中的行內 SVG 存成檔案並替換。

    需在 HTML 解析器處理之前呼叫，避免解析器把 ``viewBox`` 轉成小寫。

    :param html: 含行內 SVG 的 HTML 字串。
    :param assets_dir: 資產輸出資料夾（相同檔名已存在時不覆寫）。
    :param rel_prefix: 從 Markdown 檔到資產資料夾的相對路徑，如 ``../assets``。
    :param formulas: 公式鍵 → LaTeX 結果；None 表示不做公式轉換。
    :return: 公式換成 ``@@FORMULA…@@`` 標記（有結果者），其餘 SVG 換成
        ``<img data-local="1">``。
    """

    def _write(svg: str) -> str:
        svg = normalize_svg(svg)
        name = svg_asset_name(svg)
        path = assets_dir / name
        if not path.exists():
            assets_dir.mkdir(parents=True, exist_ok=True)
            path.write_text(svg, encoding="utf-8")
        return name

    def _image(svg: str) -> str:
        name = _write(svg)
        return f'<img data-local="1" src="{rel_prefix}/{name}" alt="figure">'

    def _formula(match: re.Match[str]) -> str:
        svg = match.group("svg")
        key = formula_key(svg)
        result = formulas.get(key) if formulas else None
        if result is None:
            return _image(svg)
        asset = None if result.source == "decode" else _write(svg)
        return make_token(key, match.group("cls") == "displaymath", asset)

    html = FORMULA_RE.sub(_formula, html)
    return _SVG_RE.sub(lambda match: _image(match.group(0)), html)
