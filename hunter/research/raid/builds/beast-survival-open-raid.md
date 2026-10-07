# Beast-Survival — Raid (open talent search) — 16/11/24

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/11/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) raid build the open talent search found on 2026-10-07: every legal 51-point build with no tree rule, searched in the community simulator's melee-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +7.5% over melee-survival-raid, the best of our builds in that rotation.

## Point allocation

### Beast Mastery (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Improved Aspect of the Monkey** | 3/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |

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
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 5 sec. |
| **Survivalist's Discipline** | 1/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 20%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |

## Core talents (priority order)

1. **Lone Wolf** — 182 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
2. **Summon Hawk** — 122 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Predator's Edge** — 112 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
4. **Expose Prey** — 93 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
5. **Deadly Aspects** — 84 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
6. **Careful Aim** — 59 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Lethal Attacks** — 55 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Strider Kick** — 54 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**4 of 5** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: hand draft | 5/16/30 | 467 | +0.0% | 1070 | -8.6% | 9 s |
| 2 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 447 | -4.3% | 1062 | -9.2% | 8 s |
| 3 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 445 | -4.8% | 1086 | -7.1% | 44 s |
| 4 | **[`beast-survival-open-raid`](beast-survival-open-raid.md)** | ours: hand draft | 16/11/24 | 380 | -18.6% | 1170 | +0.0% | 126 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: parse build | 5/14/32 | 344 | -26.3% | 1036 | -11.5% | 117 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 8 passes, the last 2026-10-06, 2 changes to the base rotation; third-seed check: open winner 739 -> 1118 DPS (+51.4%), survival-raid 752 -> 1022 DPS (+35.9%), melee-survival-raid 767 -> 1040 DPS (+35.6%), opt-melee-dps-raid-dps 767 -> 1015 DPS (+32.4%), survival-ml-parse 767 -> 1040 DPS (+35.6%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`beast-survival-open-raid`](beast-survival-open-raid.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive: cast Summon Hawk | 3.7 |
| 2 | cast Aspect of the Beast | 0.3 |
| 3 | cast Mongoose Bite | 3.5 |
| 4 | cast Raptor Strike | 11.1 |
| 5 | cast Immolation Trap | 1.0 |
| 6 | use every other cooldown when ready | as ready |
| 7 | cast Strider Kick | 2.3 |
| 8 | cast Major Mana Potion | as ready |
| 9 | cast Wing Clip | 6.4 |

Lines of the simulator's rotation these builds never cast: cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`beast-survival-open-raid`](beast-survival-open-raid.md) |
|---|---|
| Auto Attack | 50% |
| Summon Hawk | 18% |
| Raptor Strike | 11% |
| Mongoose Bite | 9% |
| Immolation Trap | 4% |
| Strider Kick | 3% |
| Dragonbreath Chili | 3% |
| Wing Clip | 2% |

## Notes

- Open search result (melee-dps, full raid): 16/11/24 (Beast-Survival (a Beast Mastery/Survival hybrid)) at 1117.7 DPS; melee-survival-raid 1039.6, survival-ml-parse 1039.6, survival-raid 1021.7, opt-melee-dps-raid-dps 1015.4 in the same fights; 4,445 builds simulated, 2 independent runs reached the top.
- The melee-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): mm-raid -49.8%, mm-lonewolf-raid -49.6%, bm-raid -49.6%; none adopted.
- A phase-1 BiS set picked for this family (_reference/data/raidsim/gear_sets/forever/tiers/hunter-hybrid-beast-mastery-survival-bis.gear.json, item level 67.2): 1103.5 DPS against 1114.2 in the rotation's standard set: the standard set stays.
- The search ran before 2026-10-06, when the bench's target got a creature type (an Elemental): Improved Tracking measured 0 in it and is +5% damage against every raid creature type but Mechanical since (+4.9% for this build in a full raid). The search's numbers above are from that run; the page's numbers come from the re-race. Re-run the search (family_search.py --fresh) to value the talent in the search itself.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Focused Fire, Improved Aspect of the Monkey, Survivalist.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.
- 2026-10-07 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Focused Fire -> Endurance Training (survival); Focused Fire -> Endurance Training (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Beast-Survival build: check it against the community's Beast-Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/hunter/60/50230005001-005005001-5002302300500211-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
