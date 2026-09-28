"""Run the talent scorer/optimizer.

    python _reference/data/scorer/run.py <class> --spec <spec-model> --profile <profile> [--game forever|classic-era]
                                          [--compare <build-id>] [--write] [--lookahead 4]

Prints: marginal value of every talent (next rank) at 60 from an empty tree and from the optimized build,
the optimized 51-point build, its leveling order, and a comparison with an existing build from
builds.json / proposed-builds.json. --write saves a markdown report:
    forever     -> <class>/<leveling|raid|pvp>/optimizer/<spec>-<profile>.md (the profile's scenario)
    classic-era -> <class>/talents/classic-baseline/optimizer/<spec>-<profile>.md
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
from optimize import Optimizer  # noqa: E402


def load_build(game, cls, build_id):
    if build_id.endswith(".json"):   # a saved candidate file (raidsim/candidates: optimizer rounds, the simulator's presets)
        b = json.load(open(build_id, encoding="utf-8"))
        return {n: p for items in b["allocation"].values() for n, p in items}
    rel = "talents/classic-baseline/builds.json" if game == "classic-era" else "talents/forever/proposed-builds.json"
    data = json.load(open(ROOT / cls / rel, encoding="utf-8"))
    for b in data["builds"]:
        if b["id"] == build_id:
            return {n: p for items in b["allocation"].values() for n, p in items}
    raise SystemExit(f"build {build_id} not found in {rel}")


def fmt_alloc(opt, alloc):
    by_tree = {}
    for n, r in sorted(alloc.items(), key=lambda x: (opt.tree.info[x[0]][0], opt.tree.info[x[0]][1])):
        if r:
            by_tree.setdefault(opt.tree.info[n][0], []).append(f"{n} {r}")
    return "\n".join(f"  {t}: " + ", ".join(v) for t, v in by_tree.items())


def export_build(a, opt, best, best_s, steps):
    """Insert/replace the optimized build in proposed-builds.json (forever) or builds.json (classic-era)."""
    sys.path.insert(0, str(HERE.parent))
    from fmt_json import dumps
    rel = "talents/classic-baseline/builds.json" if a.game == "classic-era" else "talents/forever/proposed-builds.json"
    path = ROOT / a.cls / rel
    data = json.load(open(path, encoding="utf-8"))
    bid = f"opt-{a.spec}-{a.profile}"
    content = {"leveling-st": "leveling", "leveling-aoe": "leveling", "solo-60": "solo", "pvp": "pvp"}.get(a.profile, "raid")
    alloc = {t: [] for t in opt.tree.order}
    for n, r in sorted(best.items(), key=lambda x: (opt.tree.order.index(opt.tree.info[x[0]][0]), opt.tree.info[x[0]][1])):
        if r:
            alloc[opt.tree.info[n][0]].append([n, r])
    # core = talents whose removal costs the most
    losses = []
    for n in best:
        trial = dict(best); del trial[n]
        losses.append((best_s - opt.score(trial, 60), n))
    losses.sort(reverse=True)
    core = [{"talent": n, "why": f"Removing it costs {l*100:.1f} points of score in this model."} for l, n in losses[:8]]
    entry = {
        "id": bid,
        "name": f"Optimizer — {opt.spec.get('note', a.spec).split('.')[0]} ({a.profile})",
        "role": {"heal": "healer", "tank": "tank"}.get(opt.profile.get("mode"), "dps"), "content": content, "tier": "draft",
        "summary": (f"Produced by the stats model (`_reference/data/scorer/`) for spec model `{a.spec}` and profile `{a.profile}`: "
                    f"score {best_s*100:+.1f}% ({ {'leveling': 'time-per-kill saved', 'heal': 'healing score: 0.6 x HPS gain + 0.5 x mana gain', 'tank': 'tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain'}.get(opt.profile.get('mode'), 'DPS gain') } vs. no talents). "
                    "Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build."),
        "allocation": alloc,
        "core": core,
        "flex": [],
        "notes": [f"Report: {a.cls}/talents/{'forever' if a.game == 'forever' else 'classic-baseline'}/optimizer/{a.spec}-{a.profile}.md"],
        "open_questions": ["Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on."],
        "sources": ["https://warcraftforever.games/talents/" + a.cls if a.game == "forever" else "_reference/data/classic-era-talents.json"],
    }
    if steps:
        entry["order"] = [{"levels": lv, "tree": t, "talent": n, "points": pts} for lv, t, n, pts in opt.compress_order(steps)]
    data["builds"] = [b for b in data["builds"] if b["id"] != bid] + [entry]
    path.write_text(dumps(data) + "\n", encoding="utf-8")
    print(f"exported {bid} -> {path.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--profile", required=True)
    ap.add_argument("--game", default="forever", choices=["forever", "classic-era"])
    ap.add_argument("--compare")
    ap.add_argument("--seed", nargs="*", default=[], help="build ids (or candidate .json files) that seed the optimizer's search (the hand drafts, the simulator's competing presets); --compare seeds it too")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--lookahead", type=int, default=6)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--export", action="store_true", help="write the optimized build into the class's builds JSON (id opt-<spec>-<profile>)")
    a = ap.parse_args()

    opt = Optimizer(a.game, a.cls, a.spec, a.profile)
    lines = []
    P = lambda s="": (print(s), lines.append(s))

    P(f"# {a.cls} / {a.game} / spec {a.spec} / profile {a.profile}")
    P()
    coverage = {"parsed": 0, "manual": 0, "missing": 0}
    for n, e in opt.effects.items():
        coverage[e["source"]] += 1
    P(f"Effect coverage: {coverage['parsed']} parsed from tooltips, {coverage['manual']} hand-entered, {coverage['missing']} missing (scored as 0).")
    if coverage["missing"]:
        P("Missing: " + ", ".join(n for n, e in opt.effects.items() if e["source"] == "missing"))
    P()

    # --- single-talent values from an empty tree (what each talent's first rank is worth on its own)
    P(f"## Marginal value of each talent's first rank from an empty tree (level 60, top {a.top})")
    P()
    P("| Talent | Tree | Tier | Value | Source |")
    P("|---|---|---|---|---|")
    for s, name, tname, tier, nr, mx, legal, src in opt.marginal_table({}, 60)[: a.top]:
        P(f"| {name} | {tname} | {tier} | {s*100:+.2f}% | {src} |")
    P()

    # --- best build (the compared build seeds the search, so the optimizer never returns something it scores below it)
    seeds = [load_build(a.game, a.cls, b) for b in ([a.compare] if a.compare else []) + list(a.seed)]
    best, best_s = opt.best_build(60, seeds=seeds)
    detail = opt.score(best, 60, detail=True)
    absf = opt.spec.get("abs_dps_factor", 1.0)
    P(f"## Optimized build: {opt.tree.split(best)}  score {best_s*100:+.2f}%  (dps x{detail['dps']:.3f}, sustain x{detail['sustain']:.3f}, surv x{detail['surv']:.3f}, utility {detail['utility']*100:+.2f}%)")
    if absf != 1.0:
        P(f"Absolute DPS index (character alone, no talents = 1.00): {detail['dps']*absf:.3f}  — use this to compare models with different pet shares.")
    P()
    P("```")
    for ln in fmt_alloc(opt, best).split("\n"):
        P(ln)
    P("```")
    P()

    # --- marginal values at the optimized build (what would the 52nd point be worth / what is each taken point worth)
    P("## Next-rank values from the optimized build (what a 52nd point would buy)")
    P()
    P("| Talent | Tier | Next rank | Value | Legal now |")
    P("|---|---|---|---|---|")
    for s, name, tname, tier, nr, mx, legal, src in opt.marginal_table(best, 60)[:15]:
        P(f"| {name} | {tname} {tier} | {nr}/{mx} | {s*100:+.2f}% | {'yes' if legal else 'no'} |")
    P()

    # --- order
    steps = None
    if opt.profile.get("mode") == "leveling":
        steps = opt.order(best, lookahead=a.lookahead)
        P(f"## Leveling order (lookahead {a.lookahead}; {getattr(opt, 'order_label', 'receding horizon')})")
        P()
        P("| Levels | Tree | Talent | Pts | Score at end |")
        P("|---|---|---|---|---|")
        runs = opt.compress_order(steps)
        by_level_score = {lv: sc for lv, _, _, sc in steps}
        for levels, tname, name, pts in runs:
            end = int(levels.split("-")[-1])
            P(f"| {levels} | {tname} | {name} | {pts} | {by_level_score[end]*100:+.1f}% |")
        P()

    # --- comparison
    if a.compare:
        ref = load_build(a.game, a.cls, a.compare)
        ref_s = opt.score(ref, 60)
        P(f"## Comparison with `{a.compare}`: {opt.tree.split(ref)} scores {ref_s*100:+.2f}% vs optimized {best_s*100:+.2f}%")
        P()
        P("| Talent | Reference | Optimized |")
        P("|---|---|---|")
        for n in sorted(set(ref) | set(best), key=lambda x: (opt.tree.info[x][0], opt.tree.info[x][1], x)):
            r, o = ref.get(n, 0), best.get(n, 0)
            if r != o:
                P(f"| {n} ({opt.tree.info[n][0]} T{opt.tree.info[n][1]+1}) | {r} | {o} |")
        P()

    if a.export:
        if a.game == "classic-era":
            print("(--export ignored for classic-era: the Classic baseline stays the community consensus; see the calibration report)")
        else:
            export_build(a, opt, best, best_s, steps if opt.profile.get("mode") == "leveling" else None)

    if a.write:
        out = paths.optimizer_report(a.cls, a.game, a.spec, a.profile)
        out.parent.mkdir(parents=True, exist_ok=True)
        header = ("> Generated by `_reference/data/scorer/run.py`. Numbers come from the effect files in "
                  "`_reference/data/scorer/effects/` (tooltip-parsed or hand-entered with the arithmetic in the note), "
                  "the spec model in `_reference/data/scorer/specs/`, and the profile in `profiles.json`. "
                  "Change those inputs, not this file.\n")
        out.write_text("\n".join([lines[0], "", header] + lines[1:]) + "\n", encoding="utf-8")
        print(f"\nwrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
