"""The PvP search queue (2026-11-15, _reference/pvp-plan.md step 4): pvp_search.search for every class and talent tree that has a PvP
build of ours, started from our PvP builds of the tree, the community's PvP builds that lead in it (pvp-community-builds.json) and the
expansion seed (pvp_seeds.py: the TBC and WotLK PvP builds' consensus talents). The duels play the dropped-veto audit's kept vetoes
(duel.restored_vetoes reads veto-audit.json). One tree at a time. A tree whose record (duellab/search/<class>-<tree>.json) carries this
round is skipped, so the same command resumes. The worker count is read before each tree from --workers-file (default 2), so a change
of CPU mode reaches the next tree.

    python _reference/data/duellab/pvp_search_all.py [classes] [--round 2026-11-15] [--workers-file F] [--dry-run]
"""
import argparse
import json
import os
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path.insert(0, str(HERE))
import duel_run as DR  # noqa: E402
import pvp_search as PS  # noqa: E402
import pvp_seeds as SD  # noqa: E402

OUT = HERE / "search"


def lead_tree(trees, alloc):
    pts = {t: sum(alloc.get(n, 0) for n in tr["talents"]) for t, tr in trees.items()}
    return max(pts, key=pts.get)


def starts_for(cls, trees):
    """{tree: [refs]}: ours (proposed-builds, content pvp), the community's PvP builds, the expansion seed."""
    out = {}
    data = json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))
    for b in data["builds"]:
        if b.get("content") != "pvp":
            continue
        alloc = DR.load_build(cls, b["id"])[1]
        tree = b.get("spec") if b.get("spec") in trees else lead_tree(trees, alloc)
        out.setdefault(tree, []).append(b["id"])
    cb = json.load(open(DATA / "pvp-community-builds.json", encoding="utf-8"))
    for b in cb["builds"]:
        if b.get("class") != cls or b.get("for", "pvp") not in ("pvp", "duel"):   # duel: the warlock's Soul Link field build
            continue
        ref = f"community:{b['key']}"
        try:
            alloc = DR.load_build(cls, ref)[1]
        except SystemExit:
            continue
        tree = lead_tree(trees, alloc)
        if tree in out:
            out[tree].append(ref)
    for tree in out:
        p = SD.SEEDS / f"{cls}-{SD.slug(tree)}.json"
        if p.exists():
            out[tree].append(p.relative_to(ROOT).as_posix())   # relative: the queue runs from the repository root
        # round 2 (2026-11-17, round2_seeds.py): the round-1 winner, the blind-spot check's improved build and battleground version,
        # and a signature put-back where the winner lacked its tree's signature talent
        for q in sorted((SD.SEEDS / "r2").glob(f"{cls}-{SD.slug(tree)}-*.json")):
            out[tree].append(q.relative_to(ROOT).as_posix())
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--round", default=time.strftime("%Y-%m-%d"))
    ap.add_argument("--workers-file", default=str(DATA / "deep-runs" / "pvp1115" / "workers"))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--batch", type=int, default=48)
    ap.add_argument("--n-screen", type=int, default=40)
    ap.add_argument("--n-confirm", type=int, default=120)
    ap.add_argument("--out", default=str(OUT), help="records folder (a smoke test writes elsewhere)")
    a = ap.parse_args()
    out_dir = pathlib.Path(a.out).resolve()
    os.chdir(ROOT)   # build refs to seed files are relative to the repository root (duel_run.load_build opens them as given)
    TO, VB = PS.talent_opt()
    F = VB.load_forever()
    out_dir.mkdir(parents=True, exist_ok=True)
    for cls in sorted(F):
        if a.classes and cls not in a.classes:
            continue
        for attempt in range(6):   # a leveling lane may be rewriting the class's proposed-builds.json (2026-11-15): read it again
            try:
                starts = starts_for(cls, F[cls])
                break
            except json.JSONDecodeError:
                if attempt == 5:
                    raise
                time.sleep(5)
        for tree, refs in sorted(starts.items(), key=lambda kv: list(F[cls]).index(kv[0])):
            path = out_dir / f"{cls}-{tree.lower().replace(' ', '-')}.json"
            if path.exists() and json.load(open(path, encoding="utf-8")).get("round") == a.round:
                print(f"== {cls} {tree}: done in this round", flush=True)
                continue
            try:
                workers = max(1, int(open(a.workers_file).read().strip()))
            except (OSError, ValueError):
                workers = 2
            print(f"== {time.strftime('%H:%M')} {cls} {tree}: starts {', '.join(pathlib.Path(r).name for r in refs)}; {workers} workers",
                  flush=True)
            if a.dry_run:
                continue
            t0 = time.time()
            rec = PS.search(cls, refs, tree, a.steps, a.batch, a.n_screen, a.n_confirm, workers=workers,
                            log=lambda m: print(m, flush=True))
            rec["round"] = a.round
            rec["minutes"] = round((time.time() - t0) / 60, 1)
            path.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
            race = ", ".join(f"{pathlib.Path(k).name} {v['win']:.1%} (J {v['J']:.3f})" for k, v in rec["race"].items())
            print(f"== {cls} {tree}: final win {rec['win']:.1%}, J {rec['J']:.3f} in {rec['minutes']} min; race: {race}", flush=True)


if __name__ == "__main__":
    main()
