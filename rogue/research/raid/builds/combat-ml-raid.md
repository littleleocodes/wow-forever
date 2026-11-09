# Combat — Raid (machine-learning search) — 21/30/0

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-03 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry combat-daggers-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Assassination (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 2/3 | changed | Increases the duration of your Gouge ability by 1 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Improved Expose Armor** | 2/2 | changed | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Lethality** | 2/2 | changed | Grants 20% increased Critical Strike damage to your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Relentless Strikes** | 1/5 | unchanged | Your finishing moves have a 4% chance per Combo Point to restore 25 Energy. |

### Combat (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 2/3 | changed | Increases your Parry chance by 4%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Puncturing Wounds** | 3/3 | **NEW** | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |
| **Hack and Slash** | 5/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |

### Subtlety (0)

*No points.*

## Rank among our builds and the community simulator's

**8 of 8** for `combat-daggers-raid` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Subtlety Hemo* | community simulator | - | 480 | +0.0% | 785 | -2.9% | 0 s |
| 2 | *Asn Muti* | community simulator | - | 443 | -7.8% | 809 | +0.0% | 0 s |
| 3 | *Combat Venom* | community simulator | - | 395 | -17.8% | 706 | -12.7% | 0 s |
| 4 | *Combat SS* | community simulator | - | 358 | -25.6% | 676 | -16.4% | 0 s |
| 5 | *Combat BS* | community simulator | - | 344 | -28.4% | 755 | -6.7% | 0 s |
| 6 | [`combat-daggers-raid`](combat-daggers-raid.md) | ours: hand draft | 21/30/0 | 310 | -35.4% | 674 | -16.6% | 0 s |
| 7 | [`opt-combat-daggers-raid-raid-dps`](opt-combat-daggers-raid-raid-dps.md) | ours: optimizer | 21/30/0 | 310 | -35.4% | 674 | -16.6% | 0 s |
| 8 | **[`combat-ml-raid`](combat-ml-raid.md)** | ours: derived (ML search) | 21/30/0 | 310 | -35.4% | 674 | -16.6% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Combat 361 -> 425 DPS (+17.7%), sim preset: Combat Dual-Wield 15/33/3 355 -> 394 DPS (+11.0%)):
  1. insert at the top: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+9.7%, pass 1)
  2. only with 10s or more of the fight left: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3: cast Expose Armor (+0.2%, pass 1)
  3. only with 20s or more of the fight left: if (combo points ≥ 1 and not Slice and Dice is up and time left in the fight ≥ 6 or combo points ≥ 5 and time left on Slice and Dice < 3 and time left in the fight > 9): cast Slice and Dice (+0.3%, pass 1)
  4. threshold 3 -> 6: if time left on Expose Armor < 3 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.2%, pass 2)
  5. spell probe: insert in the middle: cast Mutilate (+15.6%, pass 4)
  6. threshold 6 -> 12: if time left on Expose Armor < 6 and combo points ≥ 5 and time left in the fight ≥ 3 and time left in the fight ≥ 10s: cast Expose Armor (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-11-08, 13 changes to the base rotation; third-seed check: combat-daggers-raid 615 -> 675 DPS (+9.7%), sim preset: Asn Muti 804 -> 809 DPS (+0.6%)):
  1. insert at the top: if combo points ≥ 4 and (Slice and Dice is up or energy ≥ 79 or time left in the fight < 6): cast Eviscerate (+0.9%, pass 1)
  2. insert at the top: if combo points ≥ 4 and Slice and Dice is up: cast Cold Blood (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Mutilate (+9.9%, pass 4)
  4. drop the condition: if energy < 59 and timeToNextEnergyTick < 1: cast Adrenaline Rush (+1.5%, pass 6)
  5. insert at the top: if (energy ≤ 15 or Eureka! is known and energy ≤ 25 and Eureka! is up) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea (+2.2%, pass 8)
  6. insert in the middle: if not Cutthroat is up and variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Backstab (rank 8) (+0.6%, pass 8)
  7. insert at the top: if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote (+0.3%, pass 8)
  8. rotation replaced by the official simulator's default.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+0.7%, pass 9)
  9. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and (not talentIsKnown or time left on Rupture ≥ 4 or variableRef or variableRef) and not variableRef: cast Eviscerate (rank 8) (+0.3%, pass 10)
  10. insert before the filler: cast Backstab (+1.5%, pass 11)
  11. drop: if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike (+3.1%, pass 11)
  12. threshold 4 -> 3: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.3%, pass 11)
  13. threshold 3 -> 1: if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 3 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) (+0.2%, pass 11)

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if variableRef: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`combat-ml-raid`](combat-ml-raid.md) casts/min |
|---|---|---|
| 1 | if variableRef: groupReference | as ready |
| 2 | if not variableRef and variableRef and variableRef and not Garrote is on the target: cast Garrote | 0.3 |
| 3 | if not Garrote is on the target and energy ≥ current cost and not variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 4 | if energy ≥ current cost and variableRef and variableRef and variableRef and not variableRef and time into the fight ≥ 1s: cast Vanish | 0.3 |
| 5 | if Blade Flurry is ready and Blood Fury is known: strict sequence: cast Blood Fury; cast Blade Flurry | 0.7 |
| 6 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 7 | groupReference | as ready |
| 8 | if (variableRef and combo points ≤ 3 and energy ≤ 80 or not variableRef and energy ≤ 80): cast Shank | 6.0 |
| 9 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 10 | if (energy ≤ 15 and not talentIsKnown or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or variableRef or Eureka! is up): cast Thistle Tea | as ready |
| 11 | if variableRef and variableRef and not variableRef and not variableRef: cast Slice and Dice | 3.3 |
| 12 | if combo points = 5 and not variableRef and energy ≥ current cost and not variableRef and not Elune's Light is up: cast Cold Blood | 0.3 |
| 13 | if (combo points ≥ 5 or combo points = 4 and Mutilate is known or combo points ≥ 4 and time left on Slice and Dice ≤ 6s and not variableRef or combo points ≥ 3 and variableRef) and not variableRef and not talentIsKnown: cast Eviscerate (rank 8) | 2.7 |
| 14 | if not Mutilate is known and not Hemorrhage is known and not variableRef and variableRef and (not variableRef or energy > (current cost + current cost) and not variableRef or not variableRef or variableRef or variableRef) and variableRef: cast Sinister Strike | 14.5 |

