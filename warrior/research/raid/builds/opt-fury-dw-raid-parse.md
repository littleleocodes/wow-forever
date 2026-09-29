# Optimizer — Raid dual-wield Fury: white ~50% (MH 35 / OH 15), Heroic Strike dump, Whirlwind, Execute, Overpower; Bloodthirst and Deep Wounds arrive as talent effects (parse) — 14/37/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/37/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fury-dw-raid` and profile `parse`: score +87.9% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Heroic Strike** | 2/3 | changed | Reduces the cost of your Heroic Strike ability by 2 Rage. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |

### Fury (37)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons. |
| **Boundless Rage** | 3/3 | **NEW** | Increases your maximum Rage by 30. |
| **Blood Craze** | 2/3 | changed | Regenerates 2% of your total Health over 6 sec after being the victim of a critical strike, dealing damage with Bloodthirst, or suffering more than 20% of your maximum Health from a single attack. |
| **Raging Blows** | 1/1 | **NEW** | Causes your Whirlwind to also strike with your off-hand weapon, and reduces the Rage cost of your Cleave ability by 2. |
| **Dual Wield Specialization** | 5/5 | changed | Increases your off-hand weapon damage by 25%, off-hand Rage generation by 100%, and chance to hit with off-hand attacks by 10%. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Precision** | 3/3 | **NEW** | Improves your chance to hit by 3%. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Dual Wield Specialization** — Removing it costs 23.9 points of score in this model.
2. **Flurry** — Removing it costs 21.2 points of score in this model.
3. **Cruelty** — Removing it costs 11.8 points of score in this model.
4. **Improved Execute** — Removing it costs 11.2 points of score in this model.
5. **Death Wish** — Removing it costs 9.5 points of score in this model.
6. **Raging Blows** — Removing it costs 8.1 points of score in this model.
7. **Unbridled Wrath** — Removing it costs 7.1 points of score in this model.
8. **Precision** — Removing it costs 6.3 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: warrior/research/talents/forever/optimizer/fury-dw-raid-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
