# Beast-Survival — Raid (open talent search) — 16/11/24

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/11/24 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast-Survival (a Beast Mastery/Survival hybrid) raid build: the best Summon Hawk + Expose Prey family of the melee-dps open search (raidsim/family_search.py: every pair of keystones of two trees polished by a short hill climb), raced again on 2026-11-18 in a full raid (every raid buff and debuff) on the current simulator by the hybrid check: 804.6 DPS, +8.9% against melee-survival-raid, the best of our builds in that rotation.

## Point allocation

### Beast Mastery (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
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
| **Deflection** | 3/5 | unchanged | Increases your Parry chance by 3%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 1/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |

## Rank among our builds and the community simulator's

**4 of 6** for `melee-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 363 | +0.0% | 737 | -8.1% | 0 s |
| 2 | [`survival-raid`](survival-raid.md) | ours: derived (simulator search) | 5/16/30 | 346 | -4.7% | 711 | -11.3% | 0 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 317 | -12.7% | 694 | -13.4% | 0 s |
| 4 | **[`beast-survival-open-raid`](beast-survival-open-raid.md)** | ours: derived (open search) | 16/11/24 | 269 | -25.9% | 802 | +0.0% | 121 s |
| 5 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 262 | -27.8% | 703 | -12.3% | 97 s |
| 6 | *SV Melee* | community simulator | - | 231 | -36.6% | 678 | -15.4% | 120 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 17 passes, the last 2026-11-10, 7 changes to the base rotation; third-seed check: melee-survival-raid 497 -> 752 DPS (+51.3%), sim preset: SV Melee 381 -> 623 DPS (+63.3%), opt-melee-dps-raid-dps 497 -> 703 DPS (+41.3%), survival-raid 467 -> 705 DPS (+50.9%), survival-ml-parse 474 -> 714 DPS (+50.5%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)
  3. move down below 'cast Strider Kick': if auraIsInactive: cast Summon Hawk (+0.3%, pass 10)
  4. move to the top: cast Raptor Strike (+0.3%, pass 10)
  5. move to the top: cast Explosive Trap (+0.6%, pass 12)
  6. only above 60% mana: cast Explosive Trap (+0.2%, pass 13)
  7. only with 20s or more of the fight left: if mana % ≥ 60%: cast Explosive Trap (+0.2%, pass 14)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`beast-survival-open-raid`](beast-survival-open-raid.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive: cast Summon Hawk | 3.5 |
| 2 | if auraIsInactive: cast Aspect of the Beast | 0.3 |
| 3 | cast Mongoose Bite | 2.0 |
| 4 | cast Raptor Strike | 2.9 |
| 5 | cast Immolation Trap | 1.3 |
| 6 | use every other cooldown when ready | as ready |
| 7 | cast Strider Kick | 2.0 |
| 8 | cast Major Mana Potion | as ready |
| 9 | cast Wing Clip | 8.9 |

Lines of the simulator's rotation these builds never cast: cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`beast-survival-open-raid`](beast-survival-open-raid.md) |
|---|---|
| Auto Attack | 61% |
| Immolation Trap | 10% |
| Pet: Auto Attack | 10% |
| Raptor Strike | 5% |
| Mongoose Bite | 4% |
| Summon Hawk | 4% |
| Strider Kick | 3% |
| Wing Clip | 3% |

## Notes

- Kept from the hybrid check (2026-11-18, `_reference/hybrid-check.md`): an open search writes one build per raid entry, filed under its winner's spec, and the melee-dps entry's winner was another spec's, so Beast-Survival had no raid build. This family passed the raid signature check (core share 64%).
- Simulator numbers are the community's model of the beta (wowsims/forever 2e6e77d (client 70938) with this project's patches), not in-game measurements.
- 2026-11-19 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Revive Pet -> Endurance Training (survival); Improved Wing Clip -> Deflection (survival); Improved Wing Clip -> Deflection (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Beast-Survival build: check it against the community's Beast-Survival builds at launch.

## Sources

- <https://talentsforever.com/hunter/60/54001005001-005005001-5102022300500121-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
