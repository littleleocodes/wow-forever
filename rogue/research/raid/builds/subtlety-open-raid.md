# Subtlety — Raid (open talent search) — 20/0/31

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/0/31 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety raid build the open talent search found on 2026-10-10: every legal 51-point build with no tree rule, searched in the community simulator's subtlety-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.5% over subtlety-hemo-raid, the best of our builds in that rotation.

## Point allocation

### Assassination (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |

### Combat (0)

*No points.*

### Subtlety (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Camouflage** | 3/5 | changed | Reduces your speed penalty from your Stealth ability by 9% and reduces its cooldown by 4 sec. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 1/3 | changed | Gives you a 33% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Dirty Tricks** | 1/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Improved Distract** | 2/2 | **NEW** | Increases the radius of your Distract ability by 5 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 2 levels lower. |
| **Heightened Senses** | 1/2 | changed | Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point. |
| **Quietus** | 5/5 | **NEW** | Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 10% more damage against targets below 35% health. |
| **Thousand Cuts** | 1/1 | **NEW** | When your Rupture ability deals periodic damage, the Energy cost of your next Hemorrhage or Backstab ability within 10 sec is reduced by 3, stacking up to 5 times. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |

## Core talents (priority order)

1. **Hemorrhage** — 387 DPS lost without it (57% of the build in a full raid; removal, 12,000 fights).
2. **Relentless Strikes** — 52 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
3. **Ruthlessness** — 46 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
4. **Thousand Cuts** — 39 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Malice** — 29 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
6. **Improved Slice and Dice** — 25 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Serrated Blades** — 25 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**2 of 3** for `subtlety-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`subtlety-hemo-raid`](subtlety-hemo-raid.md) | ours: hand draft | 20/0/31 | 399 | +0.0% | 640 | -0.5% | 0 s |
| 2 | **[`subtlety-open-raid`](subtlety-open-raid.md)** | ours: derived (open search) | 20/0/31 | 374 | -6.3% | 643 | +0.0% | 0 s |
| 3 | *Subtlety Hemo 15/0/36* | community simulator | - | 356 | -10.6% | 600 | -6.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-10, 17 changes to the base rotation; third-seed check: open winner 349 -> 374 DPS (+7.2%), subtlety-hemo-raid 347 -> 399 DPS (+14.9%), sim preset: Subtlety Hemo 15/0/36 319 -> 356 DPS (+11.5%)):
  1. drop 'combo points ≥ 4' from the condition: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+1.8%, pass 1)
  2. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.6%, pass 1)
  3. threshold 20s -> 40s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice (+0.6%, pass 1)
  4. threshold 40s -> 80s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 40s: cast Slice and Dice (+0.5%, pass 1)
  5. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+2.5%, pass 1)
  6. threshold 4 -> 5: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+2.2%, pass 1)
  7. only with 20s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  8. insert at the top: if energy ≤ 29 and combo points < 5 and time left on Expose Armor ≤ 6 and timeToNextEnergyTick > 1 and not Adrenaline Rush is up: cast Thistle Tea (+0.4%, pass 3)
  9. threshold 20s -> 10s: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 20s: cast Expose Armor (+0.3%, pass 3)
  10. threshold 8 -> 12: if not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 3)
  11. threshold 3 -> 5: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 3)
  12. insert in the middle: cast Garrote (+3.0%, pass 4)
  13. spell probe: insert before the filler: cast Blade Flurry (+0.5%, pass 5)
  14. threshold 80s -> 160s: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 80s: cast Slice and Dice (+1.8%, pass 6)
  15. threshold 60 -> 30: if energy ≥ 60 and combo points ≤ 1 and Slice and Dice is up and time left in the fight > 10: cast Vanish (+0.5%, pass 6)
  16. drop: if energy ≤ 29 and combo points < 5 and time left on Expose Armor ≤ 6 and timeToNextEnergyTick > 1 and not Adrenaline Rush is up: cast Thistle Tea (+3.0%, pass 7)
  17. insert at the end: cast Preparation (+0.3%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-14, 12 changes to the base rotation; third-seed check: ):
  1. drop 'combo points ≥ 4' from the condition: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+1.1%, pass 1)
  2. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  3. insert at the top: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 2)
  4. threshold 5 -> 3.75: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 20s: cast Slice and Dice (+0.3%, pass 2)
  5. threshold 4 -> 2: if combo points ≥ 4 and not Rupture is on the target and time left in the fight > 8: cast Rupture (+0.2%, pass 2)
  6. insert in the middle: if not Garrote is on the target: cast Garrote (+1.7%, pass 4)
  7. spell probe: insert before the filler: cast Cold Blood (+0.4%, pass 5)
  8. spell probe: insert before the filler: if auraIsInactive: cast Ghostly Strike (+0.4%, pass 5)
  9. threshold 1 -> 3: if energy ≥ 60 and combo points ≤ 1 and Slice and Dice is up and time left in the fight > 10: cast Vanish (+0.2%, pass 6)
  10. move down below 'cast Cold Blood': if auraIsInactive: cast Ghostly Strike (+0.2%, pass 6)
  11. insert before the filler: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 2 and time left in the fight > 9): cast Slice and Dice (+0.2%, pass 7)
  12. spell probe: insert before the filler: cast Blade Flurry (+0.3%, pass 9)

| # | Priority (the first line whose condition holds is cast) | [`subtlety-open-raid`](subtlety-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Expose Armor < 5 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.9 |
| 2 | if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9) and time left in the fight ≥ 160s: cast Slice and Dice | 0.7 |
| 3 | cast Premeditation | 0.7 |
| 4 | cast Garrote | 0.7 |
| 5 | if not Rupture is on the target and time left in the fight > 12: cast Rupture | 4.8 |
| 6 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 7 | cast Hemorrhage | 19.6 |
| 8 | cast Preparation | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Vanish, cast Ambush, cast Eviscerate (rank 8) (its condition never held in these fights); cast Blade Flurry (needs the Blade Flurry talent).

Damage by ability:

| Ability | [`subtlety-open-raid`](subtlety-open-raid.md) |
|---|---|
| Auto Attack | 40% |
| Hemorrhage | 28% |
| Rupture | 16% |
| Deadly Poison | 4% |
| Dense Sharpening Stone | 4% |
| Garrote | 2% |
| Dragonbreath Chili | 2% |
| Eviscerate | 2% |
| Goblin Sapper Charge | 2% |

## Notes

- +0.5% over the best hand draft of the spec, subtlety-hemo-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (subtlety-raid, full raid): 20/0/31 (Subtlety) at 676.1 DPS; subtlety-hemo-raid 672.7 in the same fights; 4,312 builds simulated, 2 independent runs reached the top.
- The subtlety-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): combat-swords-raid -15.0%, combat-daggers-raid -57.1%, assassination-raid -9.4%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Camouflage, Setup, Dirty Tricks, Improved Ambush, Improved Distract, Heightened Senses.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-10 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Camouflage -> Ghostly Strike (survival). Net -0.15% on a third seed.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Subtlety: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- An open-search Subtlety build: check it against the community's Subtlety builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/rogue/60/005303103014--4021013302113211501-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
