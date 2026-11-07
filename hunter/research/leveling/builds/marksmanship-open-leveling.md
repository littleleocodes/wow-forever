# Marksmanship — Leveling (open talent search) — 21/30/0

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Marksmanship leveling build the open leveling search found on 2026-11-03: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the mm-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (mm-raid). 

## Point allocation

### Beast Mastery (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 1/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 1/2 | changed | Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting. |

### Marksmanship (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Rapid Recuperation** | 1/2 | **NEW** | Afflicting a target with Serpent Sting allows 25% of your Mana Regeneration to continue while casting for 15 sec, increased to 50% when Rapid Killing is consumed. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 15%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |

### Survival (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Marksmanship | Lethal Attacks | 5 | 0/5/0 |
| 15-19 | Marksmanship | Careful Aim | 5 | 0/10/0 |
| 20-22 | Marksmanship | Improved Stings | 3 | 0/13/0 |
| 23-24 | Marksmanship | Rapid Killing | 2 | 0/15/0 |
| 25 | Marksmanship | Trueshot Aura | 1 | 0/16/0 |
| 26-29 | Marksmanship | Efficiency | 4 | 0/20/0 |
| 30 | Marksmanship | Rapid Recuperation | 1 | 0/21/0 |
| 31 | Marksmanship | Efficiency | 1 | 0/22/0 |
| 32-34 | Marksmanship | Barrage | 3 | 0/25/0 |
| 35-39 | Marksmanship | Ranged Weapon Specialization | 5 | 0/30/0 |
| 40-44 | Beast Mastery | Deadly Aspects | 5 | 5/30/0 |
| 45-46 | Beast Mastery | Focused Fire | 2 | 7/30/0 |
| 47-48 | Beast Mastery | Endurance Training | 2 | 9/30/0 |
| 49 | Beast Mastery | Improved Aspect of the Monkey | 1 | 10/30/0 |
| 50-54 | Beast Mastery | Unleashed Fury | 5 | 15/30/0 |
| 55-59 | Beast Mastery | Ferocity | 5 | 20/30/0 |
| 60 | Beast Mastery | Bestial Discipline | 1 | 21/30/0 |

## Core talents (priority order)

1. **Efficiency** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Unleashed Fury** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Lethal Attacks** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ferocity** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Rapid Recuperation** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Stings** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Trueshot Aura** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Ranged Weapon Specialization** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +6.6% faster than the hand draft leveling-beast-mastery, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.74; opt-bm-leveling-leveling-st 23.05, opt-bm-leveling-solo-60 23.11, opt-mm-raid-leveling-st 23.22, leveling-beast-mastery 24.24. The search simulated 27,163 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Marksmanship leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/52210005050001-005355200101305--12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
