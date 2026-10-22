# Frostfire — Leveling (open talent search) — 0/26/25

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/26/25 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-10-20: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +1.8% faster per kill than fire-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (0)

*No points.*

### Fire (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |

### Frost (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 2/3 | moved | Gives your Chill effects a 10% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 1/3 | unchanged | Increases the damage done by your Frost spells by 2%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Elemental Precision | 5 | 0/0/5 |
| 15-16 | Frost | Frostbite | 2 | 0/0/7 |
| 17-18 | Frost | Improved Frost Nova | 2 | 0/0/9 |
| 19 | Frost | Ice Shards | 1 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21 | Frost | Piercing Ice | 1 | 0/0/12 |
| 22-24 | Frost | Ice Shards | 3 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28 | Frost | Ice Block | 1 | 0/0/19 |
| 29 | Frost | Ice Shards | 1 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-34 | Frost | Frost Channeling | 3 | 0/0/25 |
| 35-39 | Fire | Improved Fireball | 5 | 0/5/25 |
| 40-44 | Fire | Ignite | 5 | 0/10/25 |
| 45-47 | Fire | Burning Soul | 3 | 0/13/25 |
| 48 | Fire | Pyroblast | 1 | 0/14/25 |
| 49 | Fire | Incineration | 1 | 0/15/25 |
| 50 | Fire | Heating Up | 1 | 0/16/25 |
| 51-53 | Fire | Master of Elements | 3 | 0/19/25 |
| 54 | Fire | Incineration | 1 | 0/20/25 |
| 55-59 | Fire | Critical Mass | 5 | 0/25/25 |
| 60 | Fire | Incineration | 1 | 0/26/25 |

## Core talents (priority order)

1. **Ice Lance** — +6.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +3.8 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Elemental Precision** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Master of Elements** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Critical Mass** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Fingers of Frost** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Frost Nova** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 33.65; fire-open-leveling 34.25, fire-leveling 35.79, opt-fire-leveling-leveling-st 39.19. The search simulated 79,053 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/-03550030100135-00550221310013002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
