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
    ap.add_argument("--make", action="store_true", help="make new tier sets for the pick (gear_tiers.make) instead of racing it in the spec's sets")
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
    old = {}
    if path.exists():
        (HERE / "ml" / "prev").mkdir(exist_ok=True)
        old = json.load(open(path, encoding="utf-8"))
        # a search's finished record goes to ml/prev/ (as ml_pipeline --fresh does); an earlier pick_tiers record never overwrites it
        if all(k in (old.get("search") or {}) for k in ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid")) and "compare" in old                 and not old.get("pick_tiers"):
            shutil.copyfile(path, HERE / "ml" / "prev" / path.name)
    commit = R.git_commit(repo)
    today = datetime.date.today().isoformat()
    rec = {"class": a.cls, "spec": a.spec, "slug": slug, "entries": [a.entry], "best": a.build, "best_entry": a.entry, "best_dps": None,
           "any_split": a.spec.startswith("Hybrid"), "date": today, "commit": commit, "gear": {}, "search": {},
           "pick_tiers": {"build": a.build, "date": today, "note": "the page's pick in each tier's gear (the short-check method of "
                          "2026-11-20); no talent search"}}
    entry = R.SPECS[a.cls][a.entry]
    prev_gear = old.get("gear") or {}
    # the spec's last search (2026-11-20, the audit: where the pick and the search's winner swap places between gear sets, each tier
    # shows the better of the two, raced in the same set on the same fights, and the record says the sets were chosen for the search's
    # winners; the gear-dependent comparison is settled in the optimality pass): the current record when it is a search's, else ml/prev/
    src = old if (old.get("search") and not old.get("pick_tiers")) else {}
    pp = HERE / "ml" / "prev" / path.name
    if not src and pp.exists():
        pv = json.load(open(pp, encoding="utf-8"))
        src = pv if (pv.get("search") and not pv.get("pick_tiers")) else {}
    flat_of = lambda al: {n: k for items in al.values() for n, k in items}   # noqa: E731
    alt_rows = {}
    # the database through the gear_tiers copy whose make() runs (ml_pipeline's): 2026-11-20 (search-improvements 0q) this script loaded
    # it through its own copy, so the copy that picked the items had an empty stat map and no vetted items, valued every item at 0 and
    # took each slot's first item in the database (Frost Med's level-30 set)
    db, zones = MP.GT.load_db(repo)
    for tier in ("bis", "prebis"):
        sp = GT.set_path(a.cls, a.spec, tier)
        if sp.exists() and not a.make:
            # the spec's own tier set as it stands (made by its search for that search's winner): the pick is raced in it. The record
            # describes the file as it is: a set kept from an earlier record keeps that record's make() fields only when they name
            # these items (a carried record had listed the level-30 set's items after the file was restored)
            rel = str(sp.relative_to(ROOT)).replace("\\", "/")
            its = json.load(open(sp, encoding="utf-8"))["items"]
            names = [db[x["id"]]["name"] if x and x.get("id") in db else None for x in its]
            ils = [db[x["id"]]["scalingOptions"]["0"].get("ilvl", 0) for x in its if x and x.get("id") in db]
            pg = prev_gear.get(tier) or {}
            g = dict(pg) if pg.get("names") == names else {k: pg[k] for k in ("entry", "setting") if k in pg}
            g.update(gear=rel, date=today, kept=True, names=names, ilvl=round(sum(ils) / max(1, len(ils)), 1),
                     note="the spec's tier set as it stands, made by its last search for that search's winner; not made for this pick")
            g.setdefault("entry", a.entry)
            g.setdefault("setting", "raid")
        else:
            g = MP.gear(rec, tier, R.alloc_of(b), a.build, a.entry, repo, db, zones)   # gear() takes the flat {talent: ranks}
        rec["gear"][tier] = g
        gpath = g["gear"]
        for setting in ("dummy", "raid"):
            gp = pathlib.Path(gpath) if pathlib.Path(gpath).is_absolute() else ROOT / gpath
            items = json.load(open(gp, encoding="utf-8"))["items"]
            sw = (((src.get("search") or {}).get(f"{tier}-{setting}") or {}).get("winner") or {})
            alt_t = R.talents_string(trees, flat_of(sw["allocation"])) if sw.get("allocation") else None
            bl = [{"label": a.build, "talents": talents, "gear_json": {"items": items}}]
            if alt_t and alt_t != talents:
                bl.append({"label": "search winner", "talents": alt_t, "gear_json": {"items": items}})
            rows = A.bench(entry, repo, bl, a.iterations, 1, setting, f"picktiers-{a.cls}-{slug}-{tier}-{setting}")
            row = rows.get(a.build) or {}
            dps = round(row.get("dps") or 0.0, 2)
            se = round((row.get("dps_stdev") or 0.0) / math.sqrt(max(1, a.iterations)), 3)
            win = {"allocation": alloc, "split": split, "dps": dps, "se": se, "iterations": a.iterations, "build": a.build}
            if len(bl) == 2:
                ar = rows.get("search winner") or {}
                adps = round(ar.get("dps") or 0.0, 2)
                alt_rows[f"{tier}-{setting}"] = {"pick_dps": dps, "search_winner_dps": adps, "search_winner_split": sw.get("split"),
                                                 "better": "search winner" if adps > dps else "pick"}
                if adps > dps:
                    win = {"allocation": sw["allocation"], "split": sw.get("split"), "dps": adps,
                           "se": round((ar.get("dps_stdev") or 0.0) / math.sqrt(max(1, a.iterations)), 3), "iterations": a.iterations,
                           "build": "the search's winner"}
            rec["search"][f"{tier}-{setting}"] = {"class": a.cls, "spec": a.spec, "setting": setting, "entry": a.entry, "date": today,
                                                  "winner": win, "gear": gpath, "commit": commit, "pick_tiers": True}
            print(f"  {tier} {setting}: {a.build} {dps:.1f} (+- {se:.2f}) in {pathlib.Path(gpath).name}"
                  + (f"; the search's winner {sw.get('split')} {alt_rows[f'{tier}-{setting}']['search_winner_dps']:.1f}"
                     if f"{tier}-{setting}" in alt_rows else ""), flush=True)
    if alt_rows:
        rec["pick_tiers"]["alt"] = alt_rows
        # the note only where the pages' rows (full raid) differ by more than the noise: the search's winner 0.5% ahead
        lead = {k: v for k, v in alt_rows.items() if k.endswith("-raid") and v["search_winner_dps"] > v["pick_dps"] * 1.005}
        if lead:
            sp_ = sorted({v["search_winner_split"] for v in lead.values() if v.get("search_winner_split")})
            rec["pick_tiers"]["note_gear"] = (f"The tier sets were chosen for the search's winning talents ({', '.join(sp_)}), which lead the "
                                              f"page's pick in them; each tier shows the better of the two. Which is better by gear is "
                                              f"settled in the optimality pass: each build in a set made for it, raced on two seeds.")
    bd = rec["search"]["bis-dummy"]["winner"]
    rec["best_dps"] = rec["search"]["bis-raid"]["winner"]["dps"]
    rec["compare"] = {"setting": "dummy", "dps": {"winner": {"entry": a.entry, "dps": bd["dps"], "se": bd["se"]}}, "best_hand": a.build,
                      "gain_vs_hand": 0.0, "commit": commit, "pick_tiers": True}
    path.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main()
