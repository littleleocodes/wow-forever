"""Upstream parity for the tanks (2026-11-20, "Simulator build first": the same rule for the tanks, the audit's plan): the official
simulator's own tank rotation and its tank presets against our tank entry's rotation and builds, standing in front of the boss (in_front,
since the same morning), the entry's gear, consumables and raid setting, tank value (run.tank_value: threat and damage taken against the
entry's first listed build under our rotation), 10,000 fights on seeds 1 and 2. The rotations are written to raidsim/apls/<class>/upstream/
with trainer ranks (the paladin's from SIML through the bench's -siml2json).

    python -u _reference/data/deep-runs/tank_upstream_race.py <class> [--fights 10000]

Record raidsim/tank-upstream-race.json {class: {entry, arms, our best arm, best arm, gain}}; prints the best arm's label last
("best: <rotation>|<build>"), which the tank lane's short check starts from when it is our rotation's.
"""
import argparse
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
from filelock import locked  # noqa: E402

OUT = DATA / "raidsim" / "tank-upstream-race.json"
CONFIG = {
    "warrior": {"entry": "prot-tank", "rot": "ui/specs/warrior/protection/apls/default.apl.json", "name": "protection-default",
                "presets": {"Protection": "05-05050005-150531120300001351"}},
    "paladin": {"entry": "prot-tank", "rot": "ui/specs/paladin/protection/apls/default.apl.siml", "name": "protection-default",
                "presets_siml": "ui/specs/paladin/protection/defaults.siml", "presets": {}},
    "druid": {"entry": "feral-bear-tank", "rot": "ui/specs/druid/feralbear/apls/adaptive.apl.json", "name": "feralbear-adaptive",
              "presets": {"Bear": "050022-5023030212310112501-055", "Hybrid": "050012-50230302123110125011-055"}},
}


def bench_exe(repo):
    return repo / ("foreverbench.exe" if (repo / "foreverbench.exe").exists() else "foreverbench")


def siml2json(repo, path):
    r = subprocess.run([str(bench_exe(repo)), "-siml2json", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"siml2json {path}: {r.stderr[-400:]}")
    return json.loads(r.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls", choices=sorted(CONFIG))
    ap.add_argument("--fights", type=int, default=10000)
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    cfg = CONFIG[a.cls]
    src = repo / cfg["rot"]
    rot = siml2json(repo, src) if src.suffix == ".siml" else json.loads(src.read_text(encoding="utf-8"))
    mp = TR.load_map()
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in mp.items()}
    dst = DATA / "raidsim" / "apls" / a.cls / "upstream"
    dst.mkdir(parents=True, exist_ok=True)
    up_path = dst / f"{cfg['name']}.apl.json"
    up_path.write_text(TR.swap_text(json.dumps(rot, indent=1) + "\n", fwd), encoding="utf-8", newline="")
    presets = dict(cfg["presets"])
    if cfg.get("presets_siml"):
        presets["Default"] = siml2json(repo, repo / cfg["presets_siml"])["player"]["talentsString"]
    entry = R.SPECS[a.cls][cfg["entry"]]
    trees = R.load_trees(repo, a.cls)
    ours = {b["id"]: b for b in json.load(open(ROOT / a.cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    builds = {bid: R.talents_string(trees, R.alloc_of(ours[bid])) for bid in entry.get("builds", []) if bid in ours}
    for n, t in presets.items():
        if t not in builds.values():
            builds[f"sim preset: {n}"] = t
    rots = {"ours": str(R.apl_path(entry, repo, "raid")), "upstream": str(up_path)}
    ref_label = f"ours|{next(iter(builds))}"
    print(f"== {a.cls} {cfg['entry']}: rotations {list(rots)}, builds {list(builds)}; reference {ref_label}", flush=True)
    rows = {}
    for seed in (1, 2):
        bl = [{"label": f"{rn}|{bn}", "talents": t, "apl": rp} for rn, rp in rots.items() for bn, t in builds.items()]
        out = A.bench(entry, repo, bl, a.fights, seed, "raid", f"tankup-{a.cls}")
        for lab, row in out.items():
            rows.setdefault(lab, {})[str(seed)] = {k: row.get(k) for k in ("dps", "threat", "dtps")}
    val = {lab: {s: R.tank_value(v[s], rows[ref_label][s]) for s in v} for lab, v in rows.items()}
    mean = {lab: sum(x.values()) / len(x) for lab, x in val.items() if all(x.values())}
    our_best = max((lab for lab in mean if lab.startswith("ours|") and not lab.startswith("ours|sim preset")), key=mean.get)
    best = max(mean, key=mean.get)
    for lab in sorted(mean, key=mean.get, reverse=True):
        r1, r2 = rows[lab]["1"], rows[lab]["2"]
        print(f"   {lab:52s} value {val[lab]['1']:.4f} / {val[lab]['2']:.4f}   threat {r1['threat']:.0f} / {r2['threat']:.0f}   "
              f"dtps {r1['dtps']:.1f} / {r2['dtps']:.1f}", flush=True)
    rec_e = {"entry": cfg["entry"], "fights": a.fights, "commit": R.git_commit(repo), "rotations": rots, "builds": builds, "rows": rows,
             "value": val, "reference": ref_label, "our_best": our_best, "best": best,
             "gain": [round(val[best][s] / val[our_best][s] - 1, 4) for s in ("1", "2")]}
    with locked(OUT.with_suffix(".lock")):
        rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        rec[a.cls] = rec_e
        OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"   ours: {our_best}; best: {best} ({rec_e['gain'][0]:+.2%} / {rec_e['gain'][1]:+.2%})", flush=True)
    print(f"best: {best}", flush=True)


if __name__ == "__main__":
    main()
