# Fire — Leveling (open talent search) — 1/32/18

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/32/18 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build the open leveling search found on 2026-11-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +1.6% faster per kill than fire-open-leveling, the fastest of our leveling builds in that race.

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
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
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
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frost Channeling** | 2/3 | moved | Reduces the mana cost of your Frost spells by 10% and reduces the threat caused by your Frost spells by 20%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Fire | Accelerant | 5 | 0/5/0 |
| 15-19 | Fire | Ignite | 5 | 0/10/0 |
| 20 | Fire | Pyroblast | 1 | 0/11/0 |
| 21-22 | Fire | Improved Fire Blast | 2 | 0/13/0 |
| 23-24 | Fire | Burning Soul | 2 | 0/15/0 |
| 25 | Fire | Heating Up | 1 | 0/16/0 |
| 26 | Fire | Burning Soul | 1 | 0/17/0 |
| 27-29 | Fire | Master of Elements | 3 | 0/20/0 |
| 30-32 | Fire | Critical Mass | 3 | 0/23/0 |
| 33-34 | Fire | Incineration | 2 | 0/25/0 |
| 35-37 | Fire | Fire Power | 3 | 0/28/0 |
| 38-39 | Fire | Incineration | 2 | 0/30/0 |
| 40 | Fire | Combustion | 1 | 0/31/0 |
| 41 | Fire | Incineration | 1 | 0/32/0 |
| 42-43 | Frost | Precision | 2 | 0/32/2 |
| 44-45 | Frost | Frost Warding | 2 | 0/32/4 |
| 46 | Frost | Precision | 1 | 0/32/5 |
| 47-48 | Frost | Improved Frost Nova | 2 | 0/32/7 |
| 49-51 | Frost | Ice Shards | 3 | 0/32/10 |
| 52 | Frost | Ice Lance | 1 | 0/32/11 |
| 53-54 | Frost | Frost Channeling | 2 | 0/32/13 |
| 55-56 | Frost | Ice Shards | 2 | 0/32/15 |
| 57-59 | Frost | Shatter | 3 | 0/32/18 |
| 60 | Arcane | Wand Specialization | 1 | 1/32/18 |

## Core talents (priority order)

1. **Shatter** — +2.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ice Lance** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ignite** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Heating Up** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Precision** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Pyroblast** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Master of Elements** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
8. **Combustion** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-20: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Fire Ward to Improved Fire Blast at 60 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Improved Scorch to Burning Soul at 45 (gate: -0.3% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.83; fire-open-leveling 33.34, fire-leveling 33.88, opt-fire-leveling-leveling-st 34.82. The search simulated 54,185 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/1-55500301200133031-2035020201003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
