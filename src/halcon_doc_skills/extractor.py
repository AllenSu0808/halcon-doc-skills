"""以 Playwright 取出各語言的可見頁面內容。"""
from __future__ import annotations

from dataclasses import dataclass


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
