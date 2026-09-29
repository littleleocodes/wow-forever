# Optimizer — Two-handed Arms/raid or leveling: white ~45%, Heroic Strike, Overpower, Execute, Rend; Mortal Strike/Slam arrive as talent effects (raid-dps) — 19/32/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `arms-2h-raid` and profile `raid-dps`: score +79.1% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Impale** | 2/2 | changed | Increases the critical strike damage bonus of your abilities by 20%. |
| **Two-Handed Weapon Specialization** | 2/3 | changed | Increases the damage you deal with two-handed melee weapons by 2%. |

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

1. **Flurry** — Removing it costs 22.3 points of score in this model.
2. **Death Wish** — Removing it costs 14.4 points of score in this model.
3. **Cruelty** — Removing it costs 10.2 points of score in this model.
4. **Deep Wounds** — Removing it costs 8.8 points of score in this model.
5. **Bloodthirst** — Removing it costs 8.5 points of score in this model.
6. **Improved Execute** — Removing it costs 8.2 points of score in this model.
7. **Precision** — Removing it costs 5.7 points of score in this model.
8. **Impale** — Removing it costs 5.2 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 5** for `arms-2h-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-arms-2h-raid-raid-dps`](opt-arms-2h-raid-raid-dps.md)** | ours: optimizer | 19/32/0 | 218 | +0.0% | 456 | +0.0% | 0 s |
| 2 | [`arms-2h-raid`](arms-2h-raid.md) | ours: hand draft | 19/32/0 | 216 | -0.6% | 455 | -0.3% | 0 s |
| 3 | *DPS* | community simulator | - | 196 | -10.1% | 427 | -6.5% | 0 s |
| 4 | *Fury 17/34/0* | community simulator | - | 190 | -12.7% | 411 | -9.9% | 0 s |
| 5 | *Arms 39/12/0* | community simulator | - | 166 | -23.5% | 376 | -17.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 11 changes to the base rotation; third-seed check: opt-arms-2h-raid-raid-dps 154 -> 217 DPS (+41.1%), sim preset: DPS 144 -> 195 DPS (+35.8%)):
  1. drop: if false: cast Recklessness (+16.4%, pass 1)
  2. insert before the filler: if stacks of Sunder Armor < 5: cast Sunder Armor (+5.8%, pass 1)
  3. drop: if rage < 90: cast Bloodrage (+1.7%, pass 1)
  4. drop the condition: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+3.2%, pass 1)
  5. drop: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+2.2%, pass 1)
  6. threshold 30s -> 22.5s: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.3%, pass 1)
  7. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+0.9%, pass 1)
  8. move to the top: if execute phase (E20): cast Execute (+0.4%, pass 1)
  9. threshold 22.5s -> 23.5s: if (time left in the fight ≤ 22.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.3%, pass 1)
  10. threshold 23.5s -> 24.5s: if (time left in the fight ≤ 23.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.9%, pass 1)
  11. threshold 24.5s -> 25.5s: if (time left in the fight ≤ 24.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.5%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-arms-2h-raid-raid-dps 378 -> 457 DPS (+20.9%), sim preset: DPS 354 -> 427 DPS (+20.7%)):
  1. drop: if false: cast Recklessness (+12.7%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+5.3%, pass 1)
  3. drop: if not Battle Shout is up: cast Battle Shout (+1.0%, pass 1)
  4. drop the condition: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.4%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`opt-arms-2h-raid-raid-dps`](opt-arms-2h-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if execute phase (E20): cast Execute | 4.6 |
| 2 | cast item 10646 | as ready |
| 3 | cast item 18641 | as ready |
| 4 | if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish | 0.5 |
| 5 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 6 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 7 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 8 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 9 | if (time left in the fight ≤ 25.5s or time left in the fight ≥ 140s): use every other cooldown when ready | as ready |
| 10 | if number of targets > 1: cast Whirlwind | 3.3 |
| 11 | cast Bloodthirst | 2.4 |
| 12 | cast Whirlwind | 3.3 |
| 13 | if not Battle Shout is up: cast Battle Shout | 0.5 |
| 14 | if stacks of Sunder Armor < 5: cast Sunder Armor | 5.6 |

Lines of the simulator's rotation these builds never cast: cast Blood Fury, cast spell 24427, cast spell 29602, cast Cleave, cast Hamstring, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`opt-arms-2h-raid-raid-dps`](opt-arms-2h-raid-raid-dps.md) |
|---|---|
| Auto Attack | 44% |
| Execute | 37% |
| Whirlwind | 8% |
| Bloodthirst | 5% |
| Deep Wound | 5% |
| Dragonbreath Chili | 1% |

## Notes

- Report: warrior/talents/forever/optimizer/arms-2h-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
