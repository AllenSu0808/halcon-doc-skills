"""verify_output 的測試。"""

from pathlib import Path

from halcon_doc_skills.verify import verify_output


def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _good_tree(root: Path) -> None:
    _write(root, "assets/a.svg", "<svg/>")
    for lang in ("hdevelop", "dotnet", "python"):
        _write(root, f"{lang}/INDEX.md", "# Index\n\n- [a](a.md)\n")
        _write(
            root,
            f"{lang}/a.md",
            "# a\n\n[b](b.md) ![figure](../assets/a.svg) [x](https://e.org/)\n",
        )
        _write(root, f"{lang}/b.md", "# b\n")


def test_good_tree_has_no_problems_and_reports_counts(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    report = verify_output(tmp_path)
    assert report.ok
    assert report.counts == {"hdevelop": 2, "dotnet": 2, "python": 2}


def test_missing_language_folder_or_index_is_reported(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    (tmp_path / "python" / "INDEX.md").unlink()
    report = verify_output(tmp_path)
    assert any("INDEX.md" in p and "python" in p for p in report.problems)


def test_broken_link_and_image_are_reported(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    _write(tmp_path, "python/c.md", "[gone](gone.md) ![figure](../assets/no.svg)\n")
    problems = verify_output(tmp_path).problems
    assert any("gone.md" in p for p in problems)
    assert any("no.svg" in p for p in problems)


def test_repeated_word_is_reported(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    _write(tmp_path, "python/d.md", "# abs_imageabs_image (Operator)\n")
    assert any("重複" in p for p in verify_output(tmp_path).problems)


def test_unbalanced_dollar_and_leftover_token_are_reported(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    _write(tmp_path, "python/f.md", "cost $5 and $$x$$\n")
    _write(tmp_path, "python/g.md", "@@FORMULA:0123456789abcdef:d:-@@\n")
    problems = verify_output(tmp_path).problems
    assert any("f.md" in p and "$" in p for p in problems)
    assert any("g.md" in p and "FORMULA" in p for p in problems)


def test_balanced_formulas_and_escaped_dollar_are_ok(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    _write(tmp_path, "python/h.md", "$a_{i}$ and $$b$$ and costs \\$5\n")
    assert verify_output(tmp_path).ok


def test_fenced_code_and_external_links_are_ignored(tmp_path: Path) -> None:
    _good_tree(tmp_path)
    _write(
        tmp_path,
        "python/e.md",
        "```\nx[1](2) gaussgauss\n```\n[m](mailto:a@b.c) [t](#top)\n",
    )
    assert verify_output(tmp_path).ok
