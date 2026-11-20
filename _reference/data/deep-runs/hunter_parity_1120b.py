"""The hunter parity race again, with Hunter's Mark fixed (2026-11-20 evening, the audit session's step 3 after the mark defect;
deep-runs/mark_cast_fix_1120.py). Per entry, full raid, the entry's gear, 10,000 fights, seeds 1 and 2, every build of the entry plus
the simulator's builds, under our option set and the simulator's:
- "ours": the rotation the entry ran before the 12:32 switch to the official ones (our tuned raid rotation; mm-raid's from git, the
  lane re-tuned that file at 15:39), as it was;
- "ours+mark": the same with the official rotation's two mark lines (the pre-pull cast and "cast if the mark is not up"), which our
  ranged rotations lacked entirely (they relied on the raid's hunters_mark debuff, which does nothing in the bench) and our melee
  rotations half (the pre-pull cast only, and the mark ends before a 180 s fight does);
- the official rotations, mark fixed (the build files' own: bm turret_hawk, mm turret, sv_melee melee);
- mm-raid also "lane-1539": the lane's re-tune of 15:39 (tuned on the broken base), mark fixed.
Each arm's mark casts and Mongoose Bite casts are recorded (the conversion check: a pre-pull line that never casts fails the arm).

    python _reference/data/deep-runs/hunter_parity_1120b.py [entries...] [--fights 10000]
"""
import argparse
import copy
import json
import pathlib
import subprocess
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "deep-runs"), str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import siml_upstream_race as SU  # noqa: E402

OUT = DATA / "raidsim" / "hunter-parity-1120b.json"
SCRATCH = DATA / "deep-runs" / "parity-1120b"
OURS = {"bm-raid": "raidsim/apls/hunter/bm-raid-raid.apl.json", "mm-raid": "git:raidsim/apls/hunter/mm-raid-raid.apl.json",
        "mm-lonewolf-raid": "raidsim/apls/hunter/mm-lonewolf-raid-raid.apl.json", "melee-dps": "raidsim/apls/hunter/melee-dps-raid.apl.json",
        "survival-pet-raid": "raidsim/apls/hunter/survival-pet-raid-raid.apl.json"}
UP = {"bm-raid": ["bm"], "mm-raid": ["mm"], "mm-lonewolf-raid": ["mm", "sv"], "melee-dps": ["sv_melee"], "survival-pet-raid": ["sv_melee"]}
UP_BUILDS = {"bm-raid": ["bm"], "mm-raid": [], "mm-lonewolf-raid": ["mm", "sv"], "melee-dps": ["sv_melee"], "survival-pet-raid": ["sv_melee"]}
MARK_CAST = {"spellId": {"spellId": 14325, "rank": 4}}
MARK_IDS = {"14325", "14324", "14323", "1130"}


