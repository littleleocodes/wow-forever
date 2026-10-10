# Shockadin — Leveling (open talent search) — 14/8/29

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/8/29 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) leveling build the open leveling search found on 2026-10-09: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +28.8% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 3/5 | unchanged | Increases your total Intellect by 6%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 2/5 | moved | Increases your armor value from items by 4%. |
| **Redoubt** | 3/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 12%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68, and increase your Attack Power by 1% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 60% of your Intellect. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Benediction | 5 | 0/0/5 |
| 15-16 | Retribution | Improved Judgement | 2 | 0/0/7 |
| 17-19 | Retribution | Conviction | 3 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-23 | Retribution | Sanctified Judgement | 3 | 0/0/14 |
| 24 | Retribution | Conviction | 1 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26 | Retribution | Conviction | 1 | 0/0/17 |
| 27 | Retribution | Vindication | 1 | 0/0/18 |
| 28-29 | Retribution | Deflection | 2 | 0/0/20 |
| 30-32 | Retribution | Two-Handed Weapon Specialization | 3 | 0/0/23 |
| 33-37 | Holy | Divine Strength | 5 | 5/0/23 |
| 38-40 | Holy | Improved Seals | 3 | 8/0/23 |
| 41-42 | Retribution | Vengeance | 2 | 8/0/25 |
| 43-45 | Retribution | Champion of the Light | 3 | 8/0/28 |
| 46 | Retribution | Vengeance | 1 | 8/0/29 |
| 47-48 | Holy | Divine Intellect | 2 | 10/0/29 |
| 49-51 | Holy | Reverence | 3 | 13/0/29 |
| 52-53 | Protection | Toughness | 2 | 13/2/29 |
| 54-56 | Protection | Redoubt | 3 | 13/5/29 |
| 57-59 | Protection | Precision | 3 | 13/8/29 |
| 60 | Holy | Divine Intellect | 1 | 14/8/29 |

## Core talents (priority order)

1. **Sanctified Judgement** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Seals** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Two-Handed Weapon Specialization** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Conviction** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Seal of Command** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Judgement** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Vengeance** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Sacred Arbiter** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 27.55; holy-leveling 35.48. The search simulated 58,847 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shockadin leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/53003003-233-252051310013303-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
