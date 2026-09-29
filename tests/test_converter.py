"""HTML → Markdown 轉換的測試（不需瀏覽器）。"""

from pathlib import Path

from halcon_doc_skills.assets import image_asset_name, normalize_svg, svg_asset_name
from halcon_doc_skills.converter import convert_page, is_stub_page
from halcon_doc_skills.formulas import FormulaResult, formula_key

ROOT = "https://www.mvtec.com/doc/halcon/2605/en/"
PAGE_URL = ROOT + "abs_image.html"


def _convert(
    html: str,
    tmp_path: Path,
    available: set[str] | None = None,
    page_url: str = PAGE_URL,
    lang: str = "python",
) -> str:
    return convert_page(html, page_url, lang, available or set(), tmp_path / "assets")


def test_headings_and_inline_code(tmp_path: Path) -> None:
    html = (
        "<h1>abs_image (Operator)</h1><h2>Name</h2>"
        "<p><code>abs_image</code> — Calculate the absolute value.</p>"
    )
    md = _convert(html, tmp_path)
    assert md.startswith("# abs_image (Operator)\n")
    assert "## Name" in md
    assert "`abs_image` — Calculate the absolute value." in md
    assert md.endswith("\n") and not md.endswith("\n\n")


def test_underscores_are_not_escaped(tmp_path: Path) -> None:
    md = _convert("<p>use abs_image and get_value</p>", tmp_path)
    assert "abs_image and get_value" in md


def test_pre_becomes_fenced_code(tmp_path: Path) -> None:
    md = _convert('<pre class="example">\nfoo (A, B)\nbar (B)\n</pre>', tmp_path)
    assert "```" in md
    assert "foo (A, B)\nbar (B)" in md


def test_table_becomes_pipe_table(tmp_path: Path) -> None:
    html = (
        "<table><tr><td><code>ReadBarCodeModel</code></td><td>Read a model."
        "</td></tr><tr><td><code>Other</code></td><td>Other.</td></tr></table>"
    )
    md = _convert(html, tmp_path)
    assert "|" in md and "ReadBarCodeModel" in md


def test_dl_becomes_bullet_list(tmp_path: Path) -> None:
    html = (
        '<dl><dt><a href="add_image.html"><code>add_image</code></a></dt>'
        "<dd>Add two images.</dd></dl>"
    )
    md = _convert(html, tmp_path, available={"add_image.html"})
    assert "- [`add_image`](add_image.md) — Add two images." in md


def test_noise_is_removed(tmp_path: Path) -> None:
    html = (
        "<!--OP_REF_HEADER_END--><script>var a=1;</script><style>p{}</style><p>Hi</p>"
    )
    md = _convert(html, tmp_path)
    assert md == "Hi\n"


def test_link_to_available_page_becomes_relative_md(tmp_path: Path) -> None:
    md = _convert('<a href="HImage.html#x">HImage</a>', tmp_path, {"HImage.html"})
    assert "[HImage](HImage.md)" in md


def test_link_to_unavailable_page_keeps_absolute_url(tmp_path: Path) -> None:
    md = _convert('<a href="HImage.html">HImage</a>', tmp_path, set())
    assert f"[HImage]({ROOT}HImage.html)" in md


def test_external_and_out_of_scope_links_are_absolute(tmp_path: Path) -> None:
    html = (
        '<a href="https://example.org/x">e</a> '
        '<a href="../../../../documentation.html">d</a>'
    )
    md = _convert(html, tmp_path)
    assert "[e](https://example.org/x)" in md
    assert "[d](https://www.mvtec.com/documentation.html)" in md


def test_anchor_javascript_and_self_links_are_unwrapped(tmp_path: Path) -> None:
    html = (
        '<a href="#Image"><i>Image</i></a> '
        '<a href="javascript:void(0);">js</a> '
        '<a href="abs_image.html#top">self</a> <a name="x">named</a>'
    )
    md = _convert(html, tmp_path, {"abs_image.html"})
    assert "](" not in md
    assert "Image" in md and "js" in md and "self" in md and "named" in md


