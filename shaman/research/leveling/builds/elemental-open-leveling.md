# Elemental — Leveling (open talent search) — 32/11/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/11/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental leveling build the open leveling search found on 2026-11-16: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). 

## Point allocation

### Elemental (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%. |
| **Concussion** | 3/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 3%. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage. |
| **Elemental Reach** | 2/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 6 yards. |
| **Call of Thunder** | 1/1 | changed | Increases critical strike chance of Lightning Bolt and Chain Lightning by 5%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Enhancement (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Improved Lightning Shield** | 2/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 10%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Restoration | Tidal Focus | 5 | 0/0/5 |
| 15-17 | Restoration | Mindfulness | 3 | 0/0/8 |
| 18-22 | Enhancement | Thundering Strikes | 5 | 0/5/8 |
| 23-25 | Enhancement | Mental Dexterity | 3 | 0/8/8 |
| 26-27 | Enhancement | Improved Lightning Shield | 2 | 0/10/8 |
| 28 | Enhancement | Shamanistic Focus | 1 | 0/11/8 |
| 29-33 | Elemental | Convection | 5 | 5/11/8 |
| 34-36 | Elemental | Elemental Alacrity | 3 | 8/11/8 |
| 37-38 | Elemental | Call of Flame | 2 | 10/11/8 |
| 39 | Elemental | Elemental Focus | 1 | 11/11/8 |
| 40 | Elemental | Call of Flame | 1 | 12/11/8 |
| 41-43 | Elemental | Concussion | 3 | 15/11/8 |
| 44 | Elemental | Reverberation | 1 | 16/11/8 |
| 45-47 | Elemental | Eye of the Storm | 3 | 19/11/8 |
| 48 | Elemental | Reverberation | 1 | 20/11/8 |
| 49-51 | Elemental | Lightning Overload | 3 | 23/11/8 |
| 52 | Elemental | Call of Thunder | 1 | 24/11/8 |
| 53 | Elemental | Reverberation | 1 | 25/11/8 |
| 54-58 | Elemental | Elemental Fury | 5 | 30/11/8 |
| 59-60 | Elemental | Elemental Reach | 2 | 32/11/8 |

## Core talents (priority order)

1. **Shamanistic Focus** — +3.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Elemental Alacrity** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Lightning Overload** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Convection** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Tidal Focus** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Elemental Fury** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Thundering Strikes** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Mindfulness** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-16: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Reverberation to Elemental Reach at 59 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Concussion to Reverberation at 44 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 28.54; . The search simulated 26,225 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Elemental leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/540333100301135-05003201-053-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
