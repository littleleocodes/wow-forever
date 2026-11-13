"""Typical Forever leveling gear for every leveling page pick, level by level (2026-11-13, the gear add-on).

    python -u _reference/data/characters/forever_base.py [classes] [--jobs 10]   -> characters/weights/forever-base.json

The fight lab's standard leveling gear (fightlab/gear_stats.py) comes from the Classic 1.12 item database and leaves out random-suffix
world-drop greens ("of Frozen Wrath"), the items that carry most of a Forever caster's Spell Power: a mage at 30 has 0 Spell Power in
it, Arcea at 30 had 77 (her armory statistics, 2026-11-12). With Arcea-like Spell Power the Arcane-Frost build kills 25% faster at 30
and a point of Spell Power is worth a third less (scratchpad test, 2026-11-13), so values measured on the standard gear are off.
This builds the same model from Forever's own items (the simulator's item database, every suffix version: pawn_compare.item_pool):
at level L every slot holds the typical good pick among the green items the class can wear with a required level from L-6 to L-1 (the
standard gear's window, GEAR_LAG 4), "typical good pick" = each base item at the suffix such a player keeps (the top quarter of its versions by the build's own stat values,
weights/leveling/), then the median of the better half (gear_stats.py's rule); rings two different items; the weapon setup the build plays (two-hander,
main hand and off hand or shield or held item, wand or ranged); no trinkets (the standard gear has none). The record holds each
level's set and GEAR_BONUS that turns the standard gear into it (pawn_compare.bonus_of), without hit and expertise (the add-on applies
those against the cap with the character's own hit; stat_weights.py measures their value under the cap).
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA / "fightlab"), str(DATA / "scorer"), str(DATA)]
RECORD = HERE / "weights" / "forever-base.json"
LEVELS = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
CLASSES = "druid hunter mage paladin priest rogue shaman warlock warrior".split()


def kept_versions(lst, score):
    """One version per base item: the suffix a player of this build keeps when one drops, the version at the top quarter of the item's
    own versions by `score` (2026-11-13: with every version in the list, the better half's median was a suffix no such player wears:
    a Protection warrior's typical set at 40 carried 44 Intellect)."""
    by = {}
    for x in lst:
        by.setdefault(x["id"].split(":")[0], []).append(x)
    out = []
    for vs in by.values():
        vs = sorted(vs, key=score, reverse=True)
        out.append(vs[len(vs) // 4])
    return out


def typical_pick(lst, score, n=1, avoid=()):
    """The median of the better half by `score`, `n` different items (rings), each base item once (kept_versions)."""
    lst = sorted((x for x in kept_versions(lst, score) if x["id"].split(":")[0] not in avoid), key=score, reverse=True)
    half = lst[:max(1, (len(lst) + 1) // 2)]
    out, seen = [], set(avoid)
    i = len(half) // 2
    order = half[i:] + half[:i][::-1]   # the median, then the next ones down, then up
    for x in order:
        b = x["id"].split(":")[0]
        if b in seen:
            continue
        out.append(x)
        seen.add(b)
        if len(out) == n:
            break
    return out


def one(job):
    cls, bid, alloc, level, rot = job
    import addon_values as AV
    import pawn_compare as PC
    share = AV.school_shares(cls, alloc, level, rot) or {}
    pool = [x for x in PC.item_pool(cls, level, share) if x["quality"] == 2 and level - 6 <= x["req"] <= level - 1]
    setup = PC.setup_of(cls, alloc, level, rot)
    by = PC.candidates(pool, setup, cls)
    by.pop("trinket", None)
    vals = PC.our_values(cls, bid, level)
    score = lambda it: PC.our_item_value(vals, it, setup) + vals.get("hit_rating", 0) * it["lab"].get("hit", 0) * 0.5   # noqa: E731
    s = {}
    for slot in PC.ARMOR_SLOTS:
        b = typical_pick(by.get(slot, []), score)
        if b:
            s[slot] = b[0]
    for k, x in enumerate(typical_pick(by.get("finger", []), score, 2)):
        s[f"finger{k + 1}"] = x
    r = typical_pick(by.get("ranged", []), score)
    if r:
        s["ranged"] = r[0]
    two, mh = typical_pick(by.get("2h", []), score), typical_pick(by.get("mh", []), score)
    oh = typical_pick(by.get("oh", []), score, avoid={mh[0]["id"].split(":")[0]} if mh else ())
    pair = (score(mh[0]) if mh else 0) + (score(oh[0]) if oh else 0)
    if two and (setup.get("two_hand") or (not (setup.get("dual") or setup.get("shield")) and score(two[0]) >= pair)):
        s["weapon"] = two[0]
    else:
        if mh:
            s["weapon"] = mh[0]
        if oh:
            s["offhand"] = oh[0]
    typ = PC.typical_gear(cls, alloc, level, rot)
    bonus = {k: round(v, 1) for k, v in PC.bonus_of(s, typ, level, setup).items() if k not in ("hit_rating", "expertise_rating")}
    tot = {k: round(v, 1) for k, v in PC.totals(s).items()}
    # the best set the level offers (greens and blues with a required level from L-6 to L, every suffix, trinkets included): the
    # Pawn comparison's "ours" (pawn_compare.choose with our values and the caps), the high end of the add-on's gear points
    full = PC.candidates(PC.item_pool(cls, level, share), setup, cls)
    best = PC.choose(full, score, PC.our_set_score(vals, setup), setup)
    bb = {k: round(v, 1) for k, v in PC.bonus_of(best, typ, level, setup).items() if k not in ("hit_rating", "expertise_rating")}
    return (cls, bid, level), {"set": {k: x["name"] for k, x in sorted(s.items())}, "totals": tot, "standard": {k: round(v, 1) for k, v in typ.items()},
                               "bonus": bonus, "pool": len(pool),
                               "best": {"set": {k: x["name"] for k, x in sorted(best.items())},
                                        "totals": {k: round(v, 1) for k, v in PC.totals(best).items()}, "bonus": bb}}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*", default=CLASSES)
    ap.add_argument("--jobs", type=int, default=10)
    a = ap.parse_args()
    import level_guides as LG
    import run as FR
    SA = LG.fightlab_signature_audit()
    jobs = []
    for cls in a.classes:
        for slot in SA.page_slots(cls):
            if not slot[1]:
                continue
            spec, b = slot[0], slot[1][0]
            _, order, _, rot = LG.pick(cls, spec)
            for L in LEVELS:
                jobs.append((cls, b["id"], FR.allocation_at({"allocation": b["allocation"], "order": order}, L), L, rot))
    import fl_talent_opt as FT
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        res = pool.map(one, jobs, chunksize=1)
    rec = json.loads(RECORD.read_text(encoding="utf-8")) if RECORD.exists() else {"builds": {}}
    rec.update(date=datetime.date.today().isoformat(), levels=LEVELS, note=__doc__.split("\n\n")[1].replace("\n", " "))
    for (cls, bid, L), row in res:
        rec["builds"].setdefault(f"{cls}-{bid}", {})[str(L)] = row
    RECORD.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8", newline="\n")
    for (cls, bid, L), row in res:
        if L in (20, 30, 40, 60):
            t = row["totals"]
            print(f"{cls:8s} {bid[:34]:34s} {L:2d}: " + ", ".join(f"{k} {v:g}" for k, v in sorted(row["bonus"].items())), flush=True)
    print(f"wrote {RECORD}")


if __name__ == "__main__":
    main()
