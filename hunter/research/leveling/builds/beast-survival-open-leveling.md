# Beast-Survival — Leveling (open talent search) — 19/8/24

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/8/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) leveling build the open leveling search found on 2026-10-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +6.5% faster per kill than opt-melee-dps-solo-60, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 3/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 6% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 6% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 4/5 | changed | Increases the critical strike chance of your pets and hawks by 8%. |

### Marksmanship (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |

### Survival (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 3/5 | changed | Increases your Parry chance by 3%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 4/5 | **NEW** | Increases your melee critical strike damage by 24% and your Off Hand weapon damage by 40%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Marksmanship | Lethal Attacks | 5 | 0/5/0 |
| 15-17 | Marksmanship | Improved Stings | 3 | 0/8/0 |
| 18-22 | Survival | Improved Tracking | 5 | 0/8/5 |
| 23-24 | Survival | Savage Strikes | 2 | 0/8/7 |
| 25-27 | Survival | Deflection | 3 | 0/8/10 |
| 28-30 | Survival | Surefooted | 3 | 0/8/13 |
| 31-32 | Survival | Clever Traps | 2 | 0/8/15 |
| 33-36 | Survival | Predator's Edge | 4 | 0/8/19 |
| 37 | Survival | Survival Tactics | 1 | 0/8/20 |
| 38-39 | Survival | Resourcefulness | 2 | 0/8/22 |
| 40-41 | Survival | Survivalist's Discipline | 2 | 0/8/24 |
| 42-44 | Beast Mastery | Deadly Aspects | 3 | 3/8/24 |
| 45-46 | Beast Mastery | Endurance Training | 2 | 5/8/24 |
| 47-48 | Beast Mastery | Focused Fire | 2 | 7/8/24 |
| 49-51 | Beast Mastery | Endurance Training | 3 | 10/8/24 |
| 52-56 | Beast Mastery | Unleashed Fury | 5 | 15/8/24 |
| 57-60 | Beast Mastery | Ferocity | 4 | 19/8/24 |

## Core talents (priority order)

1. **Resourcefulness** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Unleashed Fury** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Clever Traps** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Tracking** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
6. **Ferocity** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Lethal Attacks** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Stings** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 24.64; opt-melee-dps-solo-60 26.24, leveling-melee 26.31, opt-bm-leveling-leveling-aoe 29.88. The search simulated 44,296 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/3520000504-0053-530200230140202-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
