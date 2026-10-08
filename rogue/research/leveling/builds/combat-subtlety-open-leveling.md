# Combat-Subtlety — Leveling (open talent search) — 11/17/23

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/17/23 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat-Subtlety (a Combat/Subtlety hybrid) leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +3.9% faster per kill than subtlety-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 2/3 | changed | Increases the duration of your Gouge ability by 1 sec. |
| **Malice** | 3/5 | changed | Increases your critical strike chance with all attacks and Poisons by 3%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |

### Combat (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 1/5 | changed | Increases the damage done by your off-hand weapon by 5%. |

### Subtlety (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Improved Distract** | 1/2 | **NEW** | Increases the radius of your Distract ability by 3 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 1 level lower. |
| **Heightened Senses** | 1/2 | changed | Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-14 | Subtlety | Master of Deception | 3 | 0/0/5 |
| 15-17 | Subtlety | Setup | 3 | 0/0/8 |
| 18-19 | Subtlety | Elusiveness | 2 | 0/0/10 |
| 20 | Subtlety | Ghostly Strike | 1 | 0/0/11 |
| 21-23 | Subtlety | Initiative | 3 | 0/0/14 |
| 24 | Subtlety | Improved Distract | 1 | 0/0/15 |
| 25-27 | Subtlety | Serrated Blades | 3 | 0/0/18 |
| 28 | Subtlety | Premeditation | 1 | 0/0/19 |
| 29 | Subtlety | Heightened Senses | 1 | 0/0/20 |
| 30 | Subtlety | Hemorrhage | 1 | 0/0/21 |
| 31-32 | Subtlety | Dirty Deeds | 2 | 0/0/23 |
| 33-35 | Combat | Improved Eviscerate | 3 | 0/3/23 |
| 36-37 | Combat | Lightning Reflexes | 2 | 0/5/23 |
| 38-40 | Combat | Precision | 3 | 0/8/23 |
| 41-43 | Combat | Deflection | 3 | 0/11/23 |
| 44 | Combat | Riposte | 1 | 0/12/23 |
| 45-47 | Combat | Lightning Reflexes | 3 | 0/15/23 |
| 48 | Combat | Flawless Execution | 1 | 0/16/23 |
| 49-51 | Assassination | Malice | 3 | 3/16/23 |
| 52-53 | Assassination | Improved Gouge | 2 | 5/16/23 |
| 54-55 | Assassination | Murder | 2 | 7/16/23 |
| 56-58 | Assassination | Ruthlessness | 3 | 10/16/23 |
| 59 | Assassination | Relentless Strikes | 1 | 11/16/23 |
| 60 | Combat | Dual Wield Specialization | 1 | 11/17/23 |

## Core talents (priority order)

1. **Setup** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Hemorrhage** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Eviscerate** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
4. **Flawless Execution** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Precision** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Relentless Strikes** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Dirty Deeds** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.52; subtlety-leveling 26.51. The search simulated 88,664 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Combat-Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/2033201-305033010011-0323200311113201-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
