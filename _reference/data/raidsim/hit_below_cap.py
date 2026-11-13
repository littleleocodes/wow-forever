"""What hit is worth below the cap at 60, per damage spec (2026-11-13, the gear add-on; user: "keep in mind caps for certain stats").

    python _reference/data/raidsim/hit_below_cap.py [classes...] [--iterations 6000]

The ML records' BiS stat weights (gear.bis.weights) are measured in each spec's phase-1 BiS set; a set at the hit cap reads hit as 0 there
(Arms: no StatHitRating at all), which says nothing about a player below the cap. This runs the simulator's stat weights once more for the
spec's best build in that set with the set's own hit rating taken off again (bonus_stats StatHitRating = minus the items' hit), so only the
build's talents and racial hit remain: the value of a hit point under the cap (in the same DPS-per-point unit as the record's weights).
Record raidsim/hit-below-cap.json.
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parent.parent
sys.path[:0] = [str(HERE), str(DATA)]
import gear_opt as G  # noqa: E402
import gear_tiers as GT  # noqa: E402
import run as R  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--iterations", type=int, default=6000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, _ = GT.load_db(repo)
    out = {"date": datetime.date.today().isoformat(), "iterations": a.iterations, "unit": "DPS per point (the ML record's weights' unit)",
           "specs": {}}
    for f in sorted((HERE / "ml").glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        cls = rec.get("class")
        bis = (rec.get("gear") or {}).get("bis")
        if (a.classes and cls not in a.classes) or not isinstance(bis, dict) or not bis.get("gear"):
            continue
        builds = {b["id"]: b for b in json.loads((ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json").read_text(encoding="utf-8"))["builds"]}
        b = builds.get(rec.get("best"))
        if not b:
            continue
        items = json.load(open(ROOT / bis["gear"], encoding="utf-8"))["items"]
        hit = sum(((db.get(x.get("id")) or {}).get("scalingOptions", {}).get("0", {}).get("stats", {}).get("17", 0) or 0) for x in items if x)
        e = R.SPECS[cls][bis.get("entry") or rec["best_entry"]]
        tal = R.talents_string(R.load_trees(repo, cls), {n: r for n, r in R.alloc_of(b).items() if r})
        build = {"label": "w", "talents": tal, "gear_json": {"items": items}}
        if hit:
            build["bonus_stats"] = {"StatHitRating": -float(hit)}
        row = G.run_bench(repo, G.bench_cfg(e, repo, [build], a.iterations, 1, "raid", statweights=True), f"hit-{f.stem}")["w"]
        if row.get("error"):
            print(f"{f.stem}: {row['error']}", flush=True)
            continue
        w = row["weights"]
        out["specs"][f.stem] = {"gear_hit_rating": hit, "hit_below_cap": round(w.get("StatHitRating", 0.0), 4),
                                "spell_damage": round(w.get("StatSpellDamage", 0.0), 4), "attack_power": round(w.get("StatAttackPower", 0.0), 4),
                                "at_bis": (bis.get("weights") or {}).get("StatHitRating", 0.0)}
        print(f"{f.stem:42s} gear hit {hit:4.0f}: below the cap {w.get('StatHitRating', 0):.4f} (at BiS "
              f"{(bis.get('weights') or {}).get('StatHitRating', 0):.4f})", flush=True)
    (HERE / "hit-below-cap.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
