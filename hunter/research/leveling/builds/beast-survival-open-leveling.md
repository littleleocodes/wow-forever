# Beast-Survival — Leveling (open talent search) — 22/5/24

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/5/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) leveling build the open leveling search found on 2026-10-07: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +9.2% faster per kill than opt-melee-dps-solo-60, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 3/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 6% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 6% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 4/5 | changed | Increases the critical strike chance of your pets and hawks by 8%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

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
| **Predator's Edge** | 4/5 | **NEW** | Increases your melee critical strike damage by 24% and your Off Hand weapon damage by 40%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
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
| 32-36 | Marksmanship | Lethal Attacks | 5 | 0/5/22 |
| 37-38 | Survival | Survivalist's Discipline | 2 | 0/5/24 |
| 39-41 | Beast Mastery | Deadly Aspects | 3 | 3/5/24 |
| 42-43 | Beast Mastery | Endurance Training | 2 | 5/5/24 |
| 44-45 | Beast Mastery | Focused Fire | 2 | 7/5/24 |
| 46-48 | Beast Mastery | Endurance Training | 3 | 10/5/24 |
| 49-53 | Beast Mastery | Unleashed Fury | 5 | 15/5/24 |
| 54-57 | Beast Mastery | Ferocity | 4 | 19/5/24 |
| 58 | Beast Mastery | Summon Hawk | 1 | 20/5/24 |
| 59-60 | Beast Mastery | Bestial Discipline | 2 | 22/5/24 |

## Core talents (priority order)

1. **Survivalist's Discipline** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Resourcefulness** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Clever Traps** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Unleashed Fury** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Tracking** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Predator's Edge** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Lethal Attacks** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Bestial Discipline** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 24.02; opt-melee-dps-solo-60 26.24, leveling-melee 26.31, opt-bm-leveling-leveling-aoe 29.88. The search simulated 48,123 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/35200005041002-005-530200230140202-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
