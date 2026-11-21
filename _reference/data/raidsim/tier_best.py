"""Each raid page's pick in the best set each gear tier allows (2026-11-21, the audit session's interim fix for the tier tables): the
tier sets of the gear night (2026-11-18/19) were chosen for the builds and rotations of before 2026-11-20, and six pages showed Raid BiS
below Pre-BiS, four Raid BiS below the page's own standard-set number. Every pre-BiS item is allowed in Raid BiS and every dungeon item in
pre-BiS, so for each tier the pick is raced in every set legal there: the tier's own set, each lower tier's own set, and the entry's
standard set when the tier's pool (gear_tiers.pool_of) holds every item of it. The best is the tier's number, and the record says which
set it is. A tier with none of these is left out. The proper fix, sets made again for each pick under its current rotation, follows.

    python -u _reference/data/raidsim/tier_best.py [classes] [--fights 5000] [--write]

Record raidsim/tier-best.json {class: {spec: {build, entry, date, fights, sets: {name: {file, dps}}, standard_legal: {tier: bool},
tiers: {tier: {set, dps}}}}}; render_modes.tier_lines reads it for the page's pick.
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
OUT = HERE / "tier-best.json"
TIERS = ("dungeon", "prebis", "bis")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=5000)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    classes = a.classes or ["mage", "priest", "warlock", "hunter", "warrior", "rogue", "paladin", "shaman", "druid"]
    # the page picks in their own process (page_stat_weights.page_specs: the page code imports the fight lab's run.py)
    picks = json.loads(subprocess.run([sys.executable, str(HERE / "page_stat_weights.py"), "--list", *classes], capture_output=True,
                                      text=True, check=True, encoding="utf-8").stdout)
    import run as R
    import apl_opt as A
    import gear_tiers as GT
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    pools = {t: GT.pool_of(t, zones, repo) for t in TIERS}
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    today = datetime.date.today().isoformat()
    for cls in classes:
        trees = R.load_trees(repo, cls)
        for spec, b, ename in picks.get(cls) or []:
            entry = R.SPECS[cls][ename]
            talents = R.talents_string(trees, R.alloc_of(b))
            sets = {}
            for t in TIERS:
                p = GT.set_path(cls, spec, t)
                if p.exists():
                    sets[t] = p
            sp = R.sim_path(entry["gear"])
            sp = pathlib.Path(sp) if pathlib.Path(sp).is_absolute() else repo / entry["gear"]
            std_items = json.load(open(sp, encoding="utf-8"))["items"]
            legal = {}
            for t in TIERS:
                ids = [x.get("id") for x in std_items if x and x.get("id")]
                legal[t] = bool(ids) and all(i in db and pools[t](db[i]) for i in ids)
            sets["standard"] = sp
            items = {n: json.load(open(p, encoding="utf-8"))["items"] for n, p in sets.items()}
            bl = [{"label": n, "talents": talents, "gear_json": {"items": items[n]}} for n in sets]
            rows = A.bench(entry, repo, bl, a.fights, 1, "raid", f"tierbest-{cls}-{ename}")
            dps = {n: round((rows.get(n) or {}).get("dps") or 0.0, 2) for n in sets}
            out = {"build": b["id"], "entry": ename, "date": today, "fights": a.fights,
                   "sets": {n: {"file": str(p.relative_to(ROOT)).replace("\\", "/") if str(p).startswith(str(ROOT)) else str(p).replace("\\", "/"),
                                "dps": dps[n]} for n, p in sets.items()},
                   "standard_legal": legal, "tiers": {}}
            for i, t in enumerate(TIERS):
                cands = [x for x in TIERS[: i + 1] if x in sets] + (["standard"] if legal[t] else [])
                if cands:
                    best = max(cands, key=lambda n: dps[n])
                    out["tiers"][t] = {"set": best, "dps": dps[best], "own": dps.get(t)}
            print(f"{cls} {spec} ({b['id']} in {ename}): " + "; ".join(
                f"{t} {v['dps']:.1f} in {v['set']}" + (f" (own {v['own']:.1f})" if v.get("own") and v["set"] != t else "")
                for t, v in out["tiers"].items()) + f"; standard {dps['standard']:.1f} (legal in {', '.join(t for t in TIERS if legal[t]) or 'no tier'})",
                flush=True)
            rec.setdefault(cls, {})[spec] = out
            if a.write:
                OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
