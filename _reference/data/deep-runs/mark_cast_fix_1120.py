"""The converted official hunter rotations cast Hunter's Mark again (2026-11-20, the audit session's finding from the user's question on
Expose Prey). Our patch moves the mark's aura to rank 3 (14324: debuffs_auto_gen.go's huntersMarkSpell) while the hunter still casts
rank 4 (14325: hunters_mark.go registers spellData.HuntersMark.Highest()). siml_upstream_race.py's PATCH_RANKS swapped 14325 -> 14324
everywhere in the text, the casts too: no spell 14324 is registered for the hunter, so the cast lines (the pre-pull mark and the
"if the mark is not up" line) were dropped and the boss never carried the hunter's mark (ranged attack power lost, Expose Prey never
opening Mongoose Bite). Here every castSpell of 14324 goes back to {14325, rank 4}; the aura checks keep 14324, the aura the cast applies.

    python _reference/data/deep-runs/mark_cast_fix_1120.py [--write]
"""
import argparse
import json
import pathlib

DATA = pathlib.Path(__file__).resolve().parents[1]
FILES = ["raidsim/apls/hunter/upstream/default.apl.json", "raidsim/apls/hunter/upstream/melee.apl.json",
         "raidsim/apls/hunter/upstream/turret.apl.json", "raidsim/apls/hunter/upstream/turret_hawk.apl.json",
         "raidsim/apls/hunter/mm-raid-raid.apl.json"]


def fix(x, counts):
    if isinstance(x, dict):
        for k, v in x.items():
            if k == "castSpell" and isinstance(v, dict) and isinstance(v.get("spellId"), dict) and v["spellId"].get("spellId") == 14324:
                v["spellId"] = {"spellId": 14325, "rank": 4}
                counts["cast"] += 1
            elif k.endswith("auraId") and isinstance(v, dict) and v.get("spellId") == 14324:
                counts["aura"] += 1
            fix(v, counts)
    elif isinstance(x, list):
        for v in x:
            fix(v, counts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for rel in FILES:
        p = DATA / rel
        text = p.read_text(encoding="utf-8")
        d = json.loads(text)
        counts = {"cast": 0, "aura": 0}
        fix(d, counts)
        indent = 1 if text.startswith("{\n ") and not text.startswith("{\n  ") else 2
        print(f"{rel}: {counts['cast']} cast(s) restored to 14325 rank 4, {counts['aura']} aura check(s) on 14324 kept (indent {indent})")
        if a.write and counts["cast"]:   # each file keeps its own line endings (apl_opt writes CRLF here)
            p.write_text(json.dumps(d, indent=indent) + "\n", encoding="utf-8", newline="\r\n" if "\r\n" in text else "")


if __name__ == "__main__":
    main()
