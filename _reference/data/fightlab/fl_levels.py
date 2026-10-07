"""The 20-60 polish of an open leveling winner, and the choice of its talent order (2026-10-07).

    python -u _reference/data/fightlab/fl_levels.py <class> [--rotation <fight-lab spec>] [--fresh] [--jobs 10]   # post hoc on a record

The open leveling search (fl_open_search.py) optimizes kills per hour at level 60 and picks its winner by a race at levels 20-60 among
the level-60 finalists. Self-audit of the shaman's Elemental rotation (2026-10-07): the level-60 winner 31/11/9 was 2.1% faster at 60
than opt-elemental-dps-leveling-st, 5.7% slower at 50 and 1.8% slower at 40, so 0.9% slower on the pages' measure (time per kill at
levels 20-60, weights level / 10). Level 60 is a proxy; what the pages rank on is the 20-60 race. So after the race:

1. **Polish at levels 40, 50 and 60** (`polish`): a hill climb from the race's pick over its one-move, prerequisite-chain and tier-chain
   neighbours (random batches), each neighbour with the stats model's own leveling order (fl_talent_opt.order_of, computed in the pool:
   about 9 s a build), scored on the weighted time per kill at levels 40, 50 and 60 (weights 4, 5, 6; the first twenty points of two
   neighbours differ little and levels 20-30 carry a quarter of the weight) with common random numbers; the best of a batch is kept when
   it is 0.3% faster on a second seed with more fights. The pick stays when no batch improves it.
2. **The order** (`pick_order`): the (polished) winner is raced at levels 20-60 on the race's seed and fights with three orders, the
   stats model's, own tree first and own tree last (raid_path_leveling's variants; the lead tree is the one with most points); the
   fastest is the page's (`order_label`). When the polish changed the build, the race's old pick stays in the table as a finalist and
   wins back when it is faster there: the race at 20-60 decides, as before.
A changed winner gets new talent values and loses its leveling certificate, which the caller redoes (fl_open_search's main loop, or
`main` here post hoc; a post-hoc change also redoes the class's cross-rotation races). Records: `level_polish`, `order_label` and the
race rows `finalist <split> (<order>)` / `finalist <split> (before the 20-60 polish)` in the rotation's entry of fightlab/open/<class>.json.
The fight lab is this project's model of stated assumptions, not an in-game measurement.
"""
import argparse
import datetime
import json
import multiprocessing
import os
import pathlib
import random
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data")]
import fl_open_search as FO  # noqa: E402
import fl_talent_opt as FT  # noqa: E402
import run as FR  # noqa: E402
import paths  # noqa: E402
import render_start_here as RSH  # noqa: E402
import spec_modes as SM  # noqa: E402

POLISH = dict(levels=(40, 50, 60), fights=150, batch=40, rounds=6, min_gain=0.003, confirm=400)
log = FO.log


# ------------------------------------------------------------------------------------------------ helpers
def alloc_of(space, flat):
    return {t: [[n, flat[n]] for n in space.by_tree[t] if flat.get(n)] for t in space.tree_names}


def expand(order):
    """Compressed order -> [(tree, talent)] one entry per point (raid_path_leveling.expand)."""
    return [(s["tree"], s["talent"]) for s in order for _ in range(s["points"])]


def compress(points, start=10):
    out = []
    for i, (tree, name) in enumerate(points):
        lv = start + i
        if out and out[-1]["talent"] == name:
            out[-1]["points"] += 1
            out[-1]["levels"] = f"{out[-1]['levels'].split('-')[0]}-{lv}"
        else:
            out.append({"levels": str(lv), "tree": tree, "talent": name, "points": 1})
    return out


def weighted_at(per, levels):
    tot = sum(L / 10 for L in levels)
    return sum(per[L] * L / 10 for L in levels) / tot


def evaluate(pool, cls, spec, builds, levels, fights, seed):
    """Weighted time per kill over `levels` for {allocation, order} builds (the allocation at each level from the order)."""
    jobs = [(cls, spec, FR.allocation_at(b, L), L, fights, seed) for b in builds for L in levels]
    res = pool.map(FO._ttk, jobs, chunksize=1)
    return [weighted_at({L: res[i * len(levels) + k][0] for k, L in enumerate(levels)}, levels) for i in range(len(builds))]


