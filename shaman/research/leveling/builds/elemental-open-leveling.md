# Elemental — Leveling (open talent search) — 31/11/9

*[Shaman](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/11/9 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental leveling build the open leveling search found on 2026-10-07: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the elemental-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (elemental-dps). +2.0% faster per kill than opt-elemental-dps-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Elemental (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 3/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 3%. |
| **Reverberation** | 2/5 | changed | Reduces the cooldown of your Shock spells by 0.4 sec. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Devastation** | 1/3 | changed | Your offensive spell critical strikes will increase your chance to get a critical strike with melee attacks by 3% for 10 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Call of Thunder** | 1/1 | changed | Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 3%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 150 to 192 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |

### Enhancement (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Tidal Focus** | 1/5 | changed | Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Enhancement | Thundering Strikes | 5 | 0/5/0 |
| 15-16 | Enhancement | Improved Ghost Wolf | 2 | 0/7/0 |
| 17-19 | Enhancement | Improved Lightning Shield | 3 | 0/10/0 |
| 20 | Enhancement | Shamanistic Focus | 1 | 0/11/0 |
| 21-25 | Restoration | Totemic Focus | 5 | 0/11/5 |
| 26-28 | Restoration | Mindfulness | 3 | 0/11/8 |
| 29 | Restoration | Tidal Focus | 1 | 0/11/9 |
| 30-34 | Elemental | Convection | 5 | 5/11/9 |
| 35-37 | Elemental | Call of Flame | 3 | 8/11/9 |
| 38-39 | Elemental | Concussion | 2 | 10/11/9 |
| 40 | Elemental | Elemental Focus | 1 | 11/11/9 |
| 41-43 | Elemental | Elemental Alacrity | 3 | 14/11/9 |
| 44 | Elemental | Concussion | 1 | 15/11/9 |
| 45 | Elemental | Call of Thunder | 1 | 16/11/9 |
| 46-48 | Elemental | Eye of the Storm | 3 | 19/11/9 |
| 49 | Elemental | Reverberation | 1 | 20/11/9 |
| 50-52 | Elemental | Lightning Overload | 3 | 23/11/9 |
| 53 | Elemental | Reverberation | 1 | 24/11/9 |
| 54 | Elemental | Elemental Devastation | 1 | 25/11/9 |
| 55-59 | Elemental | Elemental Fury | 5 | 30/11/9 |
| 60 | Elemental | Lava Burst | 1 | 31/11/9 |

## Core talents (priority order)

1. **Shamanistic Focus** — +5.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Elemental Fury** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Mindfulness** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Convection** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Lava Burst** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
6. **Thundering Strikes** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
7. **Elemental Alacrity** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
8. **Elemental Focus** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 37.28; opt-elemental-dps-leveling-st 38.04. The search simulated 40,150 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Elemental leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/shaman/60/5302311303103051-050002301-05301-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
