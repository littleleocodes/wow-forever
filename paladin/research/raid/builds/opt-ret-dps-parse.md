# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (parse) — 9/8/34

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/8/34 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `parse`: score +100.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 1/5 | unchanged | Increases your total Intellect by 2%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 200, and increase your Attack Power by 3% for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage and healing by up to 100% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Core talents (priority order)

1. **Champion of the Light** — Removing it costs 39.5 points of score in this model.
2. **Seal of Command** — Removing it costs 20.7 points of score in this model.
3. **Vengeance** — Removing it costs 12.9 points of score in this model.
4. **Improved Seals** — Removing it costs 11.5 points of score in this model.
5. **Conviction** — Removing it costs 8.6 points of score in this model.
6. **Instrument of Law** — Removing it costs 7.0 points of score in this model.
7. **Precision** — Removing it costs 6.7 points of score in this model.
8. **Improved Judgement** — Removing it costs 5.4 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: paladin/research/talents/forever/optimizer/ret-dps-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
