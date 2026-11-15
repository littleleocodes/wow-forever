# Survival — Leveling (open talent search) — 3/17/31

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 3/17/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival leveling build the open leveling search found on 2026-11-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). 

## Point allocation

### Beast Mastery (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 2/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 4% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 4% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |

### Marksmanship (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 2/3 | **NEW** | Increases the damage of your Serpent Sting ability by 13%, reduces the cooldown of your Viper Sting ability by 4 sec, and increases the duration of your Scorpid Sting ability by 30 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 4/5 | **NEW** | Increases your Attack Power by 80% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 1/5 | unchanged | Increases your Parry chance by 1%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 2/5 | changed | Increases your total Health by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
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
| 31 | Survival | Survival Tactics | 1 | 0/0/22 |
| 32 | Survival | Resourcefulness | 1 | 0/0/23 |
| 33-34 | Survival | Survivalist's Discipline | 2 | 0/0/25 |
| 35-39 | Marksmanship | Lethal Attacks | 5 | 0/5/25 |
| 40-42 | Marksmanship | Careful Aim | 3 | 0/8/25 |
| 43-47 | Survival | Lightning Reflexes | 5 | 0/8/30 |
| 48-49 | Marksmanship | Improved Stings | 2 | 0/10/30 |
| 50-51 | Beast Mastery | Deadly Aspects | 2 | 2/10/30 |
| 52 | Beast Mastery | Endurance Training | 1 | 3/10/30 |
| 53 | Marksmanship | Efficiency | 1 | 3/11/30 |
| 54 | Survival | Strider Kick | 1 | 3/11/31 |
| 55-57 | Marksmanship | Efficiency | 3 | 3/14/31 |
| 58 | Marksmanship | Careful Aim | 1 | 3/15/31 |
| 59 | Marksmanship | Efficiency | 1 | 3/16/31 |
| 60 | Marksmanship | Trueshot Aura | 1 | 3/17/31 |

## Core talents (priority order)

1. **Resourcefulness** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
3. **Lethal Attacks** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Surefooted** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
5. **Efficiency** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Survival Tactics to Efficiency at 53 (tie-break: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill); Rapid Killing to Careful Aim at 58 (no loss: +0.0% seed 3, -0.0% seed 4, level-weighted time per kill); Improved Stings to Trueshot Aura at 60 (no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill); Deadly Aspects to Endurance Training at 52 (no loss: +0.1% seed 3, -0.0% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 21.12; opt-bm-leveling-leveling-aoe 24.58. The search simulated 43,753 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/3-0053431-51022023025020215-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
