# Arcane — Leveling (derived) — 30/0/21

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Arcane build, 30+ points kept in Arcane, playing the arcane-leveling rotation; the talent order is the stats model's (frost-leveling).

## Point allocation

### Arcane (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 3/5 | changed | Improves your chance to hit with Arcane spells by 3%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 1/2 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Shielding** | 1/2 | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |

### Fire (0)

*No points.*

### Frost (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 2/3 | unchanged | Increases the damage done by your Frost spells by 4%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 1/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1 spell cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Improved Frostbolt | 5 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-22 | Frost | Piercing Ice | 2 | 0/0/13 |
| 23-24 | Frost | Ice Shards | 2 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26 | Frost | Ice Shards | 1 | 0/0/17 |
| 27 | Frost | Ice Block | 1 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30 | Frost | Fingers of Frost | 1 | 0/0/21 |
| 31-32 | Arcane | Wand Specialization | 2 | 2/0/21 |
| 33-35 | Arcane | Arcane Focus | 3 | 5/0/21 |
| 36-40 | Arcane | Arcane Concentration | 5 | 10/0/21 |
| 41-42 | Arcane | Arcane Subtlety | 2 | 12/0/21 |
| 43 | Arcane | Magic Absorption | 1 | 13/0/21 |
| 44 | Arcane | Arcane Resilience | 1 | 14/0/21 |
| 45 | Arcane | Arcane Impact | 1 | 15/0/21 |
| 46-48 | Arcane | Arcane Meditation | 3 | 18/0/21 |
| 49 | Arcane | Arcane Shielding | 1 | 19/0/21 |
| 50 | Arcane | Arcane Impact | 1 | 20/0/21 |
| 51 | Arcane | Presence of Mind | 1 | 21/0/21 |
| 52-55 | Arcane | Arcane Mind | 4 | 25/0/21 |
| 56-58 | Arcane | Arcane Instability | 3 | 28/0/21 |
| 59 | Arcane | Arcane Mind | 1 | 29/0/21 |
| 60 | Arcane | Arcane Impact | 1 | 30/0/21 |

## Core talents (priority order)

1. **Ice Lance** — The scorer's value in this build: +21.2% of its score (model frost-leveling).
2. **Shatter** — The scorer's value in this build: +12.5% of its score (model frost-leveling).
3. **Ice Shards** — The scorer's value in this build: +8.5% of its score (model frost-leveling).
4. **Frostbite** — The scorer's value in this build: +6.4% of its score (model frost-leveling).
5. **Improved Frostbolt** — The scorer's value in this build: +3.1% of its score (model frost-leveling).
6. **Fingers of Frost** — The scorer's value in this build: +2.7% of its score (model frost-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start arcane-leveling, moves: 2 points Improved Counterspell -> Arcane Impact; 1 point Magic Absorption -> Arcane Impact. Race against arcane-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.3% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- A derived Arcane leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
