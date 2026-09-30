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
