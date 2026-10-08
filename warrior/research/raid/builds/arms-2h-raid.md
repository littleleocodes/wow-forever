# Fury — Two-Handed (Improved Slam / Bloodthrill) — 19/32/0

*[Warrior](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 19/32/0 (Arms / Fury / Protection) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `fury-2h-raid` |

## Summary

Allocation adopted on 2026-09-26 from `opt-arms-2h-raid-raid-dps`, the best build in the community simulator (+8.5% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Improved Slam moved from Fury to Arms tier 6 and no longer resets the swing timer, so the two-hander build becomes an Arms build: Mortal Strike, Weaponmaster (crit/armor/extra attacks by weapon type), Bloodthrill (Overpower procs from Rend) and Improved Slam, with Cruelty, Unbridled Wrath and Improved Execute from Fury. Replaces the Classic 2H Fury/Bloodthirst build, which can no longer reach Improved Slam.

## Point allocation

### Arms (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | unchanged | Increases your Parry chance by 3%. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Tactical Mastery** | 5/5 | **NEW** | Tactical Mastery lets you retain up to an additional 15 Rage when you change stances. |
| **Anger Management** | 1/1 | changed | Generates 1 Rage every 3 sec while in combat, and reduces Rage loss while out of combat by 30%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 3%. |
| **Impale** | 1/2 | changed | Increases the critical strike damage bonus of your abilities by 10%. |

### Fury (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Booming Voice** | 5/5 | changed | Increases the area of effect of your Shouts by 50% and reduces their Rage cost by 25%. |
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Lingering Rage** | 3/5 | changed | Increases the time before your Rage begins to decay after leaving combat by 6 sec. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |
| **Improved Execute** | 2/2 | changed | Reduces the Rage cost of your Execute ability by 5. |
| **Death Wish** | 1/1 | changed | When activated, increases your Physical damage done by 20% and makes you immune to Fear effects, but increases all damage you take by 5%. Lasts 30 sec. |
| **Flurry** | 5/5 | changed | Increases your melee attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Bloodthirst** | 1/1 | changed | Instantly attack the target causing damage equal to 45% of your Attack Power plus 30 and increasing your movement speed by 10% for 10 sec. |

### Protection (0)

*No points.*

## Core talents (priority order)

1. **Flurry** — Raid sim (2026-09-26): removing it costs +12% DPS.
2. **Cruelty** — +5% crit. Raid sim (2026-09-26): removing it costs +9% DPS.
3. **Bloodthirst** — Raid sim (2026-09-26): removing it costs +9% DPS.
4. **Death Wish** — Raid sim (2026-09-26): removing it costs +6% DPS.
5. **Deep Wounds** — Bleed on crit; two-handers make it hit hard. Raid sim (2026-09-26): removing it costs +5% DPS.
6. **Precision** — Raid sim (2026-09-26): removing it costs +4% DPS.
7. **Improved Execute** — Raid sim (2026-09-26): removing it costs +3% DPS.
8. **Two-Handed Weapon Specialization** — Now 3 ranks (+3% est.). Raid sim (2026-09-26): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Impale | any utility talent legal at that tier | Measures +0.6% DPS in the community simulator (noise): these points are free to move. |
| 3 | Deflection | Improved Heroic Strike, any utility talent legal at that tier | Measures +0.4% DPS in the community simulator (noise): these points are free to move. |
| 3 | Improved Rend | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 5 | Improved Tactical Mastery | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Booming Voice | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 3 | Booming Voice | Boundless Rage, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 5 | Enrage | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**2 of 5** for `arms-2h-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-arms-2h-raid-raid-dps`](opt-arms-2h-raid-raid-dps.md) | ours: optimizer | 20/31/0 | 347 | +0.0% | 733 | +0.0% | 0 s |
| 2 | **[`arms-2h-raid`](arms-2h-raid.md)** | ours: hand draft | 19/32/0 | 344 | -0.9% | 725 | -1.1% | 0 s |
| 3 | *DPS* | community simulator | - | 329 | -5.1% | 692 | -5.6% | 0 s |
| 4 | *Fury 17/34/0* | community simulator | - | 324 | -6.6% | 689 | -6.1% | 0 s |
| 5 | *Arms 39/12/0* | community simulator | - | 302 | -12.9% | 655 | -10.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-08, 18 changes to the base rotation; third-seed check: open winner 302 -> 367 DPS (+21.3%), opt-arms-2h-raid-raid-dps 299 -> 372 DPS (+24.5%), sim preset: DPS 280 -> 341 DPS (+22.0%), arms-2h-raid 296 -> 357 DPS (+20.7%)):
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
  12. show the hidden: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s: cast Berserker Rage (+0.8%, pass 5)
  13. threshold 140s -> 70s: if (time left in the fight ≤ 25.5s or time left in the fight ≥ 140s): use every other cooldown when ready (+0.7%, pass 5)
  14. drop the condition: if number of targets > 1: cast Whirlwind (+0.2%, pass 5)
  15. drop the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s: cast Berserker Rage (+0.4%, pass 5)
  16. move to the top: if not Battle Shout is up: cast Battle Shout + move to the top: cast Berserker Rage (+0.5%, pass 5)
  17. insert in the middle: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor + threshold 1 -> 3: if stacks of Sunder Armor < 1 and not Expose Armor is up: cast Sunder Armor (+2.0%, pass 5)
  18. threshold 3 -> 4: if stacks of Sunder Armor < 3 and not Expose Armor is up: cast Sunder Armor (+0.5%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-08, 9 changes to the base rotation; third-seed check: open winner 667 -> 804 DPS (+20.6%), opt-arms-2h-raid-raid-dps 659 -> 799 DPS (+21.2%), sim preset: DPS 618 -> 750 DPS (+21.3%), arms-2h-raid 653 -> 790 DPS (+20.9%)):
  1. drop: if false: cast Recklessness (+12.7%, pass 1)
  2. drop: if number of targets = 1 and (rage ≥ 40 or execute phase (E20)): cast Heroic Strike (+5.3%, pass 1)
  3. drop: if not Battle Shout is up: cast Battle Shout (+1.0%, pass 1)
  4. drop the condition: if time until Bloodthirst is ready > 1.5s: cast Whirlwind (+0.4%, pass 1)
  5. drop the condition: if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring (+6.8%, pass 5)
  6. drop 'time left in the fight ≥ 140s' from the condition: if (time left in the fight ≤ 30s or time left in the fight ≥ 140s): use every other cooldown when ready (+1.0%, pass 5)
  7. threshold 30s -> 45s: if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish (+0.7%, pass 5)
  8. threshold 30s -> 45s: if time left in the fight ≤ 30s: use every other cooldown when ready (+0.3%, pass 5)
  9. move to the top: cast Bloodthirst (+0.3%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`arms-2h-raid`](arms-2h-raid.md) casts/min |
