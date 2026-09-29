"""圖片資產處理的測試。"""
from pathlib import Path

from halcon_doc_skills.assets import (
    extract_inline_svgs,
    image_asset_name,
    normalize_svg,
    svg_asset_name,
)
from halcon_doc_skills.formulas import FormulaResult, formula_key, make_token

SVG = '<svg viewBox="0 0 10 5" width="2em"><path d="M0 0L10 5"/></svg>'


def test_normalize_svg_adds_namespace() -> None:
    result = normalize_svg(SVG)
    assert 'xmlns="http://www.w3.org/2000/svg"' in result
    assert 'viewBox="0 0 10 5"' in result


def test_normalize_svg_keeps_existing_namespace_and_adds_xlink() -> None:
    svg = '<svg xmlns="http://www.w3.org/2000/svg"><use xlink:href="#a"/></svg>'
    result = normalize_svg(svg)
    assert result.count('xmlns="http://www.w3.org/2000/svg"') == 1
    assert 'xmlns:xlink="http://www.w3.org/1999/xlink"' in result


def test_asset_names_are_deterministic() -> None:
    assert svg_asset_name(SVG) == svg_asset_name(SVG)
    assert svg_asset_name(SVG).endswith(".svg")
    assert image_asset_name("https://x/a/pic.PNG?v=1") == image_asset_name(
        "https://x/a/pic.PNG?v=1"
    )
    assert image_asset_name("https://x/a/pic.PNG?v=1").endswith(".png")
    assert image_asset_name("https://x/a/noext").endswith(".bin")


def test_extract_inline_svgs_writes_file_and_replaces_tag(tmp_path: Path) -> None:
    html = f"<p>a {SVG} b</p>"
    result = extract_inline_svgs(html, tmp_path / "assets", "../assets")
    name = svg_asset_name(normalize_svg(SVG))
    assert f'<img data-local="1" src="../assets/{name}" alt="figure">' in result
    assert "<svg" not in result
    saved = (tmp_path / "assets" / name).read_text(encoding="utf-8")
    assert 'viewBox="0 0 10 5"' in saved
    assert 'xmlns="http://www.w3.org/2000/svg"' in saved


def test_identical_svgs_are_deduplicated(tmp_path: Path) -> None:
    html = f"<p>{SVG}</p><p>{SVG}</p>"
    extract_inline_svgs(html, tmp_path / "assets", "../assets")
    assert len(list((tmp_path / "assets").iterdir())) == 1


def _formula_html(svg: str, cls: str = "displaymath") -> str:
    return f'<p><span title="1" class="{cls}"><!-- c -->{svg}</span></p>'


def test_decoded_formula_becomes_token_without_asset(tmp_path: Path) -> None:
    key = formula_key(SVG)
    result = extract_inline_svgs(
        _formula_html(SVG),
        tmp_path / "assets",
        "../assets",
        {key: FormulaResult("x", "decode")},
    )
    assert result == f"<p>{make_token(key, True, None)}</p>"
    assert not (tmp_path / "assets").exists()


def test_ocr_formula_keeps_asset_and_marks_inline(tmp_path: Path) -> None:
    key = formula_key(SVG)
    result = extract_inline_svgs(
        _formula_html(SVG, "math"),
        tmp_path / "assets",
        "../assets",
        {key: FormulaResult("x", "ocr")},
    )
    name = svg_asset_name(normalize_svg(SVG))
    assert result == f"<p>{make_token(key, False, name)}</p>"
    assert (tmp_path / "assets" / name).exists()


def test_unresolved_formula_falls_back_to_image(tmp_path: Path) -> None:
    result = extract_inline_svgs(
        _formula_html(SVG), tmp_path / "assets", "../assets", {}
    )
    assert '<img data-local="1"' in result and "<span" not in result
    assert len(list((tmp_path / "assets").iterdir())) == 1


def test_non_formula_svg_is_still_an_image_when_formulas_given(
    tmp_path: Path,
) -> None:
    formulas = {formula_key(SVG): FormulaResult("x", "decode")}
    result = extract_inline_svgs(
        f'<a href="x">{SVG}</a>', tmp_path / "assets", "../assets", formulas
    )
    assert '<img data-local="1"' in result and "@@FORMULA" not in result


def test_multiline_svg_and_no_svg(tmp_path: Path) -> None:
    multi = '<svg viewBox="0 0 1 1">\n<g>\n</g>\n</svg>'
    result = extract_inline_svgs(multi, tmp_path / "assets", "../assets")
    assert result.startswith("<img")
    assert extract_inline_svgs("<p>none</p>", tmp_path / "a2", "..") == "<p>none</p>"
    assert not (tmp_path / "a2").exists()
