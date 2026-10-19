"""Repair the talent orders of saved fight-lab candidates that the current trees reject (2026-10-19).

    python _reference/data/candidate_orders.py [classes] [--write]

The 2026-10-03 repair of the 70170 trees fixed the candidates' allocations but kept their orders, so nine warrior candidates still
level through Boundless Rage (removed) with a Fury tier one point short. rebuild.py's race promotes an earlier round's candidate into
the optimizer build when it is faster, order included: on 2026-10-19 cand-aoe-r1 put that order into opt-arms-2h-raid-leveling-aoe
and the build failed validation. Each candidate whose allocation is legal but whose order is not gets the stats model's order for its
allocation (Optimizer.order under the candidate's model and profile: the main spec's leveling-st, a variant's own profile, by the
`cand-<tag>-` prefix), with a note. A candidate with an illegal allocation is only reported. rebuild.py calls `fix_order` before it
promotes a candidate.
"""
import argparse
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE / "fightlab"), str(HERE / "scorer"), str(HERE)]
import paths  # noqa: E402
import validate_builds as VB  # noqa: E402
from fmt_json import dumps  # noqa: E402

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
_TREES = {}


def trees(cls):
    if not _TREES:
        _TREES.update(VB.load_forever())
    return _TREES[cls]


def models(cls):
    """{candidate tag: (scorer model, profile, lookahead)} from the class module's PIPELINE."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("fl_run", HERE / "fightlab" / "run.py")   # not scorer/run.py (sys.path order varies)
    FR = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(FR)
    P = dict(__import__(FR.MODULES[cls][0]).PIPELINE)
    out = {P["tag"]: (P["spec"], "leveling-st", P.get("lookahead", 16))}
    for V in P.get("variants", []):
        out[V["tag"]] = (V["spec"], V["profile"], V.get("lookahead", P.get("lookahead", 16)))
    return out


def errors(cls, b):
    x = {"id": b.get("id", "?"), "allocation": b["allocation"], **({"order": b["order"]} if b.get("order") else {})}
    return VB.validate_build(trees(cls), x, b.get("id", "?"))


def fix_order(cls, b, tag):
    """Make `b` (a candidate dict) legal: an illegal allocation is repaired the way repair_builds.py repairs builds (renames carried,
    removed talents dropped, tier gating and the leftover points refilled by the stats model), then an illegal or lost order is
    replaced by the stats model's order for the allocation. Returns True when `b` changed and is now legal."""
    if not errors(cls, b):
        return False
    from optimize import Optimizer
    import repair_builds as RB
    model, profile, look = models(cls)[tag]
    opt = Optimizer("forever", cls, model, profile)
    if errors(cls, {"id": b.get("id"), "allocation": b["allocation"]}):
        old = "/".join(str(sum(r for _, r in v)) for v in b["allocation"].values())
        flat, log = RB.repair(cls, b, opt)
        alloc = {t: [] for t in opt.tree.order}
        for name in sorted(flat, key=lambda x: (opt.tree.info[x][1], x)):
            alloc[opt.tree.info[name][0]].append([name, flat[name]])
        b["allocation"] = alloc
        b.setdefault("notes", []).append(f"{datetime.date.today().isoformat()} (candidate_orders.py, repair_builds.repair, client build 70425 "
                                         f"trees): {old} -> {opt.tree.split(flat)}; " + "; ".join(log) + f" (the {model} model, {profile}).")
        b["order"] = b.get("order") or [{}]   # re-ordered below
    flat = {n: r for items in b["allocation"].values() for n, r in items if r}
    b["order"] = [{"levels": lv, "tree": t, "talent": n, "points": p} for lv, t, n, p in opt.compress_order(opt.order(flat, lookahead=look))]
    b.setdefault("notes", []).append(f"{datetime.date.today().isoformat()} (candidate_orders.py): the saved order named talents the current trees "
                                     f"lack; replaced by the stats model's {profile} order for the same allocation ({model}).")
    return not errors(cls, b)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for cls in a.classes or CLASSES:
        tags = models(cls)
        for f in sorted((paths.fightlab_dir(cls) / "candidates").glob("cand-*.json")):
            tag = f.stem.split("-")[1]
            b = json.load(open(f, encoding="utf-8"))
            err = errors(cls, b)
            if not err:
                continue
            if tag not in tags:
                print(f"{cls} {f.name}: invalid, no pipeline model for tag {tag!r}: {err[0]}")
                continue
            ok = fix_order(cls, b, tag)
            print(f"{cls} {f.name}: {'order replaced' if ok else 'NOT repaired'} ({len(err)} errors, first: {err[0]})")
            if ok and a.write:
                f.write_text(dumps(b) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
