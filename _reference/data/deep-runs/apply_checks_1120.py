"""The escalated short checks' confirmed moves, applied ahead of the full search (2026-11-20, the audit session's call: "a page should
not ship a pick we already know a confirmed better neighbour of"; the full search stays for the optimality pass). Each candidate is the
check's own result (raidsim/talent_opt.py --setting raid --rounds 2: every kept move confirmed on a second seed), legal by
validate_builds.

    python _reference/data/deep-runs/apply_checks_1120.py [--write]
"""
import argparse
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA)]
import paths  # noqa: E402
import validate_builds as VB  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402

CHECKS = [("hunter", "mm-lonewolf-raid", "mm-lone-wolf-raid"), ("hunter", "bm-raid", "beast-marks-ml-raid"),
          ("hunter", "melee-dps", "beast-survival-open-raid")]


def flat(al):
    return {n: r for items in (al or {}).values() for n, r in items if r}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    forever = VB.load_forever()
    for cls, entry, bid in CHECKS:
        cand = json.load(open(ROOT / cls / "research/raid/raidsim/candidates" / f"check-{entry}-{bid}.json", encoding="utf-8"))
        s = cand.get("search") or {}
        moves = s.get("moves") or []
        txt = "; ".join(f"{m['move'].replace('1 point ', '')} ({m['gain_seed1']:+.2%} / {m['gain_seed2']:+.2%})" for m in moves)
        errors = []
        VB.check_state(forever[cls], {t: {n: r for n, r in v} for t, v in cand["allocation"].items()}, bid, errors)
        if errors:
            raise SystemExit(f"{bid}: the check's build is illegal: {errors[0]}")
        print(f"{cls} {bid}: {txt}; {s.get('gain', 0):+.2%} in all")
        if not a.write:
            continue
        bp = paths.builds_json("forever", cls)
        with locked(bp.with_suffix(".lock")):
            data = json.load(open(bp, encoding="utf-8"))
            b = next(x for x in data["builds"] if x["id"] == bid)
            if flat(b["allocation"]) == flat(cand["allocation"]):
                print("   already applied")
                continue
            b["allocation"] = cand["allocation"]
            gone = set(flat({t: v for t, v in b["allocation"].items()})) ^ set()
            b["core"] = [c for c in b.get("core", []) if c.get("talent") in flat(cand["allocation"])]
            b.setdefault("notes", []).append(
                f"2026-11-20: the short check's confirmed move{'s' if len(moves) != 1 else ''} applied ahead of the full search "
                f"(raidsim/talent_opt.py --setting raid --rounds 2 from this build in {entry}, full raid, seeds 1 / 2): {txt}; "
                f"{s.get('gain', 0):+.2%} in all ({cand.get('note', '').split(': ')[-1]}). The audit session's call: a page should not ship a "
                "pick with a confirmed better neighbour; the full search stays for the optimality pass.")
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
        print("   applied")


if __name__ == "__main__":
    main()
