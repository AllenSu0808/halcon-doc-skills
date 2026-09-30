# halcon-doc-skills

以 Playwright 爬取 [HALCON 26.05 Operator Reference](https://www.mvtec.com/doc/halcon/2605/en/index.html)，
逐語言（HDevelop、.NET、Python）轉成 Markdown，供 Claude 當參考資料。

## 安裝

    uv sync
    uv run playwright install chromium

## 使用

    uv run halcon-doc-skills crawl            # 爬取並轉換（約 2,700 頁，需要一段時間）
    uv run halcon-doc-skills crawl --limit 20 # 試跑
    uv run halcon-doc-skills crawl --entry abs_image.html --limit 1  # 抽樣單頁
    uv run halcon-doc-skills convert          # 只用 cache/ 重新轉換
    uv run halcon-doc-skills verify           # 檢查輸出品質

## 公式

站上的公式是 MetaPost 排版的行內 SVG。轉換時：

1. 先以 SVG 字形（字型 + 字碼）離線解碼成 LaTeX，行內公式輸出 `$…$`、獨立公式輸出 `$$…$$`。
2. 分數、矩陣、根號、求和積分、多行等無法可靠解碼的公式會保留圖檔 `![figure](../assets/….svg)`。
3. 加上 `--ocr-fallback` 時，這些公式改用 [latexconvert.com](https://latexconvert.com/zh/) 做 OCR
   （**會把公式圖片上傳到第三方**，預設關閉；間隔 5 秒、每次最多 500 筆）。OCR 結果可能有誤，
   因此一律附上原圖供核對。

        uv run halcon-doc-skills convert --ocr-fallback --ocr-max 20   # 先小量試跑

公式結果快取在 `cache/latex/`，重跑不會重複上傳。

## 輸出結構

    output/
      hdevelop/ dotnet/ python/   # 每個語言：<page>.md 與 INDEX.md
      assets/                     # 三語言共用的圖片（雜湊命名）
    cache/                        # 各語言可見 HTML 與中繼資料（可重複轉換）

- 類別頁（如 `HBarCode`）只有 .NET 有內容，HDevelop 與 Python 不輸出。
- 解碼成功的公式不產生 `.svg`；未轉成 LaTeX 的公式才會出現在 `output/assets/`。
- 中斷後重跑 `crawl` 會沿用 `cache/`，只補抓缺少的頁面。
- 失敗的網址記錄在 `cache/failed.txt`。

## 產生 Claude Code skill

    uv run halcon-doc-skills build-skill                           # 產生到 dist/skill/halcon-expert/
    uv run halcon-doc-skills build-skill --out /tmp/halcon-expert  # 指定輸出位置

把 `dist/skill/halcon-expert/` 整個複製到 HALCON 專案的 `.claude/skills/halcon-expert/`。

- 只需要部分語言時，刪除 `references/<lang>/` 與 `pitfalls/<lang>.md` 即可。
- skill 附帶 `scripts/halcon_doc.py`（Python 3.10+，只用標準函式庫），提供
  `search`、`sig`、`params`、`section`、`class`、`check` 子命令。
- `--out` 已存在但不是先前產生的 skill（沒有 `SKILL.md`）時會拒絕覆寫。
- skill 原始檔在 `skill_template/`；修改後重跑 `build-skill` 並重新複製到專案。

