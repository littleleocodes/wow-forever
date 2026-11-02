# Subtlety — Leveling (open talent search) — 12/9/30

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/9/30 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +0.9% faster per kill than subtlety-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 4/5 | changed | Increases your critical strike chance with all attacks and Poisons by 4%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |

### Combat (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 2/5 | unchanged | Increases your Dodge chance by 2%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Subtlety (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Camouflage** | 4/5 | changed | Reduces your speed penalty from your Stealth ability by 12% and reduces its cooldown by 5 sec. |
| **Master of Deception** | 2/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 2 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Dirty Tricks** | 2/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. |
| **Improved Distract** | 2/2 | **NEW** | Increases the radius of your Distract ability by 5 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 2 levels lower. |
| **Heightened Senses** | 2/2 | changed | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point. |
| **Cutthroat** | 1/5 | **NEW** | Your Backstab has a 3% chance to cause your next Ambush within 10 sec to not require Stealth. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Assassination | Remorseless Attacks | 2 | 2/0/0 |
| 12-14 | Combat | Improved Eviscerate | 3 | 2/3/0 |
| 15 | Assassination | Malice | 1 | 3/3/0 |
| 16-17 | Combat | Lightning Reflexes | 2 | 3/5/0 |
| 18-20 | Combat | Precision | 3 | 3/8/0 |
| 21-23 | Assassination | Malice | 3 | 6/8/0 |
| 24-25 | Assassination | Murder | 2 | 8/8/0 |
| 26-27 | Assassination | Ruthlessness | 2 | 10/8/0 |
| 28 | Assassination | Relentless Strikes | 1 | 11/8/0 |
| 29-30 | Subtlety | Opportunity | 2 | 11/8/2 |
| 31-32 | Subtlety | Master of Deception | 2 | 11/8/4 |
| 33 | Subtlety | Camouflage | 1 | 11/8/5 |
| 34-36 | Subtlety | Setup | 3 | 11/8/8 |
| 37-38 | Subtlety | Camouflage | 2 | 11/8/10 |
| 39 | Subtlety | Ghostly Strike | 1 | 11/8/11 |
| 40-42 | Subtlety | Initiative | 3 | 11/8/14 |
| 43 | Subtlety | Camouflage | 1 | 11/8/15 |
| 44-46 | Subtlety | Serrated Blades | 3 | 11/8/18 |
| 47 | Subtlety | Premeditation | 1 | 11/8/19 |
| 48-50 | Subtlety | Improved Ambush | 3 | 11/8/22 |
| 51-52 | Subtlety | Heightened Senses | 2 | 11/8/24 |
| 53 | Assassination | Ruthlessness | 1 | 12/8/24 |
| 54 | Combat | Deflection | 1 | 12/9/24 |
| 55-56 | Subtlety | Dirty Tricks | 2 | 12/9/26 |
| 57-58 | Subtlety | Improved Distract | 2 | 12/9/28 |
| 59 | Subtlety | Hemorrhage | 1 | 12/9/29 |
| 60 | Subtlety | Cutthroat | 1 | 12/9/30 |

## Core talents (priority order)

1. **Setup** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Remorseless Attacks** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Eviscerate** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Improved Ambush** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Relentless Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.40; subtlety-leveling 25.64. The search simulated 41,965 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/0243201-302013-422302331221300101-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
