"""Open leveling search: every legal build, no tree rule, in every leveling rotation of a class (2026-10-04, user request after the raid
open search: the leveling builds have the same blind spot, a tree rule that keeps hybrids out of every search).

    python -u _reference/data/fightlab/fl_open_search.py <class> [--rotation <fight-lab spec>] [--fresh] [--smoke] [--jobs 10]
    python -u _reference/data/fightlab/fl_open_search.py --report          # the cross-class page only

Per leveling rotation of the class (derive_leveling.LEVEL: the fight-lab spec each tree levels with; a healer or tank tree with its own
rotation counts as one):
1. the machine-learning search of raidsim/ml_talents.py (random forest + genetic search, races, the one-move and chain-move check) over
   every legal 51-point build (Space with any_split), scored on kills per hour at level 60 in the fight lab (solo, same-level mobs, eating,
   drinking and deaths included; green gear), builds measured in parallel processes with common random numbers; starts: every build of
   ours, the popular builds;
2. the scorer's leveling order for the winner (fl_talent_opt.order_of: Optimizer.order under the rotation's model);
3. a race at levels 20-60 (weights level / 10, the pages' measure) on a fresh seed: the winner against our leveling builds of the trees
   that level with this rotation;
4. talent values at level 60: seconds per kill each talent of the winner saves (removal, common random numbers).
Level 60 is where the search looks: a build best at 60 but slow early loses the 20-60 race, which decides. Record
fightlab/open/<class>.json (resumable per rotation), reports <class>/research/leveling/open-search.md and _reference/leveling-open-search.md.
The fight lab is this project's model of stated assumptions (fightlab/tables.py), not an in-game measurement.
"""
import argparse
import datetime
import importlib.util
import json
import math
import multiprocessing
import os
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data")]
import fl_talent_opt as FT  # noqa: E402
import run as FR  # noqa: E402
import paths  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


OUT = HERE / "open"
PAGE = ROOT / "_reference" / "leveling-open-search.md"
TODAY = datetime.date.today().isoformat()
SEARCH = dict(runs=3, budget=2000, screen=400, patience=5, max_rounds=20, random_init=300, pool=8000, parents=40, finalists=6,
              race_stages=((1500, 2, 4), (4000, 3, 2), (10000, 4, 2)), cert_its=(800, 4000))
RACE_FIGHTS, VALUE_FIGHTS = 3000, 3000
SMOKE = False


def log(m):
    print(m, flush=True)


def _ttk(job):
    """(time per kill, per-fight spread of the fight time) of an allocation at a level; a broken build loses."""
    cls, spec, alloc, level, fights, seed = job
    try:
        o = FR.simulate(cls, alloc, level, spec, fights, seed, 0)
        return o["time_per_kill"], o.get("fight_sd") or 0.0
    except Exception as e:   # noqa: BLE001
        print(f"  error {type(e).__name__}: {e}", flush=True)
        return 1e9, 0.0


