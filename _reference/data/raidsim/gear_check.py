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
import re
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


LIST_FILE = re.compile(r"-(dungeon|prebis|bis)(-nopvp)?(?:-(alliance|horde))?\.gear\.json$")
_GT = {}


def list_rule(repo, items, tier, nopvp, side, cls=None):
    """gear_tiers.list_guard on a set file (the database and the lists' context loaded once, through gear_tiers)."""
    if "GT" not in _GT:
        import gear_tiers as GT
        _GT["GT"], (_GT["db"], _GT["zones"]) = GT, GT.load_db(repo)
    return _GT["GT"].list_guard(items, tier, _GT["db"], _GT["zones"], repo, nopvp=nopvp, side=side, cls=cls)


def check_set(path, db, edb):
    """(missing items and enchants, number of filled slots) of a gear file; (["no file"], 0) when it does not exist."""
    if not path.exists():
        return ["no file"], 0
    items = items_of(path)
    return G.missing_in(items, db, edb), sum(1 for x in items if x and x.get("id"))


def page_files():
    """{path}: every set file a record the pages read names (the ML records' gear entries, the tanks' and healers' gear records)."""
    out = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "gear" and isinstance(v, str) and v.endswith(".gear.json"):
                    out.add((ROOT / v).resolve())
                else:
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for f in list(ML_DIR.glob("*.json")) + [HERE / "tank-gear.json", HERE.parent / "heallab" / "heal-gear.json"]:
        if f.exists():
            walk(json.load(open(f, encoding="utf-8")))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--pool", action="store_true", help="also list tier-set items outside the phase-1 pool (gear_opt.in_pool)")
    ap.add_argument("--quiet", action="store_true", help="print only the sets that fail")
    ap.add_argument("--lists-final", action="store_true",
                    help="after the all-class makes (make_lists.py's step 4): a list file a page reads that was made before the lists (no "
                         "\"rules\") fails too; before it such files are counted only (2026-11-23)")
    a = ap.parse_args()
    repo = R.SETUP.checkout("forever")
    (db, zones), edb = G.load_db(repo), G.enchant_db(repo)
    if a.pool:
        G.load_vetted(repo, db)
    specs = json.load(open(HERE / "specs.json", encoding="utf-8"))
    classes = a.classes or [c for c in specs if not c.startswith("_")]
    print(f"gear check on {repo} ({R.git_commit(repo)}; {len(db)} items in the database)")
    bad, older = 0, 0
    shown = page_files() if a.lists_final else set()
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
        tb, before = 0, []
        for f in tier_files:
            miss, n = check_set(f, db, edb)
            # 2026-11-23 (the audit session's rulings on the list test): a set file made under the lists (it carries "rules") passes its
            # list's rule: every item in the list's pool and every enchant in its enchant pool, a side's set only items its side can
            # use, a no-PvP set no item only PvP puts in its list (gear_tiers.list_guard, also run when the set is made); a failure is
            # fatal. A file without "rules" was made before the lists: counted, never skipped silently (after the all-class makes the
            # count must be 0 for every spec a page shows)
            m = LIST_FILE.search(f.name)
            if m:
                if json.load(open(f, encoding="utf-8")).get("rules"):
                    broken = list_rule(repo, items_of(f), m.group(1), bool(m.group(2)), (m.group(3) or "").capitalize() or None, cls=cls)
                    if broken:
                        bad += 1
                        print(f"    LIST RULE BROKEN {f.name}: " + "; ".join(broken))
                else:
                    before.append(f.name)
                    if f.resolve() in shown:
                        bad += 1
                        print(f"    MADE BEFORE THE LISTS, READ BY A PAGE {f.name} (--lists-final)")
            out = []
            if a.pool:
                out = [db[x["id"]]["name"] for x in items_of(f) if x and x.get("id") in db and not G.in_pool(db[x["id"]], zones)]
            if miss or out:
                tb += 1
                print(f"    tier set {f.name}: " + ("missing " + ", ".join(miss) if miss else "") + ("; " if miss and out else "")
                      + ("outside the pool: " + ", ".join(out) if out else ""))
        # 2026-11-23 (the audit session's read of make_lists.py): a record made under the lists describes the set in its file (the pages
        # and gear_links read records; the side feedback rewrites a file and then its record): every list entry of the class's ML
        # records with "rules" must name the file's items slot by slot, else fatal
        for mf in sorted(ML_DIR.glob(f"{cls}-*.json")):
            rec = json.load(open(mf, encoding="utf-8"))
            for key, g in (rec.get("gear") or {}).items():
                if not isinstance(g, dict) or not g.get("rules") or not g.get("gear") or g.get("names") is None:
                    continue
                gf = ROOT / g["gear"]
                if not gf.exists():
                    bad += 1
                    print(f"    RECORD WITHOUT ITS FILE {mf.name} {key}: {g['gear']}")
                    continue
                its = items_of(gf)
                have = [(db.get(x.get("id")) or {}).get("name") if x and x.get("id") else None for x in its]
                want = list(g["names"]) + [None] * (len(have) - len(g["names"]))
                diff = [(i, w_, h_) for i, (w_, h_) in enumerate(zip(want, have)) if (w_ or None) != (h_ or None)]
                if diff:
                    bad += 1
                    print(f"    RECORD AND FILE DIFFER {mf.name} {key}: " + "; ".join(f"slot {i}: record {w_}, file {h_}" for i, w_, h_ in diff[:6]))
        if tier_files and not a.quiet:
            print(f"    {cls}: {len(tier_files)} tier sets, {tb} with a missing item" + (" or an item outside the pool" if a.pool else ""))
        if before:
            older += len(before)
            print(f"    {cls}: {len(before)} tier sets made before the lists (no \"rules\" in the file, the list rule not checked)"
                  + ("" if a.quiet else ": " + ", ".join(before)))
    print(f"tier sets made before the lists: {older}")
    print("sets failing (entry sets missing gear, list rules broken):", bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
