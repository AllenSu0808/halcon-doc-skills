"""命令列介面的測試。"""

from pathlib import Path

import pytest

from halcon_doc_skills import cli, config
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.cli import build_parser, main
from halcon_doc_skills.extractor import PageExtract
from halcon_doc_skills.formulas import collect_formula_svgs
from halcon_doc_skills.ocr import OcrOptions
from halcon_doc_skills.pipeline import FormulaReport

FIXTURES = Path(__file__).parent / "fixtures"


def test_parser_defaults_and_overrides() -> None:
    args = build_parser().parse_args(["crawl"])
    assert args.cache_dir == Path("cache") and args.output == Path("output")
    assert args.concurrency == config.DEFAULT_CONCURRENCY
    assert args.limit is None and args.entries is None and args.force is False
    assert args.ocr_fallback is False and args.ocr_delay == 5.0 and args.ocr_max == 500

    args = build_parser().parse_args(
        ["crawl", "--limit", "5", "--entry", "a.html", "--entry", "b.html", "--force"]
    )
    assert args.limit == 5 and args.entries == ["a.html", "b.html"]
    assert args.force is True


def test_convert_then_verify(tmp_path: Path) -> None:
    cache = PageCache(tmp_path / "cache")
    html = "<h1>op (Operator)</h1><h2>Name</h2><p><code>op</code> — Does it.</p>"
    cache.save(
        "op.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/op.html",
            title="op",
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang={"hdevelop": html, "dotnet": html, "python": html},
        ),
    )
    out = tmp_path / "output"
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(out)]
    assert main(["convert", *argv]) == 0
    assert (out / "python" / "op.md").exists()
    assert main(["verify", "--output", str(out)]) == 0

    (out / "python" / "op.md").write_text("[gone](gone.md)\n", encoding="utf-8")
    assert main(["verify", "--output", str(out)]) == 1


def test_convert_writes_latex_for_decodable_formulas(tmp_path: Path) -> None:
    page = (FIXTURES / "threshold.html").read_text(encoding="utf-8")
    svg = collect_formula_svgs(page)[0][0]
    html = (
        "<h1>op (Operator)</h1>"
        f'<p><span title="1" class="displaymath"><!-- c -->{svg}</span></p>'
    )
    cache = PageCache(tmp_path / "cache")
    cache.save(
        "op.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/op.html",
            title="op",
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang={"hdevelop": html, "dotnet": html, "python": html},
        ),
    )
    out = tmp_path / "output"
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(out)]
    assert main(["convert", *argv]) == 0
    md = (out / "python" / "op.md").read_text(encoding="utf-8")
    assert r"$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$" in md
    assert (tmp_path / "cache" / "latex").is_dir()
    assert main(["verify", "--output", str(out)]) == 0


def test_ocr_options_are_wired(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    captured: list[OcrOptions | None] = []

    def fake_resolve(cache, store, ocr_options=None) -> FormulaReport:
        captured.append(ocr_options)
        return FormulaReport()

    monkeypatch.setattr(cli, "resolve_formulas", fake_resolve)
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(tmp_path / "out")]
    assert main(["convert", *argv]) == 0
    ocr_argv = ["--ocr-fallback", "--ocr-delay", "7", "--ocr-max", "3"]
    assert main(["convert", *argv, *ocr_argv]) == 0
    assert captured == [None, OcrOptions(delay=7.0, max_count=3)]