class LabSim:
    """ml_talents.Sim's interface on the fight lab: run(allocs, fights, seed) -> [(kills per hour, per-fight spread)]."""

    def __init__(self, cls, spec, pool, procs):
        self.cls, self.spec, self.pool, self.procs = cls, spec, pool, procs
        self.setting = "leveling"
        self.n = 0
        self.fights = 0

    def run(self, allocs, iterations, seed):
        jobs = [(self.cls, self.spec, al, 60, iterations, seed) for al in allocs]
        res = self.pool.map(_ttk, jobs, chunksize=max(1, len(jobs) // (self.procs * 4)))
        self.n += len(allocs)
        self.fights += len(allocs) * iterations
        return [(3600.0 / t, 3600.0 * sd / t ** 2) if t < 1e8 else (0.0, 0.0) for t, sd in res]


def rotations(cls):
    """{fight-lab spec: (scorer model, [trees that level with it])}."""
    DL = _load("derive_leveling_open", ROOT / "_reference/data/derive_leveling.py")
    out = {}
    for (c, tree), (spec, model) in DL.LEVEL.items():
        if c == cls:
            out.setdefault(spec, (model, []))[1].append(tree)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--rotation", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    global OUT, SEARCH, RACE_FIGHTS, VALUE_FIGHTS, SMOKE
    if a.report:
        write_page()
        return
    if a.smoke:
        OUT, SMOKE, RACE_FIGHTS, VALUE_FIGHTS = HERE / "open-smoke", True, 200, 200
        SEARCH = dict(runs=1, budget=60, screen=60, patience=1, max_rounds=1, random_init=20, pool=300, parents=6, finalists=2,
                      race_stages=((100, 2, 2), (200, 3, 1), (300, 4, 1)), cert_its=(60, 200))
    cls = a.cls
    s = importlib.util.spec_from_file_location("ml_talents_open", ROOT / "_reference/data/raidsim/ml_talents.py")
    MLT = importlib.util.module_from_spec(s)
    s.loader.exec_module(MLT)
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / f"{cls}.json"
    prev = rp.with_suffix(".prev.json")
    if a.fresh and rp.exists() and not SMOKE:
        rp.replace(prev)   # warm start (2026-10-05): the last run's winners seed the new search after a beta update
    st = json.load(open(rp, encoding="utf-8")) if rp.exists() and not a.fresh else {"class": cls, "date": TODAY, "rotations": {}}
    warm = [FT.flat_of(r["winner"]) for r in json.load(open(prev, encoding="utf-8")).get("rotations", {}).values()
            if r.get("winner")] if prev.exists() else []

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    space = MLT.Space(cls, "any", any_split=True)
    starts = [FT.flat_of(b) for b in data.values()] + MLT.popular_allocs(cls) + warm
    starts = [x for x in starts if space.valid(x)]
    space.start_splits = [space.split(x) for x in starts]
    import random
    starts = starts + space.keystone_starts(random.Random(83))   # every pair of keystones from different trees
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for spec, (model, trees) in rotations(cls).items():
            if a.rotation and spec not in a.rotation:
                continue
            r = st["rotations"].setdefault(spec, {"model": model, "trees": trees})
            if r.get("done"):
                continue
            t0 = time.time()
            if "winner" not in r:
                log(f"== {cls} {spec} (levels as {', '.join(trees)}): open search at level 60, {len(starts)} valid starts")
                sim = LabSim(cls, spec, pool, a.jobs)
                opts = MLT.defaults(**SEARCH, seed=81)
                rec, win = MLT.optimize(space, {spec: sim}, starts, opts, log)
                r.update({"winner": rec["winner"], "runs_agree": rec["runs_agree"], "simulated_builds": rec["simulated_builds"],
                          "important_features": rec.get("important_features")})
                save()
            w = FT.flat_of(r["winner"])
            if "order" not in r:
                r["order"] = FT.order_of(cls, model, w)
                save()
            ours = {bid: b for bid, b in data.items() if SM.mode_of(b) == "leveling" and SM.spec_of(cls, b) in trees and b.get("order")}
            if "race" not in r:
                builds = [{"id": "open winner", "allocation": r["winner"]["allocation"], "order": r["order"]}] + list(ours.values())
                res = FT.race(pool, cls, spec, builds, RACE_FIGHTS, 3)
                r["race"] = {b["id"]: {"weighted": round(x[0], 2), "levels": {str(L): round(v, 2) for L, v in x[1].items()}} for b, x in zip(builds, res)}
                save()
            if "values" not in r:
                jobs = [(cls, spec, w, 60, VALUE_FIGHTS, 5)] + [(cls, spec, {k: v for k, v in w.items() if k != n}, 60, VALUE_FIGHTS, 5) for n in w]
                res = pool.map(_ttk, jobs, chunksize=1)
                base = res[0][0]
                r["values"] = dict(sorted({n: {"ranks": w[n], "seconds": round(res[i + 1][0] - base, 2),
                                               "per_point": round((res[i + 1][0] - base) / w[n], 2)} for i, n in enumerate(w)}.items(),
                                          key=lambda kv: -kv[1]["seconds"]))
                r["values_base"] = round(base, 2)
                save()
            best = min((k for k in r["race"] if k != "open winner"), key=lambda k: r["race"][k]["weighted"], default=None)
            r.update({"split": space.split(w), "family": space.classify(w), "link": RSH.tf_link(cls, w), "ours_best": best,
                      "gain_vs_ours": round(r["race"][best]["weighted"] / r["race"]["open winner"]["weighted"] - 1, 4) if best else None,
                      "minutes": round((time.time() - t0) / 60, 1), "done": True})
            save()
            log(f"  {cls} {spec}: open winner {r['split']} ({r['family']}), {r['race']['open winner']['weighted']:.2f} s per kill (20-60)"
                + (f", {r['gain_vs_ours']:+.1%} faster than {best} ({r['race'][best]['weighted']:.2f} s)" if best else ""))
    if not SMOKE:
        write_class(cls, st)
        write_page()
    log("== done")


def write_class(cls, st):
    o = [f"# {cls.capitalize()}: open leveling search (generated)", "",
         f"> Generated by `_reference/data/fightlab/fl_open_search.py` on {TODAY}; record `_reference/data/fightlab/open/{cls}.json`. Do not hand-edit.", "",
         "Every legal 51-point build, no tree rule, searched in each leveling rotation of the class at level 60 in the fight lab (solo, "
         "same-level mobs, eating, drinking and deaths included), then given a leveling order and raced at levels 20-60 (higher levels count "
         "more) against our leveling builds. Faster is better. The fight lab is this project's model of stated assumptions.", "",
         "| Rotation | Trees that level with it | Open winner | Family | Seconds per kill (20-60) | vs our fastest there |", "|---|---|---|---|---|---|"]
    for spec, r in st["rotations"].items():
        if r.get("done"):
            o.append(f"| {spec} | {', '.join(r['trees'])} | [{r['split']}]({r['link']}) | {r['family']} | {r['race']['open winner']['weighted']:.2f} | "
                     + (f"{r['gain_vs_ours']:+.1%} faster than {r['ours_best']}" if r.get("ours_best") else "-") + " |")
    o.append("")
    for spec, r in st["rotations"].items():
        if not r.get("done"):
            continue
        o += [f"## {spec}", "", f"**Open winner {r['split']}** ({r['family']}): talent values at level 60 (seconds per kill lost without the "
              f"talent; the build: {r['values_base']:.2f} s):", "", "| Talent | Ranks | Seconds lost without it | Per point |", "|---|---|---|---|"]
        o += [f"| {n} | {v['ranks']} | {v['seconds']:+.2f} | {v['per_point']:+.2f} |" for n, v in r["values"].items()]
        o += ["", "Race at levels 20-60 (seconds per kill): " + ", ".join(f"{k} {v['weighted']:.2f}" for k, v in sorted(r["race"].items(), key=lambda kv: kv[1]["weighted"])) + ".", ""]
    p = paths.scenario_dir(cls, "leveling") / "open-search.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


def write_page():
    rows = []
    for f in sorted(OUT.glob("*.json")):
        st = json.load(open(f, encoding="utf-8"))
        for spec, r in st.get("rotations", {}).items():
            if r.get("done"):
                rows.append((st["class"], spec, r))
    o = ["# Open leveling search across the classes (generated)", "",
         f"> Generated by `_reference/data/fightlab/fl_open_search.py` on {TODAY}. Do not hand-edit.", "",
         "The fastest leveling build found with no tree rule in each leveling rotation (fight lab, levels 20-60, seconds per kill), against "
         "our fastest leveling build there. This project's fight-lab model; not in-game measurements.", "",
         "| Class | Rotation | Open winner | Family | Seconds per kill | vs ours |", "|---|---|---|---|---|---|"]
    for cls, spec, r in sorted(rows, key=lambda x: x[2]["race"]["open winner"]["weighted"]):
        o.append(f"| [{cls}]({paths.rel(PAGE, paths.scenario_dir(cls, 'leveling') / 'open-search.md')}) | {spec} | [{r['split']}]({r['link']}) | "
                 f"{r['family']} | {r['race']['open winner']['weighted']:.2f} | " + (f"{r['gain_vs_ours']:+.1%}" if r.get("gain_vs_ours") is not None else "-") + " |")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {PAGE.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
