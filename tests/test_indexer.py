"""索引產生的測試。"""

from halcon_doc_skills.indexer import (
    IndexEntry,
    build_index,
    category_from_breadcrumb,
    read_title_and_summary,
)


def test_operator_title_and_summary() -> None:
    md = (
        "# abs_image (Operator)\n\n## Name\n\n"
        "`abs_image` — Calculate the absolute value.\n"
    )
    assert read_title_and_summary(md, "abs_image.html") == (
        "abs_image",
        "Calculate the absolute value.",
    )


def test_class_title_strips_suffix() -> None:
    md = "# HBarCode (Class)\n\n## Name\n\n`HBarCode` — Reads bar codes.\n"
    assert read_title_and_summary(md, "HBarCode.html") == (
        "HBarCode",
        "Reads bar codes.",
    )


def test_toc_page_uses_first_heading_and_no_summary() -> None:
    assert read_title_and_summary("## Arithmetic\n\ntext\n", "toc_a.html") == (
        "Arithmetic",
        "",
    )


def test_title_falls_back_to_page_stem() -> None:
    assert read_title_and_summary("just text\n", "sub/abs_image.html") == (
        "abs_image",
        "",
    )


def test_category_from_breadcrumb() -> None:
    crumbs = [
        ("HALCON 26.05.0.0", "u"),
        ("HALCON Operator Reference", "u"),
        ("Filters", "u"),
        ("Arithmetic", "u"),
    ]
    assert category_from_breadcrumb(crumbs) == "Filters / Arithmetic"
    assert category_from_breadcrumb(crumbs[:2]) == "Other"
    assert category_from_breadcrumb([]) == "Other"


def test_build_index_groups_sorts_and_links() -> None:
    entries = [
        IndexEntry("b_op.html", "b_op", "Second.", "Filters / Arithmetic"),
        IndexEntry("a_op.html", "a_op", "First.", "Filters / Arithmetic"),
        IndexEntry("toc_filters.html", "Filters", "", "Other"),
        IndexEntry("HThing.html", "HThing", "", "Other"),
    ]
    text = build_index("python", entries)
    assert text.startswith("# HALCON 26.05 Reference Index (python)\n")
    assert text.index("## Table of Contents") < text.index("## Filters / Arithmetic")
    assert "- [Filters](toc_filters.md)" in text
    assert "- [a_op](a_op.md) — First." in text
    assert text.index("a_op.md") < text.index("b_op.md")
    assert "## Other" in text and "- [HThing](HThing.md)" in text
    assert text.endswith("\n")
