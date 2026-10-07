# Prot-Ret — Leveling (open talent search) — 8/16/27

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 8/16/27 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Prot-Ret (a Protection/Retribution hybrid) leveling build the open leveling search found on 2026-10-07: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +29.0% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Redoubt** | 2/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 8%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Anticipation** | 1/5 | changed | Increases your Defense Skill by 4. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Sacred Duty** | 2/2 | **NEW** | Increases your total Stamina by 4% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |

### Retribution (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Benediction** | 3/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 2/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 133, and increase your Attack Power by 2% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 1/3 | **NEW** | Increases your spell damage by up to 20% of your Intellect. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Retribution | Benediction | 3 | 0/0/3 |
| 13-14 | Retribution | Deflection | 2 | 0/0/5 |
| 15-16 | Retribution | Improved Judgement | 2 | 0/0/7 |
| 17-19 | Retribution | Conviction | 3 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-23 | Retribution | Sanctified Judgement | 3 | 0/0/14 |
| 24 | Retribution | Conviction | 1 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26 | Retribution | Conviction | 1 | 0/0/17 |
| 27-28 | Retribution | Vindication | 2 | 0/0/19 |
| 29 | Retribution | Deflection | 1 | 0/0/20 |
| 30-32 | Retribution | Two-Handed Weapon Specialization | 3 | 0/0/23 |
| 33-37 | Holy | Divine Strength | 5 | 5/0/23 |
| 38-40 | Holy | Improved Seals | 3 | 8/0/23 |
| 41-42 | Retribution | Vengeance | 2 | 8/0/25 |
| 43 | Retribution | Champion of the Light | 1 | 8/0/26 |
| 44 | Retribution | Vengeance | 1 | 8/0/27 |
| 45-49 | Protection | Toughness | 5 | 8/5/27 |
| 50-52 | Protection | Precision | 3 | 8/8/27 |
| 53 | Protection | Anticipation | 1 | 8/9/27 |
| 54 | Protection | Redoubt | 1 | 8/10/27 |
| 55-56 | Protection | Sacred Duty | 2 | 8/12/27 |
| 57 | Protection | Redoubt | 1 | 8/13/27 |
| 58 | Protection | Guardian's Favor | 1 | 8/14/27 |
| 59 | Protection | Improved Seal of Fury | 1 | 8/15/27 |
| 60 | Protection | Swift Judgement | 1 | 8/16/27 |

## Core talents (priority order)

1. **Sanctified Judgement** — +3.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Seal of Command** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Seals** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Two-Handed Weapon Specialization** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Swift Judgement** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Conviction** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Sacred Arbiter** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Vengeance** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 27.48; holy-leveling 35.45. The search simulated 68,400 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Prot-Ret leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/50003-5231110021-332052310013301-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
