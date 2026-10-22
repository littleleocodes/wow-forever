"""The beta client build our talent and spell data come from, read from forever-talents/ (2026-10-09: the pages and reports had build
1.60.1.70009 written into their code and kept saying so after the refreshes to 70170 and 70291).

2026-10-22: the capture date is per class. A hotfix of 2026-10-20 changed only the mage's talents in build 70425 (Piercing Ice removed,
Elemental Precision 3 ranks); this module had read BUILD and CAPTURED from mage.json alone, so refreshing the mage would have dated every
class's data 2026-10-20 and made the pages drop the other eight classes' results of 10-16..10-19 as stale. CAPTURED is now the earliest
class capture (what "current" means for a record without a class); `captured(cls)` is one class's."""
import json
import pathlib

_DIR = pathlib.Path(__file__).resolve().parent / "forever-talents"
_CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
_ALL = {c: json.load(open(_DIR / f"{c}.json", encoding="utf-8")) for c in _CLASSES if (_DIR / f"{c}.json").exists()}
BUILD = (_ALL.get("mage") or next(iter(_ALL.values()), {})).get("build", "unknown")
CAPTURED = min((d.get("captured", "") for d in _ALL.values()), default="")


def captured(cls):
    """The date one class's talent data was captured (a class-only hotfix moves it: mage 2026-10-20)."""
    return (_ALL.get(cls) or {}).get("captured", CAPTURED)
