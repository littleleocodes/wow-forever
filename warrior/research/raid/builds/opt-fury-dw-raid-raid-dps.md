# Optimizer — Raid dual-wield Fury: white ~50% (MH 35 / OH 15), Heroic Strike dump, Whirlwind, Execute, Overpower; Bloodthirst and Deep Wounds arrive as talent effects (raid-dps) — 13/38/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 13/38/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fury-dw-raid` and profile `raid-dps`: score +118.4% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arms (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Deflection** | 2/5 | unchanged | Increases your Parry chance by 2%. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 2/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 40% of your melee weapon's average damage over 12 sec. |

### Fury (38)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Booming Voice** | 2/5 | changed | Increases the radius of your Battle Shout and Demoralizing Shout abilities by 20%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. This effect is increased to 2 Rage for two-handed weapons. |
| **Boundless Rage** | 3/3 | **NEW** | Increases your maximum Rage by 30. |
| **Raging Blows** | 1/1 | **NEW** | Causes your Whirlwind to also strike with your off-hand weapon, and reduces the Rage cost of your Cleave ability by 2. |
| **Dual Wield Specialization** | 5/5 | changed | Increases your off-hand weapon damage by 25%, off-hand Rage generation by 100%, and chance to hit with off-hand attacks by 10%. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Precision** | 3/3 | **NEW** | Improves your chance to hit by 3%. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 35% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Dual Wield Specialization** — Removing it costs 31.8 points of score in this model.
2. **Flurry** — Removing it costs 30.8 points of score in this model.
3. **Bloodthirst** — Removing it costs 19.7 points of score in this model.
4. **Improved Execute** — Removing it costs 12.8 points of score in this model.
5. **Death Wish** — Removing it costs 10.9 points of score in this model.
6. **Cruelty** — Removing it costs 10.1 points of score in this model.
7. **Raging Blows** — Removing it costs 8.8 points of score in this model.
8. **Precision** — Removing it costs 7.4 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 5** for `fury-dw-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`fury-dw-raid`](fury-dw-raid.md) | ours: hand draft | 13/38/0 | 390 | +0.0% | 706 | -0.5% | 0 s |
| 2 | **[`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md)** | ours: optimizer | 13/38/0 | 390 | -0.0% | 710 | +0.0% | 0 s |
| 3 | *DPS* | community simulator | - | 371 | -5.0% | 683 | -3.8% | 0 s |
| 4 | *Fury 17/34/0* | community simulator | - | 344 | -11.8% | 629 | -11.4% | 0 s |
| 5 | *Arms 39/12/0* | community simulator | - | 234 | -40.1% | 448 | -36.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 20 changes to the base rotation; third-seed check: ml: Fury 320 -> 396 DPS (+23.9%), fury-dw-raid 318 -> 390 DPS (+22.6%), sim preset: DPS 299 -> 371 DPS (+24.0%)):
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
  16. drop: if stacks of Sunder Armor < 4 and not Expose Armor is up and time left in the fight ≥ 20s: cast Sunder Armor (+0.5%, pass 5)
  17. threshold 60 -> 120: if number of targets = 1 and (rage ≥ 60 or execute phase (E20)) and time left in the fight ≥ 40s: cast Heroic Strike (+0.4%, pass 5)
  18. threshold 22.5s -> 33.75s: if time left in the fight ≤ 22.5s: cast Recklessness (+0.3%, pass 5)
  19. threshold 30s -> 45s: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+1.2%, pass 5)
  20. threshold 22.5s -> 33.75s: if (time left in the fight ≤ 22.5s or time left in the fight ≥ 70s): use every other cooldown when ready (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 9 changes to the base rotation; third-seed check: ml: Fury 669 -> 720 DPS (+7.6%), fury-dw-raid 665 -> 707 DPS (+6.3%), sim preset: DPS 632 -> 683 DPS (+8.1%)):
  1. drop: if false: cast Recklessness (+11.1%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+2.5%, pass 1)
  3. threshold 90 -> 45: if rage < 90: cast Bloodrage (+0.7%, pass 1)
  4. drop: if not Battle Shout is up: cast Battle Shout (+0.6%, pass 1)
  5. threshold 45 -> 22.5: if rage < 45: cast Bloodrage (+0.3%, pass 1)
  6. drop 'time left in the fight ≥ 140s' from the condition: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.8%, pass 5)
  7. threshold 30s -> 45s: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+0.7%, pass 5)
  8. threshold 1.5s -> 0s: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.6%, pass 5)
  9. threshold 30s -> 45s: if time left in the fight ≤ 30s: use every other cooldown when ready (+0.5%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if (time left in the fight ≤ 45s or time left in the fight ≥ 211.5s): cast Death Wish | 0.3 |
| 2 | if execute phase (E20): cast Execute | 6.7 |
| 3 | cast Bloodthirst | 5.7 |
| 4 | if time left in the fight ≤ 33.75s: cast Recklessness | 0.3 |
| 5 | cast Goblin Sapper Charge | as ready |
| 6 | cast Dense Dynamite | as ready |
| 7 | if false: cast Recklessness | 0.3 |
| 8 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 9 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 10 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 11 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 12 | if (time left in the fight ≤ 33.75s or time left in the fight ≥ 70s): use every other cooldown when ready | as ready |
| 13 | cast Whirlwind | 3.9 |
| 14 | if time until Bloodthirst is ready > 1.5s: cast Whirlwind | 3.9 |
| 15 | if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring | 0.1 |
| 16 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 17 | if stacks of Sunder Armor < 5: cast Sunder Armor | 7.1 |

Lines of the simulator's rotation these builds never cast: cast Blood Fury, cast Diamond Flask, cast Jom Gabbar, cast Heroic Strike, cast Cleave, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`opt-fury-dw-raid-raid-dps`](opt-fury-dw-raid-raid-dps.md) |
|---|---|
| Auto Attack | 53% |
| Execute | 24% |
| Bloodthirst | 11% |
| Whirlwind | 9% |
| Deep Wound | 1% |
| Dragonbreath Chili | 1% |
| Hamstring | 0% |
| Heroic Strike | 0% |

## Notes

- Report: warrior/research/talents/forever/optimizer/fury-dw-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
