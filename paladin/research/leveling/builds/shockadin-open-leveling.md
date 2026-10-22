# Shockadin — Leveling (open talent search) — 13/9/29

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 13/9/29 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) leveling build the open leveling search found on 2026-10-19: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +32.1% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 2/5 | unchanged | Increases your total Intellect by 4%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |

### Protection (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Anticipation** | 1/5 | changed | Increases your Defense Skill by 4. |

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 30% of your Intellect. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Deflection | 5 | 0/0/5 |
| 15-19 | Retribution | Conviction | 5 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-23 | Retribution | Sanctified Judgement | 3 | 0/0/14 |
| 24 | Retribution | Improved Judgement | 1 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26-30 | Holy | Divine Strength | 5 | 5/0/16 |
| 31-33 | Holy | Improved Seals | 3 | 8/0/16 |
| 34 | Retribution | Improved Judgement | 1 | 8/0/17 |
| 35-37 | Retribution | Vindication | 3 | 8/0/20 |
| 38-40 | Retribution | Vengeance | 3 | 8/0/23 |
| 41-42 | Retribution | Two-Handed Weapon Specialization | 2 | 8/0/25 |
| 43-47 | Protection | Toughness | 5 | 8/5/25 |
| 48-50 | Protection | Precision | 3 | 8/8/25 |
| 51 | Retribution | Two-Handed Weapon Specialization | 1 | 8/8/26 |
| 52-54 | Retribution | Champion of the Light | 3 | 8/8/29 |
| 55-56 | Holy | Divine Intellect | 2 | 10/8/29 |
| 57-59 | Holy | Reverence | 3 | 13/8/29 |
| 60 | Protection | Anticipation | 1 | 13/9/29 |

## Core talents (priority order)

1. **Sanctified Judgement** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Conviction** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Seals** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Vengeance** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Judgement** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Sacred Arbiter** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Reverence** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 27.78; holy-leveling 36.71. The search simulated 52,653 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shockadin leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/52003003-50301-502053310013303-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
