# HALCON 文件爬取與 Markdown 轉換工具 設計文件

日期：2026/09/30
狀態：待使用者審閱（已加入公式轉 LaTeX：字形解碼為主、latexconvert OCR 為備援）

## 1. 目標與範圍

### 目標
以 Playwright 讀取 `https://www.mvtec.com/doc/halcon/2605/en/index.html` 及其所有連結的文件頁面，轉換為乾淨的 Markdown 並存到本機，供 Claude 當參考資料（skill / 知識庫）使用。公式盡可能還原成 LaTeX 文字，讓 Claude 能直接閱讀。

### 範圍
- 網址範圍：`/doc/halcon/2605/en/` 底下的 `.html` 頁面，不跟隨外部連結。
- 頁面類型：全部轉換（類別頁僅輸出於有內容的語言，見 §2），包含
  - 運算子頁（約 2,314 頁，如 `abs_image.html`）
  - 類別頁（約 100 頁，如 `HBarCode.html`）
  - 目錄頁 `toc_*.html`（約 230 頁）
  - 其他站內頁面（如 `legal_notes.html`、`index_*.html`）
- 語言：只處理 **HDevelop、.NET、Python** 三種，每種語言一個資料夾。C++ 與 C 不處理。
- 圖片：不丟棄，下載到本機。
- 公式：行內 SVG 公式轉成 LaTeX（§5）。優先以 SVG 字形離線解碼；解碼不了的可選用 latexconvert.com 做 OCR 備援；仍失敗則保留圖檔。
- 規模預估：約 2,700 頁 × 3 語言 ≈ 8,100 個 `.md`，外加圖片與公式快取。

### 非目標
- 不處理其他 HALCON 版本或其他語系（`de`、`cn`）。
- 不處理 C++ / C 語言內容。
- 不保證公式的排版語意 100% 等同原圖：字形解碼保證字元正確（且拒絕不確定者），OCR 結果可能有誤（§5.3）。

## 2. 網站觀察（設計依據）

- 頁面為**靜態 HTML**，不需 JS 渲染內容。
- 每頁含 5 個語言分頁（`#syn-hdevelop`、`#syn-dotnet`、`#syn-python`、`#syn-cpp`、`#syn-c`），所有語言內容都在 HTML 內，以 `data-if="<lang>"` 標記並用 inline `display:none` 隱藏；點擊分頁會呼叫 `toggleLanguage('<lang>')` 切換顯示。
- 同一個運算子在不同語言名稱不同（`abs_image` / `AbsImage`），簽名與參數表也各有版本，直接轉換會出現重複文字，因此必須逐語言取「可見內容」。
- 頁面**沒有 `<img>` 檔案**。內容中的圖是行內 SVG，全是公式（MetaPost 產生）。頁首 logo 與頁尾社群圖示也是 SVG，但不在內容區。
- **類別頁只有 .NET / C++ 有內容**：`HBarCode.html` 等類別頁在 HDevelop、Python（與 C）分頁只顯示一句 "Use the tabs on the upper right to switch to a different programming language."，視為空殼頁。
- 不存在的網址回 HTTP 404（不是 200 的錯誤頁），可直接用狀態碼判斷。
- 只有運算子頁含 `<!--OP_REF_HEADER_END-->` 標記；所有頁面都含 `<!--OP_REF_FOOTER_START-->`，其後是頁尾（`<hr>`、版權、社群圖示）。`.tabbar`、`.indexlink`、`.footer` 位於 `.body_main` 內，麵包屑（`.breadcrumb`）在 `.body_main` 外，且其中第一個連結是只有 logo 的空文字連結。
- 語言切換只會改變 `div` / `span` 的 inline `display`，且頁面上帶 `data-if` 的元素只有這兩種標籤。
- 入口 `index.html` 只含約 230 個 `toc_*` 連結；運算子頁需藉由 `index_by_name.html`（約 2,314 個連結）與 `index_classes.html`（約 100 個）及各 `toc_*` 頁取得。
- **公式的結構**（2026/09/30 抽樣 120 個運算子頁）：
  - 約 30% 的頁面含公式；120 頁共 139 個，全站估計約 700 頁、1,100 個公式。
  - 容器為 `<span title="N" class="math|displaymath"><!-- Created by MetaPost … --><svg …>`；`math` 是行內（92 個）、`displaymath` 是獨立（47 個）。`title` 只是公式編號，不含公式文字，頁面也沒有 MathML 或 LaTeX 原始碼。
  - SVG 內每個字元是 `<use xlink:href="#GLYPH<字型>_<字碼>">`，位置由外層 `<g transform="matrix(1.6,0,0,1.6,tx,ty)">` 與 `x` 屬性決定。用到的字型：`cmr10`、`cmmi10/7/5`、`cmsy10/7/5`、`cmex10`、`cmti10`、`cmbx10`、`cmr7/5`、`pcrr8r`（Courier）、`ptmr8r`／`ptmri8r`（Times）。
  - 使用 `viewBox`（大小寫敏感）；寬高以 `em` 表示。
