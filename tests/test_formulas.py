"""formulas：字形解碼、公式標記與快取的測試。"""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills import formulas
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract, extract_page
from halcon_doc_skills.formulas import (
    FormulaResult,
    FormulaStore,
    Reject,
    collect_formula_svgs,
    decode_svg,
    formula_key,
    make_token,
    render_tokens,
    scan_and_decode,
)

FIXTURES = Path(__file__).parent / "fixtures"
KEY = "0123456789abcdef"


def _svgs(page: str) -> list[str]:
    """取出樣本頁面內所有公式的 SVG。"""
    html = (FIXTURES / f"{page}.html").read_text(encoding="utf-8")
    return [svg for svg, _ in collect_formula_svgs(html)]


def _svg(*groups, extra: str = "") -> str:
    """合成公式 SVG。groups：``(tx, ty, [(字型, 字碼, x 偏移或 None), ...])``。"""
    parts = ["<svg><defs></defs>"]
    for tx, ty, uses in groups:
        parts.append(f'<g transform="matrix(1.6,0,0,1.6,{tx},{ty})">')
        for font, code, x in uses:
            attr = f' x="{x}"' if x is not None else ""
            parts.append(f'<use xlink:href="#GLYPH{font}_{code}"{attr}></use>')
        parts.append("</g>")
    parts.append(f"{extra}</svg>")
    return "".join(parts)


def _reason(svg: str) -> str:
    with pytest.raises(Reject) as info:
        decode_svg(svg)
    return str(info.value)


# ── 真實公式 ─────────────────────────────────────────────


@pytest.mark.parametrize(
    "page, index, expected",
    [
        ("threshold", 0, r"\texttt{MinGray}\le g\le\texttt{MaxGray}."),
        (
            "dyn_threshold",
            2,
            r"g_{t}-\texttt{Offset}\le g_{o}\le g_{t}+\texttt{Offset}",
        ),
        ("determinant_matrix", 0, r"\texttt{Value}=\det \texttt{Matrix}."),
        ("affine_trans_image", 2, r"B_{max}=0.5\cdot S\cdot I/2^{15}"),
        ("create_dl_layer_affine_grid", 2, r"(x^{\prime},y^{\prime})"),
        (
            "harmonic_interpolation",
            1,
            r"u_{xx}(x,y)=u(x-1,y)-2u(x,y)+u(x+1,y)",
        ),
        ("set_lut", 0, r"g\_min"),
        ("find_shape_model_3d", 1, r"(\infty)"),
    ],
)
def test_real_formulas_decode(page: str, index: int, expected: str) -> None:
    assert decode_svg(_svgs(page)[index]) == expected


@pytest.mark.parametrize(
    "page, index, reason",
    [
        ("hom_mat2d_rotate", 0, "cmex"),
        ("create_dl_layer_lrn", 2, "rule"),
        ("cooc_feature_image", 0, "multi-baseline"),
        ("gray_erosion", 0, "code:cmsy10_9"),
    ],
)
def test_real_formulas_are_rejected(page: str, index: int, reason: str) -> None:
    assert _reason(_svgs(page)[index]) == reason


# ── 合成公式：上下標、字型、串接 ─────────────────────────


def test_subscript_superscript_and_both() -> None:
    x = (0, 10, [("cmmi10", 120, None)])
    assert decode_svg(_svg(x, (10, 12, [("cmmi7", 105, None)]))) == "x_{i}"
    assert decode_svg(_svg(x, (10, 8, [("cmmi7", 105, None)]))) == "x^{i}"
    both = _svg(x, (10, 12, [("cmmi7", 105, None)]), (10, 8, [("cmmi7", 106, None)]))
    assert decode_svg(both) == "x_{i}^{j}"


