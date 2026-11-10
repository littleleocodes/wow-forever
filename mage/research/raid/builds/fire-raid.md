# Fire — Ignite / Heating Up (simulator winner adopted 2026-09-28) — 16/32/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/32/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fire-raid` |

## Summary

Allocation adopted on 2026-09-28 from `cand-fire-raid-r5`, the best build in the community simulator (+2.7% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Ignite (40% at max), Improved Scorch (100% chance, 5 stacks of 3%), Critical Mass, Fire Power, Master of Elements and Combustion all survive; Incinerate and Improved Fire Blast are gone; Hot Streak (crits shorten Pyroblast up to 75%; renamed Heating Up in build 70170) is the new 16-point talent. Elemental Precision is taken to 5 for hit, so Arcane stops at Arcane Concentration and Magic Absorption/Arcane Resilience fillers.

## Point allocation

### Arcane (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Meditation** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |

## Core talents (priority order)

1. **Improved Scorch** — 5 stacks of +3% Fire damage taken; 100% application at max rank (est.). Raid sim (2026-09-28): removing it costs +54% DPS.
2. **Heating Up** — New: Fireball/Scorch/Fire Blast crits stack -25% Pyroblast cast time (3 stacks) — a 1.5s Pyroblast after three crits. Raid sim (2026-09-28): the simulator's rotation reads this talent's own proc, so its removal run breaks the rotation and is not its value. (Hot Streak was renamed Heating Up in build 70170.)
3. **Ignite** — 40% of crit damage as a burn (unchanged) — still the fire engine. Raid sim (2026-09-28): removing it costs +14% DPS.
4. **Fire Power** — +10% Fire damage. Raid sim (2026-09-28): removing it costs +10% DPS.
5. **Combustion** — Reworked: each Fire hit +10% crit until 4 crits. Raid sim (2026-09-28): removing it costs +9% DPS.
6. **Arcane Concentration** — Clearcasting. Raid sim (2026-09-28): removing it costs +9% DPS.
7. **Critical Mass** — +6% Fire crit. Raid sim (2026-09-28): removing it costs +6% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Improved Fire Blast | any utility talent legal at that tier | Measures +0.5% DPS in the community simulator (noise): these points are free to move. (Wake of Fire until build 70425; the client renamed it Improved Fire Blast in place.) |
| 5 | Burning Soul | Arcane Focus, any utility talent legal at that tier | Measures +0.1% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Wand Specialization, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Magic Absorption, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**5 of 11** for `fire-raid` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`fire-open-raid`](fire-open-raid.md) | ours: derived (open search) | 17/31/3 | 581 | +0.0% | 869 | +0.0% | 4 s |
| 2 | *Fire* | community simulator | - | 579 | -0.3% | 867 | -0.3% | 4 s |
| 3 | *Fire Skyborne GT 180* | community simulator | - | 579 | -0.3% | 861 | -1.0% | 2 s |
| 4 | *Fire Skyborne LT 180* | community simulator | - | 576 | -0.8% | 858 | -1.2% | 4 s |
| 5 | **[`fire-raid`](fire-raid.md)** | ours: hand draft | 16/32/3 | 572 | -1.4% | 831 | -4.4% | 5 s |
| 6 | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) | ours: optimizer | 18/31/2 | 566 | -2.4% | 827 | -4.9% | 1 s |
| 7 | *FFB* | community simulator | - | 465 | -19.9% | 610 | -29.8% | 38 s |
| 8 | *Arcane Fire* | community simulator | - | 405 | -30.2% | 580 | -33.3% | 1 s |
| 9 | *Arcane* | community simulator | - | 357 | -38.6% | 430 | -50.5% | 1 s |
| 10 | *Frost Incin* | community simulator | - | 322 | -44.5% | 365 | -58.0% | 0 s |
| 11 | *Frost Med* | community simulator | - | 313 | -46.2% | 392 | -54.9% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 5 passes, the last 2026-10-23, 12 changes to the base rotation; third-seed check: open winner 594 -> 652 DPS (+9.8%), opt-fire-raid-raid-dps 597 -> 648 DPS (+8.4%), sim preset: Fire 584 -> 643 DPS (+10.1%), fire-raid 566 -> 623 DPS (+10.1%)):
  1. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+3.1%, pass 1)
  2. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.1%, pass 1)
  3. insert before the filler: if Missile Barrage is up: cast Arcane Missiles (+0.2%, pass 1)
  4. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 2)
  5. insert before the filler: cast Fireball (+0.3%, pass 4)
  6. threshold 5s -> 6s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.3%, pass 4)
  7. only with 3s or more of the fight left: cast Fireball (+0.2%, pass 4)
  8. always rank 10 instead of rank 11: if mana % ≥ 10%: cast Fireball (rank 11) (+4.2%, pass 5)
  9. insert before the filler: cast Robe of the Archmage (+1.9%, pass 5)
  10. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (+1.4%, pass 5)
  11. insert at the end: cast Frost Blast (+0.5%, pass 5)
  12. only above 25% mana: if mana % ≤ 60%: cast Mana Ruby (+0.4%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 15 passes, the last 2026-11-10, 32 changes to the base rotation; third-seed check: fire-open-raid 687 -> 861 DPS (+25.2%), sim preset: Fire 691 -> 866 DPS (+25.4%), fire-raid 683 -> 830 DPS (+21.6%), opt-fire-raid-raid-dps 671 -> 827 DPS (+23.1%)):
  1. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.7%, pass 1)
  2. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.5%, pass 1)
  3. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.2%, pass 1)
  4. only with 3s or more of the fight left: if mana % ≥ 10%: cast Fireball (+0.2%, pass 2)
  5. move to the top: cast Fire Blast (+0.2%, pass 2)
  6. threshold 5s -> 7.5s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  7. insert before the filler: cast Blast Wave (+0.3%, pass 3)
  8. insert before the filler: cast Cone of Cold (+0.3%, pass 3)
  9. insert before the filler: cast Fireball (+0.3%, pass 4)
  10. insert in the middle: if stacks of Heating Up ≥ 2 and (time left in the fight < 6s or time left on Heating Up < 3.5s): cast Pyroblast (+0.2%, pass 5)
  11. drop: cast Fireball (+1.0%, pass 6)
  12. drop 'mana % ≥ 10%' from the condition: if mana % ≥ 10% and time left in the fight ≥ 3s: cast Fireball (+0.4%, pass 6)
  13. insert in the middle: cast Major Mana Potion (+0.3%, pass 6)
  14. move down below 'use every other cooldown when ready': if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 6)
  15. insert in the middle: if Missile Barrage is up: cast Arcane Missiles (rank 7) (+3.8%, pass 7)
  16. move to the top: if stacks of Heating Up = 3: cast Pyroblast (+0.9%, pass 7)
  17. insert at the end: cast Evocation (+1.4%, pass 8)
  18. insert before the filler: cast Robe of the Archmage (+0.4%, pass 8)
  19. threshold 80% -> 75%: if mana % ≤ 80%: cast Mana Ruby (+0.3%, pass 8)
  20. only above 10% mana: cast Evocation (+0.2%, pass 8)
  21. drop: if mana % ≥ 10%: cast Evocation (+12.4%, pass 9)
  22. threshold 3s -> 4s: if time left in the fight ≥ 3s: cast Fireball (rank 11) (+0.4%, pass 9)
  23. insert at the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+2.1%, pass 10)
  24. drop '(stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5)' from the condition: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+9.1%, pass 10)
  25. insert at the top: if stacks of Heating Up = 3 and not spellIsCasting: cast Pyroblast (+2.2%, pass 10)
  26. move to the top: cast Fire Blast (+1.2%, pass 10)
  27. drop: cast Robe of the Archmage (+0.6%, pass 10)
  28. insert before the filler: if (not Read Leyline is known or not Read Leyline is ready or Energized is up): channel Evocation (interrupt it when a higher line is ready) (+0.4%, pass 10)
  29. rotation replaced by the official simulator's deepFire.apl.json at 54ceac638 (rotation-lag audit after the re-pin) (+2.8%, pass 11)
  30. insert at the top: cast Major Mana Potion (+0.3%, pass 13)
  31. threshold 4 -> 2: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability < 4 or not spellIsCasting): cast Scorch (+0.2%, pass 14)
  32. drop: if mana < current cost: groupReference (+0.4%, pass 15)

