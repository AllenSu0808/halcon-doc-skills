"""PageCache 讀寫與完整性判斷的測試。"""

from pathlib import Path

from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract, PageFetchError


def _extract() -> PageExtract:
    return PageExtract(
        url="https://www.mvtec.com/doc/halcon/2605/en/abs_image.html",
        title="abs_image",
        breadcrumb=[("HALCON 26.05", "https://x/"), ("Filters", "https://x/f")],
        links=["https://www.mvtec.com/doc/halcon/2605/en/add_image.html"],
        image_urls=[],
        html_by_lang={
            "hdevelop": "<p>hd</p>",
            "dotnet": "<p>net</p>",
            "python": "<p>py</p>",
        },
    )


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    cache.save("abs_image.html", _extract())
    assert cache.load_html("python", "abs_image.html") == "<p>py</p>"
    meta = cache.load_meta("abs_image.html")
    assert meta["title"] == "abs_image"
    assert meta["breadcrumb"][1] == ["Filters", "https://x/f"]
    assert meta["links"] == ["https://www.mvtec.com/doc/halcon/2605/en/add_image.html"]


def test_is_complete_requires_meta_and_all_languages(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    assert cache.is_complete("abs_image.html") is False
    cache.save("abs_image.html", _extract())
    assert cache.is_complete("abs_image.html") is True
    cache.html_path("dotnet", "abs_image.html").unlink()
    assert cache.is_complete("abs_image.html") is False


def test_pages_lists_sorted_names_including_subdirs(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    for name in ("b.html", "a.html", "sub/c.html"):
        cache.save(name, _extract())
    assert cache.pages() == ["a.html", "b.html", "sub/c.html"]


def test_record_failure_appends_lines(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    cache.record_failure("https://x/a.html", "HTTP 404")
    cache.record_failure("https://x/b.html", "timeout")
    lines = cache.failed_path.read_text(encoding="utf-8").splitlines()
    assert lines == ["https://x/a.html\tHTTP 404", "https://x/b.html\ttimeout"]


def test_page_fetch_error_retryable_rules() -> None:
    assert PageFetchError("x", status=None).retryable is True
    assert PageFetchError("x", status=503).retryable is True
    assert PageFetchError("x", status=429).retryable is True
    assert PageFetchError("x", status=404).retryable is False
    assert PageFetchError("x", status=200).retryable is False
