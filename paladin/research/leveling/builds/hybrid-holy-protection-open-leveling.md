# Holy/Protection hybrid — Leveling (open talent search) — 21/16/14

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/16/14 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy/Protection hybrid (a Holy/Protection hybrid) leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +2.7% faster per kill than holy-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 4/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 80% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 1/2 | **NEW** | Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Redoubt** | 1/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Improved Hammer of Justice** | 1/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 5 sec. |
| **Toughness** | 3/5 | moved | Increases your armor value from items by 6%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |

### Retribution (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Benediction** | 3/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Retribution | Benediction | 3 | 0/0/3 |
| 13-14 | Retribution | Deflection | 2 | 0/0/5 |
| 15-17 | Retribution | Sanctified Judgement | 3 | 0/0/8 |
| 18-19 | Retribution | Conviction | 2 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21 | Retribution | Conviction | 1 | 0/0/12 |
| 22-26 | Holy | Divine Strength | 5 | 5/0/12 |
| 27-29 | Holy | Improved Seals | 3 | 8/0/12 |
| 30-31 | Retribution | Improved Judgement | 2 | 8/0/14 |
| 32-36 | Protection | Divine Intellect | 5 | 8/5/14 |
| 37-39 | Protection | Precision | 3 | 8/8/14 |
| 40 | Protection | Redoubt | 1 | 8/9/14 |
| 41 | Protection | Guardian's Favor | 1 | 8/10/14 |
| 42 | Protection | Templar's Bulwark | 1 | 8/11/14 |
| 43 | Protection | Improved Hammer of Justice | 1 | 8/12/14 |
| 44-46 | Protection | Toughness | 3 | 8/15/14 |
| 47 | Protection | Swift Judgement | 1 | 8/16/14 |
| 48-49 | Holy | Reverence | 2 | 10/16/14 |
| 50-51 | Holy | Holy Conduit | 2 | 12/16/14 |
| 52-54 | Holy | Illumination | 3 | 15/16/14 |
| 55 | Holy | Divine Precision | 1 | 16/16/14 |
| 56 | Holy | Illumination | 1 | 17/16/14 |
| 57-58 | Holy | Improved Seals | 2 | 19/16/14 |
| 59 | Holy | Divine Favor | 1 | 20/16/14 |
| 60 | Holy | Holy Shock | 1 | 21/16/14 |

## Core talents (priority order)

1. **Sanctified Judgement** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Swift Judgement** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Seals** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Conviction** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Holy Conduit** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Judgement** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Seal of Command** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 29.47; holy-open-leveling 30.28, holy-leveling 34.88. The search simulated 31,494 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Holy/Protection hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/05025014210001-5131011031-23233001-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
