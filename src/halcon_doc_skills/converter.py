"""將單一語言的可見 HTML 轉成 Markdown。"""
from __future__ import annotations

import posixpath
import re
from collections.abc import Collection, Mapping
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify

from . import config
from .assets import extract_inline_svgs, image_asset_name
from .crawler import md_name, normalize_url, page_name
from .formulas import FormulaResult, render_tokens

_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

# markdownify 預設會把標題、表格儲存格內的圖片降級成 alt 文字，這裡明確保留
_IMAGE_PARENTS = ["a", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "li", "p"]


def convert_page(
    html: str,
    page_url: str,
    lang: str,
    available: Collection[str],
    assets_dir: Path,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> str:
    """將可見 HTML 轉成 Markdown。

    :param html: 某語言的可見內容 HTML（來自 ``PageCache``）。
    :param page_url: 該頁面的原站網址，用來解析相對連結。
    :param lang: 語言資料夾名稱，用來計算資產相對路徑。
    :param available: 該語言有輸出 .md 的頁面名稱集合。
    :param assets_dir: 共用資產資料夾（SVG 會寫入此處）。
    :param formulas: 公式鍵 → LaTeX 結果；None 表示不做公式轉換。
    :return: 結尾為單一換行的 Markdown 字串。
    """
    page = page_name(page_url)
    rel_assets = posixpath.relpath(
        "assets", posixpath.join(lang, posixpath.dirname(page))
    )
    html = extract_inline_svgs(html, assets_dir, rel_assets, formulas)
    soup = BeautifulSoup(html, "html.parser")
    _strip_noise(soup)
    _rewrite_images(soup, page_url, rel_assets, assets_dir)
    _rewrite_links(soup, page_url, page, available)
    _dl_to_list(soup)
    text = markdownify(
        str(soup),
        heading_style="ATX",
        bullets="-",
        escape_underscores=False,
        escape_asterisks=False,
        keep_inline_images_in=_IMAGE_PARENTS,
    )
    # 公式在 markdownify 之後才換回 LaTeX，避免 _、\\、*、[ 被跳脫
    text = render_tokens(text, formulas or {}, rel_assets)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def is_stub_page(html: str) -> bool:
    """判斷是否為只有「請切換語言」提示的空殼頁。"""
    soup = BeautifulSoup(_COMMENT_RE.sub("", html), "html.parser")
    return " ".join(soup.get_text().split()) == config.STUB_MARKER


def _strip_noise(soup: BeautifulSoup) -> None:
    """移除註解、script 與 style。"""
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()


def _rewrite_images(
    soup: BeautifulSoup, page_url: str, rel_assets: str, assets_dir: Path
) -> None:
    """已下載的圖片改指向本機資產，否則保留原站絕對網址。"""
    for img in soup.find_all("img"):
        if img.has_attr("data-local"):
            del img["data-local"]
            continue
        src = img.get("src")
        if not src:
            img.decompose()
            continue
        absolute = urljoin(page_url, src)
        name = image_asset_name(absolute)
        local = (assets_dir / name).exists()
        img["src"] = f"{rel_assets}/{name}" if local else absolute


def _rewrite_links(
    soup: BeautifulSoup, page_url: str, page: str, available: Collection[str]
) -> None:
    """改寫連結：本機可用 → 相對 .md；其餘 → 完整網址；頁內錨點 → 純文字。"""
    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if href is None:
            anchor.unwrap()
            continue
        href = href.strip()
        if href.startswith("#") or href.lower().startswith("javascript:"):
            anchor.unwrap()
            continue
        target = normalize_url(href, page_url)
        if target is None:
            anchor["href"] = urljoin(page_url, href)
            continue
        name = page_name(target)
        if name == page:
            anchor.unwrap()
        elif name in available:
            start = posixpath.dirname(page) or "."
            anchor["href"] = posixpath.relpath(md_name(name), start=start)
        else:
            anchor["href"] = target


def _dl_to_list(soup: BeautifulSoup) -> None:
    """將 ``<dl><dt/><dd/></dl>`` 轉成 ``<ul><li>dt — dd</li></ul>``。"""
    for dl in soup.find_all("dl"):
        bullets = soup.new_tag("ul")
        current = None
        for child in list(dl.children):
            name = getattr(child, "name", None)
            if name == "dt":
                current = soup.new_tag("li")
                current.extend(list(child.contents))
                bullets.append(current)
            elif name == "dd":
                if current is None:
                    current = soup.new_tag("li")
                    bullets.append(current)
                else:
                    current.append(" — ")
                current.extend(list(child.contents))
        dl.replace_with(bullets)
