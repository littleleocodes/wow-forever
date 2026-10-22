# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (solo-60) — 8/16/27

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 8/16/27 (Holy / Protection / Retribution) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `solo-60`: score +38.7% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 20%. Lasts 10 sec or 5 blocks. |
| **Anticipation** | 2/5 | changed | Increases your Defense Skill by 8. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Sacred Duty** | 2/2 | **NEW** | Increases your total Stamina by 4% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec. |
| **Shield Specialization** | 2/3 | changed | Increases the amount of damage absorbed by your shield by 20%, and gives your blocks a 66% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |

### Retribution (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68, and increase your Attack Power by 1% for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Two-Handed Weapon Specialization** | 2/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 4%. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1.0 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Benediction | 5 | 0/0/5 |
| 15-19 | Retribution | Conviction | 5 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-22 | Retribution | Sanctified Judgement | 2 | 0/0/13 |
| 23-24 | Retribution | Pursuit of Justice | 2 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26 | Retribution | Sanctified Judgement | 1 | 0/0/17 |
| 27-28 | Retribution | Improved Judgement | 2 | 0/0/19 |
| 29 | Retribution | Vindication | 1 | 0/0/20 |
| 30-32 | Retribution | Vengeance | 3 | 0/0/23 |
| 33-34 | Retribution | Two-Handed Weapon Specialization | 2 | 0/0/25 |
| 35-36 | Retribution | Instrument of Law | 2 | 0/0/27 |
| 37-41 | Holy | Divine Strength | 5 | 5/0/27 |
| 42-44 | Holy | Improved Seals | 3 | 8/0/27 |
| 45-49 | Protection | Redoubt | 5 | 8/5/27 |
| 50-52 | Protection | Precision | 3 | 8/8/27 |
| 53-54 | Protection | Anticipation | 2 | 8/10/27 |
| 55-56 | Protection | Sacred Duty | 2 | 8/12/27 |
| 57-58 | Protection | Shield Specialization | 2 | 8/14/27 |
| 59 | Protection | Improved Seal of Fury | 1 | 8/15/27 |
| 60 | Protection | Swift Judgement | 1 | 8/16/27 |

## Core talents (priority order)

1. **Seal of Command** — Removing it costs 3.9 points of score in this model.
2. **Sanctified Judgement** — Removing it costs 3.9 points of score in this model.
3. **Improved Seals** — Removing it costs 2.5 points of score in this model.
4. **Conviction** — Removing it costs 2.4 points of score in this model.
5. **Precision** — Removing it costs 2.4 points of score in this model.
6. **Pursuit of Justice** — Removing it costs 2.3 points of score in this model.
7. **Vengeance** — Removing it costs 2.3 points of score in this model.
8. **Instrument of Law** — Removing it costs 1.8 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: paladin/research/talents/forever/optimizer/ret-dps-solo-60.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
