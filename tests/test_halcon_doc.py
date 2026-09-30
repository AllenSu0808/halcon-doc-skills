"""skill 查詢腳本 halcon_doc.py 的測試。"""

import os
import subprocess
import sys
from pathlib import Path

import pytest

from halcon_doc_skills.skill_build import build_skill

from . import skill_scripts
from .md_fixtures import write_output

import halcon_doc  # noqa: E402  # isort: skip
import halcon_ref  # noqa: E402  # isort: skip


@pytest.fixture
def skill(tmp_path: Path) -> Path:
    """以樣本文件與實際範本產生的 skill 資料夾。"""
    dest = tmp_path / "skill"
    build_skill(write_output(tmp_path / "output"), skill_scripts.TEMPLATE, dest)
    return dest


def run(skill: Path, *argv: str, cwd: Path | None = None) -> str:
    return halcon_doc.run(list(argv), root=skill / "references", cwd=cwd or skill)


def test_key_normalizes_all_spellings() -> None:
    names = ["FindShapeModel", "find_shape_model", "HOperatorSet.FindShapeModel"]
    assert {halcon_ref.key(n) for n in names} == {"findshapemodel"}


def test_sig_lists_all_overloads_for_any_spelling(skill: Path) -> None:
    for name in ("find_shape_model", "HOperatorSet.FindShapeModel", "FindShapeModel"):
        out = run(skill, "--lang", "dotnet", "sig", name)
        assert out.splitlines()[0] == (
            "# find_shape_model — Find the best matches of a shape model in an image."
        )
        assert "static void HOperatorSet.FindShapeModel(" in out
        assert "void HImage.FindShapeModel(" in out
        assert str(skill / "references" / "dotnet" / "find_shape_model.md") in out


def test_sig_python_includes_s_variant(skill: Path) -> None:
    out = run(skill, "--lang", "python", "sig", "find_shape_model")
    assert "def find_shape_model(" in out and "def find_shape_model_s(" in out


def test_sig_unknown_suggests_close_names(skill: Path) -> None:
    with pytest.raises(halcon_ref.DocError, match="相近名稱：find_shape_model"):
        run(skill, "--lang", "hdevelop", "sig", "find_shap_model")


def test_search_ranks_name_hits_first(skill: Path) -> None:
    out = run(skill, "--lang", "hdevelop", "search", "shape", "model")
    assert out.splitlines() == [
        "find_shape_model — Find the best matches of a shape model in an image.",
        "create_shape_model — Prepare a shape model for matching.",
    ]
    with pytest.raises(halcon_ref.DocError, match="search 無結果"):
        run(skill, "--lang", "hdevelop", "search", "nothing_like_this")


def test_params_prints_only_requested_blocks(skill: Path) -> None:
    out = run(skill, "--lang", "hdevelop", "params", "FindShapeModel", "num_levels")
    assert out.startswith("**`NumLevels`** (input_control)")
    assert "List of values:\n0, 1, 2" in out and "SubPixel" not in out
    with pytest.raises(halcon_ref.DocError, match="沒有參數「Bogus」"):
        run(skill, "--lang", "hdevelop", "params", "find_shape_model", "Bogus")


def test_params_without_names_prints_whole_section(skill: Path) -> None:
    out = run(skill, "--lang", "python", "params", "find_shape_model")
    assert "**`image`**" in out and "**`column`**" in out


def test_section_matches_prefix_case_insensitive(skill: Path) -> None:
    out = run(skill, "--lang", "dotnet", "section", "find_shape_model", "possible succ")
    assert out == "## Possible Successors\n\n`clear_shape_model`"


def test_class_list_constructors_and_methods(skill: Path) -> None:
    out = run(skill, "--lang", "dotnet", "class", "HShapeModel")
    assert out.splitlines() == [
        "# HShapeModel — Represents an instance of a shape model for matching.",
        "",
        "## Constructors",
        "public HShapeModel(HImage template, string metric)",
        "",
        "## Methods",
        "FindShapeModel — Find the best matches of a shape model in an image.",
    ]
    with pytest.raises(halcon_ref.DocError, match="只適用於 dotnet"):
        run(skill, "--lang", "python", "class", "HShapeModel")


@pytest.mark.parametrize(
    ("marker", "lang"),
    [
        ("App.csproj", "dotnet"),
        ("pyproject.toml", "python"),
        ("src/main.hdev", "hdevelop"),
    ],
)
def test_detect_lang_from_project_files(tmp_path: Path, marker: str, lang: str) -> None:
    (tmp_path / marker).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / marker).write_text("", encoding="utf-8")
    assert halcon_ref.detect_lang(tmp_path) == lang


def test_detect_lang_ignores_deep_and_skipped_dirs(tmp_path: Path) -> None:
    (tmp_path / "a" / "b" / "c").mkdir(parents=True)
    (tmp_path / "a" / "b" / "c" / "deep.py").write_text("", encoding="utf-8")
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "x.py").write_text("", encoding="utf-8")
    (tmp_path / "App.csproj").write_text("", encoding="utf-8")
    assert halcon_ref.detect_lang(tmp_path) == "dotnet"


def test_detect_lang_ambiguous_or_empty_raises(tmp_path: Path) -> None:
    with pytest.raises(halcon_ref.DocError, match="找不到"):
        halcon_ref.detect_lang(tmp_path)
    (tmp_path / "App.csproj").write_text("", encoding="utf-8")
    (tmp_path / "tool.py").write_text("", encoding="utf-8")
    with pytest.raises(halcon_ref.DocError, match="dotnet、python"):
        halcon_ref.detect_lang(tmp_path)


def test_missing_language_reports_installed(skill: Path) -> None:
    import shutil

    shutil.rmtree(skill / "references" / "python")
    with pytest.raises(
        halcon_ref.DocError, match="python 文件未安裝（已安裝：hdevelop, dotnet）"
    ):
        run(skill, "--lang", "python", "sig", "find_shape_model")


def test_script_runs_standalone_from_built_skill(skill: Path, tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()
    (project / "App.csproj").write_text("", encoding="utf-8")
    script = skill / "scripts" / "halcon_doc.py"

    ok = subprocess.run(
        [sys.executable, str(script), "sig", "FindShapeModel"],
        cwd=project,
        capture_output=True,
        encoding="utf-8",
    )
    assert ok.returncode == 0, ok.stderr
    assert "HOperatorSet.FindShapeModel(" in ok.stdout

    missing = subprocess.run(
        [sys.executable, str(script), "sig", "NoSuchOperator"],
        cwd=project,
        capture_output=True,
        encoding="utf-8",
    )
    assert missing.returncode == 1 and missing.stderr.startswith("錯誤：查無")


def test_script_output_survives_non_utf8_console(skill: Path, tmp_path: Path) -> None:
    """Windows 主控台（cp950 等）不能讓中文與「—」輸出失敗。"""
    env = {**os.environ, "PYTHONIOENCODING": "ascii"}
    result = subprocess.run(
        [
            sys.executable,
            str(skill / "scripts" / "halcon_doc.py"),
            "--lang",
            "dotnet",
            "sig",
            "NoSuchOperator",
        ],
        cwd=tmp_path,
        capture_output=True,
        env=env,
    )
    assert result.returncode == 1
    assert result.stderr.decode("utf-8").startswith("錯誤：查無")
