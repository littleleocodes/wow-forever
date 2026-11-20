"""Whether a respec to the leveling page's order pays for a character off it (2026-11-20; the user, asked by the audit session what
Arcea should play at 37: "Even if I have to respec"; the audit's request for the planner: "her talents against the page's order at her
level, the minutes saved over the levels left against the respec's gold, shown when it pays").

The character's own path (plan.talents_check: the talents now, then the page's remaining points in the planned order, next_talents'
race included) against the page's order itself, each build measured in the fight lab at the character's level and every EVERY levels to
60 (the page's rotation, FIGHTS fights on seeds 1 and 2, common dice). Minutes saved = over each level left, that level's kills
(plan.kills_per_level) x the difference in seconds a kill (linear between the measured levels) / 60. A respec "pays" when it is faster at
the character's level and saves at least min_minutes (the gear plan's MIN_MINUTES, 20). Its price is Classic's: 1 gold the first time,
5 the second, then 5 more each time up to 50 (the price falls back over time; the planner cannot see how many times you respecced).

    python _reference/data/characters/respec_value.py <character>     # print the check for a character (no page written)
"""
import concurrent.futures as CF
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
FIGHTS, SEEDS, EVERY = 1500, (1, 2), 5
PRICE_TEXT = "1 gold the first time, 5 the second, then 5 more each time up to 50"


def levels_from(level):
    return sorted({level, 60} | {L for L in range(((level // EVERY) + 1) * EVERY, 61, EVERY)})


def own_at(have, path, L):
    """The character's build at level L: its talents now plus its path's points taken by then."""
    out = dict(have)
    for Lp, n in path:
        if Lp <= L:
            out[n] = out.get(n, 0) + 1
    return {n: k for n, k in out.items() if k}


def check(cls, rot, have, path, page_at, level, kills_at, min_minutes=20.0, fights=FIGHTS, seeds=SEEDS, workers=4):
    """-> {"levels", "own": {L: s}, "page": {L: s}, "minutes", "pays", "build"} (seconds a kill, the fight lab's); page_at(L) -> the page's
    {talent: ranks} at L; kills_at(L) -> kills in level L."""
    sys.path.insert(0, str(HERE))
    import next_talents as NT
    levels = levels_from(level)
    jobs, keys = [], []
    for L in levels:
        for who, alloc in (("own", own_at(have, path, L)), ("page", {n: k for n, k in page_at(L).items() if k})):
            for s in seeds:
                jobs.append((cls, rot, tuple(sorted(alloc.items())), L, fights, s))
                keys.append((who, L))
    if workers > 1:
        with CF.ProcessPoolExecutor(max_workers=workers) as ex:
            times = list(ex.map(NT._ttk, jobs))
    else:
        times = [NT._ttk(j) for j in jobs]
    acc = {}
    for k, t in zip(keys, times):
        acc.setdefault(k, []).append(t)
    own = {L: sum(acc[("own", L)]) / len(seeds) for L in levels}
    page = {L: sum(acc[("page", L)]) / len(seeds) for L in levels}

    def interp(d, L):
        lo = max(x for x in levels if x <= L)
        hi = min(x for x in levels if x >= L)
        return d[lo] if hi == lo else d[lo] + (d[hi] - d[lo]) * (L - lo) / (hi - lo)
    minutes = sum(kills_at(L) * (interp(own, L) - interp(page, L)) for L in range(level, 60)) / 60
    return {"levels": levels, "own": {L: round(v, 2) for L, v in own.items()}, "page": {L: round(v, 2) for L, v in page.items()},
            "minutes": round(minutes, 1), "pays": minutes >= min_minutes and page[level] < own[level],
            "build": {n: k for n, k in page_at(level).items() if k}, "fights": fights, "seeds": list(seeds)}


def text(r, level):
    """The planner's line: the respec when it pays, else one sentence saying why not (the audit session, 2026-11-20: the character
    asked, so the page says so); None without a check."""
    if not r:
        return None
    if not r.get("pays"):
        if r["minutes"] <= 0 or r["page"][level] >= r["own"][level]:
            return ("A respec to the page's order would save nothing to 60: your path is as fast or faster (the fight lab, "
                    f"{r['page'][level]:.1f} against your {r['own'][level]:.1f} s a kill at {level}).")
        return (f"A respec to the page's order would save about {r['minutes']:.0f} minutes of killing to 60 ({r['page'][level]:.1f} against "
                f"your path's {r['own'][level]:.1f} s a kill at {level}, the gap closing as your points fill in): not worth it.")
    L1 = next((L for L in r["levels"] if L > level), None)
    ahead = f", {r['page'][L1]:.1f} against {r['own'][L1]:.1f} at {L1}" if L1 else ""
    return (f"**A respec pays:** the page's build at level {level} kills in {r['page'][level]:.1f} s against your path's "
            f"{r['own'][level]:.1f}{ahead}, about {r['minutes']:.0f} minutes of killing saved over the levels to 60 (the fight lab, "
            f"{r['fights']:,} fights on seeds {' and '.join(map(str, r['seeds']))}). A respec at your class trainer costs {PRICE_TEXT}: "
            "then take the page's order from where it is.")


if __name__ == "__main__":
    import plan as P
    name = sys.argv[1]
    cfg = P.load_cfg(name) if hasattr(P, "load_cfg") else json.load(open(ROOT / "_characters" / name / "character.json", encoding="utf-8"))
    print("use plan.py: the check runs inside the planner's talent step (plan.talents_check)")
