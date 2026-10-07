# Fire — Leveling (open talent search) — 0/31/20

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/31/20 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Fire leveling build the open leveling search found on 2026-10-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the fire-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (fire-leveling). 

## Point allocation

### Arcane (0)

*No points.*

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 4/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.4 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Flamestrike** | 1/3 | unchanged | Increases the critical strike chance of your Flamestrike spell by 5%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Ward** | 1/2 | unchanged | Causes your Fire Ward to have a 10% chance to reflect Fire spells while active. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Frost Nova** | 2/2 | unchanged | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Piercing Ice** | 1/3 | unchanged | Increases the damage done by your Frost spells by 2%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Frost | Elemental Precision | 5 | 0/0/5 |
| 15-17 | Frost | Frostbite | 3 | 0/0/8 |
| 18-19 | Frost | Improved Frost Nova | 2 | 0/0/10 |
| 20 | Frost | Ice Lance | 1 | 0/0/11 |
| 21-24 | Fire | Improved Fireball | 4 | 0/4/11 |
| 25 | Fire | Incineration | 1 | 0/5/11 |
| 26-30 | Fire | Ignite | 5 | 0/10/11 |
| 31-33 | Fire | Burning Soul | 3 | 0/13/11 |
| 34 | Fire | Pyroblast | 1 | 0/14/11 |
| 35 | Fire | Incineration | 1 | 0/15/11 |
| 36-38 | Fire | Master of Elements | 3 | 0/18/11 |
| 39 | Fire | Incineration | 1 | 0/19/11 |
| 40 | Fire | Improved Flamestrike | 1 | 0/20/11 |
| 41 | Fire | Blast Wave | 1 | 0/21/11 |
| 42-44 | Fire | Critical Mass | 3 | 0/24/11 |
| 45 | Fire | Improved Fire Ward | 1 | 0/25/11 |
| 46-50 | Fire | Fire Power | 5 | 0/30/11 |
| 51 | Fire | Combustion | 1 | 0/31/11 |
| 52 | Frost | Piercing Ice | 1 | 0/31/12 |
| 53-55 | Frost | Ice Shards | 3 | 0/31/15 |
| 56-58 | Frost | Shatter | 3 | 0/31/18 |
| 59-60 | Frost | Ice Shards | 2 | 0/31/20 |

## Core talents (priority order)

1. **Ice Lance** — +9.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Shatter** — +3.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Frostbite** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ice Shards** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
5. **Combustion** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Master of Elements** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Ignite** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Frost Nova** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 34.64; . The search simulated 81,340 builds.
- The spec's other leveling builds on the pages: fire-leveling 35.81 s, opt-fire-leveling-leveling-st 36.86 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Fire leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/mage>
- <https://talentsforever.com/mage/60/-03450031101033151-00550231010003-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
