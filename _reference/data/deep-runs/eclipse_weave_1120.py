"""The independent audit's H5 (2026-11-20): a Wrath weave for Eclipse in every Balance rotation of ours. Forever's Eclipse ("Your Wrath
spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges. Lasts 15 sec.") needs Wrath, which no
Balance rotation cast, so every search read the talent at 0 (bit-identical when added). The line, before the Starfire filler: Wrath
(rank 8, 9912) while fewer than 2 Eclipse charges are stored, guarded by the Eclipse aura (408255) being known, so a build without the
talent is untouched (the simulator's absent rule reads a missing aura's stacks as 0, which would cast Wrath forever).

Size check (scratch ab_h5.py, full raid, 6,000 fights, seeds 1 and 2): the page pick, no Eclipse, bit-identical with the line (688.5);
the pick with Eclipse 3/3 and Improved Wrath 5/5 added unpaid: no weave 688.5, weave below 1 charge +6.7/+6.9%, below 2 +7.2/+7.5%,
below 3 +6.0/+6.1%. The search that pays the 8 points is the optimality pass's.

    python _reference/data/deep-runs/eclipse_weave_1120.py [--write]
"""
import argparse
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
ECL, WRATH, STARFIRES = 408255, 9912, (9876, 9875, 8951, 25298)
NOTE = ("added 2026-11-20 (the independent audit's H5): Wrath while fewer than 2 Eclipse charges are stored, guarded by the Eclipse aura "
        "being known, so builds without the talent are unchanged")
LINE = {"action": {"condition": {"and": {"vals": [
    {"auraIsKnown": {"auraId": {"spellId": ECL}}},
    {"cmp": {"op": "OpLt", "lhs": {"auraNumStacks": {"auraId": {"spellId": ECL}}}, "rhs": {"const": {"val": "2"}}}}]}},
    "castSpell": {"spellId": {"spellId": WRATH}}}, "notes": NOTE}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    import run as R
    R.set_game("forever")
    files = set()
    for name, e in R.SPECS["druid"].items():
        if not isinstance(e, dict) or e.get("tank"):
            continue
        for key in ("apl", "apl_opt", "apl_opt_raid"):
            if str(e.get(key, "")).startswith("_reference/"):
                files.add(ROOT / e[key])
    for p in sorted(files):
        apl = json.loads(p.read_text(encoding="utf-8"))
        pl = apl.get("priorityList", [])
        if f'"spellId": {ECL}' in json.dumps(apl):
            print(f"has the Eclipse line already: {p.relative_to(ROOT)}")
            continue
        i = next((k for k, it in enumerate(pl) if (it.get("action", {}).get("castSpell") or {}).get("spellId", {}).get("spellId") in STARFIRES
                  and not it.get("action", {}).get("condition")), None)
        if i is None:
            print(f"no plain Starfire line, left: {p.relative_to(ROOT)}")
            continue
        pl.insert(i, json.loads(json.dumps(LINE)))
        print(f"{'wrote' if a.write else 'would write'}: {p.relative_to(ROOT)} (line {i + 1} of {len(pl)})")
        if a.write:
            p.write_text(json.dumps(apl, indent=1) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
