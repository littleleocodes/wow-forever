# Beast-Survival — Leveling (open talent search) — 22/5/24

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/5/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) leveling build the open leveling search found on 2026-10-19: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +6.7% faster per kill than leveling-melee, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 3/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 2/5 | changed | Increases the damage done by your pets and hawks by 6%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Bestial Discipline** | 1/2 | changed | Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting. |

### Marksmanship (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |

### Survival (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 3/5 | unchanged | Increases your Parry chance by 3%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 4/5 | **NEW** | Increases your melee ability critical strike damage by 24% and your Off Hand weapon damage by 40%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-19 | Survival | Deflection | 3 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23-24 | Survival | Clever Traps | 2 | 0/0/15 |
| 25-28 | Survival | Predator's Edge | 4 | 0/0/19 |
| 29 | Survival | Survival Tactics | 1 | 0/0/20 |
| 30-31 | Survival | Resourcefulness | 2 | 0/0/22 |
| 32-33 | Survival | Survivalist's Discipline | 2 | 0/0/24 |
| 34-38 | Marksmanship | Lethal Attacks | 5 | 0/5/24 |
| 39-43 | Beast Mastery | Deadly Aspects | 5 | 5/5/24 |
| 44-45 | Beast Mastery | Focused Fire | 2 | 7/5/24 |
| 46-48 | Beast Mastery | Endurance Training | 3 | 10/5/24 |
| 49-50 | Beast Mastery | Unleashed Fury | 2 | 12/5/24 |
| 51-53 | Beast Mastery | Improved Aspect of the Monkey | 3 | 15/5/24 |
| 54-58 | Beast Mastery | Ferocity | 5 | 20/5/24 |
| 59 | Beast Mastery | Bestial Discipline | 1 | 21/5/24 |
| 60 | Beast Mastery | Spirit Bond | 1 | 22/5/24 |

## Core talents (priority order)

1. **Resourcefulness** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
3. **Clever Traps** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Lethal Attacks** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Ferocity** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Tracking** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
7. **Bestial Discipline** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
8. **Surefooted** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.11; leveling-melee 23.60, opt-bm-leveling-leveling-aoe 28.33. The search simulated 69,161 builds.
- The spec's other leveling builds on the pages: opt-melee-dps-leveling-st 23.28 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/53230002050101-005-530200230140202-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
