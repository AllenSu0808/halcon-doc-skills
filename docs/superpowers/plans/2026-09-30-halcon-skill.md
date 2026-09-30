# HALCON 程式撰寫 Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增 `build-skill` 子命令，把 `output/` 的 HALCON 26.05 文件包成可複製到專案 `.claude/skills/halcon/` 的 skill（SKILL.md、查詢／檢查腳本、陷阱清單、簽章與參數表）。

**Architecture:** 產生端（本 repo 套件）以 `signatures.py` 解析每頁 Markdown 產生 `SIGNATURES.tsv` / `PARAMS.tsv`，`skill_build.py` 把手寫的 `skill_template/` 與各語言文件組成 `dist/skill/halcon/`。使用端是 `skill_template/scripts/` 下三支純標準函式庫腳本：`halcon_ref.py`（讀表與名稱比對）、`halcon_check.py`（程式碼檢查）、`halcon_doc.py`（CLI）。

**Tech Stack:** Python 3.13（產生端）、Python 3.10+ 標準函式庫（skill 腳本）、pytest、ruff、uv。

**Spec:** `docs/superpowers/specs/2026-09-30-halcon-skill-design.md`

## Global Constraints

- skill 腳本（`skill_template/scripts/*.py`）只能用 Python 3.10+ 標準函式庫；不可用 3.11+ 功能（`tomllib`、`ExceptionGroup`、`typing.Self`、`datetime.UTC` 等）。以 `uv run ruff check --target-version py310 skill_template` 驗證。
- 所有註解與 docstring 用繁體中文（zh-TW），Sphinx/reST 風格；識別字用英文。
- 程式碼行寬 88；以 `uv run ruff format` 與 `uv run ruff check .` 為準。
- 文件版本固定為 HALCON 26.05；語言固定為 `hdevelop`、`dotnet`、`python`（沿用 `config.LANGS`）。
- 不打包 `output/assets/`；`dist/` 已在 `.gitignore`，不進版本控管。
- `build-skill` 任一語言運算子頁解析失敗率 > 1%（`MAX_FAILURE_RATE = 0.01`）或沒有任何語言時 exit 1。
- `check` 所有結果皆為警告，不修改檔案；`halcon_doc.py check` exit code 固定為 0（語言無法判斷等 DocError 除外）。
- Commit message 依使用者規範：`<prefix>: <中文摘要>`，下一行起以 `--- 類別 ---` 分段、條列 `1.` `2.`。

## 與 Spec 的差異（實作前已確認的調整）

原型已對完整 `output/` 驗證（三語言 0 頁解析失敗；dotnet 6,214 簽章列）。以下差異已同步寫回 spec（Task 6 Step 1）：

1. **`PARAMS.tsv` 第一欄為 `page` 而非 `name`**：Python 同頁有 `find_x` 與 `find_x_s` 兩個名稱，用頁面檔名當鍵才能共用參數。
2. **類別頁只產生一列 `kind=class`**：`class` 子命令改用運算子頁中 `owner=<類別>` 的 method / constructor 列，能直接顯示完整簽章，不需要解析類別頁表格。
3. **腳本拆成三個檔案**：`halcon_ref.py` / `halcon_check.py` / `halcon_doc.py`，避免 `__main__` 與模組重複載入造成例外類別不一致。
4. **複製頁面時把 U+00A0（不換行空白）換成一般空白**：實際 Python 簽章是 `def abs_image(image: HObject)`，不處理會讓 grep 退路失效。
5. **`check` 依副檔名判斷語言**（`.cs` / `.py` / `.hdev` / `.hdvp`），無法判斷才用專案推斷。
6. **`build-skill` 拒絕覆寫非 skill 的資料夾**：`--out` 已存在但沒有 `SKILL.md` 時 raise `FileExistsError`，避免 `--out output` 之類的誤刪。
7. **陷阱清單每條標示來源**：「文件」（可在 references 查證）或「經驗」（本文件未收錄）；並新增「角度可能是 `angle.deg`」一條（實測 13 個 HDevelop 運算子用度數，例如 `rotate_image`）。

## Review Focus

1. `--out` 指向既有的非 skill 資料夾（例如 `output/`）時不可刪除資料 → 由 Task 2 `test_refuses_to_overwrite_unrelated_folder` 與 `test_cli_build_skill_exit_codes` 釘住。
2. 實際頁面含 U+00A0，簽章解析與 grep 退路都必須正常 → Task 1 `test_python_signature_with_nbsp_and_s_variant`、Task 2 `test_build_replaces_nbsp_in_copied_pages`。
3. Windows 主控台（cp950 / ascii）輸出中文與「—」不可崩潰 → Task 4 `test_script_output_survives_non_utf8_console`。
4. 跨多行呼叫、字串內含逗號與括號的參數計數要正確 → Task 3 `test_split_args_respects_nesting_and_strings`、`test_dotnet_correct_code_is_ok`（跨兩行呼叫）。
5. HDevelop 控制流程關鍵字、XML 註解、`.hdev` 內自訂 procedure 不可被誤報 → Task 3 `test_hdevelop_xml_skips_keywords_procedures_and_comments`。

## File Structure

| 檔案 | 動作 | 責任 |
|---|---|---|
| `src/halcon_doc_skills/signatures.py` | 新增 | 解析單頁 Markdown → `SignatureRow` / `ParamRow`；寫 TSV |
| `src/halcon_doc_skills/skill_build.py` | 新增 | 複製範本與頁面、產生 TSV、統計與失敗率 |
| `src/halcon_doc_skills/cli.py` | 修改 | 新增 `build-skill` 子命令 |
| `skill_template/scripts/halcon_ref.py` | 新增 | 讀 TSV、名稱正規化、語言推斷、段落切割 |
| `skill_template/scripts/halcon_check.py` | 新增 | 抽出呼叫、參數切割、三項檢查 |
| `skill_template/scripts/halcon_doc.py` | 新增 | CLI：search / sig / params / section / class / check |
| `skill_template/SKILL.md` | 新增 | 觸發描述、鐵則、工作流程 |
| `skill_template/pitfalls/{dotnet,python,hdevelop}.md` | 新增 | 各語言陷阱 30～60 條 |
| `tests/md_fixtures.py` | 新增 | 三語言樣本頁（仿實際格式，含 U+00A0） |
| `tests/skill_scripts.py` | 新增 | 把 `skill_template/scripts` 加入 `sys.path` |
| `tests/test_signatures.py` 等 5 個測試檔 | 新增 | 見各 Task |
| `README.md` | 修改 | 新增「產生 Claude Code skill」段落 |

---

### Task 1: 簽章與參數解析器

**Files:**
- Create: `tests/md_fixtures.py`
- Create: `tests/test_signatures.py`
- Create: `src/halcon_doc_skills/signatures.py`

**Interfaces:**
- Consumes: `halcon_doc_skills.indexer.read_title_and_summary(md: str, page: str) -> tuple[str, str]`（既有）
- Produces:
  - `SignatureRow(name, kind, owner, signature, summary, page)`（frozen dataclass，全為 `str`；`kind` ∈ `operator` / `method` / `constructor` / `class`）
  - `ParamRow(page, param, direction, type, default, list_of_values, suggested_values)`（frozen dataclass，全為 `str`；多值以 `" | "` 分隔）
  - `ParsedPage(kind: str, signatures: list[SignatureRow], params: list[ParamRow])`
  - `parse_page(md: str, page: str, lang: str) -> ParsedPage | None`（非運算子／類別頁回傳 `None`）
  - `write_tsv(path: Path, rows: Iterable[SignatureRow | ParamRow], cls: type) -> None`
  - `clean(text: str) -> str`、`split_values(text: str) -> str`、`VALUE_SEP = " | "`
  - `tests/md_fixtures.py`：`HDEVELOP` / `DOTNET` / `PYTHON`（`dict[檔名, Markdown]`）、`write_output(root: Path, langs: tuple[str, ...] = (...)) -> Path`

- [ ] **Step 1: 建立樣本頁 `tests/md_fixtures.py`**

檔案 `tests/md_fixtures.py`：

```python
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
```

- [ ] **Step 2: 寫失敗的測試 `tests/test_signatures.py`**

檔案 `tests/test_signatures.py`：

```python
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
```

- [ ] **Step 3: 執行測試確認失敗**

Run: `uv run pytest tests/test_signatures.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'halcon_doc_skills.signatures'`

- [ ] **Step 4: 實作 `src/halcon_doc_skills/signatures.py`**

檔案 `src/halcon_doc_skills/signatures.py`：

