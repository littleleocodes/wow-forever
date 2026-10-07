# Beast-Marks — Raid (machine-learning search) — 28/23/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/23/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Marks build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-04 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry bm-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 3/5 | unchanged | Gives your pet a 60% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Marksmanship (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 2/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 6%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 5** for `bm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`beast-mastery-raid`](beast-mastery-raid.md) | ours: hand draft | 30/21/0 | 499 | +0.0% | 867 | -3.1% | 6 s |
| 2 | [`beast-mastery-ml-parse`](beast-mastery-ml-parse.md) | ours: parse build | 31/20/0 | 498 | -0.2% | 895 | +0.0% | 25 s |
| 3 | **[`beast-marks-ml-raid`](beast-marks-ml-raid.md)** | ours: hand draft | 28/23/0 | 493 | -1.3% | 890 | -0.6% | 18 s |
| 4 | [`mm-hawk-raid`](mm-hawk-raid.md) | ours: hand draft | 22/29/0 | 490 | -1.8% | 868 | -3.1% | 13 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 474 | -5.0% | 845 | -5.6% | 14 s |

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

| # | Priority (the first line whose condition holds is cast) | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire | 0.3 |
| 2 | cast Summon Hawk | 9.7 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left on Serpent Sting < 4s: cast Serpent Sting | 5.0 |
| 5 | if auraIsInactive and mana % ≥ 70%: cast Intimidation | 0.3 |

Damage by ability:

| Ability | [`beast-marks-ml-raid`](beast-marks-ml-raid.md) |
|---|---|
| Auto Shot | 37% |
| Summon Hawk | 27% |
| Serpent Sting | 19% |
| Pet: Auto Attack | 14% |
| Pet: Claw | 2% |
| Pet: Bite | 2% |

## Notes

- Against the best hand draft mm-hawk-raid in a full raid, same gear and fights (100,000, one seed): +1.4% (under the 2% bar: the hand draft stays the pick).
- Search result (full raid): 28/23/0 at 876.2 ± 0.06 DPS over 200,000 fights; runner-up 28/23/0 (+0.00%; the winner takes Endurance Training 2, Pathfinding 1; the runner-up Endurance Training 1, Pathfinding 2); 7,254 builds simulated; certificate: none of its 188 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 28/23/0 at 844.7 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 27/24/0 at 494.2 DPS.
- 2026-10-04 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Pathfinding -> Endurance Training (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- A machine-searched Beast-Marks build: check it against the community's Beast-Marks builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
