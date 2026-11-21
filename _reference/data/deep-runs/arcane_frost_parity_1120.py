"""Upstream parity for the Arcane/Frost hybrid (2026-11-20 night): the play check's c2 comparison read our arcane-frost-raid rotation
2-4% behind the official simulator's frost and arcane rotations on the entry's builds (3,000 fights, seed 1). "Simulator build first"
(2026-11-20): where the official rotation leads, it is the base unless ours is 0.5% ahead on two seeds; a hybrid may play either of its
two trees' rotations. The race: our raid rotation against the official frost, arcane and arcaneFireFill rotations (our converted copies
under apls/mage/upstream/), every build of the entry, full raid, 10,000 fights, seeds 1 and 2.

    python _reference/data/deep-runs/arcane_frost_parity_1120.py
Record raidsim/arcane-frost-parity-1120.json.
"""
import argparse
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import paths  # noqa: E402

OUT = DATA / "raidsim" / "arcane-frost-parity-1120.json"
UP = DATA / "raidsim" / "apls" / "mage" / "upstream"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    cls, ename = "mage", "arcane-frost-raid"
    entry = R.SPECS[cls][ename]
    rots = {"ours": json.load(open(R.apl_path(entry, repo, "raid"), encoding="utf-8"))}
    for n in ("frost", "arcane", "arcaneFireFill"):
        rots[n] = json.load(open(UP / f"{n}.apl.json", encoding="utf-8"))
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    trees = R.load_trees(repo, cls)
    bids = [b for b in entry.get("builds", []) if b in data]
    rec = {"entry": ename, "fights": a.fights, "rotation": pathlib.Path(R.apl_path(entry, repo, "raid")).name, "dps": {}}
    for seed in (1, 2):
        bl = [{"label": f"{rn}|{b}", "talents": R.talents_string(trees, R.alloc_of(data[b])), "apl_json": r} for rn, r in rots.items() for b in bids]
        rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"afparity-{seed}")
        for rn in rots:
            for b in bids:
                rec["dps"].setdefault(b, {}).setdefault(rn, {})[f"seed {seed}"] = round((rows.get(f"{rn}|{b}") or {}).get("dps") or 0, 2)
    for b in bids:
        d = rec["dps"][b]
        o1, o2 = d["ours"]["seed 1"], d["ours"]["seed 2"]
        line = []
        for rn in rots:
            v1, v2 = d[rn]["seed 1"], d[rn]["seed 2"]
            line.append(f"{rn} {v1:.1f}/{v2:.1f} ({v1 / o1 - 1:+.2%}/{v2 / o2 - 1:+.2%})")
        best = max((rn for rn in rots if rn != "ours"), key=lambda rn: min(d[rn]["seed 1"] / o1, d[rn]["seed 2"] / o2))
        lead = min(d[best]["seed 1"] / o1, d[best]["seed 2"] / o2) - 1
        rec.setdefault("best", {})[b] = {"rotation": best, "lead_both_seeds": round(lead, 4)}
        print(f"{b}: " + "; ".join(line) + f" -> best official {best}, ahead of ours by {lead:+.2%} on both seeds", flush=True)
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
