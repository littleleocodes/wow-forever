# Optimizer — Two-handed Arms/raid or leveling: white ~45%, Heroic Strike, Overpower, Execute, Rend; Mortal Strike/Slam arrive as talent effects (parse) — 19/32/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `arms-2h-raid` and profile `parse`: score +79.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Deflection** | 3/5 | unchanged | Increases your Parry chance by 3%. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 3%. |
| **Spearing Strike** | 1/1 | **NEW** | A brutal attack that deals 40% weapon damage. Deals an additional 80% weapon damage against Giants, Dragonkin, and mounted targets. Mounted targets are dismounted. |

### Fury (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Booming Voice** | 2/5 | changed | Increases the radius of your Battle Shout and Demoralizing Shout abilities by 20%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons. |
| **Boundless Rage** | 3/3 | **NEW** | Increases your maximum Rage by 30. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Precision** | 3/3 | **NEW** | Improves your chance to hit by 3%. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 35% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Flurry** — Removing it costs 28.9 points of score in this model.
2. **Bloodthirst** — Removing it costs 15.4 points of score in this model.
3. **Cruelty** — Removing it costs 8.9 points of score in this model.
4. **Deep Wounds** — Removing it costs 8.8 points of score in this model.
5. **Unbridled Wrath** — Removing it costs 6.4 points of score in this model.
6. **Precision** — Removing it costs 5.7 points of score in this model.
7. **Two-Handed Weapon Specialization** — Removing it costs 5.2 points of score in this model.
8. **Anger Management** — Removing it costs 4.5 points of score in this model.

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Report: warrior/research/talents/forever/optimizer/arms-2h-raid-parse.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