Lines of the simulator's rotation these builds never cast: cast Ambush, cast Blood Fury, cast Elune's Light, cast Eureka!, cast Rupture, cast Backstab (rank 8) (its condition never held in these fights); cast Preparation (needs the Preparation talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Premeditation (needs the Premeditation talent); cast Death Mark (needs the Death Mark talent); cast Ghostly Strike (needs the Ghostly Strike talent); cast Hemorrhage (needs the Hemorrhage talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`combat-ml-raid`](combat-ml-raid.md) |
|---|---|
| Auto Attack | 48% |
| Sinister Strike | 18% |
| Eviscerate | 14% |
| spell 25349 | 9% |
| spell 11337 | 6% |
| Goblin Sapper Charge | 2% |
| Garrote | 2% |
| Shank | 1% |

## Notes

- Against the best hand draft combat-daggers-raid in a full raid, same gear and fights (100,000, one seed): +1.1% (under the 2% bar: the hand draft stays the pick).
- Where the simulator measured no difference, the points follow combat-daggers-raid: Improved Sinister Strike → Lightning Reflexes (2 points), Endurance → Deflection (the same DPS as the search winner 16/33/2 on one seed, 30,000 fights).
- Search result (full raid): 16/33/2 at 720.3 ± 0.10 DPS over 100,000 fights; runner-up 16/33/2 (+0.18%; the winner takes Cold Blood 1; the runner-up Improved Poisons 1); 3,601 builds simulated; certificate: 1 confirmed move first, then none of its 295 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 16/33/2 at 672.3 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 16/33/2 at 424.7 DPS.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Combat: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 16/33/2 -> 21/30/0; Lethality 3 -> 2 (rank cap); Improved Eviscerate -> Coup de Grace (renamed); Dual Wield Specialization 5 -> 2 (rank cap); +1 Vigor (tier gating for Cold Blood); +1 Vigor (tier gating for Cold Blood); +1 Improved Expose Armor (tier gating for Relentless Strikes); +1 Improved Expose Armor (tier gating for Relentless Strikes); +1 Improved Gouge (tier gating for Relentless Strikes); +1 Improved Gouge (tier gating for Relentless Strikes); +1 Deflection (tier gating for Adrenaline Rush); -1 Opportunity (over 51); -1 Opportunity (over 51); -1 Adrenaline Rush (over 51) (refill: the combat-swords-raid model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Combat build: check it against the community's Combat builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
