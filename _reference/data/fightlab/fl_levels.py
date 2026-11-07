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
import re
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
ORDER = dict(levels=(30, 40, 50), fights=150, batch=30, rounds=6, min_gain=0.003, confirm=400)   # the order polish: level 60 is the same for every order
log = FO.log


def sig_order(cls, rot, build):
    """A build's order with its spec's signature talents at the earliest level their tree allows (fl_signature.sig_order; user
    decision 2026-11-06, page-audit K5). Every order this module races or polishes goes through it."""
    return FO.FS.sig_order(cls, rot, build)


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
    # each level is judged as a level of the build's path (fl_open_search._ttk's 8th element, 2026-11-06), not as a build of its own
    jobs = [(cls, spec, FR.allocation_at(b, L), L, fights, seed, True, (FT.flat_of(b), b["order"])) for b in builds for L in levels]
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
    cur_b["order"] = sig_order(cls, spec, cur_b)   # the reference plays by the neighbours' rule (a record from before 2026-11-06 may
    rng = random.Random(97)                        # hold an order with a late signature talent, which the objective penalizes)
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
        for c in cands:   # 2026-11-06 (page-audit K5): each neighbour's order with its signature talents as early as the tree allows
            c["order"] = sig_order(cls, spec, c)
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


def pick_order(cls, spec, r, pool, space, save, before=None, model=None):
    """Race the winner's orders at levels 20-60 on the race's seed and fights: the stats model's (`order_stats`, computed from the model
    when the record has none for this build), own tree first, own tree last, the current order when it is none of those (a polished one
    from an earlier run) and, after a build polish, the race's old pick; the fastest row becomes "open winner" (the old pick wins back
    when it is faster: the 20-60 race decides)."""
    w = FT.flat_of(r["winner"])
    split = space.split(w)
    if r.get("order_stats_split") != split or not r.get("order_stats"):
        r["order_stats"] = FT.order_of(cls, model, w) if model else r["order"]
        r["order_stats_split"] = split
    stats = r["order_stats"]
    lead = max(space.tree_names, key=lambda t: sum(w.get(n, 0) for n in space.by_tree[t]))
    pts = expand(stats)
    variants = [("stats model", stats),
                ("own tree first", compress([x for x in pts if x[0] == lead] + [x for x in pts if x[0] != lead])),
                ("own tree last", compress([x for x in pts if x[0] != lead] + [x for x in pts if x[0] == lead]))]
    cur_lab = r.get("order_label") or "stats model"
    # 2026-11-06 (user decision on page-audit K5): every order raced takes the spec's signature talents as early as their tree allows
    # (fl_signature.sig_order: the Assassination page had taken Mutilate at 60, own tree last). Two variants the rule makes equal race once.
    sig = lambda o: sig_order(cls, spec, {"allocation": r["winner"]["allocation"], "order": o})   # noqa: E731
    firsts, uniq = [], []
    for lab, o in variants:
        o2 = sig(o)
        if o2 != o:
            firsts.append(lab)
        if o2 not in [x for _, x in uniq]:
            uniq.append((lab, o2))
    variants = uniq
    cur = sig(r["order"])
    if cur != r["order"] or firsts:
        r["order_signature_first"] = {"date": FO.TODAY, "moved_in": firsts + ([cur_lab + " (the record's)"] if cur != r["order"] else [])}
        log(f"  {cls} {spec}: signature talents moved to the earliest level their tree allows in the "
            + ", ".join(r["order_signature_first"]["moved_in"]) + " order" + ("s" if len(r["order_signature_first"]["moved_in"]) > 1 else ""))
    if cur not in [o for _, o in variants]:   # a polished order from an earlier run competes under its own label
        variants.append((cur_lab, cur))
    table = r["race"]
    before_id = None
    if before:
        before_id = f"finalist {before['split']} (before the 20-60 polish)"
        table[before_id] = table.pop("open winner")
    elif cur != r["order"]:   # the record's row was raced with the signature talents late: kept under its own name, never a pick
        table[f"finalist {split} ({cur_lab} order, signature talents late)"] = table["open winner"]
    else:
        table[f"finalist {split} ({cur_lab} order)"] = table["open winner"]
    labels, cands = {}, []
    for lab, o in variants:
        cid = f"finalist {split} ({lab} order)"
        labels[cid] = (lab, o)
        cands.append({"id": cid, "allocation": r["winner"]["allocation"], "order": o})
    res = FT.race(pool, cls, spec, cands, FO.RACE_FIGHTS, 3)
    for c, x in zip(cands, res):
        table[c["id"]] = row(x)
    pool_ids = list(labels) + ([before_id] if before_id else [])
    if before_id:   # 2026-10-26 audit: the old pick won back on plain time (Survival 10/11/30 at a 49.5% melee share against a polished
        new_id = min(labels, key=lambda k: table[k]["weighted"])   # build that passes); it does only when it plays its spec too
        (ok_old, _), (ok_new, _) = FO.FS.qualifying(pool, cls, spec, [before, {"allocation": r["winner"]["allocation"], "order": labels[new_id][1]}])
        if ok_new and not ok_old:
            pool_ids.remove(before_id)
            log(f"  {cls} {spec}: the race's old pick {before['split']} fails its signature check and the polished build passes: no win back")
    best_id = min(pool_ids, key=lambda k: table[k]["weighted"])
    if before_id and best_id == before_id:
        r["winner"] = {"allocation": before["allocation"], "split": before["split"],
                       "picked_by": "the 20-60 race (the polish's gain at levels 40-60 did not hold at 20-60)"}
        r["order"], r["order_label"] = before["order"], before.get("order_label", "stats model")
        r["order_stats"], r["order_stats_split"] = before.get("order_stats", before["order"]), before["split"]
        log(f"  {cls} {spec}: the race's old pick {before['split']} stays ({table[before_id]['weighted']:.2f} s against the polished "
            f"{split} at {min(table[k]['weighted'] for k in labels):.2f})")
    else:
        r["order"], r["order_label"] = labels[best_id][1], labels[best_id][0]
        others = ", ".join(f"{labels[k][0]} {table[k]['weighted']:.2f}" for k in labels if k != best_id)
        log(f"  {cls} {spec}: order {labels[best_id][0]} ({table[best_id]['weighted']:.2f} s per kill at 20-60; {others})")
    table["open winner"] = table.pop(best_id)
    r["race"] = table
    r["orders_raced"] = split   # ensure_order's test: the orders of this build were raced (the chosen one's row is "open winner")
    save()


