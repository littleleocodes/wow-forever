# Frostfire — Leveling (open talent search) — 3/26/22

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 3/26/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frostfire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +20.4% faster per kill than frostfire-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |

### Fire (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Fire Power** | 1/3 | unchanged | Increases the damage done by your Fire spells by 1% per your Fire effects on the target, up to a maximum increase of 4%. Effects which mix multiple schools of magic do not qualify. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 1/5 | changed | Reduces the casting time of your Frostbolt spell by 0.1 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Frost | Precision | 2 | 0/0/2 |
| 12-13 | Frost | Frost Warding | 2 | 0/0/4 |
| 14 | Frost | Improved Frostbolt | 1 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Ice Shards | 3 | 0/0/14 |
| 24 | Frost | Frost Channeling | 1 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28-29 | Frost | Frost Channeling | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Arcane | Arcane Resilience | 1 | 1/0/22 |
| 33-34 | Arcane | Wand Specialization | 2 | 3/0/22 |
| 35-39 | Fire | Accelerant | 5 | 3/5/22 |
| 40-44 | Fire | Ignite | 5 | 3/10/22 |
| 45-47 | Fire | Burning Soul | 3 | 3/13/22 |
| 48-49 | Fire | Incineration | 2 | 3/15/22 |
| 50-52 | Fire | Master of Elements | 3 | 3/18/22 |
| 53-54 | Fire | Incineration | 2 | 3/20/22 |
| 55 | Fire | Blast Wave | 1 | 3/21/22 |
| 56-58 | Fire | Critical Mass | 3 | 3/24/22 |
| 59 | Fire | Incineration | 1 | 3/25/22 |
| 60 | Fire | Fire Power | 1 | 3/26/22 |

## Core talents (priority order)

1. **Ice Lance** — +10.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +7.6 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Fingers of Frost** — +3.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frostbite** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Frost Channeling** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Accelerant** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Master of Elements** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 36.40; frostfire-open-leveling 43.84. The search simulated 75,576 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/201-5550030000003311-2125300301003002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
