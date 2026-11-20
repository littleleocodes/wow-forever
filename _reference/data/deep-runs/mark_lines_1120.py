"""Every hunter rotation an entry points at carries Hunter's Mark (2026-11-20, the audit session after D11; the cause found the same
evening: the official simulator's hunter.go turns the raid's Hunter's Mark off for a hunter, "The hunter casts its own mark, so a raid's
permanent one would credit it before the cast", so a hunter rotation without its own mark lines fights with no mark at all; our ranged
rotations had none, our melee ones only the pre-pull cast, and the mark ends before a 180 s fight does). Each file gets the official
rotation's two lines where it lacks them: the pre-pull cast and "cast Hunter's Mark if the mark is not up" (first in the priority list).
The same pass takes out the lines that cast a rank the simulator does not register for the class (apl_validate's unknown_cast: the
lines never fire): Counterattack rank 4 in the hunter files, Fireball rank 10 in fire-raid's dummy rotation.

    python _reference/data/deep-runs/mark_lines_1120.py [--write]
"""
import argparse
import copy
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402

MARK = 14325
MARK_AURA = 14324
DEAD = {20910: "Counterattack rank 4", 10150: "Fireball rank 10"}
EXTRA = ["_reference/data/raidsim/apls/mage/fire-raid.apl.json"]   # the Fireball rank 10 line


def cast_of(item):
    act = (item or {}).get("action") or {}
    for k in ("castSpell", "channelSpell"):
        sid = ((act.get(k) or {}).get("spellId") or {}).get("spellId")
        if sid:
            return int(sid)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    up = json.load(open(DATA / "raidsim/apls/hunter/upstream/melee.apl.json", encoding="utf-8"))
    pre = next(x for x in up["prepullActions"] if cast_of(x) == MARK)
    line = next(x for x in up["priorityList"] if cast_of(x) == MARK)
    files = set()
    for e, v in R.SPECS["hunter"].items():
        if isinstance(v, dict):
            for k in ("apl", "apl_opt", "apl_opt_raid"):
                if v.get(k) and (ROOT / v[k]).exists():
                    files.add(v[k])
    for rel in sorted(files) + EXTRA:
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        d = json.loads(text)
        notes = []
        for key in ("prepullActions", "priorityList"):
            keep = []
            for x in d.get(key) or []:
                if cast_of(x) in DEAD:
                    notes.append(f"{key}: removed {DEAD[cast_of(x)]}")
                else:
                    keep.append(x)
            d[key] = keep
        if "/hunter/" in rel:
            if not any(cast_of(x) == MARK for x in d.get("prepullActions") or []):
                d["prepullActions"] = [copy.deepcopy(pre)] + list(d.get("prepullActions") or [])
                notes.append("added the pre-pull mark")
            if not any(cast_of(x) == MARK for x in d.get("priorityList") or []):
                d["priorityList"] = [copy.deepcopy(line)] + list(d.get("priorityList") or [])
                notes.append("added the recast line")
        print(f"{rel}: {'; '.join(notes) or 'nothing to do'}")
        if a.write and notes:
            indent = 1 if text.startswith("{\n ") or text.startswith("{\r\n ") else 2
            if text.startswith("{\n  ") or text.startswith("{\r\n  "):
                indent = 2
            p.write_text(json.dumps(d, indent=indent) + "\n", encoding="utf-8", newline="\r\n" if "\r\n" in text else "")


if __name__ == "__main__":
    main()