- **latexconvert.com 觀察**：
  - 是給人使用的網頁 OCR 工具（Next.js），支援 JPEG、PNG、GIF、WebP，不支援 SVG；沒有公開 API。
  - 服務條款允許研究與商業使用，禁止「利用、逆向工程或壓垮服務」，並聲明識別結果可能有錯；FAQ 說明後端有按 IP 的基本限流。
  - `robots.txt` 對 `/convert`（頁面內部呼叫的端點）為 Disallow；網頁 `/zh/` 本身為 Allow。
  - 實測：上傳 PNG 後，結果出現在 `textarea.latex-output`。

## 3. 架構

### 元件
| 模組 | 職責 | 依賴 |
|---|---|---|
| `config.py` | 常數：網址範圍、入口頁、語言清單、預設並行數／重試次數／延遲、空殼頁標記文字 | 無 |
| `crawler.py` | 管理待爬佇列：入口為 `index.html`、`index_by_name.html`、`index_classes.html`；網址正規化（去除 `#fragment` 與 query）、範圍過濾、去重 | 無 |
| `extractor.py` | 以 Playwright 開頁（每頁只載入一次），對 3 種語言各點一次分頁，於頁面內取出「可見」的 `.body_main` HTML；同時收集頁內內部連結、`<img>` 網址與麵包屑 | playwright |
| `cache.py` | `PageCache`：讀寫各語言可見 HTML 與頁面中繼資料（標題、麵包屑、連結、圖片網址）、記錄失敗 | 無 |
| `formulas.py` | 公式核心：辨識公式容器、以 SVG 字形解碼 LaTeX（含安全閘）、公式結果快取 `FormulaStore`、Markdown 標記換成 `$…$` | 無 |
| `assets.py` | 行內 SVG 存成 `.svg`（雜湊命名）；公式容器依結果換成標記或圖片；`<img>` 資產命名規則 | formulas |
| `ocr.py` | OCR 備援：SVG 轉 PNG，驅動 latexconvert.com 網頁介面，節流與失敗保護 | playwright、formulas、assets |
| `converter.py` | 將可見 HTML 轉為 Markdown；內部 `.html` 連結改寫為同語言資料夾內的 `.md` 相對連結；頁內錨點轉為純文字；圖片節點轉為 `![alt](相對路徑)`；公式標記換成 LaTeX | markdownify、beautifulsoup4、formulas、assets |
| `indexer.py` | 為每個語言產生 `INDEX.md`（名稱 → 檔案 → 分類；分類取自麵包屑與 `toc_*`） | 無 |
| `pipeline.py` | `crawl()`（非同步爬取並行、重試、斷點續爬）、`resolve_formulas()`（掃描解碼並可選 OCR）、`convert_all()`（離線轉換、略過空殼頁、產生索引） | 以上模組 |
| `verify.py` | 驗收檢查：連結與圖片路徑可解析、無語言重複文字、公式定界符成對且無殘留標記、各語言檔案數統計 | 無 |
| `cli.py` | 子命令與參數（見 §6） | 以上模組 |

