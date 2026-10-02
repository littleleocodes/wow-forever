# Beast Mastery — Raid (derived) — 30/21/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/21/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery raid damage build derived on 2026-09-30 (derive_raid.py): the community simulator's talent search (raidsim/talent_opt.py, entry bm-raid, training dummy) from the spec's best build beast-mastery-raid, 30+ points kept in Beast Mastery.

## Point allocation

### Beast Mastery (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Revive Pet** | 2/2 | unchanged | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Marksmanship (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increased the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 4/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 12%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Mortal Shots** | 3/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 18%. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**2 of 5** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: hand draft | 23/28/0 | 473 | +0.0% | 808 | -0.5% | 18 s |
| 2 | **[`beast-mastery-raid`](beast-mastery-raid.md)** | ours: hand draft | 30/21/0 | 465 | -1.8% | 793 | -2.3% | 22 s |
| 3 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 461 | -2.6% | 810 | -0.2% | 26 s |
| 4 | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) | ours: parse build | 31/20/0 | 450 | -5.0% | 812 | +0.0% | 30 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 431 | -8.8% | 762 | -6.1% | 28 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-02, 10 changes to the base rotation; third-seed check: ml: Beast Mastery 433 -> 465 DPS (+7.4%), ml: Hybrid Beast Mastery/Marksmanship 442 -> 473 DPS (+6.9%), beast-mastery-raid 433 -> 464 DPS (+7.2%), sim preset: Beast Mastery 35/16/0 406 -> 432 DPS (+6.4%)):
  1. drop: use every other cooldown when ready (+3.0%, pass 1)
  2. drop: if time to the next auto attack > 1s: cast Aimed Shot (+0.5%, pass 1)
  3. drop: if time to the next auto attack > 0.5s: cast Multi-Shot (+2.1%, pass 1)
  4. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and mana % ≥ 30%: cast Serpent Sting (+2.8%, pass 1)
  5. drop the condition: if time to the next auto attack > 1s: cast Summon Hawk (+0.8%, pass 1)
  6. move down below 'cast Summon Hawk': if time left on Serpent Sting < 1s: cast Serpent Sting (+0.9%, pass 1)
  7. insert before the filler: use every other cooldown when ready (+3.8%, pass 2)
  8. threshold 1s -> 2s: if time left on Serpent Sting < 1s: cast Serpent Sting (+0.4%, pass 2)
  9. threshold 2s -> 4s: if time left on Serpent Sting < 2s: cast Serpent Sting (+1.3%, pass 2)
  10. spell probe: insert at the end: if auraIsInactive: cast Intimidation (+0.5%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 8 changes to the base rotation; third-seed check: ml: Beast Mastery 762 -> 787 DPS (+3.3%), ml: Hybrid Beast Mastery/Marksmanship 782 -> 808 DPS (+3.2%), beast-mastery-raid 768 -> 793 DPS (+3.3%), sim preset: Beast Mastery 35/16/0 741 -> 763 DPS (+3.0%)):
  1. move to the top: if time to the next auto attack > 0.5s: cast Multi-Shot (+1.9%, pass 1)
  2. drop the condition: if time to the next auto attack > 1s: cast Summon Hawk (+0.4%, pass 1)
  3. threshold 1s -> 0.75s: if time left on Serpent Sting < 1s and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 2)
  4. threshold 0.75s -> 0.25s: if time left on Serpent Sting < 0.75s and mana % ≥ 30%: cast Serpent Sting + move to the top: if time left on Serpent Sting < 0.25s and mana % ≥ 30%: cast Serpent Sting (+0.3%, pass 3)
  5. drop: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 5)
  6. insert at the end: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.3%, pass 5)
  7. move down below 'cast Summon Hawk': if time to the next auto attack > 1s: cast Aimed Shot (+0.4%, pass 5)
  8. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 5)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`beast-mastery-raid`](beast-mastery-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 2 | cast Summon Hawk | 10.0 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s: cast Serpent Sting | 4.7 |

Lines of the simulator's rotation these builds never cast: cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`beast-mastery-raid`](beast-mastery-raid.md) |
|---|---|
| Auto Shot | 38% |
| Summon Hawk | 28% |
| Serpent Sting | 22% |
| Pet: Auto Attack | 8% |
| Pet: Claw | 1% |
| Pet: Bite | 1% |

## Notes

- Simulator talent search from beast-mastery-raid: 1 point Intimidation -> Endurance Training; 2 points Mortal Shots -> Efficiency (+2.2% DPS on the search's third seed).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements.

## Open questions (verify in the live game)

- A derived Beast Mastery raid build: check it against the community's Beast Mastery builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
