# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (raid-dps) — 21/30/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `raid-dps`: score +66.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |

### Combat (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Relentless Strikes** — Removing it costs 12.4 points of score in this model.
2. **Improved Slice and Dice** — Removing it costs 9.2 points of score in this model.
3. **Malice** — Removing it costs 7.9 points of score in this model.
4. **Ruthlessness** — Removing it costs 7.8 points of score in this model.
5. **Dual Wield Specialization** — Removing it costs 7.8 points of score in this model.
6. **Precision** — Removing it costs 5.8 points of score in this model.

## Rank among our builds and the community simulator's

**5 of 7** for `combat-swords-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Subtlety Hemo* | community simulator | - | 480 | +0.0% | 803 | +0.0% | 0 s |
| 2 | *Combat Venom* | community simulator | - | 416 | -13.3% | 794 | -1.2% | 0 s |
| 3 | *Combat SS* | community simulator | - | 377 | -21.4% | 761 | -5.3% | 0 s |
| 4 | *Combat BS* | community simulator | - | 366 | -23.9% | 737 | -8.3% | 0 s |
| 5 | **[`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md)** | ours: optimizer | 21/30/0 | 356 | -25.9% | 709 | -11.8% | 0 s |
| 6 | [`combat-swords-raid`](combat-swords-raid.md) | ours: hand draft | 21/30/0 | 341 | -28.9% | 690 | -14.1% | 0 s |
| 7 | *Asn Muti* | community simulator | - | 148 | -69.3% | 292 | -63.6% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-10, 9 changes to the base rotation; third-seed check: open winner 353 -> 392 DPS (+11.1%), combat-swords-raid 343 -> 409 DPS (+19.3%), sim preset: Improved Expose Armor (SS) 343 -> 409 DPS (+19.3%), opt-combat-swords-raid-raid-dps 349 -> 391 DPS (+12.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.4%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.8%, pass 2)
  5. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.9%, pass 2)
  6. spell probe: insert before the filler: cast Hemorrhage (+13.1%, pass 4)
  7. spell probe: insert in the middle: cast Mutilate (+1.2%, pass 4)
  8. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.2%, pass 4)
  9. move to the top: if Slice and Dice is up: use every other cooldown when ready (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 14 passes, the last 2026-11-09, 12 changes to the base rotation; third-seed check: open winner 779 -> 781 DPS (+0.3%), opt-combat-swords-raid-raid-dps 690 -> 693 DPS (+0.3%), sim preset: Subtlety Hemo 788 -> 788 DPS (+0.0%), combat-swords-raid 673 -> 675 DPS (+0.3%), combat-swords-open-raid 691 -> 693 DPS (+0.3%)):
  1. threshold 5 -> 2.5: if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.5%, pass 1)
  2. spell probe: insert before the filler: cast Mutilate (+0.6%, pass 4)
  3. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 4)
  4. spell probe: insert at the top: cast Hemorrhage (+8.6%, pass 4)
  5. threshold 2.5 -> 3.75: if combo points ≥ 2.5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.2%, pass 5)
  6. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.1%, pass 9)
  7. insert at the end: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not time left on Slice and Dice ≤ 2s or combo points ≥ 3 and time left in the fight ≤ 6s) and (not talentIsKnown or time left on Rupture ≥ 4 or energy ≥ 75 or time left in the fight ≤ 6s) and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s): cast Eviscerate (rank 8) (+0.2%, pass 10)
  8. drop: if combo points ≥ 3.75 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (rank 8) (+0.2%, pass 10)
  9. insert at the end: if combo points = 5 and not time left on Slice and Dice ≤ 2s and energy ≥ current cost and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s) and not Elune's Light is up: cast Cold Blood (+0.3%, pass 10)
  10. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not time left on Slice and Dice ≤ 2s or combo points ≥ 3 and time left in the fight ≤ 6s) and (not talentIsKnown or time left on Rupture ≥ 4 or energy ≥ 75 or time left in the fight ≤ 6s) and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s): cast Eviscerate (rank 8) (+0.2%, pass 10)
  11. drop 'energy ≥ current cost' from the condition: if combo points = 5 and not time left on Slice and Dice ≤ 2s and energy ≥ current cost and not false and false and (not Expose Armor is up or time left on Expose Armor ≤ 16s) and not Elune's Light is up: cast Cold Blood (+0.4%, pass 11)
  12. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.2%, pass 12)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if variableRef: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if variableRef: groupReference | as ready |
| 2 | if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote | 0.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 4 | if energy ≥ current cost and variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 5 | if Blade Flurry is ready and Blood Fury is known: strict sequence: cast Blood Fury; cast Blade Flurry | 0.7 |
| 6 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 7 | groupReference | as ready |
| 8 | if (variableRef and combo points ≤ 3 and energy ≤ 80 or not variableRef and energy ≤ 80): cast Shank | 6.0 |
| 9 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 10 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea | as ready |
| 11 | if variableRef and variableRef and not variableRef and not variableRef: cast Slice and Dice | 3.3 |
| 12 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 3.3 |
| 13 | if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike | 16.4 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Death Mark (needs the Death Mark talent); cast Cold Blood (needs the Cold Blood talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) |
|---|---|
| Auto Attack | 44% |
| Sinister Strike | 21% |
| Eviscerate | 13% |
| spell 25349 | 9% |
| spell 11337 | 8% |
| Goblin Sapper Charge | 2% |
| Shank | 1% |
| Garrote | 1% |

## Notes

- Allocation taken from cand-combat-swords-raid-r7 on 2026-10-24: the optimizer's earlier round beat its last export in the community simulator (327 vs 316 DPS; the calibration moved the model past the better build).
- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-raid-dps.md
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 20/31/0 -> 21/30/0; Murder 2 gone; Improved Sinister Strike -> Efficient Strikes (renamed); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Vigor (tier gating for Improved Poisons); +1 Vigor (tier gating for Improved Poisons); +1 Lethality (tier gating for Improved Poisons); +1 Hack and Slash (tier gating for Adrenaline Rush); +1 Flawless Execution (tier gating for Adrenaline Rush); +1 Deflection (tier gating for Adrenaline Rush); -1 Adrenaline Rush (over 51) (refill: the combat-swords-raid model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Improved Sinister Strike, Adrenaline Rush; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
