"""Static check of the gear sets the raid tools run in (2026-11-06, page-audit.md J3; user: "Go with your recs").

    python _reference/data/raidsim/gear_check.py [classes] [--pool] [--quiet]      # exit 1 when an entry's set fails

The item database moves under the gear tools (CLAUDE.md, 2026-11-05): the 2026-10-30 update dropped a third of the items, the bench
empties the slot of an item the database lacks and reports `missing_gear`, and nothing read that report, so every raid number from
that re-pin on ran with one or two empty slots in all 14 standard sets. This reads, without a simulator run, on the checkout the
tools would use (setup.checkout(): WOW_FOREVER_SIM or the main clone):
  * every raid entry's gear set (specs.json `gear`: a project file or one of the checkout's presets): items and enchants the
    database lacks, and empty slots a complete set must fill (gear_complete's slots);
  * every tier set of the class's ML records (`raidsim/ml/<class>-*.json`, key `gear`) and of gear_sets/forever/tiers/: the same,
    and with --pool the items outside the tier's pool (gear_opt.in_pool with the tier's rules: PvP rewards, later raids' quest
    rewards, later reputations).
An entry set that fails is an error (exit 1): `run.check_bench_stderr` stops every bench run that reports missing gear since the same
day, so fix the set first (gear_opt.py <class> --write --fresh, then --apply; tank and healer sets: tank_gear.py). Tier sets are
listed only: gear_tiers.py and the ML final step re-make them. Run it after every re-pin, next to spec_check.py.
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_opt as G  # noqa: E402
import run as R  # noqa: E402

TIERS = HERE / "gear_sets" / "forever" / "tiers"
ML_DIR = HERE / "ml"


def items_of(path):
    return [x for x in json.load(open(path, encoding="utf-8")).get("items", [])]


def resolve(repo, rel):
    p = pathlib.Path(R.sim_path(rel))
    return p if p.is_absolute() else pathlib.Path(repo) / rel


def check_set(path, db, edb):
    """(missing items and enchants, number of filled slots) of a gear file; (["no file"], 0) when it does not exist."""
    if not path.exists():
        return ["no file"], 0
    items = items_of(path)
    return G.missing_in(items, db, edb), sum(1 for x in items if x and x.get("id"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--pool", action="store_true", help="also list tier-set items outside the phase-1 pool (gear_opt.in_pool)")
    ap.add_argument("--quiet", action="store_true", help="print only the sets that fail")
    a = ap.parse_args()
    repo = R.SETUP.checkout("forever")
    (db, zones), edb = G.load_db(repo), G.enchant_db(repo)
    if a.pool:
        G.load_vetted(repo, db)
    specs = json.load(open(HERE / "specs.json", encoding="utf-8"))
    classes = a.classes or [c for c in specs if not c.startswith("_")]
    print(f"gear check on {repo} ({R.git_commit(repo)}; {len(db)} items in the database)")
    bad = 0
    for cls in classes:
        seen = {}
        for name, e in specs.get(cls, {}).items():
            if isinstance(e, dict) and e.get("gear"):
                seen.setdefault(e["gear"], []).append(name)
        for rel, names in seen.items():
            miss, n = check_set(resolve(repo, rel), db, edb)
            if miss:
                bad += 1
            if miss or not a.quiet:
                print(f"  {cls} {', '.join(names)}: {pathlib.Path(rel).name}: {n} slots filled; "
                      + ("MISSING " + ", ".join(f"{m} ({G.item_name(db, int(m.split(':')[1])) if m.startswith('item:') else 'enchant'})" for m in miss)
                         if miss and miss != ["no file"] else "NO FILE" if miss else "complete"))
        tier_files = sorted(TIERS.glob(f"{cls}-*.gear.json"))
        tb = 0
        for f in tier_files:
            miss, n = check_set(f, db, edb)
            out = []
            if a.pool:
                out = [db[x["id"]]["name"] for x in items_of(f) if x and x.get("id") in db and not G.in_pool(db[x["id"]], zones)]
            if miss or out:
                tb += 1
                print(f"    tier set {f.name}: " + ("missing " + ", ".join(miss) if miss else "") + ("; " if miss and out else "")
                      + ("outside the pool: " + ", ".join(out) if out else ""))
        if tier_files and not a.quiet:
            print(f"    {cls}: {len(tier_files)} tier sets, {tb} with a missing item" + (" or an item outside the pool" if a.pool else ""))
    print("entry sets failing:", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
