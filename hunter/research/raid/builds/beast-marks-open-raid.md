# Beast-Marks — Raid (open talent search) — 27/21/3

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/21/3 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Marks (a Beast Mastery/Marksmanship hybrid) raid build the open talent search found on 2026-10-09: every legal 51-point build with no tree rule, searched in the community simulator's bm-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.4% over beast-marks-open-raid, the best of our builds in that rotation.

## Point allocation

### Beast Mastery (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 1/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 2/5 | unchanged | Gives your pet a 40% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Marksmanship (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Arcane Shot** | 3/5 | changed | Reduces the cooldown of your Arcane Shot by 0.9 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |

### Survival (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 3/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 3%. |

## Core talents (priority order)

1. **Careful Aim** — 49 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
2. **Lethal Attacks** — 42 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
3. **Mortal Shots** — 38 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
4. **Deadly Aspects** — 36 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
5. **Frenzy** — 29 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
6. **Bestial Discipline** — 26 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Unleashed Fury** — 23 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Ferocity** — 19 DPS lost without it (2% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**5 of 6** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) | ours: parse build | 31/20/0 | 489 | +0.0% | 843 | -1.4% | 25 s |
| 2 | [`beast-mastery-raid`](beast-mastery-raid.md) | ours: hand draft | 30/21/0 | 487 | -0.4% | 810 | -5.3% | 6 s |
| 3 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: hand draft | 28/23/0 | 479 | -2.0% | 833 | -2.6% | 18 s |
| 4 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 475 | -2.9% | 807 | -5.6% | 13 s |
| 5 | **[`beast-marks-open-raid`](beast-marks-open-raid.md)** | ours: hand draft | 27/21/3 | 474 | -3.1% | 855 | +0.0% | 23 s |
| 6 | *Beast Mastery 35/16/0* | community simulator | - | 462 | -5.5% | 789 | -7.8% | 14 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-09, 15 changes to the base rotation; third-seed check: open winner 427 -> 473 DPS (+10.7%), beast-marks-open-raid 450 -> 490 DPS (+8.9%), sim preset: Beast Mastery 35/16/0 437 -> 463 DPS (+5.9%), mm-hawk-raid 438 -> 475 DPS (+8.5%), beast-mastery-raid 449 -> 487 DPS (+8.6%), beast-marks-ml-raid 443 -> 480 DPS (+8.3%)):
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
  11. only above 60% mana: if auraIsInactive: cast Intimidation (+0.2%, pass 7)
  12. threshold 60% -> 70%: if auraIsInactive and mana % ≥ 60%: cast Intimidation (+0.3%, pass 8)
  13. insert at the top: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+19.8%, pass 10)
  14. threshold 30% -> 10%: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+2.9%, pass 10)
  15. only with 3s or more of the fight left: if time left on Serpent Sting < 4s: cast Serpent Sting (+0.4%, pass 10)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-09, 12 changes to the base rotation; third-seed check: open winner 718 -> 854 DPS (+18.9%), beast-marks-open-raid 805 -> 843 DPS (+4.7%), sim preset: Beast Mastery 35/16/0 761 -> 789 DPS (+3.7%), mm-hawk-raid 766 -> 807 DPS (+5.4%), beast-mastery-raid 776 -> 810 DPS (+4.5%), beast-mastery-ml-parse 805 -> 843 DPS (+4.6%), beast-marks-ml-raid 796 -> 833 DPS (+4.6%)):
  1. move to the top: if time to the next auto attack > 0.5s: cast Multi-Shot (+1.9%, pass 1)
  2. drop the condition: if time to the next auto attack > 1s: cast Summon Hawk (+0.4%, pass 1)
  3. threshold 1s -> 0.75s: if time left on Serpent Sting < 1s and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 2)
  4. threshold 0.75s -> 0.25s: if time left on Serpent Sting < 0.75s and mana % ≥ 30%: cast Serpent Sting + move to the top: if time left on Serpent Sting < 0.25s and mana % ≥ 30%: cast Serpent Sting (+0.3%, pass 3)
  5. drop: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 5)
  6. insert at the end: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.3%, pass 5)
  7. move down below 'cast Summon Hawk': if time to the next auto attack > 1s: cast Aimed Shot (+0.4%, pass 5)
  8. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 5)
  9. insert at the top: if time to the next auto attack > 1s: cast Summon Hawk + insert in the middle: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+0.8%, pass 6)
  10. only with 10s or more of the fight left: if time to the next auto attack > 1s: cast Summon Hawk (+0.2%, pass 6)
  11. drop: if time to the next auto attack > 1s and time left in the fight ≥ 10s: cast Summon Hawk (+1.1%, pass 10)
  12. drop the condition: if time to the next auto attack > 0.5s and mana % ≥ 30%: cast Arcane Shot (+0.3%, pass 11)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`beast-marks-open-raid`](beast-marks-open-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack > 0.5s and mana % ≥ 10%: cast Arcane Shot | 9.3 |
| 2 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s and time left in the fight ≥ 3s: cast Serpent Sting | 5.0 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`beast-marks-open-raid`](beast-marks-open-raid.md) |
|---|---|
| Auto Shot | 39% |
| Arcane Shot | 19% |
| Pet: Auto Attack | 18% |
| Serpent Sting | 17% |
| Pet: Claw | 6% |
| Pet: Bite | 0% |

## Notes

- +5.9% over the best hand draft of the spec, mm-hawk-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (bm-raid, full raid): 27/21/3 (Beast-Marks (a Beast Mastery/Marksmanship hybrid)) at 855.0 DPS; beast-marks-open-raid 843.3, beast-mastery-ml-parse 842.6, beast-marks-ml-raid 833.3, beast-mastery-raid 810.0, mm-hawk-raid 807.3 in the same fights; 4,589 builds simulated, 2 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): bm-mm-raid 806.2, opt-mm-raid-raid-dps 806.2.
- The bm-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): mm-raid +0.0%, mm-lonewolf-raid +0.2%, melee-dps -46.6%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Endurance Training, Improved Aspect of the Monkey, Improved Revive Pet, Improved Mend Pet.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-09 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Mend Pet -> Endurance Training (survival); Improved Revive Pet -> Endurance Training (survival); Improved Revive Pet -> Endurance Training (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Beast-Marks build: check it against the community's Beast-Marks builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/hunter/60/522102051500022-00530503005-3-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
