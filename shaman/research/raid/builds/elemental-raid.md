# Elemental — Raid (generated) — 30/8/13

*[Shaman](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/8/13 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The best Elemental raid build with at least 30 points in Elemental, generated on 2026-09-29 by spec_builds.py: the stats model's optimum (elemental-dps, profile raid-dps), refined in the community simulator's talent search (elemental-dps). No hand draft exists for this spec and mode yet; treat it as a starting point.

## Point allocation

### Elemental (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 70% chance to not lose casting time when you take damage. |
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

1. **Elemental Alacrity** — The scorer's value in this build: +41.1% of its score (model elemental-dps).
2. **Elemental Fury** — The scorer's value in this build: +21.2% of its score (model elemental-dps).
3. **Tidal Focus** — The scorer's value in this build: +12.0% of its score (model elemental-dps).
4. **Thundering Strikes** — The scorer's value in this build: +9.5% of its score (model elemental-dps).
5. **Concussion** — The scorer's value in this build: +9.4% of its score (model elemental-dps).
6. **Call of Flame** — The scorer's value in this build: +8.2% of its score (model elemental-dps).

## Rank among our builds and the community simulator's

**4 of 4** for `elemental-dps` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Standard* | community simulator | - | 507 | +0.0% | 602 | -2.8% | 1 s |
| 2 | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) | ours: optimizer | 31/11/9 | 506 | -0.3% | 603 | -2.6% | 2 s |
| 3 | [`elemental-raid-dps`](elemental-raid-dps.md) | ours: hand draft | 29/22/0 | 497 | -2.0% | 619 | +0.0% | 9 s |
| 4 | **[`elemental-raid`](elemental-raid.md)** | ours: generated | 30/8/13 | 484 | -4.5% | 586 | -5.3% | 7 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 7 passes, the last 2026-10-03, 4 changes to the base rotation; third-seed check: deep: Elemental (dummy) 423 -> 441 DPS (+4.2%), deep: Elemental (raid) 423 -> 441 DPS (+4.2%), deep: Hybrid Elemental/Enhancement (dummy) 426 -> 438 DPS (+2.7%), opt-elemental-dps-raid-dps 423 -> 440 DPS (+3.8%), sim preset: Elemental 31/6/14 416 -> 435 DPS (+4.6%), elemental-raid-dps 426 -> 437 DPS (+2.6%)):
  1. always rank 2 instead of rank 4: cast Lightning Bolt (+5.2%, pass 1)
  2. only with 20s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  3. always rank 8 instead of rank 10: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.3%, pass 1)
  4. always rank 7 instead of rank 8: if mana ≥ (time left in the fight × 35): cast Lightning Bolt + threshold 35 -> 26.25: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-26, 8 changes to the base rotation; third-seed check: open winner 618 -> 622 DPS (+0.7%), elemental-raid-dps 616 -> 619 DPS (+0.5%), sim preset: Standard 596 -> 602 DPS (+1.1%), opt-elemental-dps-raid-dps 597 -> 603 DPS (+1.1%), elemental-raid 583 -> 586 DPS (+0.5%)):
  1. only with 10s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  2. always rank 2 instead of rank 4: cast Lightning Bolt (+0.4%, pass 1)
  3. threshold 100 -> 200: if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning (+0.2%, pass 2)
  4. drop the condition: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+1.4%, pass 8)
  5. threshold 0s -> 1s: if number of targets = 1 and time left on the totem ≤ 0s and time left in the fight ≥ 10s: cast Searing Totem (+0.2%, pass 9)
  6. insert in the middle: if mana % < 80%: cast ResourcePotion (+0.2%, pass 9)
  7. move down below 'if not Flame Shock is on the target: cast Flame Shock': use every other cooldown when ready (+0.2%, pass 9)
  8. drop 'Clearcasting is up' from the condition: if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 200)): cast Chain Lightning (+0.3%, pass 10)

Before the pull: at -2s: cast Lightning Bolt.

| # | Priority (the first line whose condition holds is cast) | [`elemental-raid`](elemental-raid.md) casts/min |
|---|---|---|
| 1 | if number of targets = 1 and time left on the totem ≤ 0s and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if not Flame Shock is on the target: cast Flame Shock | 3.1 |
| 4 | cast Lava Burst (rank 3) | 4.6 |
| 5 | if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning | 2.1 |
| 6 | if mana ≥ (time left in the fight × 26.25): cast Lightning Bolt (rank 8) | 20.1 |
| 7 | cast Lightning Bolt (rank 8) | 20.1 |

Lines of the simulator's rotation these builds never cast: cast Magma Totem (its condition never held in these fights).

Damage by ability:

| Ability | [`elemental-raid`](elemental-raid.md) |
|---|---|
| Lightning Bolt | 55% |
| Lava Burst | 19% |
| Flame Shock | 14% |
| Searing Totem | 6% |
| Chain Lightning | 4% |
| Demonic Rune | 2% |

## Notes

- Generated 2026-09-29 (spec_builds.py) so every spec has a raid build; model elemental-dps, profile raid-dps.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Elemental Devastation -> Eye of the Storm (interrupt); Elemental Warding -> Eye of the Storm (interrupt); Elemental Warding -> Eye of the Storm (interrupt); Elemental Warding -> Elemental Reach (range). Net +0.00% on a third seed.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Elemental: its full-raid winner is +0.02% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 31/7/13 -> 30/8/13; Call of Thunder 1 gone; refill +1 Ancestral Knowledge (refill: the elemental-dps model, raid-dps).

## Open questions (verify in the live game)

- A generated Elemental build: check it against the community's Elemental builds at launch.

## Sources

- <https://talentsforever.com/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
