"""Raid stat values for the damage specs the ML records leave out (2026-11-13, the gear add-on; user: "I want the add-on to be usable
across all classes and specs").

    python -u _reference/data/raidsim/page_stat_weights.py [classes] [--iterations 6000] [--dry-run]

The add-on's raid values come from each spec's ML record (ml/<class>-<spec slug>.json gear.bis.weights) and hit's value under the cap
from hit_below_cap.py, both for the record's best build. Raid pages with no such record (the Protection-Retribution and Shockadin
paladins, the Assassination-Subtlety rogue) or whose record names a build that is gone (Beast Mastery: beast-mastery-raid) get the
simulator's stat weights here, for the page's raid pick (render_modes.rank_builds, its full-raid entry) in the raid setting: in the spec's
own phase-1 BiS set (gear_sets/forever/tiers/<class>-<spec slug>-bis.gear.json, or the ML record's), else the BiS set of the ML record of
the build's biggest tree; hit under the cap with the set's hit taken off (bonus_stats StatHitRating, as hit_below_cap.py). Record
raidsim/page-stat-weights.json; characters/addon_values.py reads it after the ML records.
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
RECORD = HERE / "page-stat-weights.json"


def page_specs(cls):
    """[(spec, top build, entry)] for the class's raid pages with a damage pick. Run in its own process (--list): the page code imports
    the fight lab's `run`, a module name the simulator's run.py shares, and the two in one process read each other's."""
    import render_modes as RM
    import render_rotations as rr
    import spec_modes as SM
    B = rr.builds(cls)
    g = SM.grid(cls, list(B.values()))
    nums = (RM.raid_numbers(cls), RM.leveling_numbers(cls), RM.healer_numbers(cls))
    g = RM.own_rotation_only(cls, g, nums)
    specs = SM.trees(cls) + sorted(s for s in g if s.startswith("Hybrid") and g[s].get("raid"))
    out = []
    for spec in specs:
        bs = (g.get(spec) or {}).get("raid") or []
        if not bs:
            continue
        top = RM.rank_builds(cls, "raid", bs, nums)
        if not top or top[0].get("role") in ("healer", "tank"):
            continue
        r = nums[0].get(top[0]["id"]) or {}
        out.append((spec, top[0], r.get("entry")))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--iterations", type=int, default=6000)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true", help=argparse.SUPPRESS)
    a = ap.parse_args()
    classes = a.classes or "druid hunter mage paladin priest rogue shaman warlock warrior".split()
    if a.list:
        print(json.dumps({c: [[s, b, e] for s, b, e in page_specs(c)] for c in classes}))
        return
    import subprocess
    picks = json.loads(subprocess.run([sys.executable, __file__, "--list", *classes], capture_output=True, text=True, check=True).stdout)
    import gear_opt as G
    import gear_tiers as GT
    import run as R
    import spec_modes as SM
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, _ = GT.load_db(repo)
    below = json.loads((HERE / "hit-below-cap.json").read_text(encoding="utf-8")).get("specs", {})
    rec = json.loads(RECORD.read_text(encoding="utf-8")) if RECORD.exists() else {"specs": {}}
    rec.update(date=datetime.date.today().isoformat(), iterations=a.iterations)
    for cls in classes:
        trees = R.load_trees(repo, cls)
        for spec, b, entry in picks[cls]:
            stem = f"{cls}-{SM.slug(spec)}"
            mlf = HERE / "ml" / f"{stem}.json"
            ml = json.loads(mlf.read_text(encoding="utf-8")) if mlf.exists() else {}
            bis = (ml.get("gear") or {}).get("bis") if isinstance((ml.get("gear") or {}).get("bis"), dict) else None
            builds = {x["id"] for x in json.loads((ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json").read_text(encoding="utf-8"))["builds"]}
            covered = bool(bis and bis.get("weights")) and ml.get("best") in builds and stem in below
            if covered:
                continue
            need_w = not (bis and bis.get("weights"))
            own = HERE / "gear_sets" / "forever" / "tiers" / f"{stem}-bis.gear.json"
            if bis and bis.get("gear"):
                gear_path, why = bis["gear"], "the spec's ML record's BiS set"
            elif own.exists():
                gear_path, why = own.relative_to(ROOT).as_posix(), "the spec's own BiS set"
            else:
                pts = SM.tree_points(cls, b)
                lead = max(pts, key=pts.get)
                lf = HERE / "ml" / f"{cls}-{SM.slug(lead)}.json"
                gear_path = json.loads(lf.read_text(encoding="utf-8"))["gear"]["bis"]["gear"]
                why = f"the {lead} ML record's BiS set (no set of its own)"
            print(f"{stem}: page pick {b['id']} in {entry}; gear {gear_path} ({why}); "
                  + ("weights and hit" if need_w else "hit under the cap only"), flush=True)
            if a.dry_run:
                continue
            items = json.load(open(ROOT / gear_path, encoding="utf-8"))["items"]
            e = R.SPECS[cls][entry]
            tal = R.talents_string(trees, {n: r for n, r in R.alloc_of(b).items() if r})
            hit = sum(((db.get(x.get("id")) or {}).get("scalingOptions", {}).get("0", {}).get("stats", {}).get("17", 0) or 0) for x in items if x)
            row = {"class": cls, "spec": spec, "build": b["id"], "entry": entry, "gear": gear_path, "gear_why": why, "gear_hit_rating": hit}
            if need_w:
                w = G.run_bench(repo, G.bench_cfg(e, repo, [{"label": "w", "talents": tal, "gear_json": {"items": items}}], a.iterations, 1,
                                                  "raid", statweights=True), f"psw-{stem}")["w"]
                if w.get("error"):
                    print(f"  {w['error']}", flush=True)
                    continue
                row["weights"] = w["weights"]
            bw = {"label": "w", "talents": tal, "gear_json": {"items": items}}
            if hit:
                bw["bonus_stats"] = {"StatHitRating": -float(hit)}
            h = G.run_bench(repo, G.bench_cfg(e, repo, [bw], a.iterations, 1, "raid", statweights=True), f"psh-{stem}")["w"]
            row["hit_below_cap"] = round((h.get("weights") or {}).get("StatHitRating", 0.0), 4)
            rec["specs"][stem] = row
            ww = row.get("weights") or (bis or {}).get("weights") or {}
            print(f"  hit under the cap {row['hit_below_cap']:.4f}; spell damage {ww.get('StatSpellDamage', 0):.4f}, attack power "
                  f"{ww.get('StatAttackPower', 0):.4f}", flush=True)
            RECORD.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
