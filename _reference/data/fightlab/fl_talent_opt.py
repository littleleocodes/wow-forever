"""Search leveling talents directly in the fight lab: local search over a level-60 allocation, then a leveling order and a race
(2026-09-30, user request: "each spec to have a leveling, raid and PvP spec that we can best derive from everything").

    python _reference/data/fightlab/fl_talent_opt.py <class> --spec <fight-lab spec> --model <scorer model> --tree <tree>
           --start <build id | candidate .json> [--start ...] [--incumbent <build id>] [--write <candidate .json>]

1. Start: the fastest of the --start builds at level 60 (the spec's hand leveling builds and the scorer's best build with 30+ points in
   the tree), measured in the fight lab under the spec's rotation (fightlab/rotations).
2. Local search at level 60 (full allocation): the moves of raidsim/talent_opt.py (1, 2, 3 or 5 points, every validator rule, 30+
   points kept in --tree). There are hundreds of moves and the fight lab is noisy, so each round screens them: the scorer's best
   --screen moves under --model plus --explore random ones (the scorer misjudges talents the lab sees), all run with common random
   numbers (seed 1, --fights); the best --top are confirmed on seed 2 (--confirm) and one is kept when it wins there by more than
   --min-gain. Stops when nothing wins.
3. Order and race: the scorer's leveling order for the result (Optimizer.order), then the level-weighted time per kill at 20-60
   (weights level / 10, as the races) against --incumbent on a third seed. Level 60 is where the search looks; the lower levels hold
   the order's first points, which the scorer picks: the race says whether the path is also faster.

Talents the rotation needs (the spec's key spells, --keep) never go to 0. --write saves {"id", "allocation", "order", "search"}.
"""
import argparse
import datetime
import importlib.util
import json
import multiprocessing
import pathlib
import random
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data")]
import run as FR  # noqa: E402  (fightlab/run.py)
import validate_builds as VB  # noqa: E402

