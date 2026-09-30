"""簽章與參數解析的測試。"""

from pathlib import Path

from halcon_doc_skills.signatures import (
    ParamRow,
    SignatureRow,
    clean,
    parse_page,
    split_values,
    write_tsv,
)

from .md_fixtures import DOTNET, HDEVELOP, PYTHON


def test_hdevelop_operator_signature_and_params() -> None:
    page = parse_page(
        HDEVELOP["find_shape_model.md"], "find_shape_model.md", "hdevelop"
    )
    assert page is not None and page.kind == "operator"
    assert [(s.name, s.kind, s.owner) for s in page.signatures] == [
        ("find_shape_model", "operator", "")
    ]
    assert page.signatures[0].summary == (
        "Find the best matches of a shape model in an image."
    )
    names = [p.param for p in page.params]
    assert names == ["Image", "ModelID", "SubPixel", "NumLevels", "Row", "Column"]
    sub_pixel = page.params[2]
    assert sub_pixel.direction == "input_control"
    assert sub_pixel.default == "'least_squares'"
    assert sub_pixel.list_of_values == ""
    assert (
        sub_pixel.suggested_values == "'none' | 'least_squares' | 'max_deformation 1'"
    )
    assert page.params[3].list_of_values == "0 | 1 | 2"


def test_dotnet_overloads_become_separate_rows() -> None:
    page = parse_page(
        DOTNET["create_shape_model.md"], "create_shape_model.md", "dotnet"
    )
    assert page is not None
    assert [(s.name, s.kind, s.owner) for s in page.signatures] == [
        ("CreateShapeModel", "operator", "HOperatorSet"),
        ("HShapeModel", "constructor", "HShapeModel"),
        ("CreateShapeModel", "method", "HImage"),
    ]
    assert page.params[1].list_of_values == '"ignore_global_polarity" | "use_polarity"'


def test_dotnet_param_type_strips_markdown_links() -> None:
    page = parse_page(DOTNET["find_shape_model.md"], "find_shape_model.md", "dotnet")
    assert page is not None
    assert page.params[1].type == "HShapeModel, HTuple (IntPtr)"


def test_python_signature_with_nbsp_and_s_variant() -> None:
    page = parse_page(PYTHON["find_shape_model.md"], "find_shape_model.md", "python")
    assert page is not None
    assert [s.name for s in page.signatures] == [
        "find_shape_model",
        "find_shape_model_s",
    ]
    assert " " not in page.signatures[0].signature
    assert page.signatures[0].signature.startswith(
        "def find_shape_model(image: HObject"
    )


def test_class_page_yields_single_class_row() -> None:
    page = parse_page(DOTNET["HShapeModel.md"], "HShapeModel.md", "dotnet")
    assert page is not None and page.kind == "class" and page.params == []
    assert page.signatures == [
        SignatureRow(
            "HShapeModel",
            "class",
            "",
            "",
            "Represents an instance of a shape model for matching.",
            "HShapeModel.md",
        )
    ]


def test_non_reference_pages_return_none() -> None:
    assert (
        parse_page("## Matching\n\nList of Operators ↓\n", "toc_m.md", "dotnet") is None
    )
    assert parse_page("# HALCON 26.05 Reference Index\n", "INDEX.md", "dotnet") is None


def test_operator_without_signature_has_empty_rows() -> None:
    md = "# broken (Operator)\n\n## Name\n\n`broken` — X.\n\n## Signature\n\nnone\n"
    page = parse_page(md, "broken.md", "hdevelop")
    assert page is not None and page.signatures == []


def test_split_values_keeps_quoted_commas_and_spaces() -> None:
    assert split_values("'a, b', 'max_deformation 1', 3") == (
        "'a, b' | 'max_deformation 1' | 3"
    )


def test_clean_collapses_whitespace() -> None:
    assert clean(" a\tb\n c d ") == "a b c d"


def test_write_tsv_has_header_and_one_line_per_row(tmp_path: Path) -> None:
    path = tmp_path / "PARAMS.tsv"
    rows = [ParamRow("p.md", "A", "input_control", "x\ty", "", "1 | 2", "")]
    write_tsv(path, rows, ParamRow)
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0].split("\t") == [
        "page",
        "param",
        "direction",
        "type",
        "default",
        "list_of_values",
        "suggested_values",
    ]
    assert lines[1].split("\t") == [
        "p.md",
        "A",
        "input_control",
        "x y",
        "",
        "1 | 2",
        "",
    ]