```python
"""由轉換後的 Markdown 頁面解析簽章與參數，產生 skill 用的 TSV。"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import astuple, dataclass, fields
from pathlib import Path

from .indexer import read_title_and_summary

# 標題尾端的頁面種類，例如 ``# find_shape_model (Operator)``
_KIND_RE = re.compile(r"^# .+ \((Operator|Class)\)\s*$", re.MULTILINE)
_SECTION_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
_HDEVELOP_SIG_RE = re.compile(r"^([a-z][a-z0-9_]*) ?\((.*)\)$")
_PYTHON_SIG_RE = re.compile(r"^def ([a-z][a-z0-9_]*)\((.*)\) -> .+$")
_DOTNET_MEMBER_RE = re.compile(r"^(?:static )?\S+ (\w+)\.(\w+)\((.*)\)$")
_DOTNET_CTOR_RE = re.compile(r"^public (\w+)\((.*)\)$")
_PARAM_RE = re.compile(r"^\*\*`(\w+)`\*\* \((\w+)\)\s+.*?`→`\s*(.*)$")
_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_VALUE_RE = re.compile(r"'[^']*'|\"[^\"]*\"|[^,]+")

# 參數屬性標籤 → ParamRow 欄位
_ATTR_FIELDS = {
    "Default:": "default",
    "List of values:": "list_of_values",
    "Suggested values:": "suggested_values",
}

VALUE_SEP = " | "


@dataclass(frozen=True)
class SignatureRow:
    """SIGNATURES.tsv 的一列。"""

    name: str
    kind: str  # operator / method / constructor / class
    owner: str
    signature: str
    summary: str
    page: str


@dataclass(frozen=True)
class ParamRow:
    """PARAMS.tsv 的一列。"""

    page: str
    param: str
    direction: str
    type: str
    default: str
    list_of_values: str
    suggested_values: str


@dataclass(frozen=True)
class ParsedPage:
    """單一頁面的解析結果。"""

    kind: str  # operator / class
    signatures: list[SignatureRow]
    params: list[ParamRow]


def clean(text: str) -> str:
    """把不換行空白、tab 與換行換成一般空白，並去掉頭尾空白。"""
    return re.sub(r"[\s ]+", " ", text).strip()


def sections(md: str) -> dict[str, str]:
    """把頁面切成 ``{段落標題: 內文}``。"""
    matches = list(_SECTION_RE.finditer(md))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(md)
        result[match.group(1)] = md[match.end() : end]
    return result


def _signature_row(
    lang: str, text: str, summary: str, page: str
) -> SignatureRow | None:
    if lang in ("hdevelop", "python"):
        pattern = _HDEVELOP_SIG_RE if lang == "hdevelop" else _PYTHON_SIG_RE
        match = pattern.match(text)
        if not match:
            return None
        return SignatureRow(match[1], "operator", "", text, summary, page)
    ctor = _DOTNET_CTOR_RE.match(text)
    if ctor:
        return SignatureRow(ctor[1], "constructor", ctor[1], text, summary, page)
    member = _DOTNET_MEMBER_RE.match(text)
    if not member:
        return None
    kind = "operator" if member[1] == "HOperatorSet" else "method"
    return SignatureRow(member[2], kind, member[1], text, summary, page)


def _parse_signatures(
    lang: str, body: str, summary: str, page: str
) -> list[SignatureRow]:
    rows: list[SignatureRow] = []
    for line in body.splitlines():
        line = clean(line)
        if not (line.startswith("`") and line.endswith("`") and len(line) > 2):
            continue
        row = _signature_row(lang, line[1:-1], summary, page)
        if row:
            rows.append(row)
    return rows


def split_values(text: str) -> str:
    """把 ``'a', 'b', 1`` 這類清單轉成以 `` | `` 分隔的字串。"""
    values = (clean(v) for v in _VALUE_RE.findall(text))
    return VALUE_SEP.join(v for v in values if v)


def _parse_params(body: str, page: str) -> list[ParamRow]:
    rows: list[ParamRow] = []
    current: dict[str, str] | None = None
    pending: str | None = None  # 等待值的屬性欄位
    collected: list[str] = []

    def flush_attr() -> None:
        nonlocal pending
        if current is not None and pending and collected:
            raw = " ".join(collected)
            current[pending] = raw if pending == "default" else split_values(raw)
        pending = None
        collected.clear()

    def flush_param() -> None:
        flush_attr()
        if current is not None:
            rows.append(ParamRow(page=page, **current))

    for raw_line in body.splitlines():
        line = clean(raw_line)
        header = _PARAM_RE.match(line)
        if header:
            flush_param()
            current = {
                "param": header[1],
                "direction": header[2],
                "type": clean(_LINK_RE.sub(r"\1", header[3]).replace("*", "")),
                "default": "",
                "list_of_values": "",
                "suggested_values": "",
            }
            continue
        if line in _ATTR_FIELDS:
            flush_attr()
            pending = _ATTR_FIELDS[line]
        elif pending and line:
            collected.append(line)
        elif pending:
            flush_attr()
    flush_param()
    return rows


def parse_page(md: str, page: str, lang: str) -> ParsedPage | None:
    """解析一頁運算子或類別頁；其他頁面（目錄、索引）回傳 ``None``。

    :param md: 頁面 Markdown。
    :param page: 頁面檔名，例如 ``find_shape_model.md``。
    :param lang: ``hdevelop`` / ``dotnet`` / ``python``。
    :return: 解析結果；運算子頁沒有任何簽章時 ``signatures`` 為空。
    """
    kind_match = _KIND_RE.search(md)
    if not kind_match:
        return None
    title, summary = read_title_and_summary(md, page)
    summary = clean(summary)
    body = sections(md)
    if kind_match[1] == "Class":
        row = SignatureRow(clean(title), "class", "", "", summary, page)
        return ParsedPage("class", [row], [])
    signatures = _parse_signatures(lang, body.get("Signature", ""), summary, page)
    params = _parse_params(body.get("Parameters", ""), page)
    return ParsedPage("operator", signatures, params)


def write_tsv(path: Path, rows: Iterable[SignatureRow | ParamRow], cls: type) -> None:
    """寫出 tab 分隔檔，首行為欄名；欄位內的空白已先以 ``clean`` 正規化。"""
    header = "\t".join(f.name for f in fields(cls))
    lines = [header] + ["\t".join(clean(v) for v in astuple(r)) for r in rows]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
```

- [ ] **Step 5: 執行測試確認通過**

Run: `uv run pytest tests/test_signatures.py -v`
Expected: 10 passed

- [ ] **Step 6: 以完整 output 煙霧測試（有 `output/` 時）**

Run:
```bash
uv run python - <<'EOF'
from pathlib import Path
from halcon_doc_skills.signatures import parse_page
for lang in ("hdevelop", "dotnet", "python"):
    ops = sigs = failed = 0
    for p in sorted(Path("output", lang).glob("*.md")):
        page = parse_page(p.read_text(encoding="utf-8"), p.name, lang)
        if page and page.kind == "operator":
            ops += 1
            sigs += len(page.signatures)
            failed += not page.signatures
    print(lang, ops, sigs, failed)
EOF
```
Expected（原型實測值）：`hdevelop 2313 2313 0`、`dotnet 2235 6115 0`、`python 2235 2697 0`

- [ ] **Step 7: Lint 並 commit**

```bash
uv run ruff format src tests && uv run ruff check .
git add src/halcon_doc_skills/signatures.py tests/md_fixtures.py tests/test_signatures.py
git commit -m "feat: 新增 HALCON 頁面簽章與參數解析器
--- feat ---
1. 新增 parse_page 解析三語言簽章與參數屬性
2. 新增 write_tsv 輸出 SIGNATURES 與 PARAMS 表
--- test ---
1. 新增三語言樣本頁與解析測試"
```

---

### Task 2: `build-skill` 產生流程

**Files:**
- Create: `src/halcon_doc_skills/skill_build.py`
- Modify: `src/halcon_doc_skills/cli.py`
- Modify: `README.md`（在「## 輸出結構」段落之後新增一節）
- Test: `tests/test_skill_build.py`

**Interfaces:**
- Consumes: Task 1 的 `parse_page`、`write_tsv`、`SignatureRow`、`ParamRow`；`config.LANGS`；`tests/md_fixtures.write_output`
- Produces:
  - `MAX_FAILURE_RATE = 0.01`
  - `LangStats(pages, operators, classes, signatures, params: int, failed: list[str])`，屬性 `failure_rate: float`
  - `BuildReport(stats: dict[str, LangStats])`，屬性 `ok: bool`
  - `build_skill(output: Path, template: Path, dest: Path) -> BuildReport`（`dest` 存在但無 `SKILL.md` 時 raise `FileExistsError`）
  - CLI：`halcon-doc-skills build-skill [--output output] [--template skill_template] [--out dist/skill/halcon]`
  - 產出結構：`<dest>/references/<lang>/{*.md, SIGNATURES.tsv, PARAMS.tsv}`，加上範本內容（排除 `__pycache__`）

- [ ] **Step 1: 寫失敗的測試 `tests/test_skill_build.py`**

檔案 `tests/test_skill_build.py`：

```python
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
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `uv run pytest tests/test_skill_build.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'halcon_doc_skills.skill_build'`

- [ ] **Step 3: 實作 `src/halcon_doc_skills/skill_build.py`**

檔案 `src/halcon_doc_skills/skill_build.py`：

```python
"""組出可直接複製到專案的 HALCON skill 資料夾。"""

from __future__ import annotations

import logging
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from . import config
from .signatures import ParamRow, SignatureRow, parse_page, write_tsv

log = logging.getLogger(__name__)

# 解析失敗率超過此值時 build-skill 視為失敗
MAX_FAILURE_RATE = 0.01


@dataclass
class LangStats:
    """單一語言的產生統計。"""

    pages: int = 0
    operators: int = 0
    classes: int = 0
    signatures: int = 0
    params: int = 0
    failed: list[str] = field(default_factory=list)

    @property
    def failure_rate(self) -> float:
        """解析失敗頁數 / 運算子頁數。"""
        return len(self.failed) / self.operators if self.operators else 0.0


@dataclass
class BuildReport:
    """build_skill 的結果。"""

    stats: dict[str, LangStats] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """至少產生一種語言，且每種語言失敗率都不超過門檻。"""
        return bool(self.stats) and all(
            s.failure_rate <= MAX_FAILURE_RATE for s in self.stats.values()
        )


def _build_lang(source: Path, dest: Path, lang: str) -> LangStats:
    stats = LangStats()
    signatures: list[SignatureRow] = []
    params: list[ParamRow] = []
    dest.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.glob("*.md")):
        # 不換行空白會讓 grep 找不到簽章，複製時一併換成一般空白
        text = path.read_text(encoding="utf-8").replace(" ", " ")
        (dest / path.name).write_text(text, encoding="utf-8")
        stats.pages += 1
        page = parse_page(text, path.name, lang)
        if page is None:
            continue
        if page.kind == "class":
            stats.classes += 1
        else:
            stats.operators += 1
            if not page.signatures:
                stats.failed.append(path.name)
        signatures += page.signatures
        params += page.params
    write_tsv(dest / "SIGNATURES.tsv", signatures, SignatureRow)
    write_tsv(dest / "PARAMS.tsv", params, ParamRow)
    stats.signatures = len(signatures)
    stats.params = len(params)
    return stats


def build_skill(output: Path, template: Path, dest: Path) -> BuildReport:
    """以 ``template`` 為基礎、``output`` 的文件為參考資料產生 skill。

    :param output: crawl/convert 產出的資料夾（含各語言子資料夾）。
    :param template: 手寫的 skill 範本資料夾（SKILL.md、scripts/、pitfalls/）。
    :param dest: 產出位置；若是先前產生的 skill（含 SKILL.md）會先整個刪除。
    :return: 各語言統計；缺少的語言不會出現在 ``stats``。
    :raises FileExistsError: ``dest`` 已存在但不是先前產生的 skill。
    """
    if dest.exists():
        # 避免 --out 指錯位置（例如 output/）時把資料整個刪掉
        if not (dest / "SKILL.md").is_file():
            raise FileExistsError(f"{dest} 已存在且不是先前產生的 skill，拒絕覆寫")
        shutil.rmtree(dest)
    shutil.copytree(template, dest, ignore=shutil.ignore_patterns("__pycache__"))
    report = BuildReport()
    for lang in config.LANGS:
        source = output / lang
        if not source.is_dir():
            log.warning("略過 %s：找不到 %s", lang, source)
            continue
        report.stats[lang] = _build_lang(source, dest / "references" / lang, lang)
    return report
