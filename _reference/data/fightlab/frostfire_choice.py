"""What playing Frostfire Bolt while leveling costs (2026-11-21; the user's decision, relayed by the audit session, "Go with your
recommendations": the Frostfire leveling page levels as Frost and switches at 60, with a short section "If you want to play Frostfire Bolt
while leveling" and this cost table; spec_modes.LEVEL_AS_CHOICE).

Three ways to reach 60 on the same footing (the pages' fight-lab setting: quest greens, same-level single pulls, each pick's tuned rules;
seeds 1 and 2, FIGHTS fights a level):
  frost  the Frost page's pick, which the Frostfire page levels as;
  ffb40  the Frostfire page's leveling pick, Frostfire Bolt in place of Frostbolt from its talent (40; mage.FROSTFIRE_FROM 0);
  ffb48  the same build keeping Frostbolt until 48 (mage.FROSTFIRE_FROM 48), the cheapest way to play it that the 2026-11-21 sweep found.
Record fightlab/frostfire-choice.json (render_modes.level_as_choice reads it; `fingerprints` holds level_guides.fingerprint of each pick, so
a page can tell a record made on other builds or rules). Run it after the mage's leveling picks or rules change:
    python _reference/data/fightlab/frostfire_choice.py [--jobs 10]"""
import argparse
import datetime
import json
import multiprocessing
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
sys.path[:0] = [str(HERE), str(DATA)]
OUT = HERE / "frostfire-choice.json"
LEVELS = [20, 30] + list(range(40, 61, 2))
FIGHTS = 2000
SEEDS = (1, 2)
VARIANTS = (("frost", "Frost", 0), ("ffb40", "Hybrid Fire/Frost", 0), ("ffb48", "Hybrid Fire/Frost", 48))


def _init():
    import level_guides as LG
    LG._init()   # the pages' setting: quest greens


def _job(a):
    var, knob, level, seed, alloc, rot = a
    import run as FR
    modname, clsname = FR.MODULES["mage"]
    getattr(__import__(modname), clsname).FROSTFIRE_FROM = knob
    r = FR.simulate("mage", alloc, level, rot, FIGHTS, seed, 0)
    return var, level, seed, r.get("time_per_kill")


def weighted(per):
    """The pages' level weighting (render_modes.weighted): levels 20, 30, 40, 50 and 60, each weighing its level / 10."""
    per = {L: v for L, v in per.items() if L in (20, 30, 40, 50, 60)}
    tot = sum(L / 10 for L in per)
    return sum(v * L / 10 for L, v in per.items()) / tot if tot else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--jobs", type=int, default=10)
    a = ap.parse_args()
    import level_guides as LG
    import run as FR
    jobs, picks = [], {}
    for var, spec, knob in VARIANTS:
        b, order, prov, rot = LG.pick("mage", spec)
        if not b:
            raise SystemExit(f"no leveling pick for {spec}")
        picks[var] = {"spec": spec, "build": b["id"], "rotation": rot, "frostfire_from": knob, "provisional_order": prov,
                      "fingerprint": LG.fingerprint("mage", b, order, rot)}
        ob = {"allocation": b["allocation"], "order": order}
        jobs += [(var, knob, L, s, FR.allocation_at(ob, L), rot) for L in LEVELS for s in SEEDS]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        res = pool.map(_job, jobs, chunksize=1)
    t = {}
    for var, L, s, v in res:
        t.setdefault(var, {}).setdefault(L, {})[s] = v
    per = {var: {L: sum(d.values()) / len(d) for L, d in sorted(t[var].items())} for var in t}
    rec = {"date": datetime.date.today().isoformat(), "fights": FIGHTS, "seeds": list(SEEDS), "levels": LEVELS, "gear": "greens",
           "variants": {var: dict(picks[var], per_level={str(L): round(v, 3) for L, v in per[var].items()},
                                  by_seed={str(L): {str(s): round(x, 3) for s, x in d.items()} for L, d in sorted(t[var].items())},
                                  weighted=round(weighted(per[var]), 3)) for var in picks}}
    OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    base = rec["variants"]["frost"]["weighted"]
    for var in picks:
        w = rec["variants"][var]["weighted"]
        print(f"{var:6s} {picks[var]['build']:32s} 20-60 weighted {w:6.2f} s ({w / base - 1:+.1%} against levelling as Frost)", flush=True)
    print(f"wrote {OUT.relative_to(DATA.parents[1])}")


if __name__ == "__main__":
    main()
