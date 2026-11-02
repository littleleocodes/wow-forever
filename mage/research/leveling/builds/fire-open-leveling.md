# Fire — Leveling (open talent search) — 0/31/20

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/31/20 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +5.4% faster per kill than fire-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (0)

*No points.*

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 1/? | ? |  |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 1/2 | unchanged | Increases the range of your Fire spells by 3 yards. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Flamestrike** | 1/3 | unchanged | Increases the critical strike chance of your Flamestrike spell by 5%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 1/3 | changed | Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/3 | unchanged | Increases the critical strike chance of your Fire spells by 2%. *(rank 1 shown; rank 5 text not captured)* |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 1/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 15%, gives your Frost Ward a 10% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 10%. |
| **Improved Frostbolt** | 2/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.2 sec. |
| **Elemental Precision** | 3/? | ? |  |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Frost | Elemental Precision | 3 | 0/0/3 |
| 13 | Frost | Frost Warding | 1 | 0/0/4 |
| 14 | Frost | Improved Frostbolt | 1 | 0/0/5 |
| 15-16 | Frost | Improved Frost Nova | 2 | 0/0/7 |
| 17-19 | Frost | Ice Shards | 3 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-23 | Frost | Frost Channeling | 3 | 0/0/14 |
| 24 | Frost | Ice Shards | 1 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28 | Frost | Ice Shards | 1 | 0/0/19 |
| 29 | Frost | Improved Frostbolt | 1 | 0/0/20 |
| 30-31 | Fire | Improved Fire Blast | 2 | 0/2/20 |
| 32 | Fire | Improved Fireball | 1 | 0/3/20 |
| 33-34 | Fire | Incineration | 2 | 0/5/20 |
| 35 | Fire | Flame Throwing | 1 | 0/6/20 |
| 36-40 | Fire | Ignite | 5 | 0/11/20 |
| 41-43 | Fire | Burning Soul | 3 | 0/14/20 |
| 44 | Fire | Pyroblast | 1 | 0/15/20 |
| 45 | Fire | Heating Up | 1 | 0/16/20 |
| 46 | Fire | Improved Scorch | 1 | 0/17/20 |
| 47-49 | Fire | Master of Elements | 3 | 0/20/20 |
| 50-54 | Fire | Critical Mass | 5 | 0/25/20 |
| 55-57 | Fire | Fire Power | 3 | 0/28/20 |
| 58 | Fire | Incineration | 1 | 0/29/20 |
| 59 | Fire | Improved Flamestrike | 1 | 0/30/20 |
| 60 | Fire | Combustion | 1 | 0/31/20 |

## Core talents (priority order)

1. **Ice Lance** — +4.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +2.8 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
4. **Master of Elements** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Elemental Precision** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Ignite** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Critical Mass** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
8. **Combustion** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 34.21; fire-leveling 36.06, opt-fire-leveling-leveling-st 39.05. The search simulated 42,634 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/-23151031110135031-1235020301003-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
