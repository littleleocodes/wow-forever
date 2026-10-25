# Fire — Ignite / Heating Up (simulator winner adopted 2026-09-28) — 14/34/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/34/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fire-raid` |

## Summary

Allocation adopted on 2026-09-28 from `cand-fire-raid-r5`, the best build in the community simulator (+2.7% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Ignite (40% at max), Improved Scorch (100% chance, 5 stacks of 3%), Critical Mass, Fire Power, Master of Elements and Combustion all survive; Incinerate and Improved Fire Blast are gone; Hot Streak (crits shorten Pyroblast up to 75%; renamed Heating Up in build 70170) is the new 16-point talent. Elemental Precision is taken to 5 for hit, so Arcane stops at Arcane Concentration and Magic Absorption/Arcane Resilience fillers.

## Point allocation

### Arcane (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, your Arcane Missile hits a 10% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |

### Fire (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 5/5 | unchanged | Increases the critical strike chance of your Fire spells by 10%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |

## Core talents (priority order)

1. **Improved Scorch** — 5 stacks of +3% Fire damage taken; 100% application at max rank (est.). Raid sim (2026-09-28): removing it costs +54% DPS.
2. **Heating Up** — New: Fireball/Scorch/Fire Blast crits stack -25% Pyroblast cast time (3 stacks) — a 1.5s Pyroblast after three crits. Raid sim (2026-09-28): the simulator's rotation reads this talent's own proc, so its removal run breaks the rotation and is not its value. (Hot Streak was renamed Heating Up in build 70170.)
3. **Ignite** — 40% of crit damage as a burn (unchanged) — still the fire engine. Raid sim (2026-09-28): removing it costs +14% DPS.
4. **Fire Power** — +10% Fire damage. Raid sim (2026-09-28): removing it costs +10% DPS.
5. **Combustion** — Reworked: each Fire hit +10% crit until 4 crits. Raid sim (2026-09-28): removing it costs +9% DPS.
6. **Arcane Concentration** — Clearcasting. Raid sim (2026-09-28): removing it costs +9% DPS.
7. **Critical Mass** — +6% Fire crit. Raid sim (2026-09-28): removing it costs +6% DPS.
8. **Improved Fireball** — -0.5s Fireball (also Frostfire Bolt). Raid sim (2026-09-28): removing it costs +6% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Improved Fire Blast | any utility talent legal at that tier | Measures +0.5% DPS in the community simulator (noise): these points are free to move. (Wake of Fire until build 70425; the client renamed it Improved Fire Blast in place.) |
| 5 | Burning Soul | Arcane Focus, any utility talent legal at that tier | Measures +0.1% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Wand Specialization, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Magic Absorption, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**4 of 7** for `fire-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) | ours: optimizer | 18/31/2 | 648 | +0.0% | 815 | -4.1% | 17 s |
| 2 | [`fire-open-raid`](fire-open-raid.md) | ours: derived (open search) | 17/31/3 | 646 | -0.4% | 850 | +0.0% | 29 s |
| 3 | *Fire* | community simulator | - | 642 | -0.9% | 848 | -0.2% | 29 s |
| 4 | **[`fire-raid`](fire-raid.md)** | ours: hand draft | 14/34/3 | 623 | -3.9% | 830 | -2.3% | 33 s |
| 5 | *FFB* | community simulator | - | 393 | -39.3% | 546 | -35.8% | 59 s |
| 6 | *Arcane Fire* | community simulator | - | 379 | -41.6% | 619 | -27.1% | 12 s |
| 7 | *Arcane Frost* | community simulator | - | 340 | -47.5% | 436 | -48.7% | 12 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-10-23, 20 changes to the base rotation; third-seed check: open winner 810 -> 849 DPS (+4.8%), fire-raid 813 -> 831 DPS (+2.2%), sim preset: Fire 814 -> 848 DPS (+4.1%), opt-fire-raid-raid-dps 786 -> 816 DPS (+3.8%)):
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

| # | Priority (the first line whose condition holds is cast) | [`fire-raid`](fire-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch | 5.2 |
| 2 | if mana % ≤ 60% and mana % ≥ 25%: cast Mana Ruby | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 5 | if stacks of Heating Up = 3: cast Pyroblast | 3.0 |
| 6 | cast Fire Blast | 6.6 |
| 7 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 1.9 |
| 8 | if time left in the fight ≥ 3s: cast Fireball (rank 11) | 7.6 |
| 9 | cast Robe of the Archmage | as ready |
| 10 | cast Scorch | 5.2 |
| 11 | cast Frost Blast | 1.9 |

Lines of the simulator's rotation these builds never cast: cast Fireball (rank 10) (its condition never held in these fights).

Damage by ability:

| Ability | [`fire-raid`](fire-raid.md) |
|---|---|
| Fireball | 32% |
| Pyroblast | 20% |
| Fire Blast | 18% |
| Ignite | 10% |
| Arcane Missiles | 9% |
| Scorch | 8% |
| Demonic Rune | 1% |
| Frost Blast | 1% |

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

## Open questions (verify in the live game)

- Does a 3-stack Hot Streak Pyroblast (1.5s cast) beat Fireball per cast time? If yes, Pyroblast enters the rotation.
- Incineration (Scorch/Fire Blast/Arcane Blast crit) vs. Flame Throwing.
- Whether Arcane Meditation 3/3 (est. 51% regen while casting) is worth 5 Arcane filler points and 2 hit.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
