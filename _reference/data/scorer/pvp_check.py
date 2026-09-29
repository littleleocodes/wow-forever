"""How close the scorer's PvP optimum lands to the PvP builds: the Classic community builds (the calibration cases) and the
Forever hand drafts (checked against the calibrated weights).

    python _reference/data/scorer/pvp_check.py [--game classic-era|forever] [--set burst=0.5 --set stun=4 ...] [--grid] [--write]

The PvP profile (profiles.json "pvp") scores burst damage (or healing), survival, mana and control / escape / stealth with its
`pvp_weights` and `kind_weights`, taking every effect that applies in solo-60 plus the ones tagged pvp. A case's overlap is the
share of the 51 points the optimized build and the reference build have in common (the sum over talents of the smaller rank).
`--set` overrides a weight for this run (burst, surv, mana, utility are pvp_weights; kite, stun, stick, move, range, stealth, avoid are
kind_weights); `--grid` searches a small grid of them for the best mean overlap on the Classic cases; `--write` stores the
chosen weights in profiles.json (with --grid) and writes _reference/pvp-check.md.
"""
import argparse
import itertools
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

# (class, spec model, reference build id): the model whose damage or healing sources fit the build's playstyle
CASES = {
    "classic-era": [("druid", "resto-heal", "pvp-resto-feral-hybrid"), ("hunter", "mm-raid", "pvp-mm-surv"), ("mage", "frost-leveling", "pvp-frost"),
                    ("paladin", "holy-heal", "pvp-shockadin"), ("priest", "shadow-dps", "pvp-shadow"), ("rogue", "combat-daggers-raid", "pvp-seal-fate-daggers"),
                    ("rogue", "combat-swords-raid", "pvp-hemo-prep"), ("shaman", "elemental-dps", "pvp-elemental-ns"), ("warlock", "affliction-leveling", "pvp-soul-link"),
                    ("warrior", "arms-2h-raid", "arms-pvp")],
    "forever": [("druid", "resto-heal", "pvp-resto"), ("hunter", "mm-raid", "pvp-mm-surv"), ("mage", "frost-leveling", "pvp-frost"),
                ("paladin", "holy-heal", "pvp-shockadin"), ("priest", "shadow-dps", "shadow-pvp"), ("rogue", "combat-daggers-raid", "pvp-seal-fate-daggers"),
                ("rogue", "combat-swords-raid", "pvp-hemo-prep"), ("shaman", "elemental-dps", "pvp-elemental-ns"), ("warlock", "affliction-leveling", "pvp-soul-link"),
                ("warrior", "arms-2h-raid", "arms-pvp")],
}
PVP_KEYS = ("burst", "surv", "mana", "utility")
KIND_KEYS = ("kite", "stun", "stick", "move", "range", "stealth", "avoid")


def builds_path(game, cls):
    return ROOT / cls / ("research/talents/classic-baseline/builds.json" if game == "classic-era" else "research/talents/forever/proposed-builds.json")


def reference(game, cls, bid):
    for b in json.load(open(builds_path(game, cls), encoding="utf-8"))["builds"]:
        if b["id"] == bid:
            return {n: r for items in b["allocation"].values() for n, r in items}
    raise KeyError(bid)


def overlap(a, b):
    return sum(min(r, b.get(n, 0)) for n, r in a.items()) / max(1, sum(b.values()))


def run_case(args):
    game, cls, spec, ref_id, sets = args
    from optimize import Optimizer
    opt = Optimizer(game, cls, spec, "pvp")
    for k, v in sets.items():
        (opt.profile.setdefault("pvp_weights", {}) if k in PVP_KEYS else opt.profile.setdefault("kind_weights", {}))[k] = v
    opt._ev.clear()
    opt._cache.clear()
    ref = reference(game, cls, ref_id)
    best, s = opt.best_build(60)
    best = {n: r for n, r in best.items() if r}
    split = "/".join(str(sum(r for n, r in best.items() if opt.tree.info[n][0] == t)) for t in opt.tree.order)
    rsplit = "/".join(str(sum(r for n, r in ref.items() if opt.tree.info[n][0] == t)) for t in opt.tree.order)
    ref_s = opt.score(ref, 60)
    missing = sorted((n, r - best.get(n, 0)) for n, r in ref.items() if best.get(n, 0) < r)
    extra = sorted((n, r - ref.get(n, 0)) for n, r in best.items() if ref.get(n, 0) < r)
    return {"game": game, "cls": cls, "spec": spec, "ref": ref_id, "overlap": overlap(best, ref), "split": split, "ref_split": rsplit,
            "score": s, "ref_score": ref_s, "missing": missing, "extra": extra, "best": best}


def run_all(game, sets, jobs):
    todo = [(game, cls, spec, ref, sets) for cls, spec, ref in CASES[game]]
    with ProcessPoolExecutor(max_workers=jobs) as ex:
        return list(ex.map(run_case, todo))


