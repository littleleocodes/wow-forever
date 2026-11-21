# Subtlety — Raid (machine-learning search) — 12/8/31

*[Rogue](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/8/31 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-11-10 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry subtlety-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Assassination (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Improved Slice and Dice** | 3/3 | unchanged | Increases the duration of your Slice and Dice ability by 45%. |
| **Blood Splatter** | 1/1 | **NEW** | Increases the duration of your Rupture ability by 6 seconds and your Garrote ability by 9 seconds. |

### Combat (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Subtlety (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Master of Deception** | 2/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 2 levels higher. |
| **Opportunity** | 5/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 20%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Camouflage** | 3/3 | changed | Grants 15% increased movement speed in stealth and reduces stealth's cooldown by 6 seconds. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |
| **Boot Knife** | 5/5 | **NEW** | Gives your Shank ability a 100% chance to add 2 Combo Points to the target. |
| **Death Mark** | 1/1 | **NEW** | Finishing move that marks the target, storing a portion of the damage dealt by your attacks per Combo Point. Garrote and Rupture damage is stored at twice the rate. After 6 sec, the stored damage is dealt up to a maximum increased by Attack Power and Critical Strike chance. |

## Rank among our builds and the community simulator's

**1 of 4** for `subtlety-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`subtlety-ml-raid`](subtlety-ml-raid.md)** | ours: derived (ML search) | 12/8/31 | 480 | +0.0% | 820 | -0.4% | 0 s |
| 2 | *Subtlety Hemo* | community simulator | - | 480 | +0.0% | 820 | -0.4% | 0 s |
| 3 | [`hybrid-assassination-subtlety-open-raid`](hybrid-assassination-subtlety-open-raid.md) | ours: derived (open search) | 27/2/22 | 465 | -3.2% | 823 | +0.0% | 0 s |
| 4 | [`subtlety-hemo-raid`](subtlety-hemo-raid.md) | ours: hand draft | 21/0/30 | 369 | -23.1% | 668 | -18.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/rogue/upstream/default.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-10 (17 changes, `subtlety-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/rogue/upstream/default.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-11-10 (24 changes, `subtlety-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: at -3: cast Blade Flurry; at -2s: cast Premeditation; at -1s: if “Start In Stealth”: cast Stealth.

| # | Priority (the first line whose condition holds is cast) | [`subtlety-ml-raid`](subtlety-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not “Use Ambush Opener” and “Use Vanish for Damage” and “Current Points less than 5” and not Garrote is on the target: cast Garrote | 2.3 |
| 2 | if not Garrote is on the target and energy ≥ current cost and not “Use Ambush Opener” and “Use Vanish for Damage” and “Current Points less than 5” and not “SnD Fall Imminent” and time into the fight ≥ 1s: cast Vanish | 0.5 |
| 3 | if not Vanish is ready: cast Preparation | 0.3 |
| 4 | if Slice and Dice is up: use every other cooldown when ready | as ready |
| 5 | if “Gnome Eureka - Should Cast”: strict sequence: wait until energy ≥ 90 | as ready |
| 6 | if (“Boot Knife Known” and combo points ≤ 3 and energy ≤ 80 or not “Boot Knife Known” and energy ≤ 80): cast Shank | 5.8 |
| 7 | if (not Blade Flurry is known or Blade Flurry is up): cast OffensivePotion | as ready |
| 8 | if (energy ≤ 15 and not Death Mark is taken or Eureka! is known and energy ≤ 25 and energy ≤ 25 or energy ≤ 25 and Death Mark is on the target) and (combo points < 3 or “Expose - Low Duration” or Eureka! is up): cast Thistle Tea | as ready |
| 9 | if combo points ≤ 3: cast Premeditation | 1.0 |
| 10 | if combo points ≥ 4: cast Death Mark | 4.7 |
| 11 | if (Blood Splatter is taken or Hemorrhage is taken) and (combo points ≥ 3) and not Rupture is on the target and not “Fight About to End” and not “Expose - Prevent Other Finishers” and not Flawless Execution is taken: cast Rupture | 2.8 |
| 12 | if “At or Below SnD Clipping Threshold” and “Above SnD Point Threshold” and not “Fight About to End” and not “Expose - Prevent Other Finishers”: cast Slice and Dice | 2.9 |
| 13 | if “Current Points less than 5” and (not in front of the target or “Dirty Deeds Known”) and time left on Garrote ≤ 4s: cast Ghostly Strike | 2.0 |
| 14 | if not “Use Backstab” and “Current Points less than 5” and (not “SnD Fall Imminent” or energy > (current cost + current cost) and not “SnD Fall Imminent” or not “Above SnD Point Threshold” or “In Danger of Energy Capping” or “Expose - Low Duration”) and “Gnome Eureka - Active or Not Ready” and (time left on Garrote ≥ 8s or not Ghostly Strike is taken or “In Danger of Energy Capping”): cast Hemorrhage | 12.9 |

Lines of the simulator's rotation these builds never cast: cast Expose Armor, cast Ambush, cast Vanish, cast Hemorrhage, cast Backstab (rank 8) (a switch this rotation keeps off); cast Blood Fury, cast Elune's Light, cast Eureka!, cast Eviscerate (rank 8), cast Sinister Strike (its condition never held in these fights); strict sequence: cast Blood Fury; cast Blade Flurry (needs the Blade Flurry talent); cast Adrenaline Rush, strict sequence: cast Blood Fury; cast Adrenaline Rush, strict sequence: cast Elune's Light; cast Adrenaline Rush (needs the Adrenaline Rush talent); cast Cold Blood (needs the Cold Blood talent); cast Mutilate (needs the Mutilate talent).

Damage by ability:

| Ability | [`subtlety-ml-raid`](subtlety-ml-raid.md) |
|---|---|
| Death Mark | 27% |
| Auto Attack | 26% |
| Garrote | 14% |
| Rupture | 13% |
| Hemorrhage | 8% |
| spell 25349 | 4% |
| spell 11337 | 4% |
| Ghostly Strike | 2% |
| Goblin Sapper Charge | 1% |
| Shank | 1% |

## Notes

- Against the best hand draft subtlety-hemo-raid in a full raid, same gear and fights (100,000, one seed): +23.4% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow subtlety-hemo-raid: Elusiveness → Master of Deception (2 points) (the same DPS as the search winner 12/8/31 on one seed, 30,000 fights).
- Search result (full raid): 12/8/31 at 789.4 ± 0.08 DPS over 100,000 fights; runner-up 12/8/31 (+0.00%; the winner takes Elusiveness 2; the runner-up Elusiveness 1, Heightened Senses 1); 1,466 builds simulated; certificate: none of its 282 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 12/8/31 at 773.8 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 12/8/31 at 473.0 DPS.

## Open questions (verify in the live game)

- A machine-searched Subtlety build: check it against the community's Subtlety builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
