# Subtlety — Leveling (derived) — 5/16/30

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/16/30 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Subtlety build, 30+ points kept in Subtlety, playing the subtlety-leveling rotation; the talent order is the stats model's (combat-swords-raid).

## Point allocation

### Assassination (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 3/5 | changed | Increases your critical strike chance with all attacks and Poisons by 3%. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |

### Subtlety (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Camouflage** | 2/5 | changed | Reduces your speed penalty from your Stealth ability by 6% and reduces its cooldown by 3 sec. |
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Quietus** | 5/5 | **NEW** | Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 10% more damage against targets below 35% health. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Combat | Improved Sinister Strike | 1 | 0/1/0 |
| 11-12 | Assassination | Remorseless Attacks | 2 | 2/1/0 |
| 13 | Combat | Improved Sinister Strike | 1 | 2/2/0 |
| 14-16 | Combat | Improved Eviscerate | 3 | 2/5/0 |
| 17 | Combat | Deflection | 1 | 2/6/0 |
| 18-19 | Combat | Precision | 2 | 2/8/0 |
| 20-21 | Combat | Deflection | 2 | 2/10/0 |
| 22 | Combat | Riposte | 1 | 2/11/0 |
| 23 | Combat | Precision | 1 | 2/12/0 |
| 24-26 | Combat | Lightning Reflexes | 3 | 2/15/0 |
| 27 | Combat | Flawless Execution | 1 | 2/16/0 |
| 28-30 | Assassination | Malice | 3 | 5/16/0 |
| 31-32 | Subtlety | Opportunity | 2 | 5/16/2 |
| 33-35 | Subtlety | Master of Deception | 3 | 5/16/5 |
| 36-38 | Subtlety | Setup | 3 | 5/16/8 |
| 39-40 | Subtlety | Elusiveness | 2 | 5/16/10 |
| 41 | Subtlety | Ghostly Strike | 1 | 5/16/11 |
| 42-44 | Subtlety | Initiative | 3 | 5/16/14 |
| 45 | Subtlety | Camouflage | 1 | 5/16/15 |
| 46-48 | Subtlety | Serrated Blades | 3 | 5/16/18 |
| 49 | Subtlety | Premeditation | 1 | 5/16/19 |
| 50 | Subtlety | Heightened Senses | 1 | 5/16/20 |
| 51 | Subtlety | Preparation | 1 | 5/16/21 |
| 52-53 | Subtlety | Dirty Deeds | 2 | 5/16/23 |
| 54 | Subtlety | Heightened Senses | 1 | 5/16/24 |
| 55 | Subtlety | Camouflage | 1 | 5/16/25 |
| 56-60 | Subtlety | Quietus | 5 | 5/16/30 |

## Core talents (priority order)

1. **Riposte** — The scorer's value in this build: +11.5% of its score (model combat-swords-raid).
2. **Improved Sinister Strike** — The scorer's value in this build: +7.6% of its score (model combat-swords-raid).
3. **Serrated Blades** — The scorer's value in this build: +7.4% of its score (model combat-swords-raid).
4. **Flawless Execution** — The scorer's value in this build: +7.4% of its score (model combat-swords-raid).
5. **Precision** — The scorer's value in this build: +7.1% of its score (model combat-swords-raid).
6. **Remorseless Attacks** — The scorer's value in this build: +7.0% of its score (model combat-swords-raid).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start subtlety-leveling, moves: none (the start was already the best the search found). Race against subtlety-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.0% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- A derived Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
