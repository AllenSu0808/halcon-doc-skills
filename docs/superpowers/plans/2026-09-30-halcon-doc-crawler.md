# HALCON 文件爬取與 Markdown 轉換工具 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 以 Playwright 爬取 `https://www.mvtec.com/doc/halcon/2605/en/` 全部文件頁，逐語言（HDevelop、.NET、Python）取可見 DOM，轉成乾淨 Markdown（含圖片，公式盡量還原為 LaTeX）存到本機。

**Architecture:** `crawl` 以 async Playwright 開頁（每頁載入 1 次、點擊 3 種語言分頁、取可見 `.body_main` HTML）並寫入 `cache/`；`convert` 離線讀 `cache/`，行內 SVG 存為共用資產、改寫連結、markdownify 轉 Markdown、略過空殼類別頁並產生各語言 `INDEX.md`；`verify` 檢查輸出品質。公式（MetaPost 行內 SVG）先以字形（字型 + 字碼）離線解碼成 LaTeX；解碼被拒者，在使用者加 `--ocr-fallback` 時改用 latexconvert.com 網頁介面 OCR 備援；仍失敗則保留圖檔。

**Tech Stack:** Python ≥3.13、uv、playwright（async）、markdownify、beautifulsoup4、pytest、ruff。

**Spec:** [docs/superpowers/specs/2026-09-30-halcon-doc-crawler-design.md](../specs/2026-09-30-halcon-doc-crawler-design.md)

## Global Constraints

- Python ≥3.13，uv 專案（沿用現有 `pyproject.toml`，build backend `uv_build`，套件路徑 `src/halcon_doc_skills/`）。
- 所有程式碼註解與 docstring 一律使用**繁體中文**；docstring 用 Sphinx/reST 風格；識別字用英文。
- PEP 8：4 空格縮排；程式碼每行 ≤88 字元，註解／docstring ≤80 字元；函式／變數 snake_case、類別 PascalCase、常數 UPPER_SNAKE_CASE。
- 診斷輸出用 `logging`，不用 `print()`；禁止 bare `except Exception:`，只捕捉具體例外。
- 語言固定為 `hdevelop`、`dotnet`、`python`（不處理 C++ / C）。
- 網址範圍：`https://www.mvtec.com/doc/halcon/2605/en/*.html`，不跟隨外部連結。
- 輸出結構：`output/<lang>/<page>.md`、`output/<lang>/INDEX.md`、`output/assets/`（三語言共用）；快取 `cache/html/<lang>/<page>`、`cache/meta/<page>.json`、`cache/failed.txt`；`output/` 與 `cache/` 不進版控。
- 預設並行 4、重試 3 次、請求後延遲 0.3 秒。
- lint／格式：每個任務的 `ruff` 步驟若只出現 import 排序（I001）或格式問題，用 `uv run ruff check --fix && uv run ruff format` 修正；`src/` 內若出現 E501（行過長）則手動換行。
- 公式：字形解碼寧可拒絕也不猜測（未知字型／字碼、圖形元素、`cmex`、多基線、二層上下標一律 `Reject`），且解析到的字形數必須等於 SVG 內 `<use>` 數。
- 公式輸出：行內 `$…$`、獨立 `$$…$$`；解碼成功不寫 `.svg`；OCR 結果一律附原圖 `![figure](…)`；公式以 `@@FORMULA:<key>:<d|i>:<圖檔或->@@` 標記佔位，待 markdownify 完成後才換成 LaTeX。
- OCR 備援：預設關閉，需 `--ocr-fallback`；只驅動 `https://latexconvert.com/zh/` 網頁介面（`input[type=file]` → `textarea.latex-output`），不呼叫其 `/convert` 端點；預設間隔 5 秒、上限 500 筆、連續失敗 3 次停止、每個公式最多嘗試 2 次；自動化測試不連線該網站。
- Commit message 依全域規範：繁體中文，摘要行 `<prefix>: <中文摘要>`，下一行起以 `--- 類別 ---` 分段、項目以 `1.` 開頭並以動詞起頭。

## Review Focus

