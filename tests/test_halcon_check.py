"""skill 檢查腳本 halcon_check.py 的測試。"""

from pathlib import Path

import pytest

from halcon_doc_skills.skill_build import build_skill

from . import skill_scripts
from .md_fixtures import write_output

import halcon_check  # noqa: E402  # isort: skip
import halcon_ref  # noqa: E402  # isort: skip


@pytest.fixture
def refs(tmp_path: Path) -> Path:
    """樣本文件產生的 references/ 資料夾。"""
    dest = tmp_path / "skill"
    build_skill(write_output(tmp_path / "output"), skill_scripts.TEMPLATE, dest)
    return dest / "references"


def check(refs: Path, tmp_path: Path, name: str, code: str) -> list[str]:
    path = tmp_path / name
    path.write_text(code, encoding="utf-8")
    report = halcon_check.run_check([path], refs, None, tmp_path)
    return [line.replace(f"{path}:", "") for line in report.splitlines()]


def test_split_args_respects_nesting_and_strings() -> None:
    assert halcon_check.split_args('a, f(b, c), [1, 2], \'x, y\', "p,\\"q"') == [
        "a",
        "f(b, c)",
        "[1, 2]",
        "'x, y'",
        '"p,\\"q"',
    ]
    assert halcon_check.split_args("") == []
    assert halcon_check.split_args(" ") == []


def test_dotnet_correct_code_is_ok(refs: Path, tmp_path: Path) -> None:
    code = (
        'HOperatorSet.CreateShapeModel(ho_Image, "use_polarity", out hv_Model);\n'
        'HOperatorSet.FindShapeModel(ho_Image, hv_Model, "least_squares", 0,\n'
        "    out hv_Row, out hv_Column);\n"
        'model.FindShapeModel(img, "none", 0, out r, out c);\n'
    )
    assert check(refs, tmp_path, "A.cs", code) == ["OK: 2 HALCON calls checked"]


def test_dotnet_reports_each_problem(refs: Path, tmp_path: Path) -> None:
    code = (
        "HOperatorSet.FindShapeMdl(ho_Image);\n"
        'HOperatorSet.FindShapeModel(ho_Image, hv_Model, "none", out r, out c);\n'
        'HOperatorSet.CreateShapeModel(ho_Image, "use_polarty", out m);\n'
    )
    lines = check(refs, tmp_path, "A.cs", code)
    assert lines[0].startswith("1: [unknown-operator] HOperatorSet.FindShapeMdl 不存在")
    assert "FindShapeModel" in lines[0]
    assert lines[1] == (
        "2: [arg-count] HOperatorSet.FindShapeModel 需要 6 個參數，實際 5 個"
        " → 執行 sig FindShapeModel"
    )
    assert lines[2] == (
        '3: [invalid-value] HOperatorSet.CreateShapeModel 參數 metric="use_polarty"'
        " 不在合法值內 → ignore_global_polarity, use_polarity"
    )
    assert lines[3] == "3 warning(s) in 3 HALCON calls"


def test_python_alias_kwargs_and_helpers(refs: Path, tmp_path: Path) -> None:
    code = (
        "import halcon as ha\n"
        "m = ha.create_shape_model(img, metric='use_polarity')\n"
        "r, c = ha.find_shape_model(img, m, 'least_squares', 0)\n"
        "r, c = ha.find_shape_model_s(img, m, sub_pixel='none', num_levels=0)\n"
        "arr = ha.himage_as_numpy_array(img)\n"
    )
    assert check(refs, tmp_path, "a.py", code) == ["OK: 3 HALCON calls checked"]


def test_python_reports_count_and_value(refs: Path, tmp_path: Path) -> None:
    code = (
        "import halcon\n"
        "halcon.find_shape_model(img, m, 'none')\n"
        "halcon.create_shape_model(img, metric='bogus')\n"
        "halcon.no_such_op()\n"
    )
    lines = check(refs, tmp_path, "a.py", code)
    assert lines[0].startswith(
        "2: [arg-count] find_shape_model 需要 4 個參數，實際 3 個"
    )
    assert lines[1].startswith(
        "3: [invalid-value] create_shape_model 參數 metric='bogus'"
    )
    assert lines[2].startswith("4: [unknown-operator] no_such_op 不存在")


def test_python_without_halcon_import_has_no_calls(refs: Path, tmp_path: Path) -> None:
    assert check(refs, tmp_path, "a.py", "ha.find_shape_model(1)\n") == [
        "OK: 0 HALCON calls checked"
    ]


def test_hdevelop_xml_skips_keywords_procedures_and_comments(
    refs: Path, tmp_path: Path
) -> None:
    code = (
        '<hdevelop><procedure name="main"><body>\n'
        "<l>create_shape_model (Image, 'use_polarity', ModelID)</l>\n"
        "<l>find_shape_model (Image, ModelID, 'none', 0, Row, Column)</l>\n"
        "<l>if (|Row| &gt; 0)</l>\n"
        "<l>    my_proc (Image)</l>\n"
        "<l>endif</l>\n"
        "<c>* bogus_op (X)</c>\n"
        '</body></procedure><procedure name="my_proc"></procedure></hdevelop>\n'
    )
    assert check(refs, tmp_path, "main.hdev", code) == ["OK: 2 HALCON calls checked"]


def test_hdevelop_reports_count_value_and_unknown(refs: Path, tmp_path: Path) -> None:
    code = (
        "find_shape_model (Image, ModelID, 'none', 0, Row)\n"
        "create_shape_model (Image, 'use_polarty', ModelID)\n"
        "my_helper (Image)\n"
    )
    lines = check(refs, tmp_path, "main.hdev", code)
    assert lines[0].startswith(
        "1: [arg-count] find_shape_model 需要 6 個參數，實際 5 個"
    )
    assert lines[1].startswith(
        "2: [invalid-value] create_shape_model 參數 Metric='use_polarty'"
    )
    assert lines[2].startswith("3: [unknown-operator] my_helper 不存在")
    assert lines[2].endswith("（若為自訂 procedure 可忽略）")


def test_lang_from_extension_overrides_project(refs: Path, tmp_path: Path) -> None:
    (tmp_path / "App.csproj").write_text("", encoding="utf-8")
    code = "import halcon as ha\nha.create_shape_model(img, 'use_polarity')\n"
    assert check(refs, tmp_path, "tool.py", code) == ["OK: 1 HALCON calls checked"]


def test_unreadable_file_does_not_stop_others(refs: Path, tmp_path: Path) -> None:
    good = tmp_path / "a.cs"
    good.write_text("HOperatorSet.FindShapeMdl(x);\n", encoding="utf-8")
    report = halcon_check.run_check(
        [tmp_path / "missing.cs", good], refs, None, tmp_path
    ).splitlines()
    assert report[0].startswith(f"{tmp_path / 'missing.cs'}: [read-error]")
    assert report[1].startswith(f"{good}:1: [unknown-operator]")
    assert report[2] == "1 warning(s) in 1 HALCON calls"


def test_unknown_extension_without_project_raises(refs: Path, tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()
    path = project / "code.txt"
    path.write_text("x\n", encoding="utf-8")
    with pytest.raises(halcon_ref.DocError, match="無法判斷語言"):
        halcon_check.run_check([path], refs, None, project)
