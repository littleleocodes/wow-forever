# Optimizer — Maul 40%, white 30%, Swipe 15%, Faerie Fire/Demoralizing Roar 5%, Thorns 10%; Mangle arrives as a talent effect (raid-tank) — 7/35/9

*[Druid](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/35/9 (Balance / Feral Combat / Restoration) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-bear-tank` and profile `raid-tank`: score +53.0% (tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |

### Feral Combat (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Leap behind an enemy. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Predatory Instincts** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20%. |
| **Natural Reaction** | 5/5 | **NEW** | Increases your dodge chance by 5%, and gives you a 100% chance to gain 5 Rage each time you dodge. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 4/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.4 sec and increases all damage you deal by 4%. |

## Core talents (priority order)

1. **Blood Frenzy** — Removing it costs 9.9 points of score in this model.
2. **Shredding Attacks** — Removing it costs 9.3 points of score in this model.
3. **Thick Hide** — Removing it costs 8.0 points of score in this model.
4. **Natural Reaction** — Removing it costs 7.2 points of score in this model.
5. **Sharpened Claws** — Removing it costs 6.6 points of score in this model.
6. **Rend and Tear** — Removing it costs 5.7 points of score in this model.
7. **Feral Swiftness** — Removing it costs 3.4 points of score in this model.
8. **Nature's Majesty** — Removing it costs 3.0 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 3** for `feral-bear-tank` by tank value in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | [`feral-bear-tank`](feral-bear-tank.md) | ours: hand draft | 7/35/9 | 1.000 | +0.0% | 802 | 1042 |
| 2 | **[`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md)** | ours: optimizer | 7/35/9 | 1.000 | +0.0% | 802 | 1042 |
| 3 | *Bear Tank 0/31/20* | community simulator | - | 0.857 | -14.3% | 612 | 1096 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 2 passes, the last 2026-09-28, 2 changes to the base rotation; third-seed check: feral-bear-tank 381 -> 384 DPS (+0.8%), sim preset: Bear Tank 0/31/20 368 -> 364 DPS (-1.1%)):
  1. threshold 25 -> 50: if rage ≥ 25: cast Maul (+0.9%, pass 1)
  2. move down below 'if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate': cast Primal Bite (+0.6%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if (stacks of Lacerate < 5 or time left on Lacerate ≤ 4.5s): cast Lacerate | 38.9 |
| 3 | if rage ≥ 50: cast Maul | 1.1 |
| 4 | cast Lacerate | 38.9 |

Lines of the simulator's rotation these builds never cast: cast Faerie Fire, cast Demoralizing Roar (its condition never held in these fights); cast Primal Bite (needs the Primal Bite talent).

Damage by ability (threat for tanks):

| Ability | [`opt-feral-bear-tank-raid-tank`](opt-feral-bear-tank-raid-tank.md) |
|---|---|
| Lacerate | 77% |
| Auto Attack | 17% |
| Maul | 3% |
| OtherActionRageGain | 2% |
| Retribution Aura | 1% |
| Thorns | 1% |
| Dragonbreath Chili | 0% |

## Notes

- Report: druid/talents/forever/optimizer/feral-bear-tank-raid-tank.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
