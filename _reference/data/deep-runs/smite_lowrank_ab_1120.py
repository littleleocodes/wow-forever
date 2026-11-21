"""Smite rank 2 in the Smite raid rotation (2026-11-20 night, the audit session's question): smite-open-raid casts Smite rank 2 (591,
taught at level 6, 2.0 s) 33.8 times a fight for 20.5% of its damage, more than its top rank. The official simulator gives rank 2 the full
cast-time coefficient (SPCoef 0.571 = 2.0 / 3.5) and applies no penalty for ranks learned below level 20 (Classic's rule, x(1 - (20 -
level) x 0.0375): 0.475 for a level-6 rank); our fork-era downranking patch was retired at the port. The A/B: the entry's raid rotation
against the same rotation without its rank-2 line, every build of the entry, full raid, 10,000 fights, seeds 1 and 2. Also a scan of
every rotation file of ours for casts of ranks taught below level 20.

    python _reference/data/deep-runs/smite_lowrank_ab_1120.py [--fights 10000]
Record raidsim/smite-lowrank-ab-1120.json.
"""
import argparse
import copy
import glob
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import paths  # noqa: E402
import flags_bench as FB  # noqa: E402

OUT = DATA / "raidsim" / "smite-lowrank-ab-1120.json"


def rank_levels(cls):
    out = {}
    p = DATA / "forever-spells" / f"{cls}.json"
    for tab in json.load(open(p, encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            for r in sp.get("ranks", []):
                if r.get("id"):
                    out[int(r["id"])] = (sp["name"], r.get("rank"), int(r.get("level") or 1))
    return out


def scan():
    rows = []
    for f in sorted(glob.glob(str(DATA / "raidsim" / "apls" / "*" / "*.apl.json"))):
        cls = pathlib.Path(f).parent.name
        lv = rank_levels(cls)
        apl = json.load(open(f, encoding="utf-8"))
        for part, i, sid, tag in FB.casts(apl):
            if sid in lv and lv[sid][2] < 20:
                rows.append({"file": pathlib.Path(f).relative_to(DATA).as_posix(), "line": f"{part}[{i}]", "spell": lv[sid][0], "rank": lv[sid][1],
                             "level": lv[sid][2]})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    low = scan()
    print(f"casts of ranks taught below level 20 in our rotation files: {len(low)}")
    for r in low:
        print(f"   {r['file']} {r['line']}: {r['spell']} {r['rank']} (level {r['level']})")
    cls, ename = "priest", "smite-dps"
    entry = R.SPECS[cls][ename]
    path = R.apl_path(entry, repo, "raid")
    rot = json.load(open(path, encoding="utf-8"))
    drop = [i for i, x in enumerate(rot["priorityList"]) if any(s == 591 for _, _, s, _ in FB.casts({"priorityList": [x]}))]
    rot_b = copy.deepcopy(rot)
    rot_b["priorityList"] = [x for i, x in enumerate(rot["priorityList"]) if i not in drop]
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    trees = R.load_trees(repo, cls)
    bids = [b for b in entry.get("builds", []) if b in data]
    names = R.spell_names(repo, cls)
    rec = {"rotation": pathlib.Path(path).name, "dropped_lines": drop, "fights": a.fights, "low_rank_casts": low, "builds": {}}
    for seed in (1, 2):
        bl = [{"label": f"{k}|{b}", "talents": R.talents_string(trees, R.alloc_of(data[b])), "apl_json": r}
              for k, r in (("with", rot), ("without", rot_b)) for b in bids]
        rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"smite-ab-{seed}")
        for b in bids:
            w, wo = rows.get(f"with|{b}") or {}, rows.get(f"without|{b}") or {}
            smites = lambda row: {f"rank {rank_levels(cls)[int(x['spellId'])][1].split()[-1]}": round(x.get("casts") or 0, 1)   # noqa: E731
                                  for x in (row.get("actions") or []) if x.get("spellId") in (585, 591, 598, 984, 1004, 6060, 10933, 10934) and x.get("casts")}
            rec["builds"].setdefault(b, {})[f"seed {seed}"] = {"with": round(w.get("dps") or 0, 2), "without": round(wo.get("dps") or 0, 2),
                                                              "smite_with": smites(w), "smite_without": smites(wo),
                                                              "oom_with": round(w.get("oom_seconds") or 0, 1), "oom_without": round(wo.get("oom_seconds") or 0, 1)}
            d = rec["builds"][b][f"seed {seed}"]
            print(f"   seed {seed} {b}: {d['with']} with the rank-2 line, {d['without']} without ({d['without'] / d['with'] - 1:+.2%}); "
                  f"Smite casts {d['smite_with']} -> {d['smite_without']}; out of mana {d['oom_with']} -> {d['oom_without']} s", flush=True)
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
