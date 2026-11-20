"""Rotation lines that never fire, removed from our rotation files (2026-11-20, the play check's (a): a page built from them would print
them). Each removal is behaviour-neutral: the line never cast in any build of its entry.
- frost-raid (raid and dummy): the official Frost rotation's pre-pull Blink, timed at minus Blink's own aura; the simulator's Blink only
  moves the mage toward the boss, and our entry stands at 10 yards for Cone of Cold (a deliberate difference), so it never fires.
The converted official copies (apls/<class>/upstream/) keep every line: they must equal a fresh conversion (play_check.py's (e)).

    python _reference/data/deep-runs/dead_lines_1120.py [--write]
"""
import argparse
import json
import pathlib

DATA = pathlib.Path(__file__).resolve().parents[1]
DEAD = {"raidsim/apls/mage/frost-raid-raid.apl.json": [("prepullActions", 1953, "Blink")],
        "raidsim/apls/mage/frost-raid.apl.json": [("prepullActions", 1953, "Blink")]}


def cast_of(x):
    act = (x or {}).get("action") or {}
    return ((act.get("castSpell") or {}).get("spellId") or {}).get("spellId")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for rel, rules in DEAD.items():
        p = DATA / rel
        text = p.read_text(encoding="utf-8")
        d = json.loads(text)
        notes = []
        for part, sid, name in rules:
            keep = [x for x in d.get(part) or [] if cast_of(x) != sid]
            if len(keep) != len(d.get(part) or []):
                notes.append(f"{part}: removed {name}")
            d[part] = keep
        print(f"{rel}: {'; '.join(notes) or 'nothing to do'}")
        if a.write and notes:
            indent = 2 if text.startswith("{\n  ") or text.startswith("{\r\n  ") else 1
            p.write_text(json.dumps(d, indent=indent) + "\n", encoding="utf-8", newline="\r\n" if "\r\n" in text else "")


if __name__ == "__main__":
    main()
