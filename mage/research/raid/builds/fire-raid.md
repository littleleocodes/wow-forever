# Fire — Ignite / Hot Streak (simulator winner adopted 2026-09-28) — 12/34/5

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/34/5 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fire-raid` |

## Summary

Allocation adopted on 2026-09-28 from `cand-fire-raid-r5`, the best build in the community simulator (+2.7% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Ignite (40% at max), Improved Scorch (100% chance, 5 stacks of 3%), Critical Mass, Fire Power, Master of Elements and Combustion all survive; Incinerate and Improved Fire Blast are gone; Hot Streak (crits shorten Pyroblast up to 75%) is the new 16-point talent. Elemental Precision is taken to 5 for hit, so Arcane stops at Arcane Concentration and Magic Absorption/Arcane Resilience fillers.

## Point allocation

### Arcane (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |

### Fire (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Wake of Fire** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Hot Streak** | 1/1 | **NEW** | Your non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch grant Hot Streak for 20 sec. Hot Streak reduces the cast time of Pyroblast by 25%, stacking up to 3 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 4 non-periodic critical strikes with Fire spells. |
| **Burning Soul** | 2/3 | changed | Gives your Fire spells a 47% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 20%. |

### Frost (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |

## Core talents (priority order)

1. **Improved Scorch** — 5 stacks of +3% Fire damage taken; 100% application at max rank (est.). Raid sim (2026-09-28): removing it costs +54% DPS.
2. **Hot Streak** — New: Fireball/Scorch/Fire Blast crits stack -25% Pyroblast cast time (3 stacks) — a 1.5s Pyroblast after three crits. Raid sim (2026-09-28): the simulator's rotation reads this talent's own proc, so its removal run breaks the rotation and is not its value.
3. **Ignite** — 40% of crit damage as a burn (unchanged) — still the fire engine. Raid sim (2026-09-28): removing it costs +14% DPS.
4. **Fire Power** — +10% Fire damage. Raid sim (2026-09-28): removing it costs +10% DPS.
5. **Combustion** — Reworked: each Fire hit +10% crit until 4 crits. Raid sim (2026-09-28): removing it costs +9% DPS.
6. **Arcane Concentration** — Clearcasting. Raid sim (2026-09-28): removing it costs +9% DPS.
7. **Critical Mass** — +6% Fire crit. Raid sim (2026-09-28): removing it costs +6% DPS.
8. **Improved Fireball** — -0.5s Fireball (also Frostfire Bolt). Raid sim (2026-09-28): removing it costs +6% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Wake of Fire | any utility talent legal at that tier | Measures +0.5% DPS in the community simulator (noise): these points are free to move. |
| 5 | Burning Soul | Arcane Focus, any utility talent legal at that tier | Measures +0.1% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Wand Specialization, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Channeling | Magic Absorption, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 8** for `fire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`fire-raid`](fire-raid.md)** | ours: hand draft | 12/34/5 | 510 | +0.0% | 636 | +0.0% | 1 s |
| 2 | [`opt-fire-raid-raid-dps`](opt-fire-raid-raid-dps.md) | ours: optimizer | 14/32/5 | 510 | +0.0% | 636 | +0.0% | 1 s |
| 3 | *Fire DPS* | community simulator | - | 492 | -3.6% | 607 | -4.5% | 0 s |
| 4 | *Fire 0/35/16* | community simulator | - | 483 | -5.4% | 609 | -4.3% | 3 s |
| 5 | *Arcane DPS* | community simulator | - | 378 | -26.0% | 462 | -27.3% | 0 s |
| 6 | *Arcane 35/0/16* | community simulator | - | 273 | -46.5% | 338 | -46.8% | 1 s |
| 7 | *Frost DPS* | community simulator | - | 258 | -49.5% | 322 | -49.3% | 0 s |
| 8 | *Frost 14/0/37* | community simulator | - | 250 | -51.0% | 324 | -49.1% | 2 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: fire-raid 495 -> 534 DPS (+7.9%), sim preset: Fire 0/35/16 481 -> 520 DPS (+8.0%)):
  1. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+3.1%, pass 1)
  2. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.1%, pass 1)
  3. insert before the filler: if spell 44404 is up: cast Arcane Missiles (+0.2%, pass 1)
  4. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 8 changes to the base rotation; third-seed check: fire-raid 619 -> 665 DPS (+7.3%), sim preset: Fire 0/35/16 608 -> 653 DPS (+7.4%)):
  1. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+3.7%, pass 1)
  2. move to the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.5%, pass 1)
  3. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.2%, pass 1)
  4. only with 3s or more of the fight left: if mana % ≥ 10%: cast Fireball (+0.2%, pass 2)
  5. move to the top: cast Fire Blast (+0.2%, pass 2)
  6. threshold 5s -> 7.5s: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  7. insert before the filler: cast Blast Wave (+0.3%, pass 3)
  8. insert before the filler: cast Cone of Cold (+0.3%, pass 3)

| # | Priority (the first line whose condition holds is cast) | [`fire-raid`](fire-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch | 4.1 |
| 2 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 5 | if stacks of Hot Streak = 3: cast Pyroblast | 1.4 |
| 6 | cast Fire Blast | 7.4 |
| 7 | if mana % ≥ 10%: cast Fireball | 10.5 |
| 8 | if Missile Barrage is up: cast Arcane Missiles | 0.3 |
| 9 | cast Scorch | 3.3 |

Damage by ability:

| Ability | [`fire-raid`](fire-raid.md) |
|---|---|
| Fireball | 46% |
| Fire Blast | 21% |
| Ignite | 11% |
| Scorch | 10% |
| Pyroblast | 10% |
| Arcane Missiles | 1% |

## Notes

- Adopted from the community simulator on 2026-09-28: `cand-fire-raid-r5` beat the previous draft by +2.7% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Scorch to 5 stacks -> Fireball -> Pyroblast at 3 Hot Streak stacks (if a 1.5s Pyroblast beats a Fireball) -> Fire Blast on the move.
- Fire immunity in the new raids is unknown; in Classic this build was AQ40/Naxx only.
- 2026-09-27 scenario audit: Magic Absorption 2, Arcane Resilience 1 -> Burning Soul 1, Wake of Fire 2. Arcane Resilience (armor) and Magic Absorption (resistances) only matter when you are hit; a raid caster is not. Wake of Fire measures +0.9% in the simulator on the optimizer build (ElliotWood/Forever 40be98e) and Burning Soul's third rank lowers Fire threat further.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Magic Absorption -> Improved Channeling (interrupt); Magic Absorption -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Arcane Focus -> Improved Channeling (interrupt); Arcane Focus -> Arcane Subtlety (threat); Arcane Focus -> Arcane Subtlety (threat); Arcane Focus -> Burning Soul (threat); Arcane Focus -> Burning Soul (threat). Net -0.10% on a third seed.

## Open questions (verify in the live game)

- Does a 3-stack Hot Streak Pyroblast (1.5s cast) beat Fireball per cast time? If yes, Pyroblast enters the rotation.
- Incineration (Scorch/Fire Blast/Arcane Blast crit) vs. Flame Throwing.
- Whether Arcane Meditation 3/3 (est. 51% regen while casting) is worth 5 Arcane filler points and 2 hit.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
