"""The quests-and-dungeons gear tier for every raid damage spec (2026-11-18; user: "a pre-BIS list for the things that can just be
obtained through questing or doing dungeons and not having to do all of the work to get the 0.5 tier set", then "Go with your recs").

    python -u _reference/data/raidsim/dungeon_tier.py [classes] [--spec "<spec>" ...] [--fresh] [--iterations 30000]

Per ML record (raidsim/ml/<class>-<spec slug>.json) with a full-raid pre-BiS search:
1. the tier's set for that search's winner, in its entry, chosen in a full raid (gear_tiers.make with the `dungeon` pool: quest rewards
   of no raid, 5-player dungeon boss drops at 5% or more, trainer recipes, reputation to Honored, what Forever has now; the rules are
   gear_tiers.DUNGEONS's): the simulator's stat weights, the best item per slot, the trinkets raced, the choice confirmed on seed 2;
2. the record's tier winners (pre-BiS and BiS, full raid and training dummy) raced in that set in a full raid (`--iterations`, seed 1):
   the fastest is the tier's number. The tier has no talent search of its own: the other tiers' winners are its candidates, and between
   neighbouring gear tiers the best talents seldom move.
Record keys gear.dungeon and search["dungeon-raid"] (winner {allocation, split, dps}, race, candidates), so ml_builds.py --rank and
render_modes.py read it as they read the other tiers. Resumable: a record whose search["dungeon-raid"] ran on the current simulator commit
is skipped unless --fresh. --refit (2026-11-22, the audit session's G1-G3): the tier's set file as it stands goes through
gear_tiers.refit instead of a new make (with --fresh to redo a record already on the current commit).
"""
import argparse
import datetime
import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE)]
import gear_tiers as GT  # noqa: E402

G, R = GT.G, GT.R
ML = HERE / "ml"
KEYS = ("prebis-raid", "bis-raid", "prebis-dummy", "bis-dummy")
TODAY = datetime.date.today().isoformat()


def flat(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--spec", nargs="*", default=[])
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--iterations", type=int, default=30000)
    ap.add_argument("--smoke", action="store_true", help="small budgets; the ML record is not written (a test)")
    ap.add_argument("--refit", action="store_true", help="refit the tier's set as it stands (gear_tiers.refit) instead of making it again")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    commit = R.git_commit(repo)
    ga = GT.args_ns(iterations=500, confirm=1000, weight_iterations=500, max_pairs=3) if a.smoke else GT.args_ns()
    if a.smoke:
        a.iterations = 2000
    for f in sorted(p for p in ML.glob("*.json") if p.name not in ("rotations.json", "spell-probe.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        cls, spec = rec.get("class"), rec.get("spec")
        if (a.classes and cls not in a.classes) or (a.spec and spec not in a.spec):
            continue
        s = rec.get("search") or {}
        if not (s.get("prebis-raid") or {}).get("winner"):
            print(f"== {f.name}: no full-raid pre-BiS winner; skipped", flush=True)
            continue
        done = s.get("dungeon-raid") or {}
        if done.get("commit") == commit and not a.fresh:
            print(f"== {f.name}: done ({done.get('date')})", flush=True)
            continue
        t0 = time.time()
        trees = R.load_trees(repo, cls)
        known = {R.talent_key(t) for tr in trees for t in tr["talents"]}
        entry = s["prebis-raid"]["entry"]
        e = R.SPECS[cls][entry]
        base = {n: r for n, r in flat(s["prebis-raid"]["winner"]["allocation"]).items() if n in known}
        print(f"== {f.name}: the quests-and-dungeons set in {entry} for the pre-BiS full-raid winner", flush=True)
        dpath = GT.SETS / f"{cls}-{rec['slug']}-dungeon.gear.json"
        if a.refit and dpath.exists():   # (2026-11-22) the set as it stands, refit; its make() fields stay when they name the filed items
            names = [db[x["id"]]["name"] if x and x.get("id") in db else None for x in json.load(open(dpath, encoding="utf-8"))["items"]]
            pg = (rec.get("gear") or {}).get("dungeon") or {}
            g = GT.refit(cls, spec, "dungeon", entry, R.talents_string(trees, base), "ml winner (pre-BiS, full raid)", repo, db, zones, ga,
                         path=dpath, write=not a.smoke)
            gd = dict(pg) if pg.get("names") == names else {}
            gd.update({k: g[k] for k in ("entry", "gear", "date", "setting", "chosen", "ilvl", "names", "confirm_seed2", "weights", "weapons", "set_pieces", "enchants", "changes", "refit") if k in g})
            rec.setdefault("gear", {})["dungeon"] = dict(gd, commit=commit)
        else:
            g = GT.make(cls, spec, "dungeon", entry, R.talents_string(trees, base), "ml winner (pre-BiS, full raid)", repo, db, zones, ga,
                        path=dpath)
            keep = ("entry", "gear", "date", "chosen", "ilvl", "trinkets", "trinket_screen", "names", "race_seed1", "confirm_seed2", "weights",
                    "evaluated_on", "enchants_dropped", "weapons", "set_pieces", "enchants")
            rec.setdefault("gear", {})["dungeon"] = dict({k: g[k] for k in keep if k in g}, commit=commit)
        # the candidates: every tier winner of the record, distinct talents, raced in the new set in a full raid
        cands, seen = [], set()
        for k in KEYS:
            w = (s.get(k) or {}).get("winner")
            if not w:
                continue
            fl = {n: r for n, r in flat(w["allocation"]).items() if n in known}
            key = tuple(sorted(fl.items()))
            if key in seen:
                continue
            seen.add(key)
            cands.append((k, w["allocation"], fl))
        builds = [{"label": k, "talents": R.talents_string(trees, fl), "gear_json": {"items": g["items"]}} for k, _, fl in cands]
        res = G.run_bench(repo, G.bench_cfg(e, repo, builds, a.iterations, 1, "raid"), f"dungeon-{cls}-{rec['slug']}")
        scored = [(k, al, (res.get(k) or {}).get("dps")) for k, al, _ in cands if (res.get(k) or {}).get("dps")]
        if not scored:
            print(f"   no result for any candidate: {res}", flush=True)
            continue
        k, al, dps = max(scored, key=lambda x: x[2])
        split = "/".join(str(sum(r for _, r in v)) for v in al.values())
        rec.setdefault("search", {})["dungeon-raid"] = {
            "class": cls, "spec": spec, "setting": "raid", "entry": entry, "date": TODAY, "commit": commit,
            "method": "the record's tier winners raced in the tier's set in a full raid (no search of its own)",
            "winner": {"allocation": al, "split": split, "dps": round(dps, 1), "from": k},
            "race": [{"iterations": a.iterations, "seed": 1, "dps": sorted((round(x[2], 1) for x in scored), reverse=True)}],
            "candidates": {kk: round(d, 1) for kk, _, d in scored}, "minutes": round((time.time() - t0) / 60, 1)}
        if not a.smoke:
            f.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"   {spec}: {dps:.1f} DPS ({k}'s talents, {split}); candidates " + ", ".join(f"{kk} {d:.1f}" for kk, _, d in scored)
              + f"; {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
