# Daggers (split) — Raid (open talent search) — 29/22/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/22/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) raid build the open talent search found on 2026-11-10: every legal 51-point build with no tree rule, searched in the community simulator's combat-daggers-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +16.8% over combat-daggers-raid, the best of our builds in that rotation.

## Point allocation

### Assassination (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Vigor** | 1/2 | changed | Increases your maximum Energy by 5. |
| **Blood Splatter** | 1/1 | **NEW** | Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 2/5 | changed | Increases the chance to apply Poisons to your target by 4%, and gives Poison applications a 20% chance to not consume a charge. |
| **Relentless Strikes** | 5/5 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Venom** | 1/1 | **NEW** | Causes your Shank ability to increase your Poison damage by 30% and your chance to apply Poisons by 20% for 6 seconds. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 4/5 | unchanged | Increases your Dodge chance by 4%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 2/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 10. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 1/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 1%. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Puncturing Wounds** — 98 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
2. **Relentless Strikes** — 67 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
3. **Seal Fate** — 54 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
4. **Venom** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Flawless Execution** — 39 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Dual Wield Specialization** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Ruthlessness** — 36 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Malice** — 35 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 9** for `combat-daggers-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Subtlety Hemo* | community simulator | - | 483 | +0.0% | 794 | -4.3% | 0 s |
| 2 | *Asn Muti* | community simulator | - | 448 | -7.4% | 829 | +0.0% | 0 s |
| 3 | *Combat Venom* | community simulator | - | 399 | -17.5% | 714 | -13.9% | 0 s |
| 4 | **[`daggers-split-open-raid`](daggers-split-open-raid.md)** | ours: derived (open search) | 29/22/0 | 375 | -22.4% | 797 | -3.9% | 0 s |
| 5 | *Combat SS* | community simulator | - | 360 | -25.4% | 682 | -17.8% | 0 s |
| 6 | *Combat BS* | community simulator | - | 347 | -28.2% | 764 | -7.9% | 0 s |
| 7 | [`combat-ml-raid`](combat-ml-raid.md) | ours: derived (ML search) | 13/33/5 | 334 | -30.8% | 773 | -6.8% | 0 s |
| 8 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 21/30/0 | 312 | -35.5% | 681 | -17.9% | 0 s |
| 9 | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) | ours: optimizer | 21/30/0 | 312 | -35.5% | 681 | -17.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Combat 361 -> 425 DPS (+17.7%), sim preset: Combat Dual-Wield 15/33/3 355 -> 394 DPS (+11.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
  5. spell probe: insert in the middle: cast Mutilate (+15.6%, pass 4)
  6. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-11-09, 14 changes to the base rotation; third-seed check: open winner 727 -> 787 DPS (+8.3%), combat-daggers-raid 615 -> 674 DPS (+9.6%), sim preset: Asn Muti 804 -> 809 DPS (+0.6%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Mutilate (+9.9%, pass 4)
  4. drop the condition: if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush (+1.5%, pass 6)
  5. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.2%, pass 8)
  6. insert in the middle: if not Cutthroat is up and variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Backstab (rank 8) (+0.6%, pass 8)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.3%, pass 8)
  8. rotation replaced by the official simulator's default.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+0.7%, pass 9)
  9. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and (not talentIsKnown or time left on Rupture ≥ 4 or variableRef or variableRef) and not variableRef: cast Eviscerate (rank 8) (+0.3%, pass 10)
  10. insert before the filler: cast Backstab (+1.5%, pass 11)
  11. drop: if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike (+3.1%, pass 11)
  12. threshold 4 -> 3: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.3%, pass 11)
  13. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 3 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.2%, pass 11)
  14. threshold 5 -> 3.75: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 3 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 1 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.6%, pass 12)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if “Start In Stealth”: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`daggers-split-open-raid`](daggers-split-open-raid.md) casts/min |
|---|---|---|
| 1 | if “Use Expose Armor”: groupReference | as ready |
| 2 | if not “Use Ambush Opener” and “Use Vanish for Damage” and “Current Points less than 5” and not Garrote is on the target: cast Garrote | 0.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not “Use Ambush Opener” and “Use Vanish for Damage” and “Current Points less than 5” and not “SnD Fall Imminent” and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 4 | if energy ≥ current cost and “Use Ambush Opener” and “Use Vanish for Damage” and “Current Points less than 5” and not “SnD Fall Imminent” and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 5 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 6 | groupReference | as ready |
| 7 | if (“Boot Knife Known” and combo points ≤ 3 and energy ≤ 80 or not “Boot Knife Known” and energy ≤ 80): cast Shank | 6.0 |
| 8 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 9 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or “Expose - Low Duration” or Eureka! is up): cast Thistle Tea | as ready |
| 10 | if “At or Below SnD Clipping Threshold” and “Above SnD Point Threshold” and not “Fight About to End” and not “Expose - Prevent Other Finishers”: cast Slice and Dice | 3.2 |
| 11 | if combo points = 5 and not “SnD Fall Imminent” and energy ≥ current cost and not “Expose - Prevent Other Finishers” and not Elune's Light is up: cast Cold Blood | 0.3 |
| 12 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not “SnD Fall Imminent” or combo points ≥ 3 and “Fight About to End”) and not “Expose - Prevent Other Finishers” and not talentIsKnown: cast Eviscerate (rank 8) | 4.1 |
| 13 | if not Mutilate is known and not Hemorrhage is known and not “Use Backstab” and “Current Points less than 5” and (not “SnD Fall Imminent” or energy > (current cost + current cost) and not “SnD Fall Imminent” or not “Above SnD Point Threshold” or “In Danger of Energy Capping” or “Expose - Low Duration”) and “Gnome Eureka - Active or Not Ready”: cast Sinister Strike | 17.0 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); strict sequence: cast Blood Fury; cast Blade Flurry (needs the Blade Flurry talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Death Mark (needs the Death Mark talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`daggers-split-open-raid`](daggers-split-open-raid.md) |
|---|---|
| Auto Attack | 37% |
| Eviscerate | 17% |
| Sinister Strike | 16% |
| spell 25349 | 13% |
| spell 11337 | 13% |
| Garrote | 2% |
| Goblin Sapper Charge | 2% |
| Shank | 1% |

## Notes

- +14.6% over the best hand draft of the spec, assassination-seal-fate-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (combat-daggers-raid, full raid): 29/22/0 (Daggers (split) (an Assassination/Combat hybrid)) at 787.5 DPS; combat-daggers-raid 674.0, opt-combat-daggers-raid-raid-dps 674.0, combat-ml-raid 674.0 in the same fights; 2,397 builds simulated, 1 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): assassination-seal-fate-raid 687.1, assassination-mutilate-raid 678.4.
- The combat-daggers-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): combat-swords-raid -7.4%, assassination-raid -0.1%, subtlety-raid -8.3%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Efficient Strikes, Lightning Reflexes, Endurance.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.
- 2026-11-10 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Efficient Strikes -> Lightning Reflexes (survival); Endurance -> Lightning Reflexes (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Daggers (split) build: check it against the community's Daggers (split) builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/rogue/60/0053031122125103-312303010201132--12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
