# Arcane-Frost — Leveling (open talent search) — 28/0/23

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/0/23 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the arcane-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). +7.8% faster per kill than arcane-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 3/5 | changed | Improves your chance to hit with Arcane spells by 3%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Geometry** | 2/2 | **NEW** | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Elemental Precision** | 3/5 | changed | Improves your chance to hit with Frost and Fire spells by 3%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 1/3 | unchanged | Increases the damage done by your Frost spells by 2%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Frost | Elemental Precision | 3 | 0/0/3 |
| 13-14 | Frost | Frost Warding | 2 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Piercing Ice | 1 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26-27 | Frost | Ice Shards | 2 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Frost | Ice Shards | 1 | 0/0/23 |
| 33-34 | Arcane | Wand Specialization | 2 | 2/0/23 |
| 35-37 | Arcane | Arcane Focus | 3 | 5/0/23 |
| 38-42 | Arcane | Arcane Concentration | 5 | 10/0/23 |
| 43-44 | Arcane | Arcane Geometry | 2 | 12/0/23 |
| 45-47 | Arcane | Arcane Impact | 3 | 15/0/23 |
| 48 | Arcane | Arcane Meditation | 1 | 16/0/23 |
| 49 | Arcane | Arcane Blast | 1 | 17/0/23 |
| 50 | Arcane | Missile Barrage | 1 | 18/0/23 |
| 51-52 | Arcane | Arcane Meditation | 2 | 20/0/23 |
| 53-57 | Arcane | Arcane Mind | 5 | 25/0/23 |
| 58-60 | Arcane | Arcane Instability | 3 | 28/0/23 |

## Core talents (priority order)

1. **Ice Lance** — +5.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Missile Barrage** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shatter** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Arcane Blast** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Ice Shards** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Fingers of Frost** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Frostbite** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Arcane Instability** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 31.39; arcane-leveling 33.84. The search simulated 65,338 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane-Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/23000502310031053--20350031310003002-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
