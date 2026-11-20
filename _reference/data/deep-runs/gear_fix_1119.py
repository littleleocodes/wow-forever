"""Fixes for what the gear night of 2026-11-18 left out (2026-11-19):

    python _reference/data/deep-runs/gear_fix_1119.py shockadin | tankshield | orphans

- shockadin: the Shockadin's own Raid BiS set (tiers/paladin-hybrid-holy-retribution-bis.gear.json), which the night never made
  again (no ML record), held five later-phase items (Earthweave Cloak, Rockfury Bracers, Belt of Preserved Heads, Band of Earthen Might,
  Grand Marshal's Demolisher). gear_tiers.make for the page's pick (shockadin-open-raid) in the shockadin-raid entry, in a full raid;
  the old set cannot compete (its items are out of the pool).
- tankshield: the paladin tank's standard set (paladin-protection-default.gear.json; tanks keep their sets) held Force Reactive Disk,
  a later-phase shield. It takes the shield both of the tank's new tier sets chose (Evergreen Shield, with its enchant).
- orphans: seven tier files no record reads that held later-phase items (old "<tier>-raid" sets and the Beast-Survival sets of an
  older open search): removed (git rm).
"""
import argparse
import json
import pathlib
import subprocess
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
SETS = DATA / "raidsim" / "gear_sets" / "forever"
sys.path[:0] = [str(DATA / "raidsim"), str(DATA)]
ORPHANS = ["hunter-hybrid-beast-mastery-marksmanship-prebis-raid", "hunter-hybrid-beast-mastery-survival-bis",
           "hunter-hybrid-beast-mastery-survival-prebis", "hunter-marksmanship-bis-raid", "hunter-marksmanship-prebis-raid",
           "rogue-combat-prebis-raid", "shaman-hybrid-elemental-enhancement-prebis-raid"]


def shockadin():
    import run as R
    import gear_opt as G
    import gear_tiers as GT
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = G.load_db(repo)
    b = next(x for x in json.load(open(ROOT / "paladin/research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]
             if x["id"] == "shockadin-open-raid")
    trees = R.load_trees(repo, "paladin")
    tal = R.talents_string(trees, {n: r for items in b["allocation"].values() for n, r in items if r})
    path = SETS / "tiers" / "paladin-hybrid-holy-retribution-bis.gear.json"
    g = GT.make("paladin", "Hybrid Holy/Retribution", "bis", "shockadin-raid", tal, "page pick shockadin-open-raid", repo, db, zones,
                GT.args_ns(), path=path)
    late = [db[x["id"]]["name"] for x in json.load(open(path, encoding="utf-8"))["items"] if x and x.get("id") in db and G.later_phase(db[x["id"]], zones)]
    print(f"shockadin: {path.name} made again ({g.get('chosen')}, item level {g.get('ilvl')}); later-phase items left: {late or 'none'}")
    if late:
        raise SystemExit(1)


def tankshield():
    p = SETS / "paladin-protection-default.gear.json"
    d = json.load(open(p, encoding="utf-8"))
    src = json.load(open(SETS / "tiers" / "paladin-protection-bis.gear.json", encoding="utf-8"))["items"][15]
    old = d["items"][15]
    if old.get("id") == src.get("id"):
        print("tankshield: already done")
        return
    d["items"][15] = src
    p.write_text(json.dumps(d, indent="\t") + "\n", encoding="utf-8")   # the file's own tab layout
    print(f"tankshield: off hand {old.get('id')} -> {src.get('id')} (enchant {src.get('enchant')})")


def orphans():
    gone = []
    for stem in ORPHANS:
        f = SETS / "tiers" / f"{stem}.gear.json"
        if f.exists():
            subprocess.run(["git", "rm", "-q", "--", str(f.relative_to(ROOT))], cwd=ROOT, check=True)
            gone.append(stem)
    print(f"orphans: removed {len(gone)}: {', '.join(gone) or 'none left'}")


if __name__ == "__main__":
    {"shockadin": shockadin, "tankshield": tankshield, "orphans": orphans}[sys.argv[1]]()
