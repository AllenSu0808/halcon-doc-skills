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