def test_font_kinds_and_spacing() -> None:
    tt = _svg((0, 10, [("pcrr8r", 65, None), ("pcrr8r", 66, 6.0)]))
    assert decode_svg(tt) == r"\texttt{AB}"
    words = _svg((0, 10, [("ptmr8r", 97, None)]), (10, 10, [("ptmr8r", 98, None)]))
    assert decode_svg(words) == r"\text{a b}"
    rm = _svg(
        (0, 10, [("cmr10", 52, None)]),
        (10, 10, [("cmr10", 115, None), ("cmr10", 105, 3.0), ("cmr10", 110, 6.0)]),
    )
    assert decode_svg(rm) == r"4\sin"
    assert decode_svg(_svg((0, 10, [("cmmi10", 25, None)]))) == r"\pi"


def test_command_followed_by_letter_gets_a_space() -> None:
    gamma, x = (0, 10, [("cmmi10", 13, None)]), (10, 10, [("cmmi10", 120, None)])
    assert decode_svg(_svg(gamma, x)) == r"\gamma x"  # 不能變成 \gammax
    le = (10, 10, [("cmsy10", 20, None)])
    assert decode_svg(_svg(gamma, le, (20, 10, [("cmmi10", 120, None)]))) == (
        r"\gamma\le x"
    )


# ── 拒絕條件（寧可拒絕也不猜測）─────────────────────────


def test_reject_reasons() -> None:
    x = (0, 10, [("cmmi10", 120, None)])
    assert _reason(_svg(x, (0, 30, [("cmmi10", 121, None)]))) == "multi-baseline"
    assert _reason(_svg(x, extra='<path d="M0 0"/>')) == "rule"
    assert _reason(_svg((0, 10, [("cmex10", 50, None)]))) == "cmex"
    assert _reason(_svg((0, 10, [("cmr10", 200, None)]))) == "code:cmr10_200"
    assert _reason(_svg((0, 10, [("foo12", 65, None)]))) == "font:foo12"
    assert _reason(_svg(x, (10, 12, [("cmmi5", 105, None)]))) == "nested-script"
    assert _reason(_svg((0, 10, [("cmmi7", 105, None)]), (10, 10, x[2]))) == (
        "script-first"
    )
    assert _reason("<svg><defs></defs></svg>") == "empty"
    assert _reason("<svg></svg>") == "no-defs"


def test_unparsed_use_is_rejected_instead_of_dropping_glyphs() -> None:
    svg = _svg((0, 10, [("cmr10", 65, None)])).replace(
        "</g>", '<use xlink:href="#weird"></use></g>'
    )
    assert _reason(svg) == "unparsed-use"


# ── 公式容器、鍵、標記 ───────────────────────────────────


def test_collect_formula_svgs_reports_display_flag_and_ignores_other_svgs() -> None:
    html = (
        '<p><span title="1" class="math"><!-- c --><svg id="a"><defs></defs></svg>'
        '</span><span title="2" class="displaymath"><svg id="b"></svg></span>'
        '<a><svg id="logo"></svg></a></p>'
    )
    found = collect_formula_svgs(html)
    assert [display for _, display in found] == [False, True]
    assert 'id="logo"' not in "".join(svg for svg, _ in found)


def test_formula_key_is_stable_16_hex() -> None:
    assert formula_key("<svg/>") == formula_key("<svg/>")
    assert len(formula_key("<svg/>")) == 16 and formula_key("a") != formula_key("b")


def test_make_token_and_render_tokens() -> None:
    assert make_token(KEY, True, None) == f"@@FORMULA:{KEY}:d:-@@"
    assert make_token(KEY, False, "a.svg") == f"@@FORMULA:{KEY}:i:a.svg@@"

    results = {KEY: FormulaResult(r"a_{i}\le b*c", "decode")}
    md = f"if {make_token(KEY, False, None)} then\n\n{make_token(KEY, True, None)}\n"
    assert render_tokens(md, results, "../assets") == (
        "if $a_{i}\\le b*c$ then\n\n$$a_{i}\\le b*c$$\n"
    )


def test_render_tokens_ocr_appends_image_and_collapses_whitespace() -> None:
    results = {KEY: FormulaResult("a\n   b", "ocr")}
    md = make_token(KEY, False, "x.svg")
    assert render_tokens(md, results, "../assets") == "$a b$ ![figure](../assets/x.svg)"


