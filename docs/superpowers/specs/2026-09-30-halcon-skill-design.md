# HALCON 程式撰寫 Skill 設計文件

日期：2026/09/30
狀態：待使用者審閱

## 1. 目標與範圍

### 目標
把 `output/` 中的 HALCON 26.05 文件（HDevelop、.NET、Python）包成一個 Claude Code skill，讓 Agent 撰寫 HALCON 程式時先查文件再寫呼叫，並在寫完後自動檢查，降低捏造運算子、參數順序錯、漏 `out` 參數、字串參數值錯誤等問題。

### 範圍
- 三種語言皆支援，skill 依專案自動判斷語言，也可明確指定。
- skill 部署在**專案層級**（目標專案的 `.claude/skills/halcon/`）。
- 本 repo 新增 `build-skill` 子命令，產生完整 skill 到 `dist/skill/halcon/`；使用者**手動複製**到目標專案。
- skill 附一支純標準函式庫的 Python 查詢腳本 `halcon_doc.py`（Python 3.10+）。

### 非目標（YAGNI）
- 不做自動安裝到專案、不做 `.gitignore` 管理。
- 不打包 `output/assets/`（公式已轉 LaTeX，其餘圖檔對寫程式幫助有限）。
- 不支援 HALCON 26.05 以外版本。
- `check` 不做自動修正、不做 .NET 物件導向多載的參數數量解析。

## 2. 文件觀察（設計依據）

- 三個語言資料夾各約 2,500 頁、15MB；`INDEX.md` 約 242KB（3,109 行），不可整份載入。
- **檔名三語言一致為 snake_case**（如 `dotnet/find_shape_model.md` 內標題為 `FindShapeModel`）。類別頁（如 `HShapeModel.md`）只存在於 dotnet。
- 運算子頁段落固定：`## Name`、`## Signature`、`## Description`、`## Execution Information`、`## Parameters`、`## Example (HDevelop)`、`## Result`、`## Possible Predecessors`、`## Possible Successors`、`## Alternatives`、`## See also`、`## Module`。
- `## Name` 格式：`` `名稱` — 一句話摘要 ``。
- `## Signature` 每個簽章是一行反引號字串；dotnet 一個運算子有多個簽章（`static void HOperatorSet.X(...)` 以及 `void HClass.X(...)` 多載）。
- `## Parameters` 中每個參數以 `` **`name`** (direction)  semantic_type `→` type `` 開頭，其後的屬性為「標籤行 + 值行」：
  - 出現次數（三語言合計）：`Default:` 10,620、`Suggested values:` 5,418、`List of values:` 3,175、`Restriction:` 2,354、`Value range:` 2,301。
  - **只有 `List of values` 是嚴格列舉**；`Suggested values` 僅為建議。
- 類別頁有 `## Constructors`、`## Methods` 表格，每列 `` | `名稱` |  | 摘要 | ``。
- 頁內 `../assets/…` 圖片連結在 skill 中會失效（不打包 assets）。

## 3. 架構與目錄結構

### 本 repo（產生端）
```
src/halcon_doc_skills/
  signatures.py      # 新增：解析 output/<lang>/*.md 產生 SIGNATURES / PARAMS
  skill_build.py     # 新增：組出 dist/skill/halcon/
  cli.py             # 新增子命令 build-skill
skill_template/      # 手寫、版本控管的 skill 原始檔
  SKILL.md
  scripts/halcon_doc.py
  pitfalls/hdevelop.md
  pitfalls/dotnet.md
  pitfalls/python.md
```

### 產出（`uv run halcon-doc-skills build-skill`）
```
dist/skill/halcon/
  SKILL.md
  scripts/halcon_doc.py
  pitfalls/<lang>.md
  references/<lang>/
    SIGNATURES.tsv
    PARAMS.tsv
    INDEX.md
    *.md             # 原始運算子/類別/目錄頁
```

- 使用者可刪除不需要的 `references/<lang>/` 與 `pitfalls/<lang>.md` 以縮小體積；腳本與 `SKILL.md` 對缺少的語言須能正常處理（`halcon_doc.py` 回報「此語言未安裝」）。
- `dist/` 已在 `.gitignore` 中，不進版本控管。

## 4. 資料產生流程（`build-skill`）

### 4.1 步驟
1. 清空並建立 `dist/skill/halcon/`（`--out` 可改路徑）。
2. 複製 `skill_template/` 全部內容。
3. 對每種語言：複製 `output/<lang>/*.md` 到 `references/<lang>/`，並以 `signatures.py` 產生兩份 TSV。
4. 印出每種語言的統計：頁數、簽章列數、參數列數、解析失敗頁面清單。
5. 任一語言的運算子頁解析失敗率 > 1% 時以 exit code 1 結束。

