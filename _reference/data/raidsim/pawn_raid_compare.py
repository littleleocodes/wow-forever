"""Pawn's best raid set against the simulator's, raced in the simulator (2026-11-13; user: "the gear sets can be picked based on what Pawn
thinks is best at that level versus what we think is best and then raced and compared").

    python _reference/data/raidsim/pawn_raid_compare.py [classes...] [--iterations 10000]

Per damage spec with an ML record (ml/<class>-<spec slug>.json): our set is the spec's phase-1 BiS set (gear.bis.gear: picked by the
simulator's stat weights for the spec's best build, trinkets and variants raced); Pawn's set comes from the same pool (gear_tiers.pool_of
"bis") by the same per-slot step (gear_opt.class_picker's greedy), scored with Pawn 2.14.2's Forever weights for the tree with the most
points (before 2026-11-13 every spec read its class's first tree: pawn_scales.tree_points) (characters/pawn_scales.py: "+N Spell Power" 0, ratings times Classic's factors, no caps), the two trinkets with the
highest Pawn score, the relic and enchants kept. Both race the spec's best build in a full raid (seeds 1 and 2). Unlike the leveling race,
the simulator is not where our numbers come from by construction: its own engine plays the real items (procs, set bonuses, caps).
Record raidsim/pawn-raid-compare.json; characters/pawn_compare.py --write puts it on _reference/pawn-comparison.md.
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
sys.path[:0] = [str(HERE), str(DATA), str(DATA / "characters")]
import gear_opt as G  # noqa: E402
import gear_tiers as GT  # noqa: E402
import pawn_scales as PC  # noqa: E402
import run as R  # noqa: E402
import spec_modes as SM  # noqa: E402


def pawn_value_fn(scale):
    def value(it, w, slot):
        so = it.get("scalingOptions", {}).get("0", {})
        raw = {int(k): v for k, v in (so.get("stats") or {}).items()}
        dps = 0.0
        if it.get("type") in (13, 14) and so.get("weaponDamageMax") and it.get("weaponSpeed"):
            dps = (so["weaponDamageMin"] + so["weaponDamageMax"]) / 2 / it["weaponSpeed"]
        return PC.pawn_score(scale, PC.pawn_item_stats(raw, dps, it.get("type") == 14))
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--iterations", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    pool = GT.pool_of("bis", zones)
    scales = PC.pawn_scales()
    rows = []
    for f in sorted((HERE / "ml").glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        cls = rec.get("class")
        if a.classes and cls not in a.classes:
            continue
        bis = (rec.get("gear") or {}).get("bis")
        if not isinstance(bis, dict) or not bis.get("gear"):
            continue
        builds = {b["id"]: b for b in json.loads((ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json").read_text(encoding="utf-8"))["builds"]}
        b = builds.get(rec.get("best"))
        if not b:   # a record whose best build was renamed since (Beast Mastery's beast-mastery-raid): the raid page's pick
            pg = (json.loads((HERE / "page-stat-weights.json").read_text(encoding="utf-8")).get("specs", {}).get(f.stem, {})
                  if (HERE / "page-stat-weights.json").exists() else {})
            b = builds.get(pg.get("build"))
        if not b:
            print(f"{f.stem}: no build", flush=True)
            continue
        alloc = {n: r for n, r in R.alloc_of(b).items() if r}
        ti, tn = PC.tree_of(cls, alloc)
        scale = scales.get((PC.PAWN_CLASS[cls], PC.pawn_spec(cls, ti, tn, rec["spec"])))
        entry_name = bis.get("entry") or rec.get("best_entry")
        e = R.SPECS[cls][entry_name]
        ours = json.load(open(ROOT / bis["gear"], encoding="utf-8"))["items"]
        _, trinkets, greedy = G.class_picker(repo, cls, db, pool)
        orig = G.value
        G.value = pawn_value_fn(scale)
        try:
            pawn = greedy(ours, {}, False)
            tv = sorted((t for t in trinkets if t in db), key=lambda i: G.value(db[i], {}, 12), reverse=True)
            picked = []
            for t in tv:
                if len(picked) == 2:
                    break
                if not picked or G.pair_ok(db, (picked[0], t)):
                    picked.append(t)
            if len(picked) == 2:
                pawn[12], pawn[13] = {"id": picked[0]}, {"id": picked[1]}
        finally:
            G.value = orig
        trees = R.load_trees(repo, cls)
        tal = R.talents_string(trees, alloc)
        res = {}
        for seed in (1, 2):
            cfg = G.bench_cfg(e, repo, [{"label": "ours", "talents": tal, "gear_json": {"items": ours}},
                                        {"label": "pawn", "talents": tal, "gear_json": {"items": pawn}}], a.iterations, seed, "raid")
            out = G.run_bench(repo, cfg, f"pawn-{cls}-{rec['slug']}")
            for k in ("ours", "pawn"):
                res.setdefault(k, []).append(out[k].get("dps") or 0.0)
        o, p = sum(res["ours"]) / 2, sum(res["pawn"]) / 2
        name = lambda items, i: (db.get(items[i].get("id"), {}).get("name") if i < len(items) and items[i].get("id") else None)  # noqa: E731
        diff = {i: (name(pawn, i), name(ours, i)) for i in range(17) if (pawn[i].get("id") if i < len(pawn) else None) != (ours[i].get("id") if i < len(ours) else None)}
        row = {"class": cls, "spec": rec["spec"], "build": b["id"], "entry": entry_name, "pawn_scale": f"{cls} {PC.TREES[cls][ti - 1]}",
               "ours_dps": round(o, 1), "pawn_dps": round(p, 1), "ours_ahead": round(o / p - 1, 4) if p else None,
               "slots_differ": len(diff), "diff": {str(k): {"pawn": v[0], "ours": v[1]} for k, v in diff.items()}}
        rows.append(row)
        print(f"{cls:8s} {rec['spec'][:30]:30s}: ours {o:7.1f}, Pawn {p:7.1f} ({100 * row['ours_ahead']:+.1f}%), {len(diff)} slots differ", flush=True)
    rec = {"date": datetime.date.today().isoformat(), "iterations": a.iterations, "seeds": [1, 2], "setting": "raid", "rows": rows,
           "pawn": "Pawn 2.14.2, ClassicHawsJon.lua Forever weights"}
    (HERE / "pawn-raid-compare.json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
