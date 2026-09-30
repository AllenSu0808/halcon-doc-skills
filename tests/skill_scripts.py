"""讓測試能匯入 skill_template/scripts/ 下的獨立腳本。"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "skill_template"
SCRIPTS = TEMPLATE / "scripts"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
