# Combat Swords (simulator winner adopted 2026-09-28) — 19/32/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `combat-swords-raid` |

## Summary

Allocation adopted on 2026-09-28 from the community simulator's own preset 'Improved Expose Armor (SS)', the best build in the community simulator (+4.6% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Sword Specialization is gone but Hack and Slash gives swords the same 5% extra-attack proc, Precision is now 3 points for 3% hit, and Restless Blades (the new 16-point talent) shortens Adrenaline Rush/Blade Flurry with every finisher. Improved Eviscerate moved into Combat tier 1, so the Assassination dip shrinks to 18 while keeping Malice, Ruthlessness, Improved Slice and Dice, Relentless Strikes and a much stronger Lethality.

## Point allocation

### Assassination (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Lethality** | 5/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |

### Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Weapon Expertise** | 1/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 1%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |
| **Lightning Reflexes** | 4/5 | unchanged | Increases your Dodge chance by 4%. |

### Subtlety (0)

*No points.*

## Core talents (priority order)

1. **Relentless Strikes** — Energy on finishers. Raid sim (2026-09-28): removing it costs +10% DPS.
2. **Adrenaline Rush** — Reworked: 100% energy regeneration for 15s on a 5-minute cooldown — Restless Blades brings it back faster. Raid sim (2026-09-28): removing it costs +8% DPS.
3. **Improved Sinister Strike** — Raid sim (2026-09-28): removing it costs +8% DPS.
4. **Improved Slice and Dice** — Longer Slice and Dice. Raid sim (2026-09-28): removing it costs +6% DPS.
5. **Improved Expose Armor** — Raid sim (2026-09-28): removing it costs +6% DPS.
6. **Ruthlessness** — Raid sim (2026-09-28): removing it costs +6% DPS.
7. **Malice** — +5% crit, now including poisons. Raid sim (2026-09-28): removing it costs +5% DPS.
8. **Dual Wield Specialization** — +5% off-hand damage per rank (est. 25%); requires Precision 3/3. Raid sim (2026-09-28): removing it costs +4% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Blade Flurry | any utility talent legal at that tier | Measures +0.6% DPS in the community simulator (noise): these points are free to move. |
| 3 | Deflection | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Lightning Reflexes | Endurance, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Lightning Reflexes | Riposte, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Lightning Reflexes | Improved Sprint, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 9** for `combat-swords-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`combat-swords-raid`](combat-swords-raid.md)** | ours: hand draft | 19/32/0 | 394 | +0.0% | 687 | -1.3% | 0 s |
| 2 | *Improved Expose Armor (SS)* | community simulator | - | 394 | +0.0% | 687 | -1.3% | 0 s |
| 3 | [`opt-combat-swords-raid-raid-dps`](opt-combat-swords-raid-raid-dps.md) | ours: optimizer | 20/31/0 | 376 | -4.5% | 682 | -2.1% | 0 s |
| 4 | *Sinister Strike* | community simulator | - | 371 | -5.7% | 696 | +0.0% | 0 s |
| 5 | *Combat Dual-Wield 15/33/3* | community simulator | - | 365 | -7.4% | 682 | -2.0% | 0 s |
| 6 | *Assassination Mutilate 31/20/0* | community simulator | - | 340 | -13.6% | 618 | -11.2% | 0 s |
| 7 | *Mutilate* | community simulator | - | 330 | -16.3% | 608 | -12.6% | 0 s |
| 8 | *Backstab* | community simulator | - | 319 | -19.0% | 621 | -10.7% | 0 s |
| 9 | *Subtlety Hemo 15/0/36* | community simulator | - | 302 | -23.4% | 536 | -23.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-01, 8 changes to the base rotation; third-seed check: ):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.4%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.8%, pass 2)
  5. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.9%, pass 2)
  6. spell probe: insert before the filler: cast Hemorrhage (+13.1%, pass 4)
  7. spell probe: insert in the middle: cast Mutilate (+1.2%, pass 4)
  8. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+2.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-01, 4 changes to the base rotation; third-seed check: ):
  1. threshold 5 -> 2.5: if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.5%, pass 1)
  2. spell probe: insert before the filler: cast Mutilate (+0.6%, pass 4)
  3. spell probe: insert at the top: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 4)
  4. spell probe: insert at the top: cast Hemorrhage (+8.6%, pass 4)

| # | Priority (the first line whose condition holds is cast) | [`combat-swords-raid`](combat-swords-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 2.2 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.4 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 1.0 |
| 6 | cast Sinister Strike | 17.9 |

Lines of the simulator's rotation these builds never cast: cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (needs the Mutilate talent); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`combat-swords-raid`](combat-swords-raid.md) |
|---|---|
| Auto Attack | 53% |
| Sinister Strike | 30% |
| Eviscerate | 6% |
| Deadly Poison | 5% |
| Dense Sharpening Stone | 3% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- Adopted from the community simulator on 2026-09-28: the community simulator's own preset 'Improved Expose Armor (SS)' beat the previous draft by +4.6% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Weapon skill mattered in Classic because of glancing blows; whether glancing blows exist in Forever decides how valuable Weapon Expertise's new dodge/parry reduction is.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Endurance -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival). Net +0.00% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Riposte was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Riposte -> Lightning Reflexes (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Does Forever keep Classic glancing-blow penalties? (Weapon Expertise no longer gives weapon skill.)
- Restless Blades value: with 5-point finishers every ~10s, Adrenaline Rush could be up every ~2 minutes.
- Whether the Assassination Mutilate build (below) overtakes Combat swords with daggers.

## Sources

- <https://warcraftforever.games/talents/rogue>
- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/rogue/dps/presets.ts>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
