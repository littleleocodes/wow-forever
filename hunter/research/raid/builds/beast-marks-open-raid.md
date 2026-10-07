# Beast-Marks — Raid (open talent search) — 27/19/5

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/19/5 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Marks (a Beast Mastery/Marksmanship hybrid) raid build the open talent search found on 2026-10-07: every legal 51-point build with no tree rule, searched in the community simulator's bm-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.9% over beast-mastery-ml-parse, the best of our builds in that rotation.

## Point allocation

### Beast Mastery (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 4/5 | changed | Increases the Health and Armor of your pets by 12%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 1/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 2/5 | unchanged | Gives your pet a 40% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Marksmanship (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 2/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 6%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Mortal Shots** | 4/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 24%. |

### Survival (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |

## Core talents (priority order)

1. **Summon Hawk** — 60 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
2. **Careful Aim** — 49 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
3. **Lethal Attacks** — 42 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
4. **Deadly Aspects** — 40 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
5. **Unleashed Fury** — 37 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
6. **Improved Tracking** — 35 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Mortal Shots** — 28 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Ferocity** — 27 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 6** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`beast-marks-open-raid`](beast-marks-open-raid.md)** | ours: hand draft | 27/19/5 | 505 | +0.0% | 903 | +0.0% | 20 s |
| 2 | [`beast-mastery-raid`](beast-mastery-raid.md) | ours: hand draft | 30/21/0 | 499 | -1.2% | 867 | -3.9% | 6 s |
| 3 | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) | ours: parse build | 31/20/0 | 498 | -1.4% | 895 | -0.8% | 25 s |
| 4 | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) | ours: hand draft | 28/23/0 | 493 | -2.4% | 890 | -1.4% | 18 s |
| 5 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 490 | -2.9% | 868 | -3.9% | 13 s |
| 6 | *Beast Mastery 35/16/0* | community simulator | - | 474 | -6.1% | 845 | -6.4% | 14 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-04, 12 changes to the base rotation; third-seed check: deep: Beast Mastery (dummy) 466 -> 498 DPS (+6.9%), deep: Beast Mastery (raid) 453 -> 488 DPS (+7.8%), deep: Hybrid Beast Mastery/Marksmanship (dummy) 471 -> 494 DPS (+5.0%), deep: Hybrid Beast Mastery/Marksmanship (raid) 444 -> 479 DPS (+7.9%), beast-mastery-raid 467 -> 490 DPS (+4.9%), sim preset: Beast Mastery 35/16/0 439 -> 463 DPS (+5.5%), mm-hawk-raid 459 -> 478 DPS (+4.0%), beast-marks-ml-raid 447 -> 468 DPS (+4.6%)):
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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-07, 10 changes to the base rotation; third-seed check: open winner 871 -> 904 DPS (+3.8%), beast-mastery-raid 839 -> 867 DPS (+3.3%), sim preset: Beast Mastery 35/16/0 816 -> 844 DPS (+3.4%), mm-hawk-raid 838 -> 868 DPS (+3.5%), beast-mastery-ml-parse 863 -> 895 DPS (+3.6%), beast-marks-ml-raid 858 -> 890 DPS (+3.7%)):
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

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`beast-marks-open-raid`](beast-marks-open-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 2 | cast Summon Hawk | 9.7 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s: cast Serpent Sting | 4.7 |

Lines of the simulator's rotation these builds never cast: cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`beast-marks-open-raid`](beast-marks-open-raid.md) |
|---|---|
| Auto Shot | 37% |
| Summon Hawk | 28% |
| Serpent Sting | 19% |
| Pet: Auto Attack | 13% |
| Pet: Claw | 2% |
| Pet: Bite | 2% |

## Notes

- +4.1% over the best hand draft of the spec, mm-hawk-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (bm-raid, full raid): 27/19/5 (Beast-Marks (a Beast Mastery/Marksmanship hybrid)) at 903.1 DPS; beast-mastery-ml-parse 895.2, beast-marks-ml-raid 889.7, mm-hawk-raid 867.7, beast-mastery-raid 866.9 in the same fights; 4,434 builds simulated, 2 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): bm-mm-raid 851.8, opt-mm-raid-raid-dps 851.8.
- The bm-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): mm-raid -1.1%, mm-lonewolf-raid -1.7%, melee-dps -31.9%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Endurance Training, Improved Aspect of the Monkey, Pathfinding, Lone Wolf.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.
- 2026-10-07 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Lone Wolf -> Efficiency (mana); Pathfinding -> Endurance Training (survival). Net +0.02% on a third seed.

## Open questions (verify in the live game)

- An open-search Beast-Marks build: check it against the community's Beast-Marks builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/hunter/60/532110050510022-00531500104-5-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