目錄頁（`toc_*.md`）、`INDEX.md` 及其他非運算子/類別頁不解析，只複製。

### 4.2 `SIGNATURES.tsv`
UTF-8、tab 分隔、首行為欄名。一個簽章一列。

| 欄位 | 說明 |
|---|---|
| `name` | 該語言的名稱（`FindShapeModel` / `find_shape_model`） |
| `kind` | `operator` 或 `class` |
| `owner` | dotnet：`HOperatorSet` 或類別名（如 `HShapeModel`）；其他語言與類別列留空 |
| `signature` | 簽章原文（去掉反引號）；類別列留空 |
| `summary` | `## Name` 的一句話摘要 |
| `page` | 頁面檔名（如 `find_shape_model.md`） |

類別頁另外為 `## Constructors`、`## Methods` 中每個名稱產生一列：`kind=method`（或 `constructor`）、`owner=類別名`、`signature` 留空，供 `class` 與 `check` 使用。

### 4.3 `PARAMS.tsv`
一個運算子的一個參數一列（以該語言的參數名為準）。

| 欄位 | 說明 |
|---|---|
| `name` | 運算子名稱 |
| `param` | 參數名 |
| `direction` | `input_object` / `input_control` / `output_object` / `output_control` |
| `type` | `→` 後的型別字串 |
| `default` | `Default:` 值，無則空 |
| `list_of_values` | `List of values:` 值，以 ` \| ` 分隔 |
| `suggested_values` | `Suggested values:` 值，以 ` \| ` 分隔 |

### 4.4 轉義
欄位內的 tab 與換行一律換成單一空白；多值欄位內部以 ` | ` 分隔（原值逗號分隔的清單拆開後再接合）。

## 5. 查詢腳本 `halcon_doc.py`

### 5.1 共通行為
- 以腳本所在位置推得 `references/` 路徑，不依賴目前工作目錄。
- `--lang {hdevelop,dotnet,python}`；未指定時由目前目錄推斷：有 `*.csproj` → dotnet；有 `pyproject.toml` 或 `*.py` → python；有 `*.hdev` → hdevelop；皆無或多種並存 → 報錯要求指定。推斷只看目前目錄與往下兩層。
- **名稱正規化**：去掉 `HOperatorSet.`、`ho.`、類別前綴後，PascalCase 轉 snake_case 再比對 `page` 或 `name`，因此 `FindShapeModel`、`find_shape_model`、`HOperatorSet.FindShapeModel` 視為同一運算子。
- 查無結果時以 `difflib.get_close_matches` 列出最多 5 個相近名稱，exit code 1。

### 5.2 子命令

| 子命令 | 用途 | 輸出 |
|---|---|---|
| `search <關鍵字…>` | 找運算子 | 名稱與摘要同時含所有關鍵字（不分大小寫）的前 20 筆：`name — summary` |
| `sig <name>` | 取得簽章 | 該運算子所有簽章列 |
| `params <name> [param…]` | 查參數 | 頁面 `## Parameters` 中指定參數的原文段落；未指定參數則輸出整段 |
| `section <name> <段落>` | 讀其他段落 | 指定 `## 段落` 原文（段落名不分大小寫、可只給前綴） |
| `class <HClass>` | 類別成員（僅 dotnet） | 建構子與方法清單：`name — summary` |
| `check <file…>` | 驗證程式碼 | 可疑處清單：`file:line 問題 → 建議` |

### 5.3 `check` 規則（保守、只報高信心問題）
- 抽取呼叫（以正規表示式，不做完整語法分析）：
  - dotnet：僅 `HOperatorSet.X(`。
  - python：`ha.x(` / `halcon.x(`（模組別名由 `import halcon as <alias>` 取得）。
  - hdevelop：行首 `x (`（排除控制流程關鍵字與 `*` 註解行）。
- 檢查項目：
  1. **運算子不存在**：`HOperatorSet`、python、hdevelop 呼叫的名稱不在 SIGNATURES 中 → 警告並附相近名稱。
  2. **參數數量不符**：僅對 `HOperatorSet`、python、hdevelop 呼叫，比對 PARAMS 的參數數量（python 只計 input 參數；hdevelop 與 `HOperatorSet` 計全部）。呼叫跨多行時合併到括號配對為止。
  3. **字串參數值不合法**：參數位置上的字串常值不在該參數的 `list_of_values` 中（`list_of_values` 為空則不檢查）。
  4. **.NET 物件導向方法（`img.FindShapeModel(...)`）不檢查**：以正規表示式無法得知變數型別，名稱也會與一般 .NET 方法混淆，誤報率過高。這類呼叫改由 `SKILL.md` 要求 Agent 以 `sig` / `class` 事先查證。
