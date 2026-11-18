# Fire — Leveling (open talent search) — 1/31/19

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/31/19 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build the open leveling search found on 2026-11-17: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +1.1% faster per kill than fire-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards. |
| **Improved Scorch** | 1/3 | changed | Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Fire | Accelerant | 5 | 0/5/0 |
| 15-19 | Fire | Ignite | 5 | 0/10/0 |
| 20 | Fire | Pyroblast | 1 | 0/11/0 |
| 21-22 | Frost | Precision | 2 | 0/11/2 |
| 23-24 | Frost | Frost Warding | 2 | 0/11/4 |
| 25 | Frost | Precision | 1 | 0/11/5 |
| 26-27 | Frost | Improved Frost Nova | 2 | 0/11/7 |
| 28-30 | Frost | Ice Shards | 3 | 0/11/10 |
| 31 | Frost | Ice Lance | 1 | 0/11/11 |
| 32-34 | Frost | Frost Channeling | 3 | 0/11/14 |
| 35 | Frost | Ice Shards | 1 | 0/11/15 |
| 36-38 | Frost | Shatter | 3 | 0/11/18 |
| 39 | Frost | Ice Shards | 1 | 0/11/19 |
| 40 | Arcane | Wand Specialization | 1 | 1/11/19 |
| 41 | Fire | Improved Fire Blast | 1 | 1/12/19 |
| 42-43 | Fire | Burning Soul | 2 | 1/14/19 |
| 44 | Fire | Incineration | 1 | 1/15/19 |
| 45 | Fire | Heating Up | 1 | 1/16/19 |
| 46 | Fire | Improved Scorch | 1 | 1/17/19 |
| 47-49 | Fire | Master of Elements | 3 | 1/20/19 |
| 50-52 | Fire | Critical Mass | 3 | 1/23/19 |
| 53-54 | Fire | Incineration | 2 | 1/25/19 |
| 55-57 | Fire | Fire Power | 3 | 1/28/19 |
| 58-59 | Fire | Incineration | 2 | 1/30/19 |
| 60 | Fire | Combustion | 1 | 1/31/19 |

## Core talents (priority order)

1. **Ice Lance** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +2.8 s per kill at level 60 without it (removal, 3,000 fights).
3. **Heating Up** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ignite** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Precision** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Master of Elements** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Frost Nova** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Critical Mass** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 33.62; fire-open-leveling 33.99, fire-leveling 34.14, opt-fire-leveling-leveling-st 36.11. The search simulated 54,185 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/1-55500201110133031-2035020301003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
