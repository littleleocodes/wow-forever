"""Full-raid talent searches for every damage entry (2026-10-01, the lesson of the Arms miss: builds searched on the training dummy drop
talents that only pay off with raid buffs; raidsim/setting_audit.py has the measurements).

    python _reference/data/raidsim/fullraid_search.py [classes] [--jobs 3] [--write]

Per damage entry (tanks are measured in the raid setting already):
1. Starts: our best build in the full-raid setting and the best talentsforever.com popular build in that setting
   (`_reference/data/popular-race.json`, kept when within 10% of ours), each a candidate file.
2. raidsim/talent_opt.py --setting raid from each start, keeping 30+ points in the start's lead tree when it has them.
3. Head-to-head race (full raid, seed 3, 20,000 iterations): every raid build of ours in the entry against the search results; the best
   result becomes `<entry>-fullraid-parse` (derived: raid, a "parse" build: the build for a full raid) when it beats our best by 2%+
   (the user's rule), noted with its start and moves. The training-dummy pick is unchanged.
Records: `raidsim/fullraid-search.json` (resumable).
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "_reference/data/scorer"), str(ROOT / "_reference/data"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import spec_builds as SB  # noqa: E402
import setting_audit as SA  # noqa: E402  (apl_opt / run loaders)
from fmt_json import dumps  # noqa: E402

A, R = SA.A, SA.R
OUT = HERE / "fullraid-search.json"
TODAY = datetime.date.today().isoformat()
MIN_GAIN = 0.02


def lead_tree(cls, al):
    trees = json.load(open(ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]
    pts = {t["name"]: sum(al.get(x["name"], 0) for x in t["talents"]) for t in trees}
    t = max(pts, key=pts.get)
    return t if pts[t] >= SM.SPEC_POINTS else None


def plan(cls, entry):
    pop = json.load(open(ROOT / "_reference/data/popular-race.json", encoding="utf-8"))["classes"].get(cls, {}).get("raid", {}).get("rows", [])
    rows = [r for r in pop if r["entry"] == entry and r["setting"] == "raid" and r.get("dps") and not r.get("error")]
    ours = [r for r in rows if r["kind"] == "ours"]
    popular = [r for r in rows if r["kind"] == "popular"]
    if not ours:
        return []
    best = max(ours, key=lambda r: r["dps"])
    starts = [("ours", best["label"])]
    if popular:
        p = max(popular, key=lambda r: r["dps"])
        if p["dps"] >= 0.9 * best["dps"]:
            starts.append(("popular", p["label"]))
    return starts


def start_file(cls, label):
    cdir = paths.raidsim_dir(cls) / "candidates"
    if label.startswith("tf-popular-"):
        b = next(x for x in json.load(open(ROOT / "_reference/data/popular-builds.json", encoding="utf-8"))["classes"][cls]["top"] if x["id"] == label)
    else:
        b = next(x for x in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"] if x["id"] == label)
    p = cdir / f"fullraid-start-{label}.json"
    p.write_text(json.dumps({"id": label, "allocation": b["allocation"]}, indent=1) + "\n", encoding="utf-8")
    return p, R.alloc_of(b)


def search(cls, entry, kind, label):
    p, al = start_file(cls, label)
    out = paths.raidsim_dir(cls) / "candidates" / f"fullraid-{entry}-{kind}.json"
    args = [sys.executable, str(HERE / "talent_opt.py"), cls, "--spec", entry, "--start", str(p), "--setting", "raid", "--write", str(out)]
    t = lead_tree(cls, al)
    if t:
        args += ["--min-tree", f"{t}={SM.SPEC_POINTS}"]
    r = subprocess.run(args, capture_output=True, text=True)
    print(f"  [{cls} {entry} {kind}] " + " | ".join(ln.strip() for ln in r.stdout.splitlines() if "round" in ln or "final" in ln)[-400:], flush=True)
    return out if out.exists() else None


def race(cls, entry, cands):
    e = R.SPECS[cls][entry]
    repo = R.repo_path(argparse.Namespace(repo=None))
    tr = R.load_trees(repo, cls)
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    ours = [b for b in e.get("builds", []) if b in data]
    bl = [{"label": b, "talents": R.talents_string(tr, R.alloc_of(data[b]))} for b in ours]
    bl += [{"label": f"cand:{k}", "talents": R.talents_string(tr, R.alloc_of(json.load(open(p, encoding="utf-8"))))} for k, p in cands.items()]
    rows = A.bench(e, repo, bl, 20000, 3, "raid", f"fullraid-{cls}-{entry}")
    our_best = max(ours, key=lambda b: (rows.get(b) or {}).get("dps") or 0)
    res = {k: (rows.get(f"cand:{k}") or {}).get("dps") or 0 for k in cands}
    top = max(res, key=res.get) if res else None
    return {"our_best": our_best, "our_dps": rows[our_best]["dps"], "candidates": res, "top": top,
            "gain": (res[top] / rows[our_best]["dps"] - 1) if top else 0.0}


def run_entry(cls, entry, rec):
    starts = plan(cls, entry)
    if not starts:
        return None
    cands = {}
    for kind, label in starts:
        p = search(cls, entry, kind, label)
        if p:
            cands[kind] = str(p)
    r = race(cls, entry, cands) if cands else {}
    r.update({"starts": dict(starts), "files": cands, "date": TODAY})
    r["verdict"] = "new parse build" if r.get("gain", 0) >= MIN_GAIN else "ours stays"
    print(f"== {cls} {entry}: ours {r.get('our_best')} {r.get('our_dps', 0):.0f}; " + ", ".join(f"{k} {v:.0f}" for k, v in r.get("candidates", {}).items())
          + f" -> {r['verdict']} ({r.get('gain', 0):+.1%})", flush=True)
    return r


def write(rec):
    for cls, es in rec.items():
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        for entry, r in es.items():
            if not r or r.get("verdict") != "new parse build":
                continue
            c = json.load(open(r["files"][r["top"]], encoding="utf-8"))
            s = c.get("search", {})
            moves = "; ".join(m["move"] for m in s.get("moves", [])) or "none"
            al = R.alloc_of(c)
            tree = lead_tree(cls, al)
            bid = f"{entry}-fullraid-parse"
            b = {"id": bid, "name": f"{(tree or 'Hybrid')} — Full raid (searched in the full-raid setting)", "role": "dps", "content": "raid", "tier": "draft",
                 **({"spec": tree} if tree else {}), "generated": TODAY, "derived": "raid",
                 "summary": (f"The build for a full raid (every raid buff and debuff): a talent search in the community simulator's full-raid setting "
                             f"from {r['starts'][r['top']]} ({r['top']}), {r['gain']:+.1%} over our best ({r['our_best']}) in a head-to-head race. "
                             f"The training-dummy pick is unchanged."),
                 "allocation": SB.to_allocation(cls, al), "core": [], "flex": [],
                 "notes": [f"{TODAY} raidsim/fullraid_search.py (the lesson of the Arms miss: talents that pay off only with raid buffs read "
                           f"as worthless on the dummy). Moves: {moves}. Race: full raid, seed 3, 20,000 iterations.",
                           "Simulator numbers are the community's model of the beta."],
                 "open_questions": ["Check the full-raid build against live raid logs at launch."],
                 "sources": ["https://github.com/ElliotWood/Forever"] + (["https://talentsforever.com/popular.js"] if r["top"] == "popular" else [])}
            data["builds"] = [x for x in data["builds"] if x["id"] != bid] + [b]
            SB.add_to_entry(cls, entry, bid)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    rec = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    todo = [(c, n) for c, es in R.SPECS.items() if not c.startswith("_") and (not a.classes or c in a.classes)
            for n, e in es.items() if isinstance(e, dict) and e.get("gear") and not e.get("tank") and n not in rec.get(c, {})]

    def one(job):
        cls, entry = job
        r = run_entry(cls, entry, rec)
        rec.setdefault(cls, {})[entry] = r
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    with ThreadPoolExecutor(a.jobs) as ex:
        list(ex.map(one, todo))
    if a.write:
        write(rec)


if __name__ == "__main__":
    main()
