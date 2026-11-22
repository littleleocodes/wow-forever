"""The fight lab's rest rule as the pages and reports state it (2026-11-21, the audit session: "Footers and the fight lab's method note
must state the rest rule and its source"). Read from fightlab/tables.py's text (REST_REGEN), so a renderer needs no fight-lab import."""
import pathlib
import re

_T = pathlib.Path(__file__).resolve().parent / "fightlab" / "tables.py"


def on():
    """True when the fight lab lets your own regeneration run while you eat and drink (tables.REST_REGEN)."""
    m = re.search(r"^REST_REGEN = (True|False)\b", _T.read_text(encoding="utf-8"), re.M)
    return bool(m and m.group(1) == "True")


def note():
    """One sentence on the rest rule and its source, for footers and method notes."""
    if on():
        return ("Between fights, your own health and mana regeneration keeps running while you eat and drink, as on Classic's servers; "
                "not yet checked against a Forever combat log.")
    return "Between fights, only the food and drink refill you: your own regeneration is left out while you eat and drink."
