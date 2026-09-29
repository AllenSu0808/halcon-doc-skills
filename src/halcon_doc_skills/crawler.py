"""網址正規化、範圍過濾與去重佇列。"""

from __future__ import annotations

from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit

from . import config


def normalize_url(href: str, base_url: str) -> str | None:
    """將連結轉成範圍內的絕對網址。

    :param href: 頁面上的原始 href。
    :param base_url: 該頁面本身的網址，用來解析相對連結。
    :return: 去除 fragment 與 query、scheme 統一後的網址；
        若不在文件範圍內或不是 .html 則回傳 None。
    """
    href = href.strip()
    if not href or href.lower().startswith(("javascript:", "mailto:", "tel:")):
        return None
    absolute, _ = urldefrag(urljoin(base_url, href))
    parts = urlsplit(absolute)
    if parts.scheme not in ("http", "https"):
        return None
    if parts.netloc != config.BASE_HOST:
        return None
    if not parts.path.startswith(config.SCOPE_PREFIX):
        return None
    if not parts.path.endswith(".html"):
        return None
    scheme = urlsplit(config.BASE_URL).scheme
    return urlunsplit((scheme, parts.netloc, parts.path, "", ""))


def page_name(url: str) -> str:
    """回傳範圍內網址相對於文件根目錄的路徑，如 ``abs_image.html``。"""
    return urlsplit(url).path[len(config.SCOPE_PREFIX) :]


def md_name(page: str) -> str:
    """將頁面路徑的副檔名由 .html 換成 .md。"""
    if page.endswith(".html"):
        return page[: -len(".html")] + ".md"
    return page + ".md"


class Frontier:
    """記錄已見過的網址，避免重複爬取，並可限制總數（試跑用）。"""

    def __init__(self, limit: int | None = None) -> None:
        self._seen: set[str] = set()
        self._limit = limit

    def add(self, url: str) -> bool:
        """加入網址。

        :return: 首次加入且未超過上限時為 True，否則為 False。
        """
        if url in self._seen:
            return False
        if self._limit is not None and len(self._seen) >= self._limit:
            return False
        self._seen.add(url)
        return True

    def __len__(self) -> int:
        return len(self._seen)
