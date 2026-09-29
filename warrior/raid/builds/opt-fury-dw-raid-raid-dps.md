# Optimizer — Raid dual-wield Fury: white ~50% (MH 35 / OH 15), Heroic Strike dump, Whirlwind, Execute, Overpower; Bloodthirst and Deep Wounds arrive as talent effects (raid-dps) — 14/37/0

*[Warrior](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/37/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fury-dw-raid` and profile `raid-dps`: score +90.4% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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

1. **Dual Wield Specialization** — Removing it costs 23.0 points of score in this model.
2. **Flurry** — Removing it costs 20.2 points of score in this model.
3. **Death Wish** — Removing it costs 16.5 points of score in this model.
4. **Improved Execute** — Removing it costs 14.2 points of score in this model.
5. **Cruelty** — Removing it costs 9.4 points of score in this model.
6. **Unbridled Wrath** — Removing it costs 6.7 points of score in this model.
7. **Raging Blows** — Removing it costs 6.7 points of score in this model.
8. **Precision** — Removing it costs 6.3 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 5** for `fury-dw-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md)** | ours: optimizer | 14/37/0 | 256 | +0.0% | 442 | -2.9% | 0 s |
| 2 | [`fury-dw-raid`](fury-dw-raid.md) | ours: hand draft | 13/38/0 | 255 | -0.7% | 455 | +0.0% | 0 s |
| 3 | *DPS* | community simulator | - | 240 | -6.3% | 439 | -3.6% | 0 s |
| 4 | *Fury 17/34/0* | community simulator | - | 223 | -13.1% | 408 | -10.3% | 0 s |
| 5 | *Arms 39/12/0* | community simulator | - | 144 | -44.0% | 275 | -39.6% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 15 changes to the base rotation; third-seed check: opt-fury-dw-raid-raid-dps 183 -> 256 DPS (+40.2%), sim preset: DPS 171 -> 240 DPS (+40.4%)):
  1. insert at the top: if time left in the fight ≤ 15s: cast Recklessness (+14.7%, pass 1)
  2. insert before the filler: if stacks of Sunder Armor < 5: cast Sunder Armor (+12.1%, pass 1)
  3. threshold 15s -> 22.5s: if time left in the fight ≤ 15s: cast Recklessness (+1.5%, pass 1)
  4. only with 20s or more of the fight left: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+0.9%, pass 1)
  5. threshold 20s -> 40s: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)) and time left in the fight ≥ 20s: cast Heroic Strike (+0.5%, pass 1)
  6. drop: cast Bloodthirst (+0.4%, pass 1)
  7. only with 20s or more of the fight left: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+0.7%, pass 1)
  8. threshold 1 -> 3: if stacks of Sunder Armor < 1 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor (+0.2%, pass 1)
  9. drop: if rage < 90: cast Bloodrage (+0.3%, pass 1)
  10. threshold 30s -> 22.5s: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.6%, pass 1)
  11. threshold 140s -> 70s: if (time left in the fight ≤ 22.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.2%, pass 1)
  12. move to the top: if execute phase (E20): cast Execute (+0.6%, pass 1)
  13. threshold 40 -> 60: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)) and time left in the fight ≥ 40s: cast Heroic Strike (+0.2%, pass 1)
  14. drop the condition: if number of targets > 1: cast Whirlwind (+0.4%, pass 1)
  15. threshold 3 -> 4: if stacks of Sunder Armor < 3 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor + move to the top: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: opt-fury-dw-raid-raid-dps 383 -> 441 DPS (+15.2%), sim preset: DPS 378 -> 439 DPS (+16.2%)):
  1. drop: if false: cast Recklessness (+11.1%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+2.5%, pass 1)
  3. threshold 90 -> 45: if rage < 90: cast Bloodrage (+0.7%, pass 1)
  4. drop: if not Battle Shout is up: cast Battle Shout (+0.6%, pass 1)
  5. threshold 45 -> 22.5: if rage < 45: cast Bloodrage (+0.3%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish | 0.5 |
| 2 | if execute phase (E20): cast Execute | 6.5 |
| 3 | if time left in the fight ≤ 22.5s: cast Recklessness | 0.5 |
| 4 | if stacks of Sunder Armor < 4 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor | 8.5 |
| 5 | cast item 10646 | as ready |
| 6 | cast item 18641 | as ready |
| 7 | if false: cast Recklessness | 0.5 |
| 8 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 9 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 10 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 11 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 12 | if (time left in the fight ≤ 22.5s or time left in the fight ≥ 70s): use every other cooldown when ready | as ready |
| 13 | cast Whirlwind | 4.0 |
| 14 | if time until Bloodthirst is ready > 1.5s: cast Whirlwind | 4.0 |
| 15 | if number of targets = 1 and (rage ≥ 60 or execute phase (E20)) and time left in the fight ≥ 40s: cast Heroic Strike | 4.5 |
| 16 | if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring | 0.1 |
| 17 | if not Battle Shout is up: cast Battle Shout | 0.5 |
| 18 | if stacks of Sunder Armor < 5: cast Sunder Armor | 8.5 |

Lines of the simulator's rotation these builds never cast: cast Blood Fury, cast spell 24427, cast spell 29602, cast Cleave, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md) |
|---|---|
| Execute | 41% |
| Auto Attack | 40% |
| Heroic Strike | 8% |
| Whirlwind | 8% |
| Deep Wound | 2% |
| Dragonbreath Chili | 1% |
| Hamstring | 0% |

## Notes

- Report: warrior/talents/forever/optimizer/fury-dw-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
