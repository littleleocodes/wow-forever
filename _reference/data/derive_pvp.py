"""Derive one PvP build per spec from the stats model and the community's pick rates (2026-09-30, user request: "each spec to have a
leveling, raid and PvP spec that we can best derive from everything"; the user chose "model + community").

    python _reference/data/derive_pvp.py [classes] [--tol 0.01] [--min-gain 0.02] [--write]

No simulator plays PvP, so the scorer's `pvp` profile (burst, survival, sustain and PvP utility; scorer/pvp_check.py tunes it on the
Classic community PvP builds) is the only measurement-like input. Where it has an opinion it decides; where talents score alike, the
community decides:

1. The scorer's best build with 30+ points in the tree (spec_builds.forced_optimizer, the spec's PvP model, spec_builds.MODEL).
2. From there, one legal move at a time (raidsim/talent_opt.py's moves: 1, 2, 3 or 5 points, 30+ points kept in the tree), take the
   move that raises the build's community pick score most while the scorer's score stays within --tol of the optimum's gain over a
   talentless character. Pick score = sum over talents of (share of talentsforever.com builds leading in this tree that take the
   talent) x (ranks / max ranks). Stops when no move raises it.
3. A hand PvP draft of the spec stays the spec's PvP build unless the derived build beats it by --min-gain of the gain over a talentless
   character (the user's replacement rule); then the derived build ranks first and the hand draft stays as the alternative. A spec
   without a hand draft gets the derived build (it replaces the generated one).
4. Disagreements: talents at least --high % of the tree's builds take and the derived build skips (with the scorer's value per point
   against the build's weakest point), and talents it takes that at most --low % take (with their value).

Writes `_reference/data/derived-pvp.json` (generated) and, with --write, the builds into proposed-builds.json (`generated`, `derived`,
`spec`; `replaces` when it beat a hand draft). Pick rates are what calculator visitors planned for level 60 (all content, not PvP
only): a tie-break, never a measurement.
"""
import argparse
import datetime
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "scorer"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import spec_builds as SB  # noqa: E402
import validate_builds as VB  # noqa: E402
from fmt_json import dumps  # noqa: E402
from popular_builds import load_popular, latest_raw  # noqa: E402

_s = importlib.util.spec_from_file_location("raid_talent_opt", HERE / "raidsim/talent_opt.py")
T = importlib.util.module_from_spec(_s)
_s.loader.exec_module(T)

OUT = HERE / "derived-pvp.json"
TODAY = datetime.date.today().isoformat()


def picks(pop, cls, tree):
    """{talent: pick %} among the site's builds leading in `tree`, and the number of builds behind it."""
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    pc = pop["classes"][cls.capitalize()]
    per = pc["pickBy"].get(tree)
    if not per:
        return {}, 0
    return {t["name"]: p for tr, ps in zip(data["trees"], per) for t, p in zip(tr["talents"], ps)}, pc["specN"].get(tree, 0)


