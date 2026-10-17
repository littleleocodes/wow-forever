# Retribution — Leveling (open talent search) — 12/8/31

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/8/31 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the ret-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). 

## Point allocation

### Holy (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 1/5 | unchanged | Increases your total Intellect by 2%. |
| **Healing Light** | 1/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 4%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Unyielding Faith** | 1/2 | changed | Reduces the duration of Fear and Disorient effects on you by 15%. |
| **Reverence** | 1/3 | **NEW** | Allows 10% of your Mana regeneration to continue while casting. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68, and increase your Attack Power by 1% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 30% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1.0 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Benediction | 5 | 0/0/5 |
| 15-16 | Retribution | Holy Conduit | 2 | 0/0/7 |
| 17-18 | Retribution | Improved Judgement | 2 | 0/0/9 |
| 19 | Retribution | Conviction | 1 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-23 | Retribution | Sanctified Judgement | 3 | 0/0/14 |
| 24 | Retribution | Conviction | 1 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26-28 | Retribution | Conviction | 3 | 0/0/19 |
| 29 | Retribution | Vindication | 1 | 0/0/20 |
| 30-32 | Retribution | Two-Handed Weapon Specialization | 3 | 0/0/23 |
| 33-34 | Retribution | Vengeance | 2 | 0/0/25 |
| 35-36 | Retribution | Instrument of Law | 2 | 0/0/27 |
| 37-39 | Retribution | Champion of the Light | 3 | 0/0/30 |
| 40 | Retribution | Vengeance | 1 | 0/0/31 |
| 41-45 | Holy | Divine Strength | 5 | 5/0/31 |
| 46-48 | Holy | Improved Seals | 3 | 8/0/31 |
| 49-53 | Protection | Toughness | 5 | 8/5/31 |
| 54-56 | Protection | Precision | 3 | 8/8/31 |
| 57 | Holy | Divine Intellect | 1 | 9/8/31 |
| 58 | Holy | Unyielding Faith | 1 | 10/8/31 |
| 59 | Holy | Reverence | 1 | 11/8/31 |
| 60 | Holy | Healing Light | 1 | 12/8/31 |

## Core talents (priority order)

1. **Sanctified Judgement** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Seal of Command** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Two-Handed Weapon Specialization** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Conviction** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Seals** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Holy Conduit** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Judgement** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Instrument of Law** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +0.8% faster than the hand draft leveling-retribution, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 27.82; leveling-retribution 28.05, opt-ret-dps-solo-60 28.34, opt-ret-dps-leveling-st 28.41, opt-ret-dps-leveling-aoe 29.25. The search simulated 53,558 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Retribution leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/51103101-503-0522513100133032-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
