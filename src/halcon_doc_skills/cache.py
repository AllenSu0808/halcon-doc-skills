"""爬取結果的本機快取：各語言可見 HTML 與頁面中繼資料。"""

from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path

from . import config
from .extractor import PageExtract


class PageCache:
    """管理 ``html/<lang>/<page>``、``meta/<page>.json`` 與 ``failed.txt``。"""

    def __init__(self, root: Path, langs: Sequence[str] = config.LANGS) -> None:
        self.root = Path(root)
        self.langs = tuple(langs)

    def html_path(self, lang: str, page: str) -> Path:
        """某語言可見 HTML 的快取路徑。"""
        return self.root / "html" / lang / page

    def meta_path(self, page: str) -> Path:
        """頁面中繼資料 JSON 的路徑。"""
        return self.root / "meta" / f"{page}.json"

    @property
    def failed_path(self) -> Path:
        """失敗網址清單的路徑。"""
        return self.root / "failed.txt"

    def is_complete(self, page: str) -> bool:
        """中繼資料與所有語言的 HTML 都存在才視為完成。"""
        if not self.meta_path(page).exists():
            return False
        return all(self.html_path(lang, page).exists() for lang in self.langs)

    def save(self, page: str, extract: PageExtract) -> None:
        """寫入各語言 HTML，最後才寫中繼資料（中斷時不會被誤判為完成）。"""
        for lang in self.langs:
            path = self.html_path(lang, page)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(extract.html_by_lang[lang], encoding="utf-8")
        meta = {
            "url": extract.url,
            "title": extract.title,
            "breadcrumb": [list(item) for item in extract.breadcrumb],
            "links": extract.links,
            "image_urls": extract.image_urls,
        }
        meta_path = self.meta_path(page)
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8"
        )

    def load_meta(self, page: str) -> dict:
        """讀取頁面中繼資料。"""
        text = self.meta_path(page).read_text(encoding="utf-8")
        return json.loads(text)

    def load_html(self, lang: str, page: str) -> str:
        """讀取某語言的可見 HTML。"""
        return self.html_path(lang, page).read_text(encoding="utf-8")

    def pages(self) -> list[str]:
        """列出所有已有中繼資料的頁面（排序後）。"""
        meta_root = self.root / "meta"
        if not meta_root.exists():
            return []
        names = [
            path.relative_to(meta_root).as_posix()[: -len(".json")]
            for path in meta_root.rglob("*.json")
        ]
        return sorted(names)

    def record_failure(self, url: str, reason: str) -> None:
        """附加一筆失敗紀錄。"""
        self.root.mkdir(parents=True, exist_ok=True)
        with self.failed_path.open("a", encoding="utf-8") as fp:
            fp.write(f"{url}\t{reason}\n")
