"""Re-tune one leveling rotation's rules after a mechanics change and keep whichever rule set is fastest (2026-11-06).

    python -u _reference/data/fightlab/rules_retune.py <class> <rotation> <build id> [--jobs 4] [--min-gain 0.003] [--dry-run]

`rotation_opt.py <class> --fresh --write` covers the class pipeline's rotations only, and a from-scratch run writes its result even when
the saved rules are faster (search-improvements.md, 2026-10-27 and open idea 0e of 2026-11-06: eight rule files of the 2026-11-02 patch
queue predated their class's module port). This runs rotation_opt's own search twice on the build, from scratch and continued from the
saved file, and compares the three rule sets on the tuner's final check (seed 3, --confirm fights per level, common random numbers):
the saved rules, the from-scratch rules and the continued rules. The fastest set that reaches the spec's signature floor is written to
fightlab/rotations/<class>-<rotation>.json when it beats the saved rules by --min-gain (default 0.3%); otherwise the saved file stays.
With no saved file the hand-written rotation is the reference. The record written is rotation_opt's own, plus a `retune` entry with
the three times. After an install: the rotation's open record from the 20-60 race on, then builds, races and reports.
"""
import argparse
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "scorer")]
import rotation_opt as RO  # noqa: E402
import run as FR  # noqa: E402

KEYS = ("veto", "drink_below", "eat_below", "knobs")


def rules_of(rec):
    return {k: rec[k] for k in KEYS if rec.get(k)}


def floor_ok(rec, which):
    """The rule set (`before`: the one the search started from, `after`: its result) reaches the spec's core-share floor and, since
    2026-11-06, casts every required spell the tuning build holds at every level (rotation_opt's `played_*`). The second half decides
    the Fire rules: the saved set never cast Pyroblast before Heating Up and was 0.4% faster than the set with the Pyroblast opener,
    so a comparison on speed alone would have kept it."""
    sig = rec.get("signature") or {}
    share, floor = sig.get(f"core_share_{which}"), sig.get("min_share")
    return (share is None or not floor or share >= floor) and sig.get(f"played_{which}", True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls")
    ap.add_argument("spec")
    ap.add_argument("build")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--min-gain", type=float, default=0.003)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--fights", type=int, default=600, help="rotation_opt's --fights (a smoke test lowers it)")
    ap.add_argument("--confirm", type=int, default=3000, help="rotation_opt's --confirm")
    ap.add_argument("--rounds", type=int, default=12, help="rotation_opt's --rounds")
    a = ap.parse_args()
    p = FR.rotation_file(a.cls, a.spec)
    base = dict(rounds=a.rounds, fights=a.fights, confirm=a.confirm, top=5, screen_gain=0.003, min_gain=0.004, jobs=a.jobs, write=False, spec=a.spec,
                build=a.build, cls=a.cls, all=False, check_rules=False)
    with multiprocessing.Pool(a.jobs, initializer=RO._init) as pool:
        _, levels = RO.targets(a.cls)
        print(f"=== {a.cls} {a.spec} on {a.build}: from scratch", flush=True)
        fresh = RO.search(pool, a.cls, a.spec, a.build, levels, argparse.Namespace(fresh=True, **base))
        cont = None
        if p.exists():
            print(f"=== {a.cls} {a.spec} on {a.build}: continued from the saved rules ({p.name})", flush=True)
            cont = RO.search(pool, a.cls, a.spec, a.build, levels, argparse.Namespace(fresh=False, **base))
    # the reference: the saved rules (the continued run's start), else the hand-written rotation (the from-scratch run's start)
    ref, ref_ok = (cont["weighted_before"], floor_ok(cont, "before")) if cont else (fresh["weighted_before"], floor_ok(fresh, "before"))
    cands = [("from scratch", fresh)] + ([("continued", cont)] if cont else [])
    ok = [(n, r) for n, r in cands if floor_ok(r, "after")] or cands
    name, best = min(ok, key=lambda x: x[1]["weighted_after"])
    gain = 1 - best["weighted_after"] / ref
    times = {"saved" if cont else "hand-written": round(ref, 3), **{n: round(r["weighted_after"], 3) for n, r in cands}}
    print(f"=== {a.cls} {a.spec}: " + ", ".join(f"{k} {v:.2f} s" for k, v in times.items())
          + f"; best {name} ({gain:+.2%} against the reference)"
          + ("" if ref_ok else "; the reference misses the signature floor or leaves a required spell uncast"), flush=True)
    same = cont is not None and rules_of(best) == rules_of(json.load(open(p, encoding="utf-8")))
    # kept: the best set is the saved one; or no set is faster by the bar while the reference plays its spec (or the best set does not
    # either: a slower set that fails the same check is no repair)
    if same or (gain < a.min_gain and (ref_ok or not floor_ok(best, "after"))):
        print(f"  kept: {'the saved rules' if cont else 'the hand-written rotation'} "
              + ("(the best set is the saved one)" if same else f"(no set {a.min_gain:.1%} faster)"), flush=True)
        return
    best = dict(best, retune={"times": times, "installed": name, "reference_ok": ref_ok})
    print(f"  {'would install' if a.dry_run else 'installed'}: the {name} rules {json.dumps(rules_of(best))}", flush=True)
    if not a.dry_run:
        FR.ROTATIONS.mkdir(exist_ok=True)
        tmp = p.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(best, indent=1), encoding="utf-8")
        tmp.replace(p)
        print(f"  wrote {p.name}", flush=True)


if __name__ == "__main__":
    main()
