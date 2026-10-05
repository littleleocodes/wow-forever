"""Open talent search: every legal build, no tree rule, in every damage rotation of a class (2026-10-04, user request: "Hybrid builds
across the classes might be the best performing specs ... theoretically each spec could be 17/17/17 ... we need to possibly do a ranking
of each specific talent and its weight and how much it brings to each build ... that also requires looking at different rotations").

    python -u _reference/data/raidsim/family_search.py <class> [--entry <entry>] [--fresh] [--smoke]
    python -u _reference/data/raidsim/family_search.py --report          # the cross-class page only

Why: every other search keeps a spec's tree rule (30+ points in the tree, or a named hybrid's two largest trees), so a build outside
every family is never tried, however long a search runs (2026-10-03: the 16/11/24 Summon Hawk + Lone Wolf melee hunter, 7% ahead of the
Survival pick in the simulator, was found by hand). Here the search space is all 51-point builds the trees allow (ml_talents.Space with
any_split), per damage entry of the class (each entry is a rotation and gear set; the showcase entries too), in a full raid:
1. the machine-learning search (random forest + genetic search, races, the one-move and chain-move check) from every build of ours,
   the entry's simulator presets and talentsforever.com's popular builds;
2. when the winner is a family the entry was not built for, or beats our best build there by 0.5%, the entry's rotation is re-tuned on
   it (apl_opt.py --tune; every build the entry lists stays protected) and the search runs once more, seeded with the winner;
3. a race over 30,000 fights: the winner against every build of ours the entry races;
4. talent values: every talent of the winner and of our best build there removed in turn (12,000 fights, common random numbers): DPS
   lost, per point, and the share of the build's DPS, plus the search's own feature importances (which talents its model leaned on).
The family of a build is spec_modes' rule: a tree with 30+ points, else "Hybrid A/B" of its two largest trees. A winner in a family no
machine-learning record covers is a lead for a deep search (deep_opt.py with a record for that family). Record raidsim/families/<class>.json
(resumable per entry), reports <class>/research/raid/family-search.md and _reference/family-search.md. The simulator's model of the beta
(and our patches), not in-game measurements; a family that wins on a mechanic the simulator may have wrong says so in the report.
"""
import argparse
import datetime
import importlib.util
import json
import math
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents_family", HERE / "ml_talents.py")
A, R = MLT.A, MLT.R
OUT = HERE / "families"
PAGE = ROOT / "_reference" / "family-search.md"
TODAY = datetime.date.today().isoformat()
SEARCH = dict(runs=3, budget=3000, screen=1500, patience=5, max_rounds=20, random_init=400, pool=10000, parents=48, finalists=6, screen_budget=600)
AGAIN = dict(SEARCH, runs=2, budget=2000)
RACE, VALUES = 30000, 12000
SMOKE = False


def log(m):
    print(m, flush=True)


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def by_tree(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


def entries(cls):
    """Every damage rotation of the class (tanks and healers have their own searches)."""
    return [e for e, x in R.SPECS[cls].items() if isinstance(x, dict) and "apl" in x and not x.get("tank")
            and x.get("profile", "raid-dps") == "raid-dps"]


def ours(cls):
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    return {bid: b for bid, b in data.items() if SM.mode_of(b) == "raid" and b.get("role") not in ("healer", "tank")}


def run_search(cls, entry, repo, settings, starts, seed, protect=None):
    space = MLT.Space(cls, "any", any_split=True)
    starts = [s for s in starts if s and space.valid(s)]
    space.protect = set(protect) if protect is not None else MLT.protected(cls, [entry], repo, "raid", starts)
    space.start_splits = [space.split(s) for s in starts]
    import random
    seeds = space.keystone_starts(random.Random(seed))   # every pair of keystones from different trees (Summon Hawk + Lone Wolf ...)
    starts = starts + seeds
    log(f"== {cls} {entry}: {len(seeds)} keystone seeds ({len(space.keystones())} keystones)")
    log(f"== {cls} {entry}: open search (any split, full raid), {len(starts)} valid starts; kept: {', '.join(sorted(space.protect)) or 'none'}")
    a = MLT.defaults(**settings, seed=seed)
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"family-{cls}-{entry}")
    rec, win = MLT.optimize(space, {entry: sim}, starts, a, log)
    return space, rec


def values(cls, entry, repo, flat):
    """{talent: {ranks, lost, per_point, share}}: DPS lost when each talent is removed (common random numbers)."""
    trees = R.load_trees(repo, cls)
    builds = [{"label": "base", "talents": R.talents_string(trees, flat)}]
    for n in flat:
        builds.append({"label": n, "talents": R.talents_string(trees, {k: v for k, v in flat.items() if k != n})})
    rows = A.bench(R.SPECS[cls][entry], repo, builds, VALUES, 5, "raid", f"family-values-{cls}")
    base = (rows.get("base") or {}).get("dps") or 0.0
    out = {}
    for n, r in flat.items():
        d = (rows.get(n) or {}).get("dps")
        if d is None or not base:
            continue
        lost = base - d
        out[n] = {"ranks": r, "lost": round(lost, 1), "per_point": round(lost / r, 1), "share": round(lost / base, 4)}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["lost"])), round(base, 1)


