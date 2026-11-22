# Beast-Marks — Leveling (open talent search) — 23/23/5

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 23/23/5 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Marks (a Beast Mastery/Marksmanship hybrid) leveling build the open leveling search found on 2026-11-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the bm-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (bm-leveling). 

## Point allocation

### Beast Mastery (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Revive Pet** | 1/2 | unchanged | Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Mortal Shots** | 1/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 6%. |
| **Rapid Recuperation** | 1/2 | **NEW** | Afflicting a target with Serpent Sting allows 25% of your Mana Regeneration to continue while casting for 15 sec, increased to 50% when Rapid Killing is consumed. |

### Survival (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Marksmanship | Lethal Attacks | 5 | 0/5/0 |
| 15-19 | Marksmanship | Efficiency | 5 | 0/10/0 |
| 20-22 | Marksmanship | Improved Stings | 3 | 0/13/0 |
| 23-24 | Marksmanship | Careful Aim | 2 | 0/15/0 |
| 25 | Marksmanship | Trueshot Aura | 1 | 0/16/0 |
| 26 | Marksmanship | Careful Aim | 1 | 0/17/0 |
| 27 | Marksmanship | Rapid Killing | 1 | 0/18/0 |
| 28 | Marksmanship | Careful Aim | 1 | 0/19/0 |
| 29 | Marksmanship | Rapid Killing | 1 | 0/20/0 |
| 30 | Marksmanship | Rapid Recuperation | 1 | 0/21/0 |
| 31 | Survival | Improved Tracking | 1 | 0/21/1 |
| 32 | Marksmanship | Careful Aim | 1 | 0/22/1 |
| 33-35 | Survival | Improved Tracking | 3 | 0/22/4 |
| 36-40 | Beast Mastery | Deadly Aspects | 5 | 5/22/4 |
| 41-42 | Beast Mastery | Focused Fire | 2 | 7/22/4 |
| 43-44 | Beast Mastery | Endurance Training | 2 | 9/22/4 |
| 45 | Beast Mastery | Improved Revive Pet | 1 | 10/22/4 |
| 46-50 | Beast Mastery | Unleashed Fury | 5 | 15/22/4 |
| 51-55 | Beast Mastery | Ferocity | 5 | 20/22/4 |
| 56-57 | Beast Mastery | Bestial Discipline | 2 | 22/22/4 |
| 58 | Marksmanship | Mortal Shots | 1 | 22/23/4 |
| 59 | Beast Mastery | Spirit Bond | 1 | 23/23/4 |
| 60 | Survival | Improved Tracking | 1 | 23/23/5 |

## Core talents (priority order)

1. **Unleashed Fury** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Efficiency** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Lethal Attacks** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ferocity** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Stings** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Trueshot Aura** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Tracking** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).
8. **Deadly Aspects** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-22: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Bestial Swiftness to Bestial Discipline at 56 (tie-break: -0.0% seed 3, -0.1% seed 4, level-weighted time per kill).
- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Rapid Recuperation to Barrage at 31 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Pathfinding to Bestial Swiftness at 56 (no loss: +0.0% seed 3, +0.0% seed 4, level-weighted time per kill); Spirit Bond to Hawk Eye at 60 (no loss: -0.0% seed 3, +0.1% seed 4, level-weighted time per kill); Barrage to Improved Tracking at 31 (tie-break: -0.1% seed 3, -0.2% seed 4, level-weighted time per kill); Hawk Eye to Improved Tracking at 60 (tie-break: -0.0% seed 3, -0.1% seed 4, level-weighted time per kill); Bestial Discipline to Mortal Shots at 58 (no loss: -0.0% seed 3, +0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.09; beast-mastery-leveling 22.18, bm-solo-farm 23.15. The search simulated 35,601 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Marks leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/52201015050101-005355200111-5-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
