# Beast-Survival — Raid (open talent search) — 16/11/24

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/11/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) raid build the open talent search found on 2026-10-09: every legal 51-point build with no tree rule, searched in the community simulator's melee-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Beast Mastery (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |
| **Improved Aspect of the Monkey** | 3/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |

### Marksmanship (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Survivalist's Discipline** | 1/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 20%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |

## Core talents (priority order)

1. **Lone Wolf** — 172 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
2. **Predator's Edge** — 114 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Expose Prey** — 97 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
4. **Deadly Aspects** — 85 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
5. **Careful Aim** — 59 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Strider Kick** — 54 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Summon Hawk** — 53 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Lethal Attacks** — 50 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 5** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: derived (simulator search) | 5/16/30 | 488 | +0.0% | 987 | -2.9% | 9 s |
| 2 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 466 | -4.5% | 1007 | -1.0% | 44 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 465 | -4.8% | 975 | -4.1% | 8 s |
| 4 | **[`beast-survival-open-raid`](beast-survival-open-raid.md)** | ours: derived (open search) | 16/11/24 | 360 | -26.3% | 1017 | +0.0% | 127 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 360 | -26.3% | 959 | -5.7% | 117 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 8 passes, the last 2026-10-05, 9 changes to the base rotation; third-seed check: open winner 298 -> 363 DPS (+21.9%), survival-raid 313 -> 445 DPS (+42.1%), melee-survival-raid 319 -> 423 DPS (+32.5%), opt-melee-dps-raid-dps 319 -> 426 DPS (+33.2%)):
  1. insert before the filler: cast Wing Clip (+7.4%, pass 1)
  2. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+14.3%, pass 2)
  3. insert in the middle: cast Major Mana Potion (+0.4%, pass 3)
  4. move to the top: cast Immolation Trap (+0.5%, pass 3)
  5. move to the top: cast Raptor Strike (+0.3%, pass 3)
  6. move down below 'cast Strider Kick': cast Major Mana Potion (+0.4%, pass 4)
  7. move to the top: cast Mongoose Bite (+0.2%, pass 4)
  8. move to the top: cast Aspect of the Beast (+0.2%, pass 4)
  9. move to the top: if auraIsInactive: cast Summon Hawk (+0.3%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 10 passes, the last 2026-10-09, 4 changes to the base rotation; third-seed check: beast-survival-open-raid 736 -> 1057 DPS (+43.6%), melee-survival-raid 764 -> 1048 DPS (+37.1%), opt-melee-dps-raid-dps 764 -> 1017 DPS (+33.1%), survival-raid 749 -> 1028 DPS (+37.3%), survival-ml-parse 729 -> 999 DPS (+37.1%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)
  3. move down below 'cast Strider Kick': if auraIsInactive: cast Summon Hawk (+0.3%, pass 10)
  4. move to the top: cast Raptor Strike (+0.3%, pass 10)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`beast-survival-open-raid`](beast-survival-open-raid.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive: cast Summon Hawk | 3.7 |
| 2 | cast Aspect of the Beast | 0.3 |
| 3 | cast Mongoose Bite | 3.6 |
| 4 | cast Raptor Strike | 10.9 |
| 5 | cast Immolation Trap | 1.0 |
| 6 | use every other cooldown when ready | as ready |
| 7 | cast Strider Kick | 2.2 |
| 8 | cast Major Mana Potion | as ready |
| 9 | cast Wing Clip | 6.3 |

Lines of the simulator's rotation these builds never cast: cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`beast-survival-open-raid`](beast-survival-open-raid.md) |
|---|---|
| Auto Attack | 55% |
| Raptor Strike | 12% |
| Mongoose Bite | 10% |
| Summon Hawk | 9% |
| Immolation Trap | 5% |
| Strider Kick | 4% |
| Dragonbreath Chili | 3% |
| Wing Clip | 2% |

## Notes

- Open search result (melee-dps, full raid): 16/11/24 (Beast-Survival (a Beast Mastery/Survival hybrid)) at 1050.7 DPS; melee-survival-raid 1047.8, survival-raid 1028.2, opt-melee-dps-raid-dps 1016.6, survival-ml-parse 998.8 in the same fights; 8,204 builds simulated, 3 independent runs reached the top.
- Sibling rotations tried on it (10,000 fights): mm-raid -53.6%, mm-lonewolf-raid -54.0%, bm-raid -53.3%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Endurance Training, Improved Aspect of the Monkey, Survivalist.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Hybrid Beast Mastery/Survival: its full-raid winner is +0.00% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- An open-search Beast-Survival build: check it against the community's Beast-Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/hunter/60/52030005001-005005001-5002302300500211-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
