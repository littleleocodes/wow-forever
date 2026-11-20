"""The page's pick under "Simulator build first" (2026-11-20, CLAUDE.md): the simulator's own build against ours in the entry's full raid,
10,000 fights on seeds 1 and 2; ours is the pick only when it leads by 0.5% or more on both seeds, else the simulator's build is.

    python -u _reference/data/raidsim/pick_decide.py <class> <entry> --sim <build id> --ours <build id> [<build id> ...] [--fights 10000]

Record raidsim/pick-decisions.json {class/entry: {sim, ours, dps, pick, gain}}; prints the pick on its last line ("pick: <id>").
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
from filelock import locked  # noqa: E402

OUT = HERE / "pick-decisions.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("entry")
    ap.add_argument("--sim", required=True)
    ap.add_argument("--ours", nargs="+", required=True)
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    trees = R.load_trees(repo, a.cls)
    data = {b["id"]: b for b in json.load(open(ROOT / a.cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    entry = R.SPECS[a.cls][a.entry]
    ids = [a.sim] + [b for b in a.ours if b != a.sim]
    bl = [{"label": b, "talents": R.talents_string(trees, R.alloc_of(data[b]))} for b in ids]
    dps = {}
    for seed in (1, 2):
        rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"pick-{a.cls}-{a.entry}")
        for b in ids:
            dps.setdefault(b, {})[str(seed)] = round((rows.get(b) or {}).get("dps") or 0.0, 2)
    best_ours = max(ids[1:], key=lambda b: dps[b]["1"] + dps[b]["2"])
    gains = [dps[best_ours][s] / dps[a.sim][s] - 1 for s in ("1", "2")]
    pick = best_ours if min(gains) >= 0.005 else a.sim
    for b in ids:
        print(f"  {b:40s} {dps[b]['1']:8.1f} {dps[b]['2']:8.1f}", flush=True)
    print(f"  ours' best {best_ours}: {gains[0]:+.2%} / {gains[1]:+.2%} against the simulator's {a.sim}", flush=True)
    with locked(OUT.with_suffix(".lock")):
        rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        rec[f"{a.cls}/{a.entry}"] = {"date": datetime.date.today().isoformat(), "commit": R.git_commit(repo), "fights": a.fights,
                                     "sim": {"repo": str(repo), **R.sim_switches(repo)},
                                     "sim": a.sim, "ours": ids[1:], "dps": dps, "best_ours": best_ours,
                                     "gain": [round(g, 4) for g in gains], "pick": pick}
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"pick: {pick}", flush=True)


if __name__ == "__main__":
    main()
