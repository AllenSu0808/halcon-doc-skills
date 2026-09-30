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
