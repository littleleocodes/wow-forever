# Elemental — Raid (generated) — 31/7/13

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/7/13 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The best Elemental raid build with at least 30 points in Elemental, generated on 2026-09-29 by spec_builds.py: the stats model's optimum (elemental-dps, profile raid-dps), refined in the community simulator's talent search (elemental-dps). No hand draft exists for this spec and mode yet; treat it as a starting point.

## Point allocation

### Elemental (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Call of Thunder** | 1/1 | changed | Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 3%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 150 to 192 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards, and increases the range of your Flame Shock spell by 8 yards. |

### Enhancement (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 2/5 | changed | Increases your Intellect by 4%. |

### Restoration (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |

## Core talents (priority order)

1. **Elemental Alacrity** — The scorer's value in this build: +41.1% of its score (model elemental-dps).
2. **Elemental Fury** — The scorer's value in this build: +21.2% of its score (model elemental-dps).
3. **Tidal Focus** — The scorer's value in this build: +12.0% of its score (model elemental-dps).
4. **Thundering Strikes** — The scorer's value in this build: +9.5% of its score (model elemental-dps).
5. **Concussion** — The scorer's value in this build: +9.4% of its score (model elemental-dps).
6. **Call of Flame** — The scorer's value in this build: +8.2% of its score (model elemental-dps).

## Rank among our builds and the community simulator's

**3 of 6** for `elemental-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`elemental-raid-dps`](elemental-raid-dps.md) | ours: hand draft | 29/22/0 | 375 | +0.0% | 515 | +0.0% | 0 s |
| 2 | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) | ours: optimizer | 31/7/13 | 357 | -4.8% | 508 | -1.4% | 0 s |
| 3 | **[`elemental-raid`](elemental-raid.md)** | ours: generated | 31/7/13 | 357 | -4.8% | 508 | -1.4% | 0 s |
| 4 | *Elemental 31/6/14* | community simulator | - | 334 | -11.0% | 500 | -2.9% | 0 s |
| 5 | *Level 60* | community simulator | - | 332 | -11.5% | 485 | -5.8% | 0 s |
| 6 | *Stormcaller 28/23/0* | community simulator | - | 304 | -19.1% | 477 | -7.5% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 4 changes to the base rotation; third-seed check: deep: Elemental (dummy) 423 -> 441 DPS (+4.2%), deep: Elemental (raid) 423 -> 441 DPS (+4.2%), deep: Hybrid Elemental/Enhancement (dummy) 426 -> 438 DPS (+2.7%), opt-elemental-dps-raid-dps 423 -> 440 DPS (+3.8%), sim preset: Elemental 31/6/14 416 -> 435 DPS (+4.6%), elemental-raid-dps 426 -> 437 DPS (+2.6%)):
  1. always rank 2 instead of rank 4: cast Lightning Bolt (+5.2%, pass 1)
  2. only with 20s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  3. always rank 8 instead of rank 10: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.3%, pass 1)
  4. always rank 7 instead of rank 8: if mana ≥ (time left in the fight × 35): cast Lightning Bolt + threshold 35 -> 26.25: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-09, 4 changes to the base rotation; third-seed check: elemental-raid-dps 517 -> 518 DPS (+0.1%), sim preset: Elemental 31/6/14 493 -> 503 DPS (+2.1%), opt-elemental-dps-raid-dps 509 -> 510 DPS (+0.3%)):
  1. only with 10s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  2. always rank 2 instead of rank 4: cast Lightning Bolt (+0.4%, pass 1)
  3. threshold 100 -> 200: if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning (+0.2%, pass 2)
  4. drop the condition: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+1.4%, pass 8)

Before the pull: at -2s: cast Lightning Bolt.

| # | Priority (the first line whose condition holds is cast) | [`elemental-raid`](elemental-raid.md) casts/min |
|---|---|---|
| 1 | if number of targets = 1 and not Searing Totem is on the target and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if not Flame Shock is on the target: cast Flame Shock | 4.9 |
| 4 | cast Lava Burst | 4.7 |
| 5 | if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning | 2.3 |
| 6 | if mana ≥ (time left in the fight × 26.25): cast Lightning Bolt (rank 7) | 14.6 |
| 7 | cast Lightning Bolt (rank 2) | 6.4 |

Lines of the simulator's rotation these builds never cast: cast Magma Totem (its condition never held in these fights).

Damage by ability:

| Ability | [`elemental-raid`](elemental-raid.md) |
|---|---|
| Lightning Bolt | 47% |
| Lava Burst | 20% |
| Flame Shock | 19% |
| Attack | 7% |
| Chain Lightning | 6% |

## Notes

- Generated 2026-09-29 (spec_builds.py) so every spec has a raid build; model elemental-dps, profile raid-dps.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Elemental Devastation -> Eye of the Storm (interrupt); Elemental Warding -> Eye of the Storm (interrupt); Elemental Warding -> Eye of the Storm (interrupt); Elemental Warding -> Elemental Reach (range). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- A generated Elemental build: check it against the community's Elemental builds at launch.

## Sources

- <https://talentsforever.com/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
