"""URL 正規化、範圍過濾與去重的測試。"""
from halcon_doc_skills.crawler import Frontier, md_name, normalize_url, page_name

BASE = "https://www.mvtec.com/doc/halcon/2605/en/index.html"
PREFIX = "https://www.mvtec.com/doc/halcon/2605/en/"


def test_relative_link_is_resolved() -> None:
    assert normalize_url("toc_1dmeasuring.html", BASE) == PREFIX + "toc_1dmeasuring.html"


def test_fragment_and_query_are_removed() -> None:
    assert normalize_url("abs_image.html#Image", BASE) == PREFIX + "abs_image.html"
    assert normalize_url("abs_image.html?interface=python", BASE) == (
        PREFIX + "abs_image.html"
    )


def test_http_scheme_is_upgraded_to_base_scheme() -> None:
    url = "http://www.mvtec.com/doc/halcon/2605/en/abs_image.html"
    assert normalize_url(url, BASE) == PREFIX + "abs_image.html"


def test_out_of_scope_links_are_rejected() -> None:
    assert normalize_url("../../../../documentation.html", BASE) is None
    assert normalize_url("http://www.mvtec.com/", BASE) is None
    assert normalize_url("https://www.linkedin.com/company/x", BASE) is None
    assert normalize_url("https://www.mvtec.com/doc/halcon/2505/en/x.html", BASE) is None


def test_non_html_and_pseudo_links_are_rejected() -> None:
    assert normalize_url("javascript:void(0);", BASE) is None
    assert normalize_url("mailto:a@b.c", BASE) is None
    assert normalize_url("style.css", BASE) is None
    assert normalize_url("", BASE) is None


def test_page_name_and_md_name() -> None:
    assert page_name(PREFIX + "abs_image.html") == "abs_image.html"
    assert page_name(PREFIX + "sub/x.html") == "sub/x.html"
    assert md_name("abs_image.html") == "abs_image.md"
    assert md_name("sub/x.html") == "sub/x.md"


def test_frontier_deduplicates() -> None:
    frontier = Frontier()
    assert frontier.add("a") is True
    assert frontier.add("a") is False
    assert len(frontier) == 1


def test_frontier_respects_limit() -> None:
    frontier = Frontier(limit=2)
    assert frontier.add("a") is True
    assert frontier.add("b") is True
    assert frontier.add("c") is False
    assert len(frontier) == 2
