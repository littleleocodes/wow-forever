# Optimizer — Raid daggers: white ~40%, Backstab (or Mutilate via talent) ~33%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (raid-dps) — 16/33/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/33/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-daggers-raid` and profile `raid-dps`: score +78.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |

### Combat (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Endurance** | 1/2 | changed | Reduces the cooldown of your Sprint and Evasion abilities by 30%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Core talents (priority order)

1. **Puncturing Wounds** — Removing it costs 23.5 points of score in this model.
2. **Relentless Strikes** — Removing it costs 12.1 points of score in this model.
3. **Improved Slice and Dice** — Removing it costs 8.5 points of score in this model.
4. **Adrenaline Rush** — Removing it costs 7.9 points of score in this model.
5. **Malice** — Removing it costs 7.6 points of score in this model.
6. **Hack and Slash** — Removing it costs 7.2 points of score in this model.
7. **Ruthlessness** — Removing it costs 6.6 points of score in this model.
8. **Precision** — Removing it costs 6.1 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 9** for `combat-daggers-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md)** | ours: optimizer | 16/33/2 | 403 | +0.0% | 720 | +0.0% | 0 s |
| 2 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 16/33/2 | 399 | -0.9% | 712 | -1.1% | 0 s |
| 3 | *Combat Dual-Wield 15/33/3* | community simulator | - | 394 | -2.1% | 702 | -2.5% | 0 s |
| 4 | *Backstab* | community simulator | - | 371 | -7.8% | 672 | -6.6% | 0 s |
| 5 | *Mutilate* | community simulator | - | 371 | -7.9% | 648 | -10.0% | 0 s |
| 6 | *Assassination Mutilate 31/20/0* | community simulator | - | 359 | -10.8% | 630 | -12.5% | 0 s |
| 7 | *Improved Expose Armor (SS)* | community simulator | - | 347 | -13.8% | 620 | -13.8% | 0 s |
| 8 | *Sinister Strike* | community simulator | - | 334 | -17.0% | 629 | -12.6% | 0 s |
| 9 | *Subtlety Hemo 15/0/36* | community simulator | - | 258 | -35.9% | 500 | -30.5% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-combat-daggers-raid-raid-dps 374 -> 413 DPS (+10.6%), sim preset: Combat Dual-Wield 15/33/3 365 -> 405 DPS (+10.9%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 2 changes to the base rotation; third-seed check: opt-combat-daggers-raid-raid-dps 731 -> 742 DPS (+1.5%), sim preset: Combat Dual-Wield 15/33/3 714 -> 721 DPS (+0.9%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.7 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.7 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 0.5 |
| 6 | cast Backstab | 11.8 |

Damage by ability:

| Ability | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) |
|---|---|
| Auto Attack | 47% |
| Backstab | 37% |
| Deadly Poison | 6% |
| Dense Sharpening Stone | 3% |
| Eviscerate | 3% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- Allocation taken from cand-combat-daggers-raid-r1 on 2026-09-29: the optimizer's earlier round beat its last export in the community simulator (403 vs 400 DPS; the calibration moved the model past the better build).
- Report: rogue/research/talents/forever/optimizer/combat-daggers-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
