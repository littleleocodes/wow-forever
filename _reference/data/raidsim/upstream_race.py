"""Upstream parity (2026-11-19, the independent audit's D1-D6 and its proposed permanent check; user: "Go with the audits
recommendations"): the official simulator's own rotations for a class against each of our entries' raid rotations, in every arm:
each rotation of the entry's tree x each build (the entry's own and the simulator's presets of that tree, by their talent strings),
full raid, the entry's gear, options and consumables, the same fights, seeds 1 and 2. A gain is then the rotation's, the talents' or
the pair's. The upstream rotations are copied into raidsim/apls/<class>/upstream/ with trainer ranks (trainer_ranks.py) first.

    python _reference/data/raidsim/upstream_race.py <class> [entries] [--fights 10000] [--copy-only]

Record raidsim/upstream-race.json {class: {entry: arms, our best arm, best arm, gain}}. The warlock's build files (rotation, talents and
a demon option set each) were raced by deep-runs/warlock_upstream_race.py into raidsim/warlock-upstream-race.json.
Run it at every re-pin: an upstream arm 0.5% ahead of our best is a lead (the entry's base rotation, a build, or both).
"""
import argparse
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import trainer_ranks as TR  # noqa: E402

OUT = HERE / "upstream-race.json"
# per class and entry: the simulator's rotations of that entry's tree (ui/specs/<spec dir>/apls/<file>) and its presets' talents
# (presets.ts makePresetTalents), each pair as presets.ts makes its build
CONFIG = {
    "mage": {"dir": "ui/specs/mage/dps", "entries": {
        "arcane-dps": {"rots": ["arcane", "arcaneFireFill"],
                       "builds": {"Arcane": "050205223101311531-5500003-003", "Arcane Fire": "050205203100311531-525000012001-003"}},
        "fire-raid": {"rots": ["deepFire"], "builds": {"Fire": "0502052001001-55500001230133031-003"}},
        "frost-raid": {"rots": ["frost"], "builds": {"Frost Incin": "203205-5-053500011121331251",
                                                     "Frost Med": "2032250100003--053500001121331251"}},
        "frostfire-raid": {"rots": ["ffb"], "builds": {"FFB": "-5550000123011303-2035010311013002"}}}},
    # the entry's base is upstream's adaptive rotation read from the checkout; our raid rotation was tuned from an older version of it
    # (the audit's D6: today's adaptive +0.9% on feral-combat-open-raid)
    "druid": {"dir": "ui/specs/druid/feralcat", "entries": {
        "feral-cat-dps": {"rots": ["adaptive"], "builds": {"Cat": "050021-53200032123012125001-055",
                                                           "Hybrid": "050012-50230302123110125011-055"}}}},
}


def copy_rotations(cls, repo_src):
    """The class's upstream rotations into apls/<class>/upstream/, book ranks swapped (one mapping: trainer-ranks.json)."""
    cfg = CONFIG[cls]
    dst = HERE / "apls" / cls / "upstream"
    dst.mkdir(parents=True, exist_ok=True)
    mp = TR.load_map()
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in mp.items()}
    commit = subprocess.run(["git", "-C", str(repo_src), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    names = sorted({r for e in cfg["entries"].values() for r in e["rots"]})
    for n in names:
        src = pathlib.Path(repo_src) / cfg["dir"] / "apls" / f"{n}.apl.json"
        text = TR.swap_text(json.dumps(json.loads(src.read_text(encoding="utf-8")), indent=1) + "\n", fwd)
        (dst / f"{n}.apl.json").write_text(text, encoding="utf-8", newline="")
    readme = dst / "README.md"
    if not readme.exists():
        readme.write_text(f"# Upstream {cls} rotations\n\nThe official wowsims/forever simulator's own {cls} rotations at {commit} "
                          f"(`{cfg['dir']}/apls/`), copied on 2026-11-19 for the independent audit's upstream-parity check "
                          "(`raidsim/upstream_race.py`). Book ranks swapped to trainer ranks (`trainer_ranks.py`). An entry that adopts one "
                          "takes it as its base (`apl`) and tunes from there.\n", encoding="utf-8")
    return {n: dst / f"{n}.apl.json" for n in names}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("entries", nargs="*")
    ap.add_argument("--fights", type=int, default=10000)
    ap.add_argument("--copy-only", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    src = pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever"
    files = copy_rotations(a.cls, src)
    if a.copy_only:
        print("copied:", ", ".join(str(f.relative_to(ROOT)) for f in files.values()))
        return
    trees = R.load_trees(repo, a.cls)
    ours = {b["id"]: b for b in json.load(open(ROOT / a.cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    cfg = CONFIG[a.cls]["entries"]
    for e in a.entries or list(cfg):
        entry = R.SPECS[a.cls][e]
        rots = {"ours": str(R.apl_path(entry, repo, "raid"))}
        rots.update({n: str(files[n]) for n in cfg[e]["rots"]})
        builds = {}
        for bid in entry.get("builds", []):
            b = ours.get(bid)
            if b:
                builds[bid] = R.talents_string(trees, {n: r for items in b["allocation"].values() for n, r in items if r})
        for n, t in cfg[e]["builds"].items():
            if t not in builds.values():
                builds[f"up:{n}"] = t
        print(f"== {a.cls} {e}: rotations {list(rots)}, builds {list(builds)}", flush=True)
        bl = [{"label": f"{rn}|{bn}", "talents": t, "apl": rp} for rn, rp in rots.items() for bn, t in builds.items()]
        res = {}
        for seed in (1, 2):
            rows = A.bench(entry, repo, bl, a.fights, seed, "raid", f"upr-{a.cls}-{e}")
            for lab, row in rows.items():
                res.setdefault(lab, {})[str(seed)] = round(row.get("dps") or 0.0, 2)
        mean = {lab: sum(v.values()) / len(v) for lab, v in res.items() if len(v) == 2}
        our_best = max((lab for lab in mean if lab.startswith("ours|") and not lab.startswith("ours|up:")), key=mean.get)
        best = max(mean, key=mean.get)
        rec.setdefault(a.cls, {})[e] = {"fights": a.fights, "rotations": {k: str(pathlib.Path(v).resolve().relative_to(ROOT)) if str(v).startswith(str(ROOT)) else v
                                                                          for k, v in rots.items()},
                                         "builds": builds, "dps": res, "our_best": our_best, "best": best,
                                         "gain": round(mean[best] / mean[our_best] - 1, 4)}
        for lab in sorted(mean, key=mean.get, reverse=True)[:10]:
            print(f"   {lab:58s} {res[lab]['1']:8.1f} {res[lab]['2']:8.1f}", flush=True)
        print(f"   ours: {our_best} {mean[our_best]:.1f}; best: {best} {mean[best]:.1f} ({rec[a.cls][e]['gain']:+.2%})", flush=True)
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
