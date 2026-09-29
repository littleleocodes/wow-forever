# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (raid-dps) — 9/35/7

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/35/7 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `raid-dps`: score +108.2% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Feral Swiftness** | 1/2 | **NEW** | Increases your movement speed while in Cat Form by 15%, and increases your chance to Dodge by 2%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **King of the Jungle** | 3/3 | **NEW** | Tiger's Fury now instantly grants you 60 Energy. |
| **Predatory Instincts** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20%. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 100% of the Energy you had when you were last in Cat Form, plus 10 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 100 Energy. |
| **Naturalist** | 2/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.2 sec and increases all damage you deal by 2%. |

## Core talents (priority order)

1. **Shredding Attacks** — Removing it costs 35.6 points of score in this model.
2. **King of the Jungle** — Removing it costs 17.9 points of score in this model.
3. **Blood Frenzy** — Removing it costs 15.1 points of score in this model.
4. **Sharpened Claws** — Removing it costs 10.9 points of score in this model.
5. **Rend and Tear** — Removing it costs 10.4 points of score in this model.
6. **Berserk** — Removing it costs 7.4 points of score in this model.
7. **Predatory Strikes** — Removing it costs 6.7 points of score in this model.
8. **Predatory Instincts** — Removing it costs 6.6 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 4** for `feral-cat-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md)** | ours: optimizer | 9/35/7 | 350 | +0.0% | 556 | +0.0% | 0 s |
| 2 | *Feral Cat 9/35/7* | community simulator | - | 350 | +0.0% | 556 | +0.0% | 0 s |
| 3 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 349 | -0.4% | 555 | -0.2% | 0 s |
| 4 | *Feral* | community simulator | - | 335 | -4.5% | 533 | -4.2% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 7 changes to the base rotation; third-seed check: opt-feral-cat-dps-raid-dps 336 -> 356 DPS (+6.0%), sim preset: Feral Cat 9/35/7 336 -> 356 DPS (+6.0%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+2.2%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.6%, pass 1)
  3. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+1.1%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.4%, pass 1)
  5. drop the condition: if not Cat Form is up: cast item 10646 (+0.2%, pass 1)
  6. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 13.9: cancel Cat Form (+0.2%, pass 1)
  7. threshold 14.0s -> 28s: if Faerie Fire should be refreshed: cast Faerie Fire (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-feral-cat-dps-raid-dps 549 -> 566 DPS (+3.2%), sim preset: Feral Cat 9/35/7 549 -> 566 DPS (+3.2%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.3%, pass 1)
  3. drop: if not Cat Form is up and mana % ≤ 40% and time left in the fight ≥ 20.0 and not (Demonic Rune is known and Demonic Rune is ready or Potion is known and Potion is ready): cast Innervate (+0.5%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.2%, pass 1)

Before the pull: at -1.0s: cast Faerie Fire; at -3.5s: cast Tiger's Fury.

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | cast Tiger's Fury | 2.3 |
| 2 | if Faerie Fire should be refreshed: cast Faerie Fire | 5.5 |
| 3 | if Cat Form is up: use every other cooldown when ready | as ready |
| 4 | if combo points ≥ 3.75 and not Rip is on the target: cast Rip | 4.6 |
| 5 | cast Shred | 17.1 |
| 6 | if Faerie Fire should be refreshed: cast Faerie Fire | 5.5 |
| 7 | cast Goblin Sapper Charge | as ready |
| 8 | if not Cat Form is up and (mana + 1500.0) ≤ (mana ÷ mana %): cast Demonic Rune | as ready |
| 9 | if not Cat Form is up and (mana + 2250.0) ≤ (mana ÷ mana %): cast Potion | as ready |
| 10 | if not Cat Form is up: cast Cat Form | 0.3 |

Lines of the simulator's rotation these builds never cast: cast spell 13494, cast spell 23724, cast Innervate (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) |
|---|---|
| Rip | 37% |
| Shred | 31% |
| Auto Attack | 29% |
| item 10646 | 2% |
| Dragonbreath Chili | 1% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
