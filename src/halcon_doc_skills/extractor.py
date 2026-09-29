"""以 Playwright 取出各語言的可見頁面內容。"""

from __future__ import annotations

import logging
from collections.abc import Sequence
from dataclasses import dataclass

from playwright.async_api import Page

from . import config

log = logging.getLogger(__name__)

# 頁尾標記：其後是 <hr>、版權與社群圖示，不屬於內容
FOOTER_MARKER = "<!--OP_REF_FOOTER_START-->"

_TAB_SELECTOR = "#syn-{lang} a"

# 在頁面內執行：把目前隱藏的 data-if 元素標記後複製 .body_main，
# 從複本移除標記元素、script、分頁列、索引連結與頁尾
_VISIBLE_JS = r"""
() => {
  const marked = [];
  for (const el of document.querySelectorAll('[data-if]')) {
    if (getComputedStyle(el).display === 'none') {
      el.setAttribute('data-hh-hidden', '1');
      marked.push(el);
    }
  }
  const root = document.querySelector('.body_main') || document.body;
  const clone = root.cloneNode(true);
  for (const el of marked) el.removeAttribute('data-hh-hidden');
  const drop = '[data-hh-hidden], script, .tabbar, .indexlink, .footer';
  for (const el of clone.querySelectorAll(drop)) el.remove();
  const clean = (s) => s.replace(/\s+/g, ' ').trim();
  return {
    html: clone.innerHTML,
    images: [...clone.querySelectorAll('img[src]')].map((i) => i.src),
    links: [...document.querySelectorAll('a[href]')].map((a) => a.href),
    breadcrumb: [...document.querySelectorAll('.breadcrumb a')]
      .map((a) => [clean(a.textContent), a.href])
      .filter(([text]) => text !== ''),
    title: document.title,
  };
}
"""


class PageFetchError(Exception):
    """頁面載入失敗或不是 HALCON 文件頁。"""

    def __init__(self, message: str, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status

    @property
    def retryable(self) -> bool:
        """網路錯誤、5xx 與 429 值得重試；其他（如 404）不重試。"""
        return self.status is None or self.status >= 500 or self.status == 429


@dataclass
class PageExtract:
    """單一頁面的擷取結果。"""

    url: str
    title: str
    breadcrumb: list[tuple[str, str]]
    links: list[str]
    image_urls: list[str]
    html_by_lang: dict[str, str]


async def extract_page(
    page: Page,
    url: str,
    langs: Sequence[str] = config.LANGS,
    timeout_ms: int = 60_000,
) -> PageExtract:
    """載入頁面一次，逐語言點擊分頁並取出可見內容。

    :param page: Playwright 分頁。
    :param url: 要擷取的頁面網址。
    :param langs: 要擷取的語言（對應 ``#syn-<lang>`` 分頁）。
    :param timeout_ms: 載入與點擊的逾時毫秒數。
    :return: 各語言的可見 HTML 與頁面中繼資料。
    :raises PageFetchError: 回應非 200，或頁面不是 HALCON 文件頁。
    """
    response = await page.goto(url, wait_until="load", timeout=timeout_ms)
    status = response.status if response is not None else None
    if status != 200:
        raise PageFetchError(f"{url} 回應狀態 {status}", status=status)
    if await page.locator("#syn-hdevelop").count() == 0:
        raise PageFetchError(f"{url} 不是 HALCON 文件頁", status=200)

    html_by_lang: dict[str, str] = {}
    links: dict[str, None] = {}
    images: dict[str, None] = {}
    title = ""
    breadcrumb: list[tuple[str, str]] = []
    for lang in langs:
        await page.click(_TAB_SELECTOR.format(lang=lang), timeout=timeout_ms)
        data = await page.evaluate(_VISIBLE_JS)
        html_by_lang[lang] = data["html"].partition(FOOTER_MARKER)[0]
        links.update(dict.fromkeys(data["links"]))
        images.update(dict.fromkeys(data["images"]))
        title = data["title"]
        breadcrumb = [(text, href) for text, href in data["breadcrumb"]]
    log.debug("擷取完成：%s", url)
    return PageExtract(
        url=url,
        title=title,
        breadcrumb=breadcrumb,
        links=list(links),
        image_urls=list(images),
        html_by_lang=html_by_lang,
    )
