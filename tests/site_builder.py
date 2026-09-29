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
        "plain.html": (
            "<!DOCTYPE html><html><body><p>not a doc page</p></body></html>"
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
