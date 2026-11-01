# Elemental-Enhancement — Leveling (open talent search) — 21/22/8

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/22/8 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental-Enhancement (an Elemental/Enhancement hybrid) leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). +5.0% faster per kill than opt-elemental-dps-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Elemental Devastation** | 1/3 | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec. |
| **Reverberation** | 3/5 | changed | Reduces the cooldown of your Shock spells by 0.6 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Call of Flame** | 2/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 10%, as well as increases the duration of your Flame Shock spell by 6 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Trial by Fire** | 2/2 | **NEW** | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 70% chance to not lose casting time when you take damage. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 4/5 | changed | Increases your Intellect by 8%. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Elemental Weapons** | 2/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 13%, your Windfury Weapon effect by 27% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 10%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Anticipation** | 2/3 | changed | Increases your chance to dodge by an additional 4%. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Enhancement | Thundering Strikes | 5 | 0/5/0 |
| 15-18 | Enhancement | Ancestral Knowledge | 4 | 0/9/0 |
| 19 | Enhancement | Mental Dexterity | 1 | 0/10/0 |
| 20 | Enhancement | Shamanistic Focus | 1 | 0/11/0 |
| 21-22 | Enhancement | Anticipation | 2 | 0/13/0 |
| 23-24 | Enhancement | Mental Dexterity | 2 | 0/15/0 |
| 25-27 | Enhancement | Improved Lightning Shield | 3 | 0/18/0 |
| 28-29 | Enhancement | Elemental Weapons | 2 | 0/20/0 |
| 30-31 | Enhancement | Mental Quickness | 2 | 0/22/0 |
| 32-36 | Restoration | Tidal Focus | 5 | 0/22/5 |
| 37-39 | Restoration | Mindfulness | 3 | 0/22/8 |
| 40-44 | Elemental | Convection | 5 | 5/22/8 |
| 45-47 | Elemental | Elemental Alacrity | 3 | 8/22/8 |
| 48-49 | Elemental | Call of Flame | 2 | 10/22/8 |
| 50 | Elemental | Elemental Focus | 1 | 11/22/8 |
| 51 | Elemental | Elemental Devastation | 1 | 12/22/8 |
| 52-54 | Elemental | Reverberation | 3 | 15/22/8 |
| 55-57 | Elemental | Eye of the Storm | 3 | 18/22/8 |
| 58-59 | Elemental | Trial by Fire | 2 | 20/22/8 |
| 60 | Elemental | Lava Burst | 1 | 21/22/8 |

## Core talents (priority order)

1. **Shamanistic Focus** — +3.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mental Quickness** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Elemental Alacrity** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Convection** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Mindfulness** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Tidal Focus** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Elemental Focus** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Eye of the Storm** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 34.88; opt-elemental-dps-leveling-st 36.61. The search simulated 48,676 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Elemental-Enhancement leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/5013321023001-054030321200002-053-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
