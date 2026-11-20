"""The hunter pet's swing against upstream's in-game evidence (2026-11-20, the independent audit's H15 follow-up: "make it a small check
in the repo ... so a later change cannot drift from it unseen").

Upstream's EV-0071 (wowsims/forever docs/evidence/EV-0071-hunter-cat-swing-level-30.md): one combat log of a level-30 Cat at 1.2 s with
Unleashed Fury 5/5, 152 swings that are neither crits nor glancing blows. Damage before armor, logged against the normalized model:

    pet attack power 119: logged 42-55, model 42.4-55.6
    pet attack power 146: logged 46-59, model 46.1-59.2

The lab's pet (hunter.make_pet, engine.pet_swing; tables.PET_SWING_NORMALIZED) must give the model's range within 0.3 at both.

    python _reference/data/fightlab/pet_swing_check.py      (exit 1 on a drift)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
NOTE = {119: (42.4, 55.6), 146: (46.1, 59.2)}
TOLERANCE = 0.3


def main():
    import os
    os.chdir(HERE.parents[2])
    import tables
    import run as FR
    if not tables.PET_SWING_NORMALIZED:
        print("PET_SWING_NORMALIZED is off: the check reads the normalized swing only")
        return 1
    mod = FR.make_module("hunter", {"Unleashed Fury": 5}, 30, "bm-leveling")
    pet = mod.make_pet(30, mod.make_player(30))
    bad = 0
    for ap, (lo_n, hi_n) in NOTE.items():
        f = (pet.norm_speed / 2.0) * pet.dmg_mult
        lo, hi = (pet.dmg_min + ap / 14.0 * 2.0) * f, (pet.dmg_max + ap / 14.0 * 2.0) * f
        ok = abs(lo - lo_n) <= TOLERANCE and abs(hi - hi_n) <= TOLERANCE
        bad += not ok
        print(f"{'ok  ' if ok else 'DRIFT'} attack power {ap}: the lab {lo:.1f}-{hi:.1f}, EV-0071's model {lo_n}-{hi_n}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
