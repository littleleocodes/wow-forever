"""Repair the builds a new talent tree breaks (2026-10-16, client 70425: 55 priest, shaman, mage and warlock builds).

    python _reference/data/repair_builds.py [classes] [--write]

Per build that fails on the current trees: talents the client renamed carry their points (RENAMES: same cell, same effect, a new name);
talents that are gone lose theirs, ranks above a new cap are trimmed; tier gating is restored from the lowest tier up (one point at a
time, the talent the build's stats model values most among the legal additions below the gap, in the same tree); a prerequisite that
cannot be met drops its dependant; the points left over are spent by the stats model's greedy refill (`Optimizer.refill`). The model is
the build's own (optimizer builds name it in their id) or the nearest one for its lead tree and content (MODEL). A leveling build loses
its `order` (run order_repair.py, or raid_path_leveling.py for `raid_path` builds, once the fight-lab modules are current). Every repaired
build gets a note. The searches that follow a refresh redo the builds; this only keeps the hand drafts legal and close to their intent.
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "scorer"), str(HERE / "fightlab"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
from fmt_json import dumps  # noqa: E402
from optimize import Optimizer, TOTAL  # noqa: E402
import validate_builds as VB  # noqa: E402
import data_build as DB  # noqa: E402

TODAY = datetime.date.today().isoformat()
# old name -> new name: the client renamed the talent in place and kept what it does (70425: Improved Fire Nova -> Trial by Fire adds
# Magma Totem duration; Wake of Fire -> Improved Fire Blast keeps the cooldown and drops the on-kill crit). Malediction -> Grim Reach and
# Improved Fade -> Dark Inspiration share a cell but not an effect: not renames.
# 70707 (live hotfixes of 28-30 Oct): Improved Fireball -> Accelerant (same cell, still the Fireball cast time, plus Arcane Wrath), Elemental
# Precision -> Precision (same cell, hit for every school); Gift of the Earthmother's cell now holds Bloom, a different effect: not a rename.
RENAMES = {"shaman": {"Improved Fire Nova": "Trial by Fire"},
           "mage": {"Wake of Fire": "Improved Fire Blast", "Improved Fireball": "Accelerant", "Elemental Precision": "Precision"}}


def model_for(cls, b, lead):
    """(scorer model, profile) for refilling a build."""
    content, role = b.get("content"), b.get("role")
    profile = {"leveling": "leveling-st", "solo": "solo-60", "pvp": "pvp"}.get(content, "raid-heal" if role == "healer" else "raid-dps")
    if b["id"].startswith("opt-"):
        import importlib.util
        s = importlib.util.spec_from_file_location("fl_run", HERE / "fightlab" / "run.py")   # not scorer/run.py
        FR = importlib.util.module_from_spec(s)
        s.loader.exec_module(FR)
        m = FR.spec_of_build(cls, b["id"], None)
        if m:
            return m, b["id"][4 + len(m) + 1:]
    lev = content in ("leveling", "solo")
    M = {"priest": "holy-heal" if role == "healer" else "shadow-dps",
         "shaman": "resto-heal" if role == "healer" else "elemental-dps" if lead == "Elemental" else "enhancement-dps",
         "mage": ("fire-leveling" if lead == "Fire" else "frost-leveling") if lev else ("fire-raid" if lead == "Fire" else "frost-raid"),
         "warlock": "affliction-leveling" if lev else ("affliction-raid" if lead == "Affliction" else
                                                         "fire-destro-raid" if "fire" in b["id"] else "sb-raid"),
         "druid": "resto-heal" if role == "healer" else "feral-bear-tank" if role == "tank" else "balance-dps" if lead == "Balance"
                  else "resto-heal" if lead == "Restoration" else "feral-cat-dps",
         "hunter": "bm-leveling" if lev and lead == "Beast Mastery" else "melee-dps" if lead == "Survival" or "melee" in b["id"]
                   else "mm-raid"}
    return M[cls], profile


def repair(cls, b, opt):
    tree = opt.tree
    ren = RENAMES.get(cls, {})
    flat, log = {}, []
    for items in b["allocation"].values():
        for n, r in items:
            if not r:
                continue
            n2 = ren.get(n, n)
            if n2 != n:
                log.append(f"{n} -> {n2} (renamed)")
            if n2 not in tree.info:
                log.append(f"{n} {r} gone")
                continue
            mx = tree.info[n2][2]
            if r > mx:
                log.append(f"{n2} {r} -> {mx} (rank cap)")
                r = mx
            flat[n2] = flat.get(n2, 0) + r
    for _ in range(TOTAL * 2):   # tier gating, lowest gap first, filled in its own tree below the gap
        bad = sorted((tree.info[n][1], n) for n, r in flat.items()
                     if tree.points_below(flat, tree.info[n][0], tree.info[n][1]) < tree.info[n][1] * 5)
        if not bad:   # then prerequisites a new rank cap left short (70425: Combustion needs Critical Mass 5/5, it had 3 ranks)
            short = [(rn, n) for n in flat for rn, rr in tree.info[n][3] if flat.get(rn, 0) < rr and tree.can_add(flat, rn)]
            if not short:
                break
            rn, n = short[0]
            flat[rn] = flat.get(rn, 0) + 1
            log.append(f"+1 {rn} (prerequisite of {n})")
            continue
        row, n = bad[0]
        tname = tree.info[n][0]
        cands = [m for m, (t, rw, mx, req) in tree.info.items() if t == tname and rw < row and tree.can_add(flat, m)]
        if not cands:
            break
        base = opt.score(flat)
        best = max(cands, key=lambda m: opt.score({**flat, m: flat.get(m, 0) + 1}) - base)
        flat[best] = flat.get(best, 0) + 1
        log.append(f"+1 {best} (tier gating for {n})")
    while sum(flat.values()) > TOTAL:   # a moved talent's gating filled past 51: give back the point the model misses least
        base = opt.score(flat)
        cands = [n for n in flat if tree.legal({**flat, n: flat[n] - 1})]
        if not cands:
            break
        n = min(cands, key=lambda m: base - opt.score({**flat, m: flat[m] - 1}))
        flat[n] -= 1
        if not flat[n]:
            del flat[n]
        log.append(f"-1 {n} (over 51)")
    while not tree.legal(flat):   # what gating or a lost prerequisite still breaks: drop the deepest offender
        off = [n for n, r in flat.items() if tree.points_below(flat, tree.info[n][0], tree.info[n][1]) < tree.info[n][1] * 5
               or any(flat.get(rn, 0) < rr for rn, rr in tree.info[n][3])]
        n = max(off, key=lambda x: tree.info[x][1])
        log.append(f"{n} {flat.pop(n)} dropped (illegal)")
    before = dict(flat)
    flat = opt.refill(flat)
    added = {n: flat[n] - before.get(n, 0) for n in flat if flat[n] != before.get(n, 0)}
    if added:
        log.append("refill " + ", ".join(f"+{k} {n}" for n, k in added.items()))
    return flat, log


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    FT = VB.load_forever()
    for cls in a.classes or SM.CLASSES:
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        trees = FT[cls]
        opts, n = {}, 0
        for b in data["builds"]:
            if not VB.validate_build(trees, b, b["id"]):
                continue
            tree_pts = {t: sum(r for _, r in v) for t, v in b["allocation"].items()}
            lead = max(tree_pts, key=tree_pts.get)
            mp = model_for(cls, b, lead)
            if mp not in opts:
                opts[mp] = Optimizer("forever", cls, *mp)
            opt = opts[mp]
            flat, log = repair(cls, b, opt)
            alloc = {t: [] for t in opt.tree.order}
            for name in sorted(flat, key=lambda x: (opt.tree.info[x][1], x)):
                alloc[opt.tree.info[name][0]].append([name, flat[name]])
            old = "/".join(str(v) for v in tree_pts.values())
            b["allocation"] = alloc
            if b.get("order"):
                b.pop("order", None)
                b.pop("order_label", None)
                log.append("order dropped (order_repair.py)")
            b.setdefault("notes", []).append(f"{TODAY} (repair_builds.py, client build {DB.BUILD} trees): {old} -> {opt.tree.split(flat)}; "
                                             + "; ".join(log) + f" (refill: the {mp[0]} model, {mp[1]}).")
            errs = VB.validate_build(trees, b, b["id"])
            print(f"{cls} {b['id']}: {old} -> {opt.tree.split(flat)} [{mp[0]} {mp[1]}] {'; '.join(log)}"
                  + (f"  STILL INVALID: {errs[:3]}" if errs else ""), flush=True)
            n += 1
        if n and a.write:
            bp.write_text(dumps(data) + "\n", encoding="utf-8")
            print(f"wrote {bp} ({n} builds)", flush=True)


if __name__ == "__main__":
    main()
