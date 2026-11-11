# Assassination/Subtlety hybrid — Raid (open talent search) — 27/2/22

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/2/22 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination/Subtlety hybrid (an Assassination/Subtlety hybrid) raid build the open talent search found on 2026-11-10: every legal 51-point build with no tree rule, searched in the community simulator's subtlety-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +24.4% over subtlety-hemo-raid, the best of our builds in that rotation.

## Point allocation

### Assassination (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Vigor** | 1/2 | changed | Increases your maximum Energy by 5. |
| **Blood Splatter** | 1/1 | **NEW** | Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vile Poisons** | 1/5 | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Venom** | 1/1 | **NEW** | Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 seconds. |
| **Seal Fate** | 1/3 | moved | Your critical strikes from abilities that add Combo Points have a 33% chance to add an additional Combo Point. |

### Combat (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |

### Subtlety (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 2/3 | changed | Gives you a 30% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Opportunity** | 5/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 20%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Camouflage** | 2/3 | changed | Grants 10% increased movement speed in stealth and reduces stealth's cooldown by 4 seconds. |
| **Improved Ambush** | 1/3 | moved | Increases the critical strike chance of your Ambush ability by 15%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |

## Core talents (priority order)

1. **Dirty Deeds** — 273 DPS lost without it (34% of the build in a full raid; removal, 12,000 fights).
2. **Hemorrhage** — 69 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
3. **Relentless Strikes** — 64 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Blood Splatter** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Venom** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Ghostly Strike** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
7. **Efficient Strikes** — 35 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Malice** — 35 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 4** for `subtlety-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`subtlety-ml-raid`](subtlety-ml-raid.md) | ours: derived (ML search) | 12/8/31 | 480 | +0.0% | 803 | -0.9% | 0 s |
| 2 | *Subtlety Hemo* | community simulator | - | 480 | +0.0% | 803 | -0.9% | 0 s |
| 3 | **[`hybrid-assassination-subtlety-open-raid`](hybrid-assassination-subtlety-open-raid.md)** | ours: derived (open search) | 27/2/22 | 462 | -3.9% | 811 | +0.0% | 0 s |
| 4 | [`subtlety-hemo-raid`](subtlety-hemo-raid.md) | ours: hand draft | 21/0/30 | 359 | -25.2% | 651 | -19.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-10, 17 changes to the base rotation; third-seed check: open winner 349 -> 374 DPS (+7.2%), subtlety-hemo-raid 347 -> 399 DPS (+14.9%), sim preset: Subtlety Hemo 15/0/36 319 -> 356 DPS (+11.5%)):
  1. drop 'combo points ≥ 4' from the condition: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+1.8%, pass 1)
  2. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.6%, pass 1)
  3. threshold 20s -> 40s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice (+0.6%, pass 1)
  4. threshold 40s -> 80s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 40s: cast Slice and Dice (+0.5%, pass 1)
  5. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+2.5%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+2.2%, pass 1)
  7. only with 20s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  8. insert at the top: if energy ≤ 29 and combo points < 5 and time left on Expose Armor ≤ 6 and timeToNextEnergyTick > 1 and not Adrenaline Rush is up: cast Thistle Tea (+0.4%, pass 3)
  9. threshold 20s -> 10s: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 20s: cast Expose Armor (+0.3%, pass 3)
  10. threshold 8 -> 12: if not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 3)
  11. threshold 3 -> 5: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 3)
  12. insert in the middle: cast Garrote (+3.0%, pass 4)
  13. spell probe: insert before the filler: cast Blade Flurry (+0.5%, pass 5)
  14. threshold 80s -> 160s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 80s: cast Slice and Dice (+1.8%, pass 6)
  15. threshold 60 -> 30: if energy ≥ 60 and combo points ≤ 1 and Slice and Dice is up and time left in the fight > 10: cast Vanish (+0.5%, pass 6)
  16. drop: if energy ≤ 29 and combo points < 5 and time left on Expose Armor ≤ 6 and timeToNextEnergyTick > 1 and not Adrenaline Rush is up: cast Thistle Tea (+3.0%, pass 7)
  17. insert at the end: cast Preparation (+0.3%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 13 passes, the last 2026-11-10, 24 changes to the base rotation; third-seed check: open winner 789 -> 796 DPS (+0.9%), subtlety-hemo-raid 626 -> 639 DPS (+2.0%), sim preset: Subtlety Hemo 788 -> 788 DPS (+0.0%)):
  1. drop 'combo points ≥ 4' from the condition: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+1.1%, pass 1)
  2. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  3. insert at the top: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 2)
  4. threshold 5 -> 3.75: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice (+0.3%, pass 2)
  5. threshold 4 -> 2: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 2)
  6. insert in the middle: if not Garrote is on the target: cast Garrote (+1.7%, pass 4)
  7. spell probe: insert before the filler: cast Cold Blood (+0.4%, pass 5)
  8. spell probe: insert before the filler: if auraIsInactive: cast Ghostly Strike (+0.4%, pass 5)
  9. threshold 1 -> 3: if energy ≥ 60 and combo points ≤ 1 and Slice and Dice is up and time left in the fight > 10: cast Vanish (+0.2%, pass 6)
  10. move down below 'cast Cold Blood': if auraIsInactive: cast Ghostly Strike (+0.2%, pass 6)
  11. insert before the filler: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 2 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 7)
  12. spell probe: insert before the filler: cast Blade Flurry (+0.3%, pass 9)
  13. insert in the middle: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.7%, pass 10)
  14. drop: if auraIsInactive: cast Ghostly Strike (+0.3%, pass 10)
  15. threshold 3 -> 1: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+0.3%, pass 10)
  16. drop: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 3.75 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice (+0.3%, pass 10)
  17. threshold 60 -> 45: if energy ≥ 60 and combo points ≤ 3 and Slice and Dice is up and time left in the fight > 10: cast Vanish (+0.2%, pass 10)
  18. insert at the end: if not Vanish is ready: cast Preparation (+0.2%, pass 11)
  19. insert at the top: if true and not Hemorrhage is up and combo points < 5: cast Hemorrhage (+0.2%, pass 11)
  20. drop the condition: if not Garrote is on the target: cast Garrote (+0.2%, pass 11)
  21. threshold 8s -> 6s: if not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef and (time left on Garrote ≥ 8s or not talentIsKnown): cast Hemorrhage (+0.5%, pass 12)
  22. threshold 4 -> 5: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.2%, pass 12)
  23. drop '(combo points < 3 or variableRef or Eureka! is up)' from the condition: if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+0.2%, pass 12)
  24. drop 'variableRef' from the condition: if variableRef and not Hemorrhage is up and variableRef: cast Hemorrhage (+0.2%, pass 12)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if variableRef: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`hybrid-assassination-subtlety-open-raid`](hybrid-assassination-subtlety-open-raid.md) casts/min |
|---|---|---|
| 1 | if variableRef: groupReference | as ready |
| 2 | if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote | 2.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.4 |
| 4 | if energy ≥ current cost and variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.4 |
| 5 | if not Vanish is ready: cast Preparation | 0.3 |
| 6 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 7 | groupReference | as ready |
| 8 | if (variableRef and combo points ≤ 3 and energy ≤ 80 or not variableRef and energy ≤ 80): cast Shank | 5.9 |
| 9 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 10 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea | as ready |
| 11 | if combo points ≤ 3: cast Premeditation | 1.0 |
| 12 | if (talentIsKnown or talentIsKnown) and (combo points ≥ 3) and not Rupture is on the target and not variableRef and not variableRef and not talentIsKnown: cast Rupture | 2.9 |
| 13 | if variableRef and variableRef and not variableRef and not variableRef: cast Slice and Dice | 3.1 |
| 14 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 3.3 |
| 15 | if variableRef and (not in front of the target or variableRef) and time left on Garrote ≤ 4s: cast Ghostly Strike | 2.0 |
| 16 | if variableRef and not Hemorrhage is up and variableRef: cast Hemorrhage | 18.3 |
| 17 | if not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef and (time left on Garrote ≥ 8s or not talentIsKnown): cast Hemorrhage | 18.3 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Backstab (rank 8), cast Sinister Strike (its condition never held in these fights); strict sequence: cast Blood Fury; cast Blade Flurry (needs the Blade Flurry talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Death Mark (needs the Death Mark talent); cast Cold Blood (needs the Cold Blood talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`hybrid-assassination-subtlety-open-raid`](hybrid-assassination-subtlety-open-raid.md) |
|---|---|
| Auto Attack | 27% |
| Garrote | 15% |
| Rupture | 14% |
| Hemorrhage | 13% |
| spell 11337 | 11% |
| spell 25349 | 9% |
| Eviscerate | 8% |
| Ghostly Strike | 2% |
| Goblin Sapper Charge | 1% |
| Shank | 1% |

## Notes

- Open search result (subtlety-raid, full raid): 27/2/22 (Assassination/Subtlety hybrid (an Assassination/Subtlety hybrid)) at 795.2 DPS; subtlety-hemo-raid 639.1 in the same fights; 2,316 builds simulated, 1 independent runs reached the top.
- The subtlety-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): combat-swords-raid -0.8%, combat-daggers-raid -1.5%, assassination-raid -2.2%; none adopted.
- A phase-1 BiS set picked for this family (_reference/data/raidsim/gear_sets/forever/tiers/rogue-hybrid-assassination-subtlety-bis.gear.json, item level 62.4): 795.9 DPS against 795.2 in the rotation's standard set: a lead for the gear sets (not applied).
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Setup, Camouflage, Improved Ambush.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Assassination/Subtlety hybrid build: check it against the community's Assassination/Subtlety hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/rogue/60/0053031121045101-02-2052210313010011-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
