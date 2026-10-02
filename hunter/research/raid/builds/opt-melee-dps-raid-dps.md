# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (raid-dps) — 5/15/31

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/15/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `raid-dps`: score +123.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 4/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 12%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 5/5 | changed | Increases your total Health by 10%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your offhand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 5 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage over 21 sec equal to 40% of the damage done by Mongoose Bite. |

## Core talents (priority order)

1. **Expose Prey** — Removing it costs 29.5 points of score in this model.
2. **Deadly Aspects** — Removing it costs 19.2 points of score in this model.
3. **Lone Wolf** — Removing it costs 19.1 points of score in this model.
4. **Resourcefulness** — Removing it costs 15.6 points of score in this model.
5. **Predator's Edge** — Removing it costs 11.9 points of score in this model.
6. **Careful Aim** — Removing it costs 11.6 points of score in this model.
7. **Lightning Reflexes** — Removing it costs 10.3 points of score in this model.
8. **Strider Kick** — Removing it costs 10.2 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 4** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: hand draft | 5/16/30 | 450 | +0.0% | 967 | -2.4% | 12 s |
| 2 | **[`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md)** | ours: optimizer | 5/15/31 | 430 | -4.5% | 965 | -2.6% | 9 s |
| 3 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 426 | -5.3% | 991 | +0.0% | 47 s |
| 4 | [`survival-ml-parse`](survival-ml-parse.md) | ours: parse build | 5/14/32 | 347 | -22.9% | 991 | -0.0% | 119 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 3 passes, the last 2026-10-02, 5 changes to the base rotation; third-seed check: ml: Survival 318 -> 449 DPS (+41.5%)):
  1. insert before the filler: cast Wing Clip (+7.4%, pass 1)
  2. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+14.3%, pass 2)
  3. insert in the middle: cast Major Mana Potion (+0.4%, pass 3)
  4. move to the top: cast Immolation Trap (+0.5%, pass 3)
  5. move to the top: cast Raptor Strike (+0.3%, pass 3)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 3 passes, the last 2026-10-02, 2 changes to the base rotation; third-seed check: ml: Survival 713 -> 968 DPS (+35.9%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | cast Raptor Strike | 20.0 |
| 2 | cast Immolation Trap | 2.0 |
| 3 | cast Aspect of the Beast | 0.3 |
| 4 | use every other cooldown when ready | as ready |
| 5 | cast Mongoose Bite | 12.3 |
| 6 | cast Major Mana Potion | as ready |
| 7 | cast Strider Kick | 6.4 |
| 8 | cast Wing Clip | 24.5 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) |
|---|---|
| Auto Attack | 45% |
| Raptor Strike | 17% |
| Mongoose Bite | 15% |
| Strider Kick | 8% |
| Wing Clip | 6% |
| Immolation Trap | 6% |
| Dragonbreath Chili | 3% |

## Notes

- Report: hunter/talents/forever/optimizer/melee-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