def race(cls, entry, repo, flat, mine):
    rows = {"open winner": flat} | {bid: R.alloc_of(b) for bid, b in mine.items()}
    sim = MLT.Sim(cls, entry, "raid", None, repo, f"family-race-{cls}")
    res = sim.run(list(rows.values()), RACE, 43)
    return {k: {"dps": round(d, 1), "se": round(sd / math.sqrt(RACE), 2)} for k, (d, sd) in zip(rows, res)}


def retune(cls, entry, flat):
    tune = OUT / "tune" / f"{cls}-{entry}.json"
    tune.parent.mkdir(parents=True, exist_ok=True)
    tune.write_text(json.dumps([{"label": "open winner", "allocation": flat}], indent=1), encoding="utf-8")
    log(f"== rotation {cls}/{entry}: tuning on the open winner (every build the entry lists protected)")
    r = subprocess.run([sys.executable, str(HERE / "apl_opt.py"), cls, "--spec", entry, "--tune", str(tune), "--write", "--rounds", "20"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    for ln in r.stdout.splitlines():
        if ln.strip().startswith(("==", "round", "raid", "wrote", "no change")):
            log("  " + ln.strip()[:220])
    R.set_game("forever")
    return "wrote" in r.stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    ap.add_argument("--report", action="store_true", help="write the cross-class page from the records and stop")
    a = ap.parse_args()
    global OUT, SEARCH, AGAIN, RACE, VALUES, SMOKE
    if a.report:
        write_page()
        return
    if a.smoke:
        OUT, SMOKE, RACE, VALUES = HERE / "families-smoke", True, 2000, 1000
        SEARCH = AGAIN = dict(runs=1, budget=150, screen=300, patience=1, max_rounds=1, random_init=40, pool=600, parents=8, finalists=2,
                              screen_budget=60, race_stages=((1000, 2, 2), (2000, 3, 1), (4000, 4, 1)), cert_its=(500, 2000))
    cls = a.cls
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / f"{cls}.json"
    st = json.load(open(rp, encoding="utf-8")) if rp.exists() and not a.fresh else {"class": cls, "date": TODAY, "entries": {}}

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    mine_all = ours(cls)
    starts = [R.alloc_of(b) for b in mine_all.values()] + MLT.popular_allocs(cls)
    for entry in a.entry or entries(cls):
        if entry in st["entries"] and st["entries"][entry].get("done"):
            continue
        t0 = time.time()
        e = st["entries"].setdefault(entry, {})
        here = {bid: mine_all[bid] for bid in R.SPECS[cls][entry].get("builds", []) if bid in mine_all}
        if "first" not in e:
            sp, rec = run_search(cls, entry, repo, SEARCH, starts + MLT.preset_allocs(cls, R.SPECS[cls][entry], repo), 71)
            e["first"] = {"winner": rec["winner"], "family": sp.classify(flat_of(rec["winner"]["allocation"])), "runs_agree": rec["runs_agree"],
                          "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"], "protected": sorted(sp.protect)}
            save()
        w = flat_of(e["first"]["winner"]["allocation"])
        if "race_first" not in e:
            e["race_first"] = race(cls, entry, repo, w, here)
            save()
        best_ours = max((v["dps"] for k, v in e["race_first"].items() if k != "open winner"), default=0.0)
        new_family = e["first"]["family"] not in {SM.spec_of(cls, b) for b in here.values()}
        if "again" not in e:
            if (new_family or e["race_first"]["open winner"]["dps"] > best_ours * 1.005) and not SMOKE:
                e["rotation_changed"] = retune(cls, entry, w)
                sp, rec = run_search(cls, entry, repo, AGAIN, [w] + starts, 72, protect=e["first"]["protected"])
                e["again"] = {"winner": rec["winner"], "family": sp.classify(flat_of(rec["winner"]["allocation"])), "runs_agree": rec["runs_agree"],
                              "important_features": rec.get("important_features"), "simulated_builds": rec["simulated_builds"]}
            else:
                e["again"] = None
            save()
        fin = e["again"] or e["first"]
        w = flat_of(fin["winner"]["allocation"])
        if "race" not in e:
            e["race"] = race(cls, entry, repo, w, here) if e["again"] else e["race_first"]
            save()
        if "values" not in e:
            e["values"], e["values_base"] = values(cls, entry, repo, w)
            best = max((k for k in e["race"] if k != "open winner"), key=lambda k: e["race"][k]["dps"], default=None)
            if best:
                e["values_ours"], e["values_ours_base"] = values(cls, entry, repo, R.alloc_of(mine_all[best]))
                e["ours_best"] = best
            save()
        sp = MLT.Space(cls, "any", any_split=True)
        e.update({"family": sp.classify(w), "split": sp.split(w), "dps": e["race"]["open winner"]["dps"], "link": RSH.tf_link(cls, w),
                  "gap_vs_ours": round(e["race"]["open winner"]["dps"] / max(1e-9, max((v["dps"] for k, v in e["race"].items() if k != "open winner"),
                                                                                    default=1e-9)) - 1, 4) if len(e["race"]) > 1 else None,
                  "minutes": round((time.time() - t0) / 60, 1), "done": True})
        save()
        log(f"  {cls} {entry}: open winner {e['split']} ({e['family']}) {e['dps']:.1f} DPS"
            + (f", {e['gap_vs_ours']:+.1%} vs our best there ({e.get('ours_best')})" if e.get("gap_vs_ours") is not None else ""))
    if not SMOKE:
        write_class(cls, st)
        write_page()
    log("== done")


def table(vals, base):
    o = ["| Talent | Ranks | DPS lost without it | Per point | Share of the build |", "|---|---|---|---|---|"]
    o += [f"| {n} | {v['ranks']} | {v['lost']:+.1f} | {v['per_point']:+.1f} | {v['share']:+.1%} |" for n, v in vals.items()]
    return o + ["", f"(the build: {base:.1f} DPS in a full raid; removal values do not add up to the build: talents interact)", ""]


def write_class(cls, st):
    o = [f"# {cls.capitalize()}: open talent search (generated)", "",
         f"> Generated by `_reference/data/raidsim/family_search.py` on {TODAY}; record `_reference/data/raidsim/families/{cls}.json`. Do not hand-edit.", "",
         "Every legal 51-point build, no tree rule, searched in each damage rotation of the class in a full raid (the community simulator's "
         "model of the beta with this project's patches). The family is a tree with 30+ points, else the two largest trees. Talent values: "
         "DPS lost when the talent is removed from the build, 12,000 fights, common random numbers.", "",
         "| Rotation (entry) | Open winner | Family | DPS | vs our best build there | Rotation re-tuned |", "|---|---|---|---|---|---|"]
    for entry, e in st["entries"].items():
        if not e.get("done"):
            continue
        o.append(f"| {entry} | [{e['split']}]({e['link']}) | {e['family']} | {e['dps']:.1f} | "
                 + (f"{e['gap_vs_ours']:+.1%} ({e.get('ours_best')})" if e.get("gap_vs_ours") is not None else "-")
                 + f" | {'yes' if e.get('rotation_changed') else 'no'} |")
    o.append("")
    for entry, e in st["entries"].items():
        if not e.get("done"):
            continue
        o += [f"## {entry}", "", f"**Open winner {e['split']}** ({e['family']}):", ""] + table(e["values"], e["values_base"])
        if e.get("values_ours"):
            o += [f"**Our best build there, {e['ours_best']}:**", ""] + table(e["values_ours"], e["values_ours_base"])
        imp = (e.get("again") or e.get("first") or {}).get("important_features") or []
        if imp:
            o += ["The search model's most important talents (random-forest importance): "
                  + ", ".join(f"{x['feature']} {x['importance']:.2f}" for x in imp[:10]) + ".", ""]
    p = paths.scenario_dir(cls, "raid") / "family-search.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


def write_page():
    rows = []
    for f in sorted(OUT.glob("*.json")):
        st = json.load(open(f, encoding="utf-8"))
        for entry, e in st.get("entries", {}).items():
            if e.get("done"):
                rows.append((st["class"], entry, e))
    o = ["# Open talent search across the classes (generated)", "",
         f"> Generated by `_reference/data/raidsim/family_search.py` on {TODAY}. Do not hand-edit.", "",
         "The best build found with no tree rule in each damage rotation, in a full raid, against our best build in that rotation. A winner "
         "in a family no search covered before (a hybrid such as 16/11/24) is a lead for a deep search. The community simulator's model of "
         "the beta with this project's patches; not in-game measurements.", "",
         "| Class | Rotation (entry) | Open winner | Family | DPS | vs our best there |", "|---|---|---|---|---|---|"]
    for cls, entry, e in sorted(rows, key=lambda x: -x[2]["dps"]):
        o.append(f"| [{cls}]({paths.rel(PAGE, paths.scenario_dir(cls, 'raid') / 'family-search.md')}) | {entry} | [{e['split']}]({e['link']}) | "
                 f"{e['family']} | {e['dps']:.1f} | " + (f"{e['gap_vs_ours']:+.1%}" if e.get("gap_vs_ours") is not None else "-") + " |")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {PAGE.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
