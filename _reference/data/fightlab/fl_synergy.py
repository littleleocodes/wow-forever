"""Synergy certificate for an open leveling search's winner (2026-10-07): the fight-lab counterpart of raidsim/synergy.py, because the
leveling search has the same blind spot the raid search had (talents worth nothing alone and a lot together, behind a step that costs).

    python _reference/data/fightlab/fl_synergy.py <class> [--rotation <fight-lab spec>] [--fresh] [--no-search] [--jobs N]

Per done rotation of fightlab/open/<class>.json, around the winner at level 60 (kills per hour on SCREEN fights, common random numbers,
builds measured in parallel processes): every relevant talent the winner lacks added at full rank, every present one removed and at one
and two ranks less, every pair (both added; one added and one removed, different trees; both removed), all UNPAID (the fight lab applies
the talents as given); interaction = both - a - b + winner. Leads: pairs whose build gains or interacts, built legally (synergy.py's helpers,
the record's seconds-per-kill values as costs), screened at 60, the best polished keeping the pair, then raced at levels 20-60 with the
stats model's order against the winner (the pages' measure). A lead LEAD_BAR faster per kill means the search missed it: the open search
runs again seeded with the leads (a shorter budget), the winner is picked by the 20-60 race among the finalists, the leads and the known
positives, the values redone; `rotation["synergy"]` records it all and fl_open_search's report shows it. The fight lab is this project's
model of stated assumptions, not a measurement.
"""
import argparse
import datetime
import importlib.util
import json
import multiprocessing
import os
import pathlib
import random
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/raidsim")]


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


import fl_open_search as FO  # noqa: E402  (a real import: the worker processes unpickle its _ttk by module name)
FT, FR, SM, RSH = FO.FT, FO.FR, FO.SM, FO.RSH
SY = _load("synergy_fl", ROOT / "_reference/data/raidsim/synergy.py")   # pay / add_talent / with_talents / fill_up (generic over a Space)
TODAY = datetime.date.today().isoformat()
SCREEN = 400          # fights per measured build at level 60
POLISH_FIGHTS = 150   # the leads' climb
LEAD_WINDOW = 0.01    # lead builds within this of the winner at 60 are polished
LEAD_BAR = 0.01       # a polished lead this much faster per kill (levels 20-60) means the search missed it (the lab is noisier than the sim)
MAX_PAIRS = 2500
TOP_LEADS = 4
AGAIN = dict(FO.SEARCH, runs=2, budget=1500, random_init=150)


def log(m):
    print(m, flush=True)


def mlt():
    s = importlib.util.spec_from_file_location("ml_talents_syn", ROOT / "_reference/data/raidsim/ml_talents.py")
    M = importlib.util.module_from_spec(s)
    s.loader.exec_module(M)
    return M


