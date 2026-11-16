# Arcane-Frost — Leveling (open talent search) — 28/0/23

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/0/23 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane-Frost (an Arcane/Frost hybrid) leveling build the open leveling search found on 2026-11-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the barrage-frost-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Improved Channeling** | 4/5 | **NEW** | Gives your Arcane Missiles spell a 80% chance and your Arcane Blast and Arcane Wrath spells a 56% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Improved Counterspell** | 1/2 | changed | Your Counterspell also Silences the target for 2 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 4/5 | changed | Increases your Intellect by 8% and increases the critical strike damage bonus of your Arcane spells by 80%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 3/5 | changed | Reduces the casting time of your Frostbolt spell by 0.3 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 4/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 80%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Frost | Precision | 2 | 0/0/2 |
| 12-14 | Frost | Improved Frostbolt | 3 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Ice Shards | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25 | Frost | Shatter | 1 | 0/0/16 |
| 26 | Frost | Ice Shards | 1 | 0/0/17 |
| 27 | Frost | Arctic Reach | 1 | 0/0/18 |
| 28-29 | Frost | Shatter | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32-33 | Arcane | Wand Specialization | 2 | 2/0/22 |
| 34 | Arcane | Arcane Resilience | 1 | 3/0/22 |
| 35-36 | Arcane | Improved Channeling | 2 | 5/0/22 |
| 37-38 | Arcane | Missile Barrage | 2 | 7/0/22 |
| 39 | Frost | Arctic Reach | 1 | 7/0/23 |
| 40-41 | Arcane | Arcane Subtlety | 2 | 9/0/23 |
| 42-46 | Arcane | Arcane Concentration | 5 | 14/0/23 |
| 47 | Arcane | Improved Channeling | 1 | 15/0/23 |
| 48-50 | Arcane | Arcane Meditation | 3 | 18/0/23 |
| 51 | Arcane | Improved Channeling | 1 | 19/0/23 |
| 52 | Arcane | Improved Counterspell | 1 | 20/0/23 |
| 53 | Arcane | Presence of Mind | 1 | 21/0/23 |
| 54-57 | Arcane | Arcane Mind | 4 | 25/0/23 |
| 58-60 | Arcane | Arcane Instability | 3 | 28/0/23 |

## Core talents (priority order)

1. **Shatter** — +2.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Missile Barrage** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ice Shards** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Frostbite** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Fingers of Frost** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Frostbolt** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Ice Shards to Arctic Reach at 27 (gate: -0.5% seed 3, -0.4% seed 4, level-weighted time per kill); Improved Channeling to Improved Counterspell at 52 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 28.26; opt-frost-leveling-leveling-st 29.14. The search simulated 56,559 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane-Frost leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/25120520000030143--0325300301103002-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