def derive(cls, tree, pop, a):
    model = SB.MODEL[(cls, tree)]["pvp"]
    from optimize import Optimizer
    opt = Optimizer("forever", cls, model, "pvp")
    forced = SB.forced_optimizer(cls, model, "pvp", tree)
    best, _ = forced.best_build(level=60)
    best = {k: v for k, v in best.items() if v}
    trees = VB.load_forever()[cls]
    cap = {n: t["talents"][n]["max"] for t in trees.values() for n in t["talents"]}
    rate, n_builds = picks(pop, cls, tree)
    T.MIN_TREE.clear()
    T.MIN_TREE[tree] = SM.SPEC_POINTS
    s0, sbest = opt.score({}, 60), opt.score(best, 60)
    floor = sbest - a.tol * (sbest - s0)

    def pick_score(al):
        return sum(rate.get(n, 0) * r / cap[n] for n, r in al.items())
    cur, moves = dict(best), []
    for _ in range(60):
        cands = [(pick_score(al) - pick_score(cur), d, al) for d, al in T.neighbors(trees, cur) if opt.score(al, 60) >= floor]
        cands = [c for c in cands if c[0] > 1e-9]
        if not cands:
            break
        gain, d, cur = max(cands, key=lambda c: (c[0], opt.score(c[2], 60)))
        moves.append({"move": d, "pick_gain": round(gain, 2), "score_share": round((opt.score(cur, 60) - s0) / (sbest - s0), 4)})
    sc = opt.score(cur, 60)

    def val(al, n):   # share of the build's talent value lost without the talent (per point)
        return (sc - opt.score({k: v for k, v in al.items() if k != n}, 60)) / (sbest - s0) / al[n]
    weak = sorted((val(cur, n), n) for n in cur if opt.tree.legal({k: v for k, v in cur.items() if k != n}))
    skipped = []
    for n, p in sorted(rate.items(), key=lambda x: -x[1]):
        if p >= a.high and n not in cur:
            add = (opt.score(dict(cur, **{n: cap[n]}), 60) - sc) / (sbest - s0) / cap[n]
            skipped.append({"talent": n, "pick": p, "value_per_point": round(add, 4)})
    rare = [{"talent": n, "pick": rate.get(n, 0), "ranks": r, "value_per_point": round(val(cur, n), 4)}
            for n, r in sorted(cur.items()) if rate.get(n, 0) <= a.low]
    return {"model": model, "tree": tree, "builds_behind_picks": n_builds, "score": sc, "score_best": sbest, "score_talentless": s0,
            "optimum": best, "allocation": cur, "moves": moves, "pick_score": round(pick_score(cur), 1), "pick_score_optimum": round(pick_score(best), 1),
            "weakest_point": {"talent": weak[0][1], "value_per_point": round(weak[0][0], 4)} if weak else None,
            "skipped_consensus": skipped, "rare": rare}, opt


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--tol", type=float, default=0.01)
    ap.add_argument("--min-gain", type=float, default=0.02)
    ap.add_argument("--high", type=float, default=70)
    ap.add_argument("--low", type=float, default=20)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    pop = load_popular(latest_raw() / "popular.js")
    res = {}
    for cls in a.classes or SM.CLASSES:
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        res[cls] = {}
        for tree in SM.trees(cls):
            r, opt = derive(cls, tree, pop, a)
            g = SM.grid(cls, data["builds"])
            hands = [b for b in g[tree]["pvp"] if not b.get("generated")]
            span = r["score_best"] - r["score_talentless"]
            r["hand"] = {b["id"]: round((opt.score(SB_flat(b), 60) - r["score_talentless"]) / span, 4) for b in hands}
            best_hand = max(r["hand"].values()) if hands else None
            mine = (r["score"] - r["score_talentless"]) / span
            r["verdict"] = ("new" if not hands else "replaces" if mine - best_hand >= a.min_gain else "hand stays")
            if hands and (cls, tree) in SB.ROUGH:   # a model borrowed from another tree cannot judge this tree's own talents: the hand draft stays
                r["verdict"] = "hand stays (borrowed model)"
            res[cls][tree] = r
            print(f"{cls:8s} {tree:14s} {r['model']:22s} pick {r['pick_score_optimum']:6.1f} -> {r['pick_score']:6.1f}, "
                  f"{len(r['moves'])} moves, score {mine:.3f} of optimum; hand {r['hand']}: {r['verdict']}", flush=True)
            bid = f"{SM.slug(tree)}-pvp"
            data["builds"] = [b for b in data["builds"] if not (b["id"] == bid and b.get("generated"))]
            if not a.write or r["verdict"].startswith("hand stays"):
                continue
            data["builds"].append(build_of(cls, tree, r, hands, best_hand))
        if a.write:
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
    from filelock import locked   # classes run in parallel processes: merge under a lock
    with locked(OUT.with_suffix(".lock")):
        old = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
        old.update(res)
        OUT.write_text(json.dumps(old, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


def SB_flat(b):
    return {n: r for items in b["allocation"].values() for n, r in items if r}


def build_of(cls, tree, r, hands, best_hand):
    moves = "; ".join(m["move"] for m in r["moves"]) or "none (the optimum is already the community's pick)"
    skip = ", ".join(f"{x['talent']} ({x['pick']:.0f}% take it)" for x in r["skipped_consensus"]) or "none"
    rare = ", ".join(f"{x['talent']} ({x['pick']:.0f}%)" for x in r["rare"]) or "none"
    b = {"id": f"{SM.slug(tree)}-pvp", "name": f"{tree} — PvP (derived)", "role": "healer" if r["model"].endswith("-heal") else "dps",
         "content": "pvp", "tier": "draft", "spec": tree, "generated": TODAY, "derived": "pvp",
         "summary": (f"The {tree} PvP build derived on {TODAY} (derive_pvp.py): the stats model's PvP optimum with 30+ points in {tree} "
                     f"(model {r['model']}, profile pvp), then, among builds the model scores within 1% of that, the one the most "
                     f"talentsforever.com {tree} builds agree with ({r['builds_behind_picks']} builds)."),
         "allocation": SB.to_allocation(cls, r["allocation"]), "core": SB.core_of(cls, r["model"], "pvp", r["allocation"]), "flex": [],
         "notes": [f"Community tie-break moves: {moves}.",
                   f"Where we disagree with the community: most {tree} builds take {skip}, which the model values below this build's "
                   f"weakest point; this build takes {rare}, which few {tree} builds take (the model values them). Pick rates cover every "
                   f"level-60 build on the site, not PvP builds only.",
                   "PvP values are assumptions: no simulator plays PvP."] + ([SB.ROUGH[(cls, tree)]] if (cls, tree) in SB.ROUGH else []),
         "open_questions": [f"A derived {tree} PvP build: check it in duels and battlegrounds at launch."],
         "sources": ["https://talentsforever.com/" + cls, "https://talentsforever.com/popular.js"]}
    if hands:
        b["replaces"] = max(hands, key=lambda h: r["hand"][h["id"]])["id"]
        b["notes"].insert(0, f"Scores {((r['score'] - r['score_talentless']) / (r['score_best'] - r['score_talentless']) - best_hand) * 100:+.1f}% "
                             f"of the optimum's talent value above the hand draft {b['replaces']}, over the 2% replacement bar: this build "
                             f"is the spec's PvP pick, the hand draft stays as the alternative.")
    return b


if __name__ == "__main__":
    main()
