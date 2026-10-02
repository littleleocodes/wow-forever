"""Derive one raid build per spec (and role) in the community simulator (2026-09-30, user request: "each spec to have a leveling, raid and
PvP spec that we can best derive from everything").

    python _reference/data/derive_raid.py [classes] [--only <tree>] [--fresh] [--write]

For every (class, tree) and role (damage; tank where the tree tanks) with raid builds: start from the spec's best raid build of ours in
the last race (training dummy DPS; tanks: tank value), and run raidsim/talent_opt.py in that build's entry with --min-tree <tree>=30 (the
dummy setting for damage, the entry's setting for tanks). The derived build replaces the spec's pick only when it beats the best hand
draft by 2% or more (the user's rule), estimated as (start / hand in the race) x (search result / start on the search's third seed);
the hand draft stays as the alternative. The re-race afterwards (raidsim/run.py --write) sets the numbers the pages show. Healers: the
healer lab's own pipeline does this (rebuild.py --steps heal,adopt: calibrate, optimize, race, adopt over 2%).
Records: `_reference/data/derived-raid.json` (generated; reused unless --fresh); candidates
`<class>/research/raid/raidsim/candidates/derived-<tree>[-tank].json`.
"""
import argparse
import datetime
from filelock import locked
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "scorer"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import spec_builds as SB  # noqa: E402
import render_start_here as rs  # noqa: E402
from fmt_json import dumps  # noqa: E402

OUT = HERE / "derived-raid.json"
TODAY = datetime.date.today().isoformat()
MIN_GAIN = 0.02


def hand(b):
    return not b.get("generated") and not b["id"].startswith("opt-")


def save(cls, key, rec):
    with locked(OUT.with_suffix(".lock")):
        old = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
        old.setdefault(cls, {})[key] = rec
        OUT.write_text(json.dumps(old, indent=1) + "\n", encoding="utf-8")


def targets(cls):
    """[(tree, role, [(build, metric, entry)])] for the class's trees, best first."""
    builds = json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]
    g = SM.grid(cls, builds)
    best = {}
    for x in rs.raid_rows(cls):
        r = x["row"]
        m = r.get("value") if x["tank"] else r.get("dps")
        if m and (r["label"] not in best or m > best[r["label"]][0]):
            best[r["label"]] = (m, x["spec"], x["tank"])
    out = []
    for tree in SM.trees(cls):
        for role in ("dps", "tank"):
            rows = [(b, *best[b["id"]][:2]) for b in g[tree]["raid"] if b["id"] in best and b.get("role") != "healer"
                    and not b["id"].endswith("-parse") and bool(best[b["id"]][2]) == (role == "tank")]
            if rows:
                out.append((tree, role, sorted(rows, key=lambda x: -x[1])))
    return out


def derive(cls, tree, role, rows, a):
    b0, m0, entry = rows[0]
    hands = [(b, m) for b, m, _ in rows if hand(b)]
    suffix = "-tank" if role == "tank" else ""
    cand = paths.raidsim_dir(cls) / "candidates" / f"derived-{SM.slug(tree)}{suffix}.json"
    rec = {"tree": tree, "role": role, "entry": entry, "start": b0["id"], "start_metric": m0, "date": TODAY,
           "hand": hands[0][0]["id"] if hands else None, "hand_metric": hands[0][1] if hands else None, "candidate": str(cand.relative_to(ROOT))}
    if a.fresh or not cand.exists():
        # a tank build belongs to its tank tree by role, not by 30 points (the Protection paladin tank is 0/23/28): tanks keep at least
        # the start's own points there
        need = SM.SPEC_POINTS if role == "dps" else min(SM.SPEC_POINTS, sum(r for _, r in b0["allocation"].get(tree, [])))
        args = [sys.executable, str(HERE / "raidsim/talent_opt.py"), cls, "--spec", entry, "--start", b0["id"], "--min-tree", f"{tree}={need}",
                "--write", str(cand)] + (["--setting", "dummy"] if role == "dps" else [])
        r = subprocess.run(args, capture_output=True, text=True)
        print("\n".join("    " + ln for ln in r.stdout.strip().splitlines()[-6:]), flush=True)
        if r.returncode or not cand.exists():
            print("    FAILED " + r.stderr[-600:], flush=True)
            rec["error"] = "search failed"
            return rec
    s = json.load(open(cand, encoding="utf-8"))["search"]
    rec["search_gain"] = s.get("gain", s["dps_end"] / s["dps_start"] - 1)
    rec["moves"] = s["moves"]
    if hands:
        rec["gain_vs_hand"] = (m0 / hands[0][1]) * (1 + rec["search_gain"]) - 1
        rec["verdict"] = "replaces" if rec["gain_vs_hand"] >= MIN_GAIN and rec["moves"] else "hand stays"
    else:
        rec["verdict"] = "new" if rec["moves"] and rec["search_gain"] > 0 else "start stays"
    return rec