def show(rows, title):
    print(f"\n== {title}: mean overlap {sum(r['overlap'] for r in rows) / len(rows):.0%}")
    for r in rows:
        print(f"{r['cls']:8s} {r['spec']:20s} vs {r['ref']:24s} {r['ref_split']:>8s} -> {r['split']:>8s}  overlap {r['overlap']:4.0%}  "
              f"(reference scores {r['ref_score'] * 100:+.1f}% vs optimum {r['score'] * 100:+.1f}%)")
        if r["missing"]:
            print("      reference has more: " + ", ".join(f"{n} +{d}" for n, d in r["missing"]))
        if r["extra"]:
            print("      optimum has more:   " + ", ".join(f"{n} +{d}" for n, d in r["extra"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--game", default="classic-era", choices=list(CASES))
    ap.add_argument("--set", action="append", default=[], help="weight=value")
    ap.add_argument("--grid", action="store_true")
    ap.add_argument("--grid-values", help='JSON {"burst": [...], "surv": [...], "utility": [...], "mana": [...]} (default: a coarse 8-point grid)')
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    sets = {k: float(v) for k, v in (x.split("=", 1) for x in a.set)}
    if a.grid:
        grid = json.loads(a.grid_values) if a.grid_values else {"burst": [0.4, 0.8], "surv": [0.2, 0.5], "utility": [0.7, 1.5], "mana": [0.05]}
        results = []
        for burst, surv, util, mana in itertools.product(grid["burst"], grid["surv"], grid["utility"], grid["mana"]):
            s = dict(sets, burst=burst, surv=surv, utility=util, mana=mana)
            rows = run_all("classic-era", s, a.jobs)
            mean = sum(r["overlap"] for r in rows) / len(rows)
            results.append((mean, s))
            print(f"burst {burst} surv {surv} utility {util} mana {mana}: mean overlap {mean:.1%}", flush=True)
        results.sort(key=lambda x: -x[0])
        best_mean, best_sets = results[0]
        print(f"\nbest: {best_sets} ({best_mean:.1%})")
        sets = best_sets
        if a.write:
            from fmt_json import dumps
            p = HERE / "profiles.json"
            prof = json.load(open(p, encoding="utf-8"))
            for k, v in sets.items():
                (prof["pvp"]["pvp_weights"] if k in PVP_KEYS else prof["pvp"]["kind_weights"])[k] = v
            p.write_text(dumps(prof) + "\n", encoding="utf-8")
            print("wrote the weights into profiles.json")
    rows_c = run_all("classic-era", sets, a.jobs)
    show(rows_c, "Classic Era community PvP builds (calibration cases)")
    rows_f = run_all("forever", sets, a.jobs)
    show(rows_f, "Forever PvP hand drafts (checks)")
    if a.write:
        write_page(rows_c, rows_f)


def write_page(rows_c, rows_f):
    prof = json.load(open(HERE / "profiles.json", encoding="utf-8"))["pvp"]
    lines = ["# PvP check", "",
             "> Generated by `_reference/data/scorer/pvp_check.py --write`. The scorer's PvP profile (`profiles.json` \"pvp\") against the PvP builds: the Classic",
             "> community builds are the calibration cases, the Forever hand drafts are checked against the same weights. Overlap = share of the 51 points both builds",
             "> spend the same way. The PvP weights are assumptions tuned to these cases, not measurements (no simulator plays PvP).", "",
             f"Weights: burst {prof['pvp_weights']['burst']}, survival {prof['pvp_weights']['surv']}, mana {prof['pvp_weights']['mana']}; kinds " +
             ", ".join(f"{k} {v}" for k, v in prof["kind_weights"].items()) + ".", ""]
    for title, rows in (("Classic Era community builds", rows_c), ("Forever hand drafts", rows_f)):
        lines += [f"## {title}", "", f"Mean overlap {sum(r['overlap'] for r in rows) / len(rows):.0%}.", "",
                  "| Class | Model | Build | Build split | Optimum | Overlap | Build lacks | Optimum lacks |", "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            lines.append(f"| {r['cls']} | {r['spec']} | {r['ref']} | {r['ref_split']} | {r['split']} | {r['overlap']:.0%} | "
                         + ", ".join(f"{n} +{d}" for n, d in r["extra"]) + " | " + ", ".join(f"{n} +{d}" for n, d in r["missing"]) + " |")
        lines.append("")
    lines += ["---", "*Generated file — do not edit by hand.*", ""]
    (ROOT / "_reference" / "pvp-check.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote _reference/pvp-check.md")
    # the same rows per class, in <class>/research/pvp/README.md
    sys.path.append(str(ROOT / "_reference/data"))
    import paths
    import readme_sections as rs
    for cls in sorted({r["cls"] for r in rows_c + rows_f}):
        readme = paths.scenario_readme(cls, "pvp")
        sec = ["## PvP check", "",
               f"The stats model's PvP profile (burst {prof['pvp_weights']['burst']}, survival {prof['pvp_weights']['surv']}, mana {prof['pvp_weights']['mana']}, "
               f"utility {prof['pvp_weights'].get('utility', 1.0)}; tuned on the Classic community PvP builds) against this class's PvP builds: overlap = the share of "
               "the 51 points the build and the model's PvP optimum spend the same way. The weights are assumptions (no simulator plays PvP); the rows the model "
               f"cannot judge well are named in [`_reference/pvp-check.md`]({paths.rel(readme, ROOT / '_reference/pvp-check.md')}). Generated by "
               "`_reference/data/scorer/pvp_check.py --write`.", "",
               "| Game | Build | Model | Build split | Optimum | Overlap | Build lacks | Optimum lacks |", "|---|---|---|---|---|---|---|---|"]
        for game, rows in (("Forever", rows_f), ("Classic Era", rows_c)):
            for r in rows:
                if r["cls"] != cls:
                    continue
                sec.append(f"| {game} | {r['ref']} | {r['spec']} | {r['ref_split']} | {r['split']} | {r['overlap']:.0%} | "
                           + ", ".join(f"{n} +{d}" for n, d in r["extra"]) + " | " + ", ".join(f"{n} +{d}" for n, d in r["missing"]) + " |")
        rs.splice_ordered(readme, "pvp", "## PvP check", "\n".join(sec))
    print("wrote the PvP check section of every <class>/research/pvp/README.md")


if __name__ == "__main__":
    main()
