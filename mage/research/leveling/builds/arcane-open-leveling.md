# Arcane — Leveling (open talent search) — 30/0/21

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane leveling build the open leveling search found on 2026-11-04: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the arcane-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (frost-leveling). 

## Point allocation

### Arcane (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (0)

*No points.*

### Frost (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 3/5 | changed | Reduces the casting time of your Frostbolt spell by 0.3 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 3/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 60%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 1/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 2 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Fingers of Frost** | 1/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1 spell cast as if the target were Frozen. Lasts 15 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10 | Arcane | Arcane Resilience | 1 | 1/0/0 |
| 11-14 | Arcane | Improved Channeling | 4 | 5/0/0 |
| 15-19 | Arcane | Arcane Concentration | 5 | 10/0/0 |
| 20-21 | Arcane | Missile Barrage | 2 | 12/0/0 |
| 22 | Arcane | Improved Channeling | 1 | 13/0/0 |
| 23 | Arcane | Arcane Impact | 1 | 14/0/0 |
| 24 | Arcane | Arcane Blast | 1 | 15/0/0 |
| 25 | Arcane | Arcane Wrath | 1 | 16/0/0 |
| 26-28 | Arcane | Arcane Meditation | 3 | 19/0/0 |
| 29 | Arcane | Arcane Impact | 1 | 20/0/0 |
| 30 | Arcane | Presence of Mind | 1 | 21/0/0 |
| 31 | Arcane | Arcane Impact | 1 | 22/0/0 |
| 32-34 | Arcane | Arcane Mind | 3 | 25/0/0 |
| 35-37 | Arcane | Arcane Instability | 3 | 28/0/0 |
| 38-39 | Arcane | Arcane Mind | 2 | 30/0/0 |
| 40-41 | Frost | Precision | 2 | 30/0/2 |
| 42-44 | Frost | Improved Frostbolt | 3 | 30/0/5 |
| 45-47 | Frost | Frostbite | 3 | 30/0/8 |
| 48-49 | Frost | Ice Shards | 2 | 30/0/10 |
| 50 | Frost | Ice Lance | 1 | 30/0/11 |
| 51 | Frost | Ice Shards | 1 | 30/0/12 |
| 52 | Frost | Improved Frost Nova | 1 | 30/0/13 |
| 53-54 | Frost | Frost Warding | 2 | 30/0/15 |
| 55-56 | Frost | Arctic Reach | 2 | 30/0/17 |
| 57-59 | Frost | Permafrost | 3 | 30/0/20 |
| 60 | Frost | Fingers of Frost | 1 | 30/0/21 |

## Core talents (priority order)

1. **Missile Barrage** — +4.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Channeling** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Arcane Blast** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Arcane Mind** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Arcane Instability** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Arcane Meditation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Arcane Concentration** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Precision** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.38; arcane-leveling 40.89. The search simulated 53,708 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Arcane leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/05100520310031153--2323313001200001-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