1. 不存在的網址（HTTP 404）不得寫入快取，也不得中斷整體爬取；4xx（429 除外）不重試 — Task 4、10。
2. 類別頁在 HDevelop / Python 只有「Use the tabs…」空殼：不輸出 `.md`、不列入索引，指向它的連結退回原站完整網址而非壞連結 — Task 7、10。
3. 只在 .NET 分頁才出現的連結（如 `HImage.html`）仍要被爬到（連結需取所有語言的聯集）— Task 4。
4. 中斷後重跑（`is_complete` 為真）仍要沿用 `meta` 內的連結繼續往下走，不能只跳過就讓子頁消失 — Task 10。
5. 行內 SVG 必須保留 `viewBox` 大小寫、補上 `xmlns`，相同公式去重成同一個檔；子目錄頁面的相對路徑（`../assets/`、`../y.md`）要正確 — Task 6、7。
6. 字形解碼不得靜默漏字或串錯：`<use>` 完整性檢查（原型曾因 `pcrr8r` 漏字而輸出 `=\det .`）、指令後接字母要補空白（`\gamma x` 不能變成 `\gammax`）— Task 5。
7. LaTeX 不得被 markdownify 跳脫（`_`、`\`、`*`、`[`），且輸出不得殘留 `@@FORMULA:` 標記或不成對的 `$` — Task 7、10、11。
8. OCR 被限流或介面改版時不能無限重試或卡住：連續失敗即停止、失敗要留紀錄並保留圖檔、已成功的結果不重複上傳 — Task 9。

---

### Task 1: 專案骨架、相依套件與測試樣本

**Files:**
- Modify: `pyproject.toml`
- Modify: `src/halcon_doc_skills/__init__.py`
- Create: `.gitignore`
- Create: `tests/__init__.py`（空檔）
- Create: `tests/fixtures/*.html`（真實頁面樣本：`abs_image`、`HBarCode`、`threshold`、`toc_filters_arithmetic`，以及含各類公式的 `dyn_threshold`、`determinant_matrix`、`affine_trans_image`、`harmonic_interpolation`、`set_lut`、`create_dl_layer_affine_grid`、`hom_mat2d_rotate`、`create_dl_layer_lrn`、`find_shape_model_3d`、`cooc_feature_image`、`gray_erosion`）
- Create: `tests/test_smoke.py`

**Interfaces:**
- Produces: 可用的 `uv run pytest`、`uv run ruff check`；`tests/fixtures/*.html` 供後續任務使用；`halcon_doc_skills.main` 暫時仍為佔位（Task 11 改為呼叫 `cli.main`）。

- [ ] **Step 1: 安裝相依套件**

Run:
```bash
cd /home/administrator/code/halcon-doc-skills
uv add playwright markdownify beautifulsoup4
uv add --dev pytest ruff
uv run playwright install chromium
```
Expected: `pyproject.toml` 出現 `dependencies` 與 `[dependency-groups] dev`；chromium 下載完成。若之後執行 Playwright 時出現缺少系統函式庫（如 `libnss3`）的錯誤，執行 `uv run playwright install-deps chromium`（需要 sudo，請使用者自行執行）。

- [ ] **Step 2: 設定 pytest 與 ruff**

在 `pyproject.toml` 末尾加入（`[tool.*]` 區段位置不限）：

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
markers = ["browser: 需要 Playwright Chromium 的測試"]

[tool.ruff]
line-length = 88
target-version = "py313"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["E501"]
```

- [ ] **Step 3: 建立 .gitignore**

```gitignore
# 爬取快取與輸出
cache/
output/

# Python
__pycache__/
*.pyc
.venv/
.pytest_cache/
.ruff_cache/
dist/
```

- [ ] **Step 4: 下載真實頁面樣本**

Run:
```bash
cd /home/administrator/code/halcon-doc-skills
mkdir -p tests/fixtures && touch tests/__init__.py
B=https://www.mvtec.com/doc/halcon/2605/en
for p in abs_image HBarCode threshold toc_filters_arithmetic \
         dyn_threshold determinant_matrix affine_trans_image harmonic_interpolation \
         set_lut create_dl_layer_affine_grid hom_mat2d_rotate create_dl_layer_lrn \
         find_shape_model_3d cooc_feature_image gray_erosion; do
  curl -sfL "$B/$p.html" -o "tests/fixtures/$p.html" || echo "FAILED $p"
  sleep 0.3
done
ls -la tests/fixtures
```
Expected: 15 個檔案，沒有 `FAILED`。（公式測試的預期結果依 MVTec HALCON 26.05 文件內容而定；若日後樣本內容變動導致 Task 5 的預期值不符，先確認是站上內容變了，再決定是否更新預期值。）

- [ ] **Step 5: 寫冒煙測試並確認環境可用**

`tests/test_smoke.py`：

```python
"""確認測試環境與樣本檔可用。"""
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def test_fixtures_exist() -> None:
    pages = sorted(FIXTURES.glob("*.html"))
    assert len(pages) >= 15
    for path in pages:
        assert "syn-hdevelop" in path.read_text(encoding="utf-8"), path.name
```

Run: `uv run pytest -v && uv run ruff check`
Expected: 1 passed；ruff 無錯誤。

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml uv.lock .gitignore .python-version README.md src tests docs
git commit -m "chore: 建立專案骨架、相依套件與測試樣本
--- docs ---
1. 新增爬取工具的設計文件與實作計畫
--- chore ---
1. 新增 playwright、markdownify、beautifulsoup4 相依
2. 設定 pytest 與 ruff
3. 新增 .gitignore 排除 cache 與 output
4. 下載真實頁面樣本供測試使用"
```
（若專案沒有 `uv.lock`，從 `git add` 移除該檔；先以 `git status` 確認。）

---

### Task 2: 設定常數與 URL 處理（config.py、crawler.py）

**Files:**
- Create: `src/halcon_doc_skills/config.py`
- Create: `src/halcon_doc_skills/crawler.py`
- Test: `tests/test_crawler.py`

**Interfaces:**
- Produces（`config`，其他模組一律以 `from . import config` 於呼叫時讀取，測試才能 monkeypatch）：
  `BASE_HOST: str`、`SCOPE_PREFIX: str`、`BASE_URL: str`、`ENTRY_PAGES: tuple[str, ...]`、`LANGS: tuple[str, ...]`、`DEFAULT_CONCURRENCY: int`、`DEFAULT_RETRIES: int`、`DEFAULT_DELAY: float`、`STUB_MARKER: str`
- Produces（`crawler`）：
  `normalize_url(href: str, base_url: str) -> str | None`、
  `page_name(url: str) -> str`（範圍內網址 → 相對於 `SCOPE_PREFIX` 的路徑，如 `abs_image.html`）、
  `md_name(page: str) -> str`（`abs_image.html` → `abs_image.md`）、
  `class Frontier`：`__init__(limit: int | None = None)`、`add(url: str) -> bool`、`__len__()`。

- [ ] **Step 1: 寫失敗測試**

`tests/test_crawler.py`：

```python
"""URL 正規化、範圍過濾與去重的測試。"""
from halcon_doc_skills.crawler import Frontier, md_name, normalize_url, page_name

BASE = "https://www.mvtec.com/doc/halcon/2605/en/index.html"
PREFIX = "https://www.mvtec.com/doc/halcon/2605/en/"


def test_relative_link_is_resolved() -> None:
    assert normalize_url("toc_1dmeasuring.html", BASE) == PREFIX + "toc_1dmeasuring.html"


def test_fragment_and_query_are_removed() -> None:
    assert normalize_url("abs_image.html#Image", BASE) == PREFIX + "abs_image.html"
    assert normalize_url("abs_image.html?interface=python", BASE) == (
        PREFIX + "abs_image.html"
    )


def test_http_scheme_is_upgraded_to_base_scheme() -> None:
    url = "http://www.mvtec.com/doc/halcon/2605/en/abs_image.html"
    assert normalize_url(url, BASE) == PREFIX + "abs_image.html"


def test_out_of_scope_links_are_rejected() -> None:
    assert normalize_url("../../../../documentation.html", BASE) is None
    assert normalize_url("http://www.mvtec.com/", BASE) is None
    assert normalize_url("https://www.linkedin.com/company/x", BASE) is None
    assert normalize_url("https://www.mvtec.com/doc/halcon/2505/en/x.html", BASE) is None


def test_non_html_and_pseudo_links_are_rejected() -> None:
    assert normalize_url("javascript:void(0);", BASE) is None
    assert normalize_url("mailto:a@b.c", BASE) is None
    assert normalize_url("style.css", BASE) is None
    assert normalize_url("", BASE) is None


def test_page_name_and_md_name() -> None:
    assert page_name(PREFIX + "abs_image.html") == "abs_image.html"
    assert page_name(PREFIX + "sub/x.html") == "sub/x.html"
    assert md_name("abs_image.html") == "abs_image.md"
    assert md_name("sub/x.html") == "sub/x.md"


def test_frontier_deduplicates() -> None:
    frontier = Frontier()
    assert frontier.add("a") is True
    assert frontier.add("a") is False
    assert len(frontier) == 1


def test_frontier_respects_limit() -> None:
    frontier = Frontier(limit=2)
    assert frontier.add("a") is True
    assert frontier.add("b") is True
    assert frontier.add("c") is False
    assert len(frontier) == 2
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_crawler.py -v`
Expected: FAIL（`ModuleNotFoundError: halcon_doc_skills.crawler`）

- [ ] **Step 3: 實作 config.py**

```python
"""全域常數。

其他模組請以 ``from . import config`` 匯入並在呼叫時讀取屬性，
讓測試可以用 monkeypatch 改寫網址範圍。
"""
from __future__ import annotations

# 網址範圍：只爬 HALCON 26.05 英文版文件
BASE_HOST = "www.mvtec.com"
SCOPE_PREFIX = "/doc/halcon/2605/en/"
BASE_URL = f"https://{BASE_HOST}{SCOPE_PREFIX}"

# 爬取入口：index 只有 toc 連結，運算子與類別需從索引頁取得
ENTRY_PAGES: tuple[str, ...] = (
    "index.html",
    "index_by_name.html",
    "index_classes.html",
)

# 要輸出的語言（每種語言一個資料夾）
LANGS: tuple[str, ...] = ("hdevelop", "dotnet", "python")

# 爬取行為預設值
DEFAULT_CONCURRENCY = 4
DEFAULT_RETRIES = 3
DEFAULT_DELAY = 0.3

# 類別頁在無內容語言只顯示這句話，視為空殼頁
STUB_MARKER = (
    "Use the tabs on the upper right to switch to a different "
    "programming language."
)
```

- [ ] **Step 4: 實作 crawler.py**

```python
"""網址正規化、範圍過濾與去重佇列。"""
from __future__ import annotations

from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit

from . import config


def normalize_url(href: str, base_url: str) -> str | None:
    """將連結轉成範圍內的絕對網址。

    :param href: 頁面上的原始 href。
    :param base_url: 該頁面本身的網址，用來解析相對連結。
    :return: 去除 fragment 與 query、scheme 統一後的網址；
        若不在文件範圍內或不是 .html 則回傳 None。
    """
    href = href.strip()
    if not href or href.lower().startswith(("javascript:", "mailto:", "tel:")):
        return None
    absolute, _ = urldefrag(urljoin(base_url, href))
    parts = urlsplit(absolute)
    if parts.scheme not in ("http", "https"):
        return None
    if parts.netloc != config.BASE_HOST:
        return None
    if not parts.path.startswith(config.SCOPE_PREFIX):
        return None
    if not parts.path.endswith(".html"):
        return None
    scheme = urlsplit(config.BASE_URL).scheme
    return urlunsplit((scheme, parts.netloc, parts.path, "", ""))


def page_name(url: str) -> str:
    """回傳範圍內網址相對於文件根目錄的路徑，如 ``abs_image.html``。"""
    return urlsplit(url).path[len(config.SCOPE_PREFIX):]


def md_name(page: str) -> str:
    """將頁面路徑的副檔名由 .html 換成 .md。"""
    if page.endswith(".html"):
        return page[: -len(".html")] + ".md"
    return page + ".md"


class Frontier:
    """記錄已見過的網址，避免重複爬取，並可限制總數（試跑用）。"""

    def __init__(self, limit: int | None = None) -> None:
        self._seen: set[str] = set()
        self._limit = limit

    def add(self, url: str) -> bool:
        """加入網址。

        :return: 首次加入且未超過上限時為 True，否則為 False。
        """
        if url in self._seen:
            return False
        if self._limit is not None and len(self._seen) >= self._limit:
            return False
        self._seen.add(url)
        return True

    def __len__(self) -> int:
        return len(self._seen)
```

- [ ] **Step 5: 執行確認通過**

Run: `uv run pytest tests/test_crawler.py -v && uv run ruff check`
Expected: 8 passed；ruff 無錯誤。

- [ ] **Step 6: Commit**

```bash
git add src/halcon_doc_skills/config.py src/halcon_doc_skills/crawler.py tests/test_crawler.py
git commit -m "feat: 新增設定常數與網址正規化、範圍過濾
--- feat ---
1. 新增 config 集中管理網址範圍、語言與預設值
2. 新增 normalize_url 過濾範圍外與非 html 連結
3. 新增 Frontier 支援去重與數量上限
4. 新增 page_name 與 md_name 頁面命名輔助"
```

---

### Task 3: 頁面快取（cache.py）

**Files:**
- Create: `src/halcon_doc_skills/extractor.py`（此任務只放 `PageFetchError` 與 `PageExtract`，Task 4 補完）
- Create: `src/halcon_doc_skills/cache.py`
- Test: `tests/test_cache.py`

**Interfaces:**
- Consumes: `config.LANGS`。
- Produces（`extractor`）：
  `class PageFetchError(Exception)`：`__init__(message: str, status: int | None = None)`，屬性 `status`，屬性 `retryable: bool`（`status is None or status >= 500 or status == 429`）。
  `@dataclass class PageExtract`：`url: str`、`title: str`、`breadcrumb: list[tuple[str, str]]`、`links: list[str]`、`image_urls: list[str]`、`html_by_lang: dict[str, str]`。
- Produces（`cache`）：`class PageCache`：`__init__(root: Path, langs: Sequence[str] = config.LANGS)`、`html_path(lang, page) -> Path`、`meta_path(page) -> Path`、`failed_path -> Path`（property）、`is_complete(page) -> bool`、`save(page: str, extract: PageExtract) -> None`、`load_meta(page) -> dict`、`load_html(lang, page) -> str`、`pages() -> list[str]`（已排序）、`record_failure(url: str, reason: str) -> None`。
  meta JSON 欄位：`url`、`title`、`breadcrumb`（`[[文字, 網址], ...]`）、`links`、`image_urls`。

- [ ] **Step 1: 寫失敗測試**

`tests/test_cache.py`：

```python
"""PageCache 讀寫與完整性判斷的測試。"""
from pathlib import Path

from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract, PageFetchError


def _extract() -> PageExtract:
    return PageExtract(
        url="https://www.mvtec.com/doc/halcon/2605/en/abs_image.html",
        title="abs_image",
        breadcrumb=[("HALCON 26.05", "https://x/"), ("Filters", "https://x/f")],
        links=["https://www.mvtec.com/doc/halcon/2605/en/add_image.html"],
        image_urls=[],
        html_by_lang={
            "hdevelop": "<p>hd</p>",
            "dotnet": "<p>net</p>",
            "python": "<p>py</p>",
        },
    )


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    cache.save("abs_image.html", _extract())
    assert cache.load_html("python", "abs_image.html") == "<p>py</p>"
    meta = cache.load_meta("abs_image.html")
    assert meta["title"] == "abs_image"
    assert meta["breadcrumb"][1] == ["Filters", "https://x/f"]
    assert meta["links"] == [
        "https://www.mvtec.com/doc/halcon/2605/en/add_image.html"
    ]


def test_is_complete_requires_meta_and_all_languages(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    assert cache.is_complete("abs_image.html") is False
    cache.save("abs_image.html", _extract())
    assert cache.is_complete("abs_image.html") is True
    cache.html_path("dotnet", "abs_image.html").unlink()
    assert cache.is_complete("abs_image.html") is False


def test_pages_lists_sorted_names_including_subdirs(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    for name in ("b.html", "a.html", "sub/c.html"):
        cache.save(name, _extract())
    assert cache.pages() == ["a.html", "b.html", "sub/c.html"]


def test_record_failure_appends_lines(tmp_path: Path) -> None:
    cache = PageCache(tmp_path)
    cache.record_failure("https://x/a.html", "HTTP 404")
    cache.record_failure("https://x/b.html", "timeout")
    lines = cache.failed_path.read_text(encoding="utf-8").splitlines()
    assert lines == ["https://x/a.html\tHTTP 404", "https://x/b.html\ttimeout"]


def test_page_fetch_error_retryable_rules() -> None:
    assert PageFetchError("x", status=None).retryable is True
    assert PageFetchError("x", status=503).retryable is True
    assert PageFetchError("x", status=429).retryable is True
    assert PageFetchError("x", status=404).retryable is False
    assert PageFetchError("x", status=200).retryable is False
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_cache.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: 實作 extractor.py（僅資料型別）**

```python
"""以 Playwright 取出各語言的可見頁面內容。"""
from __future__ import annotations

from dataclasses import dataclass


class PageFetchError(Exception):
    """頁面載入失敗或不是 HALCON 文件頁。"""

    def __init__(self, message: str, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status

    @property
    def retryable(self) -> bool:
        """網路錯誤、5xx 與 429 值得重試；其他（如 404）不重試。"""
        return self.status is None or self.status >= 500 or self.status == 429


@dataclass
class PageExtract:
    """單一頁面的擷取結果。"""

    url: str
    title: str
    breadcrumb: list[tuple[str, str]]
    links: list[str]
    image_urls: list[str]
    html_by_lang: dict[str, str]
```

- [ ] **Step 4: 實作 cache.py**

```python
"""爬取結果的本機快取：各語言可見 HTML 與頁面中繼資料。"""
from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path

from . import config
from .extractor import PageExtract


class PageCache:
    """管理 ``html/<lang>/<page>``、``meta/<page>.json`` 與 ``failed.txt``。"""

    def __init__(
        self, root: Path, langs: Sequence[str] = config.LANGS
    ) -> None:
        self.root = Path(root)
        self.langs = tuple(langs)

    def html_path(self, lang: str, page: str) -> Path:
        """某語言可見 HTML 的快取路徑。"""
        return self.root / "html" / lang / page

    def meta_path(self, page: str) -> Path:
        """頁面中繼資料 JSON 的路徑。"""
        return self.root / "meta" / f"{page}.json"

    @property
    def failed_path(self) -> Path:
        """失敗網址清單的路徑。"""
        return self.root / "failed.txt"

    def is_complete(self, page: str) -> bool:
        """中繼資料與所有語言的 HTML 都存在才視為完成。"""
        if not self.meta_path(page).exists():
            return False
        return all(self.html_path(lang, page).exists() for lang in self.langs)

    def save(self, page: str, extract: PageExtract) -> None:
        """寫入各語言 HTML，最後才寫中繼資料（中斷時不會被誤判為完成）。"""
        for lang in self.langs:
            path = self.html_path(lang, page)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(extract.html_by_lang[lang], encoding="utf-8")
        meta = {
            "url": extract.url,
            "title": extract.title,
            "breadcrumb": [list(item) for item in extract.breadcrumb],
            "links": extract.links,
            "image_urls": extract.image_urls,
        }
        meta_path = self.meta_path(page)
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8"
        )

    def load_meta(self, page: str) -> dict:
        """讀取頁面中繼資料。"""
        text = self.meta_path(page).read_text(encoding="utf-8")
        return json.loads(text)

    def load_html(self, lang: str, page: str) -> str:
        """讀取某語言的可見 HTML。"""
        return self.html_path(lang, page).read_text(encoding="utf-8")

    def pages(self) -> list[str]:
        """列出所有已有中繼資料的頁面（排序後）。"""
        meta_root = self.root / "meta"
        if not meta_root.exists():
            return []
        names = [
            path.relative_to(meta_root).as_posix()[: -len(".json")]
            for path in meta_root.rglob("*.json")
        ]
        return sorted(names)

    def record_failure(self, url: str, reason: str) -> None:
        """附加一筆失敗紀錄。"""
        self.root.mkdir(parents=True, exist_ok=True)
        with self.failed_path.open("a", encoding="utf-8") as fp:
            fp.write(f"{url}\t{reason}\n")
```

- [ ] **Step 5: 執行確認通過**

Run: `uv run pytest tests/test_cache.py -v && uv run ruff check`
Expected: 5 passed；ruff 無錯誤。

- [ ] **Step 6: Commit**

```bash
git add src/halcon_doc_skills/extractor.py src/halcon_doc_skills/cache.py tests/test_cache.py
git commit -m "feat: 新增頁面快取與擷取結果資料型別
--- feat ---
1. 新增 PageCache 管理各語言 HTML 與中繼資料
2. 新增 PageExtract 與 PageFetchError 資料型別
3. 新增完整性判斷與失敗紀錄"
```

---

### Task 4: Playwright 擷取器（extractor.py）

**Files:**
- Modify: `src/halcon_doc_skills/extractor.py`
- Create: `tests/site_builder.py`
- Create: `tests/conftest.py`
- Test: `tests/test_extractor.py`

**Interfaces:**
- Consumes: `PageExtract`、`PageFetchError`（Task 3）、`config.LANGS`。
- Produces: `async def extract_page(page: playwright.async_api.Page, url: str, langs: Sequence[str] = config.LANGS, timeout_ms: int = 60_000) -> PageExtract`。
  行為：`goto` 回應非 200 → `PageFetchError(status=code)`；頁面沒有 `#syn-hdevelop` → `PageFetchError`（`status=200`，不重試）；對每個語言點擊 `#syn-<lang> a` 後在頁面內取「可見」的 `.body_main` 內容（移除隱藏的 `data-if` 元素、`script`、`.tabbar`、`.indexlink`、`.footer`），再於 Python 端從 `<!--OP_REF_FOOTER_START-->` 起截斷；`links` 為所有語言狀態下 `a[href]` 絕對網址的聯集（保留首見順序）；`image_urls` 為內容中 `img[src]` 絕對網址聯集；`breadcrumb` 為 `.breadcrumb a` 的 `(空白正規化文字, 絕對網址)`；`title` 為 `document.title`。
- Produces（測試工具）：`tests/site_builder.py` 的 `build_site(root: Path) -> None`（建立 `en/` 真實樣本、`mini/` 迷你網站與 `ocr/` 假的 latexconvert 頁面），`tests/conftest.py` 的 session fixture `fixture_server -> str`（回傳 `http://127.0.0.1:<port>`，伺服 `build_site` 產生的目錄）。

- [ ] **Step 1: 寫測試網站建構器與 fixture**

`tests/site_builder.py`：

```python
"""建立測試用網站：真實樣本頁 (en/) 與迷你網站 (mini/)。"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"
REAL_PAGES = ("abs_image", "HBarCode", "threshold", "toc_filters_arithmetic")

_SPAN = (
    '<span data-if="hdevelop" style="display:inline;">{hd}</span>'
    '<span data-if="dotnet" style="display:none;">{net}</span>'
    '<span data-if="python" style="display:none;">{py}</span>'
)

_TEMPLATE = """<!DOCTYPE html>
<html lang="en-US"><head><meta charset="UTF-8"><title>{title}</title>
<style>
*[data-if=dotnet], *[data-if=python] {{ display: none; }}
</style>
<script>{js}</script></head>
<body onload="initialize();">
<div class="breadcrumb"><a href="index.html">HALCON
26.05.0.0</a> / <a href="index.html">HALCON Operator Reference</a> /
<a href="toc_a.html">Cat A</a></div>
<div class="body_main">
<div class="tabbar"><ul class="tabs">
<li id="syn-hdevelop" class="active"><a href="javascript:void(0);"
 onclick="toggleLanguage('hdevelop')">HDevelop</a></li>
<li id="syn-dotnet" class="inactive"><a href="javascript:void(0);"
 onclick="toggleLanguage('dotnet')">.NET</a></li>
<li id="syn-python" class="inactive"><a href="javascript:void(0);"
 onclick="toggleLanguage('python')">Python</a></li>
</ul></div>
<div class="indexlink"><a href="index.html">Operators</a></div>
{body}
<!--OP_REF_FOOTER_START-->
<hr>
<div class="footer"><div class="copyright">Copyright MVTec</div></div>
</div></body></html>
"""


# 假的 latexconvert：選檔後 0.2 秒把結果寫進 textarea.latex-output
_OCR_OK = r"""<!DOCTYPE html><html><body>
<input type="file" id="f" accept="image/*">
<textarea class="latex-output" placeholder="LaTeX 代碼將在此處顯示..."></textarea>
<script>
document.getElementById('f').addEventListener('change', () => {
  setTimeout(() => {
    document.querySelector('textarea.latex-output').value = 'FAKE \\alpha';
  }, 200);
});
</script></body></html>"""

# 假的 latexconvert（失敗版）：永遠不會出現結果
_OCR_FAIL = (
    '<!DOCTYPE html><html><body><input type="file" id="f">'
    '<textarea class="latex-output"></textarea></body></html>'
)


def _lang_js() -> str:
    """從真實樣本頁取出語言切換的 JavaScript，避免手抄。"""
    html = (FIXTURES / "abs_image.html").read_text(encoding="utf-8")
    for match in re.finditer(r"<script[^>]*>(.*?)</script>", html, re.S):
        if "toggleLanguage" in match.group(1):
            return match.group(1)
    raise RuntimeError("樣本頁找不到語言切換腳本")


def make_page(title: str, body: str) -> str:
    """以迷你網站樣板包裝頁面內容。"""
    return _TEMPLATE.format(title=title, js=_lang_js(), body=body)


def _mini_pages() -> dict[str, str]:
    op_name = _SPAN.format(hd="op_one", net="OpOne", py="op_one_py")
    stub = (
        "<p>Use the tabs on the upper right to switch to a different "
        "programming language.</p>"
    )
    return {
        "index.html": make_page(
            "Index",
            '<h2>Top</h2><p><a href="toc_a.html">Cat A</a> '
            '<a href="../outside.html">out</a> '
            '<a href="https://example.org/x.html">ext</a></p>',
        ),
        "toc_a.html": make_page(
            "Cat A",
            "<h2>Cat A</h2><dl>"
            f'<dt><a href="op_one.html"><code>{op_name}</code></a></dt>'
            "<dd>Does one thing.</dd></dl><dl>"
            '<dt><a href="HThing.html"><code>HThing</code></a></dt>'
            "<dd>A thing.</dd></dl>",
        ),
        "op_one.html": make_page(
            "op_one",
            f"<h1>{op_name} (Operator)</h1><h2>Name</h2>"
            f"<p><code>{op_name}</code> — Does one thing.</p>"
            '<p>Formula: <span title="1" class="displaymath">'
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 5" '
            'width="2em"><path d="M0 0L10 5"/></svg></span></p>'
            '<p>See <a href="HThing.html">HThing</a>, '
            '<a href="missing.html">missing</a>, '
            '<a href="#Param">Param</a>.</p>'
            '<pre class="example">\nop_one (A, B)\n</pre>',
        ),
        "HThing.html": make_page(
            "HThing",
            f'<div data-if="hdevelop" style="display:inline">{stub}</div>'
            '<div data-if="dotnet" style="display:none">'
            "<h1>HThing (Class)</h1><h2>Name</h2>"
            "<p><code>HThing</code> — A thing.</p></div>"
            f'<div data-if="python" style="display:none">{stub}</div>',
        ),
    }


def build_site(root: Path) -> None:
    """在 root 下建立 ``en/``（真實樣本）與 ``mini/``（迷你網站）。"""
    en = root / "en"
    en.mkdir(parents=True, exist_ok=True)
    for name in REAL_PAGES:
        shutil.copy(FIXTURES / f"{name}.html", en / f"{name}.html")
    mini = root / "mini"
    mini.mkdir(parents=True, exist_ok=True)
    for name, html in _mini_pages().items():
        (mini / name).write_text(html, encoding="utf-8")
    ocr = root / "ocr"
    ocr.mkdir(parents=True, exist_ok=True)
    (ocr / "index.html").write_text(_OCR_OK, encoding="utf-8")
    (ocr / "fail.html").write_text(_OCR_FAIL, encoding="utf-8")
```

在 `_mini_pages()` 回傳的字典中另外加入一個「不是文件頁」的樣本（放在 `"HThing.html"` 項目之後）：

```python
        "plain.html": (
            "<!DOCTYPE html><html><body><p>not a doc page</p></body></html>"
        ),
```

`tests/conftest.py`：

```python
"""測試共用 fixture：以本機 HTTP 伺服器提供樣本網站。"""
from __future__ import annotations

import http.server
import threading
from collections.abc import Iterator
from pathlib import Path

import pytest

from .site_builder import build_site


@pytest.fixture(scope="session")
def fixture_server(tmp_path_factory: pytest.TempPathFactory) -> Iterator[str]:
    """啟動本機伺服器，回傳網址前綴 ``http://127.0.0.1:<port>``。"""
    root: Path = tmp_path_factory.mktemp("site")
    build_site(root)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, directory=str(root), **kwargs)

        def log_message(self, format: str, *args) -> None:  # noqa: A002
            """靜音，避免測試輸出被請求記錄淹沒。"""

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
```

- [ ] **Step 2: 寫失敗測試**

`tests/test_extractor.py`：

```python
"""extract_page 的整合測試（需要 Playwright Chromium）。"""
from __future__ import annotations

import asyncio

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills.extractor import PageExtract, PageFetchError, extract_page

pytestmark = pytest.mark.browser


def _extract(url: str) -> PageExtract:
    async def go() -> PageExtract:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                return await extract_page(page, url)
            finally:
                await browser.close()

    return asyncio.run(go())


def test_each_language_keeps_only_its_own_content(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    hd = result.html_by_lang["hdevelop"]
    net = result.html_by_lang["dotnet"]
    py = result.html_by_lang["python"]

    assert "(Operator)" in hd and "AbsImage" not in hd
    assert "<b>abs_image</b>(" in hd
    assert "HOperatorSet" in net and "AbsImage" in net
    # 只有 Python 的簽名帶型別註記（原頁面以 &nbsp; 分隔 def 與函式名稱）
    assert "-&gt; HObject" not in hd and "-&gt; HObject" not in net
    assert "-&gt; HObject" in py and "HOperatorSet" not in py
    # 其他語言（含永遠隱藏的 cpp / c）的標記元素都不應殘留
    for lang, html in result.html_by_lang.items():
        for other in ("hdevelop", "dotnet", "python", "cpp", "c"):
            if other != lang:
                assert f'data-if="{other}"' not in html


def test_chrome_around_content_is_removed(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    for html in result.html_by_lang.values():
        assert 'class="tabbar"' not in html
        assert 'class="indexlink"' not in html
        assert "Copyright" not in html
        assert "OP_REF_FOOTER_START" not in html
        assert "<script" not in html


def test_metadata_title_breadcrumb_and_links(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/abs_image.html")
    assert "abs_image" in result.title
    assert result.breadcrumb[0][0].startswith("HALCON")  # 不含 logo 連結
    assert result.breadcrumb[-1][0] == "Arithmetic"
    assert all(href.startswith("http") for _, href in result.breadcrumb)
    # 只出現在 .NET 分頁的連結也要收集到
    assert any(link.endswith("/HImage.html") for link in result.links)


def test_inline_svg_keeps_viewbox_case(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/threshold.html")
    hd = result.html_by_lang["hdevelop"]
    assert "<svg" in hd and "viewBox" in hd


def test_class_page_is_stub_except_dotnet(fixture_server: str) -> None:
    result = _extract(f"{fixture_server}/en/HBarCode.html")
    assert "Use the tabs on the upper right" in result.html_by_lang["hdevelop"]
    assert "Use the tabs on the upper right" in result.html_by_lang["python"]
    assert "HBarCode (Class)" in result.html_by_lang["dotnet"]


def test_missing_page_raises_non_retryable_error(fixture_server: str) -> None:
    with pytest.raises(PageFetchError) as info:
        _extract(f"{fixture_server}/en/no_such_page.html")
    assert info.value.status == 404
    assert info.value.retryable is False


def test_non_doc_page_raises(fixture_server: str) -> None:
    with pytest.raises(PageFetchError) as info:
        _extract(f"{fixture_server}/mini/plain.html")
    assert info.value.retryable is False
```

- [ ] **Step 3: 執行確認失敗**

Run: `uv run pytest tests/test_extractor.py -v`
Expected: FAIL（`ImportError: cannot import name 'extract_page'`）

- [ ] **Step 4: 實作 extract_page**

將 `src/halcon_doc_skills/extractor.py` 改為（保留 Task 3 的 `PageFetchError`、`PageExtract` 不變，新增 import、常數與函式）：

```python
"""以 Playwright 取出各語言的可見頁面內容。"""
from __future__ import annotations

import logging
from collections.abc import Sequence
from dataclasses import dataclass

from playwright.async_api import Page

from . import config

log = logging.getLogger(__name__)

# 頁尾標記：其後是 <hr>、版權與社群圖示，不屬於內容
FOOTER_MARKER = "<!--OP_REF_FOOTER_START-->"

_TAB_SELECTOR = "#syn-{lang} a"

# 在頁面內執行：把目前隱藏的 data-if 元素標記後複製 .body_main，
# 從複本移除標記元素、script、分頁列、索引連結與頁尾
_VISIBLE_JS = r"""
() => {
  const marked = [];
  for (const el of document.querySelectorAll('[data-if]')) {
    if (getComputedStyle(el).display === 'none') {
      el.setAttribute('data-hh-hidden', '1');
      marked.push(el);
    }
  }
  const root = document.querySelector('.body_main') || document.body;
  const clone = root.cloneNode(true);
  for (const el of marked) el.removeAttribute('data-hh-hidden');
  const drop = '[data-hh-hidden], script, .tabbar, .indexlink, .footer';
  for (const el of clone.querySelectorAll(drop)) el.remove();
  const clean = (s) => s.replace(/\s+/g, ' ').trim();
  return {
    html: clone.innerHTML,
    images: [...clone.querySelectorAll('img[src]')].map((i) => i.src),
    links: [...document.querySelectorAll('a[href]')].map((a) => a.href),
    breadcrumb: [...document.querySelectorAll('.breadcrumb a')]
      .map((a) => [clean(a.textContent), a.href])
      .filter(([text]) => text !== ''),
    title: document.title,
  };
}
"""


class PageFetchError(Exception):
    """頁面載入失敗或不是 HALCON 文件頁。"""

    def __init__(self, message: str, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status

    @property
    def retryable(self) -> bool:
        """網路錯誤、5xx 與 429 值得重試；其他（如 404）不重試。"""
        return self.status is None or self.status >= 500 or self.status == 429


@dataclass
class PageExtract:
    """單一頁面的擷取結果。"""

    url: str
    title: str
    breadcrumb: list[tuple[str, str]]
    links: list[str]
    image_urls: list[str]
    html_by_lang: dict[str, str]


async def extract_page(
    page: Page,
    url: str,
    langs: Sequence[str] = config.LANGS,
    timeout_ms: int = 60_000,
) -> PageExtract:
    """載入頁面一次，逐語言點擊分頁並取出可見內容。

    :param page: Playwright 分頁。
    :param url: 要擷取的頁面網址。
    :param langs: 要擷取的語言（對應 ``#syn-<lang>`` 分頁）。
    :param timeout_ms: 載入與點擊的逾時毫秒數。
    :return: 各語言的可見 HTML 與頁面中繼資料。
    :raises PageFetchError: 回應非 200，或頁面不是 HALCON 文件頁。
    """
    response = await page.goto(url, wait_until="load", timeout=timeout_ms)
    status = response.status if response is not None else None
    if status != 200:
        raise PageFetchError(f"{url} 回應狀態 {status}", status=status)
    if await page.locator("#syn-hdevelop").count() == 0:
        raise PageFetchError(f"{url} 不是 HALCON 文件頁", status=200)

    html_by_lang: dict[str, str] = {}
    links: dict[str, None] = {}
    images: dict[str, None] = {}
    title = ""
    breadcrumb: list[tuple[str, str]] = []
    for lang in langs:
        await page.click(_TAB_SELECTOR.format(lang=lang), timeout=timeout_ms)
        data = await page.evaluate(_VISIBLE_JS)
        html_by_lang[lang] = data["html"].partition(FOOTER_MARKER)[0]
        links.update(dict.fromkeys(data["links"]))
        images.update(dict.fromkeys(data["images"]))
        title = data["title"]
        breadcrumb = [(text, href) for text, href in data["breadcrumb"]]
    log.debug("擷取完成：%s", url)
    return PageExtract(
        url=url,
        title=title,
        breadcrumb=breadcrumb,
        links=list(links),
        image_urls=list(images),
        html_by_lang=html_by_lang,
    )
```

- [ ] **Step 5: 執行確認通過**

Run: `uv run pytest tests/test_extractor.py tests/test_cache.py -v && uv run ruff check`
Expected: extractor 7 passed、cache 5 passed；ruff 無錯誤。若 `test_each_language_keeps_only_its_own_content` 的斷言與實際 HTML 有落差，先用 `uv run python -c` 印出該語言的 `html_by_lang` 內容，確認是**斷言預期**錯誤還是**擷取邏輯**錯誤；修正擷取邏輯，不要放寬成無意義的斷言。

- [ ] **Step 6: Commit**

```bash
git add src/halcon_doc_skills/extractor.py tests/site_builder.py tests/conftest.py tests/test_extractor.py
git commit -m "feat: 新增 Playwright 逐語言可見內容擷取器
--- feat ---
1. 新增 extract_page 逐語言點擊分頁並取可見 DOM
2. 新增連結、圖片網址與麵包屑收集
3. 新增 404 與非文件頁的錯誤判斷
4. 新增測試網站建構器與本機伺服器 fixture"
```

---

### Task 5: 公式解碼與快取（formulas.py）

**Files:**
- Create: `src/halcon_doc_skills/formulas.py`
- Test: `tests/test_formulas.py`

**Interfaces:**
- Consumes: `PageCache`（Task 3，僅用 `pages()`、`load_html()`、`langs`）；瀏覽器測試另用 `extract_page`（Task 4）。
- Produces:
  `FORMULA_RE`（公式容器 `span.math` / `span.displaymath` + 內含的 `<svg>`；具名群組 `cls`、`svg`）、
  `TOKEN_RE`、
  `class Reject(Exception)`（訊息為原因代碼，如 `cmex`、`rule`、`multi-baseline`、`code:cmsy10_9`、`font:foo12`、`unparsed-use`、`no-defs`、`empty`、`nested-script`、`script-first`）、
  `@dataclass(frozen=True) class FormulaResult`：`latex: str`、`source: str`（`decode` 或 `ocr`）、
  `formula_key(svg: str) -> str`（原始 SVG 字串 SHA-1 前 16 碼）、
  `collect_formula_svgs(html: str) -> list[tuple[str, bool]]`（`(svg, 是否獨立公式)`）、
  `decode_svg(svg: str) -> str`、
  `make_token(key: str, display: bool, asset: str | None) -> str`、
  `render_tokens(markdown: str, formulas: Mapping[str, FormulaResult], rel_assets: str) -> str`、
  `class FormulaStore(root: Path)`：`path(key)`、`has(key)`、`load(key) -> dict`、`save(key, data: dict)`、`keys() -> list[str]`（已排序）、`results() -> dict[str, FormulaResult]`（只含已有 LaTeX 者）、`pending_ocr(max_attempts: int = 2) -> list[tuple[str, str]]`（`(key, svg)`）；存檔欄位 `svg`、`latex`、`source`、`reject`、`ocr_attempts`（OCR 失敗時另有 `ocr_error`）、
  `class DecodeReport`：`total`、`decoded`、`rejected: Counter`（依原因代碼前綴）、`keys: set[str]`、
  `scan_and_decode(cache: PageCache, store: FormulaStore) -> DecodeReport`（掃描所有頁面與語言的公式；新公式解碼後存入；尚無 LaTeX 的舊公式重試解碼；已有 OCR 結果者不覆寫）。

- [ ] **Step 1: 寫失敗測試**

`tests/test_formulas.py`：

```python
"""formulas：字形解碼、公式標記與快取的測試。"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills import formulas
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract, extract_page
from halcon_doc_skills.formulas import (
    FormulaResult,
    FormulaStore,
    Reject,
    collect_formula_svgs,
    decode_svg,
    formula_key,
    make_token,
    render_tokens,
    scan_and_decode,
)

FIXTURES = Path(__file__).parent / "fixtures"
KEY = "0123456789abcdef"


def _svgs(page: str) -> list[str]:
    """取出樣本頁面內所有公式的 SVG。"""
    html = (FIXTURES / f"{page}.html").read_text(encoding="utf-8")
    return [svg for svg, _ in collect_formula_svgs(html)]


def _svg(*groups, extra: str = "") -> str:
    """合成公式 SVG。groups：``(tx, ty, [(字型, 字碼, x 偏移或 None), ...])``。"""
    parts = ["<svg><defs></defs>"]
    for tx, ty, uses in groups:
        parts.append(f'<g transform="matrix(1.6,0,0,1.6,{tx},{ty})">')
        for font, code, x in uses:
            attr = f' x="{x}"' if x is not None else ""
            parts.append(f'<use xlink:href="#GLYPH{font}_{code}"{attr}></use>')
        parts.append("</g>")
    parts.append(f"{extra}</svg>")
    return "".join(parts)


def _reason(svg: str) -> str:
    with pytest.raises(Reject) as info:
        decode_svg(svg)
    return str(info.value)


# ── 真實公式 ─────────────────────────────────────────────


@pytest.mark.parametrize(
    "page, index, expected",
    [
        ("threshold", 0, r"\texttt{MinGray}\le g\le\texttt{MaxGray}."),
        (
            "dyn_threshold",
            2,
            r"g_{t}-\texttt{Offset}\le g_{o}\le g_{t}+\texttt{Offset}",
        ),
        ("determinant_matrix", 0, r"\texttt{Value}=\det \texttt{Matrix}."),
        ("affine_trans_image", 2, r"B_{max}=0.5\cdot S\cdot I/2^{15}"),
        ("create_dl_layer_affine_grid", 2, r"(x^{\prime},y^{\prime})"),
        (
            "harmonic_interpolation",
            1,
            r"u_{xx}(x,y)=u(x-1,y)-2u(x,y)+u(x+1,y)",
        ),
        ("set_lut", 0, r"g\_min"),
        ("find_shape_model_3d", 1, r"(\infty)"),
    ],
)
def test_real_formulas_decode(page: str, index: int, expected: str) -> None:
    assert decode_svg(_svgs(page)[index]) == expected


@pytest.mark.parametrize(
    "page, index, reason",
    [
        ("hom_mat2d_rotate", 0, "cmex"),
        ("create_dl_layer_lrn", 2, "rule"),
        ("cooc_feature_image", 0, "multi-baseline"),
        ("gray_erosion", 0, "code:cmsy10_9"),
    ],
)
def test_real_formulas_are_rejected(page: str, index: int, reason: str) -> None:
    assert _reason(_svgs(page)[index]) == reason


# ── 合成公式：上下標、字型、串接 ─────────────────────────


def test_subscript_superscript_and_both() -> None:
    x = (0, 10, [("cmmi10", 120, None)])
    assert decode_svg(_svg(x, (10, 12, [("cmmi7", 105, None)]))) == "x_{i}"
    assert decode_svg(_svg(x, (10, 8, [("cmmi7", 105, None)]))) == "x^{i}"
    both = _svg(x, (10, 12, [("cmmi7", 105, None)]), (10, 8, [("cmmi7", 106, None)]))
    assert decode_svg(both) == "x_{i}^{j}"


def test_font_kinds_and_spacing() -> None:
    tt = _svg((0, 10, [("pcrr8r", 65, None), ("pcrr8r", 66, 6.0)]))
    assert decode_svg(tt) == r"\texttt{AB}"
    words = _svg((0, 10, [("ptmr8r", 97, None)]), (10, 10, [("ptmr8r", 98, None)]))
    assert decode_svg(words) == r"\text{a b}"
    rm = _svg(
        (0, 10, [("cmr10", 52, None)]),
        (10, 10, [("cmr10", 115, None), ("cmr10", 105, 3.0), ("cmr10", 110, 6.0)]),
    )
    assert decode_svg(rm) == r"4\sin"
    assert decode_svg(_svg((0, 10, [("cmmi10", 25, None)]))) == r"\pi"


def test_command_followed_by_letter_gets_a_space() -> None:
    gamma, x = (0, 10, [("cmmi10", 13, None)]), (10, 10, [("cmmi10", 120, None)])
    assert decode_svg(_svg(gamma, x)) == r"\gamma x"  # 不能變成 \gammax
    le = (10, 10, [("cmsy10", 20, None)])
    assert decode_svg(_svg(gamma, le, (20, 10, [("cmmi10", 120, None)]))) == (
        r"\gamma\le x"
    )


# ── 拒絕條件（寧可拒絕也不猜測）─────────────────────────


def test_reject_reasons() -> None:
    x = (0, 10, [("cmmi10", 120, None)])
    assert _reason(_svg(x, (0, 30, [("cmmi10", 121, None)]))) == "multi-baseline"
    assert _reason(_svg(x, extra='<path d="M0 0"/>')) == "rule"
    assert _reason(_svg((0, 10, [("cmex10", 50, None)]))) == "cmex"
    assert _reason(_svg((0, 10, [("cmr10", 200, None)]))) == "code:cmr10_200"
    assert _reason(_svg((0, 10, [("foo12", 65, None)]))) == "font:foo12"
    assert _reason(_svg(x, (10, 12, [("cmmi5", 105, None)]))) == "nested-script"
    assert _reason(_svg((0, 10, [("cmmi7", 105, None)]), (10, 10, x[2]))) == (
        "script-first"
    )
    assert _reason("<svg><defs></defs></svg>") == "empty"
    assert _reason("<svg></svg>") == "no-defs"


def test_unparsed_use_is_rejected_instead_of_dropping_glyphs() -> None:
    svg = _svg((0, 10, [("cmr10", 65, None)])).replace(
        "</g>", '<use xlink:href="#weird"></use></g>'
    )
    assert _reason(svg) == "unparsed-use"


# ── 公式容器、鍵、標記 ───────────────────────────────────


def test_collect_formula_svgs_reports_display_flag_and_ignores_other_svgs() -> None:
    html = (
        '<p><span title="1" class="math"><!-- c --><svg id="a"><defs></defs></svg>'
        '</span><span title="2" class="displaymath"><svg id="b"></svg></span>'
        '<a><svg id="logo"></svg></a></p>'
    )
    found = collect_formula_svgs(html)
    assert [display for _, display in found] == [False, True]
    assert 'id="logo"' not in "".join(svg for svg, _ in found)


def test_formula_key_is_stable_16_hex() -> None:
    assert formula_key("<svg/>") == formula_key("<svg/>")
    assert len(formula_key("<svg/>")) == 16 and formula_key("a") != formula_key("b")


def test_make_token_and_render_tokens() -> None:
    assert make_token(KEY, True, None) == f"@@FORMULA:{KEY}:d:-@@"
    assert make_token(KEY, False, "a.svg") == f"@@FORMULA:{KEY}:i:a.svg@@"

    results = {KEY: FormulaResult(r"a_{i}\le b*c", "decode")}
    md = f"if {make_token(KEY, False, None)} then\n\n{make_token(KEY, True, None)}\n"
    assert render_tokens(md, results, "../assets") == (
        "if $a_{i}\\le b*c$ then\n\n$$a_{i}\\le b*c$$\n"
    )


def test_render_tokens_ocr_appends_image_and_collapses_whitespace() -> None:
    results = {KEY: FormulaResult("a\n   b", "ocr")}
    md = make_token(KEY, False, "x.svg")
    assert render_tokens(md, results, "../assets") == "$a b$ ![figure](../assets/x.svg)"


def test_render_tokens_leaves_unknown_tokens_visible() -> None:
    token = make_token(KEY, False, None)
    assert render_tokens(token, {}, "../assets") == token


# ── 快取與掃描 ───────────────────────────────────────────


def test_store_results_and_pending_ocr(tmp_path: Path) -> None:
    store = FormulaStore(tmp_path / "latex")
    a, b, c = "a" * 16, "b" * 16, "c" * 16
    base = {"latex": None, "source": None, "reject": "cmex"}
    store.save(a, {"svg": "<svg/>", "latex": "x", "source": "decode", "reject": None,
                   "ocr_attempts": 0})
    store.save(b, {**base, "svg": "<svg>b</svg>", "ocr_attempts": 0})
    store.save(c, {**base, "svg": "<svg>c</svg>", "ocr_attempts": 2})
    assert store.keys() == [a, b, c]
    assert store.results() == {a: FormulaResult("x", "decode")}
    assert store.pending_ocr() == [(b, "<svg>b</svg>")]


def _cache_with(tmp_path: Path, html: str) -> PageCache:
    cache = PageCache(tmp_path / "cache")
    cache.save(
        "p.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/p.html",
            title="p",
            breadcrumb=[],
            links=[],
            image_urls=[],
            html_by_lang={lang: html for lang in cache.langs},
        ),
    )
    return cache


def _wrap(svg: str, cls: str = "displaymath") -> str:
    return f'<p><span title="1" class="{cls}"><!-- c -->{svg}</span></p>'


def test_scan_and_decode_stores_results_and_is_idempotent(tmp_path: Path) -> None:
    good, bad = _svgs("threshold")[0], _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(good) + _wrap(bad))
    store = FormulaStore(tmp_path / "latex")

    report = scan_and_decode(cache, store)
    assert (report.total, report.decoded) == (2, 1)
    assert dict(report.rejected) == {"cmex": 1}
    assert report.keys == {formula_key(good), formula_key(bad)}
    assert store.results()[formula_key(good)] == FormulaResult(
        r"\texttt{MinGray}\le g\le\texttt{MaxGray}.", "decode"
    )
    assert [key for key, _ in store.pending_ocr()] == [formula_key(bad)]

    again = scan_and_decode(cache, store)
    assert (again.total, again.decoded) == (2, 1)
    assert len(store.keys()) == 2


def test_previously_rejected_formulas_are_retried(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    bad = _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(bad))
    store = FormulaStore(tmp_path / "latex")
    scan_and_decode(cache, store)
    assert store.results() == {}

    monkeypatch.setattr(formulas, "decode_svg", lambda svg: "X")  # 模擬對照表補齊
    report = scan_and_decode(cache, store)
    assert report.decoded == 1
    assert store.results()[formula_key(bad)] == FormulaResult("X", "decode")


def test_ocr_results_are_not_overwritten(tmp_path: Path) -> None:
    bad = _svgs("hom_mat2d_rotate")[0]
    cache = _cache_with(tmp_path, _wrap(bad))
    store = FormulaStore(tmp_path / "latex")
    scan_and_decode(cache, store)
    key = formula_key(bad)
    data = store.load(key)
    data.update(latex="Y", source="ocr")
    store.save(key, data)

    report = scan_and_decode(cache, store)
    assert report.decoded == 0
    assert store.results()[key] == FormulaResult("Y", "ocr")


# ── 經過瀏覽器序列化後仍可解碼 ───────────────────────────


@pytest.mark.browser
def test_decode_survives_browser_serialization(fixture_server: str) -> None:
    async def go() -> PageExtract:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                return await extract_page(page, f"{fixture_server}/en/threshold.html")
            finally:
                await browser.close()

    result = asyncio.run(go())
    found = collect_formula_svgs(result.html_by_lang["hdevelop"])
    assert len(found) == 1
    assert decode_svg(found[0][0]) == r"\texttt{MinGray}\le g\le\texttt{MaxGray}."
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_formulas.py -v`
Expected: FAIL（`ModuleNotFoundError: halcon_doc_skills.formulas`）

- [ ] **Step 3: 實作 formulas.py**

以下是完整內容（已在 140 個真實公式上驗證：可解碼 93 個，其餘依原因被拒；不重複的 66 個解碼結果以 KaTeX 嚴格模式檢查皆為合法 LaTeX）：

```python
"""公式處理：由 MetaPost SVG 的字形還原 LaTeX，並管理結果快取。

站上的公式是 MetaPost 排版後的行內 SVG，每個字元都是
``<use xlink:href="#GLYPH<字型>_<字碼>">``。只要字型與字碼對照表齊全、
版面單純（單一基線，最多一層上下標），就能不靠 OCR 精確還原。
其餘情況一律拋出 ``Reject``，交給備援（OCR）或保留原圖。
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cache import PageCache

# 公式容器：span.math（行內）或 span.displaymath（獨立），內含註解與 <svg>
FORMULA_RE = re.compile(
    r'<span\b[^>]*\bclass="(?P<cls>displaymath|math)"[^>]*>'
    r"(?:\s*<!--.*?-->)?\s*(?P<svg><svg\b.*?</svg>)\s*</span>",
    re.DOTALL,
)
# converter 在 Markdown 產生後才把此標記換成 LaTeX，避免被 markdownify 跳脫
TOKEN_RE = re.compile(r"@@FORMULA:([0-9a-f]{16}):([di]):([^@\s]+)@@")

_GREEK_UPPER = [
    r"\Gamma", r"\Delta", r"\Theta", r"\Lambda", r"\Xi", r"\Pi",
    r"\Sigma", r"\Upsilon", r"\Phi", r"\Psi", r"\Omega",
]  # fmt: skip
_GREEK_LOWER = [
    r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon", r"\zeta",
    r"\eta", r"\theta", r"\iota", r"\kappa", r"\lambda", r"\mu", r"\nu",
    r"\xi", r"\pi", r"\rho", r"\sigma", r"\tau", r"\upsilon", r"\phi",
    r"\chi", r"\psi", r"\omega", r"\varepsilon", r"\vartheta", r"\varpi",
    r"\varrho", r"\varsigma", r"\varphi",
]  # fmt: skip


def _ascii(codes: Iterable[int]) -> dict[int, str]:
    return {code: chr(code) for code in codes}


# cmr10：羅馬字型。數字、標點、字母沿用 ASCII 位置
_CMR = _ascii(range(33, 127))
for _code in (34, 92, 94, 95, 96, 123, 124, 125, 126):
    _CMR.pop(_code, None)
_CMR.update(dict(enumerate(_GREEK_UPPER)))
_CMR.update({123: "-", 124: "--"})

# cmmi10：數學斜體。字母沿用 ASCII 位置，另有希臘字母
_CMMI = dict(enumerate(_GREEK_UPPER))
_CMMI.update({11 + i: name for i, name in enumerate(_GREEK_LOWER)})
_CMMI.update({58: ".", 59: ",", 60: "<", 61: "/", 62: ">", 64: r"\partial"})
_CMMI.update(_ascii(list(range(65, 91)) + list(range(97, 123))))

# cmsy10：數學符號（只收錄常見者；查不到的字碼會退回備援）
_CMSY = {
    0: "-", 1: r"\cdot", 2: r"\times", 3: r"\ast", 4: r"\div", 6: r"\pm",
    7: r"\mp", 14: r"\circ", 15: r"\bullet", 17: r"\equiv", 18: r"\subseteq",
    19: r"\supseteq", 20: r"\le", 21: r"\ge", 24: r"\sim", 25: r"\approx",
    26: r"\subset", 27: r"\supset", 28: r"\ll", 29: r"\gg",
    32: r"\leftarrow", 33: r"\rightarrow", 36: r"\leftrightarrow",
    40: r"\Leftarrow", 41: r"\Rightarrow", 44: r"\Leftrightarrow",
    47: r"\propto", 48: r"\prime", 49: r"\infty", 50: r"\in", 51: r"\ni",
    56: r"\forall", 57: r"\exists", 58: r"\neg", 59: r"\emptyset",
    62: r"\top", 63: r"\bot", 91: r"\cup", 92: r"\cap", 94: r"\wedge",
    95: r"\vee", 102: r"\{", 103: r"\}", 106: "|", 107: r"\|",
    110: r"\setminus", 114: r"\nabla",
}  # fmt: skip
_CMSY.update({code: rf"\mathcal{{{chr(code)}}}" for code in range(65, 91)})

_ASCII_TEXT = _ascii(range(33, 127))
_ASCII_TEXT[34] = '"'

# 字型家族 → (種類, 字碼對照表)
_FAMILY = {
    "cmr": ("rm", _CMR),
    "cmmi": ("math", _CMMI),
    "cmsy": ("sym", _CMSY),
    "pcrr": ("tt", _ASCII_TEXT),
    "ptmr": ("text", _ASCII_TEXT),
    "ptmri": ("textit", _ASCII_TEXT),
    "cmti": ("textit", _ASCII_TEXT),
    "cmbx": ("bf", _CMR),
}
_FONT_RE = re.compile(r"^(?:(cmr|cmmi|cmsy|cmex|cmti|cmbx)(\d+)|(pcrr|ptmr|ptmri)8r)$")
_WRAP = {
    "tt": r"\texttt",
    "text": r"\text",
    "textit": r"\textit",
    "bf": r"\mathbf",
}
_FUNCTIONS = {
    "sin", "cos", "tan", "cot", "sec", "csc", "exp", "log", "ln", "min",
    "max", "det", "arg", "lim", "sup", "inf", "deg", "gcd", "sinh", "cosh",
    "tanh",
}  # fmt: skip
_TEXT_ESCAPES = {
    "#": r"\#", "$": r"\$", "%": r"\%", "&": r"\&", "_": r"\_",
    "{": r"\{", "}": r"\}", "^": r"\^{}", "~": r"\~{}",
}  # fmt: skip
# 同一條基線的容許誤差；超過視為多基線（分數、矩陣、多行）
_BASELINE_TOLERANCE = 1.0
_SCRIPT_OFFSET = 0.5


class Reject(Exception):
    """無法可靠解碼；訊息是簡短的原因代碼（用於統計）。"""


@dataclass(frozen=True)
class FormulaResult:
    """公式的 LaTeX 結果。``source`` 為 ``decode`` 或 ``ocr``。"""

    latex: str
    source: str


@dataclass(frozen=True)
class _Glyph:
    x: float
    y: float
    family: str
    size: int
    code: int
    group: int


def formula_key(svg: str) -> str:
    """公式 SVG（原始字串）的快取鍵。"""
    return hashlib.sha1(svg.encode("utf-8")).hexdigest()[:16]


def collect_formula_svgs(html: str) -> list[tuple[str, bool]]:
    """取出 HTML 內所有公式，回傳 ``(svg, 是否為獨立公式)`` 清單。"""
    return [
        (m.group("svg"), m.group("cls") == "displaymath")
        for m in FORMULA_RE.finditer(html)
    ]


def _split_font(name: str) -> tuple[str, int]:
    """``cmmi7`` → ``("cmmi", 7)``；``pcrr8r`` → ``("pcrr", 10)``。"""
    match = _FONT_RE.match(name)
    if not match:
        raise Reject(f"font:{name}")
    if match.group(1):
        return match.group(1), int(match.group(2))
    return match.group(3), 10


def _parse_glyphs(svg: str) -> list[_Glyph]:
    """依 x 座標排序取出所有字形；有任何無法處理的元素就拒絕。"""
    start = svg.find("</defs>")
    if start < 0:
        raise Reject("no-defs")
    body = svg[start:]
    if re.search(r"<(path|rect|line|polygon|circle|ellipse)\b", body):
        raise Reject("rule")  # 分數線、根號橫線等
    glyphs: list[_Glyph] = []
    groups = re.finditer(
        r'<g transform="matrix\(([^)]*)\)"[^>]*>(.*?)</g>', body, re.DOTALL
    )
    for index, group in enumerate(groups):
        matrix = [float(v) for v in re.split(r"[,\s]+", group.group(1).strip())]
        uses = re.finditer(
            r'<use xlink:href="#GLYPH([a-z0-9]+)_(\d+)"(?: x="([-\d.]+)")?',
            group.group(2),
        )
        for use in uses:
            family, size = _split_font(use.group(1))
            offset = float(use.group(3) or 0)
            glyphs.append(
                _Glyph(
                    x=matrix[4] + matrix[0] * offset,
                    y=matrix[5],
                    family=family,
                    size=size,
                    code=int(use.group(2)),
                    group=index,
                )
            )
    if not glyphs:
        raise Reject("empty")
    # 完整性檢查：解析到的字形數必須等於 <use> 數，避免靜默漏字
    if len(glyphs) != len(re.findall(r"<use\b", body)):
        raise Reject("unparsed-use")
    return sorted(glyphs, key=lambda g: g.x)


def _emit_run(kind: str, chars: list[str]) -> str:
    """把同種類的連續字元轉成 LaTeX 片段。"""
    if kind == "rm":  # 數字與標點直接輸出，連續字母包成 \mathrm 或函數名
        parts: list[str] = []
        i = 0
        while i < len(chars):
            if not chars[i].isalpha():
                parts.append(chars[i])
                i += 1
                continue
            j = i
            while j < len(chars) and chars[j].isalpha():
                j += 1
            word = "".join(chars[i:j])
            if word in _FUNCTIONS:
                parts.append(f"\\{word} ")
            else:
                parts.append(rf"\mathrm{{{word}}}")
            i = j
        return "".join(parts)
    if kind in _WRAP:
        text = "".join(chars)
        if not any(c.isalnum() for c in text):  # 純標點（如括號）不需要包 \text
            return "".join(_TEXT_ESCAPES.get(c, c) for c in text)
        escaped = "".join(_TEXT_ESCAPES.get(c, c) for c in chars)
        return f"{_WRAP[kind]}{{{escaped}}}"
    return _join(chars)  # math、sym：指令後接字母要補空白


def _render(items: list[tuple[str, str, int]]) -> str:
    """``(種類, 字元, 群組)`` 序列 → LaTeX。文字字型在群組邊界補空白。"""
    tokens: list[str] = []
    i = 0
    while i < len(items):
        kind = items[i][0]
        chars: list[str] = []
        j = i
        while j < len(items) and items[j][0] == kind:
            if j > i and kind in ("text", "textit", "tt"):
                if items[j][2] != items[j - 1][2]:
                    chars.append(" ")
            chars.append(items[j][1])
            j += 1
            if kind == "sym":  # 符號逐個輸出，避免相鄰指令黏在一起
                break
        tokens.append(_emit_run(kind, chars))
        i = j
    return _join(tokens)


def _join(tokens: list[str]) -> str:
    """串接片段；指令（如 ``\\le``）後面接字母時補一個空白。"""
    result = ""
    for token in tokens:
        if result and re.search(r"\\[A-Za-z]+$", result) and token[:1].isalpha():
            result += " "
        result += token
    return result.strip()


def decode_svg(svg: str) -> str:
    """由字形還原 LaTeX。

    :param svg: 公式的行內 SVG 字串。
    :return: LaTeX 字串（不含 ``$`` 定界符）。
    :raises Reject: 版面或字型超出可可靠解碼的範圍。
    """
    glyphs = _parse_glyphs(svg)
    for glyph in glyphs:
        if glyph.family == "cmex":  # 大括號、矩陣括號、根號、求和積分
            raise Reject("cmex")
        if glyph.code not in _FAMILY[glyph.family][1]:
            raise Reject(f"code:{glyph.family}{glyph.size}_{glyph.code}")
    mains = [g for g in glyphs if g.size >= 10]
    if not mains:
        raise Reject("no-main")
    base = collections.Counter(round(g.y, 1) for g in mains).most_common(1)[0][0]
    if any(abs(g.y - base) > _BASELINE_TOLERANCE for g in mains):
        raise Reject("multi-baseline")
    if any(g.size < 7 for g in glyphs):
        raise Reject("nested-script")

    atoms: list[dict] = []  # 每個主字形一個 atom，附帶它的上下標
    for glyph in glyphs:
        kind, table = _FAMILY[glyph.family]
        item = (kind, table[glyph.code], glyph.group)
        if glyph.size >= 10:
            atoms.append({"main": item, "sup": [], "sub": []})
            continue
        if not atoms:
            raise Reject("script-first")
        if glyph.y < base - _SCRIPT_OFFSET:
            atoms[-1]["sup"].append(item)
        elif glyph.y > base + _SCRIPT_OFFSET:
            atoms[-1]["sub"].append(item)
        else:
            raise Reject("script-on-baseline")

    segments: list[str] = []
    pending: list[tuple[str, str, int]] = []  # 尚未輸出的相鄰主字形
    for atom in atoms:
        pending.append(atom["main"])
        if not atom["sup"] and not atom["sub"]:
            continue
        segments.append(_render(pending))
        pending = []
        if atom["sub"]:
            segments[-1] += f"_{{{_render(atom['sub'])}}}"
        if atom["sup"]:
            segments[-1] += f"^{{{_render(atom['sup'])}}}"
    if pending:
        segments.append(_render(pending))
    return _join(segments)


def make_token(key: str, display: bool, asset: str | None) -> str:
    """產生給 converter 的公式標記；``asset`` 為 None 表示不附圖。"""
    return f"@@FORMULA:{key}:{'d' if display else 'i'}:{asset or '-'}@@"


def render_tokens(
    markdown: str, formulas: Mapping[str, FormulaResult], rel_assets: str
) -> str:
    """把 Markdown 中的公式標記換成 ``$…$`` / ``$$…$$``（OCR 結果另附圖檔）。"""

    def _replace(match: re.Match[str]) -> str:
        key, mode, asset = match.groups()
        result = formulas.get(key)
        if result is None:  # 標記沒有對應結果（不應發生）：保留提示便於 verify 抓到
            return match.group(0)
        latex = " ".join(result.latex.split())
        text = f"$${latex}$$" if mode == "d" else f"${latex}$"
        if asset != "-":
            text += f" ![figure]({rel_assets}/{asset})"
        return text

    return TOKEN_RE.sub(_replace, markdown)


@dataclass
class FormulaStore:
    """``cache/latex/<key>.json``：每個不同的公式一個檔。

    欄位：``svg``（原始 SVG）、``latex``（可為 None）、``source``、
    ``reject``（解碼被拒的原因）、``ocr_attempts``（OCR 已嘗試次數）。
    """

    root: Path

    def path(self, key: str) -> Path:
        return self.root / f"{key}.json"

    def has(self, key: str) -> bool:
        return self.path(key).exists()

    def load(self, key: str) -> dict:
        return json.loads(self.path(key).read_text(encoding="utf-8"))

    def save(self, key: str, data: dict) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        text = json.dumps(data, ensure_ascii=False, indent=1)
        self.path(key).write_text(text, encoding="utf-8")

    def keys(self) -> list[str]:
        if not self.root.exists():
            return []
        return sorted(p.stem for p in self.root.glob("*.json"))

    def results(self) -> dict[str, FormulaResult]:
        """所有已有 LaTeX 的公式。"""
        found: dict[str, FormulaResult] = {}
        for key in self.keys():
            data = self.load(key)
            if data.get("latex"):
                found[key] = FormulaResult(data["latex"], data["source"])
        return found

    def pending_ocr(self, max_attempts: int = 2) -> list[tuple[str, str]]:
        """尚無 LaTeX、且 OCR 嘗試次數未達上限的 ``(key, svg)``。"""
        pending: list[tuple[str, str]] = []
        for key in self.keys():
            data = self.load(key)
            if not data.get("latex") and data.get("ocr_attempts", 0) < max_attempts:
                pending.append((key, data["svg"]))
        return pending


@dataclass
class DecodeReport:
    """解碼統計。"""

    total: int = 0
    decoded: int = 0
    rejected: collections.Counter = field(default_factory=collections.Counter)
    keys: set[str] = field(default_factory=set)


def scan_and_decode(cache: PageCache, store: FormulaStore) -> DecodeReport:
    """掃描快取內所有公式，以字形解碼並存入 store。

    尚無 LaTeX 的舊公式也會重試解碼（字形對照表補齊後即可救回）。

    :param cache: 頁面快取。
    :param store: 公式結果快取。
    :return: 解碼統計（``rejected`` 依原因代碼分類）。
    """
    report = DecodeReport()
    seen: set[str] = set()
    for page in cache.pages():
        for lang in cache.langs:
            for svg, _display in collect_formula_svgs(cache.load_html(lang, page)):
                key = formula_key(svg)
                if key in seen:
                    continue
                seen.add(key)
                report.keys.add(key)
                report.total += 1
                data = store.load(key) if store.has(key) else _new_entry(svg)
                if data["latex"] is None:
                    try:
                        data.update(latex=decode_svg(svg), source="decode", reject=None)
                    except Reject as exc:
                        data["reject"] = str(exc)
                    store.save(key, data)
                if data["source"] == "decode":
                    report.decoded += 1
                elif data["latex"] is None:
                    report.rejected[data["reject"].split(":")[0]] += 1
    return report


def _new_entry(svg: str) -> dict:
    return {
        "svg": svg,
        "latex": None,
        "source": None,
        "reject": None,
        "ocr_attempts": 0,
    }
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_formulas.py -v && uv run ruff check`
Expected: 27 passed（含 1 個需要瀏覽器的測試）；ruff 無錯誤。若 `test_real_formulas_decode` 或 `test_real_formulas_are_rejected` 的某一項不符，先執行下列指令列出該頁實際的公式與解碼結果，確認是「站上內容變了」還是「解碼邏輯有誤」，再決定要更新預期值還是修正 `formulas.py`；**不可**為了讓測試通過而放寬 `Reject` 條件：

```bash
uv run python - <<'PY'
from pathlib import Path
from halcon_doc_skills.formulas import Reject, collect_formula_svgs, decode_svg
html = Path("tests/fixtures/dyn_threshold.html").read_text(encoding="utf-8")
for i, (svg, display) in enumerate(collect_formula_svgs(html)):
    try:
        print(i, "獨立" if display else "行內", decode_svg(svg))
    except Reject as exc:
        print(i, "被拒", exc)
PY
```

- [ ] **Step 5: Commit**

```bash
git add src/halcon_doc_skills/formulas.py tests/test_formulas.py
git commit -m "feat: 新增公式字形解碼與公式結果快取
--- feat ---
1. 新增以 SVG 字形還原 LaTeX 的 decode_svg
2. 新增無法可靠解碼時的 Reject 安全閘與字形完整性檢查
3. 新增公式標記與 render_tokens 換成行內與獨立公式
4. 新增 FormulaStore 與 scan_and_decode 掃描快取"
```

---

### Task 6: 圖片資產（assets.py）

**Files:**
- Create: `src/halcon_doc_skills/assets.py`
- Test: `tests/test_assets.py`

**Interfaces:**
- Consumes: `formulas.FORMULA_RE`、`FormulaResult`、`formula_key`、`make_token`（Task 5）。
- Produces:
  `normalize_svg(svg: str) -> str`（補 `xmlns`、必要時補 `xmlns:xlink`）、
  `svg_asset_name(svg: str) -> str`（內容 SHA-1 前 16 碼 + `.svg`）、
  `image_asset_name(url: str) -> str`（網址 SHA-1 前 16 碼 + 原副檔名，無副檔名用 `.bin`）、
  `extract_inline_svgs(html: str, assets_dir: Path, rel_prefix: str, formulas: Mapping[str, FormulaResult] | None = None) -> str`：
  1. 先處理公式容器（`span.math` / `span.displaymath` 內的 `<svg>`）：`formulas` 中有該公式（以 `formula_key(svg)` 查）→ 換成 `make_token(...)`；來源為 `decode` 不寫 `.svg`、不附圖，來源為 `ocr` 則寫 `.svg` 並在標記帶上檔名；查不到（或 `formulas` 為 None）→ 與一般 SVG 相同處理。
  2. 其餘每個 `<svg>…</svg>` 存成 `assets_dir/<name>.svg`（已存在則不覆寫），換成 `<img data-local="1" src="<rel_prefix>/<name>" alt="figure">`。

- [ ] **Step 1: 寫失敗測試**

`tests/test_assets.py`：

```python
"""圖片資產處理的測試。"""
from pathlib import Path

from halcon_doc_skills.assets import (
    extract_inline_svgs,
    image_asset_name,
    normalize_svg,
    svg_asset_name,
)
from halcon_doc_skills.formulas import FormulaResult, formula_key, make_token

SVG = '<svg viewBox="0 0 10 5" width="2em"><path d="M0 0L10 5"/></svg>'


def test_normalize_svg_adds_namespace() -> None:
    result = normalize_svg(SVG)
    assert 'xmlns="http://www.w3.org/2000/svg"' in result
    assert 'viewBox="0 0 10 5"' in result


def test_normalize_svg_keeps_existing_namespace_and_adds_xlink() -> None:
    svg = '<svg xmlns="http://www.w3.org/2000/svg"><use xlink:href="#a"/></svg>'
    result = normalize_svg(svg)
    assert result.count('xmlns="http://www.w3.org/2000/svg"') == 1
    assert 'xmlns:xlink="http://www.w3.org/1999/xlink"' in result


def test_asset_names_are_deterministic() -> None:
    assert svg_asset_name(SVG) == svg_asset_name(SVG)
    assert svg_asset_name(SVG).endswith(".svg")
    assert image_asset_name("https://x/a/pic.PNG?v=1") == image_asset_name(
        "https://x/a/pic.PNG?v=1"
    )
    assert image_asset_name("https://x/a/pic.PNG?v=1").endswith(".png")
    assert image_asset_name("https://x/a/noext").endswith(".bin")


def test_extract_inline_svgs_writes_file_and_replaces_tag(tmp_path: Path) -> None:
    html = f"<p>a {SVG} b</p>"
    result = extract_inline_svgs(html, tmp_path / "assets", "../assets")
    name = svg_asset_name(normalize_svg(SVG))
    assert f'<img data-local="1" src="../assets/{name}" alt="figure">' in result
    assert "<svg" not in result
    saved = (tmp_path / "assets" / name).read_text(encoding="utf-8")
    assert 'viewBox="0 0 10 5"' in saved
    assert 'xmlns="http://www.w3.org/2000/svg"' in saved


def test_identical_svgs_are_deduplicated(tmp_path: Path) -> None:
    html = f"<p>{SVG}</p><p>{SVG}</p>"
    extract_inline_svgs(html, tmp_path / "assets", "../assets")
    assert len(list((tmp_path / "assets").iterdir())) == 1


def _formula_html(svg: str, cls: str = "displaymath") -> str:
    return f'<p><span title="1" class="{cls}"><!-- c -->{svg}</span></p>'


def test_decoded_formula_becomes_token_without_asset(tmp_path: Path) -> None:
    key = formula_key(SVG)
    result = extract_inline_svgs(
        _formula_html(SVG),
        tmp_path / "assets",
        "../assets",
        {key: FormulaResult("x", "decode")},
    )
    assert result == f"<p>{make_token(key, True, None)}</p>"
    assert not (tmp_path / "assets").exists()


def test_ocr_formula_keeps_asset_and_marks_inline(tmp_path: Path) -> None:
    key = formula_key(SVG)
    result = extract_inline_svgs(
        _formula_html(SVG, "math"),
        tmp_path / "assets",
        "../assets",
        {key: FormulaResult("x", "ocr")},
    )
    name = svg_asset_name(normalize_svg(SVG))
    assert result == f"<p>{make_token(key, False, name)}</p>"
    assert (tmp_path / "assets" / name).exists()


def test_unresolved_formula_falls_back_to_image(tmp_path: Path) -> None:
    result = extract_inline_svgs(
        _formula_html(SVG), tmp_path / "assets", "../assets", {}
    )
    assert '<img data-local="1"' in result and "<span" not in result
    assert len(list((tmp_path / "assets").iterdir())) == 1


def test_non_formula_svg_is_still_an_image_when_formulas_given(
    tmp_path: Path,
) -> None:
    formulas = {formula_key(SVG): FormulaResult("x", "decode")}
    result = extract_inline_svgs(
        f'<a href="x">{SVG}</a>', tmp_path / "assets", "../assets", formulas
    )
    assert '<img data-local="1"' in result and "@@FORMULA" not in result


def test_multiline_svg_and_no_svg(tmp_path: Path) -> None:
    multi = '<svg viewBox="0 0 1 1">\n<g>\n</g>\n</svg>'
    result = extract_inline_svgs(multi, tmp_path / "assets", "../assets")
    assert result.startswith("<img")
    assert extract_inline_svgs("<p>none</p>", tmp_path / "a2", "..") == "<p>none</p>"
    assert not (tmp_path / "a2").exists()
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_assets.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: 實作 assets.py**

```python
"""圖片資產：行內 SVG 存檔與資產檔名規則。"""
from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

from .formulas import FORMULA_RE, FormulaResult, formula_key, make_token

_SVG_RE = re.compile(r"<svg\b.*?</svg>", re.DOTALL | re.IGNORECASE)
_SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'
_XLINK_NS = 'xmlns:xlink="http://www.w3.org/1999/xlink"'


def _digest(data: str) -> str:
    """回傳字串 SHA-1 的前 16 碼，用作檔名。"""
    return hashlib.sha1(data.encode("utf-8")).hexdigest()[:16]


def normalize_svg(svg: str) -> str:
    """補上獨立 SVG 檔所需的命名空間宣告。

    行內 SVG 在 HTML 中可省略 ``xmlns``，但存成 .svg 檔時必須有。
    """
    head = svg[: svg.index(">")]
    additions: list[str] = []
    if "xmlns=" not in head:
        additions.append(_SVG_NS)
    if "xlink:" in svg and "xmlns:xlink=" not in head:
        additions.append(_XLINK_NS)
    if not additions:
        return svg
    return svg.replace("<svg", "<svg " + " ".join(additions), 1)


def svg_asset_name(svg: str) -> str:
    """SVG 內容對應的資產檔名（相同內容得到相同檔名）。"""
    return f"{_digest(svg)}.svg"


def image_asset_name(url: str) -> str:
    """圖片網址對應的資產檔名，保留原副檔名。"""
    suffix = PurePosixPath(urlsplit(url).path).suffix.lower() or ".bin"
    return f"{_digest(url)}{suffix}"


def extract_inline_svgs(
    html: str,
    assets_dir: Path,
    rel_prefix: str,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> str:
    """把 HTML 中的行內 SVG 存成檔案並替換。

    需在 HTML 解析器處理之前呼叫，避免解析器把 ``viewBox`` 轉成小寫。

    :param html: 含行內 SVG 的 HTML 字串。
    :param assets_dir: 資產輸出資料夾（相同檔名已存在時不覆寫）。
    :param rel_prefix: 從 Markdown 檔到資產資料夾的相對路徑，如 ``../assets``。
    :param formulas: 公式鍵 → LaTeX 結果；None 表示不做公式轉換。
    :return: 公式換成 ``@@FORMULA…@@`` 標記（有結果者），其餘 SVG 換成
        ``<img data-local="1">``。
    """

    def _write(svg: str) -> str:
        svg = normalize_svg(svg)
        name = svg_asset_name(svg)
        path = assets_dir / name
        if not path.exists():
            assets_dir.mkdir(parents=True, exist_ok=True)
            path.write_text(svg, encoding="utf-8")
        return name

    def _image(svg: str) -> str:
        name = _write(svg)
        return f'<img data-local="1" src="{rel_prefix}/{name}" alt="figure">'

    def _formula(match: re.Match[str]) -> str:
        svg = match.group("svg")
        key = formula_key(svg)
        result = formulas.get(key) if formulas else None
        if result is None:
            return _image(svg)
        asset = None if result.source == "decode" else _write(svg)
        return make_token(key, match.group("cls") == "displaymath", asset)

    html = FORMULA_RE.sub(_formula, html)
    return _SVG_RE.sub(lambda match: _image(match.group(0)), html)
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_assets.py -v && uv run ruff check`
Expected: 10 passed；ruff 無錯誤。

- [ ] **Step 5: Commit**

```bash
git add src/halcon_doc_skills/assets.py tests/test_assets.py
git commit -m "feat: 新增圖片資產處理與行內 SVG 存檔
--- feat ---
1. 新增 extract_inline_svgs 將行內 SVG 存成檔案並換成 img
2. 新增公式容器依解碼或 OCR 結果換成公式標記
3. 新增 normalize_svg 補齊命名空間
4. 新增雜湊命名規則以去除重複圖片"
```

---

### Task 7: HTML → Markdown 轉換（converter.py）

**Files:**
- Create: `src/halcon_doc_skills/converter.py`
- Test: `tests/test_converter.py`

**Interfaces:**
- Consumes: `crawler.normalize_url / page_name / md_name`、`assets.extract_inline_svgs / image_asset_name`、`formulas.FormulaResult / render_tokens`、`config.STUB_MARKER`。
- Produces:
  `convert_page(html: str, page_url: str, lang: str, available: Collection[str], assets_dir: Path, formulas: Mapping[str, FormulaResult] | None = None) -> str`
  — `available` 為該語言「有輸出 .md 的頁面名稱」集合（如 `{"HImage.html"}`）；連結目標在 `available` → 相對 `.md` 路徑；範圍內但不在 `available` → 原站完整網址；範圍外 → 完整網址；`#…`、`javascript:`、指向自己 → 移除連結只留文字。公式：`formulas` 中有結果者 → 行內 `$…$`、獨立 `$$…$$`（LaTeX 不會被跳脫；OCR 結果另附 ` ![figure](…svg)`），沒有結果者與一般行內 SVG 相同；圖片：行內 SVG → `![figure](<rel>/assets/<hash>.svg)`；`<img src>` 若 `assets_dir/<image_asset_name(絕對網址)>` 存在 → 相對路徑，否則絕對網址。回傳結尾為單一換行的 Markdown。
  `is_stub_page(html: str) -> bool`（可見文字正規化後恰為 `config.STUB_MARKER`）。

- [ ] **Step 1: 寫失敗測試**

`tests/test_converter.py`：

```python
"""HTML → Markdown 轉換的測試（不需瀏覽器）。"""
from pathlib import Path

from halcon_doc_skills.assets import image_asset_name, normalize_svg, svg_asset_name
from halcon_doc_skills.converter import convert_page, is_stub_page
from halcon_doc_skills.formulas import FormulaResult, formula_key

ROOT = "https://www.mvtec.com/doc/halcon/2605/en/"
PAGE_URL = ROOT + "abs_image.html"


def _convert(
    html: str,
    tmp_path: Path,
    available: set[str] | None = None,
    page_url: str = PAGE_URL,
    lang: str = "python",
) -> str:
    return convert_page(html, page_url, lang, available or set(), tmp_path / "assets")


def test_headings_and_inline_code(tmp_path: Path) -> None:
    html = (
        "<h1>abs_image (Operator)</h1><h2>Name</h2>"
        "<p><code>abs_image</code> — Calculate the absolute value.</p>"
    )
    md = _convert(html, tmp_path)
    assert md.startswith("# abs_image (Operator)\n")
    assert "## Name" in md
    assert "`abs_image` — Calculate the absolute value." in md
    assert md.endswith("\n") and not md.endswith("\n\n")


def test_underscores_are_not_escaped(tmp_path: Path) -> None:
    md = _convert("<p>use abs_image and get_value</p>", tmp_path)
    assert "abs_image and get_value" in md


def test_pre_becomes_fenced_code(tmp_path: Path) -> None:
    md = _convert('<pre class="example">\nfoo (A, B)\nbar (B)\n</pre>', tmp_path)
    assert "```" in md
    assert "foo (A, B)\nbar (B)" in md


def test_table_becomes_pipe_table(tmp_path: Path) -> None:
    html = (
        "<table><tr><td><code>ReadBarCodeModel</code></td><td>Read a model."
        "</td></tr><tr><td><code>Other</code></td><td>Other.</td></tr></table>"
    )
    md = _convert(html, tmp_path)
    assert "|" in md and "ReadBarCodeModel" in md


def test_dl_becomes_bullet_list(tmp_path: Path) -> None:
    html = (
        '<dl><dt><a href="add_image.html"><code>add_image</code></a></dt>'
        "<dd>Add two images.</dd></dl>"
    )
    md = _convert(html, tmp_path, available={"add_image.html"})
    assert "- [`add_image`](add_image.md) — Add two images." in md


def test_noise_is_removed(tmp_path: Path) -> None:
    html = "<!--OP_REF_HEADER_END--><script>var a=1;</script><style>p{}</style><p>Hi</p>"
    md = _convert(html, tmp_path)
    assert md == "Hi\n"


def test_link_to_available_page_becomes_relative_md(tmp_path: Path) -> None:
    md = _convert('<a href="HImage.html#x">HImage</a>', tmp_path, {"HImage.html"})
    assert "[HImage](HImage.md)" in md


def test_link_to_unavailable_page_keeps_absolute_url(tmp_path: Path) -> None:
    md = _convert('<a href="HImage.html">HImage</a>', tmp_path, set())
    assert f"[HImage]({ROOT}HImage.html)" in md


def test_external_and_out_of_scope_links_are_absolute(tmp_path: Path) -> None:
    html = (
        '<a href="https://example.org/x">e</a> '
        '<a href="../../../../documentation.html">d</a>'
    )
    md = _convert(html, tmp_path)
    assert "[e](https://example.org/x)" in md
    assert "[d](https://www.mvtec.com/documentation.html)" in md


def test_anchor_javascript_and_self_links_are_unwrapped(tmp_path: Path) -> None:
    html = (
        '<a href="#Image"><i>Image</i></a> '
        '<a href="javascript:void(0);">js</a> '
        '<a href="abs_image.html#top">self</a> <a name="x">named</a>'
    )
    md = _convert(html, tmp_path, {"abs_image.html"})
    assert "](" not in md
    assert "Image" in md and "js" in md and "self" in md and "named" in md


def test_subdirectory_page_uses_relative_paths(tmp_path: Path) -> None:
    html = '<a href="../y.html">y</a> <svg viewBox="0 0 1 1"></svg>'
    md = _convert(html, tmp_path, {"y.html"}, page_url=ROOT + "sub/x.html")
    assert "[y](../y.md)" in md
    assert "![figure](../../assets/" in md


def test_inline_svg_becomes_image_with_asset_file(tmp_path: Path) -> None:
    html = (
        '<p>f <span title="1" class="displaymath">'
        '<svg viewBox="0 0 10 5"><path d="M0 0"/></svg></span></p>'
    )
    md = _convert(html, tmp_path)
    assert "![figure](../assets/" in md and ".svg)" in md
    files = list((tmp_path / "assets").glob("*.svg"))
    assert len(files) == 1
    text = files[0].read_text(encoding="utf-8")
    assert "viewBox" in text and 'xmlns="http://www.w3.org/2000/svg"' in text
    assert "data-local" not in md


def test_downloaded_image_uses_local_asset(tmp_path: Path) -> None:
    url = ROOT + "pic.png"
    assets = tmp_path / "assets"
    assets.mkdir()
    name = image_asset_name(url)
    (assets / name).write_bytes(b"png")
    md = _convert('<img src="pic.png" alt="A pic">', tmp_path)
    assert f"![A pic](../assets/{name})" in md


def test_missing_image_keeps_absolute_url(tmp_path: Path) -> None:
    md = _convert('<img src="pic.png" alt="A pic">', tmp_path)
    assert f"![A pic]({ROOT}pic.png)" in md


def test_images_survive_inside_headings_and_table_cells(tmp_path: Path) -> None:
    svg = '<svg viewBox="0 0 1 1"><path d="M0 0"/></svg>'
    md = _convert(f"<h2>Title {svg}</h2><table><tr><td>{svg}</td></tr></table>", tmp_path)
    assert md.count("![figure](../assets/") == 2


FORMULA_SVG = '<svg viewBox="0 0 1 1"><path d="M0 0"/></svg>'


def _formula_html() -> str:
    return (
        f'<p>if <span title="1" class="math">{FORMULA_SVG}</span> then '
        f'<span title="2" class="displaymath">{FORMULA_SVG}</span></p>'
    )


def test_decoded_formulas_become_latex_and_are_not_escaped(tmp_path: Path) -> None:
    latex = r"a_{i}\le b*[c]"
    formulas = {formula_key(FORMULA_SVG): FormulaResult(latex, "decode")}
    md = convert_page(
        _formula_html(), PAGE_URL, "python", set(), tmp_path / "assets", formulas
    )
    assert md == "if $a_{i}\\le b*[c]$ then $$a_{i}\\le b*[c]$$\n"
    assert not (tmp_path / "assets").exists()


def test_ocr_formula_gets_latex_and_original_image(tmp_path: Path) -> None:
    formulas = {formula_key(FORMULA_SVG): FormulaResult("x", "ocr")}
    html = f'<p><span title="1" class="math">{FORMULA_SVG}</span></p>'
    md = convert_page(html, PAGE_URL, "python", set(), tmp_path / "assets", formulas)
    name = svg_asset_name(normalize_svg(FORMULA_SVG))
    assert md == f"$x$ ![figure](../assets/{name})\n"
    assert (tmp_path / "assets" / name).exists()


def test_unresolved_formula_stays_an_image(tmp_path: Path) -> None:
    md = convert_page(
        _formula_html(), PAGE_URL, "python", set(), tmp_path / "assets", {}
    )
    assert md.count("![figure](../assets/") == 2 and "$" not in md


def test_is_stub_page() -> None:
    stub = (
        "<!--c--><p>Use the tabs on the upper right to switch to a\n"
        "different programming language.</p>"
    )
    assert is_stub_page(stub) is True
    assert is_stub_page(stub + "<h1>Real</h1>") is False
    assert is_stub_page("") is False
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_converter.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: 實作 converter.py**

```python
"""將單一語言的可見 HTML 轉成 Markdown。"""
from __future__ import annotations

import posixpath
import re
from collections.abc import Collection, Mapping
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Comment
from markdownify import markdownify

from . import config
from .assets import extract_inline_svgs, image_asset_name
from .crawler import md_name, normalize_url, page_name
from .formulas import FormulaResult, render_tokens

_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

# markdownify 預設會把標題、表格儲存格內的圖片降級成 alt 文字，這裡明確保留
_IMAGE_PARENTS = ["a", "h1", "h2", "h3", "h4", "h5", "h6", "td", "th", "li", "p"]


def convert_page(
    html: str,
    page_url: str,
    lang: str,
    available: Collection[str],
    assets_dir: Path,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> str:
    """將可見 HTML 轉成 Markdown。

    :param html: 某語言的可見內容 HTML（來自 ``PageCache``）。
    :param page_url: 該頁面的原站網址，用來解析相對連結。
    :param lang: 語言資料夾名稱，用來計算資產相對路徑。
    :param available: 該語言有輸出 .md 的頁面名稱集合。
    :param assets_dir: 共用資產資料夾（SVG 會寫入此處）。
    :param formulas: 公式鍵 → LaTeX 結果；None 表示不做公式轉換。
    :return: 結尾為單一換行的 Markdown 字串。
    """
    page = page_name(page_url)
    rel_assets = posixpath.relpath(
        "assets", posixpath.join(lang, posixpath.dirname(page))
    )
    html = extract_inline_svgs(html, assets_dir, rel_assets, formulas)
    soup = BeautifulSoup(html, "html.parser")
    _strip_noise(soup)
    _rewrite_images(soup, page_url, rel_assets, assets_dir)
    _rewrite_links(soup, page_url, page, available)
    _dl_to_list(soup)
    text = markdownify(
        str(soup),
        heading_style="ATX",
        bullets="-",
        escape_underscores=False,
        escape_asterisks=False,
        keep_inline_images_in=_IMAGE_PARENTS,
    )
    # 公式在 markdownify 之後才換回 LaTeX，避免 _、\\、*、[ 被跳脫
    text = render_tokens(text, formulas or {}, rel_assets)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def is_stub_page(html: str) -> bool:
    """判斷是否為只有「請切換語言」提示的空殼頁。"""
    soup = BeautifulSoup(_COMMENT_RE.sub("", html), "html.parser")
    return " ".join(soup.get_text().split()) == config.STUB_MARKER


def _strip_noise(soup: BeautifulSoup) -> None:
    """移除註解、script 與 style。"""
    for comment in soup.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()


def _rewrite_images(
    soup: BeautifulSoup, page_url: str, rel_assets: str, assets_dir: Path
) -> None:
    """已下載的圖片改指向本機資產，否則保留原站絕對網址。"""
    for img in soup.find_all("img"):
        if img.has_attr("data-local"):
            del img["data-local"]
            continue
        src = img.get("src")
        if not src:
            img.decompose()
            continue
        absolute = urljoin(page_url, src)
        name = image_asset_name(absolute)
        local = (assets_dir / name).exists()
        img["src"] = f"{rel_assets}/{name}" if local else absolute


def _rewrite_links(
    soup: BeautifulSoup, page_url: str, page: str, available: Collection[str]
) -> None:
    """改寫連結：本機可用 → 相對 .md；其餘 → 完整網址；頁內錨點 → 純文字。"""
    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if href is None:
            anchor.unwrap()
            continue
        href = href.strip()
        if href.startswith("#") or href.lower().startswith("javascript:"):
            anchor.unwrap()
            continue
        target = normalize_url(href, page_url)
        if target is None:
            anchor["href"] = urljoin(page_url, href)
            continue
        name = page_name(target)
        if name == page:
            anchor.unwrap()
        elif name in available:
            start = posixpath.dirname(page) or "."
            anchor["href"] = posixpath.relpath(md_name(name), start=start)
        else:
            anchor["href"] = target


def _dl_to_list(soup: BeautifulSoup) -> None:
    """將 ``<dl><dt/><dd/></dl>`` 轉成 ``<ul><li>dt — dd</li></ul>``。"""
    for dl in soup.find_all("dl"):
        bullets = soup.new_tag("ul")
        current = None
        for child in list(dl.children):
            name = getattr(child, "name", None)
            if name == "dt":
                current = soup.new_tag("li")
                current.extend(list(child.contents))
                bullets.append(current)
            elif name == "dd":
                if current is None:
                    current = soup.new_tag("li")
                    bullets.append(current)
                else:
                    current.append(" — ")
                current.extend(list(child.contents))
        dl.replace_with(bullets)
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_converter.py -v && uv run ruff check`
Expected: 19 passed；ruff 無錯誤。若因 markdownify 版本差異（如 `<pre>` 圍欄格式、表格是否補表頭列）導致個別斷言失敗，先印出實際輸出，只調整**斷言的寫法**使其驗證同一行為；不可改變上述介面。

- [ ] **Step 5: Commit**

```bash
git add src/halcon_doc_skills/converter.py tests/test_converter.py
git commit -m "feat: 新增 HTML 轉 Markdown 轉換器
--- feat ---
1. 新增 convert_page 轉換標題、程式碼、表格與清單
2. 新增內部連結改寫為同語言相對 md 路徑
3. 新增行內 SVG 與圖片改寫為本機資產連結
4. 新增 is_stub_page 判斷空殼類別頁"
```

---

### Task 8: 索引產生（indexer.py）

**Files:**
- Create: `src/halcon_doc_skills/indexer.py`
- Test: `tests/test_indexer.py`

**Interfaces:**
- Consumes: `crawler.md_name`。
- Produces:
  `@dataclass(frozen=True) class IndexEntry`：`name: str`（頁面路徑如 `abs_image.html`）、`title: str`、`summary: str`、`category: str`。
  `category_from_breadcrumb(breadcrumb: Sequence[Sequence[str]]) -> str`（略過前 2 層「HALCON x / Operator Reference」，其餘以 ` / ` 連接；為空 → `Other`）。
  `read_title_and_summary(md: str, page: str) -> tuple[str, str]`。
  `build_index(lang: str, entries: Sequence[IndexEntry]) -> str`。

- [ ] **Step 1: 寫失敗測試**

`tests/test_indexer.py`：

```python
"""索引產生的測試。"""
from halcon_doc_skills.indexer import (
    IndexEntry,
    build_index,
    category_from_breadcrumb,
    read_title_and_summary,
)


def test_operator_title_and_summary() -> None:
    md = (
        "# abs_image (Operator)\n\n## Name\n\n"
        "`abs_image` — Calculate the absolute value.\n"
    )
    assert read_title_and_summary(md, "abs_image.html") == (
        "abs_image",
        "Calculate the absolute value.",
    )


def test_class_title_strips_suffix() -> None:
    md = "# HBarCode (Class)\n\n## Name\n\n`HBarCode` — Reads bar codes.\n"
    assert read_title_and_summary(md, "HBarCode.html") == (
        "HBarCode",
        "Reads bar codes.",
    )


def test_toc_page_uses_first_heading_and_no_summary() -> None:
    assert read_title_and_summary("## Arithmetic\n\ntext\n", "toc_a.html") == (
        "Arithmetic",
        "",
    )


def test_title_falls_back_to_page_stem() -> None:
    assert read_title_and_summary("just text\n", "sub/abs_image.html") == (
        "abs_image",
        "",
    )


def test_category_from_breadcrumb() -> None:
    crumbs = [
        ("HALCON 26.05.0.0", "u"),
        ("HALCON Operator Reference", "u"),
        ("Filters", "u"),
        ("Arithmetic", "u"),
    ]
    assert category_from_breadcrumb(crumbs) == "Filters / Arithmetic"
    assert category_from_breadcrumb(crumbs[:2]) == "Other"
    assert category_from_breadcrumb([]) == "Other"


def test_build_index_groups_sorts_and_links() -> None:
    entries = [
        IndexEntry("b_op.html", "b_op", "Second.", "Filters / Arithmetic"),
        IndexEntry("a_op.html", "a_op", "First.", "Filters / Arithmetic"),
        IndexEntry("toc_filters.html", "Filters", "", "Other"),
        IndexEntry("HThing.html", "HThing", "", "Other"),
    ]
    text = build_index("python", entries)
    assert text.startswith("# HALCON 26.05 Reference Index (python)\n")
    assert text.index("## Table of Contents") < text.index("## Filters / Arithmetic")
    assert "- [Filters](toc_filters.md)" in text
    assert "- [a_op](a_op.md) — First." in text
    assert text.index("a_op.md") < text.index("b_op.md")
    assert "## Other" in text and "- [HThing](HThing.md)" in text
    assert text.endswith("\n")
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_indexer.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: 實作 indexer.py**

```python
"""產生各語言資料夾的 INDEX.md。"""
from __future__ import annotations

import posixpath
import re
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass

from .crawler import md_name

_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
_SUFFIX_RE = re.compile(r"\s*\((?:Operator|Class)\)\s*$")
_SUMMARY_RE = re.compile(r"^## Name\s*\n+[^\n]*?—\s*([^\n]+)", re.MULTILINE)

# 麵包屑前兩層是「HALCON 版本」與「HALCON Operator Reference」，不屬於分類
_BREADCRUMB_SKIP = 2


@dataclass(frozen=True)
class IndexEntry:
    """索引中的一筆頁面。"""

    name: str
    title: str
    summary: str
    category: str


def category_from_breadcrumb(breadcrumb: Sequence[Sequence[str]]) -> str:
    """由麵包屑取得分類路徑，例如 ``Filters / Arithmetic``。"""
    texts = [item[0] for item in breadcrumb][_BREADCRUMB_SKIP:]
    return " / ".join(texts) or "Other"


def read_title_and_summary(md: str, page: str) -> tuple[str, str]:
    """從轉換後的 Markdown 取出標題與一句話摘要。"""
    match = _HEADING_RE.search(md)
    if match:
        title = _SUFFIX_RE.sub("", match.group(1))
    else:
        title = posixpath.splitext(posixpath.basename(page))[0]
    summary_match = _SUMMARY_RE.search(md)
    summary = summary_match.group(1).strip() if summary_match else ""
    return title, summary


def _line(entry: IndexEntry) -> str:
    link = f"[{entry.title}]({md_name(entry.name)})"
    return f"- {link} — {entry.summary}" if entry.summary else f"- {link}"


def build_index(lang: str, entries: Sequence[IndexEntry]) -> str:
    """產生索引 Markdown：先列目錄頁，再依分類列出其餘頁面。"""
    lines = [f"# HALCON 26.05 Reference Index ({lang})", ""]
    toc = sorted(
        (e for e in entries if e.name.startswith("toc_")), key=lambda e: e.name
    )
    if toc:
        lines += ["## Table of Contents", ""]
        lines += [_line(e) for e in toc] + [""]
    by_category: dict[str, list[IndexEntry]] = defaultdict(list)
    for entry in entries:
        if not entry.name.startswith("toc_"):
            by_category[entry.category].append(entry)
    for category in sorted(by_category):
        lines += [f"## {category}", ""]
        ordered = sorted(
            by_category[category], key=lambda e: (e.title.lower(), e.name)
        )
        lines += [_line(e) for e in ordered] + [""]
    return "\n".join(lines).rstrip() + "\n"
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_indexer.py -v && uv run ruff check`
Expected: 6 passed；ruff 無錯誤。

- [ ] **Step 5: Commit**

```bash
git add src/halcon_doc_skills/indexer.py tests/test_indexer.py
git commit -m "feat: 新增各語言 INDEX.md 產生器
--- feat ---
1. 新增標題與摘要擷取
2. 新增由麵包屑推導分類
3. 新增依分類分組並排序的索引輸出"
```

---

### Task 9: OCR 備援（ocr.py）

**Files:**
- Create: `src/halcon_doc_skills/ocr.py`
- Test: `tests/test_ocr.py`

**Interfaces:**
- Consumes: `FormulaStore`（Task 5，用 `pending_ocr()`、`load()`、`save()`）、`assets.normalize_svg`（Task 6）、`tests/site_builder.py` 的 `ocr/index.html`、`ocr/fail.html`（Task 4）。
- Produces:
  `LATEXCONVERT_URL: str`（`https://latexconvert.com/zh/`，測試以 monkeypatch 改成本機假網站）、
  `class OcrError(Exception)`、
  `@dataclass(frozen=True) class OcrOptions`：`delay: float = 5.0`、`max_count: int = 500`、`timeout_ms: int = 60_000`、`headless: bool = True`、
  `@dataclass class OcrReport`：`done: int`、`failed: int`、
  `async def render_png(page: Page, svg: str, path: Path) -> None`、
  `async def ocr_png(page: Page, png: Path, timeout_ms: int) -> str`、
  `async def ocr_pending(store: FormulaStore, options: OcrOptions | None = None) -> OcrReport`：依 `store.pending_ocr()` 的順序（依鍵排序）最多處理 `max_count` 筆；每筆先把 `ocr_attempts` 加 1；成功寫入 `latex` 與 `source="ocr"`；失敗寫入 `ocr_error`；連續失敗 3 次立即停止；每筆之間等待 `delay` 秒。

**重要限制（實作與測試都必須遵守）：**
- 只驅動網頁介面，**不得**直接請求 `https://latexconvert.com/convert`（`robots.txt` 對該路徑為 Disallow）。
- 自動化測試**一律使用本機假網站**，不得連線 latexconvert.com。
- 選擇器（2026/09/30 實測）：檔案輸入 `input[type="file"]`、結果 `textarea.latex-output`（上傳後才出現非空內容）。

- [ ] **Step 1: 寫失敗測試**

`tests/test_ocr.py`：

```python
"""ocr 備援的測試：一律使用本機假網站，不連線 latexconvert.com。"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from playwright.async_api import async_playwright

from halcon_doc_skills import ocr
from halcon_doc_skills.assets import normalize_svg
from halcon_doc_skills.formulas import FormulaStore, collect_formula_svgs, formula_key
from halcon_doc_skills.ocr import OcrOptions, ocr_pending

pytestmark = pytest.mark.browser

FIXTURES = Path(__file__).parent / "fixtures"


def _base_svg() -> str:
    html = (FIXTURES / "threshold.html").read_text(encoding="utf-8")
    return collect_formula_svgs(html)[0][0]


def _store(tmp_path: Path, count: int) -> tuple[FormulaStore, list[str]]:
    """建立 count 個「解碼被拒、等待 OCR」的公式（SVG 各不相同）。"""
    store = FormulaStore(tmp_path / "latex")
    keys = []
    for i in range(count):
        svg = _base_svg().replace("<svg", f'<svg data-n="{i}"', 1)
        key = formula_key(svg)
        keys.append(key)
        store.save(
            key,
            {"svg": svg, "latex": None, "source": None, "reject": "cmex",
             "ocr_attempts": 0},
        )
    return store, sorted(keys)


def _use(monkeypatch: pytest.MonkeyPatch, base: str, page: str) -> None:
    monkeypatch.setattr(ocr, "LATEXCONVERT_URL", f"{base}/ocr/{page}")


def test_render_png_writes_a_png(tmp_path: Path) -> None:
    png = tmp_path / "f.png"

    async def go() -> None:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            try:
                page = await browser.new_page()
                await ocr.render_png(page, normalize_svg(_base_svg()), png)
            finally:
                await browser.close()

    asyncio.run(go())
    assert png.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_ocr_reads_result_from_fake_site(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "index.html")
    store, keys = _store(tmp_path, 2)
    report = asyncio.run(ocr_pending(store, OcrOptions(delay=0, timeout_ms=10_000)))

    assert (report.done, report.failed) == (2, 0)
    result = store.results()[keys[0]]
    assert (result.latex, result.source) == (r"FAKE \alpha", "ocr")
    assert store.load(keys[0])["ocr_attempts"] == 1
    assert store.pending_ocr() == []


def test_max_count_limits_processing(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "index.html")
    store, _ = _store(tmp_path, 3)
    report = asyncio.run(
        ocr_pending(store, OcrOptions(delay=0, max_count=1, timeout_ms=10_000))
    )
    assert report.done == 1
    assert len(store.pending_ocr()) == 2


def test_stops_after_three_consecutive_failures(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "fail.html")
    store, keys = _store(tmp_path, 5)
    report = asyncio.run(ocr_pending(store, OcrOptions(delay=0, timeout_ms=1_500)))

    assert (report.done, report.failed) == (0, 3)
    attempts = [store.load(key)["ocr_attempts"] for key in keys]
    assert attempts == [1, 1, 1, 0, 0]
    assert all(store.load(key).get("ocr_error") for key in keys[:3])


def test_each_formula_is_attempted_at_most_twice(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _use(monkeypatch, fixture_server, "fail.html")
    store, keys = _store(tmp_path, 1)
    options = OcrOptions(delay=0, timeout_ms=1_000)
    for expected in (1, 2, 2):
        asyncio.run(ocr_pending(store, options))
        assert store.load(keys[0])["ocr_attempts"] == expected
    assert store.pending_ocr() == []
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_ocr.py -v`
Expected: FAIL（`ModuleNotFoundError: halcon_doc_skills.ocr`）

- [ ] **Step 3: 實作 ocr.py**

以下內容已在真實網站上以 2 個「解碼被拒」的公式（分數＋求和、矩陣）各上傳一次驗證過：

```python
"""備援：以 latexconvert.com 的網頁介面對 SVG 公式做 OCR。

只驅動網頁介面，不直接呼叫該站的 ``/convert`` 端點（robots.txt 對該路徑
為 Disallow）。循序執行、請求間隔至少數秒、有筆數上限，連續失敗即停止。
"""

from __future__ import annotations

import asyncio
import logging
import tempfile
from dataclasses import dataclass
from pathlib import Path

from playwright.async_api import Error as PlaywrightError
from playwright.async_api import Page, async_playwright, expect

from .assets import normalize_svg
from .formulas import FormulaStore

log = logging.getLogger(__name__)

LATEXCONVERT_URL = "https://latexconvert.com/zh/"
# 上傳後，LaTeX 結果會出現在這個 textarea（2026/09/30 實測）
_OUTPUT_SELECTOR = "textarea.latex-output"
_MAX_CONSECUTIVE_FAILURES = 3


class OcrError(Exception):
    """OCR 沒有產生結果。"""


@dataclass(frozen=True)
class OcrOptions:
    """OCR 備援的節流與上限。"""

    delay: float = 5.0
    max_count: int = 500
    timeout_ms: int = 60_000
    headless: bool = True


@dataclass
class OcrReport:
    """OCR 統計。"""

    done: int = 0
    failed: int = 0


async def render_png(page: Page, svg: str, path: Path) -> None:
    """把公式 SVG 轉成白底 PNG（該網站只接受 JPEG/PNG/GIF/WebP）。"""
    await page.set_content(
        f'<body style="margin:12px;background:#fff;font-size:20px">{svg}</body>'
    )
    await page.locator("svg").first.screenshot(path=str(path))


async def ocr_png(page: Page, png: Path, timeout_ms: int) -> str:
    """上傳 PNG 並讀取 LaTeX 結果。

    :raises OcrError: 逾時內沒有出現結果。
    """
    await page.goto(LATEXCONVERT_URL, wait_until="load", timeout=timeout_ms)
    await page.locator('input[type="file"]').first.set_input_files(str(png))
    output = page.locator(_OUTPUT_SELECTOR)
    try:
        await expect(output).not_to_have_value("", timeout=timeout_ms)
    except AssertionError as exc:
        raise OcrError("等不到 OCR 結果") from exc
    return (await output.input_value()).strip()


async def ocr_pending(
    store: FormulaStore, options: OcrOptions | None = None
) -> OcrReport:
    """對 store 中尚無 LaTeX 的公式逐一 OCR，結果寫回 store。"""
    options = options or OcrOptions()
    todo = store.pending_ocr()[: options.max_count]
    report = OcrReport()
    if not todo:
        return report
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=options.headless)
        try:
            render_ctx = await browser.new_context(device_scale_factor=3)
            ocr_ctx = await browser.new_context()
            render_page = await render_ctx.new_page()
            ocr_page = await ocr_ctx.new_page()
            failures = 0
            with tempfile.TemporaryDirectory() as tmp:
                for number, (key, svg) in enumerate(todo, start=1):
                    data = store.load(key)
                    data["ocr_attempts"] = data.get("ocr_attempts", 0) + 1
                    png = Path(tmp) / f"{key}.png"
                    try:
                        await render_png(render_page, normalize_svg(svg), png)
                        latex = await ocr_png(ocr_page, png, options.timeout_ms)
                    except (OcrError, PlaywrightError) as exc:
                        failures += 1
                        report.failed += 1
                        data["ocr_error"] = str(exc).splitlines()[0]
                        log.warning("OCR 失敗 [%d/%d]：%s", number, len(todo), exc)
                    else:
                        failures = 0
                        if latex:
                            data.update(latex=latex, source="ocr")
                            report.done += 1
                        else:
                            report.failed += 1
                        log.info("OCR [%d/%d] %s", number, len(todo), key)
                    store.save(key, data)
                    if failures >= _MAX_CONSECUTIVE_FAILURES:
                        log.error("連續失敗 %d 次，停止 OCR", failures)
                        break
                    await asyncio.sleep(options.delay)
        finally:
            await browser.close()
    return report
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_ocr.py -v && uv run ruff check`
Expected: 5 passed；ruff 無錯誤。

- [ ] **Step 5: （可選）對真實網站做一次冒煙測試**

只在需要確認選擇器仍然有效時執行，**一次只上傳一個公式**（這會把一張公開文件中的公式圖片送到 latexconvert.com）：

```bash
uv run python - <<'PY'
import asyncio
from pathlib import Path

from halcon_doc_skills.formulas import FormulaStore, collect_formula_svgs, formula_key
from halcon_doc_skills.ocr import OcrOptions, ocr_pending

html = Path("tests/fixtures/hom_mat2d_rotate.html").read_text(encoding="utf-8")
svg = collect_formula_svgs(html)[0][0]
store = FormulaStore(Path("cache/latex_smoke"))
store.save(formula_key(svg), {"svg": svg, "latex": None, "source": None,
                              "reject": "cmex", "ocr_attempts": 0})
print(asyncio.run(ocr_pending(store, OcrOptions(max_count=1))))
print([r.latex for r in store.results().values()])
PY
```
Expected: `OcrReport(done=1, failed=0)`，並印出一段含 `\begin{...}` 或 `\left[` 的 LaTeX。若失敗，請檢查 `textarea.latex-output` 是否仍存在（網站可能改版），只更新 `ocr.py` 頂端的 `_OUTPUT_SELECTOR`。完成後刪除 `cache/latex_smoke`。

- [ ] **Step 6: Commit**

```bash
git add src/halcon_doc_skills/ocr.py tests/test_ocr.py
git commit -m "feat: 新增 latexconvert OCR 備援
--- feat ---
1. 新增 ocr_pending 驅動網頁介面對被拒公式做 OCR
2. 新增 SVG 轉 PNG 與結果讀取
3. 新增節流、筆數上限與連續失敗停止保護
4. 新增以本機假網站進行的測試"
```

---

### Task 10: 爬取與轉換流程（pipeline.py）

**Files:**
- Create: `src/halcon_doc_skills/pipeline.py`
- Test: `tests/test_pipeline.py`

**Interfaces:**
- Consumes: `PageCache`（Task 3）、`extract_page` / `PageFetchError`（Task 4）、`assets.image_asset_name`（Task 6）、`convert_page` / `is_stub_page`（Task 7）、`FormulaResult` / `FormulaStore` / `scan_and_decode`（Task 5）、`OcrOptions` / `ocr_pending`（Task 9）、`IndexEntry` / `build_index` / `category_from_breadcrumb` / `read_title_and_summary`（Task 8）、`Frontier` / `normalize_url` / `page_name` / `md_name`（Task 2）。
- Produces:
  `@dataclass class CrawlReport`：`fetched: int = 0`、`skipped: int = 0`、`failed: list[str]`（失敗網址）。
  `@dataclass class ConvertReport`：`converted: dict[str, int]`、`skipped_stubs: dict[str, int]`（皆以語言為鍵）。
  `async def crawl(cache: PageCache, output_dir: Path, *, concurrency: int = 4, limit: int | None = None, force: bool = False, delay: float = 0.3, retries: int = 3, entries: Sequence[str] | None = None, headless: bool = True) -> CrawlReport`
  — `entries` 為相對於 `config.BASE_URL` 的入口頁；`None` 時用 `config.ENTRY_PAGES`。已完成的頁面（且未 `force`）只讀 `meta` 內的連結繼續往下走。圖片下載到 `output_dir/assets/<image_asset_name(url)>`。
  `@dataclass class FormulaReport`：`total`、`decoded`、`ocr`、`unresolved`（保留圖檔）、`rejected: Counter[str]`（被字形解碼拒絕的原因分布）。
  `def resolve_formulas(cache: PageCache, store: FormulaStore, ocr_options: OcrOptions | None = None) -> FormulaReport`
  — 先 `scan_and_decode`；`ocr_options` 不為 None 時再對被拒的公式做 OCR（`asyncio.run(ocr_pending(...))`）；統計只計算目前快取內出現的公式。
  `def convert_all(cache: PageCache, output_dir: Path, langs: Sequence[str] = config.LANGS, formulas: Mapping[str, FormulaResult] | None = None) -> ConvertReport`。

- [ ] **Step 1: 寫失敗測試**

`tests/test_pipeline.py`：

```python
"""crawl 與 convert_all 的測試。"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from halcon_doc_skills import config, ocr
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.extractor import PageExtract
from halcon_doc_skills.formulas import FormulaStore, collect_formula_svgs
from halcon_doc_skills.ocr import OcrOptions
from halcon_doc_skills.pipeline import convert_all, crawl, resolve_formulas

FIXTURES = Path(__file__).parent / "fixtures"

ROOT = "https://www.mvtec.com/doc/halcon/2605/en/"
STUB = (
    "<p>Use the tabs on the upper right to switch to a different "
    "programming language.</p>"
)


def _save(cache: PageCache, page: str, html_by_lang: dict[str, str]) -> None:
    cache.save(
        page,
        PageExtract(
            url=ROOT + page,
            title=page,
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang=html_by_lang,
        ),
    )


def test_convert_all_skips_stub_pages_and_falls_back_to_absolute_links(
    tmp_path: Path,
) -> None:
    cache = PageCache(tmp_path / "cache")
    op = '<h1>op (Operator)</h1><p><a href="HThing.html">HThing</a></p>'
    _save(cache, "op.html", {"hdevelop": op, "dotnet": op, "python": op})
    _save(
        cache,
        "HThing.html",
        {
            "hdevelop": STUB,
            "dotnet": "<h1>HThing (Class)</h1>",
            "python": STUB,
        },
    )
    out = tmp_path / "output"
    report = convert_all(cache, out)

    assert report.converted == {"hdevelop": 1, "dotnet": 2, "python": 1}
    assert report.skipped_stubs == {"hdevelop": 1, "dotnet": 0, "python": 1}
    assert not (out / "hdevelop" / "HThing.md").exists()
    assert (out / "dotnet" / "HThing.md").exists()
    assert "[HThing](HThing.md)" in (out / "dotnet" / "op.md").read_text("utf-8")
    assert f"[HThing]({ROOT}HThing.html)" in (out / "python" / "op.md").read_text(
        "utf-8"
    )
    assert "HThing.md" not in (out / "python" / "INDEX.md").read_text("utf-8")
    assert "HThing.md" in (out / "dotnet" / "INDEX.md").read_text("utf-8")


@pytest.fixture
def mini_site(fixture_server: str, monkeypatch: pytest.MonkeyPatch) -> str:
    """將網址範圍指向本機迷你網站。"""
    monkeypatch.setattr(config, "BASE_HOST", fixture_server.removeprefix("http://"))
    monkeypatch.setattr(config, "SCOPE_PREFIX", "/mini/")
    monkeypatch.setattr(config, "BASE_URL", f"{fixture_server}/mini/")
    monkeypatch.setattr(config, "ENTRY_PAGES", ("index.html",))
    return fixture_server


@pytest.mark.browser
def test_crawl_follows_links_records_failures_and_converts(
    mini_site: str, tmp_path: Path
) -> None:
    cache = PageCache(tmp_path / "cache")
    out = tmp_path / "output"
    report = asyncio.run(
        crawl(cache, out, concurrency=2, retries=3, delay=0)
    )

    assert cache.pages() == ["HThing.html", "index.html", "op_one.html", "toc_a.html"]
    assert report.fetched == 4
    assert len(report.failed) == 1 and report.failed[0].endswith("/mini/missing.html")
    assert "missing.html" in cache.failed_path.read_text(encoding="utf-8")

    convert_all(cache, out)
    py = (out / "python" / "op_one.md").read_text(encoding="utf-8")
    net = (out / "dotnet" / "op_one.md").read_text(encoding="utf-8")
    assert "op_one_py" in py and "OpOne" not in py
    assert "OpOne" in net
    assert "op_one (A, B)" in py and "](#Param)" not in py
    assert f"[HThing]({mini_site}/mini/HThing.html)" in py
    assert f"[missing]({mini_site}/mini/missing.html)" in py
    assert "[HThing](HThing.md)" in net
    assert "![figure](../assets/" in py
    assert len(list((out / "assets").glob("*.svg"))) == 1
    assert not (out / "hdevelop" / "HThing.md").exists()
    assert not (out / "python" / "HThing.md").exists()
    assert "HThing (Class)" in (out / "dotnet" / "HThing.md").read_text("utf-8")
    index = (out / "python" / "INDEX.md").read_text(encoding="utf-8")
    assert "## Cat A" in index
    assert "[op_one_py](op_one.md) — Does one thing." in index


@pytest.mark.browser
def test_second_run_resumes_from_cache_and_keeps_traversing(
    mini_site: str, tmp_path: Path
) -> None:
    cache = PageCache(tmp_path / "cache")
    out = tmp_path / "output"
    asyncio.run(crawl(cache, out, concurrency=2, retries=1, delay=0))
    report = asyncio.run(crawl(cache, out, concurrency=2, retries=1, delay=0))

    assert report.fetched == 0
    assert report.skipped == 4
    assert len(report.failed) == 1  # missing.html 仍會被重新嘗試
    assert len(cache.pages()) == 4


@pytest.mark.browser
def test_limit_and_entries_override(mini_site: str, tmp_path: Path) -> None:
    cache = PageCache(tmp_path / "limit")
    asyncio.run(crawl(cache, tmp_path / "o1", limit=2, retries=1, delay=0))
    assert len(cache.pages()) == 2

    cache2 = PageCache(tmp_path / "entries")
    asyncio.run(
        crawl(
            cache2,
            tmp_path / "o2",
            entries=["op_one.html"],
            limit=1,
            retries=1,
            delay=0,
        )
    )
    assert cache2.pages() == ["op_one.html"]


def _formula_svgs() -> tuple[str, str]:
    """一個可字形解碼的公式與一個會被拒絕的公式（矩陣）。"""

    def first(page: str) -> str:
        html = (FIXTURES / f"{page}.html").read_text(encoding="utf-8")
        return collect_formula_svgs(html)[0][0]

    return first("threshold"), first("hom_mat2d_rotate")


def _formula_cache(tmp_path: Path) -> PageCache:
    good, bad = _formula_svgs()
    html = (
        "<h1>op (Operator)</h1>"
        f'<p><span title="1" class="displaymath"><!-- c -->{good}</span></p>'
        f'<p><span title="2" class="math"><!-- c -->{bad}</span></p>'
    )
    cache = PageCache(tmp_path / "cache")
    _save(cache, "op.html", {"hdevelop": html, "dotnet": html, "python": html})
    return cache


def test_resolve_formulas_reports_and_convert_all_writes_latex(tmp_path: Path) -> None:
    cache = _formula_cache(tmp_path)
    store = FormulaStore(tmp_path / "cache" / "latex")
    report = resolve_formulas(cache, store)

    assert (report.total, report.decoded, report.ocr, report.unresolved) == (2, 1, 0, 1)
    assert dict(report.rejected) == {"cmex": 1}

    out = tmp_path / "output"
    convert_all(cache, out, formulas=store.results())
    for lang in config.LANGS:
        md = (out / lang / "op.md").read_text(encoding="utf-8")
        assert r"$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$" in md
        assert md.count("![figure](../assets/") == 1  # 被拒的公式保留圖檔
        assert "@@FORMULA" not in md
    assert len(list((out / "assets").glob("*.svg"))) == 1


@pytest.mark.browser
def test_ocr_fallback_end_to_end_with_fake_site(
    fixture_server: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(ocr, "LATEXCONVERT_URL", f"{fixture_server}/ocr/index.html")
    cache = _formula_cache(tmp_path)
    store = FormulaStore(tmp_path / "cache" / "latex")
    report = resolve_formulas(cache, store, OcrOptions(delay=0, timeout_ms=10_000))

    assert (report.decoded, report.ocr, report.unresolved) == (1, 1, 0)
    out = tmp_path / "output"
    convert_all(cache, out, formulas=store.results())
    md = (out / "python" / "op.md").read_text(encoding="utf-8")
    assert r"$FAKE \alpha$ ![figure](../assets/" in md  # OCR 結果附原圖
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_pipeline.py -v`
Expected: FAIL（`ModuleNotFoundError: halcon_doc_skills.pipeline`）

- [ ] **Step 3: 實作 pipeline.py**

```python
"""爬取（crawl）與離線轉換（convert_all）流程。"""
from __future__ import annotations

import asyncio
import logging
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin

from playwright.async_api import Browser, BrowserContext, Page, async_playwright
from playwright.async_api import Error as PlaywrightError

from . import config
from .assets import image_asset_name
from .cache import PageCache
from .converter import convert_page, is_stub_page
from .crawler import Frontier, md_name, normalize_url, page_name
from .extractor import PageExtract, PageFetchError, extract_page
from .formulas import FormulaResult, FormulaStore, scan_and_decode
from .indexer import (
    IndexEntry,
    build_index,
    category_from_breadcrumb,
    read_title_and_summary,
)
from .ocr import OcrOptions, ocr_pending

log = logging.getLogger(__name__)


@dataclass
class CrawlReport:
    """爬取統計。"""

    fetched: int = 0
    skipped: int = 0
    failed: list[str] = field(default_factory=list)


@dataclass
class ConvertReport:
    """轉換統計（以語言為鍵）。"""

    converted: dict[str, int] = field(default_factory=dict)
    skipped_stubs: dict[str, int] = field(default_factory=dict)


@dataclass
class FormulaReport:
    """公式處理統計。"""

    total: int = 0
    decoded: int = 0
    ocr: int = 0
    unresolved: int = 0
    rejected: Counter[str] = field(default_factory=Counter)


@dataclass(frozen=True)
class _Options:
    force: bool
    delay: float
    retries: int


async def crawl(
    cache: PageCache,
    output_dir: Path,
    *,
    concurrency: int = config.DEFAULT_CONCURRENCY,
    limit: int | None = None,
    force: bool = False,
    delay: float = config.DEFAULT_DELAY,
    retries: int = config.DEFAULT_RETRIES,
    entries: Sequence[str] | None = None,
    headless: bool = True,
) -> CrawlReport:
    """以廣度優先爬取文件頁並寫入快取與圖片資產。

    :param cache: 頁面快取。
    :param output_dir: 輸出根目錄（圖片放在其下的 ``assets/``）。
    :param concurrency: 同時開啟的分頁（worker）數。
    :param limit: 最多處理的不同網址數（試跑用）。
    :param force: True 時忽略已完成的快取，重新擷取。
    :param delay: 每次成功擷取後的等待秒數。
    :param retries: 每頁最多嘗試次數。
    :param entries: 入口頁（相對於 ``config.BASE_URL``），預設用設定值。
    :param headless: 是否以無頭模式啟動瀏覽器。
    :return: 爬取統計。
    """
    frontier = Frontier(limit)
    queue: asyncio.Queue[str] = asyncio.Queue()
    report = CrawlReport()
    options = _Options(force=force, delay=delay, retries=retries)
    for entry in entries if entries is not None else config.ENTRY_PAGES:
        url = urljoin(config.BASE_URL, entry)
        if frontier.add(url):
            queue.put_nowait(url)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=headless)
        try:
            workers = [
                asyncio.create_task(
                    _worker(
                        browser,
                        queue,
                        frontier,
                        cache,
                        Path(output_dir) / "assets",
                        report,
                        options,
                    )
                )
                for _ in range(concurrency)
            ]
            join = asyncio.create_task(queue.join())
            finished, _ = await asyncio.wait(
                {join, *workers}, return_when=asyncio.FIRST_COMPLETED
            )
            for task in finished:
                if task is not join:
                    task.result()  # worker 意外結束時重新拋出例外，避免卡住
            for task in (join, *workers):
                task.cancel()
            await asyncio.gather(join, *workers, return_exceptions=True)
        finally:
            await browser.close()
    log.info(
        "爬取完成：新增 %d、略過 %d、失敗 %d",
        report.fetched,
        report.skipped,
        len(report.failed),
    )
    return report


async def _worker(
    browser: Browser,
    queue: asyncio.Queue[str],
    frontier: Frontier,
    cache: PageCache,
    assets_dir: Path,
    report: CrawlReport,
    options: _Options,
) -> None:
    """從佇列取網址處理；每個 worker 使用獨立的 browser context。"""
    context = await browser.new_context()
    page = await context.new_page()
    try:
        while True:
            url = await queue.get()
            try:
                links = await _handle_url(
                    page, url, cache, assets_dir, report, options
                )
            except (PageFetchError, PlaywrightError) as exc:
                log.error("失敗：%s（%s）", url, exc)
                cache.record_failure(url, str(exc).splitlines()[0])
                report.failed.append(url)
            else:
                for link in links:
                    normalized = normalize_url(link, url)
                    if normalized and frontier.add(normalized):
                        queue.put_nowait(normalized)
            finally:
                queue.task_done()
    finally:
        await context.close()


async def _handle_url(
    page: Page,
    url: str,
    cache: PageCache,
    assets_dir: Path,
    report: CrawlReport,
    options: _Options,
) -> list[str]:
    """處理單一網址，回傳該頁連結供後續入列。"""
    name = page_name(url)
    if not options.force and cache.is_complete(name):
        report.skipped += 1
        return cache.load_meta(name)["links"]
    extract = await _fetch_with_retry(page, url, options.retries)
    cache.save(name, extract)
    await _download_images(page.context, extract.image_urls, assets_dir)
    report.fetched += 1
    done = report.fetched + report.skipped + len(report.failed)
    log.info("[%d] %s", done, name)
    await asyncio.sleep(options.delay)
    return extract.links


async def _fetch_with_retry(page: Page, url: str, retries: int) -> PageExtract:
    """擷取頁面；可重試的錯誤以指數退避重試，不可重試（如 404）立即放棄。"""
    attempt = 0
    while True:
        attempt += 1
        try:
            return await extract_page(page, url)
        except PageFetchError as exc:
            if not exc.retryable or attempt >= retries:
                raise
            log.warning("重試 %d/%d：%s（%s）", attempt, retries, url, exc)
        except PlaywrightError as exc:
            if attempt >= retries:
                raise
            log.warning("重試 %d/%d：%s（%s）", attempt, retries, url, exc)
        await asyncio.sleep(2 ** (attempt - 1))


async def _download_images(
    context: BrowserContext, urls: Sequence[str], assets_dir: Path
) -> None:
    """下載內容中的 ``<img>`` 到共用資產資料夾；失敗只記警告。"""
    for url in urls:
        path = assets_dir / image_asset_name(url)
        if path.exists():
            continue
        try:
            response = await context.request.get(url)
        except PlaywrightError as exc:
            log.warning("圖片下載失敗：%s（%s）", url, exc)
            continue
        if not response.ok:
            log.warning("圖片下載失敗：%s（HTTP %d）", url, response.status)
            continue
        assets_dir.mkdir(parents=True, exist_ok=True)
        path.write_bytes(await response.body())


def resolve_formulas(
    cache: PageCache,
    store: FormulaStore,
    ocr_options: OcrOptions | None = None,
) -> FormulaReport:
    """字形解碼快取內所有公式；給了 ``ocr_options`` 時對被拒者做 OCR 備援。

    :param cache: 頁面快取。
    :param store: 公式結果快取（``cache/latex``）。
    :param ocr_options: None 表示不啟用 OCR（預設）。
    :return: 公式統計（只計目前快取內出現的公式）。
    """
    decode_report = scan_and_decode(cache, store)
    if ocr_options is not None:
        ocr_report = asyncio.run(ocr_pending(store, ocr_options))
        log.info("OCR 完成：成功 %d、失敗 %d", ocr_report.done, ocr_report.failed)
    results = {
        key: result
        for key, result in store.results().items()
        if key in decode_report.keys
    }
    report = FormulaReport(total=decode_report.total, rejected=decode_report.rejected)
    report.decoded = sum(r.source == "decode" for r in results.values())
    report.ocr = sum(r.source == "ocr" for r in results.values())
    report.unresolved = report.total - len(results)
    log.info(
        "公式：共 %d 個，字形解碼 %d、OCR %d、保留圖檔 %d；被拒原因：%s",
        report.total,
        report.decoded,
        report.ocr,
        report.unresolved,
        dict(report.rejected),
    )
    return report


def convert_all(
    cache: PageCache,
    output_dir: Path,
    langs: Sequence[str] = config.LANGS,
    formulas: Mapping[str, FormulaResult] | None = None,
) -> ConvertReport:
    """離線將快取轉成 Markdown，略過空殼頁並產生各語言 INDEX.md。

    :param cache: 頁面快取。
    :param output_dir: 輸出根目錄。
    :param langs: 要轉換的語言。
    :param formulas: 公式鍵 → LaTeX 結果（通常是 ``store.results()``）。
    :return: 各語言的轉換與略過數量。
    """
    output_dir = Path(output_dir)
    assets_dir = output_dir / "assets"
    pages = cache.pages()
    report = ConvertReport()
    for lang in langs:
        real = {p for p in pages if not is_stub_page(cache.load_html(lang, p))}
        index_entries: list[IndexEntry] = []
        for number, page in enumerate(sorted(real), start=1):
            meta = cache.load_meta(page)
            markdown = convert_page(
                cache.load_html(lang, page),
                meta["url"],
                lang,
                real,
                assets_dir,
                formulas,
            )
            target = output_dir / lang / md_name(page)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
            title, summary = read_title_and_summary(markdown, page)
            category = category_from_breadcrumb(meta["breadcrumb"])
            index_entries.append(IndexEntry(page, title, summary, category))
            if number % 200 == 0:
                log.info("[%s] 已轉換 %d / %d", lang, number, len(real))
        index_path = output_dir / lang / "INDEX.md"
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(build_index(lang, index_entries), encoding="utf-8")
        report.converted[lang] = len(real)
        report.skipped_stubs[lang] = len(pages) - len(real)
        log.info(
            "[%s] 轉換 %d 頁，略過空殼頁 %d",
            lang,
            len(real),
            len(pages) - len(real),
        )
    return report
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_pipeline.py -v && uv run ruff check`
Expected: 6 passed；ruff 無錯誤。失敗時的診斷順序：先看 `cache.failed_path` 內容確認是哪個網址失敗，再看 `cache.load_html("python", "op_one.html")` 是否為預期的可見內容，最後才懷疑轉換器。

- [ ] **Step 5: Commit**

```bash
git add src/halcon_doc_skills/pipeline.py tests/test_pipeline.py
git commit -m "feat: 新增爬取與離線轉換流程
--- feat ---
1. 新增 crawl 以多 worker 廣度優先爬取並支援重試與斷點續爬
2. 新增圖片下載到共用資產資料夾
3. 新增 convert_all 略過空殼類別頁並產生各語言索引
4. 新增 resolve_formulas 串接字形解碼與可選的 OCR 備援
5. 新增以本機迷你網站進行的端對端測試"
```

---

### Task 11: 驗收檢查與命令列介面（verify.py、cli.py）

**Files:**
- Create: `src/halcon_doc_skills/verify.py`
- Create: `src/halcon_doc_skills/cli.py`
- Modify: `src/halcon_doc_skills/__init__.py`
- Modify: `README.md`
- Test: `tests/test_verify.py`、`tests/test_cli.py`

**Interfaces:**
- Consumes: `crawl` / `convert_all` / `resolve_formulas`（Task 10）、`FormulaStore`（Task 5）、`OcrOptions`（Task 9）、`PageCache`（Task 3）、`config`。
- Produces:
  `@dataclass class VerifyReport`：`problems: list[str]`、`counts: dict[str, int]`（各語言 `.md` 數，不含 `INDEX.md`）、`ok` 屬性。
  `verify_output(output_dir: Path, langs: Sequence[str] = config.LANGS) -> VerifyReport`：檢查每個語言資料夾存在且有 `INDEX.md`；所有 `.md` 內的相對連結與圖片路徑都指向存在的檔案；沒有「同一英文單字連續重複」（如 `abs_imageabs_image`）；公式定界符 `$` / `$$` 成對（略過程式碼區塊、行內程式碼與 `\$`）；沒有殘留的 `@@FORMULA:` 標記。
  `cli.build_parser() -> argparse.ArgumentParser`、`cli.main(argv: Sequence[str] | None = None) -> int`；`halcon_doc_skills.main` 匯出自 `cli.main`。
  子命令：`crawl`（`--cache-dir`、`--output`、`--concurrency`、`--limit`、`--entry` 可重複、`--force`、`--delay`；爬完接著解碼公式並轉換）、`convert`（`--cache-dir`、`--output`；解碼公式並轉換）、`verify`（`--output`；有問題回傳 1）。`crawl` 與 `convert` 另有 OCR 選項：`--ocr-fallback`（預設關閉）、`--ocr-delay SEC`（預設 5.0）、`--ocr-max N`（預設 500）。公式快取放在 `<cache-dir>/latex`。

- [ ] **Step 1: 寫失敗測試（verify）**

`tests/test_verify.py`：

```python
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
```

- [ ] **Step 2: 執行確認失敗**

Run: `uv run pytest tests/test_verify.py -v`
Expected: FAIL（`ModuleNotFoundError`）

- [ ] **Step 3: 實作 verify.py**

```python
"""輸出品質檢查：連結與圖片路徑、重複文字、各語言檔案數。"""
from __future__ import annotations

import os
import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

from . import config

_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)[^)]*\)")
_LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")
_REPEAT_RE = re.compile(r"\b([A-Za-z_]{4,})\1\b")
_ESCAPED_DOLLAR_RE = re.compile(r"\\\$")
_EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "#")


@dataclass
class VerifyReport:
    """檢查結果。"""

    problems: list[str] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """沒有任何問題時為 True。"""
        return not self.problems


def verify_output(
    output_dir: Path, langs: Sequence[str] = config.LANGS
) -> VerifyReport:
    """檢查輸出資料夾。

    :param output_dir: 輸出根目錄。
    :param langs: 要檢查的語言資料夾。
    :return: 問題清單與各語言 .md 檔案數。
    """
    output_dir = Path(output_dir)
    report = VerifyReport()
    for lang in langs:
        lang_dir = output_dir / lang
        if not lang_dir.is_dir():
            report.problems.append(f"缺少語言資料夾：{lang}")
            continue
        if not (lang_dir / "INDEX.md").exists():
            report.problems.append(f"缺少 INDEX.md：{lang}")
        files = sorted(p for p in lang_dir.rglob("*.md") if p.name != "INDEX.md")
        report.counts[lang] = len(files)
        for md_file in sorted(lang_dir.rglob("*.md")):
            _check_file(md_file, output_dir, report)
    return report


def _check_file(md_file: Path, root: Path, report: VerifyReport) -> None:
    rel = md_file.relative_to(root).as_posix()
    text = md_file.read_text(encoding="utf-8")
    text = _FENCE_RE.sub("", text)
    scan = _INLINE_CODE_RE.sub("", text)
    for target in _LINK_RE.findall(scan):
        if target.startswith(_EXTERNAL_PREFIXES):
            continue
        path = Path(os.path.normpath(md_file.parent / unquote(target.split("#")[0])))
        if not path.exists():
            report.problems.append(f"{rel}：連結目標不存在 {target}")
    plain = _ESCAPED_DOLLAR_RE.sub("", scan)
    if plain.count("$$") % 2 or plain.replace("$$", "").count("$") % 2:
        report.problems.append(f"{rel}：公式定界符 $ 不成對")
    if "@@FORMULA:" in text:
        report.problems.append(f"{rel}：殘留公式標記 @@FORMULA:")
    repeated = _REPEAT_RE.search(_LINK_TARGET_RE.sub("]", text))
    if repeated:
        report.problems.append(f"{rel}：疑似語言重複文字 {repeated.group(0)}")
```

- [ ] **Step 4: 執行確認通過**

Run: `uv run pytest tests/test_verify.py -v && uv run ruff check`
Expected: 7 passed；ruff 無錯誤。

- [ ] **Step 5: 寫失敗測試（cli）**

`tests/test_cli.py`：

```python
"""命令列介面的測試。"""
from pathlib import Path

import pytest

from halcon_doc_skills import cli, config
from halcon_doc_skills.cache import PageCache
from halcon_doc_skills.cli import build_parser, main
from halcon_doc_skills.extractor import PageExtract
from halcon_doc_skills.formulas import collect_formula_svgs
from halcon_doc_skills.ocr import OcrOptions
from halcon_doc_skills.pipeline import FormulaReport

FIXTURES = Path(__file__).parent / "fixtures"


def test_parser_defaults_and_overrides() -> None:
    args = build_parser().parse_args(["crawl"])
    assert args.cache_dir == Path("cache") and args.output == Path("output")
    assert args.concurrency == config.DEFAULT_CONCURRENCY
    assert args.limit is None and args.entries is None and args.force is False
    assert args.ocr_fallback is False and args.ocr_delay == 5.0 and args.ocr_max == 500

    args = build_parser().parse_args(
        ["crawl", "--limit", "5", "--entry", "a.html", "--entry", "b.html", "--force"]
    )
    assert args.limit == 5 and args.entries == ["a.html", "b.html"]
    assert args.force is True


def test_convert_then_verify(tmp_path: Path) -> None:
    cache = PageCache(tmp_path / "cache")
    html = "<h1>op (Operator)</h1><h2>Name</h2><p><code>op</code> — Does it.</p>"
    cache.save(
        "op.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/op.html",
            title="op",
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang={"hdevelop": html, "dotnet": html, "python": html},
        ),
    )
    out = tmp_path / "output"
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(out)]
    assert main(["convert", *argv]) == 0
    assert (out / "python" / "op.md").exists()
    assert main(["verify", "--output", str(out)]) == 0

    (out / "python" / "op.md").write_text("[gone](gone.md)\n", encoding="utf-8")
    assert main(["verify", "--output", str(out)]) == 1


def test_convert_writes_latex_for_decodable_formulas(tmp_path: Path) -> None:
    page = (FIXTURES / "threshold.html").read_text(encoding="utf-8")
    svg = collect_formula_svgs(page)[0][0]
    html = (
        "<h1>op (Operator)</h1>"
        f'<p><span title="1" class="displaymath"><!-- c -->{svg}</span></p>'
    )
    cache = PageCache(tmp_path / "cache")
    cache.save(
        "op.html",
        PageExtract(
            url="https://www.mvtec.com/doc/halcon/2605/en/op.html",
            title="op",
            breadcrumb=[("HALCON", "u"), ("Ref", "u"), ("Cat", "u")],
            links=[],
            image_urls=[],
            html_by_lang={"hdevelop": html, "dotnet": html, "python": html},
        ),
    )
    out = tmp_path / "output"
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(out)]
    assert main(["convert", *argv]) == 0
    md = (out / "python" / "op.md").read_text(encoding="utf-8")
    assert r"$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$" in md
    assert (tmp_path / "cache" / "latex").is_dir()
    assert main(["verify", "--output", str(out)]) == 0


def test_ocr_options_are_wired(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    captured: list[OcrOptions | None] = []

    def fake_resolve(cache, store, ocr_options=None) -> FormulaReport:
        captured.append(ocr_options)
        return FormulaReport()

    monkeypatch.setattr(cli, "resolve_formulas", fake_resolve)
    argv = ["--cache-dir", str(tmp_path / "cache"), "--output", str(tmp_path / "out")]
    assert main(["convert", *argv]) == 0
    ocr_argv = ["--ocr-fallback", "--ocr-delay", "7", "--ocr-max", "3"]
    assert main(["convert", *argv, *ocr_argv]) == 0
    assert captured == [None, OcrOptions(delay=7.0, max_count=3)]
```

- [ ] **Step 6: 執行確認失敗**

Run: `uv run pytest tests/test_cli.py -v`
Expected: FAIL（`ModuleNotFoundError: halcon_doc_skills.cli`）

- [ ] **Step 7: 實作 cli.py 與 __init__.py**

`src/halcon_doc_skills/cli.py`：

```python
"""命令列介面：crawl / convert / verify。"""
from __future__ import annotations

import argparse
import asyncio
import logging
from collections.abc import Sequence
from pathlib import Path

from . import config
from .cache import PageCache
from .formulas import FormulaStore
from .ocr import OcrOptions
from .pipeline import convert_all, crawl, resolve_formulas
from .verify import verify_output

log = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """建立命令列解析器。"""
    parser = argparse.ArgumentParser(
        prog="halcon-doc-skills",
        description="爬取 HALCON 文件並轉成各語言的 Markdown。",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    crawl_p = sub.add_parser("crawl", help="爬取並轉換")
    _add_paths(crawl_p, cache=True)
    crawl_p.add_argument("--concurrency", type=int, default=config.DEFAULT_CONCURRENCY)
    crawl_p.add_argument("--limit", type=int, default=None, help="最多處理頁數（試跑）")
    crawl_p.add_argument(
        "--entry",
        action="append",
        dest="entries",
        default=None,
        help="覆寫入口頁（相對於文件根目錄，可重複）",
    )
    crawl_p.add_argument("--force", action="store_true", help="忽略快取重新擷取")
    crawl_p.add_argument("--delay", type=float, default=config.DEFAULT_DELAY)
    _add_ocr_options(crawl_p)

    convert_p = sub.add_parser("convert", help="僅以快取重新轉換")
    _add_paths(convert_p, cache=True)
    _add_ocr_options(convert_p)

    verify_p = sub.add_parser("verify", help="檢查輸出品質")
    _add_paths(verify_p, cache=False)
    return parser


def _add_paths(parser: argparse.ArgumentParser, cache: bool) -> None:
    if cache:
        parser.add_argument("--cache-dir", type=Path, default=Path("cache"))
    parser.add_argument("--output", type=Path, default=Path("output"))


def _add_ocr_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--ocr-fallback",
        action="store_true",
        help="字形解碼被拒的公式改用 latexconvert.com 做 OCR（會上傳圖片到第三方）",
    )
    parser.add_argument("--ocr-delay", type=float, default=5.0, help="OCR 請求間隔秒數")
    parser.add_argument("--ocr-max", type=int, default=500, help="單次最多 OCR 筆數")


def _convert(cache: PageCache, args: argparse.Namespace) -> None:
    """解碼公式（可選 OCR 備援）後轉換全部頁面。"""
    store = FormulaStore(cache.root / "latex")
    ocr_options = (
        OcrOptions(delay=args.ocr_delay, max_count=args.ocr_max)
        if args.ocr_fallback
        else None
    )
    resolve_formulas(cache, store, ocr_options)
    convert_all(cache, args.output, formulas=store.results())


def main(argv: Sequence[str] | None = None) -> int:
    """程式進入點。

    :return: 結束碼；``verify`` 發現問題時為 1，其餘為 0。
    """
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    if args.command == "verify":
        report = verify_output(args.output)
        for problem in report.problems:
            log.error(problem)
        log.info("各語言 .md 檔案數：%s", report.counts)
        return 0 if report.ok else 1

    cache = PageCache(args.cache_dir)
    if args.command == "crawl":
        asyncio.run(
            crawl(
                cache,
                args.output,
                concurrency=args.concurrency,
                limit=args.limit,
                force=args.force,
                delay=args.delay,
                entries=args.entries,
            )
        )
    _convert(cache, args)
    return 0
```

`src/halcon_doc_skills/__init__.py` 改為：

```python
"""HALCON 文件爬取與 Markdown 轉換工具。"""
from .cli import main

__all__ = ["main"]
```

- [ ] **Step 8: 執行全部測試與 lint**

Run: `uv run pytest -v && uv run ruff check && uv run ruff format --check`
Expected: 全部通過。若 `ruff format --check` 報告需要格式化，執行 `uv run ruff format` 後再確認測試仍通過。

- [ ] **Step 9: 撰寫 README**

`README.md`：

```markdown
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
```

- [ ] **Step 10: Commit**

```bash
git add src/halcon_doc_skills/verify.py src/halcon_doc_skills/cli.py src/halcon_doc_skills/__init__.py tests/test_verify.py tests/test_cli.py README.md
git commit -m "feat: 新增驗收檢查與命令列介面
--- feat ---
1. 新增 verify 檢查連結、圖片路徑、重複文字與公式定界符
2. 新增 crawl、convert、verify 子命令
3. 新增 --limit 與 --entry 供試跑與抽樣
4. 新增 --ocr-fallback 等選項串接公式解碼與 OCR 備援
5. 新增 README 使用說明"
```

---

### Task 12: 真實網站試跑與全量爬取

**Files:**
- 無程式碼變更（若試跑發現問題，回到對應任務修正並補測試）。

**Interfaces:**
- Consumes: 完整 CLI（Task 11）。

- [ ] **Step 1: 抽樣試跑真實頁面（不啟用 OCR）**

Run:
```bash
cd /home/administrator/code/halcon-doc-skills
uv run halcon-doc-skills crawl \
  --entry abs_image.html --entry threshold.html --entry HBarCode.html \
  --entry toc_filters_arithmetic.html --entry dyn_threshold.html \
  --entry hom_mat2d_rotate.html --limit 6
uv run halcon-doc-skills verify
find output -type f | sort
```
Expected：
- 沒有 `ERROR` 日誌；`cache/failed.txt` 不存在或為空。
- `output/dotnet/HBarCode.md` 存在，`output/hdevelop/HBarCode.md` 與 `output/python/HBarCode.md` **不存在**。
- 日誌出現「公式：共 N 個，字形解碼 …、OCR 0、保留圖檔 …」，被拒原因中含 `cmex`（`hom_mat2d_rotate` 的矩陣）。
- `output/python/threshold.md` 含 `$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$`；`output/python/dyn_threshold.md` 的公式以 `$$…$$` 呈現；`output/python/hom_mat2d_rotate.md` 的矩陣公式為 `![figure](../assets/….svg)`。
- `verify` 結束碼為 0。

- [ ] **Step 2: 人工檢視輸出品質**

用 Read 檢視 `output/python/abs_image.md`、`output/dotnet/abs_image.md`、`output/hdevelop/abs_image.md`、`output/python/threshold.md`、`output/python/dyn_threshold.md`、`output/python/INDEX.md`。逐項確認：
1. 標題、簽名（Signature）、參數（Parameters）、範例（Example）、Result、See also 都在，且該語言的名稱正確（Python 為 `abs_image`、.NET 為 `AbsImage`、參數 `image`／`imageAbs`）。
2. 沒有導覽列、分頁標籤、版權、社群圖示、其他語言的重複文字。
3. 公式：行內為 `$…$`、獨立為 `$$…$$`，LaTeX 內的 `_`、`\`、`*` 沒有被跳脫；與原頁面的公式一致（可對照 `https://www.mvtec.com/doc/halcon/2605/en/dyn_threshold.html`）。
4. 「See also」的連結在該語言資料夾內可對應到 `.md`（若目標尚未爬到，則為原站完整網址）。

若發現格式問題（例如參數區塊排版混亂），回到 Task 7，先新增能重現該問題的最小測試（貼上有問題的 HTML 片段），再修正 `converter.py`，並重跑 `uv run halcon-doc-skills convert`（不需重爬）。公式解碼有誤則回到 Task 5，先新增重現該公式的測試再修正，並重跑 `convert`（被拒的舊公式會自動重試解碼）。

- [ ] **Step 3: 全量爬取**

Run（預期約 2,700 頁，耗時約 15～30 分鐘，可放在背景執行）：
```bash
uv run halcon-doc-skills crawl 2>&1 | tee crawl.log
```
Expected：日誌出現「爬取完成：新增 N、略過 0、失敗 F」，`N` 約 2,700（`F` 應為 0 或極少數）；接著出現「公式：共 … 個，字形解碼 …」（預期公式總數約 1,100、字形解碼約 66%）。若中途中斷，直接重跑同一指令即可續爬。

- [ ] **Step 4: 全量驗收**

Run:
```bash
uv run halcon-doc-skills verify
wc -l cache/failed.txt 2>/dev/null
for l in hdevelop dotnet python; do echo $l $(find output/$l -name '*.md' ! -name INDEX.md | wc -l); done
ls output/assets | wc -l
ls output/assets | sed 's/.*\.//' | sort | uniq -c
ls cache/latex | wc -l
```
Expected：
- `verify` 結束碼 0（否則逐條處理其輸出的問題）。
- 三個語言的 `.md` 數相差約為類別頁數（約 100；.NET 較多）。
- `output/assets` 只剩「未轉成 LaTeX 的公式」的 `.svg`（約為被拒的公式數）；副檔名統計若出現 `.png` 等，代表站上有 `<img>` 點陣圖（spec §11 的風險），請回報。
- `cache/latex` 的檔案數約為公式總數。
- `cache/failed.txt` 的每一列都能說明原因；把清單回報給使用者。

- [ ] **Step 5: 公式抽驗**

產生一份「原圖 vs. 渲染後 LaTeX」的並排頁面，隨機抽 30 個字形解碼的公式人工比對（需要網路載入 KaTeX）：

```bash
uv run python - <<'PY'
import json
import random
from pathlib import Path

items = []
for path in Path("cache/latex").glob("*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("source") == "decode":
        items.append(data)
random.seed(1)
rows = []
for data in random.sample(items, min(30, len(items))):
    rows.append(
        f"<tr><td>{data['svg']}</td><td>\\({data['latex']}\\)</td>"
        f"<td><code>{data['latex']}</code></td></tr>"
    )
html = (
    '<meta charset="utf-8">'
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.css">'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>'
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/contrib/auto-render.min.js"'
    ' onload="renderMathInElement(document.body)"></script>'
    "<table border=1 cellpadding=8><tr><th>原圖</th><th>LaTeX 渲染</th><th>LaTeX</th></tr>"
    + "".join(rows)
    + "</table>"
)
Path("cache/spotcheck.html").write_text(html, encoding="utf-8")
print("已產生 cache/spotcheck.html，共", len(rows), "列")
PY
```
用瀏覽器開啟 `cache/spotcheck.html`，逐列比對「原圖」與「LaTeX 渲染」是否一致（字元、上下標位置、`\texttt` 的等寬字）。任何不一致都要回到 Task 5 新增測試並修正字型／字碼對照表。

- [ ] **Step 6: （需使用者同意）OCR 備援**

字形解碼被拒的公式（預估約 370 個）可用 latexconvert.com 補上 LaTeX。**執行前先向使用者確認**：這會把這些公式圖片（來自公開的 HALCON 文件）上傳到第三方網站，且需要約 30 分鐘。

先小量試跑並人工核對：
```bash
uv run halcon-doc-skills convert --ocr-fallback --ocr-max 5
uv run halcon-doc-skills verify
```
Expected：日誌出現「OCR 完成：成功 5、失敗 0」；被 OCR 的公式在 Markdown 中為 `$…$`／`$$…$$` 後接 ` ![figure](../assets/….svg)`，開啟該 `.svg` 與 LaTeX 比對。若連續失敗，OCR 會自動停止（可能是被限流或網站改版）。

確認品質可接受、使用者同意後再全量執行（成功的結果已快取，中斷後重跑只會補剩下的）：
```bash
uv run halcon-doc-skills convert --ocr-fallback 2>&1 | tee ocr.log
uv run halcon-doc-skills verify
```

- [ ] **Step 7: 清理與收尾**

刪除 `crawl.log`、`ocr.log`（若不想保留），確認 `git status` 沒有 `cache/`、`output/`（已被 `.gitignore` 排除）。不需要額外 commit；把全量統計（頁數、失敗數、各語言檔案數、公式：總數／字形解碼／OCR／保留圖檔／被拒原因分布、SVG 與 `<img>` 數量）整理給使用者。