def ensure_order(cls, spec, r, pool, space, save, model=None):
    """After a certificate re-search put a new winner in with the stats model's order (fl_synergy.research), race its orders too."""
    split = space.split(FT.flat_of(r["winner"]))
    if r.get("orders_raced") == split and r.get("order_label"):   # (the chosen order's own row moves under "open winner": a key test failed)
        return False
    r["order_stats"], r["order_stats_split"] = r["order"], split   # the re-search gave the new winner the stats model's order
    choose_order(cls, spec, r, pool, space, save, None, None, model)
    finish(cls, spec, r, space)
    save()
    return True


def legal_order(space, pts, total):
    """Every prefix of a per-point order is a legal partial build (rank caps, tier gating, prerequisites) and it spends every point."""
    alloc = {}
    for _, name in pts:
        alloc[name] = alloc.get(name, 0) + 1
        if not space.ok_partial(alloc):
            return False
    return len(pts) == total


def order_moves(order, rng, n, space, levels=(30, 40, 50), ok=None):
    """Up to n random legal orders one block move away from `order`: a talent's block, or a part of it, moved up to three blocks
    earlier or later (the first ranks of a talent are worth more than the last: a split lets them come early and the rest late).
    Only moves that change the build at one of `levels` count: the race looks at levels 20-60 in steps of ten, so a move inside one
    decade changes nothing it can see (26 of 30 random moves in a first test). `ok(order)` (2026-11-06): only moves it accepts, the
    orders that still take the signature talents as early as their tree allows."""
    blocks = [(s["tree"], s["talent"], s["points"]) for s in order]
    total = sum(p for _, _, p in blocks)
    cur_key = tuple((t, nm) for t, nm, p in blocks for _ in range(p))
    base_at = {L: FR.allocation_at({"order": order}, L) for L in levels}
    seen = {cur_key}
    out, tries = [], 0
    while len(out) < n and tries < n * 30:
        tries += 1
        i = rng.randrange(len(blocks))
        t, name, p = blocks[i]
        d = rng.choice([-3, -2, -1, 1, 2, 3])
        b = list(blocks)
        if p == 1 or rng.random() < 0.5:   # the whole block
            blk = b.pop(i)
            j = i + d
            if j < 0 or j > len(b):
                continue
            b.insert(j, blk)
        else:   # part of it: the last k points move later, the first k earlier
            k = rng.randrange(1, p)
            b[i] = (t, name, p - k)
            j = i + d + (1 if d > 0 else 0)
            if j < 0 or j > len(b):
                continue
            b.insert(j, (t, name, k))
        pts = [(tt, nn) for tt, nn, pp in b for _ in range(pp)]
        key = tuple(pts)
        if key in seen:
            continue
        seen.add(key)
        cand = compress(pts)
        if all(FR.allocation_at({"order": cand}, L) == base_at[L] for L in levels) or not legal_order(space, pts, total):
            continue
        if ok is not None and not ok(cand):
            continue
        out.append(cand)
    return out