| # | Priority (the first line whose condition holds is cast) | [`fire-raid`](fire-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch | 6.7 |
| 2 | if mana % ≤ 60% and mana % ≥ 25%: cast Mana Ruby | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 5 | if stacks of Heating Up = 3: cast Pyroblast | 5.1 |
| 6 | cast Fire Blast | 5.9 |
| 7 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 0.8 |
| 8 | if time left in the fight ≥ 3s: cast Fireball (rank 11) | 5.6 |
| 9 | cast Robe of the Archmage | as ready |
| 10 | cast Scorch | 6.7 |

Lines of the simulator's rotation these builds never cast: cast Fireball (rank 10), cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`fire-raid`](fire-raid.md) |
|---|---|
| Pyroblast | 32% |
| Fireball | 24% |
| Fire Blast | 17% |
| Scorch | 12% |
| Ignite | 9% |
| Arcane Missiles | 4% |
| Demonic Rune | 1% |

## Notes

- Adopted from the community simulator on 2026-09-28: `cand-fire-raid-r5` beat the previous draft by +2.7% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Scorch to 5 stacks -> Fireball -> Pyroblast at 3 Hot Streak stacks (if a 1.5s Pyroblast beats a Fireball) -> Fire Blast on the move.
- Fire immunity in the new raids is unknown; in Classic this build was AQ40/Naxx only.
- 2026-09-27 scenario audit: Magic Absorption 2, Arcane Resilience 1 -> Burning Soul 1, Wake of Fire 2. Arcane Resilience (armor) and Magic Absorption (resistances) only matter when you are hit; a raid caster is not. Wake of Fire measures +0.9% in the simulator on the optimizer build (ElliotWood/Forever 40be98e) and Burning Soul's third rank lowers Fire threat further.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Magic Absorption -> Improved Channeling (interrupt); Magic Absorption -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Arcane Focus -> Improved Channeling (interrupt); Arcane Focus -> Arcane Subtlety (threat); Arcane Focus -> Arcane Subtlety (threat); Arcane Focus -> Burning Soul (threat); Arcane Focus -> Burning Soul (threat). Net -0.10% on a third seed.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Fire: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 12/34/5 -> 12/34/5; Wake of Fire -> Improved Fire Blast (renamed); Fire Power 5 -> 3 (rank cap); +1 Critical Mass (prerequisite of Combustion); +1 Critical Mass (prerequisite of Combustion) (refill: the fire-raid model, raid-dps).
- 2026-10-17 (audit of 2026-10-17, finding 26): flex default Wake of Fire -> Improved Fire Blast (renamed in 70425).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 12/34/5 -> 14/34/3; Elemental Precision 5 -> 3 (rank cap); refill +2 Missile Barrage (refill: the fire-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 14/34/3 -> 16/32/3; Improved Fireball -> Accelerant (renamed); Critical Mass 5 -> 3 (rank cap); Elemental Precision -> Precision (renamed); refill +1 Magic Absorption, +1 Arcane Meditation (refill: the fire-raid model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Improved Fireball; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Does a 3-stack Hot Streak Pyroblast (1.5s cast) beat Fireball per cast time? If yes, Pyroblast enters the rotation.
- Incineration (Scorch/Fire Blast/Arcane Blast crit) vs. Flame Throwing.
- Whether Arcane Meditation 3/3 (est. 51% regen while casting) is worth 5 Arcane filler points and 2 hit.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
