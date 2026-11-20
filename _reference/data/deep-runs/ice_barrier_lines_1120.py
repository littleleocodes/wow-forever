"""Audit step 4 (2026-11-20, the independent audit's H1; user: "continue to make the changes ... that the audit suggests"): Ice Barrier
in every mage raid rotation where a build can hold it. The Frost rotations carry it since 6463e0d2 (a pre-pull cast at -2 s and a top
line that casts it again when Frigid Power, its +15% Frost damage for a minute, has under 2 s left). Every other mage rotation gets the
same two lines, guarded by "Ice Barrier is known" (spellIsKnown 13033), so a build without the 31-point Frost talent is untouched. A
hand fix had reached only the rotations it was typed into (the audit's blind spot 4), and the Frostfire and Arcane-Frost searches read
the talent at 0 without them.

    python _reference/data/deep-runs/ice_barrier_lines_1120.py [--write]
"""
import argparse
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
IB, FRIGID = 13033, 1326891
NOTE = ("added 2026-11-20 (the independent audit's H1): Ice Barrier again when Frigid Power, its +15% Frost damage for 1 min, has under "
        "2 s left; guarded by Ice Barrier being known, so builds without the 31-point Frost talent are unchanged")
PREPULL = {"action": {"condition": {"spellIsKnown": {"spellId": {"spellId": IB}}}, "castSpell": {"spellId": {"spellId": IB}}},
           "doAtValue": {"const": {"val": "-2s"}}}
TOP = {"action": {"condition": {"and": {"vals": [
    {"spellIsKnown": {"spellId": {"spellId": IB}}},
    {"cmp": {"op": "OpLt", "lhs": {"auraRemainingTime": {"auraId": {"spellId": FRIGID}}}, "rhs": {"const": {"val": "2s"}}}}]}},
    "castSpell": {"spellId": {"spellId": IB}}}, "notes": NOTE}


def has_ib(apl):
    return f'"spellId": {IB}' in json.dumps(apl)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    import run as R
    R.set_game("forever")
    files = set()
    for e in R.SPECS["mage"].values():
        if not isinstance(e, dict):
            continue
        for key in ("apl", "apl_opt", "apl_opt_raid"):
            if e.get(key, "").startswith("_reference/"):
                files.add(ROOT / e[key])
    for p in sorted(files):
        text = p.read_text(encoding="utf-8")
        apl = json.loads(text)
        if has_ib(apl):
            print(f"has Ice Barrier already: {p.relative_to(ROOT)}")
            continue
        apl.setdefault("prepullActions", []).insert(0, PREPULL)
        apl.setdefault("priorityList", []).insert(0, TOP)
        print(f"{'adds' if a.write else 'would add'} the two lines: {p.relative_to(ROOT)}")
        if a.write:
            p.write_text(json.dumps(apl, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