```

- [ ] **Step 4: 修改 `src/halcon_doc_skills/cli.py`**

依下列 diff 修改（四處：模組 docstring、import、子命令、`_log_build` 與 `main` 分支）：

```diff
@@ -1,4 +1,4 @@
-"""命令列介面：crawl / convert / verify。"""
+"""命令列介面：crawl / convert / verify / build-skill。"""
 
 from __future__ import annotations
 
@@ -13,6 +13,7 @@
 from .formulas import FormulaStore
 from .ocr import OcrOptions
 from .pipeline import convert_all, crawl, resolve_formulas
+from .skill_build import MAX_FAILURE_RATE, BuildReport, build_skill
 from .verify import verify_output
 
 log = logging.getLogger(__name__)
@@ -47,6 +48,11 @@
 
     verify_p = sub.add_parser("verify", help="檢查輸出品質")
     _add_paths(verify_p, cache=False)
+
+    skill_p = sub.add_parser("build-skill", help="產生 HALCON skill 資料夾")
+    _add_paths(skill_p, cache=False)
+    skill_p.add_argument("--template", type=Path, default=Path("skill_template"))
+    skill_p.add_argument("--out", type=Path, default=Path("dist/skill/halcon"))
     return parser
 
 
@@ -78,10 +84,31 @@
     convert_all(cache, args.output, formulas=store.results())
 
 
