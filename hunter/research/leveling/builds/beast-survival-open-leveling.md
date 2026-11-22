# Beast-Survival — Leveling (open talent search) — 22/4/25

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/4/25 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) leveling build the open leveling search found on 2026-11-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the melee-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (melee-dps). +0.3% faster per kill than survival-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 4/5 | **NEW** | Increases your critical strike chance with all attacks by 4%. |

### Survival (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 1/5 | unchanged | Increases your Parry chance by 1%. |
| **Entrapment** | 2/5 | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 2 sec. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-18 | Survival | Entrapment | 2 | 0/0/9 |
| 19 | Survival | Deflection | 1 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23-24 | Survival | Clever Traps | 2 | 0/0/15 |
| 25-28 | Survival | Predator's Edge | 4 | 0/0/19 |
| 29 | Survival | Survival Tactics | 1 | 0/0/20 |
| 30 | Survival | Resourcefulness | 1 | 0/0/21 |
| 31 | Marksmanship | Lethal Attacks | 1 | 0/1/21 |
| 32 | Survival | Resourcefulness | 1 | 0/1/22 |
| 33-34 | Survival | Survivalist's Discipline | 2 | 0/1/24 |
| 35-37 | Marksmanship | Lethal Attacks | 3 | 0/4/24 |
| 38-42 | Beast Mastery | Deadly Aspects | 5 | 5/4/24 |
| 43-44 | Beast Mastery | Focused Fire | 2 | 7/4/24 |
| 45-47 | Beast Mastery | Endurance Training | 3 | 10/4/24 |
| 48-52 | Beast Mastery | Unleashed Fury | 5 | 15/4/24 |
| 53-57 | Beast Mastery | Ferocity | 5 | 20/4/24 |
| 58-59 | Beast Mastery | Bestial Discipline | 2 | 22/4/24 |
| 60 | Survival | Predator's Edge | 1 | 22/4/25 |

## Core talents (priority order)

1. **Resourcefulness** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Survivalist's Discipline** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Bestial Discipline** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Unleashed Fury** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Clever Traps** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Tracking** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Ferocity** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Surefooted** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-22: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Survivalist to Entrapment at 18 (gate that did nothing, no loss: +0.0% seed 3, +0.0% seed 4, level-weighted time per kill); Survivalist to Entrapment at 17 (gate that did nothing, no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill).
- 2026-11-21: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Entrapment to Deflection at 19 (gate that did nothing, no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill).
- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Expose Prey to Lethal Attacks at 31 (measured: -0.4% seed 3, -0.4% seed 4, level-weighted time per kill); Spirit Bond to Predator's Edge at 60 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- +5.6% faster than the hand draft leveling-melee, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 21.09; survival-open-leveling 21.15, opt-bm-leveling-leveling-aoe 24.58. The search simulated 60,489 builds.
- The spec's other leveling builds on the pages: opt-melee-dps-leveling-st 22.17 s, leveling-melee 22.28 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast-Survival leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/53200005050102-003-501220230140212-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