### 目錄結構
```
output/                      # 不進版控
  hdevelop/  dotnet/  python/   # 各含 <page>.md 與 INDEX.md
  assets/                       # 三語言共用的圖片（雜湊命名、去重）
cache/                       # 不進版控
  html/<lang>/<page>.html       # 各語言的可見 HTML
  meta/<page>.json              # 標題、麵包屑、連結、圖片網址
  latex/<key>.json              # 公式：原始 SVG、LaTeX、來源、被拒原因
  failed.txt                    # 失敗的網址
```
頁面路徑對應原站（原站為扁平結構，例如 `output/python/abs_image.md`）。圖片放在共用的 `output/assets/`，Markdown 以相對路徑（如 `../assets/<hash>.svg`）引用，避免三語言重複儲存。

## 4. 資料流

```
入口頁 → 佇列 → extractor（每頁載入 1 次，切換 3 種語言）
                  ├→ cache/html/<lang>/<page>.html
                  ├→ <img> 下載 → output/assets/
                  └→ 新發現的連結 → 回到佇列
cache/html → resolve_formulas ─→ cache/latex/<key>.json（字形解碼；--ocr-fallback 時對被拒者 OCR）
cache/html + cache/latex → converter → output/<lang>/<page>.md（+ output/assets/*.svg）
output/<lang>/…     → indexer   → output/<lang>/INDEX.md
```
因為各語言的可見 HTML 與公式結果都已寫入 `cache/`，調整轉換規則或補齊字形對照表只需重跑 `convert`，不必重爬、不必重複 OCR。

## 5. 公式轉 LaTeX

### 5.1 分層策略
1. **字形解碼（預設、離線、精確）**：直接由 SVG 的字形（字型 + 字碼）還原 LaTeX。
2. **OCR 備援（選用）**：字形解碼被拒的公式，交給 latexconvert.com。需明確加 `--ocr-fallback`，預設關閉。
3. **保留圖檔**：以上皆失敗或未啟用時，輸出 `![figure](…svg)`，與現況相同。

### 5.2 字形解碼的規則與安全閘
所有條件都成立才輸出 LaTeX；任何一項不成立就拋出 `Reject`（記錄原因代碼），絕不猜測：
- 字型都在支援清單，且每個字碼都在對照表內。
- 沒有 `<path>` / `<rect>` 等圖形元素（分數線、根號橫線）。
- 沒有 `cmex` 字型（大括號、矩陣括號、根號、求和、積分）。
- 所有主字形（字型尺寸 ≥ 10）位於同一條基線（容許誤差 1.0）；出現多條基線代表分數、矩陣或多行，一律拒絕。
- 上下標只有一層：尺寸 7 的字形（如 `cmmi7`）依 y 座標高於基線為上標、低於為下標；尺寸 5（二層上下標）拒絕。
- **完整性檢查**：解析到的字形數必須等於 SVG 內 `<use>` 的數量，避免解析器漏字而輸出殘缺公式。（原型曾因字型名稱 `pcrr8r` 的數字不在尾端而漏掉字形，造成 `=\det .` 這類缺字結果，因此列為硬性規則。）
- 輸出對照：`pcrr8r` → `\texttt{}`、`ptmr8r` → `\text{}`（純標點不包）、`ptmri8r`／`cmti10` → `\textit{}`、`cmbx10` → `\mathbf{}`、`cmr10` 的字母 → `\mathrm{}`（函數名如 `\sin`、`\max`）、`cmmi10` → 數學斜體與希臘字母、`cmsy10` → 符號（`\le`、`\cdot`、`\prime` 等）。文字字型在 `<g>` 群組邊界補空白。
- 原型量測（120 頁抽樣共 140 個公式）：可解碼 **93 個（66%）**；被拒 47 個：`cmex` 22、分數線 10、多基線 6、上標開頭 5、未知字碼 4。

### 5.3 OCR 備援（latexconvert.com）
- **何時使用**：只對字形解碼被拒的公式（預估約 370 個），且需 `--ocr-fallback`。預設關閉的理由：這會把公式圖片送到第三方服務，而該站沒有公開 API。
- **做法**：只驅動網頁介面 `https://latexconvert.com/zh/`——以 Playwright 把 SVG 轉成白底 PNG（縮放 3 倍），設定到 `input[type=file]`，等待 `textarea.latex-output` 出現非空內容並讀取。
- **限制與禮貌**：
  - 不直接呼叫 `/convert` 端點（`robots.txt` 對它 Disallow）。
  - 循序執行，請求間隔預設 5 秒（`--ocr-delay`）；每次執行最多處理 500 筆（`--ocr-max`）。
  - 連續失敗 3 次即停止（可能被限流或需要驗證）；每個公式最多嘗試 2 次；成功結果永久快取，不重複上傳。
  - 預估 370 筆約 30 分鐘。