def order_diff(a, b):
    """'Talent: levels -> levels' for the talents whose levels changed (the first three)."""
    la = {}
    for s in a:
        la.setdefault(s["talent"], []).append(s["levels"])
    lb = {}
    for s in b:
        lb.setdefault(s["talent"], []).append(s["levels"])
    ch = [f"{n}: {'/'.join(la.get(n, ['-']))} -> {'/'.join(lb.get(n, ['-']))}" for n in lb if la.get(n) != lb.get(n)]
    return "; ".join(ch[:3]) + (f" (+{len(ch) - 3} more)" if len(ch) > 3 else "")


def order_polish(cls, spec, r, pool, space, save, cfg=None):
    """Hill climb over the winner's order (block moves) on the weighted time per kill at levels 30-50; returns the order when it moved."""
    cfg = cfg or ORDER
    lv = list(cfg["levels"])
    alloc = r["winner"]["allocation"]
    cur = r["order"]
    rng = random.Random(53)
    steps, t0 = [], time.time()
    log(f"== {cls} {spec}: order polish of the {r.get('order_label', 'stats model')} order (levels {', '.join(map(str, lv))}, batches of "
        f"{cfg['batch']} block moves, {cfg['fights']} fights, kept at {cfg['min_gain']:.1%} on a second seed)")
    for rnd in range(1, cfg["rounds"] + 1):
        cands = order_moves(cur, rng, cfg["batch"], space, lv, ok=lambda o: FO.FS.order_ok(cls, spec, {"allocation": alloc, "order": o}))
        if not cands:
            log(f"    round {rnd}: no legal block move left")
            break
        sc = evaluate(pool, cls, spec, [{"allocation": alloc, "order": o} for o in [cur] + cands], lv, cfg["fights"], 13)
        ref, sc = sc[0], sc[1:]
        bi = min(range(len(cands)), key=lambda i: sc[i])
        if sc[bi] > ref * (1 - cfg["min_gain"]):
            log(f"    round {rnd}: {len(cands)} orders, none {cfg['min_gain']:.1%} faster at levels 30-50 (best {sc[bi] / ref - 1:+.2%})")
            break
        c2 = evaluate(pool, cls, spec, [{"allocation": alloc, "order": o} for o in (cur, cands[bi])], lv, cfg["confirm"], 14)
        desc = order_diff(cur, cands[bi])
        if c2[1] > c2[0] * (1 - cfg["min_gain"]):
            log(f"    round {rnd}: {desc}: {sc[bi] / ref - 1:+.2%} on seed 13, {c2[1] / c2[0] - 1:+.2%} on seed 14: not confirmed")
            continue
        steps.append({"round": rnd, "change": desc, "seed1": round(sc[bi] / ref - 1, 4), "seed2": round(c2[1] / c2[0] - 1, 4),
                      "seconds_30_50": round(c2[1], 2)})
        log(f"    round {rnd}: {desc}: {steps[-1]['seed1']:+.2%} on seed 13, {steps[-1]['seed2']:+.2%} on seed 14 ({c2[0]:.2f} -> {c2[1]:.2f} s): kept")
        cur = cands[bi]
    r["order_polish"] = {"date": FO.TODAY, "levels": lv, "from": r.get("order_label", "stats model"), "steps": steps,
                         "minutes": round((time.time() - t0) / 60, 1), "changed": bool(steps)}
    save()
    return cur if steps else None


