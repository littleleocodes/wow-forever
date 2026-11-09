# Daggers (split) — Raid (open talent search) — 28/21/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/21/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) raid build the open talent search found on 2026-11-02: every legal 51-point build with no tree rule, searched in the community simulator's assassination-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.2% over assassination-ml-raid, the best of our builds in that rotation.

## Point allocation

### Assassination (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Vile Poisons** | 1/5 | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Dual Wield Specialization** | 1/2 | changed | Increases the damage done by your off-hand weapon by 25%. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 8%. |

## Core talents (priority order)

1. **Relentless Strikes** — 58 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
2. **Dual Wield Specialization** — 32 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
3. **Malice** — 29 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
4. **Seal Fate** — 24 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
5. **Improved Slice and Dice** — 23 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
6. **Ruthlessness** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Improved Poisons** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Flawless Execution** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 5** for `assassination-raid` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Asn Muti* | community simulator | - | 443 | +0.0% | 811 | +0.0% | 0 s |
| 2 | [`assassination-ml-raid`](assassination-ml-raid.md) | ours: derived (ML search) | 29/22/0 | 323 | -27.1% | 695 | -14.3% | 0 s |
| 3 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 28/21/2 | 314 | -29.1% | 687 | -15.3% | 0 s |
| 4 | **[`daggers-split-open-raid`](daggers-split-open-raid.md)** | ours: derived (open search) | 28/21/2 | 311 | -29.7% | 685 | -15.6% | 0 s |
| 5 | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) | ours: hand draft | 29/22/0 | 309 | -30.2% | 678 | -16.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-14, 11 changes to the base rotation; third-seed check: ):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+8.6%, pass 1)
  2. threshold 5 -> 3.75: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.8%, pass 1)
  3. insert at the top: cast Backstab (+1.6%, pass 1)
  4. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  5. threshold 6 -> 12: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood + drop 'combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9' from the condition: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  7. insert at the top: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea + threshold 29 -> 43.5: if energy ≤ 29 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+0.3%, pass 3)
  8. spell probe: insert at the end: cast Hemorrhage (+8.4%, pass 5)
  9. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.0%, pass 5)
  10. drop: if energy ≤ 43.5 and timeToNextEnergyTick > 1 and combo points < 5 and not Adrenaline Rush is up: cast Thistle Tea (+2.8%, pass 8)
  11. spell probe: insert at the top: if auraIsInactive: cast Adrenaline Rush (+1.8%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 14 passes, the last 2026-11-09, 11 changes to the base rotation; third-seed check: assassination-mutilate-raid 610 -> 679 DPS (+11.2%), sim preset: Asn Muti 804 -> 812 DPS (+0.9%), assassination-seal-fate-raid 609 -> 687 DPS (+12.9%), assassination-ml-raid 628 -> 696 DPS (+10.7%), daggers-split-open-raid 606 -> 686 DPS (+13.1%)):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)
  2. spell probe: insert at the end: cast Hemorrhage (+9.9%, pass 5)
  3. spell probe: insert in the middle: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 5)
  4. move down below 'cast Mutilate': cast Backstab (+0.2%, pass 9)
  5. spell probe: insert in the middle: if auraIsInactive: cast Adrenaline Rush (+1.4%, pass 11)
  6. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+1.3%, pass 12)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.2%, pass 12)
  8. insert in the middle: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not time left on Slice and Dice ≤ 2s or combo points ≥ 3 and time left in the fight ≤ 6s) and (not talentIsKnown or time left on Rupture ≥ 4 or energy ≥ 75 or time left in the fight ≤ 6s) and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s): cast Eviscerate (rank 8) (+0.3%, pass 13)
  9. insert before the filler: cast Backstab (+1.6%, pass 14)
  10. drop: if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike (+3.7%, pass 14)
  11. threshold 5 -> 2.5: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.6%, pass 14)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if variableRef: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`daggers-split-open-raid`](daggers-split-open-raid.md) casts/min |
|---|---|---|
| 1 | if variableRef: groupReference | as ready |
| 2 | if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote | 0.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 4 | if energy ≥ current cost and variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 5 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 6 | groupReference | as ready |
| 7 | if (variableRef and combo points ≤ 3 and energy ≤ 80 or not variableRef and energy ≤ 80): cast Shank | 6.0 |
| 8 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 9 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea | as ready |
| 10 | if variableRef and variableRef and not variableRef and not variableRef: cast Slice and Dice | 3.2 |
| 11 | if combo points = 5 and not variableRef and energy ≥ current cost and not variableRef and not Elune's Light is up: cast Cold Blood | 0.3 |
| 12 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 3.5 |
| 13 | if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike | 14.6 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); strict sequence: cast Blood Fury; cast Blade Flurry (needs the Blade Flurry talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Death Mark (needs the Death Mark talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`daggers-split-open-raid`](daggers-split-open-raid.md) |
|---|---|
| Auto Attack | 41% |
| Eviscerate | 17% |
| Sinister Strike | 17% |
| spell 25349 | 12% |
| spell 11337 | 9% |
| Goblin Sapper Charge | 2% |
| Garrote | 2% |
| Shank | 1% |

## Notes

- Open search result (assassination-raid, full raid): 28/21/2 (Daggers (split) (an Assassination/Combat hybrid)) at 663.4 DPS; assassination-ml-raid 662.0, assassination-seal-fate-raid 656.9, daggers-split-open-raid 656.5, assassination-mutilate-raid 642.9 in the same fights; 7,678 builds simulated, 3 independent runs reached the top.
- Sibling rotations tried on it (10,000 fights): combat-swords-raid -11.1%, combat-daggers-raid -0.2%, subtlety-raid -55.8%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Sinister Strike, Lightning Reflexes, Deflection, Endurance.
- Simulator numbers are the community's model of the beta (wowsims/forever 54ceac6 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Endurance -> Lightning Reflexes (survival); Improved Sinister Strike -> Lightning Reflexes (survival). Net +0.00% on a third seed.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 28/21/2 -> 28/21/2; Lethality 3 -> 2 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Improved Expose Armor (tier gating for Cold Blood); +1 Improved Expose Armor (tier gating for Cold Blood); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Vigor (tier gating for Mutilate); +1 Vigor (tier gating for Mutilate); -1 Mutilate (over 51); -1 Vile Poisons (over 51); -1 Vile Poisons (over 51); -1 Dual Wield Specialization (over 51) (refill: the combat-daggers-raid model, raid-dps).

## Open questions (verify in the live game)

- An open-search Daggers (split) build: check it against the community's Daggers (split) builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/rogue/60/0053031033150103-311333100015-002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
