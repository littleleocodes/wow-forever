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
import fl_signature as FS  # noqa: E402  (signature spells, user rule 2026-10-22)



def live_link(cls, rec):
    """A record's winner as a talentsforever link made now (current code version and talent order); the stored one if that fails."""
    try:
        w = rec.get("winner") or ((rec.get("again") or rec.get("first") or {}).get("winner") or {})
        flat = {n: k for items in (w.get("allocation") or {}).values() for n, k in items if k}
        return RSH.tf_link(cls, flat) if flat else rec.get("link", "")
    except Exception:   # noqa: BLE001 - a report must not fail on a link
        return rec.get("link", "")

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


OUT = HERE / "open"
KNOWN = ROOT / "_reference/data/raidsim/known-positives.json"
PAGE = ROOT / "_reference" / "leveling-open-search.md"
TODAY = datetime.date.today().isoformat()
POLISH = dict(fights=150, rounds=24, per_pair=1, top=5, full_fights=600, min_gain=0.005, workers=2)   # the fight lab is noisier: a bigger bar; 24 batched steps and one draw
                                                                                            # per pair (2026-10-07 audit: 18 keystones made the polish an hour per rotation)
SEARCH = dict(runs=3, budget=2000, screen=400, patience=5, max_rounds=20, random_init=300, pool=8000, parents=40, finalists=6,
              race_stages=((1500, 2, 4), (4000, 3, 2), (10000, 4, 2)), cert_its=(800, 4000))
RACE_FIGHTS, VALUE_FIGHTS = 3000, 3000
SMOKE = False


def log(m):
    """Step lines ('== ...') carry the time of day: the logs under deep-runs/ are the record of what each step costs."""
    print((time.strftime("%H:%M ") if m.startswith("==") else "") + m, flush=True)


def _ttk(job):
    """(time per kill, per-fight spread of the fight time) of an allocation at a level; a broken build loses. A build that does not play
    its spec's signature spells (fl_signature: a required spell uncast, its talent missing, the core share under min_share at 60) has its
    time divided by fl_signature.penalty (2026-10-22, user rule), so every search, polish and certificate on this objective looks for the
    fastest build that plays its spec. A 7th element False (the talent values) measures the plain time."""
    cls, spec, alloc, level, fights, seed = job[:6]
    sig = job[6] if len(job) > 6 else True
    try:
        o = FR.simulate(cls, alloc, level, spec, fights, seed, 0)
        f = FS.penalty(FS.check(cls, spec, alloc, level, o)) if sig else 1.0
        return o["time_per_kill"] / f, (o.get("fight_sd") or 0.0) / f
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


def family_cache(cls, spec):
    return OUT / "cache" / f"{cls}-{spec}.families.json"


