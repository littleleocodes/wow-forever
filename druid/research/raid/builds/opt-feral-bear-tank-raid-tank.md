# Optimizer — Maul 40%, white 30%, Swipe 15%, Faerie Fire/Demoralizing Roar 5%, Thorns 10%; Mangle arrives as a talent effect (raid-tank) — 9/42/0

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/42/0 (Balance / Feral Combat / Restoration) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-bear-tank` and profile `raid-tank`: score +155.7% (tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |

### Feral Combat (42)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Primal Bite** | 1/1 | **NEW** | Bite the target, dealing 100% normal damage plus 26 and generating a high amount of threat. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Natural Reaction** | 5/5 | **NEW** | Increases your dodge chance by 5%, and gives you a 100% chance to gain 5 Rage each time you dodge. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |

### Restoration (0)

*No points.*

## Core talents (priority order)

1. **Ferocity** — Removing it costs 58.3 points of score in this model.
2. **Blood Frenzy** — Removing it costs 54.8 points of score in this model.
3. **Sharpened Claws** — Removing it costs 19.6 points of score in this model.
4. **Shredding Attacks** — Removing it costs 17.0 points of score in this model.
5. **Nature's Majesty** — Removing it costs 13.2 points of score in this model.
6. **Natural Reaction** — Removing it costs 12.1 points of score in this model.
7. **Leader of the Pack** — Removing it costs 10.3 points of score in this model.
8. **Rend and Tear** — Removing it costs 9.5 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 4** for `feral-bear-tank` by tank value in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | **[`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md)** | ours: optimizer | 9/42/0 | 1.046 | +0.0% | 3139 | 360 |
| 2 | [`feral-bear-tank`](feral-bear-tank.md) | ours: hand draft | 7/35/9 | 1.000 | -4.4% | 2874 | 360 |
| 3 | *Hybrid* | community simulator | - | 0.889 | -15.0% | 2428 | 386 |
| 4 | *Bear* | community simulator | - | 0.825 | -21.1% | 2068 | 387 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-17, 3 changes to the base rotation; third-seed check: deep: tank 539 -> 537 DPS (-0.4%), feral-bear-tank 539 -> 537 DPS (-0.4%), sim preset: Bear Tank 0/31/20 495 -> 499 DPS (+1.0%), opt-feral-bear-tank-raid-tank 539 -> 537 DPS (-0.4%)):
  1. threshold 25 -> 50: if rage ≥ 25: cast Maul (+0.9%, pass 1)
  2. move down below 'if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate': cast Primal Bite (+0.6%, pass 1)
  3. insert before the filler: cast Barkskin (+2.2%, pass 3)

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate | 29.3 |
| 3 | cast Primal Bite | 9.6 |
| 4 | if rage ≥ 50: cast Maul | 112.9 |
| 5 | cast Barkskin | 1.0 |
| 6 | cast Lacerate | 29.3 |

Lines of the simulator's rotation these builds never cast: cast Faerie Fire, cast Demoralizing Roar (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) |
|---|---|
| Maul | 67% |
| Auto Attack | 17% |
| Lacerate | 7% |
| Primal Bite | 5% |
| Judgement of Light | 2% |
| OtherActionRageGain | 2% |
| Retribution Aura | 0% |
| Thorns | 0% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-bear-tank-raid-tank.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