def choose_order(cls, spec, r, pool, space, save, before=None, cfg=None, model=None):
    """The three orders raced (pick_order), then the order polish; a polished order becomes the page's when it is faster at 20-60."""
    pick_order(cls, spec, r, pool, space, save, before, model)
    o = order_polish(cls, spec, r, pool, space, save, cfg)
    if not o:
        return
    split = space.split(FT.flat_of(r["winner"]))
    res = FT.race(pool, cls, spec, [{"id": "x", "allocation": r["winner"]["allocation"], "order": o}], FO.RACE_FIGHTS, 3)[0]
    table = r["race"]
    label = r.get("order_label", "stats model")
    if res[0] < table["open winner"]["weighted"]:
        table[f"finalist {split} ({label} order, before the order polish)"] = table["open winner"]
        table["open winner"] = row(res)
        base = re.sub(r"^(?:polished from the )+(.*?)(?: order)+$", r"\1", label)   # 2026-10-15: a second polish nested the label
        r["order"], r["order_label"] = o, f"polished from the {base} order"
        log(f"  {cls} {spec}: the polished order is the page's ({res[0]:.2f} s per kill at 20-60, was {table[f'finalist {split} ({label} order, before the order polish)']['weighted']:.2f})")
    else:
        table[f"finalist {split} (polished order)"] = row(res)
        log(f"  {cls} {spec}: the polished order did not hold at 20-60 ({res[0]:.2f} against {table['open winner']['weighted']:.2f}): the {label} order stays")
    save()


def values(cls, spec, r, pool):
    w = FT.flat_of(r["winner"])
    jobs = [(cls, spec, w, 60, FO.VALUE_FIGHTS, 5, False)] + [(cls, spec, {k: v for k, v in w.items() if k != n}, 60, FO.VALUE_FIGHTS, 5, False) for n in w]
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


def after_race(cls, spec, r, model, trees, pool, space, ours, save, cfg=None, ocfg=None):
    """After the race's pick: the polish, then the order (three orders raced, the order polish); a changed winner gets new values and
    loses its certificate. Returns whether the winner changed."""
    split0 = space.split(FT.flat_of(r["winner"]))
    if r.get("order_stats_split") != split0:   # the race's pick carries the stats model's order
        r["order_stats"], r["order_stats_split"] = r["order"], split0
    before = {"allocation": r["winner"]["allocation"], "order": r["order"], "split": split0, "order_label": r.get("order_label", "stats model"),
              "order_stats": r["order_stats"]}
    moved = polish(cls, spec, r, model, pool, space, save, cfg)
    if moved:
        flat, order = moved
        r["winner"] = {"allocation": alloc_of(space, flat), "split": space.split(flat), "picked_by": "the 20-60 polish after the race"}
        r["order"] = order
        r["order_stats"], r["order_stats_split"] = order, space.split(flat)   # order_job gave the polished build the stats model's order
    choose_order(cls, spec, r, pool, space, save, before if moved else None, ocfg, model)
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
    ap.add_argument("--orders", action="store_true", help="only the order choice and order polish of each done rotation (the build stays)")
    a = ap.parse_args()
    cls = a.cls
    cfg, ocfg = dict(POLISH), dict(ORDER)
    if a.smoke:
        FO.OUT, FO.SMOKE, FO.RACE_FIGHTS, FO.VALUE_FIGHTS = HERE / "open-smoke", True, 200, 200
        cfg.update(fights=30, batch=4, rounds=1, confirm=40)
        ocfg.update(fights=30, batch=4, rounds=1, confirm=40)
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
            FO.FS.leveling_space(space, cls, spec)   # (2026-10-22) the rotation's own specs, signature talents kept; the polish's
                                                     # objective (fl_open_search._ttk) penalizes builds that do not play them
            if a.orders:   # the order only: the three orders raced and the order polish, on the current winner
                if "order_polish" in r and not a.fresh:
                    log(f"  {cls} {spec}: order polished already ({r['order_polish'].get('date')}); --fresh redoes it")
                    continue
                before_order = r["order"]
                choose_order(cls, spec, r, pool, space, save, None, ocfg, model)
                finish(cls, spec, r, space)
                FO.set_signature(pool, cls, spec, r)
                save()
                changed_any |= r["order"] != before_order
                log(f"  {cls} {spec}: open winner {r['split']} ({r['family']}), {r['race']['open winner']['weighted']:.2f} s per kill (20-60), "
                    f"order {r.get('order_label')}" + (" [order changed]" if r["order"] != before_order else ""))
                continue
            if "level_polish" in r and not a.fresh:
                log(f"  {cls} {spec}: polished already ({r['level_polish'].get('date')}); --fresh redoes it")
                continue
            ours = our_builds(cls, model, trees, data)
            ch = after_race(cls, spec, r, model, trees, pool, space, ours, save, cfg, ocfg)
            if ch and not FO.SMOKE:
                SYL.certificate(cls, spec, r, model, trees, pool, a.jobs, space, MLT, ours, argparse.Namespace(no_search=False), save)
                ensure_order(cls, spec, r, pool, space, save)   # a re-search's new winner comes with the stats model's order only
                finish(cls, spec, r, space)
                save()
            FO.set_signature(pool, cls, spec, r)
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
