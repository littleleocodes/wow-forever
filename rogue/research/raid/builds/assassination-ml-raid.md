# Assassination — Raid (machine-learning search) — 29/22/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/22/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry assassination-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Assassination (29)

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
| **Vile Poisons** | 2/5 | moved | Increases the damage dealt by your poisons by 8% and gives your poisons an additional 16% chance to resist dispel effects. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |
| **Seal Fate** | 3/3 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |

### Subtlety (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 5** for `assassination-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Asn Muti* | community simulator | - | 451 | +0.0% | 838 | -0.1% | 0 s |
| 2 | [`assassination-open-raid`](assassination-open-raid.md) | ours: derived (open search) | 31/19/1 | 450 | -0.2% | 839 | +0.0% | 0 s |
| 3 | **[`assassination-ml-raid`](assassination-ml-raid.md)** | ours: derived (ML search) | 29/22/0 | 329 | -27.1% | 710 | -15.3% | 0 s |
| 4 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 28/21/2 | 319 | -29.2% | 701 | -16.4% | 0 s |
| 5 | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) | ours: hand draft | 29/22/0 | 315 | -30.2% | 691 | -17.6% | 0 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 15 passes, the last 2026-11-09, 11 changes to the base rotation; third-seed check: open winner 804 -> 813 DPS (+1.1%), assassination-seal-fate-raid 609 -> 687 DPS (+12.9%), sim preset: Asn Muti 804 -> 812 DPS (+0.9%), assassination-mutilate-raid 610 -> 679 DPS (+11.2%), assassination-ml-raid 628 -> 696 DPS (+10.7%), daggers-split-open-raid 606 -> 686 DPS (+13.1%)):
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

| # | Priority (the first line whose condition holds is cast) | [`assassination-ml-raid`](assassination-ml-raid.md) casts/min |
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
| 12 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 3.6 |
| 13 | if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike | 14.8 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); strict sequence: cast Blood Fury; cast Blade Flurry (needs the Blade Flurry talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Death Mark (needs the Death Mark talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`assassination-ml-raid`](assassination-ml-raid.md) |
|---|---|
| Auto Attack | 42% |
| Eviscerate | 17% |
| Sinister Strike | 16% |
| spell 25349 | 11% |
| spell 11337 | 9% |
| Goblin Sapper Charge | 2% |
| Garrote | 2% |
| Shank | 1% |

## Notes

- Against the best hand draft assassination-seal-fate-raid in a full raid, same gear and fights (100,000, one seed): +1.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow assassination-seal-fate-raid: Improved Sinister Strike → Lightning Reflexes, Endurance → Lightning Reflexes, Improved Sprint → Lightning Reflexes (2 points) (the same DPS as the search winner 30/21/0 on one seed, 30,000 fights).
- Search result (full raid): 30/21/0 at 673.8 ± 0.09 DPS over 100,000 fights; runner-up 30/21/0 (+0.00%; the winner takes Improved Sinister Strike 1, Lightning Reflexes 1; the runner-up Improved Sinister Strike 2); 1,782 builds simulated; certificate: none of its 182 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 30/21/0 at 667.9 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 38/11/2 at 192.3 DPS.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 30/21/0 -> 29/22/0; Lethality 3 -> 2 (rank cap); Seal Fate 5 -> 3 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Improved Expose Armor (tier gating for Cold Blood); +1 Improved Expose Armor (tier gating for Cold Blood); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Weapon Expertise (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Aggression (tier gating for Dual Wield Specialization); +1 Vigor (tier gating for Mutilate); +1 Vigor (tier gating for Mutilate); -1 Mutilate (over 51); -1 Vile Poisons (over 51) (refill: the combat-daggers-raid model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Assassination build: check it against the community's Assassination builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