def row(x):
    return {"weighted": round(x[0], 2), "levels": {str(L): round(v, 2) for L, v in x[1].items()}}


def our_builds(cls, model, trees, data):
    """Our leveling builds of the trees that level with the rotation, each with an order (the stats model's when it has none)."""
    ours = {bid: b for bid, b in data.items() if SM.mode_of(b) == "leveling" and SM.spec_of(cls, b) in trees}
    for bid, b in list(ours.items()):
        if not b.get("order"):
            try:
                ours[bid] = dict(b, order=FT.order_of(cls, model, FT.flat_of(b)))
            except Exception as ex:   # noqa: BLE001
                log(f"  {bid}: no order and none could be made ({type(ex).__name__}: {ex}); left out of the race")
                ours.pop(bid)
    return ours


# ------------------------------------------------------------------------------------------------ the polish
def polish(cls, spec, r, model, pool, space, save, cfg=None):
    """Hill climb from the race's pick on the weighted time per kill at levels 40-60; returns (flat, order) when it moved, else None."""
    cfg = cfg or POLISH
    lv = list(cfg["levels"])
    cur = FT.flat_of(r["winner"])
    cur_b = {"allocation": r["winner"]["allocation"], "order": r["order"]}
    rng = random.Random(97)
    tried = {tuple(sorted(cur.items()))}
    steps, t0 = [], time.time()
    log(f"== {cls} {spec}: 20-60 polish of the race's pick {space.split(cur)} (levels {', '.join(map(str, lv))}, batches of {cfg['batch']}, "
        f"{cfg['fights']} fights, kept at {cfg['min_gain']:.1%} on a second seed)")
    for rnd in range(1, cfg["rounds"] + 1):
        nb, seen = [], set()
        for item in space.neighbours(cur, tier=True):
            x = item[1] if isinstance(item, tuple) else item
            k = tuple(sorted(x.items()))
            if k not in tried and k not in seen:
                seen.add(k)
                nb.append((k, x))
        rng.shuffle(nb)
        nb = nb[: cfg["batch"]]
        if not nb:
            log(f"    round {rnd}: no untried neighbour left")
            break
        tried.update(k for k, _ in nb)   # only the batch counts as tried: the rest may come up in a later round
        nb = [x for _, x in nb]
        orders = pool.map(FT.order_job, [(cls, model, x) for x in nb], chunksize=1)
        cands = [{"allocation": alloc_of(space, x), "order": o} for x, o in zip(nb, orders) if o]
        if not cands:
            break
        sc = evaluate(pool, cls, spec, [cur_b] + cands, lv, cfg["fights"], 11)
        ref, sc = sc[0], sc[1:]
        bi = min(range(len(cands)), key=lambda i: sc[i])
        if sc[bi] > ref * (1 - cfg["min_gain"]):
            log(f"    round {rnd}: {len(cands)} neighbours, none {cfg['min_gain']:.1%} faster at levels 40-60 (best {sc[bi] / ref - 1:+.2%})")
            break
        c2 = evaluate(pool, cls, spec, [cur_b, cands[bi]], lv, cfg["confirm"], 12)
        split = space.split(FT.flat_of(cands[bi]))
        if c2[1] > c2[0] * (1 - cfg["min_gain"]):
            log(f"    round {rnd}: {split} {sc[bi] / ref - 1:+.2%} on seed 11, {c2[1] / c2[0] - 1:+.2%} on seed 12: not confirmed")
            continue
        steps.append({"round": rnd, "split": split, "seed1": round(sc[bi] / ref - 1, 4), "seed2": round(c2[1] / c2[0] - 1, 4),
                      "seconds_40_60": round(c2[1], 2)})
        log(f"    round {rnd}: {split} {steps[-1]['seed1']:+.2%} on seed 11, {steps[-1]['seed2']:+.2%} on seed 12 ({c2[0]:.2f} -> {c2[1]:.2f} s): kept")
        cur, cur_b = FT.flat_of(cands[bi]), cands[bi]
    r["level_polish"] = {"date": FO.TODAY, "levels": lv, "from": space.split(FT.flat_of(r["winner"])), "steps": steps,
                         "neighbours_tried": len(tried) - 1, "minutes": round((time.time() - t0) / 60, 1), "changed": bool(steps)}
    save()
    return (cur, cur_b["order"]) if steps else None


