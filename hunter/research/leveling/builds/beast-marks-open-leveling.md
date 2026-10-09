# Beast-Marks — Leveling (open talent search) — 29/18/4

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/18/4 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Marks (a Beast Mastery/Marksmanship hybrid) leveling build the open leveling search found on 2026-10-07: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the bm-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (bm-leveling). +1.9% faster per kill than beast-mastery-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |
| **Improved Revive Pet** | 1/2 | unchanged | Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 4/5 | unchanged | Gives your pet a 80% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Marksmanship (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |

### Survival (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 4/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 4%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Beast Mastery | Deadly Aspects | 5 | 5/0/0 |
| 15-16 | Beast Mastery | Focused Fire | 2 | 7/0/0 |
| 17-18 | Beast Mastery | Pathfinding | 2 | 9/0/0 |
| 19 | Beast Mastery | Endurance Training | 1 | 10/0/0 |
| 20-24 | Beast Mastery | Unleashed Fury | 5 | 15/0/0 |
| 25 | Beast Mastery | Summon Hawk | 1 | 16/0/0 |
| 26-29 | Beast Mastery | Ferocity | 4 | 20/0/0 |
| 30 | Beast Mastery | Bestial Discipline | 1 | 21/0/0 |
| 31 | Beast Mastery | Ferocity | 1 | 22/0/0 |
| 32 | Beast Mastery | Bestial Discipline | 1 | 23/0/0 |
| 33 | Beast Mastery | Spirit Bond | 1 | 24/0/0 |
| 34 | Beast Mastery | Improved Revive Pet | 1 | 25/0/0 |
| 35-38 | Beast Mastery | Frenzy | 4 | 29/0/0 |
| 39-43 | Marksmanship | Lethal Attacks | 5 | 29/5/0 |
| 44-48 | Marksmanship | Efficiency | 5 | 29/10/0 |
| 49-53 | Marksmanship | Careful Aim | 5 | 29/15/0 |
| 54-56 | Marksmanship | Improved Stings | 3 | 29/18/0 |
| 57-60 | Survival | Improved Tracking | 4 | 29/18/4 |

## Core talents (priority order)

1. **Summon Hawk** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Efficiency** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Unleashed Fury** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Bestial Discipline** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Ferocity** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Stings** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Careful Aim** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Tracking** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.09; beast-mastery-leveling 26.59. The search simulated 41,813 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Marks leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/512021050511024-005355-4-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
