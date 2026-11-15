"""PvP talent values and build search on the duel lab (2026-11-14).

    python _reference/data/duellab/pvp_search.py values <class>:<build> [--n 100]
    python _reference/data/duellab/pvp_search.py search <class>:<build> [<class>:<build> ...] --tree "Frost" [--steps 20] [--write]

A build's PvP score J = mean win rate against the field (pvp_field.FIELD: one reference build per class) + 0.25 x mean health margin
(own share left minus the foe's), so a matchup stuck at 0% or 100% still says which build is closer to turning it.

values: each talent of the build removed (its points left unspent, the synergy certificate's "unpaid" measure), scored on the same
duels (common random numbers): what the talent is worth in PvP against this field.

search: local search from the given builds over legal moves (raidsim/talent_opt.neighbors: 1, 2, 3, 5 points and prerequisite
chains; 30+ points kept in --tree). Each step screens a random batch of neighbours on seed 1 with --n-screen duels a matchup, and
keeps the best only if it beats the current build on seed 2 with --n-confirm duels by --bar. Records go to
_reference/data/duellab/search/<class>-<tree slug>.json. A model of stated assumptions (duel.py), not a measurement; a talent whose
effect the duel lab does not model reads as worth nothing here.
"""
import argparse
import concurrent.futures as CF
import datetime
import importlib.util
import json
import os
import pathlib
import random
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path.insert(0, str(HERE))
import duel_run as DR  # noqa: E402
import pvp_field as PF  # noqa: E402

MARGIN_W = 0.25
_TO = {}