def pick_order(cls, spec, r, pool, space, save, before=None):
    """Race the winner's three orders (and, after a polish, the race's old pick) at levels 20-60 on the race's seed and fights; the
    fastest row becomes "open winner" (the old pick wins back when it is faster: the 20-60 race decides)."""
    w = FT.flat_of(r["winner"])
    split = space.split(w)
    lead = max(space.tree_names, key=lambda t: sum(w.get(n, 0) for n in space.by_tree[t]))
    pts = expand(r["order"])
    variants = [("own tree first", compress([p for p in pts if p[0] == lead] + [p for p in pts if p[0] != lead])),
                ("own tree last", compress([p for p in pts if p[0] != lead] + [p for p in pts if p[0] == lead]))]
    table = r["race"]
    labels = {f"finalist {split} (stats model's order)": ("stats model", r["order"])}
    before_id = None
    if before:
        before_id = f"finalist {before['split']} (before the 20-60 polish)"
        table[before_id] = table.pop("open winner")
        variants.insert(0, ("stats model", r["order"]))
    else:
        table[next(iter(labels))] = table["open winner"]
    cands = []
    for lab, o in variants:
        cid = f"finalist {split} ({lab}{'' if lab == 'stats model' else ' order'})" if lab != "stats model" else f"finalist {split} (stats model's order)"
        labels[cid] = (lab, o)
        cands.append({"id": cid, "allocation": r["winner"]["allocation"], "order": o})
    res = FT.race(pool, cls, spec, cands, FO.RACE_FIGHTS, 3)
    for c, x in zip(cands, res):
        table[c["id"]] = row(x)
    pool_ids = list(labels) + ([before_id] if before_id else [])
    best_id = min(pool_ids, key=lambda k: table[k]["weighted"])
    if before_id and best_id == before_id:
        r["winner"] = {"allocation": before["allocation"], "split": before["split"],
                       "picked_by": "the 20-60 race (the polish's gain at levels 40-60 did not hold at 20-60)"}
        r["order"], r["order_label"] = before["order"], "stats model"
        log(f"  {cls} {spec}: the race's old pick {before['split']} stays ({table[before_id]['weighted']:.2f} s against the polished "
            f"{split} at {min(table[k]['weighted'] for k in labels):.2f})")
    else:
        r["order"], r["order_label"] = labels[best_id][1], labels[best_id][0]
        others = ", ".join(f"{labels[k][0]} {table[k]['weighted']:.2f}" for k in labels if k != best_id)
        log(f"  {cls} {spec}: order {labels[best_id][0]} ({table[best_id]['weighted']:.2f} s per kill at 20-60; {others})")
    table["open winner"] = table.pop(best_id)
    r["race"] = table
    save()


def ensure_order(cls, spec, r, pool, space, save):
    """After a certificate re-search put a new winner in with the stats model's order (fl_synergy.research), race its orders too."""
    split = space.split(FT.flat_of(r["winner"]))
    if f"finalist {split} (own tree first order)" in r["race"] and r.get("order_label"):
        return False
    pick_order(cls, spec, r, pool, space, save)
    finish(cls, spec, r, space)
    save()
    return True


def values(cls, spec, r, pool):
    w = FT.flat_of(r["winner"])
    jobs = [(cls, spec, w, 60, FO.VALUE_FIGHTS, 5)] + [(cls, spec, {k: v for k, v in w.items() if k != n}, 60, FO.VALUE_FIGHTS, 5) for n in w]
    res = pool.map(FO._ttk, jobs, chunksize=1)
    base = res[0][0]
    r["values"] = dict(sorted({n: {"ranks": w[n], "seconds": round(res[i + 1][0] - base, 2), "per_point": round((res[i + 1][0] - base) / w[n], 2)}
                               for i, n in enumerate(w)}.items(), key=lambda kv: -kv[1]["seconds"]))
    r["values_base"] = round(base, 2)