_spec = importlib.util.spec_from_file_location("raid_talent_opt", ROOT / "_reference/data/raidsim/talent_opt.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)   # neighbors / valid / by_tree (the raid search's move set)

LEVELS = [20, 30, 40, 50, 60]
LOOKAHEAD = {"mage": 12, "warrior": 20}


def _init(gear):
    FR.apply_gear(gear)


def _run(job):
    cls, spec, alloc, level, fights, seed = job
    try:
        return FR.simulate(cls, alloc, level, spec, fights, seed, 0)["time_per_kill"]
    except Exception as e:   # a broken candidate (a rotation that cannot kill) loses, it does not stop the search
        print(f"  error {type(e).__name__}: {e}", flush=True)
        return 1e9


def weighted(per_level):
    tot = sum(L / 10 for L in per_level)
    return sum(v * L / 10 for L, v in per_level.items()) / tot


def flat_of(b):
    return {n: r for items in b["allocation"].values() for n, r in items if r}


def load(cls, ref):
    return FR.load_build(cls, ref)


def order_of(cls, model, flat):
    from optimize import Optimizer
    opt = Optimizer("forever", cls, model, "leveling-st")
    steps = opt.order(flat, lookahead=LOOKAHEAD.get(cls, 16))
    return [{"levels": lv, "tree": t, "talent": n, "points": pts} for lv, t, n, pts in opt.compress_order(steps)]


def order_job(job):
    """(cls, model, flat) -> the stats model's leveling order, None when it fails (a pool job: fl_levels.py computes the orders of a
    batch of neighbours in parallel, about 9 s a build)."""
    cls, model, flat = job
    try:
        return order_of(cls, model, flat)
    except Exception as e:   # noqa: BLE001
        print(f"  order error {type(e).__name__}: {e}", flush=True)
        return None


def race(pool, cls, spec, builds, fights, seed):
    """Level-weighted time per kill for each {"allocation", "order"} build; returns [(weighted, {level: time})]."""
    jobs = [(cls, spec, FR.allocation_at(b, L), L, fights, seed) for b in builds for L in LEVELS]
    res = pool.map(_run, jobs, chunksize=1)
    out = []
    for i in range(len(builds)):
        per = {L: res[i * len(LEVELS) + k] for k, L in enumerate(LEVELS)}
        out.append((weighted(per), per))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True, help="fight-lab spec string (the rotation)")
    ap.add_argument("--model", required=True, help="scorer model for screening and the leveling order")
    ap.add_argument("--tree", required=True, help="the build keeps 30+ points here")
    ap.add_argument("--start", action="append", required=True)
    ap.add_argument("--incumbent", action="append", default=[], help="builds the result races at the end, the fastest counts (default: the first --start)")
    ap.add_argument("--keep", action="append", default=[])
    ap.add_argument("--fights", type=int, default=800)
    ap.add_argument("--confirm", type=int, default=3000)
    ap.add_argument("--screen", type=int, default=40)
    ap.add_argument("--explore", type=int, default=20)
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--min-gain", type=float, default=0.005)
    ap.add_argument("--rounds", type=int, default=25)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--gear", default="greens")
    ap.add_argument("--write")
    a = ap.parse_args()
    from optimize import Optimizer
    cls = a.cls
    trees = VB.load_forever()[cls]
    T.MIN_TREE.clear()
    T.MIN_TREE[a.tree] = 30
    opt = Optimizer("forever", cls, a.model, "leveling-st")
    rng = random.Random(7)
    pool = multiprocessing.Pool(a.jobs, initializer=_init, initargs=(a.gear,))

    def at60(allocs, fights, seed):
        return pool.map(_run, [(cls, a.spec, al, 60, fights, seed) for al in allocs], chunksize=1)

    starts = [(s, flat_of(load(cls, s))) for s in a.start]
    starts = [(s, f) for s, f in starts if T.valid(trees, f)]
    if not starts:
        raise SystemExit(f"no --start build is a legal 51-point build with 30+ points in {a.tree}")
    t0 = at60([f for _, f in starts], a.confirm, 1)
    best = min(range(len(starts)), key=lambda i: t0[i])
    name, cur = starts[best]
    print(f"== {cls} {a.spec} ({a.tree}): start {name} " + ", ".join(f"{s} {t:.2f}s" for (s, _), t in zip(starts, t0)), flush=True)
    protect = set(a.keep) & set(cur)
    log = []
    for rnd in range(1, a.rounds + 1):
        nb = T.neighbors(trees, cur, protect)
        if not nb:
            break
        ranked = sorted(nb, key=lambda d: -opt.score(d[1], 60))
        pick = ranked[: a.screen]
        rest = ranked[a.screen:]
        pick += rng.sample(rest, min(a.explore, len(rest)))
        res = at60([cur] + [al for _, al in pick], a.fights, 1)
        ref = res[0]
        scored = sorted(((t / ref, i) for i, t in enumerate(res[1:])), key=lambda x: x[0])
        top = [(sc, i) for sc, i in scored if sc < 1 - a.min_gain / 2][: a.top]
        if not top:
            print(f"  round {rnd}: {len(pick)} of {len(nb)} moves, none ahead on seed 1 (best {1 - scored[0][0]:+.2%}: {pick[scored[0][1]][0]})", flush=True)
            break
        conf = at60([cur] + [pick[i][1] for _, i in top], a.confirm, 2)
        sc2, sc1, i = min(((conf[k] / conf[0], sc1, i) for k, (sc1, i) in enumerate(top, start=1)), key=lambda x: x[0])
        if sc2 > 1 - a.min_gain:
            print(f"  round {rnd}: {len(pick)} of {len(nb)} moves, {len(top)} ahead on seed 1, none confirmed (best {1 - sc2:+.2%}: {pick[i][0]})", flush=True)
            break
        desc, cur = pick[i]
        log.append({"round": rnd, "move": desc, "gain_seed1": 1 - sc1, "gain_seed2": 1 - sc2})
        print(f"  round {rnd}: {desc} ({1 - sc1:+.2%} seed 1, {1 - sc2:+.2%} seed 2 faster per kill at 60)", flush=True)
    alloc = {t: [[n, r] for n, r in items.items()] for t, items in T.by_tree(trees, cur).items()}
    # the path to 60: a start build's own order when the search kept its allocation (the scorer's order is only a fallback: on the
    # Frost mage's hand draft it was 0.9% slower per kill over 20-60, 2026-09-30), else the scorer's order
    same = [load(cls, s) for s, f in starts if f == cur and load(cls, s).get("order")]
    cand = {"id": f"fl-{a.tree.lower().replace(' ', '-')}-{a.spec}", "allocation": alloc, "order": same[0]["order"] if same else order_of(cls, a.model, cur)}
    incs = [load(cls, x) for x in (a.incumbent or a.start[:1])]
    res = race(pool, cls, a.spec, incs + [cand], a.confirm, 3)
    k = min(range(len(incs)), key=lambda i: res[i][0])   # the fastest existing build is the bar (2026-09-30: not the first listed)
    inc, fin = incs[k], [res[k], res[-1]]
    gain = 1 - fin[1][0] / fin[0][0]
    print(f"  race (seed 3, levels {LEVELS}): " + ", ".join(f"{b['id']} {r[0]:.2f}s" for b, r in zip(incs, res)) + f", search {fin[1][0]:.2f}s "
          f"({gain:+.2%} faster than {inc['id']})", flush=True)
    cand["search"] = {"date": datetime.date.today().isoformat(), "spec": a.spec, "model": a.model, "tree": a.tree, "start": name,
                      "starts": {s: t for (s, _), t in zip(starts, t0)}, "moves": log, "incumbent": inc["id"],
                      "race": {"incumbent": fin[0], "search": fin[1], "gain": gain,
                               "all": {b["id"]: r for b, r in zip(incs, res[:-1])}}, "fights": a.fights, "confirm": a.confirm}
    if a.write:
        pathlib.Path(a.write).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(a.write).write_text(json.dumps(cand, indent=1) + "\n", encoding="utf-8")
        print(f"  wrote {a.write}")


if __name__ == "__main__":
    main()
