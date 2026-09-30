"""Turn a new-builds search result into a proposed build (2026-09-28, the new-builds survey).

    python _reference/data/raidsim/add_survey_builds.py _reference/data/raidsim/survey-builds.json [build ids...]

For each configured build (a JSON config: per class a list of {id, spec (the raid entry), glob (its talent-search candidate files),
after, name, summary, why {talent: reason}, notes, open_questions, sources}): take the best candidate of its simulator talent searches
(raidsim/talent_opt.py; third-seed DPS of the search record), measure every talent's removal cost in the simulator under the entry's
rotation (raidsim/run.py --deltas all), write the build into <class>/research/talents/forever/proposed-builds.json (core ranked by removal
cost with the config's reasons, flex = talents worth under 1%), and register it in the entry's `builds` in raidsim/specs.json.
An existing build with the same id is replaced (its sources and open questions kept when the config gives none): re-running it
rewrites hand edits of core, flex, notes and summary. Then run validate_builds.py and render_builds.py.
survey-builds.json holds the texts the 2026-09-28 survey builds were written with.
"""
import datetime
import glob
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
DATA = ROOT / "_reference/data"
sys.path.insert(0, str(DATA))
from fmt_json import dumps  # noqa: E402

TODAY = datetime.date.today().isoformat()


def best_candidate(cls, pattern):
    best = None
    for f in glob.glob(str(ROOT / cls / "research/raid/raidsim/candidates" / (pattern + ".json"))):
        d = json.load(open(f, encoding="utf-8"))
        s = d.get("search")
        if not s:
            continue
        if best is None or (s.get("dps_end") or 0) > (best[1]["search"].get("dps_end") or 0):
            best = (f, d)
    return best


def removal_costs(cls, spec, cand_file):
    r = subprocess.run([sys.executable, str(DATA / "raidsim/run.py"), cls, "--spec", spec, "--builds", cand_file, "--iterations", "3000",
                        "--no-presets", "--deltas", "all"], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    vals, dep = {}, set()
    for line in r.stdout.splitlines():
        m = re.match(r"\s+(.+?)\s+(\d)\s+sim\s+([+-][0-9.]+)%", line)
        if m:
            vals[m.group(1).strip()] = float(m.group(3)) / 100
            if "rotation-dependent" in line:
                dep.add(m.group(1).strip())
    if not vals:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit(f"no removal values for {cls} {spec}")
    return vals, dep


def build_entry(cls, cfg, cand_file, cand):
    alloc = cand["allocation"]
    flat = {n: r for items in alloc.values() for n, r in items}
    vals, dep = removal_costs(cls, cfg["spec"], cand_file)
    ranked = sorted(flat, key=lambda n: -vals.get(n, 0.0))
    why = cfg.get("why", {})

    def sim_why(n):
        if n in dep:
            return f"Simulator ({TODAY}): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it."
        return f"Simulator removal run ({TODAY}): the build loses {vals[n]:.1%} of its DPS on the training dummy without it." if n in vals else ""

    core_names = [n for n in ranked if n in why or vals.get(n, 0) >= 0.01 or n in dep][: cfg.get("core_n", 9)]
    core = [{"talent": n, "why": (why.get(n, "") + " " + sim_why(n)).strip()} for n in core_names]
    flex = [{"points": flat[n], "default": n, "alternatives": ["any talent legal at that tier"],
             "why": f"Worth {vals[n]:.1%} of the DPS on the training dummy in the simulator: free points (a tier filler, or noise)."}
            for n in ranked if n not in core_names and n in vals and abs(vals[n]) < 0.01]
    s = cand["search"]
    moves = s.get("moves") or []
    start = s.get("start") or "?"
    start = pathlib.Path(start).stem if start.endswith(".json") else start
    found = (f"Talents from the simulator talent search (raidsim/talent_opt.py, {TODAY}) from `{start}`: "
             + (", ".join(m["move"] for m in moves) if moves else "no move beat the start") + ".")
    b = {"id": cfg["id"], "name": cfg["name"], "role": "dps", "content": "raid", "tier": "draft", "summary": cfg["summary"],
         "allocation": alloc, "core": core, "flex": flex,
         "notes": [found] + cfg.get("notes", []) + ["New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. "
                                                     "A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited."],
         "open_questions": cfg.get("open_questions", []), "sources": cfg.get("sources", [])}
    return b, vals


def main():
    cfgs = json.load(open(sys.argv[1], encoding="utf-8"))
    only = set(sys.argv[2:])
    sp = DATA / "raidsim/specs.json"
    specs = json.load(open(sp, encoding="utf-8"))
    for cls, items in cfgs.items():
        bp = ROOT / cls / "research/talents/forever/proposed-builds.json"
        data = json.load(open(bp, encoding="utf-8"))
        changed = False
        for cfg in items:
            if only and cfg["id"] not in only:
                continue
            got = best_candidate(cls, cfg["glob"])
            if not got:
                print(f"{cls} {cfg['id']}: no candidate for {cfg['glob']}")
                continue
            f, cand = got
            b, vals = build_entry(cls, cfg, f, cand)
            ids = [x["id"] for x in data["builds"]]
            if cfg["id"] in ids:
                old = data["builds"][ids.index(cfg["id"])]
                for k in ("sources", "open_questions"):
                    b[k] = b[k] or old.get(k, [])
                data["builds"][ids.index(cfg["id"])] = b
            else:
                after = cfg.get("after")
                i = ids.index(after) + 1 if after in ids else len(ids)
                data["builds"].insert(i, b)
            changed = True
            e = specs[cls][cfg["spec"]]
            if cfg["id"] not in e["builds"]:
                e["builds"] = e["builds"] + [cfg["id"]]
            split = "/".join(str(sum(r for _, r in v)) for v in cand["allocation"].values())
            print(f"{cls} {cfg['id']}: {split} from {pathlib.Path(f).name} ({cand['search'].get('dps_end', 0):.1f} DPS in its search); "
                  f"core {len(b['core'])}, flex {len(b['flex'])}; top: " + ", ".join(f"{n} {v:+.1%}" for n, v in sorted(vals.items(), key=lambda x: -x[1])[:5]))
        if changed:
            json.dump(data, open(bp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            subprocess.run([sys.executable, str(DATA / "fmt_json.py"), str(bp)], check=True, capture_output=True)
    sp.write_text(dumps(specs) + "\n", encoding="utf-8")
    json.loads(sp.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
