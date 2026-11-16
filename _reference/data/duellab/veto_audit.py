"""The dropped-veto audit (2026-11-15, _reference/pvp-plan.md "Open before the searches"): the duel lab drops every tuned leveling veto
of a side's rotation (they are PvE rules), and Slice and Dice showed one can move a class 6-34 points a matchup. This restores each field
build's vetoes one at a time, inside its spec's rotation only (duel.restored_vetoes, pvp_base.PvPAI.rotation_decide: a layer's own casts
of the spell stay free), and scores the build against the field (pvp_field.score, common random numbers by duel index).

A veto is kept when it raises the build's mean win rate over the eight other classes (the mirror is left out: both of its sides
restore it) by 1 point on seed 1 and by 0.5 on seed 2, or, with the win rate within half a point on both seeds, its mean health margin
by 0.02 on both. A class's kept vetoes are then raced together on seed 3; when the set loses there, only the best single one stays.
Record duellab/veto-audit.json: its "kept" ({"<class>/<rotation>": [spell, ...]}) is what every duel plays from then on (duel.py), so
re-run the matrix (pvp_field.py --matrix --write) after a --write.

    python _reference/data/duellab/veto_audit.py [classes] [--n 200] [--workers 2] [--write]
"""
import argparse
import datetime
import json
import os
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import duel as D  # noqa: E402
import duel_run as DR  # noqa: E402
import pvp_field as PF  # noqa: E402

RECORD = HERE / "veto-audit.json"
WIN_BAR, WIN_CONFIRM, FLAT, MARGIN_BAR = 0.01, 0.005, 0.005, 0.02


def tuned_vetoes(cls, ref):
    """(rotation, {spell: rule}) of a field build: the rules' vetoes as a side would have them before the duel lab drops them."""
    alloc = DR.load_build(cls, ref)[1]
    spec = DR.side(cls, alloc)[2]
    mod = D.FR.make_module(cls, alloc, 60, spec)
    return spec, {k: dict(v) for k, v in (mod.veto or {}).items()}


def scored(cls, ref, restore, n, seed, workers):
    """{opponent class: (win, draw, margin)} of the build with `restore` ({key: [spells]}) played inside its rotation."""
    os.environ["WOW_DUEL_VETO"] = json.dumps(restore)
    try:
        return PF.score([(cls, ref)], n, seed, workers)[(cls, ref)]["by"]
    finally:
        os.environ.pop("WOW_DUEL_VETO", None)


def delta(cls, test, base):
    """(mean win change, mean margin change, {opponent: win change}) over the eight other classes."""
    opp = [c for c in base if c != cls]
    by = {c: round(test[c][0] - base[c][0], 4) for c in opp}
    return (statistics.mean(by.values()), statistics.mean(test[c][2] - base[c][2] for c in opp), by)


def passes(dw, dm, bar):
    return dw >= bar or (abs(dw) < FLAT and dm >= MARGIN_BAR)


def audit(cls, ref, n, workers, log=print):
    spec, tuned = tuned_vetoes(cls, ref)
    key = f"{cls}/{spec}"
    out = {"build": ref, "rotation": spec, "tuned": tuned, "tests": {}, "kept": []}
    if not tuned:
        log(f"{key}: no tuned vetoes")
        return key, out
    base = {1: scored(cls, ref, {}, n, 1, workers)}
    out["base_win"] = round(statistics.mean(v[0] for c, v in base[1].items() if c != cls), 4)
    log(f"{key} ({ref}): field win without the vetoes {out['base_win']:.1%} (eight classes)")
    for spell in sorted(tuned):
        s1 = scored(cls, ref, {key: [spell]}, n, 1, workers)
        dw, dm, by = delta(cls, s1, base[1])
        rec = {"rule": tuned[spell], "seed1": {"win": round(dw, 4), "margin": round(dm, 4), "by": by}}
        ok = passes(dw, dm, WIN_BAR)
        if ok:
            if 2 not in base:
                base[2] = scored(cls, ref, {}, n, 2, workers)
            dw2, dm2, by2 = delta(cls, scored(cls, ref, {key: [spell]}, n, 2, workers), base[2])
            rec["seed2"] = {"win": round(dw2, 4), "margin": round(dm2, 4), "by": by2}
            ok = passes(dw2, dm2, WIN_CONFIRM) if dw >= WIN_BAR else (abs(dw2) < FLAT and dm2 >= MARGIN_BAR)
        rec["kept"] = ok
        out["tests"][spell] = rec
        if ok:
            out["kept"].append(spell)
        log(f"  {spell} {json.dumps(tuned[spell])}: win {dw:+.1%}, margin {dm:+.3f}" + (
            f"; seed 2 win {rec['seed2']['win']:+.1%}, margin {rec['seed2']['margin']:+.3f}" if "seed2" in rec else "")
            + ("  KEPT" if ok else ""))
    if len(out["kept"]) > 1:
        base3 = scored(cls, ref, {}, n, 3, workers)
        dw3, dm3, by3 = delta(cls, scored(cls, ref, {key: out["kept"]}, n, 3, workers), base3)
        out["together"] = {"spells": list(out["kept"]), "win": round(dw3, 4), "margin": round(dm3, 4), "by": by3}
        log(f"  together {out['kept']}: seed 3 win {dw3:+.1%}, margin {dm3:+.3f}")
        if not passes(dw3, dm3, 0.0):
            best = max(out["kept"], key=lambda s: out["tests"][s]["seed1"]["win"] + out["tests"][s]["seed2"]["win"])
            out["kept"] = [best]
            log(f"  the set lost on seed 3: only {best} stays")
    return key, out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rec = json.load(open(RECORD, encoding="utf-8")) if RECORD.exists() else {}
    rec.setdefault("classes", {})
    for cls, ref in PF.FIELD:
        if a.classes and cls not in a.classes:
            continue
        key, out = audit(cls, ref, a.n, a.workers)
        rec["classes"][key] = out
        if a.write:
            rec["date"] = datetime.date.today().isoformat()
            rec["n"] = a.n
            rec["rule"] = ("kept: +1 point of mean win rate over the eight other classes on seed 1 and +0.5 on seed 2, or the win rate "
                           "within half a point on both and the mean health margin +0.02 on both; a class's kept vetoes together on "
                           "seed 3, else the best single one")
            rec["kept"] = {k: v["kept"] for k, v in sorted(rec["classes"].items()) if v.get("kept")}
            with open(RECORD, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    print("kept:", json.dumps({k: v["kept"] for k, v in rec["classes"].items() if v.get("kept")}))


if __name__ == "__main__":
    main()
