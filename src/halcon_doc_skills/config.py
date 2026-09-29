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
    "Use the tabs on the upper right to switch to a different programming language."
)
