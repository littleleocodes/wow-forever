# Optimizer — Lightning Bolt 60%, Chain Lightning 15%, Earth Shock 10%, Flame Shock 8%, fire totem 7%; Lava Burst via talent (raid-dps) — 29/22/0

*[Shaman](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/22/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `elemental-dps` and profile `raid-dps`: score +74.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Elemental (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Convection** | 5/5 | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Call of Flame** | 3/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%. |
| **Reverberation** | 1/5 | changed | Reduces the cooldown of your Shock spells by 0.2 sec. |
| **Elemental Warding** | 3/3 | changed | Reduces damage taken from Fire, Frost, and Nature effects by 10%. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Call of Thunder** | 1/1 | changed | Increases the critical strike chance of your Lightning Bolt and Chain Lightning spells by 3%. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 4/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 80%. |

### Enhancement (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5/5 | changed | Increases your Intellect by 10%. |
| **Improved Lightning Shield** | 3/3 | unchanged | Increases the damage done by your Lightning Shield orbs by 15%. |
| **Guardian Totems** | 1/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 10% and reduces the cooldown of your Grounding Totem by 1 sec. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Toughness** | 5/5 | changed | Increases your Stamina by 10%. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |

### Restoration (0)

*No points.*

## Core talents (priority order)

1. **Elemental Alacrity** — Removing it costs 30.5 points of score in this model.
2. **Mental Quickness** — Removing it costs 14.8 points of score in this model.
3. **Elemental Fury** — Removing it costs 12.9 points of score in this model.
4. **Concussion** — Removing it costs 7.0 points of score in this model.
5. **Thundering Strikes** — Removing it costs 6.5 points of score in this model.
6. **Call of Flame** — Removing it costs 6.2 points of score in this model.
7. **Lightning Overload** — Removing it costs 5.0 points of score in this model.
8. **Ancestral Knowledge** — Removing it costs 3.6 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 5** for `elemental-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`elemental-raid-dps`](elemental-raid-dps.md) | ours: hand draft | 29/22/0 | 397 | +0.0% | 504 | +0.0% | 0 s |
| 2 | **[`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md)** | ours: optimizer | 29/22/0 | 396 | -0.4% | 503 | -0.2% | 0 s |
| 3 | *Elemental 31/6/14* | community simulator | - | 393 | -1.0% | 498 | -1.3% | 0 s |
| 4 | *Stormcaller 28/23/0* | community simulator | - | 381 | -4.1% | 493 | -2.2% | 2 s |
| 5 | *Level 60* | community simulator | - | 379 | -4.5% | 477 | -5.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-elemental-dps-raid-dps 387 -> 397 DPS (+2.4%), sim preset: Elemental 31/6/14 378 -> 393 DPS (+4.1%)):
  1. always rank 2 instead of rank 4: cast Lightning Bolt (+5.2%, pass 1)
  2. only with 20s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  3. always rank 8 instead of rank 10: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.3%, pass 1)
  4. always rank 7 instead of rank 8: if mana ≥ (time left in the fight × 35): cast Lightning Bolt + threshold 35 -> 26.25: if mana ≥ (time left in the fight × 35): cast Lightning Bolt (+0.2%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-elemental-dps-raid-dps 495 -> 497 DPS (+0.3%), sim preset: Elemental 31/6/14 494 -> 497 DPS (+0.5%)):
  1. only with 10s or more of the fight left: if number of targets = 1 and not Searing Totem is on the target: cast Searing Totem (+0.5%, pass 1)
  2. always rank 2 instead of rank 4: cast Lightning Bolt (+0.4%, pass 1)
  3. threshold 100 -> 200: if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning (+0.2%, pass 2)

Before the pull: at -2s: cast Lightning Bolt.

| # | Priority (the first line whose condition holds is cast) | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if number of targets = 1 and not Searing Totem is on the target and time left in the fight ≥ 20s: cast Searing Totem | 1.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if not Flame Shock is on the target: cast Flame Shock | 5.3 |
| 4 | if (Clearcasting is up or number of targets ≥ 2 or mana ≥ (time left in the fight × 100)): cast Chain Lightning | 3.4 |
| 5 | if mana ≥ (time left in the fight × 26.25): cast Lightning Bolt | 22.9 |

Lines of the simulator's rotation these builds never cast: cast Magma Totem, cast Lightning Bolt (its condition never held in these fights); cast Lava Burst (needs the Lava Burst talent).

Damage by ability:

| Ability | [`opt-elemental-dps-raid-dps`](opt-elemental-dps-raid-dps.md) |
|---|---|
| Lightning Bolt | 69% |
| Flame Shock | 17% |
| Chain Lightning | 8% |
| Attack | 6% |

## Notes

- Report: shaman/talents/forever/optimizer/elemental-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/shaman>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
