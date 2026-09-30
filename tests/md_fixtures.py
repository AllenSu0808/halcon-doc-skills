"""skill 相關測試共用的 Markdown 樣本（格式取自實際 output/，內容精簡）。"""

from __future__ import annotations

from pathlib import Path

NBSP = " "


def _param(name: str, direction: str, semantic: str, type_: str, *attrs: str) -> str:
    head = f"**`{name}`** ({direction})  {semantic} `→` {type_}\n\nDescription.\n"
    return head + "".join(f"\n{a}\n" for a in attrs)


def _operator(title: str, summary: str, signatures: list[str], params: str) -> str:
    sigs = "\n\n".join(f"`{s}`" for s in signatures)
    return (
        f"# {title} (Operator)\n\n## Name\n\n`{title}` — {summary}\n\n"
        f"## Signature\n\n{sigs}\n\n## Description\n\nText.\n\n"
        f"## Parameters\n\n{params}\n## Possible Successors\n\n`clear_shape_model`\n\n"
        "## Module\n\nMatching\n"
    )


_FIND = "Find the best matches of a shape model in an image."
_CREATE = "Prepare a shape model for matching."

HDEVELOP = {
    "find_shape_model.md": _operator(
        "find_shape_model",
        _FIND,
        [
            "find_shape_model(Image : : ModelID, SubPixel, NumLevels : Row, Column)",
        ],
        _param("Image", "input_object", "image", "object (byte)")
        + _param("ModelID", "input_control", "shape_model", " (handle)")
        + _param(
            "SubPixel",
            "input_control",
            "string",
            " (string)",
            "Default:\n'least_squares'",
            "Suggested values:\n'none', 'least_squares', 'max_deformation 1'",
        )
        + _param(
            "NumLevels",
            "input_control",
            "integer",
            " (integer)",
            "Default:\n0",
            "List of values:\n0, 1, 2",
        )
        + _param("Row", "output_control", "point.y-array", " (real)")
        + _param("Column", "output_control", "point.x-array", " (real)"),
    ),
    "create_shape_model.md": _operator(
        "create_shape_model",
        _CREATE,
        ["create_shape_model(Template : : Metric : ModelID)"],
        _param("Template", "input_object", "image", "object (byte)")
        + _param(
            "Metric",
            "input_control",
            "string",
            " (string)",
            "Default:\n'use_polarity'",
            "List of values:\n'ignore_global_polarity', 'use_polarity'",
        )
        + _param("ModelID", "output_control", "shape_model", " (handle)"),
    ),
}

DOTNET = {
    "find_shape_model.md": _operator(
        "FindShapeModel",
        _FIND,
        [
            "static void HOperatorSet.FindShapeModel(HObject image, HTuple modelID,"
            " HTuple subPixel, HTuple numLevels, out HTuple row, out HTuple column)",
            "void HShapeModel.FindShapeModel(HImage image, string subPixel,"
            " int numLevels, out HTuple row, out HTuple column)",
            "void HImage.FindShapeModel(HShapeModel modelID, string subPixel,"
            " int numLevels, out HTuple row, out HTuple column)",
        ],
        _param("image", "input_object", "image", "[HImage](HImage.md) (byte)")
        + _param(
            "modelID",
            "input_control",
            "shape_model",
            "[HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)",
        )
        + _param(
            "subPixel",
            "input_control",
            "string",
            "[HTuple](HTuple.md) (*string*)",
            'Default:\n"least_squares"',
            'Suggested values:\n"none", "least_squares", "max_deformation 1"',
        )
        + _param(
            "numLevels",
            "input_control",
            "integer",
            "[HTuple](HTuple.md) (*int* / long)",
            "Default:\n0",
            "List of values:\n0, 1, 2",
        )
        + _param("row", "output_control", "point.y-array", "[HTuple](HTuple.md)")
        + _param("column", "output_control", "point.x-array", "[HTuple](HTuple.md)"),
    ),
    "create_shape_model.md": _operator(
        "CreateShapeModel",
        _CREATE,
        [
            "static void HOperatorSet.CreateShapeModel(HObject template,"
            " HTuple metric, out HTuple modelID)",
            "public HShapeModel(HImage template, string metric)",
            "HShapeModel HImage.CreateShapeModel(string metric)",
        ],
        _param("template", "input_object", "image", "[HImage](HImage.md) (byte)")
        + _param(
            "metric",
            "input_control",
            "string",
            "[HTuple](HTuple.md) (*string*)",
            'Default:\n"use_polarity"',
            'List of values:\n"ignore_global_polarity", "use_polarity"',
        )
        + _param(
            "modelID",
            "output_control",
            "shape_model",
            "[HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)",
        ),
    ),
    "HShapeModel.md": (
        "# HShapeModel (Class)\n\n## Name\n\n"
        "`HShapeModel` — Represents an instance of a shape model for matching.\n\n"
        "## Methods\n\n|  |  |  |\n| --- | --- | --- |\n"
        "| `FindShapeModel` |  | Find the best matches of a shape model. |\n"
    ),
}

PYTHON = {
    "find_shape_model.md": _operator(
        "find_shape_model",
        _FIND,
        [
            f"def{NBSP}find_shape_model(image:{NBSP}HObject, model_id: HHandle,"
            " sub_pixel: MaybeSequence[str], num_levels: MaybeSequence[int])"
            " -> Tuple[Sequence[float], Sequence[float]]",
            "def find_shape_model_s(image: HObject, model_id: HHandle,"
            " sub_pixel: MaybeSequence[str], num_levels: MaybeSequence[int])"
            " -> Tuple[float, float]",
        ],
        _param("image", "input_object", "image", "HObject (byte)")
        + _param("model_id", "input_control", "shape_model", "HHandle")
        + _param(
            "sub_pixel",
            "input_control",
            "string",
            "MaybeSequence[str]",
            'Default:\n"least_squares"',
            'Suggested values:\n"none", "least_squares", "max_deformation 1"',
        )
        + _param(
            "num_levels",
            "input_control",
            "integer",
            "MaybeSequence[int]",
            "Default:\n0",
            "List of values:\n0, 1, 2",
        )
        + _param("row", "output_control", "point.y-array", "Sequence[float]")
        + _param("column", "output_control", "point.x-array", "Sequence[float]"),
    ),
    "create_shape_model.md": _operator(
        "create_shape_model",
        _CREATE,
        ["def create_shape_model(template: HObject, metric: str) -> HHandle"],
        _param("template", "input_object", "image", "HObject (byte)")
        + _param(
            "metric",
            "input_control",
            "string",
            "str",
            'Default:\n"use_polarity"',
            'List of values:\n"ignore_global_polarity", "use_polarity"',
        )
        + _param("model_id", "output_control", "shape_model", "HHandle"),
    ),
}

_COMMON = {
    "INDEX.md": "# HALCON 26.05 Reference Index\n\n## Matching / Shape-Based\n\n"
    "- [find_shape_model](find_shape_model.md) — Find matches.\n",
    "toc_matching.md": "## Matching\n\nList of Operators ↓\n",
}

PAGES = {"hdevelop": HDEVELOP, "dotnet": DOTNET, "python": PYTHON}


def write_output(
    root: Path, langs: tuple[str, ...] = ("hdevelop", "dotnet", "python")
) -> Path:
    """在 ``root`` 下建立與 ``output/`` 相同結構的樣本，回傳 ``root``。"""
    for lang in langs:
        folder = root / lang
        folder.mkdir(parents=True, exist_ok=True)
        for name, text in {**PAGES[lang], **_COMMON}.items():
            (folder / name).write_text(text, encoding="utf-8")
    return root
