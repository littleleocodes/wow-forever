"""Undo the exact filler pass's Expose Prey 1 -> Hawk Eye 1 in beast-survival-open-raid (2026-11-20): Expose Prey measured exactly 0 only
because the converted official melee rotation never cast Hunter's Mark (deep-runs/mark_cast_fix_1120.py); with the mark it is worth
about 4% there (the audit session's runs). The Deflection 3 -> Survivalist 3 moves stay (parry does nothing for a raid damage dealer).
The record (raidsim/credited-fillers.json) keeps the moves and says which was undone and why."""
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA)]
import paths  # noqa: E402
import validate_builds as VB  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402

BID = "beast-survival-open-raid"
WHY = ("2026-11-20: the filler pass's Expose Prey 1 -> Hawk Eye 1 is undone: Expose Prey had measured exactly 0 only because the converted "
       "official melee rotation never cast Hunter's Mark (the cast was mapped to rank 3, which no hunter spell answers to; "
       "deep-runs/mark_cast_fix_1120.py), and with the mark up it opens Mongoose Bite (about +4% in the audit session's runs). The "
       "Deflection 3 -> Survivalist 3 moves stay.")


def main():
    bp = paths.builds_json("forever", "hunter")
    with locked(bp.with_suffix(".lock")):
        data = json.load(open(bp, encoding="utf-8"))
        b = next(x for x in data["builds"] if x["id"] == BID)
        flat = {n: r for items in b["allocation"].values() for n, r in items if r}
        if flat.get("Hawk Eye", 0) < 1 or flat.get("Expose Prey", 0) != 0:
            raise SystemExit(f"{BID}: not the state the pass left (Hawk Eye {flat.get('Hawk Eye')}, Expose Prey {flat.get('Expose Prey')})")
        for tree, items in b["allocation"].items():
            for it in items:
                if it[0] == "Hawk Eye":
                    it[1] -= 1
            b["allocation"][tree] = [it for it in items if it[1]]
        surv = b["allocation"]["Survival"]
        order = [t["name"] for tr in json.load(open(DATA / "forever-talents" / "hunter.json", encoding="utf-8"))["trees"]
                 if tr["name"] == "Survival" for t in tr["talents"]]
        surv.append(["Expose Prey", 1])
        surv.sort(key=lambda it: order.index(it[0]))
        errors = []
        VB.check_state(VB.load_forever()["hunter"], {t: {n: r for n, r in v} for t, v in b["allocation"].items()}, BID, errors)
        if errors:
            raise SystemExit(f"{BID}: {errors}")
        b.setdefault("notes", []).append(WHY)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
    rp = DATA / "raidsim" / "credited-fillers.json"
    rec = json.load(open(rp, encoding="utf-8"))
    rec[f"hunter/{BID}"]["undone"] = [{"from": "Expose Prey", "to": "Hawk Eye", "why": WHY}]
    rp.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"{BID}: Expose Prey 1 back, Hawk Eye 0; legal")


if __name__ == "__main__":
    main()
