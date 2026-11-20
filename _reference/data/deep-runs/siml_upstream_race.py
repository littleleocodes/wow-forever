"""The independent audit's H6 (2026-11-20; the user asked whether to simply use the simulator's preset builds, naming the melee hunter):
the official simulator's hunter and Retribution builds have never been raced with their own rotations, which the simulator keeps as
SIML since 2026-11-03 (#812) and our tools did not read. Each build file is read with the bench's -siml2json (an IndividualSimSettings:
its talents, its class options and, for the hunter, its rotation); the paladin's rotations come from apls/*.apl.siml. Rotations are
written to raidsim/apls/<class>/upstream/ with trainer ranks (trainer_ranks.py). Then, as warlock_upstream_race.py did: each entry's
raid rotation and the upstream rotations of its tree x each option set (the entry's, and each upstream build's where it differs) x
each build (the entry's own and the upstream builds of its tree), full raid, the entry's gear and consumables, the same fights,
10,000 fights on seeds 1 and 2.

    python _reference/data/deep-runs/siml_upstream_race.py [entries] [--fights 10000] [--copy-only]

Pseudo-entry melee-dps@weave: upstream's weave (sv_weave, its rotation, 12 yards) in melee-dps's gear, reported apart (a rotation our
pages may not be able to describe). mm-lonewolf-raid also races upstream's ranged Survival (sv, 3/19/29), reported apart: a Survival
build in a Marksmanship entry's setup. The Holy Shock rotation swaps in the Manual Crowd Pummeler (itemSwap actions), which the bench
does not configure: those lines do nothing here (said in the record).
Record raidsim/siml-upstream-race.json.
"""
import argparse
import copy
import json
import pathlib
import subprocess
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import trainer_ranks as TR  # noqa: E402

OUT = DATA / "raidsim" / "siml-upstream-race.json"
BUILDS = {"hunter": ("ui/specs/hunter/dps/builds", ["bm", "mm", "sv", "sv_melee", "sv_weave"]),
          "paladin": ("ui/specs/paladin/retribution/builds", ["holy_shock", "unsealed_wrath"])}
PALADIN_ROTS = ("ui/specs/paladin/retribution/apls", ["default", "holy_shock"])
# the hunter's build files name their rotation (use "../apls/<x>.apl.siml"); the paladin's build files none: presets.ts runs
# Unsealed Wrath on the Default APL and Holy Shock on the Holy Shock APL
PALADIN_ROT_OF = {"unsealed_wrath": "default", "holy_shock": "holy_shock"}
ENTRIES = {
    "bm-raid": {"cls": "hunter", "builds": ["bm"]},
    "mm-raid": {"cls": "hunter", "builds": [], "rots": ["mm"]},        # no upstream Marksmanship build with a pet: its rotation only
    "mm-lonewolf-raid": {"cls": "hunter", "builds": ["mm", "sv"]},
    "melee-dps": {"cls": "hunter", "builds": ["sv_melee"]},
    "melee-dps@weave": {"cls": "hunter", "base": "melee-dps", "builds": ["sv_weave"], "distance": 12, "ours_rot": False},
    "ret-dps": {"cls": "paladin", "builds": ["unsealed_wrath"]},
    "shockadin-raid": {"cls": "paladin", "builds": ["holy_shock"]},
}


def bench_exe(repo):
    return repo / ("foreverbench.exe" if (repo / "foreverbench.exe").exists() else "foreverbench")


