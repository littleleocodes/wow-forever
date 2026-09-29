"""Talent pick rates on talentsforever.com against our builds (2026-09-29, user request: "did you look at the pick rate of the talents?").

    python _reference/data/popular_picks.py [classes] [--high 70] [--low 20] [--write]

talentsforever.com's popular.js (archived by popular_builds.py) carries, per class, the share of the builds made on the site that
take each talent (`pick`, the "pick rate" tick box on the class page) and the same split by the tree the build leads in (`pickBy`,
with `specN` builds behind each). For every Forever build of ours the lead tree (most points) picks the comparison group, and the
page lists

  consensus we skip   talents at least --high % of that group take and our build does not
  ours, rarely taken  talents our build takes that at most --low % of that group take

each with the scorer's value in the build's own scenario (scenario_audit.model_profile: the spec model and profile its id or the
pipeline names): for a talent we take, the share of the build's score lost without it; for one we skip, the share gained by adding its
full ranks on top (points over 51, a screen, not a legal build) next to the per-point value of the weakest talent we take (what the
points would come from). The scorer is calibrated to the simulators where they measure a talent; a talent the labs cannot see keeps
its hand value. Screen only: a swap is decided by a race (raidsim/run.py, fightlab/run.py), never by pick rates.
Writes `_reference/popular-picks.md` (generated) with --write.
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE / "scorer"))
sys.path.insert(0, str(HERE))
import scenario_audit as sa   # noqa: E402
from popular_builds import latest_raw, load_popular   # noqa: E402

CLASSES = sa.CLASSES
OUT = ROOT / "_reference/popular-picks.md"


def flat(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def lead_tree(b):
    return max(b["allocation"], key=lambda t: sum(r for _, r in b["allocation"][t]))


def analyse(cls, pop, a, opt_cache):
    from optimize import Optimizer
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    pc = pop["classes"][cls.capitalize()]
    rate = {}   # lead tree -> talent -> pick %
    tree_of = {}
    for lead, per_tree in pc["pickBy"].items():
        for tr, picks in zip(data["trees"], per_tree):
            for t, p in zip(tr["talents"], picks):
                rate.setdefault(lead, {})[t["name"]] = p
                tree_of[t["name"]] = (tr["name"], t["maxRank"])
    models = list(json.load(open(HERE / "scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"])
    rows = []
    for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]:
        lead = lead_tree(b)
        if lead not in rate:
            continue
        model, profile = sa.model_profile(cls, b, models)
        opt = None
        if model:
            key = (cls, model, profile)   # model names repeat across classes (holy-heal: paladin and priest)
            if key not in opt_cache:
                try:
                    opt_cache[key] = Optimizer("forever", cls, model, profile)
                except Exception as ex:  # noqa: BLE001
                    opt_cache[key] = ex
            opt = opt_cache[key] if not isinstance(opt_cache[key], Exception) else None
        al = flat(b["allocation"])
        base = opt.score(al, 60) if opt else None

        def removal(n):   # share of the build's score lost without the talent
            return (base - opt.score({k: v for k, v in al.items() if k != n}, 60)) / abs(base) if opt and base else None

        def addition(n):  # share gained with the talent's full ranks added on top
            return (opt.score(dict(al, **{n: tree_of[n][1]}), 60) - base) / abs(base) if opt and base else None
        per_point = sorted(((removal(n) or 0) / r, n) for n, r in al.items() if opt and not needed(opt, al, n))
        skipped = [(n, p, addition(n), addition(n) / tree_of[n][1] if opt and base else None)
                   for n, p in rate[lead].items() if p >= a.high and n not in al]
        rare = [(n, rate[lead].get(n, 0), al[n], removal(n)) for n in al if rate[lead].get(n, 0) <= a.low]
        rows.append({"id": b["id"], "content": b.get("content"), "lead": lead, "n": pc["specN"].get(lead), "model": model, "profile": profile,
                     "skipped": sorted(skipped, key=lambda x: -x[1]), "rare": sorted(rare, key=lambda x: x[1]),
                     "weakest": per_point[0] if per_point else None})
    return rows


def needed(opt, al, n):
    return not opt.tree.legal({k: v for k, v in al.items() if k != n})


def pct(x, digits=1):
    return "-" if x is None else f"{x * 100:+.{digits}f}%"


def swaps_section():
    """The races of popular_swaps.py: every consensus talent swapped into our ranked builds, against the unchanged build."""
    p = HERE / "popular-swaps.json"
    if not p.exists():
        return []
    sw = json.load(open(p, encoding="utf-8"))
    tested, untested = [], []
    for cls, parts in sw["classes"].items():
        for part, rows in parts.items():
            for r in rows:
                (tested if r.get("change") else untested).append((cls, r))

    def key(x):   # best gain first: raid by the dummy (the ranking setting; tanks by tank value), leveling by time per kill
        r = x[1]
        if r["scenario"] == "leveling":
            return r["delta"] if r.get("delta") is not None else 9
        d = (r.get("raid" if r.get("tank") else "dummy") or {}).get("delta")
        return -d if d is not None else 9
    o = [f"## Races: the consensus talents swapped into our builds ({sw['date']})", "",
         f"`popular_swaps.py`: every talent that at least {sw['high']}% of the site's builds in the same lead tree take and one of our ranked builds "
         "skips, swapped in at full ranks (points taken back where the scorer loses least, every step legal), raced against the unchanged build. "
         "Raid: the community simulator, same seed, 20,000 iterations; tanks by tank value in the raid setting. Leveling: the fight lab at levels "
         "20-60, level-weighted time per kill, both builds on the scorer's leveling order (so the base can differ from its page). Positive raid "
         "change = the swap does more; negative leveling change = the swap kills faster. Raid differences under about 0.3% and leveling ones under "
         "about 1% are noise.", "",
         "| Class | Scenario | Our build | Talent (pick) | Swap | Dummy | Raid | Leveling |", "|---|---|---|---|---|---|---|---|"]
    for cls, r in sorted(tested, key=key):
        if r["scenario"] == "leveling":
            cells = ["-", "-", pct(r.get("delta"))]
        elif r.get("tank"):
            cells = ["-", pct((r.get("raid") or {}).get("delta")) + " (tank value)", "-"]
        else:
            cells = [pct((r.get("dummy") or {}).get("delta")), pct((r.get("raid") or {}).get("delta")), "-"]
        o.append(f"| {cls} | {r['scenario']}{' (' + r['entry'] + ')' if r.get('entry') else ''} | `{r['build']}` | {r['talent']} ({r['pick']}%) | "
                 f"{r['change']} | " + " | ".join(cells) + " |")
    if sw.get("checks"):
        o += ["", f"Second and third seeds for the swaps that cleared noise ({sw.get('checks_note', '')}):", "",
              "| Class | Build | Talent | Tool | Seed 1 | Seed 2 | Seed 3 |", "|---|---|---|---|---|---|---|"]
        o += [f"| {c['class']} | `{c['build']}` | {c['talent']} | {c['tool']} | {c['seed1']} | {c['seed2']} | {c['seed3']} |" for c in sw["checks"]]
    if untested:
        o += ["", "Not tested (the tree could not hold the talent without a larger respec): "
              + "; ".join(f"{cls} `{r['build']}` {r['talent']} ({r['pick']}%)" for cls, r in untested) + "."]
    return o + [""]


def render(res, pop, a):
    o = ["# Talent pick rates on talentsforever.com vs our builds", "",
         f"> Generated by `_reference/data/popular_picks.py` from talentsforever.com's popular.js (`{a.raw}`, updated {pop.get('updated', '?')}). "
         "Pick rate = share of the builds made on the site, among those that lead in the same tree as ours, that take the talent. Values are the "
         "scorer's in the build's own scenario (calibrated to the fight lab, the community raid simulator and the healer lab where they measure the "
         "talent). A screen, not a result: swaps are decided by races. Do not hand-edit.", "",
         f"Consensus we skip: picked by at least {a.high}% of that group. Rarely taken: picked by at most {a.low}%. *Value if added* is the score "
         "gained by adding the talent's full ranks on top of the build (points over 51), per point next to it; *weakest* is the cheapest talent the "
         "build could give up (removal value per point, gating fillers excluded), so a skipped talent whose per-point value beats it is worth a race.", ""]
    o += swaps_section()
    o += ["## The screen, build by build", ""]
    for cls in CLASSES:
        rows = res.get(cls)
        if not rows:
            continue
        o += [f"### {cls.capitalize()}", ""]
        for r in rows:
            if not r["skipped"] and not r["rare"]:
                continue
            w = r["weakest"]
            o.append(f"**`{r['id']}`** ({r['content']}, leads {r['lead']}; {r['n']:,} site builds lead there; scored as "
                     + (f"`{r['model']}` / `{r['profile']}`" if r["model"] else "no scorer model") + (f"; weakest: {w[1]} {pct(w[0], 2)} per point" if w else "") + ")")
            o.append("")
            if r["skipped"]:
                o.append("- Consensus we skip: " + "; ".join(f"{n} ({p}%, value if added {pct(v)}, {pct(pp, 2)} per point)" for n, p, v, pp in r["skipped"]))
            if r["rare"]:
                o.append("- Ours, rarely taken: " + "; ".join(f"{n} {rk} ({p}%, value {pct(v)})" for n, p, rk, v in r["rare"]))
            o.append("")
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--high", type=int, default=70)
    ap.add_argument("--low", type=int, default=20)
    ap.add_argument("--raw")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    src = HERE / "raw" / a.raw if a.raw else latest_raw()
    a.raw = str((src / "popular.js").relative_to(ROOT)).replace("\\", "/")
    pop = load_popular(src / "popular.js")
    res, cache = {}, {}
    for cls in a.classes or CLASSES:
        res[cls] = analyse(cls, pop, a, cache)
        for r in res[cls]:
            w = r["weakest"]
            print(f"{cls:<8} {r['id']:<38} lead {r['lead']:<14} weakest {w[1] + ' ' + pct(w[0], 2) if w else '-'}")
            for n, p, v, pp in r["skipped"]:
                print(f"    skip {n:<32} {p:>3}%  add {pct(v)} ({pct(pp, 2)}/pt)")
            for n, p, rk, v in r["rare"]:
                print(f"    rare {n:<32} {p:>3}%  ours {rk}, value {pct(v)}")
    if a.write:
        render(res, pop, a)


if __name__ == "__main__":
    main()
