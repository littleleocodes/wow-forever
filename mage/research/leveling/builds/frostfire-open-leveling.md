# Frostfire — Leveling (open talent search) — 1/24/26

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 1/24/26 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). +11.4% faster per kill than fire-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arcane (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |

### Fire (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Ward** | 1/2 | unchanged | Causes your Fire Ward to have a 10% chance to reflect Fire spells while active. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |

### Frost (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 1/3 | unchanged | Increases the damage done by your Frost spells by 2%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 1/5 | changed | Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Elemental Precision | 5 | 0/0/5 |
| 15-16 | Frost | Frostbite | 2 | 0/0/7 |
| 17-18 | Frost | Improved Frost Nova | 2 | 0/0/9 |
| 19 | Frost | Frostbite | 1 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21 | Frost | Piercing Ice | 1 | 0/0/12 |
| 22-24 | Frost | Ice Shards | 3 | 0/0/15 |
| 25-27 | Frost | Shatter | 3 | 0/0/18 |
| 28-29 | Frost | Ice Shards | 2 | 0/0/20 |
| 30 | Frost | Fingers of Frost | 1 | 0/0/21 |
| 31-35 | Fire | Improved Fireball | 5 | 0/5/21 |
| 36 | Frost | Fingers of Frost | 1 | 0/5/22 |
| 37-41 | Fire | Ignite | 5 | 0/10/22 |
| 42-43 | Fire | Burning Soul | 2 | 0/12/22 |
| 44 | Fire | Pyroblast | 1 | 0/13/22 |
| 45-46 | Fire | Incineration | 2 | 0/15/22 |
| 47-49 | Fire | Master of Elements | 3 | 0/18/22 |
| 50 | Fire | Incineration | 1 | 0/19/22 |
| 51 | Fire | Improved Fire Ward | 1 | 0/20/22 |
| 52 | Fire | Blast Wave | 1 | 0/21/22 |
| 53-55 | Fire | Critical Mass | 3 | 0/24/22 |
| 56-58 | Frost | Frost Channeling | 3 | 0/24/25 |
| 59 | Frost | Winter's Chill | 1 | 0/24/26 |
| 60 | Arcane | Wand Specialization | 1 | 1/24/26 |

## Core talents (priority order)

1. **Ice Lance** — +12.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +4.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ice Shards** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Frostbite** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Fingers of Frost** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Master of Elements** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Elemental Precision** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Fireball** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.69; fire-leveling 36.41, opt-fire-leveling-leveling-st 37.39. The search simulated 76,919 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Frostfire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/1-035500201010331-005502313100030021-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
