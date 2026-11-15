# Fire — Leveling (open talent search) — 1/32/18

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/32/18 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build the open leveling search found on 2026-11-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +0.6% faster per kill than fire-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Scorch** | 1/3 | changed | Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 2/3 | moved | Gives your Chill effects a 10% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
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
| 28-29 | Frost | Frostbite | 2 | 0/11/9 |
| 30 | Frost | Ice Shards | 1 | 0/11/10 |
| 31 | Frost | Ice Lance | 1 | 0/11/11 |
| 32-35 | Frost | Ice Shards | 4 | 0/11/15 |
| 36-38 | Frost | Shatter | 3 | 0/11/18 |
| 39 | Arcane | Wand Specialization | 1 | 1/11/18 |
| 40-41 | Fire | Improved Fire Blast | 2 | 1/13/18 |
| 42-43 | Fire | Burning Soul | 2 | 1/15/18 |
| 44 | Fire | Heating Up | 1 | 1/16/18 |
| 45 | Fire | Improved Scorch | 1 | 1/17/18 |
| 46-48 | Fire | Master of Elements | 3 | 1/20/18 |
| 49-51 | Fire | Critical Mass | 3 | 1/23/18 |
| 52-53 | Fire | Incineration | 2 | 1/25/18 |
| 54-56 | Fire | Fire Power | 3 | 1/28/18 |
| 57-58 | Fire | Incineration | 2 | 1/30/18 |
| 59 | Fire | Combustion | 1 | 1/31/18 |
| 60 | Fire | Incineration | 1 | 1/32/18 |

## Core talents (priority order)

1. **Ice Lance** — +4.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ignite** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Master of Elements** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Heating Up** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Combustion** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
8. **Critical Mass** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Frostbite to Ice Shards at 30 (gate: -0.2% seed 3, -0.3% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 36.35; fire-leveling 36.56, opt-fire-leveling-leveling-st 39.51. The search simulated 54,185 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/1-55500201210133031-2034320001003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
