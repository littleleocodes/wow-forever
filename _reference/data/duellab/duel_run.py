"""Run duels between talent builds (duellab, 2026-11-14).

    python _reference/data/duellab/duel_run.py mage:pvp-frost warrior:arms-pvp [--n 400] [--seed 1] [--log 1] [--set KEY=VALUE]

A side is <class>:<build id> (a build in <class>/research/talents/forever/proposed-builds.json, or a .json file holding
{"allocation": {...}}). Each side plays its class's PvP layer (pvp_<class>.py, else the base layer alone) over the leveling rotation of
its build's lead tree (derive_leveling.LEVEL). Duels alternate who starts where nothing else differs, and use common random numbers:
duel i of a matchup has the same seed for every build compared, so a talent change is measured against the same dice.
"""
import argparse
import collections
import importlib
import json
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
for _p in (str(DATA / "scorer"), str(DATA), str(DATA / "fightlab"), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import duel as D  # noqa: E402
import dtables as T  # noqa: E402

AI = {"mage": ("pvp_mage", "MagePvP"), "warrior": ("pvp_warrior", "WarriorPvP"), "rogue": ("pvp_rogue", "RoguePvP"),
      "priest": ("pvp_priest", "PriestPvP"), "warlock": ("pvp_warlock", "WarlockPvP"), "hunter": ("pvp_hunter", "HunterPvP"),
      "druid": ("pvp_druid", "DruidPvP"), "paladin": ("pvp_paladin", "PaladinPvP"), "shaman": ("pvp_shaman", "ShamanPvP")}
_TREES = {}


def tree_of(cls):
    if cls not in _TREES:
        data = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        _TREES[cls] = {t["name"]: tr["name"] for tr in data["trees"] for t in tr["talents"]}
    return _TREES[cls]


def community(cls, key):
    """A community build of _reference/data/pvp-community-builds.json, decoded from its talentsforever.com link onto our talent data."""
    import popular_builds as PB
    src = json.load(open(DATA / "pvp-community-builds.json", encoding="utf-8"))
    b = next((x for x in src["builds"] if x["class"] == cls and x["key"] == key), None)
    if b is None:
        raise SystemExit(f"{cls}: no community build {key}")
    trees = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]
    return {"id": f"community:{key}", "allocation": PB.decode(cls, b["link"].split("talentsforever.com/", 1)[1], trees)}


def load_build(cls, ref):
    if ref.endswith(".json"):
        b = json.load(open(ref, encoding="utf-8"))
    elif ref.startswith("community:"):
        b = community(cls, ref.split(":", 1)[1])
    else:
        data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
        b = next((x for x in data["builds"] if x["id"] == ref), None)
        if b is None:
            raise SystemExit(f"{cls}: no build {ref}")
    alloc = b["allocation"]
    if isinstance(next(iter(alloc.values()), None), list):   # {tree: [[talent, ranks], ...]}
        alloc = {n: r for items in alloc.values() for n, r in items}
    return b.get("id", ref), alloc


def spec_for(cls, alloc):
    """The fight-lab rotation of the build's lead tree (derive_leveling.LEVEL: a healer tree plays its class's leveling rotation)."""
    import derive_leveling as DL
    pts = collections.Counter()
    for n, r in alloc.items():
        pts[tree_of(cls).get(n)] += r
    for tree, _ in pts.most_common():
        key = (cls, tree)
        if key in DL.LEVEL:
            return DL.LEVEL[key][0]
    raise SystemExit(f"{cls}: no leveling rotation for {dict(pts)}")


def make_ai(cls):
    mod, name = AI.get(cls, ("pvp_base", "PvPAI"))
    try:
        return getattr(importlib.import_module(mod), name)()
    except ModuleNotFoundError:
        return importlib.import_module("pvp_base").PvPAI()


def side(cls, alloc, spec=None):
    return (cls, alloc, spec or spec_for(cls, alloc), make_ai(cls))


def duel(a, b, seed, log=False, swap=False):
    """One duel of side tuples a, b (fresh AIs each time). swap: b is listed first (who acts first in a step)."""
    ca, aa, sa, _ = a
    cb, ab, sb, _ = b
    first, second = ((cb, ab, sb, make_ai(cb)), (ca, aa, sa, make_ai(ca))) if swap else ((ca, aa, sa, make_ai(ca)), (cb, ab, sb, make_ai(cb)))
    d = D.Duel(first, second, seed=seed, log=log)
    r = d.run()
    if swap:
        r = {"A": "B", "B": "A"}.get(r, r)
    return r, d


def matchup(a, b, n=400, seed=1):
    """{"win", "loss", "draw", "time", "hp_left"} of side a against side b over n duels (common random numbers by duel index)."""
    out = collections.Counter()
    times, left = [], []
    for i in range(n):
        r, d = duel(a, b, seed * 100_003 + i, swap=bool(i % 2))
        out[{"A": "win", "B": "loss"}.get(r, "draw")] += 1
        times.append(d.t)
        me = d.b if i % 2 else d.a
        left.append(max(0.0, me.p.hp) / me.p.hp_max)
    return {"win": out["win"] / n, "loss": out["loss"] / n, "draw": out["draw"] / n, "time": statistics.mean(times),
            "hp_left": statistics.mean(left), "n": n}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--log", type=int, default=0, help="print the log of this many duels")
    ap.add_argument("--set", action="append", default=[], help="dtables KEY=VALUE")
    args = ap.parse_args()
    for pair in args.set:
        k, v = pair.split("=", 1)
        setattr(T, k, type(getattr(T, k))(v) if not isinstance(getattr(T, k), bool) else v.lower() in ("1", "true", "yes"))
    sides = []
    for ref in (args.a, args.b):
        cls, bid = ref.split(":", 1)
        name, alloc = load_build(cls, bid)
        sides.append(side(cls, alloc))
        print(f"{ref}: {cls}, rotation {sides[-1][2]}, {sum(alloc.values())} points")
    for i in range(args.log):
        r, d = duel(sides[0], sides[1], args.seed * 100_003 + i, log=True, swap=bool(i % 2))
        print(f"\n--- duel {i}: {'swapped, ' if i % 2 else ''}result {r} at {d.t:.1f}s")
        print("\n".join(d.log))
    m = matchup(sides[0], sides[1], args.n, args.seed)
    print(f"\n{args.a} vs {args.b}: wins {m['win']:.1%}, losses {m['loss']:.1%}, draws {m['draw']:.1%}, "
          f"{m['time']:.1f}s per duel, {m['hp_left']:.0%} health left on average ({m['n']} duels)")


if __name__ == "__main__":
    main()
