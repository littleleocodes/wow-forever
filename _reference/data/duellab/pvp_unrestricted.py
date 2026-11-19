"""The no-rules PvP search (2026-11-19; user, 2026-11-18: "I think we do the no rules search after everything, checking all
combinations for each class to see what is the best spec all around, even if it's a weird super hybrid build", then "Go with no rece":
my recommendation to include PvP).

    python _reference/data/duellab/pvp_unrestricted.py [classes] [--workers 10] [--smoke] [--fresh]

Per class, one search over every legal 51-point build: no tree rule (pvp_search.search with tree=None) and no signature talents.
1. Starts we know: each tree's duel build (the blind-spot check's improved build when adopted, else the round's search winner) and
   battleground version, and the class's community PvP builds (pvp-community-builds.json).
2. Hybrid starts: blends of the trees' duel builds at set splits (each ordered pair of trees at 31/20, each pair at 26/25, all three
   at 17/17/17). A tree's share is its duel build's talents in that tree, lowest rows first, so every tier stays legal; points left
   over go to random legal talents. Each blend gets a short climb (pvp_search.search, few steps) before it competes.
3. The search: from the best of all starts, the round-2 settings with more steps (any-split moves, tier chains), then the final race
   of the winner against every start on the same duels (seed 3, 240 a matchup).
Record duellab/unrestricted/<class>.json (resumable by class). A model of stated assumptions (duel.py), not a measurement.
"""
import argparse
import datetime
import itertools
import json
import os
import pathlib
import random
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path.insert(0, str(HERE))
import duel_run as DR  # noqa: E402
import pvp_search as PS  # noqa: E402
import render_pvp_research as RP  # noqa: E402

OUT = HERE / "unrestricted"
SPLITS_PAIR = ((31, 20), (26, 25))
SPLIT_ALL = (17, 17, 17)


def known_starts(cls, trees):
    """{label: allocation} of the class's duel builds, battleground versions and community PvP builds."""
    extra = RP.newest_results()
    out = {}
    for tree in trees:
        k = f"{cls}:{tree}"
        p = HERE / "search" / f"{cls}-{RP.slug(tree)}.json"
        if not p.exists():
            continue
        r = json.loads(p.read_text(encoding="utf-8"))
        recs = {k: r}
        out[f"{tree} duel build"] = RP.duel_alloc(k, recs, extra)
        bg = (extra.get("battleground") or {}).get(k)
        if bg:
            out[f"{tree} battleground"] = {a: b for a, b in bg["allocation"].items() if b}
    src = json.loads((DATA / "pvp-community-builds.json").read_text(encoding="utf-8"))
    for b in src["builds"]:
        if b["class"] == cls and b.get("for", "pvp") == "pvp":
            try:
                al = DR.community(cls, b["key"])["allocation"]
                if isinstance(next(iter(al.values()), None), list):   # {tree: [[talent, ranks], ...]}
                    al = {n: r for items in al.values() for n, r in items}
                out[f"community:{b['key']}"] = {n: r for n, r in al.items() if r}
            except SystemExit:
                pass
    return out


def prereqs(info, cap):
    """[(talent, rank needed)] of a talent: the data lists [talent, rank] pairs (a bare name needs the talent's maximum rank)."""
    out = []
    for q in info.get("requires") or []:
        out.append((q[0], int(q[1])) if isinstance(q, (list, tuple)) else (q, cap[q]))
    return out


def legal_fill(trees, flat, rng, want=None):
    """`flat` filled to 51 points with random legal ranks, a tree's share at most `want[tree]` while another tree can take the point;
    None when it cannot be made legal. Row r of a tree opens at 5 * r points in the rows below it; a prerequisite must be at its
    maximum rank."""
    flat = {n: r for n, r in flat.items() if r}
    rows = {t: {n: info["row"] for n, info in tr["talents"].items()} for t, tr in trees.items()}
    cap = {n: info["max"] for tr in trees.values() for n, info in tr["talents"].items()}
    req = {n: prereqs(info, cap) for tr in trees.values() for n, info in tr["talents"].items()}
    tree_of = {n: t for t, tr in trees.items() for n in tr["talents"]}
    while sum(flat.values()) < 51:
        opts = []
        for n, t in tree_of.items():
            if flat.get(n, 0) >= cap[n] or any(flat.get(q, 0) < k for q, k in req[n]):
                continue
            below = sum(k for m, k in flat.items() if tree_of[m] == t and rows[t][m] < rows[t][n])
            if below < 5 * rows[t][n]:
                continue
            opts.append((n, t))
        if not opts:
            return None
        if want:
            pts = {t: sum(k for m, k in flat.items() if tree_of[m] == t) for t in trees}
            under = [(n, t) for n, t in opts if pts[t] < want.get(t, 0)]
            opts = under or opts
        n, _ = rng.choice(opts)
        flat[n] = flat.get(n, 0) + 1
    return flat


