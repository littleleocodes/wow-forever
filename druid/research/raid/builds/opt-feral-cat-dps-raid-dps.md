# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (raid-dps) — 9/30/12

*[Druid](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/30/12 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `raid-dps`: score +90.8% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Feral Combat (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 2/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Shredding Attacks** | 3/3 | **NEW** | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 15%. |

### Restoration (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Reflection** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |

## Core talents (priority order)

1. **Shredding Attacks** — Removing it costs 28.9 points of score in this model.
2. **Blood Frenzy** — Removing it costs 14.3 points of score in this model.
3. **Sharpened Claws** — Removing it costs 9.9 points of score in this model.
4. **Rend and Tear** — Removing it costs 9.5 points of score in this model.
5. **Naturalist** — Removing it costs 9.1 points of score in this model.
6. **Predatory Strikes** — Removing it costs 6.1 points of score in this model.
7. **Natural Instinct** — Removing it costs 6.0 points of score in this model.
8. **Nature's Reach** — Removing it costs 5.6 points of score in this model.

## Rank among our builds and the community simulator's

**4 of 6** for `feral-cat-dps` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Cat* | community simulator | - | 464 | +0.0% | 912 | -1.7% | 62 s |
| 2 | [`feral-combat-shifting-power-raid`](feral-combat-shifting-power-raid.md) | ours: derived (simulator preset) | 9/33/9 | 463 | -0.2% | 911 | -1.8% | 62 s |
| 3 | [`feral-combat-open-raid`](feral-combat-open-raid.md) | ours: derived (open search) | 9/32/10 | 458 | -1.3% | 927 | +0.0% | 62 s |
| 4 | **[`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md)** | ours: optimizer | 9/30/12 | 416 | -10.4% | 760 | -18.0% | 0 s |
| 5 | *Hybrid* | community simulator | - | 413 | -11.0% | 846 | -8.7% | 62 s |
| 6 | [`feral-cat-dps`](feral-cat-dps.md) | ours: hand draft | 9/32/10 | 403 | -13.1% | 740 | -20.2% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-10, 10 changes to the base rotation; third-seed check: open winner 368 -> 390 DPS (+5.9%), opt-feral-cat-dps-raid-dps 346 -> 368 DPS (+6.4%), sim preset: Feral Cat 9/35/7 368 -> 394 DPS (+7.2%), feral-cat-dps 337 -> 357 DPS (+5.9%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+2.2%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.6%, pass 1)
  3. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+1.1%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.4%, pass 1)
  5. drop the condition: if not Cat Form is up: cast Goblin Sapper Charge (+0.2%, pass 1)
  6. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 13.9: cancel Cat Form (+0.2%, pass 1)
  7. threshold 14.0s -> 28s: if Faerie Fire should be refreshed: cast Faerie Fire (+0.2%, pass 1)
  8. drop the condition: if Faerie Fire should be refreshed: cast Faerie Fire (+0.6%, pass 4)
  9. only with 6s or more of the fight left: cast Faerie Fire (+0.8%, pass 4)
  10. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+11.8%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-11-02, 10 changes to the base rotation; third-seed check: feral-combat-open-raid 758 -> 758 DPS (+0.0%), sim preset: Cat 750 -> 750 DPS (+0.0%), feral-cat-dps 620 -> 620 DPS (+0.0%), opt-feral-cat-dps-raid-dps 630 -> 630 DPS (+0.0%), feral-combat-shifting-power-raid 745 -> 745 DPS (+0.0%)):
  1. drop: if combo points = 5.0 and not Clearcasting is up and (energy + 20.2) < (current cost + current cost): cast Ferocious Bite (+1.0%, pass 1)
  2. threshold 5 -> 3.75: if combo points ≥ 5 and not Rip is on the target: cast Rip (+1.3%, pass 1)
  3. drop: if not Cat Form is up and mana % ≤ 40% and time left in the fight ≥ 20.0 and not (Demonic Rune is known and Demonic Rune is ready or Potion is known and Potion is ready): cast Innervate (+0.5%, pass 1)
  4. threshold 27.8 -> 13.9: if Furor is known and mana ≥ current cost and the global cooldown is ready and Clearcasting is known and Clearcasting is up and energy < 27.8: cancel Cat Form (+0.2%, pass 1)
  5. drop: if Furor is known and mana ≥ current cost and the global cooldown is ready and (combo points < 5.0 and (energy + 20.2) < current cost or combo points = 5.0 and (energy + 20.2) < current cost or Clearcasting is known and Clearcasting is up and energy < 27.8): cancel Cat Form (+0.2%, pass 4)
  6. insert in the middle: if Shifting Power is known and energy ≤ 60: cast Shifting Power (+9.9%, pass 5)
  7. insert at the top: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+7.5%, pass 7)
  8. drop 'combo points < 5' from the condition: if combo points < 5 and not Rake is on the target and time left in the fight > 6s: cast Rake (+0.5%, pass 7)
  9. insert at the top: if (combo points ≥ 5 and not time left in the fight ≥ 10s or combo points ≥ 3 and time left in the fight < 3s): cast Ferocious Bite (rank 4) (+0.2%, pass 8)
  10. rotation replaced by the official simulator's adaptive.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+1.0%, pass 10)

Before the pull: at -1.0s: cast Faerie Fire; at -3.5s: cast Tiger's Fury.

| # | Priority (the first line whose condition holds is cast) | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if Faerie Fire should be refreshed: cast Faerie Fire | 9.6 |
| 2 | if Cat Form is up: use every other cooldown when ready | as ready |
| 3 | if combo points ≥ 3.75 and not Rip is on the target: cast Rip | 4.3 |
| 4 | cast Shred | 14.3 |
| 5 | if time left in the fight ≥ 6s: cast Faerie Fire | 9.6 |
| 6 | cast Goblin Sapper Charge | as ready |
| 7 | if not Cat Form is up and (mana + 1500.0) ≤ (mana ÷ mana %): cast Demonic Rune | as ready |
| 8 | if not Cat Form is up and (mana + 2250.0) ≤ (mana ÷ mana %): cast Potion | as ready |

Lines of the simulator's rotation these builds never cast: cast Tiger's Fury, cast Haste, cast Metamorphosis Rune, cast Innervate, cast Cat Form (its condition never held in these fights); cast Shifting Power (needs the Shifting Power talent).

Damage by ability:

| Ability | [`opt-feral-cat-dps-raid-dps`](opt-feral-cat-dps-raid-dps.md) |
|---|---|
| Rip | 41% |
| Shred | 29% |
| Auto Attack | 28% |
| Goblin Sapper Charge | 2% |
| spell 18211 | 1% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-raid-dps.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 9/31/11 -> 9/30/12; Berserk 1 gone; refill +1 Reflection (refill: the feral-cat-dps model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
