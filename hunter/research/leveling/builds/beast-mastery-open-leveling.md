# Beast Mastery — Leveling (open talent search) — 31/16/4

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/16/4 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the bm-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (bm-leveling). +2.1% faster per kill than beast-mastery-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 2/5 | **NEW** | Increases your Attack Power by 40% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 30. |

### Survival (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 4/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 4%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Marksmanship | Lethal Attacks | 5 | 0/5/0 |
| 15-19 | Marksmanship | Efficiency | 5 | 0/10/0 |
| 20-22 | Marksmanship | Improved Stings | 3 | 0/13/0 |
| 23-24 | Marksmanship | Careful Aim | 2 | 0/15/0 |
| 25 | Marksmanship | Trueshot Aura | 1 | 0/16/0 |
| 26-30 | Beast Mastery | Deadly Aspects | 5 | 5/16/0 |
| 31-32 | Beast Mastery | Focused Fire | 2 | 7/16/0 |
| 33-35 | Beast Mastery | Endurance Training | 3 | 10/16/0 |
| 36-40 | Beast Mastery | Unleashed Fury | 5 | 15/16/0 |
| 41-45 | Beast Mastery | Ferocity | 5 | 20/16/0 |
| 46-47 | Beast Mastery | Bestial Discipline | 2 | 22/16/0 |
| 48 | Beast Mastery | Spirit Bond | 1 | 23/16/0 |
| 49 | Beast Mastery | Bestial Swiftness | 1 | 24/16/0 |
| 50-53 | Survival | Improved Tracking | 4 | 24/16/4 |
| 54 | Beast Mastery | Intimidation | 1 | 25/16/4 |
| 55-59 | Beast Mastery | Frenzy | 5 | 30/16/4 |
| 60 | Beast Mastery | Bestial Wrath | 1 | 31/16/4 |

## Core talents (priority order)

1. **Unleashed Fury** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Bestial Discipline** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Efficiency** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ferocity** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
5. **Lethal Attacks** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
6. **Frenzy** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
7. **Deadly Aspects** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Stings** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +4.3% faster than the hand draft bm-solo-farm, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 24.09; beast-mastery-leveling 24.59, bm-solo-farm 25.13. The search simulated 23,524 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast Mastery leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/5320001505011251-0053520001-4-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
