"""skill 資料夾產生的測試。"""

from pathlib import Path

import pytest

from halcon_doc_skills.cli import main
from halcon_doc_skills.skill_build import build_skill

from .md_fixtures import write_output


def _template(root: Path) -> Path:
    template = root / "template"
    (template / "scripts").mkdir(parents=True)
    (template / "SKILL.md").write_text("---\nname: halcon\n---\n", encoding="utf-8")
    (template / "scripts" / "halcon_doc.py").write_text("", encoding="utf-8")
    (template / "scripts" / "__pycache__").mkdir()
    return template


def test_build_copies_template_pages_and_writes_tsv(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output")
    dest = tmp_path / "dist" / "halcon"

    report = build_skill(output, _template(tmp_path), dest)

    assert report.ok
    assert (dest / "SKILL.md").is_file() and (
        dest / "scripts" / "halcon_doc.py"
    ).is_file()
    assert not (dest / "scripts" / "__pycache__").exists()
    for lang in ("hdevelop", "dotnet", "python"):
        refs = dest / "references" / lang
        assert (refs / "INDEX.md").is_file() and (
            refs / "find_shape_model.md"
        ).is_file()
        assert (
            (refs / "SIGNATURES.tsv")
            .read_text(encoding="utf-8")
            .startswith("name\tkind\towner\tsignature\tsummary\tpage\n")
        )
        assert (
            (refs / "PARAMS.tsv")
            .read_text(encoding="utf-8")
            .startswith("page\tparam\t")
        )
    dotnet = report.stats["dotnet"]
    assert (dotnet.operators, dotnet.classes, dotnet.signatures) == (2, 1, 7)
    assert report.stats["hdevelop"].params == 9


def test_build_replaces_nbsp_in_copied_pages(tmp_path: Path) -> None:
    dest = tmp_path / "dist"
    build_skill(write_output(tmp_path / "output"), _template(tmp_path), dest)
    text = (dest / "references" / "python" / "find_shape_model.md").read_text(
        encoding="utf-8"
    )
    assert " " not in text and "`def find_shape_model(image: HObject" in text


def test_build_skips_missing_language(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output", langs=("dotnet",))
    report = build_skill(output, _template(tmp_path), tmp_path / "dist")
    assert list(report.stats) == ["dotnet"] and report.ok
    assert not (tmp_path / "dist" / "references" / "python").exists()


def test_build_without_any_language_is_not_ok(tmp_path: Path) -> None:
    (tmp_path / "output").mkdir()
    report = build_skill(tmp_path / "output", _template(tmp_path), tmp_path / "dist")
    assert report.stats == {} and not report.ok


def test_failure_rate_over_one_percent_is_not_ok(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output", langs=("hdevelop",))
    (output / "hdevelop" / "broken.md").write_text(
        "# broken (Operator)\n\n## Name\n\n`broken` — X.\n\n## Signature\n\nnone\n",
        encoding="utf-8",
    )
    report = build_skill(output, _template(tmp_path), tmp_path / "dist")
    stats = report.stats["hdevelop"]
    assert stats.failed == ["broken.md"] and stats.failure_rate == pytest.approx(1 / 3)
    assert not report.ok


def test_rebuild_replaces_previous_skill(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output")
    template = _template(tmp_path)
    dest = tmp_path / "dist"
    build_skill(output, template, dest)
    (dest / "stale.txt").write_text("old", encoding="utf-8")
    build_skill(output, template, dest)
    assert not (dest / "stale.txt").exists()


def test_refuses_to_overwrite_unrelated_folder(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output")
    with pytest.raises(FileExistsError):
        build_skill(output, _template(tmp_path), output)
    assert (output / "dotnet" / "find_shape_model.md").is_file()


def test_cli_build_skill_exit_codes(tmp_path: Path) -> None:
    output = write_output(tmp_path / "output")
    template = _template(tmp_path)
    args = ["build-skill", "--output", str(output), "--template", str(template)]
    assert main([*args, "--out", str(tmp_path / "dist")]) == 0
    assert main([*args, "--out", str(output)]) == 1
    (tmp_path / "empty").mkdir()
    empty = [
        "build-skill",
        "--output",
        str(tmp_path / "empty"),
        "--template",
        str(template),
    ]
    assert main([*empty, "--out", str(tmp_path / "dist2")]) == 1
