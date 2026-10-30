"""Known positives: builds the open searches must find or beat (2026-10-05, user request: the search silently lost the 16/11/24 hunter
for two runs before anyone noticed).

    python _reference/data/raidsim/search_check.py [classes] [--write]

For each positive in raidsim/known-positives.json, the open search's record for its class and entry (raidsim/families/<class>.json) or
rotation (fightlab/open/<class>.json) is read, and the record's winner is raced against the positive on the same seed: raid, 30,000
fights in a full raid under the entry's rotation; leveling, levels 20-60 with 3,000 fights per level, the positive given the scorer's
leveling order under the rotation's model (fl_talent_opt.order_of). PASS: the winner is within 0.5% of the positive (raid DPS) or at
most 0.5% slower (leveling seconds per kill). FAIL: the search lost a build it once found; fix the search before trusting its run. SKIP:
no record yet. A clean test runs the search without the positives first (`family_search.py <class> --entry <entry> --no-known --fresh`,
`fl_open_search.py <class> --rotation <rotation> --no-known --fresh`), then this check. --write: _reference/search-check.md (generated).
"""
import argparse
import datetime
import importlib.util
import json
import multiprocessing
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data/fightlab"), str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data")]
import fl_talent_opt as FT  # noqa: E402  (imports fightlab/run.py as `run`; the raid side loads its run.py under another name)
import paths  # noqa: E402
import render_start_here as RSH  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MLT = _load("ml_talents_check", HERE / "ml_talents.py")
R = MLT.R
KNOWN = HERE / "known-positives.json"
PAGE = ROOT / "_reference" / "search-check.md"
TODAY = datetime.date.today().isoformat()
TOL = 0.005


def flat_of(alloc):
    return {n: r for items in alloc.values() for n, r in items if r}


def positive_alloc(p):
    if p.get("build"):
        data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", p["class"]), encoding="utf-8"))["builds"]}
        return R.alloc_of(data[p["build"]]) if p["build"] in data else None
    return {n: r for n, r in (p.get("allocation") or {}).items() if r}


def stale(cls, pos):
    """Talents of a positive the current trees no longer have (2026-10-30: the Frostfire positive's Piercing Ice, removed in 70425,
    made run.py exit and the whole check fail): reported as STALE instead of stopping the check."""
    return sorted(set(pos) - set(MLT.Space(cls, "any", any_split=True).names))


def check_raid(p, repo):
    rp = HERE / "families" / f"{p['class']}.json"
    if not rp.exists():
        return {"status": "SKIP", "why": "no record"}
    e = json.load(open(rp, encoding="utf-8")).get("entries", {}).get(p["entry"]) or {}
    w = (e.get("again") or e.get("first") or {}).get("winner")
    if not w:
        return {"status": "SKIP", "why": "no winner for the entry yet"}
    pos = positive_alloc(p)
    if not pos:
        return {"status": "SKIP", "why": "the positive's build is missing"}
    if stale(p["class"], pos):
        return {"status": "STALE", "why": "talents the trees no longer have: " + ", ".join(stale(p["class"], pos)) + "; repair the positive"}
    sim = MLT.Sim(p["class"], p["entry"], "raid", None, repo, f"check-{p['class']}")
    (wd, _), (pd, _) = sim.run([flat_of(w["allocation"]), pos], 30000, 47)
    gap = wd / pd - 1 if pd else 0.0
    sp = MLT.Space(p["class"], "any", any_split=True)
    return {"status": "PASS" if gap >= -TOL else "FAIL", "winner": sp.split(flat_of(w["allocation"])), "winner_score": round(wd, 1),
            "positive_score": round(pd, 1), "gap": round(gap, 4), "unit": "DPS, full raid, 30,000 fights"}


def check_leveling(p, pool):
    rp = ROOT / "_reference/data/fightlab/open" / f"{p['class']}.json"
    if not rp.exists():
        return {"status": "SKIP", "why": "no record"}
    r = json.load(open(rp, encoding="utf-8")).get("rotations", {}).get(p["rotation"]) or {}
    if not r.get("winner") or not r.get("order"):
        return {"status": "SKIP", "why": "no winner for the rotation yet"}
    pos = positive_alloc(p)
    if not pos:
        return {"status": "SKIP", "why": "the positive's build is missing"}
    if stale(p["class"], pos):
        return {"status": "STALE", "why": "talents the trees no longer have: " + ", ".join(stale(p["class"], pos)) + "; repair the positive"}
    sp = MLT.Space(p["class"], "any", any_split=True)
    pb = {"id": "positive", "allocation": {t: [[n, pos[n]] for n in sp.by_tree[t] if pos.get(n)] for t in sp.tree_names},
          "order": FT.order_of(p["class"], r["model"], pos)}
    wb = {"id": "winner", "allocation": r["winner"]["allocation"], "order": r["order"]}
    (ww, _), (pw, _) = FT.race(pool, p["class"], p["rotation"], [wb, pb], 3000, 3)
    gap = ww / pw - 1 if pw else 0.0   # positive = the winner is slower
    return {"status": "PASS" if gap <= TOL else "FAIL", "winner": sp.split(flat_of(r["winner"]["allocation"])), "winner_score": round(ww, 2),
            "positive_score": round(pw, 2), "gap": round(gap, 4), "unit": "seconds per kill, levels 20-60 (lower is better)"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 4) - 2))
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    pos = [p for p in json.load(open(KNOWN, encoding="utf-8")).get("positives", []) if not a.classes or p["class"] in a.classes]
    rows = []
    pool = None
    for p in pos:
        if p.get("kind") == "leveling":
            if pool is None:
                pool = multiprocessing.Pool(a.jobs, initializer=FT._init, initargs=("greens",))
            res = check_leveling(p, pool)
        else:
            res = check_raid(p, repo)
        rows.append(dict(p, **res))
        print(f"{res['status']:4} {p['class']:8} {p.get('kind', 'raid'):8} {p.get('entry') or p.get('rotation'):18} {p['name']}"
              + (f": winner {res['winner']} {res['winner_score']} vs positive {res['positive_score']} ({res['gap']:+.2%})" if "gap" in res else f": {res['why']}"), flush=True)
    if pool:
        pool.close()
    if a.write:
        o = ["# Open search check against the known positives (generated)", "",
             f"> Generated by `_reference/data/raidsim/search_check.py` on {TODAY}. Do not hand-edit.", "",
             "Builds the open searches once found and an earlier search missed (`raidsim/known-positives.json`), each raced against the "
             "current record's winner on the same seed. A FAIL means the search lost a build it once found.", "",
             "| Status | Class | Kind | Entry or rotation | Known positive | Record's winner | Winner | Positive | Gap |", "|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            o.append(f"| {r['status']} | {r['class']} | {r.get('kind', 'raid')} | {r.get('entry') or r.get('rotation')} | {r['name']} | "
                     + (f"{r['winner']} | {r['winner_score']} | {r['positive_score']} | {r['gap']:+.2%} |" if "gap" in r else f"- | - | - | {r['why']} |"))
        PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
        print(f"wrote {PAGE.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
