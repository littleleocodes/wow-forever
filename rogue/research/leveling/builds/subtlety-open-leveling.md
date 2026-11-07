# Subtlety — Leveling (open talent search) — 0/20/31

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/20/31 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build the open leveling search found on 2026-11-04: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +4.0% faster per kill than subtlety-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (0)

*No points.*

### Combat (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 1/3 | changed | Increases your Parry chance by 2%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 1/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 5. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |

### Subtlety (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 5/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 20%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Improved Ambush** | 1/3 | moved | Increases the critical strike chance of your Ambush ability by 15%. |
| **Dirty Tricks** | 1/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |
| **Boot Knife** | 5/5 | **NEW** | Gives your Shank ability a 100% chance to add 2 Combo Points to the target. |
| **Death Mark** | 1/1 | **NEW** | Finishing move that marks the target, storing a portion of the damage dealt by your attacks per Combo Point. Garrote and Rupture damage is stored at twice the rate. After 6 sec, the stored damage is dealt up to a maximum increased by Attack Power and Critical Strike chance. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Combat | Coup de Grace | 3 | 0/3/0 |
| 13-14 | Combat | Lightning Reflexes | 2 | 0/5/0 |
| 15-17 | Combat | Precision | 3 | 0/8/0 |
| 18 | Combat | Deflection | 1 | 0/9/0 |
| 19-21 | Combat | Lightning Reflexes | 3 | 0/12/0 |
| 22-23 | Combat | Efficient Strikes | 2 | 0/14/0 |
| 24 | Combat | Composure | 1 | 0/15/0 |
| 25 | Combat | Flawless Execution | 1 | 0/16/0 |
| 26-27 | Combat | Weapon Expertise | 2 | 0/18/0 |
| 28-29 | Combat | Aggression | 2 | 0/20/0 |
| 30-31 | Subtlety | Opportunity | 2 | 0/20/2 |
| 32-34 | Subtlety | Setup | 3 | 0/20/5 |
| 35-36 | Subtlety | Dirty Deeds | 2 | 0/20/7 |
| 37-39 | Subtlety | Master of Deception | 3 | 0/20/10 |
| 40-42 | Subtlety | Serrated Blades | 3 | 0/20/13 |
| 43 | Subtlety | Initiative | 1 | 0/20/14 |
| 44 | Subtlety | Premeditation | 1 | 0/20/15 |
| 45 | Subtlety | Ghostly Strike | 1 | 0/20/16 |
| 46-47 | Subtlety | Initiative | 2 | 0/20/18 |
| 48-49 | Subtlety | Opportunity | 2 | 0/20/20 |
| 50 | Subtlety | Preparation | 1 | 0/20/21 |
| 51 | Subtlety | Opportunity | 1 | 0/20/22 |
| 52 | Subtlety | Improved Ambush | 1 | 0/20/23 |
| 53 | Subtlety | Dirty Tricks | 1 | 0/20/24 |
| 54 | Subtlety | Hemorrhage | 1 | 0/20/25 |
| 55-59 | Subtlety | Boot Knife | 5 | 0/20/30 |
| 60 | Subtlety | Death Mark | 1 | 0/20/31 |

## Core talents (priority order)

1. **Boot Knife** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Coup de Grace** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Hemorrhage** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
4. **Initiative** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Dirty Deeds** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Flawless Execution** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Efficient Strikes** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Weapon Expertise** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.44; subtlety-leveling 23.33. The search simulated 32,176 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/-32501300010122-335201131301001151-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
