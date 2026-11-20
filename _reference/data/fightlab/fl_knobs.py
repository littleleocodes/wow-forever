"""The fight-lab pass's knobs (2026-11-19/20, the independent audit's step 6): every leveling page pick, level-weighted at 20/30/40/50/60,
under a knob configuration. The audit's checks at every change of the pass: (a) "off" reproduces the lab before (compare with a run of
the same picks in a worktree of the commit before), (b) "off" against "on", (c) each knob alone against "off".
  off      every knob of the pass at its "lab before" value (OFF)
  on       every knob at its default
  <knob>   all off but that one knob (the classes it touches: TOUCHES, else its module's class)

    python _reference/data/fightlab/fl_knobs.py <config name> <out.json> [--fights 3000] [--seed 1] [--classes a,b] [--jobs 8]

How the knobs are set: tables' knobs before any class module is imported (the modules filter their spellbooks by TRAINER_RANKS when they
load), then each module's knob on the module after import; a knob the module reads while it parses its spellbook (warlock AGONY_TICK_2S,
rogue GARROTE_AP_PER_TICK: BOOK_KNOBS) rebuilds that module's BOOK. Every pool worker applies the configuration itself (Windows spawns,
so the parent's settings do not carry). Add a knob here whenever the pass gains one.
"""
import argparse
import json
import multiprocessing
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
DATA = ROOT / "_reference" / "data"
LEVELS = (20, 30, 40, 50, 60)
OFF = {   # knob: its "lab before" value
    "tables.TRAINER_RANKS": False, "tables.MISS_REFUND": 0.0, "tables.BASE_STAT_TABLE": False, "tables.STAT_FIRST_20": False,
    "tables.RAGE_TAKEN_MODEL": "forever", "tables.UNAVOIDABLE_RULE": False, "tables.PET_SWING_NORMALIZED": False,
    "paladin.VINDICATION_PPM": 0.0,
    "warlock.TORMENT_TABLE": False, "warlock.VOIDWALKER_MELEE": 1.0, "warlock.AGONY_TICK_2S": False,
    "rogue.EVIS_AP_PER_POINT": 0.03, "rogue.GARROTE_AP_PER_TICK": 0.0, "rogue.GARROTE_TICKS_CRIT": False, "rogue.POISON_SPELL_CRIT": False,
    "rogue.DEATH_MARK_OFFICIAL": False,
    "hunter.QUIVER_HASTE": 0.0, "hunter.SERPENT_TICKS_CRIT": False,
    "priest.REGEN_RATES_ADD": False, "shaman.LS_OFFICIAL": False,
    "mage.FOF_ONE_ROLL": False, "mage.ARCANE_ANY_ROTATION": False, "mage.IB_MULTIPLY": False, "mage.IB_REFRESH": False,
    "mage.FB_IL_SHARED_CD": False, "mage.SHATTER_AM": False, "mage.WC_TEXT": False,
}
# the classes each knob touches (its single-knob run measures only their picks)
TOUCHES = {"tables.TRAINER_RANKS": None, "tables.MISS_REFUND": ["druid", "rogue", "warrior"], "tables.BASE_STAT_TABLE": None,
           "tables.STAT_FIRST_20": None, "tables.RAGE_TAKEN_MODEL": ["warrior"], "tables.UNAVOIDABLE_RULE": ["warrior", "hunter"],
           "tables.PET_SWING_NORMALIZED": ["hunter"]}
BOOK_KNOBS = {"warlock.AGONY_TICK_2S", "rogue.GARROTE_AP_PER_TICK"}   # read when the module builds its spell book


def config(name):
    if name == "on":
        return {}
    if name == "off":
        return dict(OFF)
    c = dict(OFF)
    c.pop(name)
    return c


def apply(cfg):
    sys.path[:0] = [str(DATA / "fightlab"), str(DATA)]
    import tables
    for k, v in cfg.items():
        if k.startswith("tables."):
            setattr(tables, k.split(".", 1)[1], v)
    import importlib
    rebuild = set()
    for k, v in cfg.items():
        mod, *attr = k.split(".")
        if mod == "tables":
            continue
        m = importlib.import_module(mod)
        obj = m
        for a in attr[:-1]:
            obj = getattr(obj, a)
        setattr(obj, attr[-1], v)
        if k in BOOK_KNOBS:
            rebuild.add(mod)
    for mod in rebuild:
        m = importlib.import_module(mod)
        m.BOOK = m.load_spellbook()


def init(cfg):
    import os
    os.chdir(ROOT)
    apply(cfg)


def job(j):
    import run as FR
    cls, rot, alloc, L, fights, seed = j
    return FR.simulate(cls, alloc, L, rot, fights, seed, 0)["time_per_kill"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("out")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--classes")
    ap.add_argument("--jobs", type=int, default=8)
    a = ap.parse_args()
    cfg = config(a.name)
    classes = a.classes.split(",") if a.classes else (
        TOUCHES.get(a.name) or ([a.name.split(".")[0]] if a.name not in ("on", "off") and not a.name.startswith("tables.") else
                                ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]))
    init(cfg)
    import run as FR
    import importlib.util
    spec = importlib.util.spec_from_file_location("sa", str(DATA / "fightlab" / "signature_audit.py"))
    SA = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SA)
    picks = []
    for cls in classes:
        for s, ranked, rots, gone, level_as in SA.page_slots(cls, signature=True):
            b = (ranked or gone or [None])[0]
            if b:
                picks.append((cls, s, b["id"], rots.get(b["id"]), b))
    jobs = [(cls, rot, FR.allocation_at(b, L), L, a.fights, a.seed) for cls, s, bid, rot, b in picks for L in LEVELS]
    with multiprocessing.Pool(a.jobs, initializer=init, initargs=(cfg,)) as pool:
        res = pool.map(job, jobs, chunksize=1)
    out = {}
    for i, (cls, s, bid, rot, b) in enumerate(picks):
        per = {L: res[i * len(LEVELS) + k] for k, L in enumerate(LEVELS)}
        w = sum(per[L] * L / 10 for L in LEVELS) / sum(L / 10 for L in LEVELS)
        out[f"{cls}/{s}"] = {"build": bid, "rotation": rot, "weighted": w, "levels": {str(L): v for L, v in per.items()}}
    pathlib.Path(a.out).write_text(json.dumps({"config": a.name, "fights": a.fights, "seed": a.seed, "picks": out}, indent=1), encoding="utf-8")
    print(a.name, len(out), "picks")


if __name__ == "__main__":
    main()