def load_ours(e):
    src = OURS[e]
    if src.startswith("git:"):
        txt = subprocess.run(["git", "show", f"HEAD:_reference/data/{src[4:]}"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
        return json.loads(txt)
    return json.load(open(DATA / src, encoding="utf-8"))


def with_mark(apl, up_melee):
    """The official melee rotation's pre-pull mark and its "if the mark is not up" line, added where the rotation lacks them."""
    a = copy.deepcopy(apl)
    pre = [x for x in up_melee.get("prepullActions", []) if ((x.get("action") or {}).get("castSpell") or {}).get("spellId") == MARK_CAST["spellId"]]
    line = [x for x in up_melee.get("priorityList", []) if ((x.get("action") or {}).get("castSpell") or {}).get("spellId") == MARK_CAST["spellId"]]
    assert pre and line, "the official melee rotation's mark lines"

    def casts_mark(items):
        return any(((x.get("action") or {}).get("castSpell") or {}).get("spellId", {}).get("spellId") in (14325, 14324) for x in items or [])
    if not casts_mark(a.get("prepullActions")):
        a["prepullActions"] = copy.deepcopy(pre) + list(a.get("prepullActions") or [])
    if not casts_mark(a.get("priorityList")):
        a["priorityList"] = copy.deepcopy(line) + list(a.get("priorityList") or [])
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entries", nargs="*")
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    up, commit = SU.read_upstream(repo)   # writes the upstream files again with the fixed conversion (identical to the repair)
    SCRATCH.mkdir(parents=True, exist_ok=True)
    up_melee = json.load(open(up["hunter"]["sv_melee"]["apl"], encoding="utf-8"))
    names = R.spell_names(repo, "hunter")
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    ours_builds = {b["id"]: b for b in json.load(open(ROOT / "hunter/research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    trees = R.load_trees(repo, "hunter")
    for e in a.entries or list(OURS):
        entry = copy.deepcopy(R.SPECS["hunter"][e])
        spec_key = next(iter(entry["spec"]))
        rots = {}
        ours = load_ours(e)
        for nm, apl in (("ours", ours), ("ours+mark", with_mark(ours, up_melee))):
            p = SCRATCH / f"{e}-{nm.replace('+', '-')}.apl.json"
            p.write_text(json.dumps(apl, indent=1) + "\n", encoding="utf-8")
            rots[nm] = str(p)
        for n in UP[e]:
            rots.setdefault(f"up:{up['hunter'][n]['rotation']}", up["hunter"][n]["apl"])
        if e == "mm-raid":
            rots["lane-1539"] = str(DATA / "raidsim/apls/hunter/mm-raid-raid.apl.json")
        opts = {"ours": dict(entry["spec"][spec_key]["options"].get("classOptions", {}))}
        for n in UP_BUILDS[e]:
            o = dict(up["hunter"][n]["options"])
            if "petType" not in o:
                o["petType"] = "PetNone"
            if o != opts["ours"] and o not in opts.values():
                opts[f"up:{n}"] = o
        builds = {}
        for bid in entry.get("builds", []):
            b = ours_builds.get(bid)
            if b:
                builds[bid] = R.talents_string(trees, {k: r for items in b["allocation"].values() for k, r in items if r})
        for n in UP_BUILDS[e]:
            if up["hunter"][n]["talents"] not in builds.values():
                builds[f"up:{n}"] = up["hunter"][n]["talents"]
        print(f"== {e}: rotations {list(rots)}, option sets {list(opts)}, builds {list(builds)}", flush=True)
        res, casts = {}, {}
        for on, o in opts.items():
            ent = copy.deepcopy(entry)
            ent["spec"][spec_key]["options"]["classOptions"] = o
            bl = [{"label": f"{rn}|{on}|{bn}", "talents": t, "apl": rp} for rn, rp in rots.items() for bn, t in builds.items()]
            for seed in (1, 2):
                rows = A.bench(ent, repo, bl, a.fights, seed, "raid", f"parity1120b-{e}")
                for lab, row in rows.items():
                    res.setdefault(lab, {})[str(seed)] = round(row.get("dps") or 0.0, 2)
                    if seed == 1 and row.get("actions"):
                        c = R.action_casts(row["actions"], names)[0]
                        mark = sum(v for k, v in c.items() if str(k) in MARK_IDS)
                        mb = sum(v for k, v in c.items() if str(k).isdigit() and names.get(int(k), "") == "Mongoose Bite")
                        casts[lab] = {"mark": round(mark, 2), "mongoose_bite": round(mb, 2)}
        mean = {lab: sum(v.values()) / len(v) for lab, v in res.items() if len(v) == 2}
        bad = sorted({lab.split("|")[0] for lab, c in casts.items() if c["mark"] < 0.5 and not lab.startswith("ours|")})
        best = max(mean, key=mean.get)
        ours_best = max((lab for lab in mean if lab.startswith("ours+mark|")), key=mean.get)
        up_best = max((lab for lab in mean if lab.startswith("up:")), key=mean.get)
        rec[e] = {"fights": a.fights, "commit": commit, "sim": {"repo": str(repo), **R.sim_switches(repo)}, "rotations": rots, "options": opts,
                  "builds": builds, "dps": res, "casts": casts, "best": best, "ours_mark_best": ours_best, "up_best": up_best,
                  "up_vs_ours_mark": round(mean[up_best] / mean[ours_best] - 1, 4), "no_mark_arms": bad}
        for lab in sorted(mean, key=mean.get, reverse=True)[:14]:
            c = casts.get(lab, {})
            print(f"   {lab:58s} {res[lab]['1']:8.1f} {res[lab]['2']:8.1f}   mark {c.get('mark', 0):.1f}  MB {c.get('mongoose_bite', 0):.1f}", flush=True)
        print(f"   best {best} {mean[best]:.1f}; ours+mark {ours_best} {mean[ours_best]:.1f}; official {up_best} {mean[up_best]:.1f} "
              f"({rec[e]['up_vs_ours_mark']:+.2%})" + (f"; NO MARK: {bad}" if bad else ""), flush=True)
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
