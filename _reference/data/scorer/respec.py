"""Respec planner: when is it worth re-speccing while leveling?

A build that is best at 60 is not necessarily best at 25, and the best level-25 build may be a dead end at 60.
This tool builds *plans* and lets a dynamic programme pick when to switch between them:

* a plan = (spec model, target level T): the optimizer's best (T-9)-point build for level T, bought in the
  optimizer's receding-horizon order from level 10, then extended greedily to 60 for players who never respec
  again (T = 60 is the ordinary "play toward the 60 build" plan);
* at any level the player may respec into another plan (its allocation for that level is bought outright) for
  the Classic respec price (1g, then +5g per respec, capped at 50g) converted to hours at that level's gold income;
* the objective is total leveling hours: hours-per-level x (1 - leveling score) summed over 10..60 plus respec time.

    python _reference/data/scorer/respec.py <class> [--game forever|classic-era] [--profile leveling-st]
                                                     [--models m1,m2] [--targets 20,30,40,50,60] [--write]

`--write` saves `<class>/research/leveling/respec-plan.md` (Forever) or `<class>/research/talents/classic-baseline/respec-plan.md`.
"""
import pathlib
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402

from optimize import Optimizer  # noqa: E402

# Leveling time and money assumptions (Classic-like pacing without heirlooms; edit freely).
HOURS_PER_LEVEL = {10: 0.7, 20: 1.2, 30: 1.6, 40: 2.2, 50: 3.0}      # by level decade
GOLD_PER_HOUR = {10: 0.3, 20: 0.8, 30: 1.5, 40: 3.0, 50: 6.0}        # questing income by decade
RESPEC_COST = lambda k: min(1.0 if k == 0 else 5.0 * k, 50.0)        # k = respecs already done
MAX_RESPECS = 4

LEVELING_MODELS = {
    "hunter": ["bm-leveling"],
    "mage": ["frost-leveling", "fire-leveling"],
    "warrior": ["arms-2h-raid", "fury-dw-raid"],
    "rogue": ["combat-swords-raid", "combat-daggers-raid"],
    "priest": ["shadow-dps"],
    "paladin": ["ret-dps"],
    "shaman": ["enhancement-dps", "elemental-dps"],
    "warlock": ["affliction-leveling"],
    "druid": ["feral-cat-dps", "balance-dps"],
}