def talent_opt():
    if "m" not in _TO:
        sys.path.insert(0, str(DATA))
        import validate_builds as VB
        spec = importlib.util.spec_from_file_location("raid_talent_opt", DATA / "raidsim" / "talent_opt.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _TO["m"], _TO["VB"] = m, VB
    return _TO["m"], _TO["VB"]


def matchup(args):
    """(label, opponent class) -> (win, draw, margin) of an allocation against one field opponent."""
    label, cls, alloc, fcls, fref, n, seed = args
    a = DR.side(cls, alloc)
    b = DR.side(fcls, DR.load_build(fcls, fref)[1])
    wins = draws = 0
    margins = []
    for i in range(n):
        r, d = DR.duel(a, b, seed * 100_003 + i, swap=bool(i % 2))
        me, foe = (d.b, d.a) if i % 2 else (d.a, d.b)
        wins += r == "A"
        draws += r == "draw"
        margins.append(max(0.0, me.p.hp) / me.p.hp_max - max(0.0, foe.p.hp) / foe.p.hp_max)
    return (label, fcls), (wins / n, draws / n, statistics.mean(margins))


def evaluate(cands, n, seed, workers=None, pool=None):
    """cands: [(label, class, allocation)] -> {label: {"by", "win", "margin", "J"}}, every candidate against the whole field."""
    jobs = [(lb, c, al, fc, fr, n, seed) for lb, c, al in cands for fc, fr in PF.FIELD]
    own = pool is None
    ex = pool or CF.ProcessPoolExecutor(max_workers=workers or max(1, (os.cpu_count() or 2) - 1))
    try:
        res = dict(ex.map(matchup, jobs, chunksize=max(1, len(jobs) // (4 * (workers or os.cpu_count() or 2)))))
    finally:
        if own:
            ex.shutdown()
    out = {}
    for lb, c, al in cands:
        by = {fc: res[(lb, fc)] for fc, _ in PF.FIELD}
        win = statistics.mean(v[0] for v in by.values())
        mg = statistics.mean(v[2] for v in by.values())
        out[lb] = {"by": by, "win": win, "margin": mg, "J": win + MARGIN_W * mg}
    return out


def values(cls, ref, n=100, seed=1, workers=None):
    name, alloc = DR.load_build(cls, ref)
    cands = [("build", cls, alloc)] + [(t, cls, {k: v for k, v in alloc.items() if k != t}) for t in alloc]
    res = evaluate(cands, n, seed, workers)
    base = res["build"]
    rows = sorted(((t, alloc[t], base["J"] - res[t]["J"], base["win"] - res[t]["win"]) for t in alloc), key=lambda x: -x[2])
    return base, rows


def tree_points(trees, flat, tree):
    return sum(flat.get(n, 0) for n in trees[tree]["talents"])


def search(cls, refs, tree, steps=20, batch=48, n_screen=40, n_confirm=120, bar=0.005, seed=1, workers=None, log=print):
    TO, VB = talent_opt()
    trees = VB.load_forever()[cls]
    TO.MIN_TREE.clear()
    TO.MIN_TREE[tree] = 30
    rng = random.Random(seed)
    starts = []
    for ref in refs:
        name, alloc = DR.load_build(cls, ref)
        if tree_points(trees, alloc, tree) >= 30 and TO.valid(trees, alloc):
            starts.append((ref, alloc))
        else:
            log(f"  start {ref} skipped: {tree_points(trees, alloc, tree)} points in {tree} or not legal")
    if not starts:
        raise SystemExit(f"{cls}: no legal start with 30+ points in {tree}")
    hist = []
    with CF.ProcessPoolExecutor(max_workers=workers or max(1, (os.cpu_count() or 2) - 1)) as pool:
        res = evaluate([(r, cls, a) for r, a in starts], n_confirm, seed + 1, pool=pool)
        ref0, cur = max(starts, key=lambda s: res[s[0]]["J"])
        cur_j = res[ref0]["J"]
        log(f"  starts: " + ", ".join(f"{r} J {res[r]['J']:.3f} (win {res[r]['win']:.1%})" for r, _ in starts) + f"; from {ref0}")
        hist.append({"step": 0, "from": ref0, "J": round(cur_j, 4), "win": round(res[ref0]["win"], 4), "alloc": cur})
        for step in range(1, steps + 1):
            nb = TO.neighbors(trees, cur)
            rng.shuffle(nb)
            nb = nb[:batch]
            if not nb:
                break
            scr = evaluate([(f"n{i}", cls, al) for i, (desc, al) in enumerate(nb)] + [("cur", cls, cur)], n_screen, seed, pool=pool)
            best = max(range(len(nb)), key=lambda i: scr[f"n{i}"]["J"])
            gain = scr[f"n{best}"]["J"] - scr["cur"]["J"]
            if gain <= bar:
                log(f"  step {step}: no neighbour of {len(nb)} gains (best {gain:+.3f}: {nb[best][0]})")
                if len(TO.neighbors(trees, cur)) <= batch:
                    break
                continue
            conf = evaluate([("new", cls, nb[best][1]), ("cur", cls, cur)], n_confirm, seed + 1, pool=pool)
            g2 = conf["new"]["J"] - conf["cur"]["J"]
            if g2 > bar:
                cur, cur_j = nb[best][1], conf["new"]["J"]
                hist.append({"step": step, "move": nb[best][0], "J": round(cur_j, 4), "win": round(conf["new"]["win"], 4), "gain": round(g2, 4)})
                log(f"  step {step}: {nb[best][0]}: J {cur_j:.3f} (+{g2:.3f} confirmed), win {conf['new']['win']:.1%}")
            else:
                log(f"  step {step}: {nb[best][0]} +{gain:.3f} on screening, {g2:+.3f} on seed {seed + 1}: not kept")
        final = evaluate([("final", cls, cur)], n_confirm * 2, seed + 2, pool=pool)["final"]
    return {"class": cls, "tree": tree, "starts": [r for r, _ in starts], "history": hist, "final": cur, "J": round(final["J"], 4),
            "win": round(final["win"], 4), "margin": round(final["margin"], 4),
            "by": {k: [round(x, 4) for x in v] for k, v in final["by"].items()},
            "settings": {"steps": steps, "batch": batch, "n_screen": n_screen, "n_confirm": n_confirm, "bar": bar, "seed": seed,
                         "margin_weight": MARGIN_W, "field": PF.FIELD}, "date": datetime.date.today().isoformat()}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=("values", "search"))
    ap.add_argument("builds", nargs="+")
    ap.add_argument("--tree")
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--batch", type=int, default=48)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--workers", type=int)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    if a.mode == "values":
        for x in a.builds:
            cls, ref = x.split(":", 1)
            base, rows = values(cls, ref, a.n, a.seed, a.workers)
            print(f"{x}: J {base['J']:.3f}, field win {base['win']:.1%}, margin {base['margin']:+.2f}")
            for t, r, dj, dw in rows:
                print(f"  {t} ({r}): {dj:+.3f} J, {dw:+.1%} win")
        return
    cls = a.builds[0].split(":", 1)[0]
    refs = [x.split(":", 1)[1] for x in a.builds]
    rec = search(cls, refs, a.tree, a.steps, a.batch, seed=a.seed, workers=a.workers)
    print(f"final: J {rec['J']:.3f}, win {rec['win']:.1%}; {json.dumps(rec['final'])}")
    if a.write:
        out = HERE / "search"
        out.mkdir(exist_ok=True)
        (out / f"{cls}-{a.tree.lower().replace(' ', '-')}.json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
