# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (raid-dps) — 30/8/13

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/8/13 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `raid-dps`: score +71.3% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards and reduces the cooldown of Totemic Projection by 10 sec. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Enhancement (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ancestral Knowledge** | 3/5 | changed | Increases your Intellect by 6%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |

### Restoration (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Tidal Focus** | 5/5 | changed | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |
| **Mindfulness** | 3/3 | **NEW** | Allows 50% of your Mana regeneration to continue while casting. |
| **Totemic Focus** | 5/5 | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |

## Core talents (priority order)

1. **Elemental Alacrity** — Removing it costs 29.5 points of score in this model.
2. **Elemental Fury** — Removing it costs 15.5 points of score in this model.
3. **Tidal Focus** — Removing it costs 10.8 points of score in this model.
4. **Thundering Strikes** — Removing it costs 6.9 points of score in this model.
5. **Concussion** — Removing it costs 6.8 points of score in this model.
6. **Call of Flame** — Removing it costs 6.1 points of score in this model.
7. **Lightning Overload** — Removing it costs 4.9 points of score in this model.
8. **Mindfulness** — Removing it costs 4.5 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 6** for `elemental-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`elemental-raid-dps`](elemental-raid-dps.md) | ours: hand draft | 29/22/0 | 375 | +0.0% | 515 | +0.0% | 0 s |
| 2 | **[`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md)** | ours: optimizer | 31/7/13 | 357 | -4.8% | 508 | -1.4% | 0 s |
| 3 | [`elemental-raid`](elemental-raid.md) | ours: generated | 31/7/13 | 357 | -4.8% | 508 | -1.4% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if number of targets = 1 and not Searing Totem is on the target and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if not Flame Shock is on the target: cast Flame Shock | 4.9 |
| 4 | cast Lava Burst (rank 3) | 4.7 |
| 5 | if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning | 2.3 |
| 6 | if mana ≥ (time left in the fight × 26.25): cast Lightning Bolt (rank 7) | 14.6 |
| 7 | cast Lightning Bolt (rank 2) | 6.4 |

Lines of the simulator's rotation these builds never cast: cast Magma Totem (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) |
|---|---|
| Lightning Bolt | 47% |
| Lava Burst | 20% |
| Flame Shock | 19% |
| Attack | 7% |
| Chain Lightning | 6% |

## Notes

- Report: shaman/research/talents/forever/optimizer/elemental-dps-raid-dps.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 31/7/13 -> 30/8/13; Call of Thunder 1 gone; refill +1 Ancestral Knowledge (refill: the elemental-dps model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