+def _log_build(report: BuildReport) -> None:
+    """輸出 build-skill 各語言統計與解析失敗頁面。"""
+    if not report.stats:
+        log.error("找不到任何語言的文件資料夾")
+    for lang, stats in report.stats.items():
+        log.info(
+            "%s：%d 頁、%d 運算子、%d 類別、%d 簽章、%d 參數、%d 解析失敗",
+            lang,
+            stats.pages,
+            stats.operators,
+            stats.classes,
+            stats.signatures,
+            stats.params,
+            len(stats.failed),
+        )
+        for page in stats.failed:
+            log.warning("%s 解析失敗：%s", lang, page)
+        if stats.failure_rate > MAX_FAILURE_RATE:
+            log.error("%s 解析失敗率 %.1f%% 超過門檻", lang, stats.failure_rate * 100)
+
+
 def main(argv: Sequence[str] | None = None) -> int:
     """程式進入點。
 
-    :return: 結束碼；``verify`` 發現問題時為 1，其餘為 0。
+    :return: 結束碼；``verify`` 發現問題或 ``build-skill`` 失敗時為 1，其餘為 0。
     """
     args = build_parser().parse_args(argv)
     logging.basicConfig(
@@ -93,6 +120,14 @@
             log.error(problem)
         log.info("各語言 .md 檔案數：%s", report.counts)
         return 0 if report.ok else 1
+    if args.command == "build-skill":
+        try:
+            build = build_skill(args.output, args.template, args.out)
+        except FileExistsError as error:
+            log.error(error)
+            return 1
+        _log_build(build)
+        return 0 if build.ok else 1
 
     cache = PageCache(args.cache_dir)
     if args.command == "crawl":
```

- [ ] **Step 5: 執行測試確認通過**

Run: `uv run pytest tests/test_skill_build.py tests/test_cli.py -v`
Expected: 全部 passed（test_skill_build 8 個）

- [ ] **Step 6: 更新 `README.md`**

在 `## 輸出結構` 那一節（最後一行為「- 失敗的網址記錄在 `cache/failed.txt`。」）之後加上：

````markdown

## 產生 Claude Code skill

    uv run halcon-doc-skills build-skill                    # 產生到 dist/skill/halcon/
    uv run halcon-doc-skills build-skill --out /tmp/halcon  # 指定輸出位置

把 `dist/skill/halcon/` 整個複製到 HALCON 專案的 `.claude/skills/halcon/`。

- 只需要部分語言時，刪除 `references/<lang>/` 與 `pitfalls/<lang>.md` 即可。
- skill 附帶 `scripts/halcon_doc.py`（Python 3.10+，只用標準函式庫），提供
  `search`、`sig`、`params`、`section`、`class`、`check` 子命令。
- `--out` 已存在但不是先前產生的 skill（沒有 `SKILL.md`）時會拒絕覆寫。
- skill 原始檔在 `skill_template/`；修改後重跑 `build-skill` 並重新複製到專案。
````

- [ ] **Step 7: Lint 並 commit**

```bash
uv run ruff format src tests && uv run ruff check .
git add src/halcon_doc_skills/skill_build.py src/halcon_doc_skills/cli.py tests/test_skill_build.py README.md
git commit -m "feat: 新增 build-skill 產生 HALCON skill 資料夾
--- feat ---
1. 新增 build_skill 複製範本與文件並產生簽章表
2. 新增 build-skill 子命令與解析失敗率門檻
3. 新增拒絕覆寫非 skill 資料夾的保護
--- docs ---
1. 新增 README 的 skill 產生說明
--- test ---
1. 新增 build-skill 產出結構與結束碼測試"
```

---

### Task 3: 參考資料讀取與 `check` 檢查邏輯

**Files:**
- Create: `tests/skill_scripts.py`
- Create: `skill_template/scripts/halcon_ref.py`
- Create: `skill_template/scripts/halcon_check.py`
- Test: `tests/test_halcon_check.py`

**Interfaces:**
- Consumes: Task 2 的 `build_skill`（測試用來產生 `references/`）；Task 1 的 TSV 欄位順序
- Produces（`halcon_ref`）：
  - `LANGS`、`REFERENCES: Path`（`<腳本目錄>/../references`）、`VALUE_SEP`
  - `class DocError(Exception)`
  - `Signature(name, kind, owner, signature, summary, page)`、`Param(page, param, direction, type, default, list_of_values, suggested_values)`，`Param.values() -> list[str]`（去引號）
  - `key(name: str) -> str`（去前綴、去底線、小寫）
  - `Reference(root: Path, lang: str)`：`.lang`、`.dir`、`.signatures`、`.params`、`.pages(name) -> list[str]`、`.suggest(name) -> str`、`.rows_for(page) -> list[Signature]`、`.params_for(page) -> list[Param]`、`.read_page(page) -> str`
  - `available_langs(root: Path = REFERENCES) -> list[str]`、`detect_lang(start: Path) -> str`
  - `sections(md: str) -> dict[str, str]`、`param_blocks(parameters: str) -> dict[str, str]`
- Produces（`halcon_check`）：
  - `Call(name: str, line: int, args: list[str], kwargs: dict[str, str])`
  - `split_args(text: str) -> list[str]`、`extract_calls(text: str, lang: str) -> list[Call]`
  - `param_names(sig: Signature, lang: str) -> list[str]`、`check_call(ref: Reference, call: Call) -> list[str]`
  - `run_check(files: Sequence[Path], root: Path, lang: str | None, cwd: Path) -> str`（最後一行為 `OK: <n> HALCON calls checked` 或 `<k> warning(s) in <n> HALCON calls`）
  - 警告格式：`<file>:<line>: [unknown-operator|arg-count|invalid-value] ...`；讀檔失敗：`<file>: [read-error] ...`

- [ ] **Step 1: 建立 `tests/skill_scripts.py`**

檔案 `tests/skill_scripts.py`：

```python
"""讓測試能匯入 skill_template/scripts/ 下的獨立腳本。"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "skill_template"
SCRIPTS = TEMPLATE / "scripts"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
```

- [ ] **Step 2: 寫失敗的測試 `tests/test_halcon_check.py`**

檔案 `tests/test_halcon_check.py`：

```python
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
```

- [ ] **Step 3: 執行測試確認失敗**

Run: `uv run pytest tests/test_halcon_check.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'halcon_check'`

- [ ] **Step 4: 實作 `skill_template/scripts/halcon_ref.py`**

檔案 `skill_template/scripts/halcon_ref.py`：

```python
"""HALCON 參考資料的讀取與名稱比對（halcon_doc.py 與 halcon_check.py 共用）。"""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from pathlib import Path

LANGS = ("hdevelop", "dotnet", "python")
REFERENCES = Path(__file__).resolve().parent.parent / "references"
VALUE_SEP = " | "

# 語言推斷時略過的資料夾
_SKIP_DIRS = {".git", ".claude", ".venv", "venv", "node_modules", "bin", "obj"}
_SECTION_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
_PARAM_HEADER_RE = re.compile(r"^\*\*`(\w+)`\*\*", re.MULTILINE)


class DocError(Exception):
    """查詢失敗（語言未安裝、查無運算子等），訊息直接給使用者看。"""


@dataclass(frozen=True)
class Signature:
    """SIGNATURES.tsv 的一列。"""

    name: str
    kind: str
    owner: str
    signature: str
    summary: str
    page: str


@dataclass(frozen=True)
class Param:
    """PARAMS.tsv 的一列。"""

    page: str
    param: str
    direction: str
    type: str
    default: str
    list_of_values: str
    suggested_values: str

    def values(self) -> list[str]:
        """合法值清單（去掉引號）；沒有嚴格列舉時為空。"""
        if not self.list_of_values:
            return []
        return [v.strip("'\"") for v in self.list_of_values.split(VALUE_SEP)]


def key(name: str) -> str:
    """名稱比對鍵：去掉前綴、底線並轉小寫，讓各語言寫法對應到同一運算子。"""
    return name.rsplit(".", 1)[-1].replace("_", "").lower()


def _read_tsv(path: Path) -> list[list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.split("\t") for line in lines[1:] if line]


class Reference:
    """單一語言的參考資料。"""

    def __init__(self, root: Path, lang: str) -> None:
        self.lang = lang
        self.dir = root / lang
        sig_path = self.dir / "SIGNATURES.tsv"
        param_path = self.dir / "PARAMS.tsv"
        if not sig_path.is_file() or not param_path.is_file():
            installed = ", ".join(available_langs(root)) or "無"
            raise DocError(f"{lang} 文件未安裝（已安裝：{installed}）")
        self.signatures = [Signature(*row) for row in _read_tsv(sig_path)]
        self.params = [Param(*row) for row in _read_tsv(param_path)]

    def pages(self, name: str) -> list[str]:
        """由任意寫法的名稱找出頁面檔名；查無時拋出含相近名稱的 DocError。"""
        wanted = key(name)
        found = {
            s.page
            for s in self.signatures
            if key(s.name) == wanted or key(Path(s.page).stem) == wanted
        }
        if found:
            return sorted(found)
        raise DocError(f"查無「{name}」。{self.suggest(name)}")

    def suggest(self, name: str) -> str:
        """回傳相近名稱提示字串。"""
        names = sorted({s.name for s in self.signatures})
        lowered = {n.lower(): n for n in names}
        close = difflib.get_close_matches(
            name.rsplit(".", 1)[-1].lower(), list(lowered), n=5, cutoff=0.6
        )
        if not close:
            return "請改用 search 以關鍵字查詢。"
        return "相近名稱：" + ", ".join(lowered[c] for c in close)

    def rows_for(self, page: str) -> list[Signature]:
        """該頁的所有簽章列（不含類別列）。"""
        return [s for s in self.signatures if s.page == page and s.kind != "class"]

    def params_for(self, page: str) -> list[Param]:
        """該頁的所有參數（依頁面順序）。"""
        return [p for p in self.params if p.page == page]

    def read_page(self, page: str) -> str:
        """讀取頁面 Markdown。"""
        return (self.dir / page).read_text(encoding="utf-8")


def available_langs(root: Path = REFERENCES) -> list[str]:
    """已安裝的語言。"""
    return [lang for lang in LANGS if (root / lang / "SIGNATURES.tsv").is_file()]


def detect_lang(start: Path) -> str:
    """由專案檔案推斷語言（只看起點與往下兩層）。

    :raises DocError: 無法判斷或同時符合多種語言時。
    """
    found: set[str] = set()
    for path in _walk(start, depth=2):
        name = path.name.lower()
        if name.endswith(".csproj"):
            found.add("dotnet")
        elif name == "pyproject.toml" or name.endswith(".py"):
            found.add("python")
        elif name.endswith((".hdev", ".hdvp")):
            found.add("hdevelop")
    if len(found) == 1:
        return found.pop()
    hint = "、".join(sorted(found)) if found else "找不到 .csproj / .py / .hdev"
    raise DocError(f"無法判斷語言（{hint}），請加上 --lang {{{','.join(LANGS)}}}")


def _walk(root: Path, depth: int) -> list[Path]:
    result: list[Path] = []
    try:
        entries = list(root.iterdir())
    except OSError:
        return result
    for entry in entries:
        if entry.is_dir():
            if depth > 0 and entry.name not in _SKIP_DIRS:
                result += _walk(entry, depth - 1)
        else:
            result.append(entry)
    return result


def sections(md: str) -> dict[str, str]:
    """把頁面切成 ``{段落標題: 內文}``。"""
    matches = list(_SECTION_RE.finditer(md))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(md)
        result[match.group(1)] = md[match.end() : end].strip("\n")
    return result


def param_blocks(parameters: str) -> dict[str, str]:
    """把 ``## Parameters`` 段落切成 ``{參數名: 原文}``。"""
    matches = list(_PARAM_HEADER_RE.finditer(parameters))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(parameters)
        )
        result[match.group(1)] = parameters[match.start() : end].strip()
    return result
```

- [ ] **Step 5: 實作 `skill_template/scripts/halcon_check.py`**

檔案 `skill_template/scripts/halcon_check.py`：

```python
"""檢查程式碼中的 HALCON 呼叫（halcon_doc.py check 的實作）。

只報高信心問題：運算子不存在、參數數量不符、字串值不在 List of values。
所有結果都是警告，不修改檔案。
"""

from __future__ import annotations

import html
import re
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path

from halcon_ref import DocError, Reference, Signature, detect_lang

_EXT_LANG = {".cs": "dotnet", ".py": "python", ".hdev": "hdevelop", ".hdvp": "hdevelop"}
_DOTNET_CALL_RE = re.compile(r"\bHOperatorSet\s*\.\s*([A-Za-z]\w*)\s*\(")
_PY_IMPORT_RE = re.compile(r"^\s*import\s+halcon(?:\s+as\s+(\w+))?\s*$", re.MULTILINE)
_HDEV_CALL_RE = re.compile(
    r"^[ \t]*(?:<l>)?[ \t]*([a-z][a-z0-9_]*)[ \t]*\(", re.MULTILINE
)
_HDEV_PROC_RE = re.compile(r'<procedure\s+name="(\w+)"')
# 看起來像呼叫的控制流程關鍵字，例如 ``if (A > 0)``
_HDEV_KEYWORDS = frozenset(
    ("if", "elseif", "while", "until", "switch", "return", "throw", "catch")
)
# halcon Python 套件中不屬於運算子的函式
_PY_HELPERS = {"himage_as_numpy_array", "himage_from_numpy_array"}
_STRING_RE = re.compile(r"""^(?:"((?:[^"\\]|\\.)*)"|'([^']*)')$""")


@dataclass(frozen=True)
class Call:
    """程式碼中的一次 HALCON 呼叫。"""

    name: str
    line: int
    args: list[str]  # 位置參數原文
    kwargs: dict[str, str]  # 關鍵字參數原文（僅 Python）


def split_args(text: str) -> list[str]:
    """以最外層逗號切開參數，忽略括號與字串內的逗號。"""
    args: list[str] = []
    depth = 0
    quote = ""
    current: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]
        if quote:
            current.append(char)
            if char == "\\" and quote == '"' and index + 1 < len(text):
                current.append(text[index + 1])
                index += 1
            elif char == quote:
                quote = ""
        elif char in "\"'":
            quote = char
            current.append(char)
        elif char in "([{":
            depth += 1
            current.append(char)
        elif char in ")]}":
            depth -= 1
            current.append(char)
        elif char == "," and depth == 0:
            args.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1
    last = "".join(current).strip()
    if last or args:
        args.append(last)
    return args


def _closing_paren(text: str, start: int) -> int:
    """回傳與 ``text[start - 1]`` 的 ``(`` 配對的 ``)`` 位置；找不到回傳 -1。"""
    depth = 1
    quote = ""
    index = start
    while index < len(text):
        char = text[index]
        if quote:
            if char == "\\" and quote == '"':
                index += 1
            elif char == quote:
                quote = ""
        elif char in "\"'":
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return -1


def _calls(text: str, pattern: re.Pattern[str], python: bool) -> Iterator[Call]:
    for match in pattern.finditer(text):
        end = _closing_paren(text, match.end())
        if end < 0:
            continue
        line = text.count("\n", 0, match.start()) + 1
        args: list[str] = []
        kwargs: dict[str, str] = {}
        for arg in split_args(text[match.end() : end]):
            kw = re.match(r"^([A-Za-z_]\w*)\s*=(?!=)\s*(.*)$", arg, re.DOTALL)
            if python and kw:
                kwargs[kw[1]] = kw[2]
            else:
                args.append(arg)
        yield Call(match[1], line, args, kwargs)


def extract_calls(text: str, lang: str) -> list[Call]:
    """抽出程式碼中的 HALCON 呼叫。"""
    if lang == "dotnet":
        return list(_calls(text, _DOTNET_CALL_RE, python=False))
    if lang == "python":
        aliases = {m[1] or "halcon" for m in _PY_IMPORT_RE.finditer(text)}
        calls: list[Call] = []
        for alias in aliases:
            pattern = re.compile(rf"\b{re.escape(alias)}\.([a-z_][a-z0-9_]*)\s*\(")
            calls += [
                c
                for c in _calls(text, pattern, python=True)
                if c.name not in _PY_HELPERS
            ]
        return sorted(calls, key=lambda c: c.line)
    text = html.unescape(text)
    procedures = set(_HDEV_PROC_RE.findall(text))
    return [
        c
        for c in _calls(text, _HDEV_CALL_RE, python=False)
        if c.name not in _HDEV_KEYWORDS and c.name not in procedures
    ]


def param_names(sig: Signature, lang: str) -> list[str]:
    """由簽章取出參數名（依呼叫時的位置順序）。"""
    inner = sig.signature[sig.signature.index("(") + 1 : sig.signature.rindex(")")]
    if lang == "hdevelop":
        parts = re.split(r"[:,]", inner)
        return [p.strip() for p in parts if p.strip()]
    names: list[str] = []
    for part in split_args(inner):
        if lang == "python":
            names.append(part.split(":", 1)[0].strip())
        else:
            names.append(part.split()[-1])
    return [n for n in names if n]


def _find(ref: Reference, call: Call) -> Signature | None:
    for sig in ref.signatures:
        if sig.name != call.name or sig.kind != "operator":
            continue
        if ref.lang != "dotnet" or sig.owner == "HOperatorSet":
            return sig
    return None


def check_call(ref: Reference, call: Call) -> list[str]:
    """回傳單一呼叫的警告（不含檔名與行號）。"""
    sig = _find(ref, call)
    shown = f"HOperatorSet.{call.name}" if ref.lang == "dotnet" else call.name
    if sig is None:
        hint = ref.suggest(call.name)
        if ref.lang == "hdevelop":
            hint += "（若為自訂 procedure 可忽略）"
        return [f"[unknown-operator] {shown} 不存在 → {hint}"]
    names = param_names(sig, ref.lang)
    given = len(call.args) + len(call.kwargs)
    warnings: list[str] = []
    if given != len(names):
        warnings.append(
            f"[arg-count] {shown} 需要 {len(names)} 個參數，實際 {given} 個"
            f" → 執行 sig {call.name}"
        )
    params = {p.param: p for p in ref.params_for(sig.page)}
    values = list(zip(names, call.args, strict=False)) + list(call.kwargs.items())
    for name, arg in values:
        literal = _STRING_RE.match(arg.strip())
        param = params.get(name)
        if not literal or param is None or not param.values():
            continue
        value = literal[1] if literal[1] is not None else literal[2]
        if value not in param.values():
            allowed = ", ".join(param.values())
            warnings.append(
                f"[invalid-value] {shown} 參數 {name}={arg.strip()} 不在合法值內"
                f" → {allowed}"
            )
    return warnings


def run_check(files: Sequence[Path], root: Path, lang: str | None, cwd: Path) -> str:
    """檢查多個檔案並回傳報告文字（讀檔失敗只影響該檔）。"""
    out: list[str] = []
    total = 0
    refs: dict[str, Reference] = {}
    for path in files:
        file_lang = lang or _EXT_LANG.get(path.suffix.lower()) or detect_lang(cwd)
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as error:
            out.append(f"{path}: [read-error] {error}")
            continue
        if file_lang not in refs:
            refs[file_lang] = Reference(root, file_lang)
        for call in extract_calls(text, file_lang):
            total += 1
            out += [
                f"{path}:{call.line}: {w}" for w in check_call(refs[file_lang], call)
            ]
    warnings = sum(1 for line in out if "[read-error]" not in line)
    if not out:
        return f"OK: {total} HALCON calls checked"
    out.append(f"{warnings} warning(s) in {total} HALCON calls")
    return "\n".join(out)


__all__ = ["Call", "DocError", "check_call", "extract_calls", "run_check", "split_args"]
```

- [ ] **Step 6: 執行測試確認通過**

Run: `uv run pytest tests/test_halcon_check.py -v`
Expected: 11 passed

- [ ] **Step 7: Lint（含 3.10 相容檢查）並 commit**

```bash
uv run ruff format skill_template tests && uv run ruff check . && uv run ruff check --target-version py310 skill_template
git add skill_template/scripts/halcon_ref.py skill_template/scripts/halcon_check.py tests/skill_scripts.py tests/test_halcon_check.py
git commit -m "feat: 新增 skill 參考資料讀取與程式碼檢查
--- feat ---
1. 新增 halcon_ref 讀取簽章表並正規化名稱
2. 新增 halcon_check 檢查運算子、參數數量與字串值
--- test ---
1. 新增三語言正確與錯誤樣本的檢查測試"
```

---

### Task 4: 查詢 CLI `halcon_doc.py`

**Files:**
- Create: `skill_template/scripts/halcon_doc.py`
- Test: `tests/test_halcon_doc.py`

**Interfaces:**
- Consumes: Task 3 的 `halcon_ref` 全部公開名稱與 `halcon_check.run_check`
- Produces:
  - `cmd_search(ref, words) -> str`、`cmd_sig(ref, name) -> str`、`cmd_params(ref, name, wanted) -> str`、`cmd_section(ref, name, title) -> str`、`cmd_class(ref, name) -> str`
  - `build_parser() -> argparse.ArgumentParser`（子命令：`search`、`sig`、`params`、`section`、`class`、`check`；全域 `--lang`）
  - `run(argv: Sequence[str], root: Path = REFERENCES, cwd: Path | None = None) -> str`（失敗 raise `DocError`）
  - `main(argv=None) -> int`：成功 0、`DocError` 時印 `錯誤：…` 到 stderr 並回傳 1；stdout / stderr 一律 UTF-8

- [ ] **Step 1: 寫失敗的測試 `tests/test_halcon_doc.py`**

檔案 `tests/test_halcon_doc.py`：

```python
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


def test_class_lists_constructors_and_methods(skill: Path) -> None:
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
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `uv run pytest tests/test_halcon_doc.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'halcon_doc'`

- [ ] **Step 3: 實作 `skill_template/scripts/halcon_doc.py`**

檔案 `skill_template/scripts/halcon_doc.py`：

```python
"""HALCON 26.05 文件查詢工具（skill 附帶，僅使用 Python 3.10+ 標準函式庫）。

用法::

    python halcon_doc.py [--lang dotnet] search shape model
    python halcon_doc.py sig FindShapeModel
    python halcon_doc.py params find_shape_model SubPixel NumLevels
    python halcon_doc.py section find_shape_model "Possible Successors"
    python halcon_doc.py class HShapeModel
    python halcon_doc.py check src/Inspect.cs
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

import halcon_check
from halcon_ref import (
    LANGS,
    REFERENCES,
    DocError,
    Reference,
    Signature,
    detect_lang,
    key,
    param_blocks,
    sections,
)


def cmd_search(ref: Reference, words: Sequence[str]) -> str:
    """名稱與摘要同時含所有關鍵字的前 20 筆；名稱命中者優先、名稱短者優先。"""
    lowered = [w.lower() for w in words]
    hits: dict[str, Signature] = {}
    for s in ref.signatures:
        text = f"{s.name} {s.summary}".lower()
        if s.page not in hits and all(w in text for w in lowered):
            hits[s.page] = s

    def rank(s: Signature) -> tuple[int, int, str]:
        in_name = all(w in s.name.lower() for w in lowered)
        return (0 if in_name else 1, len(s.name), s.name)

    ordered = sorted(hits.values(), key=rank)[:20]
    if not ordered:
        raise DocError(f"search 無結果：{' '.join(words)}")
    return "\n".join(f"{s.name} — {s.summary}" for s in ordered)


def cmd_sig(ref: Reference, name: str) -> str:
    """列出運算子所有簽章與頁面路徑。"""
    out: list[str] = []
    for page in ref.pages(name):
        rows = ref.rows_for(page)
        summary = rows[0].summary if rows else ""
        out.append(f"# {Path(page).stem} — {summary}")
        out.append(f"# 頁面：{ref.dir / page}")
        out += [r.signature for r in rows]
    return "\n".join(out)


def cmd_params(ref: Reference, name: str, wanted: Sequence[str]) -> str:
    """輸出指定參數的原文段落；未指定時輸出整段 Parameters。"""
    out: list[str] = []
    for page in ref.pages(name):
        body = sections(ref.read_page(page)).get("Parameters", "")
        if not wanted:
            out.append(body)
            continue
        blocks = param_blocks(body)
        by_key = {key(p): text for p, text in blocks.items()}
        for param in wanted:
            text = by_key.get(key(param))
            if text is None:
                raise DocError(
                    f"{Path(page).stem} 沒有參數「{param}」（有：{', '.join(blocks)}）"
                )
            out.append(text)
    return "\n\n".join(out)


def cmd_section(ref: Reference, name: str, title: str) -> str:
    """輸出標題以 ``title`` 開頭（不分大小寫）的段落。"""
    out: list[str] = []
    for page in ref.pages(name):
        body = sections(ref.read_page(page))
        match = [t for t in body if t.lower().startswith(title.lower())]
        if not match:
            raise DocError(
                f"{Path(page).stem} 沒有段落「{title}」（有：{', '.join(body)}）"
            )
        out.append(f"## {match[0]}\n\n{body[match[0]]}")
    return "\n\n".join(out)


def cmd_class(ref: Reference, name: str) -> str:
    """列出 .NET 類別的建構子與方法（依方法名去重）。"""
    if ref.lang != "dotnet":
        raise DocError("class 只適用於 dotnet")
    wanted = key(name)
    classes = [s for s in ref.signatures if s.kind == "class" and key(s.name) == wanted]
    if not classes:
        raise DocError(f"查無類別「{name}」。{ref.suggest(name)}")
    cls = classes[0].name
    members = [s for s in ref.signatures if s.owner == cls]
    out = [f"# {cls} — {classes[0].summary}", "", "## Constructors"]
    out += [f"{s.signature}" for s in members if s.kind == "constructor"]
    out += ["", "## Methods"]
    seen: set[str] = set()
    for s in sorted(members, key=lambda s: s.name):
        if s.kind == "method" and s.name not in seen:
            seen.add(s.name)
            out.append(f"{s.name} — {s.summary}")
    return "\n".join(out)


def build_parser() -> argparse.ArgumentParser:
    """建立命令列解析器。"""
    parser = argparse.ArgumentParser(prog="halcon_doc.py", description=__doc__)
    parser.add_argument("--lang", choices=LANGS, default=None)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("search").add_argument("words", nargs="+")
    sub.add_parser("sig").add_argument("name")
    params_p = sub.add_parser("params")
    params_p.add_argument("name")
    params_p.add_argument("params", nargs="*")
    section_p = sub.add_parser("section")
    section_p.add_argument("name")
    section_p.add_argument("title")
    sub.add_parser("class").add_argument("name")
    sub.add_parser("check").add_argument("files", nargs="+", type=Path)
    return parser


def run(argv: Sequence[str], root: Path = REFERENCES, cwd: Path | None = None) -> str:
    """執行子命令並回傳輸出文字。

    :raises DocError: 查詢失敗時。
    """
    args = build_parser().parse_args(argv)
    if args.command == "check":
        return halcon_check.run_check(args.files, root, args.lang, cwd or Path.cwd())
    lang = args.lang or detect_lang(cwd or Path.cwd())
    ref = Reference(root, lang)
    if args.command == "search":
        return cmd_search(ref, args.words)
    if args.command == "sig":
        return cmd_sig(ref, args.name)
    if args.command == "params":
        return cmd_params(ref, args.name, args.params)
    if args.command == "section":
        return cmd_section(ref, args.name, args.title)
    return cmd_class(ref, args.name)


def main(argv: Sequence[str] | None = None) -> int:
    """程式進入點：成功回傳 0，查詢失敗回傳 1。"""
    # Windows 主控台預設編碼可能無法輸出中文與特殊符號
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    try:
        print(run(sys.argv[1:] if argv is None else argv))
    except DocError as error:
        print(f"錯誤：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 執行測試確認通過**

Run: `uv run pytest tests/test_halcon_doc.py -v`
Expected: 17 passed

- [ ] **Step 5: 確認編碼測試真的有保護作用**

暫時把 `main()` 中的 `if hasattr(stream, "reconfigure"):` 改成 `if False:`，執行
`uv run pytest tests/test_halcon_doc.py -k non_utf8 -v`，Expected: FAIL（`UnicodeEncodeError`）。
改回原樣後再跑一次，Expected: PASS。

- [ ] **Step 6: Lint 並 commit**

```bash
uv run ruff format skill_template tests && uv run ruff check . && uv run ruff check --target-version py310 skill_template
git add skill_template/scripts/halcon_doc.py tests/test_halcon_doc.py
git commit -m "feat: 新增 skill 查詢命令列工具
--- feat ---
1. 新增 search、sig、params、section、class 子命令
2. 新增 check 子命令串接程式碼檢查
3. 新增依專案檔案推斷語言與 UTF-8 輸出
--- test ---
1. 新增查詢子命令與獨立執行測試"
```

---

### Task 5: SKILL.md 與各語言陷阱清單

**Files:**
- Create: `skill_template/SKILL.md`
- Create: `skill_template/pitfalls/dotnet.md`
- Create: `skill_template/pitfalls/python.md`
- Create: `skill_template/pitfalls/hdevelop.md`
- Test: `tests/test_skill_template.py`

**Interfaces:**
- Consumes: Task 4 的 `halcon_doc.build_parser()`（測試確認 SKILL.md 涵蓋所有子命令）
- Produces: skill 本文；SKILL.md 以 `$HDOC <子命令>` 形式列出每個子命令；指向 `pitfalls/<lang>.md`

- [ ] **Step 1: 寫失敗的測試 `tests/test_skill_template.py`**

檔案 `tests/test_skill_template.py`：

```python
"""skill 範本（SKILL.md 與陷阱清單）的結構測試。"""

import re

import pytest

from . import skill_scripts

import halcon_doc  # noqa: E402  # isort: skip

SKILL_MD = skill_scripts.TEMPLATE / "SKILL.md"


def _frontmatter() -> dict[str, str]:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "SKILL.md 必須以 YAML frontmatter 開頭"
    pairs = (line.split(":", 1) for line in match[1].splitlines())
    return {k.strip(): v.strip() for k, v in pairs}


def test_frontmatter_has_name_and_trigger_description() -> None:
    meta = _frontmatter()
    assert meta["name"] == "halcon"
    assert meta["description"].startswith("Use when")
    assert len(meta["description"]) <= 1024


def test_skill_md_is_short_enough_to_load() -> None:
    assert len(SKILL_MD.read_text(encoding="utf-8").splitlines()) <= 200


def test_skill_md_documents_every_subcommand() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    parser = halcon_doc.build_parser()
    sub = next(a for a in parser._actions if a.dest == "command")
    for command in sub.choices:
        assert f"$HDOC {command}" in text, command


@pytest.mark.parametrize("lang", ["dotnet", "python", "hdevelop"])
def test_pitfalls_have_30_to_60_numbered_items(lang: str) -> None:
    path = skill_scripts.TEMPLATE / "pitfalls" / f"{lang}.md"
    assert f"pitfalls/{lang}.md" in SKILL_MD.read_text(encoding="utf-8")
    items = re.findall(r"^\d+\. ", path.read_text(encoding="utf-8"), re.MULTILINE)
    assert 30 <= len(items) <= 60
```

- [ ] **Step 2: 執行測試確認失敗**

Run: `uv run pytest tests/test_skill_template.py -v`
Expected: FAIL，`FileNotFoundError`（SKILL.md 不存在）

- [ ] **Step 3: 建立 `skill_template/SKILL.md`**

檔案 `skill_template/SKILL.md`：

```markdown
---
name: halcon
description: Use when writing, reviewing, or debugging code that calls MVTec HALCON (HalconDotNet / HOperatorSet / HImage, Python `halcon` package, or HDevelop .hdev scripts). Look up operators and verify signatures against the bundled HALCON 26.05 reference before writing calls.
---

# HALCON 26.05 程式撰寫

本 skill 附帶 HALCON 26.05 Operator Reference（HDevelop / .NET / Python 三種語言），
以及查詢與檢查工具 `scripts/halcon_doc.py`。HALCON 有兩千多個運算子，名稱、參數順序、
字串參數值都很容易記錯，**一律以本文件為準，不憑記憶撰寫**。

## 鐵則

1. 寫出任何 HALCON 呼叫前，先以 `sig` 取得該語言的正確簽章。
2. 字串參數（例如 `'use_polarity'`）、單位（多數角度為弧度 `angle.rad`，少數為度數
   `angle.deg`）、預設值不確定時，以 `params` 查證。
3. 程式寫完後執行 `check`，逐條處理警告。
4. 文件版本為 **26.05**。若專案使用其他版本（看 NuGet 套件版本、`halcon` 套件版本或
   `.hdev` 的 `halcon_version`），提醒使用者簽章可能不同。
5. 查不到的運算子就是不存在，不要自行發明；改用 `search` 找替代品並告知使用者。

## 查詢工具

以下 `$HDOC` 代表 `python .claude/skills/halcon/scripts/halcon_doc.py`
（Windows 可用 `py -3`；需要 Python 3.10 以上，只用標準函式庫）。

| 指令 | 用途 |
|---|---|
| `$HDOC search <關鍵字…>` | 不知道用哪個運算子時，以名稱與摘要搜尋（前 20 筆） |
| `$HDOC sig <名稱>` | 列出所有簽章與頁面路徑（.NET 含 `HOperatorSet` 與各類別多載） |
| `$HDOC params <名稱> [參數…]` | 參數型別、Default、List of values、Suggested values |
| `$HDOC section <名稱> <段落>` | 讀其他段落，段落名可只給開頭（不分大小寫） |
| `$HDOC class <HClass>` | .NET 類別的建構子與方法清單 |
| `$HDOC check <檔案…>` | 檢查程式碼中的 HALCON 呼叫 |

- 名稱可用任何寫法：`FindShapeModel`、`find_shape_model`、`HOperatorSet.FindShapeModel` 都可以。
- 語言由目前目錄推斷（`*.csproj` → dotnet、`pyproject.toml` / `*.py` → python、
  `*.hdev` → hdevelop）；無法判斷時會報錯，請在子命令前加 `--lang dotnet|python|hdevelop`。
- `check` 依副檔名判斷語言（`.cs` / `.py` / `.hdev` / `.hdvp`）。
- 常用段落：`Description`、`Parameters`、`Example`、`Result`、`Possible Predecessors`、
  `Possible Successors`、`Alternatives`、`See also`、`Execution Information`。

## 工作流程

1. **找運算子**：不確定時用 `search`，或以 Grep 在
   `.claude/skills/halcon/references/<lang>/INDEX.md` 找分類段落
   （INDEX.md 很大，只 Grep，不要整份讀）。
2. **取簽章**：`sig <名稱>`。依專案風格挑選一種寫法，不要混用：
   - .NET：`HOperatorSet.X(...)`（HDevelop 匯出風格），或物件導向的 `HImage` / `HShapeModel` 方法。
   - Python：`ha.x(...)`；只要單一結果時可用 `_s` 版本（若 `sig` 有列出）。
   - HDevelop：`x (輸入物件 : 輸出物件 : 輸入控制 : 輸出控制)`，呼叫時全部以逗號分隔。
3. **查參數**：凡是字串參數、角度、可為 `'auto'` 的參數，都用 `params` 確認。
   `List of values` 是嚴格列舉；`Suggested values` 只是建議，其他值也可能合法。
4. **查搭配**：`section <名稱> "Possible Successors"` / `"Possible Predecessors"`
   確認前後流程（例如 create → find → clear），`Alternatives` 找替代運算子。
5. **讀範例**：`section <名稱> Example`（範例一律是 HDevelop 語法，需自行轉成目標語言）。
6. **檢查**：`check <檔案>`。每一則警告都回頭用 `sig` / `params` 查證後再決定改或不改：
   - `[unknown-operator]`：名稱錯誤或不存在；HDevelop 的自訂 procedure 會被誤報，可忽略。
   - `[arg-count]`：參數數量不符，通常是漏了輸出參數。
   - `[invalid-value]`：字串值不在 `List of values` 中。
   - `check` 不檢查 .NET 物件導向方法呼叫（例如 `image.FindShapeModel(...)`），
     這類呼叫必須在撰寫時就以 `sig` / `class` 查證。
7. **回報**：完成時列出查證過的運算子，以及 `check` 的結果。

## 語言差異速查

| 項目 | HDevelop | .NET（HOperatorSet） | Python |
|---|---|---|---|
| 名稱 | `find_shape_model` | `FindShapeModel` | `find_shape_model` |
| 輸出 | 參數列尾端的變數 | `out HObject` / `out HTuple` | 函式回傳值（多個時為 tuple） |
| 字串 | `'text'` | `"text"` | `'text'` 或 `"text"` |
| 圖像物件 | iconic 變數 | `HObject` / `HImage` / `HRegion` / `HXLDCont` | `HObject` |
| 控制值 | tuple | `HTuple` | `int` / `float` / `str` / `list` |

## 文件位置與退路

- 頁面：`.claude/skills/halcon/references/<lang>/<snake_case 名稱>.md`
  （三種語言檔名相同，例如 dotnet 的 `FindShapeModel` 在 `find_shape_model.md`）。
- 類別頁（僅 dotnet）：`references/dotnet/HShapeModel.md` 等。
- 簽章表：`references/<lang>/SIGNATURES.tsv`（欄位：name、kind、owner、signature、summary、page）。
- 參數表：`references/<lang>/PARAMS.tsv`（欄位：page、param、direction、type、default、
  list_of_values、suggested_values）。
- **無法執行 Python 時**：以 Grep 搜尋 `SIGNATURES.tsv`（例如 `^FindShapeModel\t`）取得簽章；
  以 Grep 找出頁面中 `^## Parameters` 的行號，再用 Read 加 offset / limit 只讀該段，不要整頁讀。
- 頁面中的 `../assets/…` 圖片連結無效（未打包圖檔）；公式以 LaTeX（`$…$`）閱讀。
- 若 `references/` 下缺少某語言資料夾，代表安裝時未包含該語言。

## 常見陷阱

撰寫前先讀對應語言的陷阱清單（只讀需要的那一份）：

- .NET：`pitfalls/dotnet.md`
- Python：`pitfalls/python.md`
- HDevelop：`pitfalls/hdevelop.md`
```

- [ ] **Step 4: 建立 `skill_template/pitfalls/dotnet.md`**

檔案 `skill_template/pitfalls/dotnet.md`：

```markdown
# .NET（HalconDotNet）常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗，
使用前請以專案實際的 HalconDotNet 版本確認。

## 專案與環境

1. 以 `using HalconDotNet;` 匯入命名空間；組件版本必須與執行環境安裝的 HALCON 版本一致。（經驗）
2. 執行時需要 HALCON 原生函式庫（安裝時設定的 `HALCONROOT` 與 PATH）；只複製
   `halcondotnet.dll` 會在第一次呼叫時失敗。（經驗）
3. 目標平台用 x64，不要用 AnyCPU 搭配「偏好 32 位元」。（經驗）
4. HDevelop 匯出的 C# 程式以 `ho_`（iconic）與 `hv_`（control）為變數前綴，
   延伸既有匯出程式時沿用相同命名。（經驗）

## 呼叫方式

5. `HOperatorSet` 的每個參數都必須傳入，沒有選用參數或預設值；
   預設值請以 `params` 查 `Default`。（文件：各運算子 Signature）
6. 參數順序固定為：輸入物件、輸出物件、輸入控制、輸出控制；輸出一律是 `out`。（文件）
7. 同一功能有 `HOperatorSet` 靜態版與物件導向版（`HImage.X`、`HShapeModel.X`），
   兩者參數列不同（物件導向版少了 `this` 對應的參數），不要把一種的參數列套到另一種。（文件：`sig`）
8. 物件導向版常有兩個多載：`HTuple` 版（可傳多值）與純量版（`double` / `int` / `string`），
   以 `sig` 確認後再選。（文件）
9. 建立模型的運算子在物件導向 API 中通常是建構子，例如 `new HShapeModel(image, ...)`，
   以 `class HShapeModel` 查看。（文件）
10. `HOperatorSet` 的控制參數型別都是 `HTuple`；`double`、`int`、`string` 與其陣列可隱式轉成
    `HTuple`，不需要手動 `new HTuple(...)`。（經驗）

## 記憶體與生命週期

11. `HObject`、`HImage`、`HRegion`、`HXLDCont` 等 iconic 物件包裝非受控記憶體，
    用 `using` 或明確 `Dispose()` 釋放；大量影像處理時只靠 GC 會造成記憶體暴增。（經驗）
12. 以 `out HObject` 重複輸出到同一個變數前，先 `Dispose()` 舊物件
    （HDevelop 匯出程式的寫法：`ho_Image.Dispose(); HOperatorSet.ReadImage(out ho_Image, ...)`）。（經驗）
13. 迴圈中產生的中間物件（例如每張影像的 `ReduceDomain` 結果）要在迴圈內釋放。（經驗）
14. Handle（模型、量測物件、檔案等）在所有參考被覆寫後會自動清除；需要在特定時間釋放時
    呼叫 `ClearHandle` 或專用的 `ClearShapeModel` 等運算子。（文件：clear_handle）
15. 呼叫 `ClearShapeModel` 之後該 handle 立即失效，不能再使用。（文件：clear_shape_model）
16. `HShapeModel` 等 handle 類別本身也實作 `IDisposable`。（經驗）

## HTuple

17. 讀取單一值用 `.D`（double）、`.I`（int）、`.L`（long）、`.S`（string）；
    陣列用 `.DArr`、`.IArr`、`.LArr`、`.SArr`；長度用 `.Length`。（經驗）
18. 型別不符（例如實際是 double 卻讀 `.I`）會拋例外；不確定時先查 `.Type`，
    或用 `params` 看輸出參數型別。（經驗）
19. `HTuple` 索引從 0 開始，但 `SelectObj` 等 iconic 物件索引從 1 開始。（文件：select_obj）
20. 找不到結果時輸出 `HTuple` 長度為 0（例如 `FindShapeModel` 沒有匹配），
    讀 `[0]` 之前先檢查 `.Length`。（經驗）
21. 多值輸出（例如多個匹配的 Row / Column / Angle / Score）同索引對應同一個結果。（文件）
22. 串接 tuple 用 `TupleConcat`（文件：tuple_concat）；`HTuple` 的 `+` 是逐元素相加
    （對應 `TupleAdd`），不是串接。（經驗）

## 座標、角度與單位

23. 座標順序是 (Row, Column) = (y, x)，與 `System.Drawing.Point(x, y)` 相反。（文件）
24. 大多數角度參數是弧度（參數標頭顯示 `angle.rad`），但也有度數參數（`angle.deg`，
    例如 `RotateImage` 的 `phi`）；一律看 `params` 的標頭再決定單位。（文件：rotate_image）
25. 度與弧度轉換用 `HTuple.TupleRad` / `TupleDeg` 或 `Math.PI / 180`。（文件：tuple_rad）
26. 像素座標以像素中心為整數座標，左上角像素中心為 (0, 0)。（經驗）

## 字串參數

27. 字串參數值必須完全一致（大小寫、底線），先以 `params` 查 `List of values`；
    `check` 會標出不在 `List of values` 內的字串常值。（文件）
28. `'auto'` 只能用在文件列出 `'auto'` 的參數。（文件）
29. 泛用參數（`genParamName` / `genParamValue`）以兩個等長 tuple 成對傳入；
    可用的名稱列在該運算子的 Parameters 或 Description 段落。（文件）

## 顯示與執行緒

30. WinForms / WPF 用 `HSmartWindowControl`（或 WPF 版本）顯示，透過 `.HalconWindow`
    取得 `HWindow`；UI 相關呼叫必須在 UI 執行緒。（經驗）
31. `DispObj` 前以 `SetPart` 設定顯示範圍，否則影像可能只顯示一部分。（文件：set_part）
32. 運算子的執行緒安全等級看 `section <名稱> "Execution Information"`；
    標示為 exclusive 的運算子不能與其他運算子平行執行。（文件）

## 錯誤處理

33. 運算子錯誤以例外拋出（`HOperatorException`，基底 `HalconException`），
    可用 `GetErrorCode()` 取得錯誤碼；不要以空的 `catch` 吞掉。（經驗）
34. 模型檔（例如 `.shm`）由較新版本 HALCON 寫出時，舊版可能讀不回來。（經驗）
35. `ReadImage` 會搜尋 `image_dir` 系統參數的路徑，也會自動嘗試補副檔名；
    路徑錯誤時錯誤訊息只會說找不到檔案。（文件：read_image）
```

- [ ] **Step 5: 建立 `skill_template/pitfalls/python.md`**

檔案 `skill_template/pitfalls/python.md`：

```markdown
# Python（halcon 套件）常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗，
使用前請以專案實際的 `halcon` 套件版本確認。

## 環境與匯入

1. 慣用匯入方式為 `import halcon as ha`；`check` 只認得 `import halcon` 與
   `import halcon as <別名>`，不支援 `from halcon import ...`。（經驗）
2. PyPI 套件版本必須對應已安裝的 HALCON 版本（26.05），並需要 HALCON 原生函式庫
   在執行環境中可被找到。（經驗）
3. 運算子是模組層級函式，名稱為 snake_case：`ha.read_image(...)`、`ha.find_shape_model(...)`。（文件）
4. Python 版本不含 `dev_*` 運算子（那些只存在於 HDevelop）；顯示用 `open_window`、
   `disp_obj` 等一般運算子。（文件：python/ 下無 dev_*.md）

## 呼叫與回傳

5. 函式參數只有輸入參數（輸入物件與輸入控制）；輸出參數全部由回傳值取得。（文件：Signature）
6. 只有一個輸出時直接回傳；多個輸出時回傳 tuple，順序與 `sig` 的回傳型別相同，
   解構時數量要一致。（文件）
7. 所有參數都沒有預設值，必須全部傳入；預設值請以 `params` 查 `Default`。（文件：Signature）
8. 可以用關鍵字參數（名稱為文件中的 snake_case 參數名，例如 `num_levels=0`）提高可讀性。（文件）
9. 控制輸出通常是 `Sequence[...]`（list）；部分運算子另有 `_s` 版本回傳單一值，
   以 `sig` 查看是否存在，不要自行在名稱後加 `_s`。（文件）
10. `MaybeSequence[T]` 參數可傳單一值或 list。（文件）
11. 物件輸出（`HObject`）可能包含多個物件，用 `ha.count_obj` 取得數量，
    `ha.select_obj` 取出單一物件，索引從 1 開始。（文件：select_obj）
12. 找不到結果時回傳空 list（例如 `find_shape_model` 沒有匹配），取 `[0]` 前先檢查長度。（經驗）
13. 多值輸出（Row / Column / Angle / Score）同索引對應同一個結果，可用 `zip` 一起走訪。（文件）

## 型別與資料

14. `HObject` 不是 numpy 陣列；需要像素資料時以套件提供的轉換函式
    （例如 `ha.himage_as_numpy_array` / `ha.himage_from_numpy_array`，不在本文件中，
    使用前確認套件版本）轉換。（經驗）
15. 不要用 `get_grayval` 逐點迴圈讀取像素，速度很慢；改用整張影像的運算子或 numpy 轉換。（經驗）
16. Handle 參數型別為 `HHandle`；不要把 handle 轉成 int 保存。（文件：Signature）
17. Handle 在所有參考消失後自動清除；需要立即釋放時呼叫 `ha.clear_handle` 或專用的
    `ha.clear_shape_model` 等運算子，之後該 handle 失效。（文件：clear_handle、clear_shape_model）
18. tuple 運算（`tuple_*` 運算子）在 Python 中通常直接用原生 list 與 `math` 即可，
    不必逐一呼叫 `ha.tuple_*`。（經驗）
19. 字串參數直接傳 Python 字串，不需要額外加引號（寫 `'use_polarity'`，不是 `"'use_polarity'"`）。（經驗）

## 座標、角度與單位

20. 座標順序是 (row, column) = (y, x)；與 numpy 陣列索引 `arr[row, col]` 一致，
    但與 OpenCV / PIL 的 (x, y) 相反。（文件）
21. 大多數角度是弧度（參數標頭 `angle.rad`），少數是度數（`angle.deg`，例如 `rotate_image`
    的 `phi`）；以 `params` 查看標頭。弧度轉換用 `math.radians`。（文件：rotate_image）
22. 像素座標以像素中心為整數座標。（經驗）

## 字串參數

23. 字串值必須完全一致，先以 `params` 查 `List of values`；`check` 會標出不合法的字串常值。（文件）
24. `Suggested values` 不是完整清單，其他值可能也合法；有疑慮時讀 Description。（文件）
25. 泛用參數（`gen_param_name` / `gen_param_value`）以兩個等長 list 成對傳入。（文件）

## 錯誤處理與效能

26. 運算子錯誤以例外拋出（`ha.HOperatorError`，名稱以套件版本為準）；
    捕捉特定例外，不要用裸 `except Exception:` 吞掉。（經驗）
27. 模型建立（例如 `create_shape_model`）很耗時，應只建立一次並重複使用，或以
    `write_shape_model` / `read_shape_model` 保存。（文件）
28. 平行執行前以 `section <名稱> "Execution Information"` 確認執行緒安全等級。（文件）
29. `read_image` 會搜尋 `image_dir` 系統參數並自動嘗試補副檔名。（文件：read_image）
30. HDevelop 範例（`section <名稱> Example`）的參數順序是「輸入…輸出」混在一起，
    轉成 Python 時要把輸出參數移到回傳值。（文件）
```

- [ ] **Step 6: 建立 `skill_template/pitfalls/hdevelop.md`**

檔案 `skill_template/pitfalls/hdevelop.md`：

```markdown
# HDevelop 常見陷阱

來源標示：「文件」表示可在 `references/` 查證；「經驗」表示本文件未收錄的一般使用經驗。

## 呼叫語法

1. 簽章格式為 `op (輸入物件 : 輸出物件 : 輸入控制 : 輸出控制)`；在程式中呼叫時
   所有參數依同樣順序以逗號分隔，例如 `threshold (Image, Region, 128, 255)`。（文件：Signature）
2. 所有參數都必須傳入，沒有預設值；預設值以 `params` 查 `Default`。（文件）
3. 輸出參數位置必須是變數，不能是常值或運算式。（經驗）
4. 運算子名稱與括號之間慣例有一個空白（`read_image (Image, 'fabrik')`）。（經驗）

## 字串、tuple 與運算式

5. 字串只能用單引號 `'text'`；雙引號不是字串。（經驗）
6. 字串中的反斜線要跳脫（`'C:\\images'`），路徑建議用 `/`。（經驗）
7. 指派用 `:=`；相等比較用 `==`，不等用 `!=`（或 `#`）。（經驗）
8. tuple 以 `[a, b, c]` 建立與串接（`[T1, T2]`），`[]` 是空 tuple。（經驗）
9. tuple 索引從 0 開始（`T[0]`），長度用 `|T|`；但 `select_obj` 等 iconic 物件索引從 1 開始。
   （文件：select_obj）
10. 兩個整數相除得到整數（`5 / 2` 為 2）；需要小數時寫成 `5.0 / 2`。（經驗）
11. tuple 與單一值做算術時會逐元素運算；兩個長度不同（且都大於 1）的 tuple 做運算會出錯。（經驗）
12. 角度函式：`rad(90)`、`deg(3.14)`。（經驗）

## 控制流程

13. 區塊語法：`if (...)` … `elseif (...)` … `else` … `endif`；
    `for I := 0 to N - 1 by 1` … `endfor`；`while (...)` … `endwhile`。（經驗）
14. 例外處理：`try` … `catch (Exception)` … `endtry`；錯誤碼用 `dev_get_exception_data`
    或 `Exception[0]` 取得。（文件：dev_get_exception_data）
15. 以 `*` 開頭的行是註解。（經驗）
16. 自訂 procedure 的呼叫語法與運算子相同；`check` 會把 `.hdev` 內定義的 procedure 排除，
    但外部 procedure（`.hdvp`）會被報為 `[unknown-operator]`，可忽略。（經驗）

## dev_* 運算子

17. `dev_*` 運算子只在 HDevelop 環境有效；匯出成 C# / Python 時會被省略或改寫，
    不要讓程式邏輯依賴它們。（文件：dev_* 頁面）
18. 批次處理時在程式開頭關閉畫面更新：`dev_update_window ('off')`、`dev_update_var ('off')`、
    `dev_update_pc ('off')`，避免每一步都更新而變慢（文件：dev_update_window 等）；
    常見的 `dev_update_off ()` 是包裝這三者的程序庫 procedure，不是運算子。（經驗）
19. 顯示用 `dev_display`，設定顏色與繪製方式用 `dev_set_color`、`dev_set_draw`。（文件）
20. 需要可匯出的顯示程式時，改用 `open_window` / `disp_obj` 等一般運算子。（文件）

## 物件與記憶體

21. iconic 變數可能包含多個物件，用 `count_obj` 取得數量、`select_obj` 取出單一物件。（文件）
22. 空物件用 `gen_empty_obj`，累加物件用 `concat_obj`。（文件）
23. Handle 在所有參考被覆寫後會自動清除；需要立即釋放時用 `clear_handle` 或
    `clear_shape_model` 等專用運算子，之後 handle 失效。（文件：clear_handle）
24. `reduce_domain` 只改變影像的定義域，不裁切影像；需要實際裁切時用 `crop_domain`。（文件）

## 座標、角度與單位

25. 座標順序是 (Row, Column) = (y, x)。（文件）
26. 大多數角度參數是弧度（`angle.rad`），少數是度數（`angle.deg`，例如 `rotate_image` 的
    `Phi`）；以 `params` 查看參數標頭。（文件：rotate_image）
27. 像素座標以像素中心為整數座標，左上角像素中心為 (0, 0)。（經驗）

## 字串參數

28. 字串值必須完全一致，先以 `params` 查 `List of values`；`check` 會標出不合法的字串常值。（文件）
29. `'auto'` 只能用在文件列出 `'auto'` 的參數。（文件）
30. `Suggested values` 不是完整清單；泛用參數（`GenParamName` / `GenParamValue`）以兩個
    等長 tuple 成對傳入。（文件）

## 檔案

31. `.hdev` 是 XML，程式行包在 `<l>…</l>` 中，`<` `>` 會被寫成 `&lt;` `&gt;`；
    直接編輯 XML 時要保持跳脫。（經驗）
32. `read_image` 會搜尋 `image_dir` 系統參數並自動嘗試補副檔名。（文件：read_image）
```

- [ ] **Step 7: 查證陷阱清單中標示「文件」的運算子都存在**

Run:
```bash
for op in clear_handle clear_shape_model select_obj rotate_image tuple_concat tuple_rad set_part read_image dev_get_exception_data dev_update_window dev_update_var dev_update_pc crop_domain gen_empty_obj concat_obj count_obj write_shape_model; do
  test -f output/hdevelop/$op.md || echo "缺少 $op"
done
grep -q "angle.deg" output/hdevelop/rotate_image.md && echo "rotate_image 為度數 OK"
```
Expected: 只輸出 `rotate_image 為度數 OK`

- [ ] **Step 8: 執行測試確認通過**

Run: `uv run pytest tests/test_skill_template.py -v`
Expected: 6 passed

- [ ] **Step 9: Commit**

```bash
git add skill_template/SKILL.md skill_template/pitfalls tests/test_skill_template.py
git commit -m "feat: 新增 HALCON skill 說明與各語言陷阱清單
--- feat ---
1. 新增 SKILL.md 觸發描述、鐵則與查詢流程
2. 新增 dotnet、python、hdevelop 陷阱清單
--- test ---
1. 新增 SKILL.md 與陷阱清單結構測試"
```

---

### Task 6: 完整產生、Spec 同步與手動驗收

**Files:**
- Modify: `docs/superpowers/specs/2026-09-30-halcon-skill-design.md`

**Interfaces:**
- Consumes: Task 1–5 全部成果、實際 `output/`
- Produces: `dist/skill/halcon/`（不進版本控管）

- [ ] **Step 1: 把「與 Spec 的差異」寫回 spec**

在 spec 修改：
- §3 產出樹：`scripts/halcon_doc.py` 改為 `scripts/halcon_ref.py`、`scripts/halcon_check.py`、`scripts/halcon_doc.py` 三行。
- §4.1 步驟 3 補上「複製時把 U+00A0 換成一般空白」；步驟 1 補上「`--out` 已存在但沒有 `SKILL.md` 時拒絕覆寫」。
- §4.2 刪除「類別頁另外為 Constructors、Methods…」那段，改為「類別頁只產生一列 `kind=class`；`class` 子命令使用運算子頁中 `owner=<類別>` 的 `method` / `constructor` 列」。`kind` 欄說明改為 `operator` / `method` / `constructor` / `class`。
- §4.3 第一欄 `name` 改為 `page`（說明：頁面檔名；Python `_s` 版本與原版共用）。
- §5.3 補一行「語言優先依副檔名判斷（`.cs` / `.py` / `.hdev` / `.hdvp`），否則用專案推斷」。
- §6.3 補一行「每條標示來源：文件 / 經驗」。
- 標頭「狀態」改為「已實作」。

- [ ] **Step 2: 全部測試與 lint**

Run: `uv run pytest -m "not browser" -q && uv run ruff check . && uv run ruff format --check . && uv run ruff check --target-version py310 skill_template`
Expected: 全部通過（原型為 140 passed，含既有測試）

- [ ] **Step 3: 以完整 output 產生 skill**

Run: `uv run halcon-doc-skills build-skill`
Expected（原型實測）：
```
hdevelop：2536 頁、2313 運算子、0 類別、2313 簽章、9826 參數、0 解析失敗
dotnet：2557 頁、2235 運算子、99 類別、6214 簽章、9718 參數、0 解析失敗
python：2458 頁、2235 運算子、0 類別、2697 簽章、9718 參數、0 解析失敗
```
exit code 0；`du -sh dist/skill/halcon` 約 50M。

- [ ] **Step 4: 產出的腳本冒煙測試**

Run:
```bash
H="python3 dist/skill/halcon/scripts/halcon_doc.py"
$H --lang dotnet sig FindShapeModel | head -3
$H --lang python search shape model find | head -3
$H --lang hdevelop params find_shape_model SubPixel
$H --lang dotnet class HShapeModel | head -5
$H --lang python sig find_shap_model; echo "exit=$?"
```
Expected：第一個列出 `static void HOperatorSet.FindShapeModel(`；search 第一筆為 `find_shape_model — …`；params 只印 `SubPixel` 段；class 列出 `public HShapeModel(`；最後一個印出「相近名稱：find_shape_model, …」且 `exit=1`。

- [ ] **Step 5: 手動驗收（需使用者參與）**

1. 建一個測試專案資料夾（含一個 `.csproj`），把 `dist/skill/halcon/` 複製到 `<專案>/.claude/skills/halcon/`。
2. 在該專案開 Claude Code，請 Agent「用 HOperatorSet 寫一段讀圖、建立 shape model、搜尋並輸出位置的 C# 程式」。
3. 確認 Agent 有載入 halcon skill、執行 `sig` / `params`，最後執行 `check` 且結果為 `OK`。
4. 另建一個含 `pyproject.toml` 的專案，以 Python 重複一次。
5. 把觀察結果（是否有跳過查詢、`check` 誤報）回報，必要時調整 SKILL.md 或 `check` 規則。

- [ ] **Step 6: Commit spec 同步**

```bash
git add docs/superpowers/specs/2026-09-30-halcon-skill-design.md
git commit -m "docs: 同步 HALCON skill 設計文件與實作差異
--- docs ---
1. 更新 PARAMS 欄位、類別列與腳本拆分說明
2. 補充不換行空白正規化與覆寫保護"
```