|---|---|---|
| 1 | if not Battle Shout is up: cast Battle Shout | 0.3 |
| 2 | if execute phase (E20): cast Execute | 4.7 |
| 3 | cast Goblin Sapper Charge | as ready |
| 4 | cast Dense Dynamite | as ready |
| 5 | if (time left in the fight ≤ 30s or time left in the fight ≥ 211.5s): cast Death Wish | 0.3 |
| 6 | if (time left in the fight ≤ 20s or time left in the fight ≥ 140s): cast Potion | as ready |
| 7 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Earthstrike | as ready |
| 8 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 9 | if stacks of Sunder Armor < 4 and not Expose Armor is up: cast Sunder Armor | 5.9 |
| 10 | if (time left in the fight ≤ 30s or time left in the fight ≥ 130s): cast Slayer's Crest | as ready |
| 11 | if (time left in the fight ≤ 25.5s or time left in the fight ≥ 70s): use every other cooldown when ready | as ready |
| 12 | cast Whirlwind | 3.7 |
| 13 | cast Bloodthirst | 5.3 |
| 14 | cast Death Wish | 0.3 |
| 15 | cast Whirlwind | 3.7 |
| 16 | if time until Bloodthirst is ready > 1.5s and time until Whirlwind is ready > 1.5s and rage > 80: cast Hamstring | 0.1 |
| 17 | if stacks of Sunder Armor < 5: cast Sunder Armor | 5.9 |

Lines of the simulator's rotation these builds never cast: cast Berserker Rage, cast Blood Fury, cast Diamond Flask, cast Jom Gabbar, cast Cleave, cast Berserker Stance (its condition never held in these fights); cast Mortal Strike (needs the Mortal Strike talent); cast Spearing Strike (needs the Spearing Strike talent).

Damage by ability:

| Ability | [`arms-2h-raid`](arms-2h-raid.md) |
|---|---|
| Auto Attack | 50% |
| Bloodthirst | 17% |
| Execute | 15% |
| Whirlwind | 10% |
| Deep Wound | 7% |
| Dragonbreath Chili | 0% |
| Hamstring | 0% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-arms-2h-raid-raid-dps beat the previous draft by +8.5% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Rend up -> Mortal Strike on cooldown -> Overpower when Bloodthrill procs -> Slam filler -> Heroic Strike when rage-capped.
- This is a Battle Stance build; Sweeping Strikes is both the cleave and the Mortal Strike prerequisite.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Boundless Rage -> Booming Voice (range); Boundless Rage -> Booming Voice (range); Boundless Rage -> Booming Voice (range); Improved Heroic Strike -> Deflection (survival); Improved Heroic Strike -> Deflection (survival); Improved Heroic Strike -> Deflection (survival). Net +0.00% on a third seed.
- 2026-09-30: renamed from "Arms — Two-Handed / Improved Slam / Bloodthrill (simulator winner adopted 2026-09-26)" so the name matches the spec the pages file it under (the point split decides the spec, spec_modes.py).
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Precision 3 out; Lingering Rage 3 in; to be re-optimized.

## Open questions (verify in the live game)

- Does Improved Slam really remove the swing reset at rank 1 (demo text says so)? If yes Slam may be the primary filler.
- Weaponmaster proc/crit values at max rank; which weapon type wins.
- Whether a Bloodthirst dual-wield build still out-damages this — Classic history says DW wins with hit and weapon skill, but Improved Slam's rework may change that.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
