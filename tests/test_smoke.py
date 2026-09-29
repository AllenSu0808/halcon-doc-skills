"""確認測試環境與樣本檔可用。"""

from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def test_fixtures_exist() -> None:
    pages = sorted(FIXTURES.glob("*.html"))
    assert len(pages) >= 15
    for path in pages:
        assert "syn-hdevelop" in path.read_text(encoding="utf-8"), path.name
