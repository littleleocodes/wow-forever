# Frostfire — Leveling (open talent search) — 2/25/24

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/25/24 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the frostfire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +20.4% faster per kill than frostfire-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |

### Fire (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 1/3 | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |

### Frost (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 3/5 | changed | Reduces the casting time of your Frostbolt spell by 0.3 sec. |
| **Precision** | 2/3 | changed | Improves your chance to hit with all spells by 4%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
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
| 21-23 | Frost | Ice Shards | 3 | 0/0/14 |
| 24 | Frost | Frost Channeling | 1 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28-29 | Frost | Frost Channeling | 2 | 0/0/20 |
| 30-31 | Frost | Fingers of Frost | 2 | 0/0/22 |
| 32 | Frost | Improved Frost Nova | 1 | 0/0/23 |
| 33-34 | Arcane | Wand Specialization | 2 | 2/0/23 |
| 35-39 | Fire | Accelerant | 5 | 2/5/23 |
| 40-44 | Fire | Ignite | 5 | 2/10/23 |
| 45-47 | Fire | Burning Soul | 3 | 2/13/23 |
| 48-49 | Fire | Incineration | 2 | 2/15/23 |
| 50-52 | Fire | Master of Elements | 3 | 2/18/23 |
| 53-54 | Fire | Incineration | 2 | 2/20/23 |
| 55 | Frost | Improved Frost Nova | 1 | 2/20/24 |
| 56-58 | Fire | Critical Mass | 3 | 2/23/24 |
| 59 | Fire | Incineration | 1 | 2/24/24 |
| 60 | Fire | Impact | 1 | 2/25/24 |

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

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Arcane Resilience to Improved Frost Nova at 32 (tie-break: -0.2% seed 3, -0.3% seed 4, level-weighted time per kill); Fire Power to Impact at 60 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Blast Wave to Improved Frost Nova at 55 (tie-break: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill); Frost Warding to Improved Frostbolt at 13 (gate: -0.3% seed 3, -0.5% seed 4, level-weighted time per kill); Frost Warding to Improved Frostbolt at 12 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 36.40; frostfire-open-leveling 43.84. The search simulated 75,576 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/201-5550030000003311-2125300301003002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