def blend(trees, duel, split, rng):
    """A build with split[t] points in tree t taken from that tree's duel build, lowest rows first, the rest filled legally."""
    rows = {n: info["row"] for tr in trees.values() for n, info in tr["talents"].items()}
    flat = {}
    for t, want in split.items():
        src = sorted(((n, r) for n, r in (duel.get(t) or {}).items() if n in trees[t]["talents"] and r), key=lambda x: rows[x[0]])
        got = 0
        for n, r in src:
            if got >= want:
                break
            k = min(r, want - got)
            flat[n] = k
            got += k
    # trim to what is legal: rebuild point by point from the chosen ranks, row order, then fill
    order = sorted(flat.items(), key=lambda x: rows[x[0]])
    base = {}
    tree_of = {n: t for t, tr in trees.items() for n in tr["talents"]}
    cap = {n: info["max"] for tr in trees.values() for n, info in tr["talents"].items()}
    req = {n: prereqs(info, cap) for tr in trees.values() for n, info in tr["talents"].items()}
    for n, k in order:
        t = tree_of[n]
        below = sum(v for m, v in base.items() if tree_of[m] == t and rows[m] < rows[n])
        if below >= 5 * rows[n] and all(base.get(q, 0) >= r for q, r in req[n]):
            base[n] = k
    return legal_fill(trees, base, rng, want=split)


def run_class(cls, a, log):
    TO, VB = PS.talent_opt()
    trees = VB.load_forever()[cls]
    names = list(trees)
    known = known_starts(cls, names)
    duel = {}
    for t in names:   # each tree's duel build, by tree, for the blends
        d = known.get(f"{t} duel build") or {}
        duel[t] = {n: r for n, r in d.items() if n in trees[t]["talents"]}
    rng = random.Random(1)
    blends = {}
    for x, y in itertools.permutations(names, 2):
        sp = {x: SPLITS_PAIR[0][0], y: SPLITS_PAIR[0][1]}
        b = blend(trees, duel, sp, rng)
        if b and TO.valid(trees, b):
            blends[f"blend {x} {sp[x]} / {y} {sp[y]}"] = b
    for x, y in itertools.combinations(names, 2):
        sp = {x: SPLITS_PAIR[1][0], y: SPLITS_PAIR[1][1]}
        b = blend(trees, duel, sp, rng)
        if b and TO.valid(trees, b):
            blends[f"blend {x} {sp[x]} / {y} {sp[y]}"] = b
    sp = dict(zip(names, SPLIT_ALL))
    b = blend(trees, duel, sp, rng)
    if b and TO.valid(trees, b):
        blends["blend " + "/".join(f"{t} {sp[t]}" for t in names)] = b
    log(f"== {time.strftime('%H:%M')} {cls}: {len(known)} known starts, {len(blends)} blends; {a.workers} workers")
    small = dict(steps=2, batch=8, n_screen=4, n_confirm=8, patience=1) if a.smoke else dict(steps=4, batch=24, n_screen=40, n_confirm=120, patience=2)
    polished = {}
    for lab, al in blends.items():
        r = PS.search(cls, {lab: al}, None, workers=a.workers, log=lambda m: None, keep_signature=False, **small)
        polished[lab] = {"J": r["J"], "win": r["win"], "allocation": r["final"], "split": RP.split_of(cls, r["final"]),
                         "moves": len(r["history"]) - 1}
        log(f"  {lab}: {polished[lab]['split']} J {r['J']:.3f} (win {r['win']:.1%}) after {polished[lab]['moves']} kept moves")
    top = sorted(polished, key=lambda k: -polished[k]["J"])[:4]
    refs = dict(known)
    refs.update({f"polished {k}": polished[k]["allocation"] for k in top})
    main = dict(steps=3, batch=8, n_screen=4, n_confirm=8, patience=1) if a.smoke else dict(steps=30, batch=48, n_screen=40, n_confirm=120, patience=8)
    rec = PS.search(cls, refs, None, workers=a.workers, log=log, keep_signature=False, **main)
    rec.update({"round": "unrestricted", "blends": polished, "known": sorted(known), "smoke": bool(a.smoke),
                "split": RP.split_of(cls, rec["final"]), "date": datetime.date.today().isoformat()})
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--smoke", action="store_true", help="tiny budgets, written under unrestricted/smoke/")
    ap.add_argument("--fresh", action="store_true")
    a = ap.parse_args()
    os.chdir(ROOT)
    out = OUT / "smoke" if a.smoke else OUT
    out.mkdir(parents=True, exist_ok=True)
    for cls in RP.CLASSES:
        if a.classes and cls not in a.classes:
            continue
        p = out / f"{cls}.json"
        if p.exists() and not a.fresh:
            print(f"== {cls}: in the record, skipped", flush=True)
            continue
        t0 = time.time()
        rec = run_class(cls, a, lambda m: print(m, flush=True))
        rec["minutes"] = round((time.time() - t0) / 60, 1)
        p.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
        print(f"== {cls}: no-rules winner {rec['split']} win {rec['win']:.1%} (J {rec['J']:.3f}) in {rec['minutes']} min; race: "
              + ", ".join(f"{k} {v['win']:.1%}" for k, v in rec["race"].items()), flush=True)


if __name__ == "__main__":
    main()
