# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (leveling-aoe) — 10/8/33

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/8/33 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `leveling-aoe`: score +36.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 2/5 | unchanged | Increases your total Intellect by 4%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204, and increase your Attack Power by 3% for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1.0 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 30% of your Intellect. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Retribution | Deflection | 5 | 0/0/5 |
| 15-19 | Retribution | Conviction | 5 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21-22 | Retribution | Sanctified Judgement | 2 | 0/0/13 |
| 23-24 | Retribution | Improved Judgement | 2 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26 | Retribution | Sanctified Judgement | 1 | 0/0/17 |
| 27-28 | Retribution | Vindication | 2 | 0/0/19 |
| 29 | Retribution | Pursuit of Justice | 1 | 0/0/20 |
| 30-32 | Retribution | Vengeance | 3 | 0/0/23 |
| 33-34 | Retribution | Two-Handed Weapon Specialization | 2 | 0/0/25 |
| 35-36 | Retribution | Instrument of Law | 2 | 0/0/27 |
| 37-41 | Holy | Divine Strength | 5 | 5/0/27 |
| 42-44 | Holy | Improved Seals | 3 | 8/0/27 |
| 45-47 | Protection | Toughness | 3 | 8/3/27 |
| 48 | Retribution | Two-Handed Weapon Specialization | 1 | 8/3/28 |
| 49-50 | Protection | Toughness | 2 | 8/5/28 |
| 51-53 | Protection | Precision | 3 | 8/8/28 |
| 54 | Retribution | Vindication | 1 | 8/8/29 |
| 55 | Retribution | Pursuit of Justice | 1 | 8/8/30 |
| 56 | Holy | Divine Intellect | 1 | 9/8/30 |
| 57-58 | Retribution | Champion of the Light | 2 | 9/8/32 |
| 59 | Holy | Divine Intellect | 1 | 10/8/32 |
| 60 | Retribution | Champion of the Light | 1 | 10/8/33 |

## Core talents (priority order)

1. **Conviction** — Removing it costs 4.0 points of score in this model.
2. **Seal of Command** — Removing it costs 3.4 points of score in this model.
3. **Vengeance** — Removing it costs 3.1 points of score in this model.
4. **Sanctified Judgement** — Removing it costs 2.8 points of score in this model.
5. **Improved Seals** — Removing it costs 2.5 points of score in this model.
6. **Precision** — Removing it costs 2.5 points of score in this model.
7. **Instrument of Law** — Removing it costs 2.2 points of score in this model.
8. **Divine Strength** — Removing it costs 1.7 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a two-hander: Blessing of Might and Devotion Aura up, a Seal recast before each pull (Seal of Command once talented, Seal of Righteousness before), the mob walks in (paladins have no charge), Judgement and Holy Strike on cooldown, Consecration while mana allows, Hammer of Justice into a doubled Seal of Command judgement or when hurt, Hammer of Wrath under 20%; Divine Protection and a Holy Light when low, Lay on Hands in an emergency. Between fights: 2 s loot, 6 s travel, Holy Light or Flash of Light back to 80% health, water below 35% mana; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-19, on top of the priority below): never cast Consecration; drink below 15% mana. Together +6.1% time per kill saved for `leveling-retribution` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/ret-dps-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Melee | 4.6 | 6.0 | 5.7 | 6.5 | 39% |
| Judgement | 2.0 | 2.4 | 2.2 | 2.4 | 17% |
| Holy Strike | 1.6 | 2.0 | 1.9 | 2.2 | 15% |
| Seal of Command | 0.7 | 0.8 | 0.7 | 0.8 | 18% |
| Hammer of Wrath | 0.0 | 0.0 | 0.8 | 0.8 | 10% |
| Hammer of Justice | 0.3 | 0.4 | 0.4 | 0.4 | 0% |
| Flash of Light | 0.1 | 0.3 | 0.2 | 0.4 | 0% |
| Holy Light | 0.0 | 0.1 | 0.1 | 0.1 | 0% |
| Divine Protection | 0.1 | 0.1 | 0.1 | 0.1 | 0% |
| Lay on Hands | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: paladin/research/talents/forever/optimizer/ret-dps-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