def test_render_tokens_leaves_unknown_tokens_visible() -> None:
    token = make_token(KEY, False, None)
    assert render_tokens(token, {}, "../assets") == token


# ── 快取與掃描 ───────────────────────────────────────────


def test_store_results_and_pending_ocr(tmp_path: Path) -> None:
    store = FormulaStore(tmp_path / "latex")
    a, b, c = "a" * 16, "b" * 16, "c" * 16
    base = {"latex": None, "source": None, "reject": "cmex"}
    store.save(
        a,
        {
            "svg": "<svg/>",
            "latex": "x",
            "source": "decode",
            "reject": None,
            "ocr_attempts": 0,
        },
    )
    store.save(b, {**base, "svg": "<svg>b</svg>", "ocr_attempts": 0})
    store.save(c, {**base, "svg": "<svg>c</svg>", "ocr_attempts": 2})
    assert store.keys() == [a, b, c]
    assert store.results() == {a: FormulaResult("x", "decode")}
    assert store.pending_ocr() == [(b, "<svg>b</svg>")]


def _cache_with(tmp_path: Path, html: str) -> PageCache:
    cache = PageCache(tmp_path / "cache")
    cache.save(
        "p.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/p.html",
            title="p",
            breadcrumb=[],
            links=[],
            image_urls=[],
            html_by_lang={lang: html for lang in cache.langs},
        ),
    )
    return cache


def _wrap(svg: str, cls: str = "displaymath") -> str:
    return f'<p><span title="1" class="{cls}"><!-- c -->{svg}</span></p>'


def test_scan_and_decode_stores_results_and_is_idempotent(tmp_path: Path) -> None:
    good, bad = _svgs("threshold")[0], _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(good) + _wrap(bad))
    store = FormulaStore(tmp_path / "latex")

    report = scan_and_decode(cache, store)
    assert (report.total, report.decoded) == (2, 1)
    assert dict(report.rejected) == {"cmex": 1}
    assert report.keys == {formula_key(good), formula_key(bad)}
    assert store.results()[formula_key(good)] == FormulaResult(
        r"\texttt{MinGray}\le g\le\texttt{MaxGray}.", "decode"
    )
    assert [key for key, _ in store.pending_ocr()] == [formula_key(bad)]

    again = scan_and_decode(cache, store)
    assert (again.total, again.decoded) == (2, 1)
    assert len(store.keys()) == 2


def test_previously_rejected_formulas_are_retried(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    bad = _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(bad))
    store = FormulaStore(tmp_path / "latex")
    scan_and_decode(cache, store)
    assert store.results() == {}

    monkeypatch.setattr(formulas, "decode_svg", lambda svg: "X")  # 模擬對照表補齊
    report = scan_and_decode(cache, store)
    assert report.decoded == 1
    assert store.results()[formula_key(bad)] == FormulaResult("X", "decode")


def test_ocr_results_are_not_overwritten(tmp_path: Path) -> None:
    bad = _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(bad))
    store = FormulaStore(tmp_path / "latex")
    scan_and_decode(cache, store)
    key = formula_key(bad)
    data = store.load(key)
    data.update(latex="Y", source="ocr")
    store.save(key, data)

    report = scan_and_decode(cache, store)
    assert report.decoded == 0
    assert store.results()[key] == FormulaResult("Y", "ocr")


# ── 經過瀏覽器序列化後仍可解碼 ───────────────────────────


@pytest.mark.browser
def test_decode_survives_browser_serialization(fixture_server: str) -> None:
    async def go() -> PageExtract:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                return await extract_page(page, f"{fixture_server}/en/threshold.html")
            finally:
                await browser.close()

    result = asyncio.run(go())
    found = collect_formula_svgs(result.html_by_lang["hdevelop"])
    assert len(found) == 1
    assert decode_svg(found[0][0]) == r"\texttt{MinGray}\le g\le\texttt{MaxGray}."