def siml2json(repo, path):
    r = subprocess.run([str(bench_exe(repo)), "-siml2json", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"siml2json {path}: {r.stderr[-400:]}")
    return json.loads(r.stdout)


def read_upstream(repo):
    """{class: {build: {talents, options, rotation file}}}, the rotations written with trainer ranks."""
    mp = TR.load_map()
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in mp.items()}
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
    out = {}
    for cls, (bdir, names) in BUILDS.items():
        dst = DATA / "raidsim" / "apls" / cls / "upstream"
        dst.mkdir(parents=True, exist_ok=True)
        out[cls] = {}
        for n in names:
            src = repo / bdir / f"{n}.siml"
            d = siml2json(repo, src)
            p = d["player"]
            spec_key = next(k for k, v in p.items() if isinstance(v, dict) and "options" in v)
            rot = p.get("rotation") or {}
            if cls == "paladin":
                rdir, _ = PALADIN_ROTS
                rot = siml2json(repo, repo / rdir / f"{PALADIN_ROT_OF[n]}.apl.siml")
                rname = PALADIN_ROT_OF[n]
            else:
                use = [ln.split('"')[1] for ln in src.read_text(encoding="utf-8").splitlines() if ln.startswith("use ") and ".apl.siml" in ln]
                rname = pathlib.Path(use[0]).name.replace(".apl.siml", "") if use else n
            f = dst / f"{rname}.apl.json"
            f.write_text(TR.swap_text(json.dumps(rot, indent=1) + "\n", fwd), encoding="utf-8", newline="")
            out[cls][n] = {"talents": p["talentsString"], "spec_key": spec_key, "options": p[spec_key]["options"].get("classOptions", {}),
                           "rotation": rname, "apl": str(f), "distance": p.get("distanceFromTarget")}
        readme = dst / "README.md"
        text = (f"# Upstream {cls} rotations (SIML)\n\nThe official wowsims/forever simulator's own {cls} rotations at {commit}, read from its "
                f"SIML files with the bench's -siml2json (deep-runs/siml_upstream_race.py, 2026-11-20, the independent audit's H6). Book "
                f"ranks swapped to trainer ranks (trainer_ranks.py). An entry that adopts one takes it as its base (`apl`) and tunes from "
                f"there.\n")
        if not readme.exists() or "SIML" not in readme.read_text(encoding="utf-8"):
            readme.write_text(text + ("\n" + readme.read_text(encoding="utf-8") if readme.exists() else ""), encoding="utf-8")
    return out, commit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entries", nargs="*")
    ap.add_argument("--fights", type=int, default=10000)
    ap.add_argument("--copy-only", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    up, commit = read_upstream(repo)
    for cls, bs in up.items():
        for n, u in bs.items():
            print(f"{cls} {n}: {u['talents']} rotation {u['rotation']} options {u['options']}", flush=True)
    if a.copy_only:
        return
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    for e in a.entries or list(ENTRIES):
        cfg = ENTRIES[e]
        cls = cfg["cls"]
        base_name = cfg.get("base", e)
        entry = copy.deepcopy(R.SPECS[cls][base_name])
        if cfg.get("distance") is not None:
            entry["distance"] = cfg["distance"]
        trees = R.load_trees(repo, cls)
        ours = {b["id"]: b for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
        spec_key = next(iter(entry["spec"]))
        rots = {} if cfg.get("ours_rot") is False else {"ours": str(R.apl_path(entry, repo, "raid"))}
        names = list(cfg["builds"]) + list(cfg.get("rots", []))
        for n in names:
            u = up[cls][n]
            rots.setdefault(u["rotation"], u["apl"])
        opts = {"ours": dict(entry["spec"][spec_key]["options"].get("classOptions", {}))}
        for n in cfg["builds"]:
            o = dict(up[cls][n]["options"])
            if cls == "hunter" and "petType" not in o:
                o["petType"] = "PetNone"   # no pet type in the build file: none out (Lone Wolf)
            if o != opts["ours"] and o not in opts.values():
                opts[f"up:{n}"] = o
        builds = {}
        for bid in entry.get("builds", []):
            b = ours.get(bid)
            if b:
                builds[bid] = R.talents_string(trees, {k: r for items in b["allocation"].values() for k, r in items if r})
        for n in cfg["builds"]:
            if up[cls][n]["talents"] not in builds.values():
                builds[f"up:{n}"] = up[cls][n]["talents"]
        print(f"== {e}: rotations {list(rots)}, option sets {list(opts)}, builds {list(builds)}", flush=True)
        res = {}
        for on, o in opts.items():
            ent = copy.deepcopy(entry)
            ent["spec"][spec_key]["options"]["classOptions"] = o
            bl = [{"label": f"{rn}|{on}|{bn}", "talents": t, "apl": rp} for rn, rp in rots.items() for bn, t in builds.items()]
            for seed in (1, 2):
                rows = A.bench(ent, repo, bl, a.fights, seed, "raid", f"simlup-{e.replace('@', '-')}")
                for lab, row in rows.items():
                    res.setdefault(lab, {})[str(seed)] = round(row.get("dps") or 0.0, 2)
        mean = {lab: sum(v.values()) / len(v) for lab, v in res.items() if len(v) == 2}
        ours_arms = [lab for lab in mean if lab.startswith("ours|ours|")]
        our_best = max(ours_arms, key=mean.get) if ours_arms else None
        best = max(mean, key=mean.get)
        rec[e] = {"class": cls, "fights": a.fights, "commit": commit, "rotations": rots, "options": opts, "builds": builds, "dps": res,
                  "our_best": our_best, "best": best,
                  "gain": round(mean[best] / mean[our_best] - 1, 4) if our_best else None,
                  "note": ("upstream's weave, reported apart" if "@weave" in e else
                           "the Holy Shock rotation's itemSwap lines (the Manual Crowd Pummeler) do nothing here" if e == "shockadin-raid" else "")}
        for lab in sorted(mean, key=mean.get, reverse=True)[:12]:
            print(f"   {lab:62s} {res[lab]['1']:8.1f} {res[lab]['2']:8.1f}", flush=True)
        if our_best:
            print(f"   ours: {our_best} {mean[our_best]:.1f}; best: {best} {mean[best]:.1f} ({rec[e]['gain']:+.2%})", flush=True)
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