- 所有結果皆為警告，不修改檔案，exit code 固定為 0；無警告時輸出 `OK: <n> HALCON calls checked`。

## 6. `SKILL.md` 與陷阱文件

### 6.1 Frontmatter
```yaml
name: halcon
description: Use when writing, reviewing, or debugging code that calls MVTec HALCON (HalconDotNet / HOperatorSet / HImage, Python `halcon` package, or HDevelop .hdev scripts). Look up operators and verify signatures against the bundled HALCON 26.05 reference before writing calls.
```

### 6.2 本文（約 150 行以內）
1. **鐵則**：不憑記憶寫任何 HALCON 呼叫，先 `sig`；參數值不確定時查 `params`。文件版本為 26.05，若專案使用其他版本需提醒使用者。
2. **語言判斷與差異對照**：腳本推斷規則；.NET 為 PascalCase 與 `out` 參數、Python 為 snake_case 且多重回傳為 tuple、HDevelop 以 `:` 分隔輸入與輸出參數。
3. **工作流程**：
   1. 不確定用哪個運算子 → `search`，或以 grep 定位 `INDEX.md` 中的分類段落（不整份讀）。
   2. `sig` 取得正確簽章。
   3. `params` 確認字串參數合法值、單位（如角度為 rad）、預設值。
   4. 必要時 `section <op> "Possible Successors"` 查搭配流程（如 create → find → clear）。
   5. 寫完執行 `check <檔案>`；每則警告回頭查文件確認後再決定是否修改。
   6. 回報時列出查過的運算子。
4. **腳本無法執行時的退路**：grep `references/<lang>/SIGNATURES.tsv`；以 grep 找到 `## Parameters` 行號後用 Read 加 offset 讀取，不讀整頁。
5. **注意**：頁面中的圖檔連結不可用，公式以 LaTeX 閱讀。
6. **陷阱**：依語言指向 `pitfalls/<lang>.md`，需要時才讀。

### 6.3 `pitfalls/<lang>.md`
每份 30～60 條，由 Claude 依文件與常見錯誤起草、使用者審閱。涵蓋方向例如：
- dotnet：`HObject` / `HImage` 需 `Dispose` 或 `using`；`HTuple` 取值用 `.D` / `.I` / `.S`；handle 生命週期；`HOperatorSet` 與物件導向 API 混用注意事項。
- python：多重回傳需解構；`HObject` 不是 numpy 陣列；`MaybeSequence` 參數。
- hdevelop：`dev_*` 運算子僅在 IDE 有效；tuple 索引與字串引號規則。

## 7. 錯誤處理
- `build-skill`：`output/<lang>/` 不存在 → 略過該語言並警告；全部不存在 → exit 1。單頁解析失敗 → 記錄後繼續；失敗率 > 1% → exit 1。
- `halcon_doc.py`：語言未安裝、TSV 缺失 → 明確錯誤訊息與 exit 1；`check` 讀檔失敗 → 該檔輸出錯誤，繼續處理其他檔案。

## 8. 測試與驗收

### 自動化（pytest，沿用 `tests/` 與 `tests/fixtures/`）
- `tests/test_signatures.py`：以 `find_shape_model`（三語言）與 `HShapeModel` 精簡 fixture 驗證：dotnet 多載拆成多列、python 單列、`List of values` / `Default` 正確、類別頁產生 method 列。
- `tests/test_halcon_doc.py`：以迷你 `references/` 驗證：名稱正規化、相近名稱建議、`params` 只輸出指定參數、語言推斷（含無法判斷報錯）、`section` 前綴比對、`check` 在三語言各一個正確與錯誤樣本（捏造運算子、參數數量錯、非法字串值），以及 .NET 物件導向呼叫不做數量檢查。
- `tests/test_skill_build.py`：產出目錄結構正確、TSV 欄位正確、失敗率 > 1% 時 exit 1。

### 手動驗收
1. 以完整 `output/` 執行 `build-skill`：每語言簽章列數 ≥ 運算子頁數、失敗率 < 1%。
2. 複製到測試專案，請 Agent 各寫一段 C# 與 Python 的 shape matching 程式，確認其依流程查詢，且 `check` 無警告。
