# Combat — Raid (machine-learning search) — 16/33/2

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/33/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-03 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry combat-daggers-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Assassination (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |

### Combat (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Rank among our builds and the community simulator's

**2 of 10** for `combat-daggers-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) | ours: optimizer | 17/32/2 | 424 | +0.0% | 672 | -3.4% | 0 s |
| 2 | **[`combat-ml-raid`](combat-ml-raid.md)** | ours: derived (ML search) | 16/33/2 | 406 | -4.1% | 695 | +0.0% | 0 s |
| 3 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 16/33/2 | 404 | -4.8% | 688 | -1.0% | 0 s |
| 4 | *Combat Dual-Wield 15/33/3* | community simulator | - | 399 | -5.9% | 678 | -2.4% | 0 s |
| 5 | *Mutilate* | community simulator | - | 383 | -9.6% | 629 | -9.6% | 0 s |
| 6 | *Assassination Mutilate 31/20/0* | community simulator | - | 382 | -9.9% | 611 | -12.1% | 0 s |
| 7 | *Backstab* | community simulator | - | 375 | -11.5% | 652 | -6.3% | 0 s |
| 8 | *Improved Expose Armor (SS)* | community simulator | - | 355 | -16.4% | 603 | -13.3% | 0 s |
| 9 | *Sinister Strike* | community simulator | - | 340 | -19.9% | 612 | -12.0% | 0 s |
| 10 | *Subtlety Hemo 15/0/36* | community simulator | - | 270 | -36.3% | 491 | -29.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Combat 361 -> 425 DPS (+17.7%), sim preset: Combat Dual-Wield 15/33/3 355 -> 394 DPS (+11.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
  5. spell probe: insert in the middle: cast Mutilate (+15.6%, pass 4)
  6. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-09, 4 changes to the base rotation; third-seed check: combat-ml-raid 718 -> 736 DPS (+2.5%), sim preset: Combat Dual-Wield 15/33/3 704 -> 719 DPS (+2.0%), combat-daggers-raid 713 -> 729 DPS (+2.1%), opt-combat-daggers-raid-raid-dps 702 -> 713 DPS (+1.7%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Mutilate (+9.9%, pass 4)
  4. drop the condition: if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush (+1.5%, pass 6)

| # | Priority (the first line whose condition holds is cast) | [`combat-ml-raid`](combat-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 12 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.9 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice | 2.8 |
| 3 | if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate | 0.3 |
| 6 | cast Backstab | 11.5 |

Lines of the simulator's rotation these builds never cast: cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`combat-ml-raid`](combat-ml-raid.md) |
|---|---|
| Auto Attack | 49% |
| Backstab | 36% |
| Deadly Poison | 6% |
| Dense Sharpening Stone | 3% |
| Dragonbreath Chili | 2% |
| Goblin Sapper Charge | 2% |
| Eviscerate | 2% |

## Notes

- Against the best hand draft combat-daggers-raid in a full raid, same gear and fights (100,000, one seed): +1.1% (under the 2% bar: the hand draft stays the pick).
- Where the simulator measured no difference, the points follow combat-daggers-raid: Improved Sinister Strike → Lightning Reflexes (2 points), Endurance → Deflection (the same DPS as the search winner 16/33/2 on one seed, 30,000 fights).
- Search result (full raid): 16/33/2 at 720.3 ± 0.10 DPS over 100,000 fights; runner-up 16/33/2 (+0.18%; the winner takes Cold Blood 1; the runner-up Improved Poisons 1); 3,601 builds simulated; certificate: 1 confirmed move first, then none of its 295 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 16/33/2 at 672.3 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 16/33/2 at 424.7 DPS.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Combat: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- A machine-searched Combat build: check it against the community's Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
