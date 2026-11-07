# Survival — Leveling (open talent search) — 5/16/30

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/16/30 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +14.1% faster per kill than opt-bm-leveling-leveling-aoe, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 3/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 9%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Mortal Shots** | 1/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 6%. |

### Survival (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 1/5 | unchanged | Increases your Parry chance by 1%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 2/5 | changed | Increases your total Health by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 1/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17 | Survival | Deflection | 1 | 0/0/8 |
| 18-19 | Survival | Survivalist | 2 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23-24 | Survival | Clever Traps | 2 | 0/0/15 |
| 25-29 | Survival | Predator's Edge | 5 | 0/0/20 |
| 30 | Survival | Resourcefulness | 1 | 0/0/21 |
| 31 | Survival | Expose Prey | 1 | 0/0/22 |
| 32 | Survival | Resourcefulness | 1 | 0/0/23 |
| 33-34 | Survival | Survivalist's Discipline | 2 | 0/0/25 |
| 35-39 | Survival | Lightning Reflexes | 5 | 0/0/30 |
| 40-44 | Marksmanship | Lethal Attacks | 5 | 0/5/30 |
| 45-49 | Marksmanship | Careful Aim | 5 | 0/10/30 |
| 50-54 | Beast Mastery | Deadly Aspects | 5 | 5/10/30 |
| 55-57 | Marksmanship | Efficiency | 3 | 5/13/30 |
| 58-59 | Marksmanship | Rapid Killing | 2 | 5/15/30 |
| 60 | Marksmanship | Mortal Shots | 1 | 5/16/30 |

## Core talents (priority order)

1. **Resourcefulness** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Clever Traps** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Lethal Attacks** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Surefooted** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Tracking** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
7. **Careful Aim** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 21.57; opt-bm-leveling-leveling-aoe 24.61. The search simulated 43,753 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/5-00503520001-51022023005021205-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
