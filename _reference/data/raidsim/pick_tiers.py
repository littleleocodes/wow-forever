"""Gear tiers for a page's pick, without a talent search (2026-11-20, the short-check method: "Simulator build first" in CLAUDE.md;
the user: "a viable build and rotation for each classes spec"; the independent audit: a short check where the pick is a simulator build
under its own rotation, "plus the gear tiers for the pick, since the pages need the tier tables").

    python -u _reference/data/raidsim/pick_tiers.py <class> "<spec>" --entry <entry> --build <build id> [--iterations 10000]

Writes the spec's ML-shaped record raidsim/ml/<class>-<spec slug>.json (the finished record it replaces moves to ml/prev/, as
ml_pipeline.py --fresh does): the pre-BiS and BiS sets made for the pick in its entry (ml_pipeline.gear: gear_tiers.make, chosen in a
full raid), the pick raced in each set on the training dummy and in a full raid (seed 1, --iterations) as the tier's "winner", and a
"compare" naming only the pick, so ml_builds.py writes no build from it. render_modes.py's tier table and gear_links.py read it as they
read a search's record; `pick_tiers` marks it (the table then says the numbers are the page's pick, not a search's best). Then run
dungeon_tier.py <class> --spec "<spec>" --fresh for the quests-and-dungeons tier.
"""
import argparse
import datetime
import json
import math
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import gear_tiers as GT  # noqa: E402
import ml_pipeline as MP  # noqa: E402
import spec_modes as SM  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("spec")
    ap.add_argument("--entry", required=True)
    ap.add_argument("--build", required=True)
    ap.add_argument("--iterations", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    trees = R.load_trees(repo, a.cls)
    data = {b["id"]: b for b in json.load(open(ROOT / a.cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    b = data[a.build]
    alloc = b["allocation"]
    talents = R.talents_string(trees, R.alloc_of(b))
    split = "/".join(str(sum(r for _, r in alloc.get(t["name"], []))) for t in trees)
    slug = SM.slug(a.spec)
    path = HERE / "ml" / f"{a.cls}-{slug}.json"
    if path.exists():
        (HERE / "ml" / "prev").mkdir(exist_ok=True)
        old = json.load(open(path, encoding="utf-8"))
        if all(k in (old.get("search") or {}) for k in ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid")) and "compare" in old:
            shutil.copyfile(path, HERE / "ml" / "prev" / path.name)
    commit = R.git_commit(repo)
    today = datetime.date.today().isoformat()
    rec = {"class": a.cls, "spec": a.spec, "slug": slug, "entries": [a.entry], "best": a.build, "best_entry": a.entry, "best_dps": None,
           "any_split": a.spec.startswith("Hybrid"), "date": today, "commit": commit, "gear": {}, "search": {},
           "pick_tiers": {"build": a.build, "date": today, "note": "the page's pick in each tier's gear (the short-check method of "
                          "2026-11-20); no talent search"}}
    db, zones = GT.load_db(repo)
    entry = R.SPECS[a.cls][a.entry]
    for tier in ("bis", "prebis"):
        g = MP.gear(rec, tier, alloc, a.build, a.entry, repo, db, zones)
        rec["gear"][tier] = g
        gpath = g["gear"]
        for setting in ("dummy", "raid"):
            gp = pathlib.Path(gpath) if pathlib.Path(gpath).is_absolute() else ROOT / gpath
            items = json.load(open(gp, encoding="utf-8"))["items"]
            rows = A.bench(entry, repo, [{"label": a.build, "talents": talents, "gear_json": {"items": items}}], a.iterations, 1, setting,
                           f"picktiers-{a.cls}-{slug}-{tier}-{setting}")
            row = rows.get(a.build) or {}
            dps = round(row.get("dps") or 0.0, 2)
            se = round((row.get("dps_stdev") or 0.0) / math.sqrt(max(1, a.iterations)), 3)
            rec["search"][f"{tier}-{setting}"] = {"class": a.cls, "spec": a.spec, "setting": setting, "entry": a.entry, "date": today,
                                                  "winner": {"allocation": alloc, "split": split, "dps": dps, "se": se,
                                                             "iterations": a.iterations},
                                                  "gear": gpath, "commit": commit, "pick_tiers": True}
            print(f"  {tier} {setting}: {a.build} {dps:.1f} (+- {se:.2f}) in {pathlib.Path(gpath).name}", flush=True)
    bd = rec["search"]["bis-dummy"]["winner"]
    rec["best_dps"] = rec["search"]["bis-raid"]["winner"]["dps"]
    rec["compare"] = {"setting": "dummy", "dps": {"winner": {"entry": a.entry, "dps": bd["dps"], "se": bd["se"]}}, "best_hand": a.build,
                      "gain_vs_hand": 0.0, "commit": commit, "pick_tiers": True}
    path.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