def by_tree(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


def certificate(cls, spec, r, model, trees, pool, jobs, space, MLT, ours, a, save):
    t0 = time.time()
    w = FT.flat_of(r["winner"])
    vals = r.get("values") or {}
    cost = {n: v["per_point"] for n, v in vals.items()}   # seconds per kill lost per point: the cheapest points pay first
    relevant = space.relevant()
    missing = [n for n in relevant if not w.get(n)]
    present = [n for n in relevant if w.get(n)]
    sim = FO.LabSim(cls, spec, pool, jobs)

    def added(flat, names):
        new = dict(flat)
        for n in names:
            new[n] = space.max[n]
        return new

    def removed(flat, names):
        return {n: v for n, v in flat.items() if n not in names}

    builds, labels = [w], ["winner"]
    for t in missing:
        builds.append(added(w, [t]))
        labels.append(t)
    for t in present:
        builds.append(removed(w, [t]))
        labels.append(f"-{t}")
        if w[t] >= 2:
            builds.append(dict(w, **{t: w[t] - 1}))
            labels.append(f"{t} -1")
        if w[t] >= 3:
            builds.append(dict(w, **{t: w[t] - 2}))
            labels.append(f"{t} -2")
    pairs = []
    for i, a1 in enumerate(missing):
        for b1 in missing[i + 1:]:
            pairs.append((a1, b1, "add"))
    for a1 in missing:
        for b1 in present:
            if space.tree_of[a1] != space.tree_of[b1]:
                pairs.append((a1, b1, "swap"))
    for i, a1 in enumerate(present):
        for b1 in present[i + 1:]:
            pairs.append((a1, b1, "drop"))
    rng = random.Random(97)
    if len(pairs) > MAX_PAIRS:
        rng.shuffle(pairs)
        pairs = pairs[:MAX_PAIRS]
    kind = {}
    for a1, b1, k in pairs:
        if k == "add":
            builds.append(added(w, [a1, b1]))
            labels.append(f"{a1} + {b1}")
        elif k == "swap":
            builds.append(removed(added(w, [a1]), [b1]))
            labels.append(f"{a1} - {b1}")
        else:
            builds.append(removed(w, [a1, b1]))
            labels.append(f"-{a1} - {b1}")
        kind[(a1, b1)] = k
    log(f"== {cls} {spec}: leveling synergy certificate around {space.split(w)} at level 60: {len(relevant)} relevant talents, {len(missing)} missing; "
        f"{len(builds) - 1} builds ({len(kind)} pairs) on {SCREEN} fights")
    res = sim.run(builds, SCREEN, 61)
    score = {lab: x[0] for lab, x in zip(labels, res)}
    base = score["winner"] or 1e-9
    diffs = {}
    for lab, b in zip(labels, builds):
        if lab != "winner":
            diffs[lab] = {"added": {n: b[n] - w.get(n, 0) for n in b if b[n] > w.get(n, 0)},
                          "removed": {n: w[n] - b.get(n, 0) for n in w if w[n] > b.get(n, 0)}, "gain": round(score[lab] / base - 1, 5)}
    singles = {t: round(score[t] / base - 1, 4) for t in missing}
    for t in present:
        singles[f"-{t}"] = round(score[f"-{t}"] / base - 1, 4)
        for k in ("-1", "-2"):
            if f"{t} {k}" in score:
                singles[f"{t} {k}"] = round(score[f"{t} {k}"] / base - 1, 4)
    inter, removed_pairs = {}, {}
    for (a1, b1), k in kind.items():
        if k == "add":
            g = score[f"{a1} + {b1}"] / base - 1
            inter[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[a1] - singles[b1], 4)}
        elif k == "swap":
            g = score[f"{a1} - {b1}"] / base - 1
            inter[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[a1] - singles[f"-{b1}"], 4), "kind": "swap"}
        else:
            g = score[f"-{a1} - {b1}"] / base - 1
            removed_pairs[f"{a1} + {b1}"] = {"gain": round(g, 4), "interaction": round(g - singles[f"-{a1}"] - singles[f"-{b1}"], 4)}
    rec = {"date": TODAY, "winner": space.split(w), "relevant": len(relevant), "missing": len(missing), "pairs": len(kind), "screen_fights": SCREEN,
           "singles": dict(sorted(singles.items(), key=lambda kv: -kv[1])[:12]),
           "top_pairs": [{"pair": k, **v} for k, v in sorted(inter.items(), key=lambda kv: -kv[1]["gain"])[:12]],
           "top_interactions": [{"pair": k, **v} for k, v in sorted(inter.items(), key=lambda kv: -kv[1]["interaction"])[:12]], "leads": [],
           "base_kills_per_hour": round(base, 2), "winner_allocation": by_tree(space, w),
           "singles_all": singles, "pairs_all": inter, "removed_pairs_all": removed_pairs, "builds_all": diffs}
    # leads: legal builds of the pairs that gain or interact, screened at 60, polished keeping the pair, raced at 20-60 against the winner
    ranked = sorted(((v["gain"] + v["interaction"], k) for k, v in inter.items() if v["gain"] >= 0.005 or v["interaction"] >= 0.005), reverse=True)
    legal = []
    for _, lab in ranked[:TOP_LEADS * 4]:
        a1, b1 = lab.split(" + ")
        b = SY.with_talents(space, w, [a1], cost, drop=[b1]) if b1 in present else SY.with_talents(space, w, [a1, b1], cost)
        if b is not None:
            legal.append(((a1, b1), b))
    cands = []
    if legal:
        res2 = sim.run([b for _, b in legal], SCREEN, 61)
        cands = sorted([(x[0], pair, b) for (pair, b), x in zip(legal, res2) if x[0] >= base * (1 - LEAD_WINDOW)], key=lambda c: -c[0])
        log(f"   {len(legal)} lead builds screened, {len(cands)} within {LEAD_WINDOW:.0%} of the winner at 60")
    polished = []
    for sc, pair, b in cands[:TOP_LEADS]:
        x, sx = MLT.polish(space, sim, b, POLISH_FIGHTS, 62, rounds=24, min_gain=0.005, keep=pair, small=False)
        polished.append((sx, pair, x))
        log(f"    lead {pair[0]} + {pair[1]}: {space.split(b)} {sc:.1f} -> polished {space.split(x)} {sx:.1f} kills/h (winner {base:.1f} on {SCREEN})")
    leads = []
    if polished:
        polished.sort(key=lambda t: -t[0])
        top = polished[:3]
        race_builds = [{"id": "winner", "allocation": r["winner"]["allocation"], "order": r["order"]}]
        for _, pair, x in top:
            race_builds.append({"id": f"{pair[0]} + {pair[1]}", "allocation": by_tree(space, x), "order": FT.order_of(cls, model, x)})
        res3 = FT.race(pool, cls, spec, race_builds, FO.RACE_FIGHTS, 7)
        wt = res3[0][0]
        for (_, pair, x), rb, (t, per) in zip(top, race_builds[1:], res3[1:]):
            gain = wt / t - 1   # faster per kill
            leads.append({"pair": f"{pair[0]} + {pair[1]}", "split": space.split(x), "seconds": round(t, 2), "gain": round(gain, 4),
                          "allocation": rb["allocation"], "order": rb["order"], "levels": {str(L): round(v, 2) for L, v in per.items()}})
            log(f"    race 20-60: {pair[0]} + {pair[1]} {space.split(x)} {t:.2f} s per kill against the winner {wt:.2f} ({gain:+.2%} faster)")
    rec["leads"] = leads
    rec["minutes"] = round((time.time() - t0) / 60, 1)
    r["synergy"] = rec
    save()
    ahead = [ld for ld in leads if ld["gain"] >= LEAD_BAR]
    if not ahead or a.no_search:
        log(f"  {cls} {spec}: leveling certificate {'confirms the winner' if not ahead else 'found leads (no search)'} ({rec['minutes']} min)")
        return
    research(cls, spec, r, model, trees, pool, jobs, space, MLT, ours, leads, max(ahead, key=lambda ld: ld["gain"]), rec, save)


