# Combat — Raid (derived) — 16/33/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/33/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat raid damage build derived on 2026-09-30 (derive_raid.py): the community simulator's talent search (raidsim/talent_opt.py, entry combat-daggers-raid, training dummy) from the spec's best build opt-combat-daggers-raid-raid-dps, 30+ points kept in Combat.

## Point allocation

### Assassination (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 1/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Poisons** | 1/5 | changed | Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge. |

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

## Rank among our builds and the community simulator's

**1 of 10** for `combat-daggers-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`combat-raid`](combat-raid.md)** | ours: hand draft | 16/33/2 | 422 | +0.0% | 712 | -0.0% | 0 s |
| 2 | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) | ours: optimizer | 17/32/2 | 416 | -1.4% | 696 | -2.3% | 0 s |
| 3 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 16/33/2 | 399 | -5.4% | 712 | +0.0% | 0 s |
| 4 | *Combat Dual-Wield 15/33/3* | community simulator | - | 394 | -6.5% | 702 | -1.5% | 0 s |
| 5 | *Backstab* | community simulator | - | 371 | -12.0% | 672 | -5.6% | 0 s |
| 6 | *Mutilate* | community simulator | - | 371 | -12.1% | 648 | -9.0% | 0 s |
| 7 | *Assassination Mutilate 31/20/0* | community simulator | - | 359 | -14.8% | 630 | -11.6% | 0 s |
| 8 | *Improved Expose Armor (SS)* | community simulator | - | 347 | -17.7% | 620 | -12.9% | 0 s |
| 9 | *Sinister Strike* | community simulator | - | 334 | -20.7% | 629 | -11.6% | 0 s |
| 10 | *Subtlety Hemo 15/0/36* | community simulator | - | 258 | -38.8% | 500 | -29.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-combat-daggers-raid-raid-dps 374 -> 413 DPS (+10.6%), sim preset: Combat Dual-Wield 15/33/3 365 -> 405 DPS (+10.9%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 2 changes to the base rotation; third-seed check: opt-combat-daggers-raid-raid-dps 731 -> 742 DPS (+1.5%), sim preset: Combat Dual-Wield 15/33/3 714 -> 721 DPS (+0.9%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`combat-raid`](combat-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.7 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.5 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 1.2 |
| 6 | cast Backstab | 12.3 |

Damage by ability:

| Ability | [`combat-raid`](combat-raid.md) |
|---|---|
| Auto Attack | 45% |
| Backstab | 35% |
| Deadly Poison | 6% |
| Eviscerate | 6% |
| Dense Sharpening Stone | 3% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- About +5.7% over the hand draft combat-daggers-raid (over the 2% replacement bar): this build is the spec's raid pick, the hand draft stays as the alternative.
- Simulator talent search from opt-combat-daggers-raid-raid-dps: 2 points Lethality -> Improved Expose Armor; 1 point Cold Blood -> Improved Poisons (+4.7% DPS on the search's third seed).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements.

## Open questions (verify in the live game)

- A derived Combat raid build: check it against the community's Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
