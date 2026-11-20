"""Audit step 2 (2026-11-19, the independent audit's D1/D2; user: "Go with the audits recommendations"): the official simulator's own
warlock rotations (raidsim/apls/warlock/upstream/, trainer ranks) against each entry's raid rotation, in every arm: each rotation of the
entry's tree x each demon option set (the entry's, and each upstream build file's where it differs) x each build (the entry's own and
the upstream builds of the entry's tree, by their talent strings), full raid, the entry's gear and consumables, the same fights,
10,000 fights on seeds 1 and 2. A gain is then the rotation's, the talents' or the pair's.

    python _reference/data/deep-runs/warlock_upstream_race.py [entries] [--fights 10000]

Record raidsim/warlock-upstream-race.json: per entry every arm's DPS on both seeds, our best arm (our rotation, our options) and the
best arm overall.
"""
import argparse
import copy
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import spec_modes as SM  # noqa: E402

UP = DATA / "raidsim" / "apls" / "warlock" / "upstream"
SIM_BUILDS = pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever" / "ui" / "specs" / "warlock" / "dps" / "builds"
OUT = DATA / "raidsim" / "warlock-upstream-race.json"
# each upstream rotation's tree (its build's spec): it competes only in entries of that tree (each spec plays its own rotation)
UP_TREE = {"aff_wrack": "Affliction", "sm_ruin": "Affliction", "demo_shadow_brand": "Demonology", "demo_fire_brand": "Demonology",
           "destro": "Destruction"}
OURS_AS = {"aff_wrack": "affliction-wrack-raid"}   # an upstream build already among ours


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entries", nargs="*")
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    trees = R.load_trees(repo, "warlock")
    ours = {b["id"]: b for b in json.load(open(ROOT / "warlock/research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    up = {}
    for f in sorted(SIM_BUILDS.glob("*.build.json")):
        name = f.name.replace(".build.json", "")
        d = json.load(open(f, encoding="utf-8"))
        up[name] = {"talents": d["player"]["talentsString"], "options": d["player"]["warlock"]["options"]["classOptions"],
                    "apl": str(UP / f"{name}.apl.json")}
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for e in a.entries or ["affliction-raid", "demonology-raid", "fire-destro-raid", "incinerate-raid", "sb-raid"]:
        entry = R.SPECS["warlock"][e]
        tree = next(iter(SM.RAID_ENTRY_TREES.get(("warlock", e), {"?"})))
        rots = {"ours": str(R.apl_path(entry, repo, "raid"))}
        rots.update({n: u["apl"] for n, u in up.items() if UP_TREE[n] == tree})
        opts = {"ours": entry["spec"]["warlock"]["options"]["classOptions"]}
        for n, u in up.items():
            if UP_TREE[n] == tree:
                o = {k: v for k, v in u["options"].items() if k != "soulShards"}
                o.setdefault("curseOptions", opts["ours"].get("curseOptions", "Elements"))
                if o not in opts.values():
                    opts[f"up:{n}"] = o
        builds = {}
        for bid in entry.get("builds", []):
            b = ours.get(bid)
            if b:
                builds[bid] = R.talents_string(trees, {n: r for items in b["allocation"].values() for n, r in items if r})
        for n, u in up.items():
            if UP_TREE[n] == tree and OURS_AS.get(n) not in builds:
                builds[f"up:{n}"] = u["talents"]
        print(f"== {e} ({tree}): rotations {list(rots)}, option sets {list(opts)}, builds {list(builds)}", flush=True)
        res = {}
        for on, o in opts.items():
            ent = copy.deepcopy(entry)
            ent["spec"]["warlock"]["options"]["classOptions"] = o
            bl = [{"label": f"{rn}|{on}|{bn}", "talents": t, "apl": rp} for rn, rp in rots.items() for bn, t in builds.items()]
            for seed in (1, 2):
                rows = A.bench(ent, repo, bl, a.fights, seed, "raid", f"wlup-{e}")
                for lab, row in rows.items():
                    res.setdefault(lab, {})[str(seed)] = round(row.get("dps") or 0.0, 2)
        mean = {lab: sum(v.values()) / len(v) for lab, v in res.items() if len(v) == 2}
        our_best = max((lab for lab in mean if lab.startswith("ours|ours|")), key=mean.get)
        best = max(mean, key=mean.get)
        rec[e] = {"tree": tree, "fights": a.fights, "rotations": rots, "options": opts, "builds": builds, "dps": res,
                  "our_best": our_best, "best": best, "gain": round(mean[best] / mean[our_best] - 1, 4)}
        for lab in sorted(mean, key=mean.get, reverse=True)[:12]:
            print(f"   {lab:60s} {res[lab]['1']:8.1f} {res[lab]['2']:8.1f}", flush=True)
        print(f"   ours: {our_best} {mean[our_best]:.1f}; best: {best} {mean[best]:.1f} ({rec[e]['gain']:+.2%})", flush=True)
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
