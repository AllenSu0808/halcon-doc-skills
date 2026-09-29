"""ocr 備援的測試：一律使用本機假網站，不連線 latexconvert.com。"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills import ocr
from halcon_doc_skills.assets import normalize_svg
from halcon_doc_skills.formulas import FormulaStore, collect_formula_svgs, formula_key
from halcon_doc_skills.ocr import OcrOptions, ocr_pending

pytestmark = pytest.mark.browser

FIXTURES = Path(__file__).parent / "fixtures"


def _base_svg() -> str:
    html = (FIXTURES / "threshold.html").read_text(encoding="utf-8")
    return collect_formula_svgs(html)[0][0]


def _store(tmp_path: Path, count: int) -> tuple[FormulaStore, list[str]]:
    """建立 count 個「解碼被拒、等待 OCR」的公式（SVG 各不相同）。"""
    store = FormulaStore(tmp_path / "latex")
    keys = []
    for i in range(count):
        svg = _base_svg().replace("<svg", f'<svg data-n="{i}"', 1)
        key = formula_key(svg)
        keys.append(key)
        store.save(
            key,
            {"svg": svg, "latex": None, "source": None, "reject": "cmex",
             "ocr_attempts": 0},
        )
    return store, sorted(keys)


def _use(monkeypatch: pytest.MonkeyPatch, base: str, page: str) -> None:
    monkeypatch.setattr(ocr, "LATEXCONVERT_URL", f"{base}/ocr/{page}")


def test_render_png_writes_a_png(tmp_path: Path) -> None:
    png = tmp_path / "f.png"

    async def go() -> None:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                await ocr.render_png(page, normalize_svg(_base_svg()), png)
            finally:
                await browser.close()

    asyncio.run(go())
    assert png.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_ocr_reads_result_from_fake_site(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "index.html")
    store, keys = _store(tmp_path, 2)
    report = asyncio.run(ocr_pending(store, OcrOptions(delay=0, timeout_ms=10_000)))

    assert (report.done, report.failed) == (2, 0)
    result = store.results()[keys[0]]
    assert (result.latex, result.source) == (r"FAKE \alpha", "ocr")
    assert store.load(keys[0])["ocr_attempts"] == 1
    assert store.pending_ocr() == []


def test_max_count_limits_processing(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "index.html")
    store, _ = _store(tmp_path, 3)
    report = asyncio.run(
        ocr_pending(store, OcrOptions(delay=0, max_count=1, timeout_ms=10_000))
    )
    assert report.done == 1
    assert len(store.pending_ocr()) == 2


def test_stops_after_three_consecutive_failures(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "fail.html")
    store, keys = _store(tmp_path, 5)
    report = asyncio.run(ocr_pending(store, OcrOptions(delay=0, timeout_ms=1_500)))

    assert (report.done, report.failed) == (0, 3)
    attempts = [store.load(key)["ocr_attempts"] for key in keys]
    assert attempts == [1, 1, 1, 0, 0]
    assert all(store.load(key).get("ocr_error") for key in keys[:3])


def test_each_formula_is_attempted_at_most_twice(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "fail.html")
    store, keys = _store(tmp_path, 1)
    options = OcrOptions(delay=0, timeout_ms=1_000)
    for expected in (1, 2, 2):
        asyncio.run(ocr_pending(store, options))
        assert store.load(keys[0])["ocr_attempts"] == expected
    assert store.pending_ocr() == []
