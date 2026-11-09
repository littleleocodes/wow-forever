"""Leveling filler pass (2026-11-08, user: "the resto druid talent spec says to take Improved Wrath. Why would that ever be a thing?
Theres not a single other better place to spend that talent? Check thinks like that constantly"; page-audit-1108 S14).

A leveling page's build can spend points on talents that do nothing in its rotation: an old hand draft the open search's polish never
touched (the Retribution pick, 2026-09-26: Vindication 3, Purifying Power 2, Sacred Duty while Improved Seals sits at 3/5), or a gate
filled with a talent nobody presses. For the spec page's pick (level_guides.pick: its build, order and rotation):

1. every talent's value at level 60 by removal (one rank less; common random numbers);
2. the zero points: a removal that costs less than the noise floor, removable while every prefix of the order stays a legal build;
3. every move of a zero point (its last rank in the order) to any other talent at the same level, legal along the whole order, raced at
   the levels from that point on (20-60 by fives, weighted level / 10 as every leveling race) on seed 3; the best that gains --bar
   (0.3%, fl_levels' bar) is checked on seed 4 and kept when it holds there, then the pass starts over;
4. else a tie-break (the best of the top moves that is faster on both seeds), else a "no loss" move (2026-11-09: one that costs at most
   NO_LOSS, 0.1%, on each seed), always into a talent that is not itself a zero point: a point that does nothing never stays.

    python _reference/data/fightlab/fl_filler_pass.py <class> --spec "<Spec>" [--fights 1500] [--jobs 10] [--write]

Record `fightlab/filler/<class>-<spec slug>.json`; `--write` applies the kept moves to the build and its order in proposed-builds.json
with a note. Then: `level_guides.py <class> --measure`, regenerate the pages. Fight-lab numbers are a model of the beta.
"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data"), str(ROOT / "_reference/data/raidsim")]
import fl_levels as FL  # noqa: E402
import fl_open_search as FO  # noqa: E402
import fl_talent_opt as FT  # noqa: E402
import level_guides as LG  # noqa: E402

LEVELS = [20, 25, 30, 35, 40, 45, 50, 55, 60]
OUT = HERE / "filler"
NO_LOSS = 0.001   # a "no loss" move may cost at most 0.1% of the level-weighted time per kill on each seed (2026-11-09)


def flat_of(pts):
    out = {}
    for _, n in pts:
        out[n] = out.get(n, 0) + 1
    return out


def per_level(pool, cls, rot, space, builds, levels, fights, seed):
    """{level: time per kill} for each per-point order in `builds` (the allocation at each level from the order)."""
    jobs = []
    for pts in builds:
        order = FL.compress(pts)
        b = {"allocation": FL.alloc_of(space, flat_of(pts)), "order": order}
        jobs += [(cls, rot, FL.FR.allocation_at(b, L), L, fights, seed, True, (flat_of(pts), order)) for L in levels]
    res = pool.map(FO._ttk, jobs, chunksize=1)
    return [{L: res[i * len(levels) + k][0] for k, L in enumerate(levels)} for i in range(len(builds))]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--bar", type=float, default=0.003)
    ap.add_argument("--max-moves", type=int, default=6)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    cls = a.cls
    b, order, prov, rot = LG.pick(cls, a.spec)
    if not b:
        sys.exit(f"{cls} {a.spec}: no leveling pick")
    MLT = FO._load("ml_talents_open", ROOT / "_reference/data/raidsim/ml_talents.py")   # as fl_levels.main loads it
    space = MLT.Space(cls, "any", any_split=True)
    pts = FL.expand(order)
    total = len(pts)
    rec = {"class": cls, "spec": a.spec, "build": b["id"], "rotation": rot, "date": datetime.date.today().isoformat(), "fights": a.fights,
           "start_order": FL.compress(pts), "steps": [], "moves": []}
    print(f"== {cls} {a.spec}: {b['id']} ({rot}), {total} points", flush=True)
    with multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",)) as pool:
        for _ in range(a.max_moves):
            base = per_level(pool, cls, rot, space, [pts], LEVELS, a.fights, 3)[0]
            w0 = FL.weighted_at(base, LEVELS)
            # 1-2: removal values at 60 and the zero points (the last rank of each talent, legal along the order without it)
            held = sorted(flat_of(pts))
            drops = []
            for n in held:
                i = max(k for k, (_, x) in enumerate(pts) if x == n)
                rest = pts[:i] + pts[i + 1:]
                if FL.legal_order(space, rest, total - 1):
                    drops.append((n, i, rest))
            r60 = per_level(pool, cls, rot, space, [rest for _, _, rest in drops], [60], a.fights, 3)
            value = {n: base[60] - r[60] for (n, _, _), r in zip(drops, r60)}   # negative: the build is slower without it
            floor = 0.003 * base[60]
            zero = [(n, i) for n, i, _ in drops if value[n] > -floor]
            print(f"  weighted {w0:.2f} s; zero points: {', '.join(n for n, _ in zero) or 'none'}", flush=True)
            rec["steps"].append({"weighted": round(w0, 3), "values_at_60": {n: round(v, 3) for n, v in value.items()}, "zero": [n for n, _ in zero]})
            if not zero:
                break
            # 3: every move of a zero point to another talent at the same level
            cand = []
            for n, i in zero:
                tree = pts[i][0]
                for tname in space.tree_names:
                    for d in space.by_tree[tname]:
                        if d == n:
                            continue
                        new = pts[:i] + [(tname, d)] + pts[i + 1:]
                        if FL.legal_order(space, new, total):
                            cand.append((n, d, i, new))
            if not cand:
                break
            scored = []
            for i in sorted({c[2] for c in cand}):   # a move changes the build from its level on: race only those levels
                group = [c for c in cand if c[2] == i]
                lv = [L for L in LEVELS if L >= 10 + i] or [60]
                for (n, d, _, new), res in zip(group, per_level(pool, cls, rot, space, [c[3] for c in group], lv, a.fights, 3)):
                    scored.append((FL.weighted_at({**base, **res}, LEVELS), n, d, i, new))
            scored.sort()
            w1, n, d, i, new = scored[0]
            if w1 <= w0 * (1 - a.bar):
                b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                print(f"  move {n} (level {10 + i}) -> {d}: {w0:.2f} -> {w1:.2f} s ({w1 / w0 - 1:+.2%}); seed 4 {g2:+.2%}", flush=True)
                if g2 <= -a.bar:
                    rec["moves"].append({"from": n, "to": d, "level": 10 + i, "seed3": round(w1 / w0 - 1, 4), "seed4": round(g2, 4), "why": "measured"})
                    pts = new
                    continue
            # no move clears the bar: the point measures nothing where it is, so it goes where it at least costs nothing and is no
            # dead weight (2026-11-08, user: "There's not a single other better place to spend that talent?"): the best few moves of
            # seed 3 that also cost no time on seed 4, a talent that is not itself a zero point
            tie = None
            moved = {m['from'] for m in rec['moves']}   # never move a point back into a talent it left
            for w1, n, d, i, new in [s for s in scored if s[0] < w0 and s[2] not in {z for z, _ in zero} and s[2] not in moved][:4]:
                b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                if g2 < -0.0005 and (tie is None or (w1 / w0 - 1) + g2 < (tie[0] / w0 - 1) + tie[5]):   # faster on both seeds: the best
                    tie = (w1, n, d, i, new, g2)
            why = "tie-break"
            if not tie:
                # 2026-11-09: no move is faster on both seeds, so noise kept a dead point where it was (the Affliction pick's Improved
                # Sayaad, a Succubus talent in a Voidwalker build). A zero point still goes to a talent that measured something, when the
                # move costs no time beyond NO_LOSS on either seed: a point that does nothing is never better than one that does
                done = {m["from"] for m in rec["moves"]} | {m["to"] for m in rec["moves"]}
                for w1, n, d, i, new in [s for s in scored if s[0] <= w0 * (1 + NO_LOSS) and s[2] not in {z for z, _ in zero}
                                         and s[2] not in moved and s[1] not in done][:4]:
                    b2, n2 = per_level(pool, cls, rot, space, [pts, new], LEVELS, a.fights, 4)
                    g2 = FL.weighted_at(n2, LEVELS) / FL.weighted_at(b2, LEVELS) - 1
                    if g2 <= NO_LOSS and (tie is None or (w1 / w0 - 1) + g2 < (tie[0] / w0 - 1) + tie[5]):
                        tie = (w1, n, d, i, new, g2)
                why = "no loss"
            if not tie:
                print(f"  best move {scored[0][1]} -> {scored[0][2]}: {w0:.2f} -> {scored[0][0]:.2f} s: under the bar, no tie-break", flush=True)
                break
            w1, n, d, i, new, g2 = tie
            print(f"  {why} {n} (level {10 + i}) -> {d}: {w0:.2f} -> {w1:.2f} s; seed 4 {g2:+.2%}", flush=True)
            rec["moves"].append({"from": n, "to": d, "level": 10 + i, "seed3": round(w1 / w0 - 1, 4), "seed4": round(g2, 4), "why": why})
            pts = new
    OUT.mkdir(exist_ok=True)
    slug = a.spec.lower().replace("/", "-").replace(" ", "-")
    rec["final_order"] = FL.compress(pts)
    (OUT / f"{cls}-{slug}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(rec["moves"], indent=1))
    if a.write and rec["moves"]:
        path = ROOT / cls / "research/talents/forever/proposed-builds.json"
        data = json.load(open(path, encoding="utf-8"))
        bb = next(x for x in data["builds"] if x["id"] == b["id"])
        bb["allocation"] = FL.alloc_of(space, flat_of(pts))
        bb["order"] = FL.compress(pts)
        text = "; ".join(f"{m['from']} to {m['to']} at {m['level']} ({m['why']}: {m['seed3']:+.1%} seed 3, {m['seed4']:+.1%} seed 4, level-weighted time per kill)"
                         for m in rec["moves"])
        bb.setdefault("notes", []).insert(0, f"{rec['date']}: leveling filler pass (fightlab/fl_filler_pass.py, {a.fights} fights a level): points that "
                                             f"measured nothing moved: {text}.")
        path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {path}")
        # open_builds.py rewrites an -open-leveling build from its search record on every run: it re-applies a written pass whose
        # start_order is still the record's order (2026-11-09), from these two fields
        rec["written"] = {"allocation": bb["allocation"], "order": bb["order"], "note": bb["notes"][0]}
        (OUT / f"{cls}-{slug}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
