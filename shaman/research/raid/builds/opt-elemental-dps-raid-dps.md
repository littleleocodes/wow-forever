# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (raid-dps) — 31/7/13

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/7/13 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `raid-dps`: score +71.3% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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
| **Eye of the Storm** | 3/3 | changed | Reduces the pushback suffered from damaging attacks while casting Lightning Bolt, Chain Lightning, and Lava Burst by 70%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Reach** | 1/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards, and increases the range of your Flame Shock spell by 8 yards. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 150 to 192 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |

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

1. **Elemental Alacrity** — Removing it costs 29.5 points of score in this model.
2. **Elemental Fury** — Removing it costs 15.5 points of score in this model.
3. **Tidal Focus** — Removing it costs 10.8 points of score in this model.
4. **Thundering Strikes** — Removing it costs 6.9 points of score in this model.
5. **Concussion** — Removing it costs 6.8 points of score in this model.
6. **Call of Flame** — Removing it costs 6.1 points of score in this model.
7. **Lightning Overload** — Removing it costs 4.9 points of score in this model.
8. **Mindfulness** — Removing it costs 4.5 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 6** for `elemental-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`elemental-raid-dps`](elemental-raid-dps.md) | ours: hand draft | 29/22/0 | 410 | +0.0% | 524 | +0.0% | 0 s |
| 2 | **[`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md)** | ours: optimizer | 31/7/13 | 408 | -0.3% | 518 | -1.1% | 0 s |
| 3 | [`elemental-raid`](elemental-raid.md) | ours: hand draft | 31/7/13 | 408 | -0.3% | 518 | -1.1% | 0 s |
| 4 | *Elemental 31/6/14* | community simulator | - | 404 | -1.5% | 514 | -1.9% | 0 s |
| 5 | *Stormcaller 28/23/0* | community simulator | - | 393 | -4.0% | 506 | -3.5% | 0 s |
| 6 | *Level 60* | community simulator | - | 389 | -5.1% | 495 | -5.6% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 4 changes to the base rotation; third-seed check: deep: Elemental (dummy) 423 -> 441 DPS (+4.2%), deep: Elemental (raid) 423 -> 441 DPS (+4.2%), deep: Hybrid Elemental/Enhancement (dummy) 426 -> 438 DPS (+2.7%), opt-elemental-dps-raid-dps 423 -> 440 DPS (+3.8%), sim preset: Elemental 31/6/14 416 -> 435 DPS (+4.6%), elemental-raid-dps 426 -> 437 DPS (+2.6%)):
  1. always rank 2 instead of rank 4: cast Lightning Bolt (+5.2%, pass 1)
  2. only with 20s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  3. always rank 8 instead of rank 10: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.3%, pass 1)
  4. always rank 7 instead of rank 8: if mana ≥ (time left in the fight × 35): cast Lightning Bolt + threshold 35 -> 26.25: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 3 changes to the base rotation; third-seed check: deep: Elemental (dummy) 554 -> 556 DPS (+0.3%), deep: Elemental (raid) 554 -> 556 DPS (+0.3%), deep: Hybrid Elemental/Enhancement (dummy) 555 -> 555 DPS (+0.0%), opt-elemental-dps-raid-dps 553 -> 554 DPS (+0.1%), sim preset: Elemental 31/6/14 547 -> 549 DPS (+0.3%), elemental-raid-dps 555 -> 555 DPS (+0.0%)):
  1. only with 10s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  2. always rank 2 instead of rank 4: cast Lightning Bolt (+0.4%, pass 1)
  3. threshold 100 -> 200: if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning (+0.2%, pass 2)

Before the pull: at -2s: cast Lightning Bolt.

| # | Priority (the first line whose condition holds is cast) | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if number of targets = 1 and not Searing Totem is on the target and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if not Flame Shock is on the target: cast Flame Shock | 5.0 |
| 4 | cast Lava Burst | 4.7 |
| 5 | if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning | 2.3 |
| 6 | if mana ≥ (time left in the fight × 26.25): cast Lightning Bolt | 14.4 |
| 7 | cast Lightning Bolt | 6.7 |

Lines of the simulator's rotation these builds never cast: cast Magma Totem (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) |
|---|---|
| Lightning Bolt | 54% |
| Lava Burst | 17% |
| Flame Shock | 17% |
| Attack | 7% |
| Chain Lightning | 5% |

## Notes

- Report: shaman/research/talents/forever/optimizer/elemental-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