def decade(level):
    return max(10, min(50, (level // 10) * 10))


def build_plan(opt, model, target_level, lookahead):
    """Allocation and leveling score for every level 10..60 when playing toward the level-T optimum."""
    opt.total = target_level - 9
    target, _ = opt.best_build(level=target_level)
    steps = opt.order(target, lookahead=lookahead)
    if target_level < 60:
        opt.total = 51
        ext = opt.refill(target, level=60)
        steps += opt.order(ext, lookahead=lookahead, start_state=target, start_level=target_level + 1)
    opt.total = 51
    state, allocs, scores = {}, {}, {}
    for level, name, rank, _ in steps:
        state[name] = state.get(name, 0) + 1
        allocs[level] = dict(state)
        scores[level] = opt.score(state, level)
    return {"model": model, "target_level": target_level, "target": target, "allocs": allocs, "scores": scores,
            "split": opt.tree.split(target), "factor": opt.spec.get("abs_dps_factor", 1.0)}


def level_hours(plan, level):
    return HOURS_PER_LEVEL[decade(level)] * (1.0 - plan["scores"][level]) / plan["factor"]


def solve(plans):
    """DP over levels: state (plan index, respecs done). Returns best cost, and the schedule."""
    n = len(plans)
    INF = float("inf")
    # cost to *finish* level `level` on plan p with k respecs done
    best = {(p, 0): (level_hours(plans[p], 10), [(10, p)]) for p in range(n)}
    for level in range(11, 61):
        nxt = {}
        for (p, k), (cost, hist) in best.items():
            # stay
            c = cost + level_hours(plans[p], level)
            if c < nxt.get((p, k), (INF,))[0]:
                nxt[(p, k)] = (c, hist)
            # respec at the start of this level
            if k < MAX_RESPECS:
                fee_h = RESPEC_COST(k) / GOLD_PER_HOUR[decade(level)]
                for q in range(n):
                    if q == p:
                        continue
                    c2 = cost + fee_h + level_hours(plans[q], level)
                    if c2 < nxt.get((q, k + 1), (INF,))[0]:
                        nxt[(q, k + 1)] = (c2, hist + [(level, q)])
        best = nxt
    (p, k), (cost, hist) = min(best.items(), key=lambda kv: kv[1][0])
    return cost, hist


def single_plan_costs(plans):
    return [(sum(level_hours(pl, lv) for lv in range(10, 61)), i) for i, pl in enumerate(plans)]


def fmt_alloc(opt, alloc):
    by_tree = {}
    for name, r in alloc.items():
        if r > 0:
            by_tree.setdefault(opt.tree.info[name][0], []).append(f"{name} {r}")
    return "; ".join(f"**{t}**: " + ", ".join(v) for t, v in by_tree.items())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls")
    ap.add_argument("--game", default="forever", choices=["forever", "classic-era"])
    ap.add_argument("--profile", default="leveling-st")
    ap.add_argument("--models")
    ap.add_argument("--targets", default="20,30,40,50,60")
    ap.add_argument("--lookahead", type=int, default=4)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    models = a.models.split(",") if a.models else LEVELING_MODELS[a.cls]
    targets = [int(t) for t in a.targets.split(",")]

    opts = {m: Optimizer(a.game, a.cls, m, a.profile) for m in models}
    plans = []
    for m in models:
        for t in targets:
            print(f"building plan {m} -> level {t}", file=sys.stderr)
            plans.append(build_plan(opts[m], m, t, a.lookahead))
    base_hours = sum(HOURS_PER_LEVEL[decade(lv)] for lv in range(10, 61))
    singles = sorted(single_plan_costs(plans))
    cost, hist = solve(plans)
    factors = {pl["model"]: pl["factor"] for pl in plans}
    cross_unmeasured = len(models) > 1 and len(set(factors.values())) == 1

    def pname(i):
        return f"{plans[i]['model']} -> level-{plans[i]['target_level']} build ({plans[i]['split']})"

    def schedule_lines(hist, cost, plans_idx):
        segs, lines = [], []
        for i, (lv, p) in enumerate(hist):
            end = hist[i + 1][0] - 1 if i + 1 < len(hist) else 60
            segs.append((lv, end, p))
        for lv, end, p in segs:
            pl = plans[p]
            lines.append(f"- **Levels {lv}-{end}: {pname(p)}**" + (" (respec here)" if lv > 10 else ""))
            lines.append(f"  - at level {lv}: {fmt_alloc(opts[pl['model']], pl['allocs'][lv])}")
            lines.append(f"  - at level {end}: {fmt_alloc(opts[pl['model']], pl['allocs'][end])}")
            # point-by-point path inside the segment (level ranges -> talent), from the plan's allocations
            runs = []
            prev = pl["allocs"][lv - 1] if lv > 10 else {}
            for l in range(lv, end + 1):
                cur = pl["allocs"][l]
                added = [(n, r) for n, r in cur.items() if r > prev.get(n, 0)]
                prev = cur
                if l == lv and lv > 10:
                    continue  # the respec buys the whole level-lv allocation at once
                for n, r in added:
                    if runs and runs[-1][1] == n:
                        runs[-1][2] = l; runs[-1][3] += 1
                    else:
                        runs.append([l, n, l, 1])
            if runs:
                lines.append("  - order: " + ", ".join(f"{a}{'-' + str(b) if b != a else ''} {n}" + (f" x{k}" if k > 1 else "") for a, n, b, k in runs))
        lines.append("")
        n = len(hist) - 1   # 2026-10-15 page audit B17: "0 respec(s)."
        lines.append(f"Total: **{cost:.1f} h** ({(1 - cost / base_hours) * 100:.1f}% faster than talentless), "
                     + ("no respec" if n == 0 else "1 respec" if n == 1 else f"{n} respecs") + ".")
        return lines

    out = [f"# {a.cls.capitalize()} / {a.game}: respec plan for `{a.profile}`", "",
           "> Generated by `_reference/data/scorer/respec.py`. Plans are optimizer builds for a target level, bought in optimizer order and extended greedily to 60; "
           "the schedule minimises total leveling hours including respec gold converted to time. Assumptions (edit in `respec.py`): "
           f"hours per level by decade {HOURS_PER_LEVEL}, gold/hour {GOLD_PER_HOUR}, respec 1g then +5g each (cap 50g), at most {MAX_RESPECS} respecs. "
           "Scores are the leveling profile's 'fraction of time per kill saved' vs a talentless character of the same model; models are compared through their `abs_dps_factor`.", "",
           f"Talentless baseline: {base_hours:.0f} h for levels 10-60 under these assumptions.", "",
           "## Recommended schedule", ""]
    if cross_unmeasured:
        out.append(f"> Models {', '.join(models)} all have `abs_dps_factor` 1.0 (unmeasured), so their plans are compared as if a talentless "
                   "character of each killed equally fast. A switch *between models* below rests on that assumption; the per-model schedules further down do not.")
        out.append("")
    out += schedule_lines(hist, cost, None)
    out.append("")
    if len(models) > 1:
        out += ["## Best schedule if you stay in one spec model", ""]
        for m in models:
            idx = [i for i, pl in enumerate(plans) if pl["model"] == m]
            sub = [plans[i] for i in idx]
            c_m, h_m = solve(sub)
            h_m = [(lv, idx[p]) for lv, p in h_m]
            out.append(f"### {m}")
            out.append("")
            out += schedule_lines(h_m, c_m, idx)
            out.append("")
    out += ["## Never respec: best single plan", "", "| Plan | Hours 10-60 | vs. schedule |", "|---|---|---|"]
    for c, i in singles:
        out.append(f"| {pname(i)} | {c:.1f} | {c - cost:+.1f} h |")
    out.append("")
    out += ["## Leveling score by level (fraction of time per kill saved)", ""]
    levels = list(range(10, 61, 5))
    out.append("| Plan | " + " | ".join(str(l) for l in levels) + " |")
    out.append("|---|" + "---|" * len(levels))
    for i, pl in enumerate(plans):
        out.append(f"| {pname(i)} | " + " | ".join(f"{pl['scores'][l] * 100:+.1f}%" for l in levels) + " |")
    out.append("")
    out += ["## Reading it", "",
            "- A respec only pays when the level-optimal build differs from the 60-build's path *and* the gap, summed over the levels until the next switch, beats the respec fee in hours. "
            "Small gaps (a few %) rarely do before 40; large ones (a different tree, e.g. Fire vs Frost, or a two-hander build vs a dual-wield build) can.",
            "- 'Extended greedily' plans (target < 60) show what happens if you stop planning after the target level; if the schedule ends on one, the 60-build path was not worth its early sacrifices.",
            "- Everything downstream of the effect encodings inherits their uncertainty; treat differences under ~1 h as noise."]
    text = "\n".join(out) + "\n"
    print(text)
    if a.write:
        path = paths.respec_plan(a.cls, a.game)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
