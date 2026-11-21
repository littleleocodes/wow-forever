"""The Smite rotations' rank-2 line replaced (2026-11-20 night, the audit session's ruling: no rank taught below level 20 while the
simulator gives such ranks their full coefficient; a downrank to a rank taught at 20 or above stays allowed). The rank-2 line (591,
level 6: below 25% mana with 10 s or more left) against no line and against the same line with rank 4 (984, level 22) or rank 5 (1004,
level 30), every Smite build, full raid, 10,000 fights, seeds 1 and 2. With --apply the best allowed variant (on both seeds, both
builds' mean) replaces the line in the raid rotation and in the dummy rotation, and the record keeps what it costs against rank 2: the
size of the gap.

    python _reference/data/deep-runs/smite_downrank_1120.py [--fights 10000] [--apply]
Record raidsim/smite-downrank-1120.json.
"""
import argparse
import copy
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import paths  # noqa: E402
import flags_bench as FB  # noqa: E402

OUT = DATA / "raidsim" / "smite-downrank-1120.json"
LOW, VARIANTS = 591, {"rank 2 (now)": 591, "rank 4": 984, "rank 5": 1004, "no line": None}
FILES = [DATA / "raidsim/apls/priest/smite-dps-raid.apl.json", DATA / "raidsim/apls/priest/smite-dps.apl.json"]


def variant(rot, sid):
    r = copy.deepcopy(rot)
    out = []
    for x in r["priorityList"]:
        if any(s == LOW for _, _, s, _ in FB.casts({"priorityList": [x]})):
            if sid is None:
                continue
            cs = x["action"]["castSpell"]["spellId"]
            cs["spellId"] = sid
            cs["rank"] = {591: 2, 984: 4, 1004: 5}[sid]
            x["notes"] = (f"2026-11-20 (the audit session: no rank taught below 20 while the simulator gives it the full coefficient): rank "
                          f"{cs['rank']} in place of rank 2, smite_downrank_1120.py. " + x.get("notes", "")).strip()
        out.append(x)
    r["priorityList"] = out
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fights", type=int, default=10000)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    cls, ename = "priest", "smite-dps"
    entry = R.SPECS[cls][ename]
    rot = json.load(open(R.apl_path(entry, repo, "raid"), encoding="utf-8"))
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    trees = R.load_trees(repo, cls)
    bids = [b for b in entry.get("builds", []) if b in data]
    rec = {"fights": a.fights, "builds": {}, "mean": {}}
    for seed in (1, 2):
        bl = [{"label": f"{v}|{b}", "talents": R.talents_string(trees, R.alloc_of(data[b])), "apl_json": variant(rot, sid)}
              for v, sid in VARIANTS.items() for b in bids]
        rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"smite-dr-{seed}")
        for v in VARIANTS:
            for b in bids:
                r = rows.get(f"{v}|{b}") or {}
                rec["builds"].setdefault(b, {}).setdefault(v, {})[f"seed {seed}"] = {"dps": round(r.get("dps") or 0, 2),
                                                                                     "oom": round(r.get("oom_seconds") or 0, 1)}
    for v in VARIANTS:
        vals = [rec["builds"][b][v][f"seed {s}"]["dps"] for b in bids for s in (1, 2)]
        rec["mean"][v] = round(sum(vals) / len(vals), 2)
    now = rec["mean"]["rank 2 (now)"]
    for v, m in rec["mean"].items():
        print(f"{v:14s} mean {m:.2f} ({m / now - 1:+.2%} against rank 2); " + "; ".join(
            f"{b} {rec['builds'][b][v]['seed 1']['dps']}/{rec['builds'][b][v]['seed 2']['dps']} oom {rec['builds'][b][v]['seed 1']['oom']} s"
            for b in bids), flush=True)
    allowed = {v: m for v, m in rec["mean"].items() if v != "rank 2 (now)"}
    best = max(allowed, key=allowed.get)
    rec["best_allowed"] = best
    rec["gap"] = round(1 - allowed[best] / now, 4)
    print(f"best allowed: {best}; the gap (what the missing penalty gave rank 2): {rec['gap']:.2%}", flush=True)
    if a.apply:
        for f in FILES:
            d = json.load(open(f, encoding="utf-8"))
            new = variant(d, VARIANTS[best])
            f.write_text(json.dumps(new, indent=1) + "\n", encoding="utf-8", newline="")
            print(f"wrote {f.name}: {best}", flush=True)
        rec["applied"] = [f.name for f in FILES]
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