def build_of(cls, rec, c):
    tree, role = rec["tree"], rec["role"]
    tank = role == "tank"
    moves = "; ".join(m["move"] for m in rec["moves"])
    b = {"id": f"{SM.slug(tree)}{'-tank' if tank else ''}-raid", "name": f"{tree} — {'Tank' if tank else 'Raid'} (derived)",
         "role": "tank" if tank else "dps", "content": "raid", "tier": "draft", "spec": tree, "generated": TODAY, "derived": "raid",
         "summary": (f"The {tree} {'tank' if tank else 'raid damage'} build derived on {TODAY} (derive_raid.py): the community simulator's talent "
                     f"search (raidsim/talent_opt.py, entry {rec['entry']}, {'the entry setting' if tank else 'training dummy'}) from the spec's best "
                     f"build {rec['start']}, 30+ points kept in {tree}."),
         "allocation": c["allocation"], "core": [], "flex": [],
         "notes": [f"Simulator talent search from {rec['start']}: {moves} ({rec['search_gain']:+.1%} "
                   f"{'tank value' if tank else 'DPS'} on the search's third seed).",
                   "Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements."],
         "open_questions": [f"A derived {tree} raid build: check it against the community's {tree} builds at launch."],
         "sources": ["https://github.com/ElliotWood/Forever"]}
    if rec["verdict"] == "replaces":
        b["replaces"] = rec["hand"]
        b["notes"].insert(0, f"About {rec['gain_vs_hand']:+.1%} over the hand draft {rec['hand']} (over the 2% replacement bar): this build is the "
                             f"spec's raid pick, the hand draft stays as the alternative.")
    return b


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--only")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    done = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    for cls in a.classes or SM.CLASSES:
        for tree, role, rows in targets(cls):
            if a.only and tree != a.only:
                continue
            key = f"{tree}{' (tank)' if role == 'tank' else ''}"
            if not a.fresh and done.get(cls, {}).get(key, {}).get("verdict"):
                print(f"== {cls} {key}: done ({done[cls][key]['verdict']})", flush=True)
                continue
            print(f"== {cls} {key}: start {rows[0][0]['id']} ({rows[0][1]:.1f}, {rows[0][2]})", flush=True)
            rec = derive(cls, tree, role, rows, a)
            save(cls, key, rec)
            print(f"  -> {rec.get('verdict', rec.get('error'))}" + (f" ({rec['gain_vs_hand']:+.2%} vs {rec['hand']})" if rec.get("gain_vs_hand") is not None else ""), flush=True)
    if a.write:
        res = json.load(open(OUT, encoding="utf-8"))
        for cls, per in res.items():
            if a.classes and cls not in a.classes:
                continue
            bp = paths.builds_json("forever", cls)
            data = json.load(open(bp, encoding="utf-8"))
            for key, rec in per.items():
                if rec.get("verdict") not in ("replaces", "new"):
                    continue
                b = build_of(cls, rec, json.load(open(ROOT / rec["candidate"], encoding="utf-8")))
                data["builds"] = [x for x in data["builds"] if x["id"] != b["id"] and not (x.get("generated") and not x.get("derived")
                                  and SM.spec_of(cls, x) == rec["tree"] and SM.mode_of(x) == "raid" and (x.get("role") == "tank") == (rec["role"] == "tank"))]
                data["builds"].append(b)
                SB.add_to_entry(cls, rec["entry"], b["id"])
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
            print(f"wrote {bp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
