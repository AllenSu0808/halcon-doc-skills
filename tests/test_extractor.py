"""extract_page 的整合測試（需要 Playwright Chromium）。"""
from __future__ import annotations

import asyncio

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills.extractor import PageExtract, PageFetchError, extract_page

pytestmark = pytest.mark.browser


def _extract(url: str) -> PageExtract:
    async def go() -> PageExtract:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                return await extract_page(page, url)
            finally:
                await browser.close()

    return asyncio.run(go())


def test_each_language_keeps_only_its_own_content(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    hd = result.html_by_lang["hdevelop"]
    net = result.html_by_lang["dotnet"]
    py = result.html_by_lang["python"]

    assert "(Operator)" in hd and "AbsImage" not in hd
    assert "<b>abs_image</b>(" in hd
    assert "HOperatorSet" in net and "AbsImage" in net
    # 只有 Python 的簽名帶型別註記（原頁面以 &nbsp; 分隔 def 與函式名稱）
    assert "-&gt; HObject" not in hd and "-&gt; HObject" not in net
    assert "-&gt; HObject" in py and "HOperatorSet" not in py
    # 其他語言（含永遠隱藏的 cpp / c）的標記元素都不應殘留
    for lang, html in result.html_by_lang.items():
        for other in ("hdevelop", "dotnet", "python", "cpp", "c"):
            if other != lang:
                assert f'data-if="{other}"' not in html


def test_chrome_around_content_is_removed(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    for html in result.html_by_lang.values():
        assert 'class="tabbar"' not in html
        assert 'class="indexlink"' not in html
        assert "Copyright" not in html
        assert "OP_REF_FOOTER_START" not in html
        assert "<script" not in html


def test_metadata_title_breadcrumb_and_links(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    assert "abs_image" in result.title
    assert result.breadcrumb[0][0].startswith("HALCON")  # 不含 logo 連結
    assert result.breadcrumb[-1][0] == "Arithmetic"
    assert all(href.startswith("http") for _, href in result.breadcrumb)
    # 只出現在 .NET 分頁的連結也要收集到
    assert any(link.endswith("/HImage.html") for link in result.links)


def test_inline_svg_keeps_viewbox_case(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/threshold.html")
    hd = result.html_by_lang["hdevelop"]
    assert "<svg" in hd and "viewBox" in hd


def test_class_page_is_stub_except_dotnet(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/HBarCode.html")
    assert "Use the tabs on the upper right" in result.html_by_lang["hdevelop"]
    assert "Use the tabs on the upper right" in result.html_by_lang["python"]
    assert "HBarCode (Class)" in result.html_by_lang["dotnet"]


def test_missing_page_raises_non_retryable_error(fixture_server: str) -> None:
    with pytest.raises(PageFetchError) as info:
        _extract(f"{fixture_server}/en/no_such_page.html")
    assert info.value.status == 404
    assert info.value.retryable is False


def test_non_doc_page_raises(fixture_server: str) -> None:
    with pytest.raises(PageFetchError) as info:
        _extract(f"{fixture_server}/mini/plain.html")
    assert info.value.retryable is False