def research(cls, spec, r, model, trees, pool, jobs, space, MLT, ours, leads, best, rec, save):
    """The search missed something: the open search again seeded with the leads, the winner by the 20-60 race, values redone."""
    log(f"== {cls} {spec}: the leveling certificate's lead {best['split']} is {best['gain']:+.1%} faster: searching again from it")
    sim = FO.LabSim(cls, spec, pool, jobs)
    w = FT.flat_of(r["winner"])
    starts = [FT.flat_of(ld) for ld in leads] + [w] + [FT.flat_of(b) for b in ours.values()] + FO.known_positives(cls)
    starts = [s for s in starts if space.valid(s)]
    opts = MLT.defaults(**AGAIN, seed=85)
    rec2, win = MLT.optimize(space, {spec: sim}, starts, opts, log)
    cands, seen = [], set()
    for f in [rec2["winner"]] + rec2.get("finalists", [])[:5] + [{"allocation": ld["allocation"]} for ld in leads] + [{"allocation": r["winner"]["allocation"]}]:
        k = tuple(sorted(FT.flat_of(f).items()))
        if k not in seen:
            seen.add(k)
            cands.append({"id": f"finalist {space.split(FT.flat_of(f))}", "allocation": f["allocation"], "order": FT.order_of(cls, model, FT.flat_of(f))})
    builds = cands + list(ours.values())
    res = FT.race(pool, cls, spec, builds, FO.RACE_FIGHTS, 3)
    table = {b["id"]: {"weighted": round(x[0], 2), "levels": {str(L): round(v, 2) for L, v in x[1].items()}} for b, x in zip(builds, res)}
    bi = min(range(len(cands)), key=lambda i: res[i][0])
    r["winner"] = {"allocation": cands[bi]["allocation"], "split": space.split(FT.flat_of(cands[bi])), "picked_by": "the 20-60 race after the leveling certificate"}
    r["order"] = cands[bi]["order"]
    table["open winner"] = table.pop(cands[bi]["id"])
    r["race"] = table
    r["simulated_builds"] = r.get("simulated_builds", 0) + rec2["simulated_builds"]
    w2 = FT.flat_of(r["winner"])
    jobs_ = [(cls, spec, w2, 60, FO.VALUE_FIGHTS, 5)] + [(cls, spec, {k: v for k, v in w2.items() if k != n}, 60, FO.VALUE_FIGHTS, 5) for n in w2]
    vres = pool.map(FO._ttk, jobs_, chunksize=1)
    base = vres[0][0]
    r["values"] = dict(sorted({n: {"ranks": w2[n], "seconds": round(vres[i + 1][0] - base, 2), "per_point": round((vres[i + 1][0] - base) / w2[n], 2)}
                               for i, n in enumerate(w2)}.items(), key=lambda kv: -kv[1]["seconds"]))
    r["values_base"] = round(base, 2)
    best_ours = min((k for k in r["race"] if k != "open winner" and not k.startswith("finalist ")), key=lambda k: r["race"][k]["weighted"], default=None)
    r.update({"split": space.split(w2), "family": space.classify(w2), "link": RSH.tf_link(cls, w2), "ours_best": best_ours,
              "gain_vs_ours": round(r["race"][best_ours]["weighted"] / r["race"]["open winner"]["weighted"] - 1, 4) if best_ours else None})
    rec["researched"] = {"winner": r["split"], "seconds": r["race"]["open winner"]["weighted"], "lead": best["split"]}
    r.pop("builds", None)
    save()
    log(f"  {cls} {spec}: after the leveling certificate the open winner is {r['split']} ({r['family']}), {r['race']['open winner']['weighted']:.2f} s per kill"
        + (f", {r['gain_vs_ours']:+.1%} faster than {best_ours}" if best_ours else ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--rotation", action="append")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--no-search", action="store_true")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    a = ap.parse_args()
    cls = a.cls
    MLT = mlt()
    rp = FO.OUT / f"{cls}.json"
    st = json.load(open(rp, encoding="utf-8"))

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    data = {b["id"]: b for b in json.load(open(FO.paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    space = MLT.Space(cls, "any", any_split=True)
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for spec, r in st["rotations"].items():
            if a.rotation and spec not in a.rotation:
                continue
            if not r.get("done"):
                continue
            if r.get("synergy") and not a.fresh:
                log(f"== {cls} {spec}: leveling certificate done ({r['synergy'].get('date')})")
                continue
            model, trees = r["model"], r["trees"]
            ours = {bid: b for bid, b in data.items() if SM.mode_of(b) == "leveling" and SM.spec_of(cls, b) in trees}
            for bid, b in list(ours.items()):
                if not b.get("order"):
                    try:
                        ours[bid] = dict(b, order=FT.order_of(cls, model, FT.flat_of(b)))
                    except Exception:   # noqa: BLE001
                        ours.pop(bid)
            certificate(cls, spec, r, model, trees, pool, a.jobs, space, MLT, ours, a, save)
    FO.write_class(cls, st)
    FO.write_page()
    log("== done")


if __name__ == "__main__":
    main()
