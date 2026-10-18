"""Per-spell global cooldowns for the fight lab (audit of 2026-10-18, row 68).

    python _reference/data/fightlab/spell_gcd.py [--store <spells_auto_gen.go>] --write

The fight lab gave every spell a 1.5 s global cooldown; the client's are 1.0 s for rogue abilities, cat-form abilities, totems and Hammer
of Wrath. This reads `GCDMs` per spell id from the raid simulator's spell store (the client's SpellCooldowns data, exported by the
simulator; default: the local clone under ~/.wow-forever-tools) and writes, per class and spell name of our spellbook
(`forever-spells/<class>.json`), the spells whose every rank has one value other than 1.5 s: `gcd` (1.0 s ones, applied by
`tables.spell_gcd`) and `off_gcd` (0: listed for reference, not applied).
"""
import argparse
import collections
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SPELLS = HERE.parent / "forever-spells"
OUT = HERE / "spell_gcd.json"
STORE = pathlib.Path.home() / ".wow-forever-tools/forever-repo/sim/core/spelldata/spells_auto_gen.go"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=str(STORE))
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rows = {}
    for line in open(a.store, encoding="utf-8"):
        m = re.search(r'\{ID: (\d+), Name: "([^"]*)"', line)
        if m:
            g = re.search(r"GCDMs: (\d+)", line)
            rows[int(m.group(1))] = int(g.group(1)) if g else 0
    out = {"source": f"GCDMs of the raid simulator's spell store ({a.store.replace(str(pathlib.Path.home()), '~')}), by our spellbooks' rank ids; "
                     "written by spell_gcd.py (audit of 2026-10-18 row 68)", "gcd": {}, "off_gcd": {}}
    build = json.load(open(SPELLS / "mage.json", encoding="utf-8")).get("build")
    out["spellbook_build"] = build
    for cls in CLASSES:
        d = json.load(open(SPELLS / f"{cls}.json", encoding="utf-8"))
        by = collections.defaultdict(set)
        tabs = list(d.get("tabs") or [])
        gen = d.get("general")
        tabs += [gen] if isinstance(gen, dict) else (gen or [])
        for tab in tabs:
            for sp in tab.get("spells", []):
                for r in sp["ranks"]:
                    if r.get("id") in rows:
                        by[sp["name"]].add(rows[r["id"]])
        out["gcd"][cls] = {n: min(v) / 1000 for n, v in sorted(by.items()) if len(v) == 1 and 0 < min(v) != 1500}
        out["off_gcd"][cls] = sorted(n for n, v in by.items() if v == {0})
        print(cls, out["gcd"][cls])
    if a.write:
        OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