- **準確性**：該站條款聲明結果可能有錯。實測同一個矩陣公式兩次辨識，一次得到 `HomMat2DRotate`，一次得到 `HomMat2Drotate`（原圖為前者）。因此 OCR 結果一律附上原圖，供人核對。

### 5.4 Markdown 輸出格式
| 情況 | 輸出 |
|---|---|
| 字形解碼成功、行內公式 | `$LaTeX$`，不附圖 |
| 字形解碼成功、獨立公式 | `$$LaTeX$$`，不附圖 |
| OCR 成功 | 同上格式，後面接 ` ![figure](../assets/<hash>.svg)` |
| 皆失敗或未啟用 OCR | `![figure](../assets/<hash>.svg)` |

- LaTeX 內的換行與連續空白壓成單一空白。
- 公式在 HTML 階段以標記 `@@FORMULA:<key>:<d|i>:<圖檔名或->@@` 佔位，等 markdownify 完成後才換回 LaTeX，避免 `_`、`\`、`*`、`[` 被跳脫。
- 解碼成功的公式不寫 `.svg` 資產，減少檔案數。

### 5.5 快取
`cache/latex/<key>.json`，`key` 為公式原始 SVG 字串的 SHA-1 前 16 碼：`svg`、`latex`（可為 null）、`source`（`decode`／`ocr`／null）、`reject`（被拒原因）、`ocr_attempts`、`ocr_error`。
`convert` 每次都掃描快取內所有公式：新公式解碼後存入；尚無 LaTeX 的舊公式會重試解碼（字形對照表補齊後即可救回，無須 OCR）。

## 6. CLI

- `halcon-doc-skills crawl`：爬取，接著解碼公式並轉換。
- `halcon-doc-skills convert`：僅以 `cache/` 解碼公式、轉換並建立索引。
- `halcon-doc-skills verify`：檢查 `output/`（§8 驗收標準與檔案數統計）。
- 共通選項：`--force`（忽略快取與已完成頁面，僅 `crawl`）、`--limit N`（試跑，只處理 N 頁）、`--entry PAGE`（可重複，覆寫入口頁，用於抽樣）、`--concurrency N`（預設 4）、`--output DIR`（預設 `output`）。
- OCR 選項（`crawl`、`convert`）：`--ocr-fallback`（啟用備援，預設關閉）、`--ocr-delay SEC`（預設 5）、`--ocr-max N`（預設 500）。

## 7. 錯誤處理與禮貌爬取

- 逾時或 HTTP 非 200：重試 3 次（指數退避），仍失敗則寫入 `cache/failed.txt`，其餘頁面繼續。
- 斷點續爬：某頁 3 個語言的快取皆存在則跳過，除非 `--force`；跳過的頁面仍沿用快取中的連結繼續往下爬。
- 未爬到的內部連結目標，或目標為該語言的空殼頁（不輸出的類別頁）：Markdown 保留原站完整網址，不產生壞連結。
- HTTP 404 等 4xx（429 除外）不重試，直接記為失敗。
- 並行 4 個分頁，請求間有短暫延遲，避免對 mvtec.com 造成負擔。
- OCR 失敗（逾時、無結果）：記錄於該公式的快取並保留圖檔；連續失敗 3 次停止整個 OCR 階段。
- 以 `logging` 輸出進度（第 N／總數、失敗數），不使用 `print`。

## 8. 測試與驗證

- **單元測試（pytest）**：網址正規化與範圍過濾、`data-if` 可見性篩選、連結改寫、圖片節點轉換、公式解碼（含被拒案例）、公式標記替換；使用 `tests/fixtures/` 內的真實頁面樣本（`abs_image.html`、`HBarCode.html`、`threshold.html`、一個 `toc_*` 頁，以及含各類公式的 `dyn_threshold.html`、`determinant_matrix.html`、`affine_trans_image.html`、`harmonic_interpolation.html`、`set_lut.html`、`create_dl_layer_affine_grid.html`、`hom_mat2d_rotate.html`、`create_dl_layer_lrn.html`）。
- **公式解碼的「經瀏覽器序列化」測試**：以 Playwright 取回頁面後再解碼，確認瀏覽器輸出的 SVG 字串仍可被解碼（`viewBox`、`<use>` 屬性未被改動）。
- **OCR 備援的測試**：以本機假網站（同樣的 `input[type=file]` 與 `textarea.latex-output`）測試流程、節流與連續失敗停止；不在自動化測試中連線 latexconvert.com。
- **整合驗證**：以 `--limit 20` 或 `--entry` 抽樣試跑並人工檢查，驗收標準：
  1. Markdown 內不含 `abs_imageabs_image…` 之類的語言重複文字。
  2. 三個語言資料夾的 `.md` 檔案數僅相差空殼類別頁（HDevelop、Python 不輸出類別頁）。
  3. 每個 `INDEX.md` 內的連結皆可解析到實際檔案。
  4. 所有 `![](…)` 路徑皆對應到存在的檔案。
  5. 公式定界符 `$` 成對，且沒有殘留的 `@@FORMULA:` 標記。
- **全量爬取後回報**：頁數（預期約 2,700）、失敗數、三個資料夾檔案數、SVG 與 `<img>` 數量、公式統計（總數、字形解碼數、OCR 數、保留圖檔數、被拒原因分布）。
- **公式抽驗**：全量後隨機抽 30 個字形解碼的公式，以 LaTeX 渲染後與原圖人工比對；OCR 結果逐一比對原圖（數量約 370，可先抽樣）。

## 9. 相依套件與環境

- Python ≥ 3.13、uv 專案（沿用現有 `pyproject.toml`）。
- 執行期：`playwright`（需執行 `playwright install chromium`）、`markdownify`、`beautifulsoup4`。公式功能不新增套件。
- 開發：`pytest`、`ruff`。
- `.gitignore` 加入 `output/`、`cache/`。

## 10. 假設（可調整）

1. 輸出放 `output/`、快取放 `cache/`，皆不進版控。
2. 並行 4、重試 3 次。
3. 圖片共用 `output/assets/`，而非每個語言各存一份。
4. 頁內錨點（`#Image`）轉為純文字，不保留為連結。
5. 未轉成 LaTeX 的行內 SVG，alt text 固定為 `figure`；`<img>` 使用其 `alt` 屬性。
6. 「只下載 HDevelop、.NET、Python」解讀為語言範圍縮減為此三種。
7. **OCR 備援預設關閉**，需 `--ocr-fallback` 才啟用（使用者要求以 latexconvert 當備援；預設關閉是因為會把圖片送往第三方、且節流下需約 30 分鐘）。若要改成預設開啟，只需改 CLI 預設值。
8. 字形解碼寧可拒絕也不猜測；OCR 結果一律附原圖。
9. 字形對照表只收錄目前抽樣看到、且有把握的字碼；遇到未知字碼會被拒並記錄，日後補表後重跑 `convert` 即可。

## 11. 已知風險

- 字形解碼只保證「字元與上下標位置」正確，尚未處理分數、根號、矩陣、求和積分等（約 34% 的公式，交由備援）。若字型對照表有誤（例如某字碼對應錯誤符號），會產生看似合理但錯誤的 LaTeX；以抽驗與 `verify` 降低風險。
- OCR 結果可能有錯，且同一張圖每次辨識結果不一定相同；因此附上原圖。
- latexconvert.com 是第三方服務：介面改版會讓自動化失效；後端有限流、頁面有 Cloudflare 驗證腳本，日後可能阻擋無頭瀏覽器；條款禁止「壓垮服務」，故採用低頻率、有上限的節流。上傳的圖片是 MVTec 公開文件中的公式。
- 全站頁面中可能存在抽查未涵蓋的 `<img>` 或其他嵌入資源，將於全量爬取後的統計回報中確認。
- 部分 `toc_*` 頁面體積大（如 `index_by_name.html` 約 1.1MB），載入較慢，但不影響正確性。
