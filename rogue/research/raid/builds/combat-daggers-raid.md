# Combat Daggers (raid DPS) — 16/33/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/33/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `combat-daggers-raid` |

## Summary

The conservative dagger adaptation: Puncturing Wounds replaces Improved Backstab (+30% Backstab crit and up to 45% chance for an extra combo point), Hack and Slash replaces Dagger Specialization (crit with daggers), and Opportunity is now only 2 points. Compare with the Assassination Mutilate build.

## Point allocation

### Assassination (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 2/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 8%. |

### Combat (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Core talents (priority order)

1. **Puncturing Wounds** — +30% Backstab crit and a 45% chance for an extra combo point on Backstab — replaces Improved Backstab and then some.
2. **Hack and Slash** — Dagger/fist: crit chance (max rank estimated at 5%, like the old Dagger Specialization).
3. **Dual Wield Specialization** — Off-hand damage.
4. **Flawless Execution** — (renamed from Restless Blades in the beta client) Cooldown reduction from finishers.
5. **Opportunity** — +10% Backstab/Ambush/Mutilate (2 ranks now).
6. **Aggression** — +6% Backstab.
7. **Precision** — Hit.
8. **Blade Flurry** — Haste/cleave.
9. **Adrenaline Rush** — Energy burst.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Lethality | Cold Blood 1 + Lethality 1 | Sixteenth Assassination point; Cold Blood is now a tier-4 (15-point) talent. |
| 2 | Lightning Reflexes | Improved Sinister Strike (useless for daggers), Deflection | Tier-1 Combat filler. |

## Rank among our builds and the community simulator's

**3 of 10** for `combat-daggers-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) | ours: optimizer | 17/32/2 | 419 | +0.0% | 747 | -3.3% | 0 s |
| 2 | [`combat-ml-raid`](combat-ml-raid.md) | ours: hand draft | 16/33/2 | 402 | -4.0% | 772 | +0.0% | 0 s |
| 3 | **[`combat-daggers-raid`](combat-daggers-raid.md)** | ours: hand draft | 16/33/2 | 398 | -4.9% | 765 | -1.0% | 0 s |
| 4 | *Combat Dual-Wield 15/33/3* | community simulator | - | 394 | -6.0% | 754 | -2.3% | 0 s |
| 5 | *Backstab* | community simulator | - | 371 | -11.5% | 721 | -6.6% | 0 s |
| 6 | *Mutilate* | community simulator | - | 363 | -13.3% | 700 | -9.3% | 0 s |
| 7 | *Improved Expose Armor (SS)* | community simulator | - | 350 | -16.4% | 668 | -13.4% | 0 s |
| 8 | *Assassination Mutilate 31/20/0* | community simulator | - | 349 | -16.5% | 681 | -11.8% | 0 s |
| 9 | *Sinister Strike* | community simulator | - | 334 | -20.1% | 680 | -11.9% | 0 s |
| 10 | *Subtlety Hemo 15/0/36* | community simulator | - | 258 | -38.3% | 539 | -30.2% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Combat 361 -> 425 DPS (+17.7%), sim preset: Combat Dual-Wield 15/33/3 355 -> 394 DPS (+11.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
  5. spell probe: insert in the middle: cast Mutilate (+15.6%, pass 4)
  6. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 3 changes to the base rotation; third-seed check: ml: Combat 707 -> 713 DPS (+0.8%), sim preset: Combat Dual-Wield 15/33/3 697 -> 702 DPS (+0.8%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Mutilate (+9.9%, pass 4)

| # | Priority (the first line whose condition holds is cast) | [`combat-daggers-raid`](combat-daggers-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.9 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.7 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 0.3 |
| 6 | cast Backstab | 11.8 |

Lines of the simulator's rotation these builds never cast: cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`combat-daggers-raid`](combat-daggers-raid.md) |
|---|---|
| Auto Attack | 48% |
| Backstab | 37% |
| Deadly Poison | 6% |
| Dense Sharpening Stone | 3% |
| Dragonbreath Chili | 2% |
| Eviscerate | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- Backstab requires being behind the target; Mutilate does not — one reason the Assassination build may win.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Endurance -> Lightning Reflexes (survival); Endurance -> Lightning Reflexes (survival); Improved Sprint -> Lightning Reflexes (survival); Improved Sprint -> Deflection (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Hack and Slash dagger rank scaling (only rank 1 = 1% crit was read; ranks 2-5 are extrapolated).

## Sources

- <https://warcraftforever.games/talents/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