def sibling_starts(cls, spec, space, have):
    """The class's other leveling rotations' polished families as extra search starts (2026-10-07, as raidsim/family_search.py
    sibling_starts: tested as warm starts of the polish instead, they made 4 of 8 families worse)."""
    seen = {tuple(sorted(x.items())) for x in have}
    out = []
    for fp in sorted((OUT / "cache").glob(f"{cls}-*.families.json")):
        if fp == family_cache(cls, spec):
            continue
        try:
            rows = json.load(open(fp, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for d in rows:
            b = d.get("build") if isinstance(d, dict) else None
            if b:
                k = tuple(sorted(b.items()))
                if k not in seen and space.valid(b):
                    seen.add(k)
                    out.append(dict(b))
    return out


def known_positives(cls):
    if not KNOWN.exists():
        return []
    return [{n: r for n, r in p["allocation"].items() if r} for p in json.load(open(KNOWN, encoding="utf-8")).get("positives", [])
            if p.get("class") == cls and p.get("kind") == "leveling" and p.get("allocation")]


def rotations(cls):
    """{fight-lab spec: (scorer model, [trees that level with it])}; a rotation built for one hybrid alone
    (spec_modes.HYBRID_LEVELING_ROTATION, 2026-10-22: the mage's frostfire-leveling) lists the hybrid, with its first tree's model."""
    DL = _load("derive_leveling_open", ROOT / "_reference/data/derive_leveling.py")
    out = {}
    for (c, tree), (spec, model) in DL.LEVEL.items():
        if c == cls:
            out.setdefault(spec, (model, []))[1].append(tree)
    for (c, hyb), rot in SM.HYBRID_LEVELING_ROTATION.items():
        if c == cls and rot not in out:
            first = next((DL.LEVEL[(c, t)][1] for t in hyb[len("Hybrid "):].split("/") if (c, t) in DL.LEVEL), None)
            if first:
                out[rot] = (first, [hyb])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--rotation", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, a separate record, nothing else written (a test)")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--no-known", action="store_true", help="leave out the known positives and the last run's winners: a clean test of the search")
    a = ap.parse_args()
    global OUT, SEARCH, RACE_FIGHTS, VALUE_FIGHTS, SMOKE, POLISH
    if a.report:
        if a.cls and (OUT / f"{a.cls}.json").exists():   # 2026-10-15: the class page too, from its record (no search)
            write_class(a.cls, json.load(open(OUT / f"{a.cls}.json", encoding="utf-8")))
        write_page()
        return
    if a.smoke:
        OUT, SMOKE, RACE_FIGHTS, VALUE_FIGHTS = HERE / "open-smoke", True, 200, 200
        POLISH = dict(fights=40, rounds=1, per_pair=1, top=1, full_fights=60, min_gain=0.01)
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

    log(f"=== {cls} open leveling search started {datetime.datetime.now():%Y-%m-%d %H:%M}" + (" (--fresh)" if a.fresh else "")
        + f"; record {rp.name} ({len([r for r in st['rotations'].values() if r.get('done')])} rotations done)")   # the log is cumulative
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    space = MLT.Space(cls, "any", any_split=True)
    starts = [FT.flat_of(b) for b in data.values()] + MLT.popular_allocs(cls) + ([] if a.no_known else warm + known_positives(cls))
    starts = [x for x in starts if space.valid(x)]
    space.start_splits = [space.split(x) for x in starts]
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for spec, (model, trees) in rotations(cls).items():
            if a.rotation and spec not in a.rotation:
                continue
            r = st["rotations"].setdefault(spec, {"model": model, "trees": trees})
            if r.get("done"):
                continue
            t0 = time.time()
            # only builds that may use this rotation (2026-10-08, user decision: no spec takes another spec's rotation; the priest's
            # Discipline rotation had found a 31-point Shadow build, which no page may show with it)
            # 2026-10-22 (signature rule): and only builds of specs that level with it (spec_modes.leveling_rotation_ok: a hybrid with its
            # HYBRID_LEVELING_ROTATION only), each keeping the talents that grant its spec's required spells (fl_signature.leveling_space)
            FS.leveling_space(space, cls, spec)
            rstarts = [x for x in starts if space.valid(x)]
            if "winner" not in r:
                import random
                sim = LabSim(cls, spec, pool, a.jobs)
                log(f"== {cls} {spec}: family polish over every pair of {len(space.keystones())} keystones from different trees")
                fam = MLT.family_polish(space, sim, random.Random(83), log, **POLISH)
                if not SMOKE:   # the polished families, for the class's other rotations (their search starts) and re-runs
                    fp = family_cache(cls, spec)
                    fp.parent.mkdir(parents=True, exist_ok=True)
                    fp.write_text(json.dumps([{"score": sc, "build": x, "label": lab} for sc, x, lab in fam]) + "\n", encoding="utf-8")
                r["families"] = [{"keystones": lab, "split": space.split(x), "family": space.classify(x), "kills_per_hour": round(sc, 2)}
                                 for sc, x, lab in fam[:15]]
                sib = sibling_starts(cls, spec, space, rstarts + [x for _, x, _ in fam])
                log(f"== {cls} {spec} (levels as {', '.join(trees)}): open search at level 60, {len(rstarts) + len(fam) + len(sib)} starts "
                    f"({len(sib)} from sibling rotations' families)")
                opts = MLT.defaults(**SEARCH, seed=81)
                rec, win = MLT.optimize(space, {spec: sim}, rstarts + [x for _, x, _ in fam] + sib, opts, log)
                r.update({"winner": rec["winner"], "runs_agree": rec["runs_agree"], "simulated_builds": rec["simulated_builds"],
                          "important_features": rec.get("important_features"), "finalists": rec.get("finalists") or []})
                save()
            ours = {bid: b for bid, b in data.items() if SM.mode_of(b) == "leveling" and SM.spec_of(cls, b) in trees}
            for bid, b in list(ours.items()):   # 2026-10-06 audit: a leveling build without an order (the mage's Fire ones) was left out of the
                if not b.get("order"):          # race, so a winner raced against nothing; it gets the stats model's order instead
                    try:
                        ours[bid] = dict(b, order=FT.order_of(cls, model, FT.flat_of(b)))
                    except Exception as ex:   # noqa: BLE001
                        log(f"  {bid}: no order and none could be made ({type(ex).__name__}: {ex}); left out of the race")
                        ours.pop(bid)
            if "race" not in r:
                # the winner is picked by the 20-60 race among the level-60 finalists (2026-10-05: a build best at 60 can be slower on the
                # way), each with the scorer's leveling order, raced together with our leveling builds
                cands, seen = [], set()
                # eligible winners: the level-60 winner and finalists, plus the known positives (2026-10-06: the search's level-60 objective
                # preferred a 19/8/24 hunter that the 20-60 race put 0.8% behind the 17/10/24 positive it started from)
                pos = [] if a.no_known else [{"allocation": {t: [[n, x[n]] for n in space.by_tree[t] if x.get(n)] for t in space.tree_names}}
                                             for x in known_positives(cls)]
                for f in [r["winner"]] + r.get("finalists", [])[:5] + pos:
                    k = tuple(sorted(FT.flat_of(f).items()))
                    if k not in seen:
                        seen.add(k)
                        cands.append({"id": f"finalist {space.split(FT.flat_of(f))}", "allocation": f["allocation"], "order": FT.order_of(cls, model, FT.flat_of(f))})
                builds = cands + list(ours.values())
                res = FT.race(pool, cls, spec, builds, RACE_FIGHTS, 3)
                table = {b["id"]: {"weighted": round(x[0], 2), "levels": {str(L): round(v, 2) for L, v in x[1].items()}} for b, x in zip(builds, res)}
                # the pick among the finalists that play their spec's signature spells at levels 20-60 (2026-10-22); all of them when none does
                qual = FS.qualifying(pool, cls, spec, cands)
                for c_, (ok_, sm_) in zip(cands, qual):
                    if sm_ is not None:
                        table[c_["id"]]["signature"] = sm_.get("verdict")
                elig = [i for i, (ok_, _) in enumerate(qual) if ok_] or list(range(len(cands)))
                best = min(elig, key=lambda i: res[i][0])
                r["winner"] = {"allocation": cands[best]["allocation"], "split": space.split(FT.flat_of(cands[best])), "picked_by": "the 20-60 race among the finalists"}
                r["order"] = cands[best]["order"]
                table["open winner"] = table.pop(cands[best]["id"])
                r["race"] = table
                save()
            if "level_polish" not in r and not SMOKE:
                # the 20-60 polish and the order choice (2026-10-07, fl_levels.py): the race's pick climbs on the pages' measure (time per
                # kill at levels 20-60; the shaman's Elemental winner was 2.1% faster at 60 and 5.7% slower at 50), then its three orders
                # race; a changed winner gets new values here and a new certificate below
                FL = _load("fl_levels_fo", HERE / "fl_levels.py")
                FL.after_race(cls, spec, r, model, trees, pool, space, ours, save)
            w = FT.flat_of(r["winner"])
            if "values" not in r:
                jobs = [(cls, spec, w, 60, VALUE_FIGHTS, 5, False)] + [(cls, spec, {k: v for k, v in w.items() if k != n}, 60, VALUE_FIGHTS, 5, False) for n in w]
                res = pool.map(_ttk, jobs, chunksize=1)
                base = res[0][0]
                r["values"] = dict(sorted({n: {"ranks": w[n], "seconds": round(res[i + 1][0] - base, 2),
                                               "per_point": round((res[i + 1][0] - base) / w[n], 2)} for i, n in enumerate(w)}.items(),
                                          key=lambda kv: -kv[1]["seconds"]))
                r["values_base"] = round(base, 2)
                save()
            if "synergy" not in r and not SMOKE:
                # the leveling synergy certificate (2026-10-07, fightlab/fl_synergy.py): every single and pair of relevant talents measured
                # around the winner at level 60; a lead 1% faster at levels 20-60 searches again from it and redoes the race and values
                SYL = _load("fl_synergy_fo", HERE / "fl_synergy.py")
                SYL.certificate(cls, spec, r, model, trees, pool, a.jobs, space, MLT, ours, argparse.Namespace(no_search=False), save)
                FL = _load("fl_levels_fo", HERE / "fl_levels.py")
                FL.ensure_order(cls, spec, r, pool, space, save, model)   # a re-search's new winner comes with the stats model's order only
                w = FT.flat_of(r["winner"])
            set_signature(pool, cls, spec, r)
            best = min((k for k in r["race"] if k != "open winner" and not k.startswith("finalist ")), key=lambda k: r["race"][k]["weighted"], default=None)
            r.update({"split": space.split(w), "family": space.classify(w), "link": RSH.tf_link(cls, w), "ours_best": best,
                      "gain_vs_ours": round(r["race"][best]["weighted"] / r["race"]["open winner"]["weighted"] - 1, 4) if best else None,
                      "minutes": round((time.time() - t0) / 60, 1), "done": True,
                      "date": datetime.date.today().isoformat()})   # render_modes.current_record: the rotation's own date (audit 2 row 75)
            save()
            log(f"  {cls} {spec}: open winner {r['split']} ({r['family']}), {r['race']['open winner']['weighted']:.2f} s per kill (20-60)"
                + (f", {r['gain_vs_ours']:+.1%} faster than {best} ({r['race'][best]['weighted']:.2f} s)" if best else ""))
        if not SMOKE and not a.rotation:   # every winner under the class's other leveling rotations (fl_synergy.cross_rotations, 2026-10-07)
            SYL = _load("fl_synergy_fo", HERE / "fl_synergy.py")
            SYL.cross_rotations(cls, st, pool, save)
    if not SMOKE:
        write_class(cls, st)
        write_page()
    log("== done")


def set_signature(pool, cls, spec, r):
    """The winner's signature check at levels 20-60 (fl_signature.check_build; 2026-10-22): open_builds.py writes a build only when it
    passes, for the fingerprint it was made for (allocation, order, rotation rules)."""
    b = {"allocation": r["winner"]["allocation"], "order": r.get("order") or []}
    fp = FS.build_fingerprint(cls, b, spec)
    if (r.get("signature") or {}).get("fingerprint") == fp:
        return r["signature"]
    sm = FS.check_build(pool, cls, spec, b)
    sm["fingerprint"] = fp
    r["signature"] = sm
    log(f"  {cls} {spec}: signature check of the winner ({sm.get('spec')}): {sm.get('verdict')}")
    return sm


def ours_vs(r):
    """(our fastest build in the rotation's 20-60 race, how much faster the open winner is), leaving out the finalists and the builds this
    search wrote itself (open_builds.py: `<spec>-open-leveling`, the winner's copy): 2026-10-15 page audit B17, the report had compared a
    winner with its own written copy. (None, None) when the race holds no other build of ours."""
    written = set((r.get("builds") or {}).get("written") or [])
    race = r.get("race") or {}
    others = {k: v for k, v in race.items() if k != "open winner" and not k.startswith("finalist ") and k not in written and v.get("weighted")}
    if "open winner" not in race or not others:
        return (None, None) if written & set(race) else (r.get("ours_best"), r.get("gain_vs_ours"))
    best = min(others, key=lambda k: others[k]["weighted"])
    return best, round(others[best]["weighted"] / race["open winner"]["weighted"] - 1, 4)


def write_class(cls, st):
    o = [f"# {cls.capitalize()}: open leveling search (generated)", "",
         f"> Generated by `_reference/data/fightlab/fl_open_search.py` on {TODAY}; record `_reference/data/fightlab/open/{cls}.json`. Do not hand-edit.", "",
         "Every legal 51-point build, no tree rule, searched in each leveling rotation of the class at level 60 in the fight lab (solo, "
         "same-level mobs, eating, drinking and deaths included), then given a leveling order and raced at levels 20-60 (higher levels count "
         "more) against our leveling builds. Faster is better. The fight lab is this project's model of stated assumptions.", "",
         "| Rotation | Trees that level with it | Open winner | Family | Seconds per kill (20-60) | vs our fastest there |", "|---|---|---|---|---|---|"]
    for spec, r in st["rotations"].items():
        if r.get("done"):
            best, gain = ours_vs(r)
            o.append(f"| {spec} | {', '.join(r['trees'])} | [{r['split']}]({live_link(cls, r)}) | {r['family']} | {r['race']['open winner']['weighted']:.2f} | "
                     + (f"{gain:+.1%} faster than {best}" if gain is not None else "-") + " |")
    o.append("")
    for spec, r in st["rotations"].items():
        if not r.get("done"):
            continue
        o += [f"## {spec}", "", f"**Open winner {r['split']}** ({r['family']}): talent values at level 60 (seconds per kill lost without the "
              f"talent; the build: {r['values_base']:.2f} s):", "", "| Talent | Ranks | Seconds lost without it | Per point |", "|---|---|---|---|"]
        o += [f"| {n} | {v['ranks']} | {v['seconds']:+.2f} | {v['per_point']:+.2f} |" for n, v in r["values"].items()]
        written = set((r.get("builds") or {}).get("written") or [])
        o += ["", "Race at levels 20-60 (seconds per kill): " + ", ".join(f"{k}{' (the build this search wrote)' if k in written else ''} {v['weighted']:.2f}"
                                                                         for k, v in sorted(r["race"].items(), key=lambda kv: kv[1]["weighted"])) + ".", ""]
        sg = r.get("signature")
        if sg:   # fl_signature.check_build (2026-10-22): does the winner play its spec's signature spells?
            o += [f"**Signature spells** ({sg.get('spec')}, levels 20-60, {sg.get('date')}): {sg.get('verdict')}"
                  + (f"; core share at 60 {sg['core_share']:.0%} (rule {sg['min_share']:.0%}: {', '.join(sg.get('core') or [])})" if sg.get("core") else "") + ".", ""]
        sy = r.get("synergy")
        if sy:   # fl_synergy.py: every pair of relevant talents measured around the winner at level 60
            o += [f"**Synergy certificate** ({sy['date']}, fightlab/fl_synergy.py): {sy['relevant']} relevant talents, {sy['missing']} the winner lacks; "
                  f"{sy['pairs']} pairs measured around {sy['winner']} at level 60 on {sy['screen_fights']} fights. Largest interactions (kills per hour of both "
                  "against the two alone): " + ", ".join(f"{x['pair']} {x['interaction']:+.1%} (build {x['gain']:+.1%})" for x in sy.get("top_interactions", [])[:6]) + ". "
                  + (("Leads polished and raced at 20-60: " + ", ".join(f"{ld['pair']} -> {ld['split']} {ld['gain']:+.1%}" for ld in sy["leads"]) + ". ") if sy.get("leads") else "No pair build within 1% of the winner. ")
                  + (f"**The search had missed it: searched again from the lead {sy['researched']['lead']}, winner now {sy['researched']['winner']} at {sy['researched']['seconds']:.2f} s per kill.**"
                     if sy.get("researched") else "The certificate confirms the winner."), ""]
        cr = (st.get("cross") or {}).get(spec)
        if cr:   # fl_synergy.cross_rotations: the winner under the class's other leveling rotations
            o += ["Under the other leveling rotations (seconds per kill, 20-60): " + ", ".join(f"{k} {v}" for k, v in cr["tested"].items())
                  # 2026-10-15 page audit B17: each spec plays its own rotation (user rule 2026-10-08); a faster sibling is research only
                  + (f"; {cr['best']} plays it faster ({cr['best_seconds']} s against {cr['own']} s). Research only: the pages keep each "
                     "spec on its own rotation." if cr.get("best") != spec
                     else f"; its own rotation plays it best ({cr['own']} s)."), ""]
        bw = r.get("builds")
        if bw:   # open_builds.py's verdict: a derived build on the pages, or the build it confirms
            o += [f"Build ({bw['date']}, open_builds.py): " + (", ".join(f"`{b}`" for b in bw["written"]) if bw.get("written") else bw.get("why") or "none") + ".", ""]
    p = paths.scenario_dir(cls, "leveling") / "open-search.md"
    p.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {p.relative_to(ROOT).as_posix()}")


def write_page():
    rows = []
    for f in sorted(OUT.glob("*.json")):
        if f.name.endswith(".prev.json"):   # a warm-start record of an earlier pass (2026-10-06: it had put the pass's rows on the page)
            continue
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
        o.append(f"| [{cls}]({paths.rel(PAGE, paths.scenario_dir(cls, 'leveling') / 'open-search.md')}) | {spec} | [{r['split']}]({live_link(cls, r)}) | "
                 f"{r['family']} | {r['race']['open winner']['weighted']:.2f} | " + (f"{ours_vs(r)[1]:+.1%}" if ours_vs(r)[1] is not None else "-") + " |")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    log(f"wrote {PAGE.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
