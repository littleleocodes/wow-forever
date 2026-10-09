"""The beta client build our talent and spell data come from, read from forever-talents/ (2026-10-09: the pages and reports had build
1.60.1.70009 written into their code and kept saying so after the refreshes to 70170 and 70291)."""
import json
import pathlib

_D = json.load(open(pathlib.Path(__file__).resolve().parent / "forever-talents" / "mage.json", encoding="utf-8"))
BUILD = _D.get("build", "unknown")
CAPTURED = _D.get("captured", "")
