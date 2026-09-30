"""skill 範本（SKILL.md 與陷阱清單）的結構測試。"""

import re

import pytest

from . import skill_scripts

import halcon_doc  # noqa: E402  # isort: skip

SKILL_MD = skill_scripts.TEMPLATE / "SKILL.md"


def _frontmatter() -> dict[str, str]:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "SKILL.md 必須以 YAML frontmatter 開頭"
    pairs = (line.split(":", 1) for line in match[1].splitlines())
    return {k.strip(): v.strip() for k, v in pairs}


def test_frontmatter_has_name_and_trigger_description() -> None:
    meta = _frontmatter()
    assert meta["name"] == "halcon"
    assert meta["description"].startswith("Use when")
    assert len(meta["description"]) <= 1024


def test_skill_md_is_short_enough_to_load() -> None:
    assert len(SKILL_MD.read_text(encoding="utf-8").splitlines()) <= 200


def test_skill_md_documents_every_subcommand() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    parser = halcon_doc.build_parser()
    sub = next(a for a in parser._actions if a.dest == "command")
    for command in sub.choices:
        assert f"$HDOC {command}" in text, command


@pytest.mark.parametrize("lang", ["dotnet", "python", "hdevelop"])
def test_pitfalls_have_30_to_60_numbered_items(lang: str) -> None:
    path = skill_scripts.TEMPLATE / "pitfalls" / f"{lang}.md"
    assert f"pitfalls/{lang}.md" in SKILL_MD.read_text(encoding="utf-8")
    items = re.findall(r"^\d+\. ", path.read_text(encoding="utf-8"), re.MULTILINE)
    assert 30 <= len(items) <= 60
