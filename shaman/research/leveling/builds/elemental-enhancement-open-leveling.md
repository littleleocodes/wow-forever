# Elemental-Enhancement — Leveling (open talent search) — 22/22/7

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/22/7 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement (an Elemental/Enhancement hybrid) leveling build the open leveling search found on 2026-10-10: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). -0.3% faster per kill than elemental-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Reverberation** | 2/5 | changed | Reduces the cooldown of your Shock spells by 0.4 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Devastation** | 1/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 3% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Call of Thunder** | 1/1 | changed | Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 3%. |
| **Lightning Overload** | 1/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 3% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Toughness** | 2/5 | changed | Increases your Stamina by 4%. |
| **Flurry** | 1/5 | changed | Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Mindfulness** | 2/3 | **NEW** | Allows 33% of your Mana regeneration to continue while casting. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Elemental | Convection | 5 | 5/0/0 |
| 15-17 | Elemental | Call of Flame | 3 | 8/0/0 |
| 18-19 | Elemental | Concussion | 2 | 10/0/0 |
| 20 | Elemental | Elemental Focus | 1 | 11/0/0 |
| 21-23 | Elemental | Elemental Alacrity | 3 | 14/0/0 |
| 24-28 | Enhancement | Thundering Strikes | 5 | 14/5/0 |
| 29-30 | Enhancement | Ancestral Knowledge | 2 | 14/7/0 |
| 31 | Restoration | Totemic Focus | 1 | 14/7/1 |
| 32-34 | Enhancement | Ancestral Knowledge | 3 | 14/10/1 |
| 35 | Enhancement | Shamanistic Focus | 1 | 14/11/1 |
| 36-38 | Elemental | Concussion | 3 | 17/11/1 |
| 39-41 | Enhancement | Mental Dexterity | 3 | 17/14/1 |
| 42 | Enhancement | Improved Lightning Shield | 1 | 17/15/1 |
| 43-44 | Enhancement | Toughness | 2 | 17/17/1 |
| 45-46 | Enhancement | Improved Lightning Shield | 2 | 17/19/1 |
| 47 | Enhancement | Flurry | 1 | 17/20/1 |
| 48-49 | Enhancement | Mental Quickness | 2 | 17/22/1 |
| 50-53 | Restoration | Totemic Focus | 4 | 17/22/5 |
| 54-55 | Restoration | Mindfulness | 2 | 17/22/7 |
| 56 | Elemental | Call of Thunder | 1 | 18/22/7 |
| 57-58 | Elemental | Reverberation | 2 | 20/22/7 |
| 59 | Elemental | Lightning Overload | 1 | 21/22/7 |
| 60 | Elemental | Elemental Devastation | 1 | 22/22/7 |

## Core talents (priority order)

1. **Shamanistic Focus** — +5.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mental Quickness** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Elemental Alacrity** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Thundering Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Convection** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Mindfulness** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Elemental Focus** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Call of Flame** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 38.16; elemental-open-leveling 38.04, opt-elemental-dps-leveling-st 39.20. The search simulated 30,700 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Elemental-Enhancement leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/5502311300101-055030301021002-052-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
