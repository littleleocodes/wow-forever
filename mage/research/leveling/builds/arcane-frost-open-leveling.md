# Arcane-Frost — Leveling (open talent search) — 29/0/22

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/0/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) leveling build the open leveling search found on 2026-10-20: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the arcane-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). +14.9% faster per kill than arcane-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 2/5 | changed | Improves your chance to hit with Arcane spells by 2%. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 15% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 15 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 3/5 | changed | Increases your Intellect by 6% and increases the critical strike damage bonus of your Arcane spells by 60%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 1/3 | moved | Gives your Chill effects a 5% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 2/3 | unchanged | Increases the damage done by your Frost spells by 4%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Arcane | Missile Barrage | 2 | 2/0/0 |
| 12-13 | Arcane | Arcane Focus | 2 | 4/0/0 |
| 14 | Arcane | Improved Channeling | 1 | 5/0/0 |
| 15-19 | Arcane | Arcane Concentration | 5 | 10/0/0 |
| 20-23 | Arcane | Improved Channeling | 4 | 14/0/0 |
| 24 | Arcane | Arcane Blast | 1 | 15/0/0 |
| 25 | Arcane | Arcane Wrath | 1 | 16/0/0 |
| 26-28 | Arcane | Arcane Meditation | 3 | 19/0/0 |
| 29-31 | Arcane | Arcane Impact | 3 | 22/0/0 |
| 32 | Arcane | Presence of Mind | 1 | 23/0/0 |
| 33-34 | Arcane | Arcane Mind | 2 | 25/0/0 |
| 35-37 | Arcane | Arcane Instability | 3 | 28/0/0 |
| 38 | Arcane | Arcane Mind | 1 | 29/0/0 |
| 39-43 | Frost | Elemental Precision | 5 | 29/0/5 |
| 44 | Frost | Frostbite | 1 | 29/0/6 |
| 45-48 | Frost | Ice Shards | 4 | 29/0/10 |
| 49 | Frost | Ice Lance | 1 | 29/0/11 |
| 50-52 | Frost | Frost Channeling | 3 | 29/0/14 |
| 53 | Frost | Piercing Ice | 1 | 29/0/15 |
| 54 | Frost | Shatter | 1 | 29/0/16 |
| 55 | Frost | Ice Shards | 1 | 29/0/17 |
| 56 | Frost | Piercing Ice | 1 | 29/0/18 |
| 57-58 | Frost | Shatter | 2 | 29/0/20 |
| 59-60 | Frost | Fingers of Frost | 2 | 29/0/22 |

## Core talents (priority order)

1. **Missile Barrage** — +3.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shatter** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Arcane Blast** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Arcane Meditation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Channeling** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Fingers of Frost** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Arcane Concentration** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 31.29; arcane-leveling 35.94. The search simulated 63,363 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane-Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/025200500310031133--00550012310003002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
