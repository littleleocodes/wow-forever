# Assassination — Raid (machine-learning search) — 30/21/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/21/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry assassination-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Assassination (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Vile Poisons** | 3/5 | moved | Increases the damage dealt by your poisons by 12% and gives your poisons an additional 24% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |

### Subtlety (0)

*No points.*

## Rank among our builds and the community simulator's

**4 of 5** for `assassination-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`assassination-seal-fate-raid`](assassination-seal-fate-raid.md) | ours: hand draft | 30/19/2 | 373 | +0.0% | 657 | -1.0% | 0 s |
| 2 | [`assassination-mutilate-raid`](assassination-mutilate-raid.md) | ours: hand draft | 30/21/0 | 371 | -0.6% | 643 | -3.2% | 0 s |
| 3 | [`daggers-split-open-raid`](daggers-split-open-raid.md) | ours: derived (open search) | 28/21/2 | 356 | -4.5% | 664 | +0.0% | 0 s |
| 4 | **[`assassination-ml-raid`](assassination-ml-raid.md)** | ours: derived (ML search) | 30/21/0 | 356 | -4.7% | 662 | -0.3% | 0 s |
| 5 | *Asn Muti* | community simulator | - | 345 | -7.5% | 648 | -2.3% | 0 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-10-24, 7 changes to the base rotation; third-seed check: assassination-ml-raid 285 -> 662 DPS (+132.1%), sim preset: Mutilate 621 -> 624 DPS (+0.5%), assassination-mutilate-raid 280 -> 643 DPS (+129.8%), assassination-seal-fate-raid 285 -> 657 DPS (+130.3%), daggers-split-open-raid 635 -> 657 DPS (+3.3%)):
  1. insert before the filler: cast Backstab (+0.8%, pass 1)
  2. spell probe: insert at the end: cast Hemorrhage (+9.9%, pass 5)
  3. spell probe: insert in the middle: if auraIsInactive: cast Ghostly Strike (+1.8%, pass 5)
  4. move down below 'cast Mutilate': cast Backstab (+0.2%, pass 9)
  5. spell probe: insert in the middle: if auraIsInactive: cast Adrenaline Rush (+1.4%, pass 11)
  6. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+1.3%, pass 12)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.2%, pass 12)

| # | Priority (the first line whose condition holds is cast) | [`assassination-ml-raid`](assassination-ml-raid.md) casts/min |
|---|---|---|
| 1 | cast Backstab (rank 8) | 9.5 |
| 2 | if time left on Expose Armor < 3 and combo points ≥ 3.75 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor | 1.8 |
| 3 | if combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 12: cast Slice and Dice | 2.9 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if combo points ≥ 5 and Slice and Dice is up: cast Cold Blood | 0.3 |
| 6 | if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (rank 8) | 1.8 |

Lines of the simulator's rotation these builds never cast: cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Mutilate (its condition never held in these fights); cast Hemorrhage (needs the Hemorrhage talent).

Damage by ability:

| Ability | [`assassination-ml-raid`](assassination-ml-raid.md) |
|---|---|
| Auto Attack | 44% |
| Backstab | 28% |
| spell 25349 | 10% |
| Eviscerate | 9% |
| spell 11337 | 6% |
| Goblin Sapper Charge | 2% |

## Notes

- Against the best hand draft assassination-seal-fate-raid in a full raid, same gear and fights (100,000, one seed): +1.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow assassination-seal-fate-raid: Improved Sinister Strike → Lightning Reflexes, Endurance → Lightning Reflexes, Improved Sprint → Lightning Reflexes (2 points) (the same DPS as the search winner 30/21/0 on one seed, 30,000 fights).
- Search result (full raid): 30/21/0 at 673.8 ± 0.09 DPS over 100,000 fights; runner-up 30/21/0 (+0.00%; the winner takes Improved Sinister Strike 1, Lightning Reflexes 1; the runner-up Improved Sinister Strike 2); 1,782 builds simulated; certificate: none of its 182 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 30/21/0 at 667.9 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 38/11/2 at 192.3 DPS.

## Open questions (verify in the live game)

- A machine-searched Assassination build: check it against the community's Assassination builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
