# Optimizer — Raid daggers: white ~40%, Backstab (or Mutilate via talent) ~33%, Eviscerate ~12%, poisons ~10%, Rupture ~5% (raid-dps) — 17/32/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/32/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `combat-daggers-raid` and profile `raid-dps`: score +92.2% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Assassination (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Lethality** | 1/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. |

### Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Core talents (priority order)

1. **Puncturing Wounds** — Removing it costs 26.7 points of score in this model.
2. **Relentless Strikes** — Removing it costs 13.6 points of score in this model.
3. **Improved Slice and Dice** — Removing it costs 12.5 points of score in this model.
4. **Adrenaline Rush** — Removing it costs 12.3 points of score in this model.
5. **Improved Expose Armor** — Removing it costs 10.0 points of score in this model.
6. **Malice** — Removing it costs 8.1 points of score in this model.
7. **Hack and Slash** — Removing it costs 7.9 points of score in this model.
8. **Ruthlessness** — Removing it costs 7.4 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 9** for `combat-daggers-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md)** | ours: optimizer | 17/32/2 | 376 | +0.0% | 663 | -3.0% | 0 s |
| 2 | [`combat-ml-raid`](combat-ml-raid.md) | ours: derived (ML search) | 16/33/2 | 359 | -4.7% | 683 | +0.0% | 0 s |
| 3 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 16/33/2 | 356 | -5.5% | 677 | -1.0% | 0 s |
| 4 | *Combat BS* | community simulator | - | 355 | -5.8% | 677 | -0.9% | 0 s |
| 5 | *Combat SS* | community simulator | - | 349 | -7.2% | 667 | -2.4% | 0 s |
| 6 | *Asn Muti* | community simulator | - | 340 | -9.8% | 647 | -5.3% | 0 s |
| 7 | *Combat Muti* | community simulator | - | 337 | -10.5% | 651 | -4.7% | 0 s |
| 8 | *Subtlety BS* | community simulator | - | 307 | -18.4% | 572 | -16.3% | 0 s |
| 9 | *Subtlety Hemo* | community simulator | - | 279 | -26.0% | 533 | -22.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Combat 361 -> 425 DPS (+17.7%), sim preset: Combat Dual-Wield 15/33/3 355 -> 394 DPS (+11.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
  5. spell probe: insert in the middle: cast Mutilate (+15.6%, pass 4)
  6. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-24, 8 changes to the base rotation; third-seed check: combat-ml-raid 659 -> 683 DPS (+3.6%), sim preset: Combat Dual-Wield 15/33/3 646 -> 667 DPS (+3.2%), combat-daggers-raid 655 -> 677 DPS (+3.3%), opt-combat-daggers-raid-raid-dps 643 -> 662 DPS (+2.9%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Mutilate (+9.9%, pass 4)
  4. drop the condition: if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush (+1.5%, pass 6)
  5. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.2%, pass 8)
  6. insert in the middle: if not Cutthroat is up and variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Backstab (rank 8) (+0.6%, pass 8)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.3%, pass 8)
  8. rotation replaced by the official simulator's default.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+0.7%, pass 9)

| # | Priority (the first line whose condition holds is cast) | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 2.0 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.4 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (rank 8) | 0.6 |
| 6 | cast Backstab (rank 8) | 10.8 |

Lines of the simulator's rotation these builds never cast: cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) |
|---|---|
| Auto Attack | 48% |
| Backstab | 35% |
| spell 25349 | 7% |
| spell 11337 | 4% |
| Eviscerate | 3% |
| Goblin Sapper Charge | 2% |

## Notes

- Report: rogue/research/talents/forever/optimizer/combat-daggers-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
