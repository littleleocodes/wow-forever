# Optimizer — Raid Combat swords: white ~43% (MH 30 / OH 13), Sinister Strike ~30%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (raid-dps) — 20/31/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/31/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-swords-raid` and profile `raid-dps`: score +66.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 1/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |

### Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Deflection** | 2/3 | changed | Increases your Parry chance by 4%. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Hack and Slash** | 4/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 4% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 4%.   Mace: Your attacks ignore 12% of  your target's armor. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Relentless Strikes** — Removing it costs 12.4 points of score in this model.
2. **Improved Sinister Strike** — Removing it costs 9.5 points of score in this model.
3. **Improved Slice and Dice** — Removing it costs 9.2 points of score in this model.
4. **Malice** — Removing it costs 7.9 points of score in this model.
5. **Ruthlessness** — Removing it costs 7.8 points of score in this model.
6. **Dual Wield Specialization** — Removing it costs 7.8 points of score in this model.
7. **Adrenaline Rush** — Removing it costs 7.3 points of score in this model.
8. **Precision** — Removing it costs 5.8 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 8** for `combat-swords-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`combat-swords-raid`](combat-swords-raid.md) | ours: hand draft | 19/32/0 | 336 | +0.0% | 625 | -1.6% | 0 s |
| 2 | **[`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md)** | ours: optimizer | 20/31/0 | 327 | -2.7% | 629 | -0.9% | 0 s |
| 3 | *Combat SS* | community simulator | - | 321 | -4.5% | 635 | +0.0% | 0 s |
| 4 | *Combat BS* | community simulator | - | 315 | -6.4% | 626 | -1.3% | 0 s |
| 5 | *Asn Muti* | community simulator | - | 292 | -13.3% | 575 | -9.4% | 0 s |
| 6 | *Combat Muti* | community simulator | - | 287 | -14.8% | 585 | -7.9% | 0 s |
| 7 | *Subtlety Hemo* | community simulator | - | 286 | -14.9% | 494 | -22.2% | 0 s |
| 8 | *Subtlety BS* | community simulator | - | 270 | -19.7% | 473 | -25.5% | 0 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-24, 6 changes to the base rotation; third-seed check: combat-swords-open-raid 626 -> 641 DPS (+2.4%), sim preset: Sinister Strike 618 -> 633 DPS (+2.4%), combat-swords-raid 611 -> 625 DPS (+2.4%), opt-combat-swords-raid-raid-dps 619 -> 630 DPS (+1.8%)):
  1. threshold 5 -> 2.5: if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.5%, pass 1)
  2. spell probe: insert before the filler: cast Mutilate (+0.6%, pass 4)
  3. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 4)
  4. spell probe: insert at the top: cast Hemorrhage (+8.6%, pass 4)
  5. threshold 2.5 -> 3.75: if combo points ≥ 2.5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.2%, pass 5)
  6. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.1%, pass 9)

| # | Priority (the first line whose condition holds is cast) | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 2 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.9 |
| 3 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.8 |
| 4 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (rank 8) | 0.3 |
| 6 | cast Sinister Strike | 15.8 |

Lines of the simulator's rotation these builds never cast: cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (needs the Mutilate talent); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) |
|---|---|
| Auto Attack | 55% |
| Sinister Strike | 25% |
| spell 11337 | 8% |
| spell 25349 | 8% |
| Goblin Sapper Charge | 2% |
| Eviscerate | 2% |

## Notes

- Allocation taken from cand-combat-swords-raid-r7 on 2026-10-24: the optimizer's earlier round beat its last export in the community simulator (327 vs 316 DPS; the calibration moved the model past the better build).
- Report: rogue/research/talents/forever/optimizer/combat-swords-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