def test_subdirectory_page_uses_relative_paths(tmp_path: Path) -> None:
    html = '<a href="../y.html">y</a> <svg viewBox="0 0 1 1"></svg>'
    md = _convert(html, tmp_path, {"y.html"}, page_url=ROOT + "sub/x.html")
    assert "[y](../y.md)" in md
    assert "![figure](../../assets/" in md


def test_inline_svg_becomes_image_with_asset_file(tmp_path: Path) -> None:
    html = (
        '<p>f <span title="1" class="displaymath">'
        '<svg viewBox="0 0 10 5"><path d="M0 0"/></svg></span></p>'
    )
    md = _convert(html, tmp_path)
    assert "![figure](../assets/" in md and ".svg)" in md
    files = list((tmp_path / "assets").glob("*.svg"))
    assert len(files) == 1
    text = files[0].read_text(encoding="utf-8")
    assert "viewBox" in text and 'xmlns="http://www.w3.org/2000/svg"' in text
    assert "data-local" not in md


def test_downloaded_image_uses_local_asset(tmp_path: Path) -> None:
    url = ROOT + "pic.png"
    assets = tmp_path / "assets"
    assets.mkdir()
    name = image_asset_name(url)
    (assets / name).write_bytes(b"png")
    md = _convert('<img src="pic.png" alt="A pic">', tmp_path)
    assert f"![A pic](../assets/{name})" in md


def test_missing_image_keeps_absolute_url(tmp_path: Path) -> None:
    md = _convert('<img src="pic.png" alt="A pic">', tmp_path)
    assert f"![A pic]({ROOT}pic.png)" in md


def test_images_survive_inside_headings_and_table_cells(tmp_path: Path) -> None:
    svg = '<svg viewBox="0 0 1 1"><path d="M0 0"/></svg>'
    md = _convert(
        f"<h2>Title {svg}</h2><table><tr><td>{svg}</td></tr></table>", tmp_path
    )
    assert md.count("![figure](../assets/") == 2


FORMULA_SVG = '<svg viewBox="0 0 1 1"><path d="M0 0"/></svg>'


def _formula_html() -> str:
    return (
        f'<p>if <span title="1" class="math">{FORMULA_SVG}</span> then '
        f'<span title="2" class="displaymath">{FORMULA_SVG}</span></p>'
    )


def test_decoded_formulas_become_latex_and_are_not_escaped(tmp_path: Path) -> None:
    latex = r"a_{i}\le b*[c]"
    formulas = {formula_key(FORMULA_SVG): FormulaResult(latex, "decode")}
    md = convert_page(
        _formula_html(), PAGE_URL, "python", set(), tmp_path / "assets", formulas
    )
    assert md == "if $a_{i}\\le b*[c]$ then $$a_{i}\\le b*[c]$$\n"
    assert not (tmp_path / "assets").exists()


def test_ocr_formula_gets_latex_and_original_image(tmp_path: Path) -> None:
    formulas = {formula_key(FORMULA_SVG): FormulaResult("x", "ocr")}
    html = f'<p><span title="1" class="math">{FORMULA_SVG}</span></p>'
    md = convert_page(html, PAGE_URL, "python", set(), tmp_path / "assets", formulas)
    name = svg_asset_name(normalize_svg(FORMULA_SVG))
    assert md == f"$x$ ![figure](../assets/{name})\n"
    assert (tmp_path / "assets" / name).exists()


def test_unresolved_formula_stays_an_image(tmp_path: Path) -> None:
    md = convert_page(
        _formula_html(), PAGE_URL, "python", set(), tmp_path / "assets", {}
    )
    assert md.count("![figure](../assets/") == 2 and "$" not in md


def test_is_stub_page() -> None:
    stub = (
        "<!--c--><p>Use the tabs on the upper right to switch to a\n"
        "different programming language.</p>"
    )
    assert is_stub_page(stub) is True
    assert is_stub_page(stub + "<h1>Real</h1>") is False
    assert is_stub_page("") is False
