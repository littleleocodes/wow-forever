# Beast-Survival — Leveling (open talent search) — 23/3/25

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 23/3/25 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) leveling build the open leveling search found on 2026-10-12: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +7.8% faster per kill than opt-melee-dps-solo-60, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 2/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 4% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 4% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 1/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 3/5 | **NEW** | Increases your critical strike chance with all attacks by 3%. |

### Survival (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 2/5 | unchanged | Increases your Parry chance by 2%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 1/5 | changed | Increases your total Health by 2%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 4/5 | **NEW** | Increases your melee ability critical strike damage by 24% and your Off Hand weapon damage by 40%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-18 | Survival | Deflection | 2 | 0/0/9 |
| 19 | Survival | Survivalist | 1 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23-24 | Survival | Clever Traps | 2 | 0/0/15 |
| 25-28 | Survival | Predator's Edge | 4 | 0/0/19 |
| 29-31 | Marksmanship | Lethal Attacks | 3 | 0/3/19 |
| 32 | Survival | Survival Tactics | 1 | 0/3/20 |
| 33 | Survival | Strider Kick | 1 | 0/3/21 |
| 34-35 | Survival | Resourcefulness | 2 | 0/3/23 |
| 36-37 | Survival | Survivalist's Discipline | 2 | 0/3/25 |
| 38-39 | Beast Mastery | Deadly Aspects | 2 | 2/3/25 |
| 40-42 | Beast Mastery | Endurance Training | 3 | 5/3/25 |
| 43-44 | Beast Mastery | Focused Fire | 2 | 7/3/25 |
| 45-46 | Beast Mastery | Endurance Training | 2 | 9/3/25 |
| 47 | Beast Mastery | Improved Aspect of the Monkey | 1 | 10/3/25 |
| 48-52 | Beast Mastery | Unleashed Fury | 5 | 15/3/25 |
| 53-57 | Beast Mastery | Ferocity | 5 | 20/3/25 |
| 58-59 | Beast Mastery | Bestial Discipline | 2 | 22/3/25 |
| 60 | Beast Mastery | Spirit Bond | 1 | 23/3/25 |

## Core talents (priority order)

1. **Resourcefulness** — +4.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
3. **Strider Kick** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Unleashed Fury** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Clever Traps** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Bestial Discipline** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Tracking** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
8. **Ferocity** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.43; opt-melee-dps-solo-60 24.17, leveling-melee 24.18, opt-bm-leveling-leveling-aoe 27.98. The search simulated 76,540 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/25210005050102-003-5202102301402021-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