def finish(cls, spec, r, space):
    w = FT.flat_of(r["winner"])
    best = min((k for k in r["race"] if k != "open winner" and not k.startswith("finalist ")), key=lambda k: r["race"][k]["weighted"], default=None)
    r.update({"split": space.split(w), "family": space.classify(w), "link": RSH.tf_link(cls, w), "ours_best": best,
              "gain_vs_ours": round(r["race"][best]["weighted"] / r["race"]["open winner"]["weighted"] - 1, 4) if best else None})


def after_race(cls, spec, r, model, trees, pool, space, ours, save, cfg=None):
    """After the race's pick: the polish, then the order; a changed winner gets new values and loses its certificate. Returns whether
    the winner changed."""
    before = {"allocation": r["winner"]["allocation"], "order": r["order"], "split": space.split(FT.flat_of(r["winner"]))}
    moved = polish(cls, spec, r, model, pool, space, save, cfg)
    if moved:
        flat, order = moved
        r["winner"] = {"allocation": alloc_of(space, flat), "split": space.split(flat), "picked_by": "the 20-60 polish after the race"}
        r["order"] = order
    pick_order(cls, spec, r, pool, space, save, before if moved else None)
    changed = FT.flat_of(r["winner"]) != FT.flat_of(before)
    r["level_polish"]["changed"] = changed
    if changed:
        r.pop("values", None)
        r.pop("synergy", None)
        values(cls, spec, r, pool)
    finish(cls, spec, r, space)
    save()
    return changed


# ------------------------------------------------------------------------------------------------ post hoc
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--rotation", action="append")
    ap.add_argument("--fresh", action="store_true", help="polish again a rotation that has a level_polish record")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument("--smoke", action="store_true", help="tiny budgets on the open-smoke copy of the record; nothing else written")
    a = ap.parse_args()
    cls = a.cls
    cfg = dict(POLISH)
    if a.smoke:
        FO.OUT, FO.SMOKE, FO.RACE_FIGHTS, FO.VALUE_FIGHTS = HERE / "open-smoke", True, 200, 200
        cfg.update(fights=30, batch=4, rounds=1, confirm=40)
    MLT = FO._load("ml_talents_open", ROOT / "_reference/data/raidsim/ml_talents.py")
    rp = FO.OUT / f"{cls}.json"
    st = json.load(open(rp, encoding="utf-8"))

    def save():
        rp.write_text(json.dumps(st, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    log(f"=== {cls} 20-60 polish started {datetime.datetime.now():%Y-%m-%d %H:%M}; record {rp.name}")
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    space = MLT.Space(cls, "any", any_split=True)
    SYL = FO._load("fl_synergy_fo", HERE / "fl_synergy.py")
    changed_any = False
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for spec, (model, trees) in FO.rotations(cls).items():
            r = st["rotations"].get(spec)
            if not r or not r.get("done") or (a.rotation and spec not in a.rotation):
                continue
            if "level_polish" in r and not a.fresh:
                log(f"  {cls} {spec}: polished already ({r['level_polish'].get('date')}); --fresh redoes it")
                continue
            ours = our_builds(cls, model, trees, data)
            ch = after_race(cls, spec, r, model, trees, pool, space, ours, save, cfg)
            if ch and not FO.SMOKE:
                SYL.certificate(cls, spec, r, model, trees, pool, a.jobs, space, MLT, ours, argparse.Namespace(no_search=False), save)
                ensure_order(cls, spec, r, pool, space, save)   # a re-search's new winner comes with the stats model's order only
                finish(cls, spec, r, space)
                save()
            changed_any |= ch
            log(f"  {cls} {spec}: open winner {r['split']} ({r['family']}), {r['race']['open winner']['weighted']:.2f} s per kill (20-60)"
                + (f", {r['gain_vs_ours']:+.1%} faster than {r['ours_best']} ({r['race'][r['ours_best']]['weighted']:.2f} s)" if r.get("ours_best") else "")
                + (" [changed]" if ch else ""))
        if changed_any and not a.rotation and not FO.SMOKE:
            st.pop("cross", None)
            SYL.cross_rotations(cls, st, pool, save)
    if not FO.SMOKE:
        FO.write_class(cls, st)
        FO.write_page()
    log("== done")


if __name__ == "__main__":
    main()
