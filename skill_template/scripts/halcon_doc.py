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
