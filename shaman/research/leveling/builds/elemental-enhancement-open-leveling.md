# Elemental-Enhancement — Leveling (open talent search) — 26/22/3

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 26/22/3 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement (an Elemental/Enhancement hybrid) leveling build the open leveling search found on 2026-11-03: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). +0.3% faster per kill than elemental-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, and Chain Lightning spells by 10%. |
| **Concussion** | 2/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 2%. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt and Chain Lightning spells by 0.50 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, and Fire Nova spells by 3 yards. |
| **Call of Thunder** | 1/1 | changed | Increases critical strike chance of Lightning Bolt and Chain Lightning by 5%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 30% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 1/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 4/5 | changed | Increases your Intellect by 8%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 150% of your Intellect. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Toughness** | 4/5 | changed | Increases your Stamina by 8%. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 3/5 | changed | Reduces the Mana cost of your healing spells by 3% and improves your chance to hit by 3%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Elemental | Convection | 5 | 5/0/0 |
| 15-17 | Elemental | Elemental Alacrity | 3 | 8/0/0 |
| 18-19 | Elemental | Call of Flame | 2 | 10/0/0 |
| 20 | Elemental | Elemental Focus | 1 | 11/0/0 |
| 21-23 | Restoration | Tidal Focus | 3 | 11/0/3 |
| 24 | Elemental | Call of Flame | 1 | 12/0/3 |
| 25-29 | Enhancement | Thundering Strikes | 5 | 12/5/3 |
| 30 | Enhancement | Mental Dexterity | 1 | 12/6/3 |
| 31-34 | Enhancement | Ancestral Knowledge | 4 | 12/10/3 |
| 35 | Enhancement | Shamanistic Focus | 1 | 12/11/3 |
| 36-37 | Elemental | Concussion | 2 | 14/11/3 |
| 38 | Elemental | Reverberation | 1 | 15/11/3 |
| 39-41 | Elemental | Eye of the Storm | 3 | 18/11/3 |
| 42-43 | Elemental | Reverberation | 2 | 20/11/3 |
| 44 | Elemental | Call of Thunder | 1 | 21/11/3 |
| 45-47 | Elemental | Lightning Overload | 3 | 24/11/3 |
| 48-49 | Enhancement | Mental Dexterity | 2 | 24/13/3 |
| 50-51 | Enhancement | Improved Lightning Shield | 2 | 24/15/3 |
| 52-55 | Enhancement | Toughness | 4 | 24/19/3 |
| 56 | Enhancement | Improved Lightning Shield | 1 | 24/20/3 |
| 57-58 | Enhancement | Mental Quickness | 2 | 24/22/3 |
| 59 | Elemental | Elemental Reach | 1 | 25/22/3 |
| 60 | Elemental | Elemental Fury | 1 | 26/22/3 |

## Core talents (priority order)

1. **Shamanistic Focus** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mental Quickness** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Lightning Overload** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Elemental Alacrity** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Convection** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Elemental Focus** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Eye of the Storm** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Reverberation** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 29.48; elemental-open-leveling 29.57. The search simulated 47,381 builds.
- The spec's other leveling builds on the pages: opt-elemental-dps-leveling-st 30.08 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Elemental-Enhancement leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/520333100301131-054033010400002-03-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
