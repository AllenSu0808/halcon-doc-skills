"""crawl 與 convert_all 的測試。"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from halcon_doc_skills import config, ocr
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract
from halcon_doc_skills.formulas import FormulaStore, collect_formula_svgs
from halcon_doc_skills.ocr import OcrOptions
from halcon_doc_skills.pipeline import convert_all, crawl, resolve_formulas

FIXTURES = Path(__file__).parent / "fixtures"

ROOT = "https://www.mvtec.com/doc/halcon/2605/en/"
STUB = (
    "<p>Use the tabs on the upper right to switch to a different "
    "programming language.</p>"
)


def _save(cache: PageCache, page: str, html_by_lang: dict[str, str]) -> None:
    cache.save(
        page,
        PageExtract(
            url=ROOT + page,
            title=page,
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang=html_by_lang,
        ),
    )


def test_convert_all_skips_stub_pages_and_falls_back_to_absolute_links(
    tmp_path: Path,
) -> None:
    cache = PageCache(tmp_path / "cache")
    op = '<h1>op (Operator)</h1><p><a href="HThing.html">HThing</a></p>'
    _save(cache, "op.html", {"hdevelop": op, "dotnet": op, "python": op})
    _save(
        cache,
        "HThing.html",
        {
            "hdevelop": STUB,
            "dotnet": "<h1>HThing (Class)</h1>",
            "python": STUB,
        },
    )
    out = tmp_path / "output"
    report = convert_all(cache, out)

    assert report.converted == {"hdevelop": 1, "dotnet": 2, "python": 1}
    assert report.skipped_stubs == {"hdevelop": 1, "dotnet": 0, "python": 1}
    assert not (out / "hdevelop" / "HThing.md").exists()
    assert (out / "dotnet" / "HThing.md").exists()
    assert "[HThing](HThing.md)" in (out / "dotnet" / "op.md").read_text("utf-8")
    assert f"[HThing]({ROOT}HThing.html)" in (out / "python" / "op.md").read_text(
        "utf-8"
    )
    assert "HThing.md" not in (out / "python" / "INDEX.md").read_text("utf-8")
    assert "HThing.md" in (out / "dotnet" / "INDEX.md").read_text("utf-8")


@pytest.fixture
def mini_site(fixture_server: str, monkeypatch: pytest.MonkeyPatch) -> str:
    """將網址範圍指向本機迷你網站。"""
    monkeypatch.setattr(config, "BASE_HOST", fixture_server.removeprefix("http://"))
    monkeypatch.setattr(config, "SCOPE_PREFIX", "/mini/")
    monkeypatch.setattr(config, "BASE_URL", f"{fixture_server}/mini/")
    monkeypatch.setattr(config, "ENTRY_PAGES", ("index.html",))
    return fixture_server


@pytest.mark.browser
def test_crawl_follows_links_records_failures_and_converts(
    mini_site: str, tmp_path: Path
) -> None:
    cache = PageCache(tmp_path / "cache")
    out = tmp_path / "output"
    report = asyncio.run(
        crawl(cache, out, concurrency=2, retries=3, delay=0)
    )

    assert cache.pages() == ["HThing.html", "index.html", "op_one.html", "toc_a.html"]
    assert report.fetched == 4
    assert len(report.failed) == 1 and report.failed[0].endswith("/mini/missing.html")
    assert "missing.html" in cache.failed_path.read_text(encoding="utf-8")

    convert_all(cache, out)
    py = (out / "python" / "op_one.md").read_text(encoding="utf-8")
    net = (out / "dotnet" / "op_one.md").read_text(encoding="utf-8")
    assert "op_one_py" in py and "OpOne" not in py
    assert "OpOne" in net
    assert "op_one (A, B)" in py and "](#Param)" not in py
    assert f"[HThing]({mini_site}/mini/HThing.html)" in py
    assert f"[missing]({mini_site}/mini/missing.html)" in py
    assert "[HThing](HThing.md)" in net
    assert "![figure](../assets/" in py
    assert len(list((out / "assets").glob("*.svg"))) == 1
    assert not (out / "hdevelop" / "HThing.md").exists()
    assert not (out / "python" / "HThing.md").exists()
    assert "HThing (Class)" in (out / "dotnet" / "HThing.md").read_text("utf-8")
    index = (out / "python" / "INDEX.md").read_text(encoding="utf-8")
    assert "## Cat A" in index
    assert "[op_one_py](op_one.md) — Does one thing." in index


@pytest.mark.browser
def test_second_run_resumes_from_cache_and_keeps_traversing(
    mini_site: str, tmp_path: Path
) -> None:
    cache = PageCache(tmp_path / "cache")
    out = tmp_path / "output"
    asyncio.run(crawl(cache, out, concurrency=2, retries=1, delay=0))
    report = asyncio.run(crawl(cache, out, concurrency=2, retries=1, delay=0))

    assert report.fetched == 0
    assert report.skipped == 4
    assert len(report.failed) == 1  # missing.html 仍會被重新嘗試
    assert len(cache.pages()) == 4


@pytest.mark.browser
def test_limit_and_entries_override(mini_site: str, tmp_path: Path) -> None:
    cache = PageCache(tmp_path / "limit")
    asyncio.run(crawl(cache, tmp_path / "o1", limit=2, retries=1, delay=0))
    assert len(cache.pages()) == 2

    cache2 = PageCache(tmp_path / "entries")
    asyncio.run(
        crawl(
            cache2,
            tmp_path / "o2",
            entries=["op_one.html"],
            limit=1,
            retries=1,
            delay=0,
        )
    )
    assert cache2.pages() == ["op_one.html"]


def _formula_svgs() -> tuple[str, str]:
    """一個可字形解碼的公式與一個會被拒絕的公式（矩陣）。"""

    def first(page: str) -> str:
        html = (FIXTURES / f"{page}.html").read_text(encoding="utf-8")
        return collect_formula_svgs(html)[0][0]

    return first("threshold"), first("hom_mat2d_rotate")


def _formula_cache(tmp_path: Path) -> PageCache:
    good, bad = _formula_svgs()
    html = (
        "<h1>op (Operator)</h1>"
        f'<p><span title="1" class="displaymath"><!-- c -->{good}</span></p>'
        f'<p><span title="2" class="math"><!-- c -->{bad}</span></p>'
    )
    cache = PageCache(tmp_path / "cache")
    _save(cache, "op.html", {"hdevelop": html, "dotnet": html, "python": html})
    return cache


def test_resolve_formulas_reports_and_convert_all_writes_latex(tmp_path: Path) -> None:
    cache = _formula_cache(tmp_path)
    store = FormulaStore(tmp_path / "cache" / "latex")
    report = resolve_formulas(cache, store)

    assert (report.total, report.decoded, report.ocr, report.unresolved) == (2, 1, 0, 1)
    assert dict(report.rejected) == {"cmex": 1}

    out = tmp_path / "output"
    convert_all(cache, out, formulas=store.results())
    for lang in config.LANGS:
        md = (out / lang / "op.md").read_text(encoding="utf-8")
        assert r"$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$" in md
        assert md.count("![figure](../assets/") == 1  # 被拒的公式保留圖檔
        assert "@@FORMULA" not in md
    assert len(list((out / "assets").glob("*.svg"))) == 1


@pytest.mark.browser
def test_ocr_fallback_end_to_end_with_fake_site(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(ocr, "LATEXCONVERT_URL", f"{fixture_server}/ocr/index.html")
    cache = _formula_cache(tmp_path)
    store = FormulaStore(tmp_path / "cache" / "latex")
    report = resolve_formulas(cache, store, OcrOptions(delay=0, timeout_ms=10_000))

    assert (report.decoded, report.ocr, report.unresolved) == (1, 1, 0)
    out = tmp_path / "output"
    convert_all(cache, out, formulas=store.results())
    md = (out / "python" / "op.md").read_text(encoding="utf-8")
    assert r"$FAKE \alpha$ ![figure](../assets/" in md  # OCR 結果附原圖
