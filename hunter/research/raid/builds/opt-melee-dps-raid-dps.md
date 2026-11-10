# Optimizer — Melee hunter (Forever): dual-wield white swings under Aspect of the Beast, Raptor Strike on the next swing, Mongoose Bite after dodges and Expose Prey procs, Strider Kick on cooldown, Counterattack after parries, the Lacerating Strikes bleed, one Serpent Sting from the pull (the 8 yd minimum range stops every other shot in melee), and the pet unless Lone Wolf (raid-dps) — 5/15/31

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/15/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `melee-dps` and profile `raid-dps`: score +126.0% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Core talents (priority order)

1. **Expose Prey** — Removing it costs 30.7 points of score in this model.
2. **Lone Wolf** — Removing it costs 19.8 points of score in this model.
3. **Deadly Aspects** — Removing it costs 19.4 points of score in this model.
4. **Predator's Edge** — Removing it costs 17.5 points of score in this model.
5. **Resourcefulness** — Removing it costs 15.6 points of score in this model.
6. **Careful Aim** — Removing it costs 11.8 points of score in this model.
7. **Strider Kick** — Removing it costs 10.7 points of score in this model.
8. **Improved Tracking** — Removing it costs 9.9 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 5** for `melee-dps` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 369 | +0.0% | 753 | +0.0% | 0 s |
| 2 | [`survival-raid`](survival-raid.md) | ours: derived (simulator search) | 5/16/30 | 345 | -6.5% | 705 | -6.3% | 0 s |
| 3 | **[`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md)** | ours: optimizer | 5/15/31 | 325 | -12.0% | 704 | -6.4% | 0 s |
| 4 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 267 | -27.7% | 714 | -5.1% | 98 s |
| 5 | *SV Melee* | community simulator | - | 216 | -41.6% | 623 | -17.3% | 120 s |

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

| # | Priority (the first line whose condition holds is cast) | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive: cast Aspect of the Beast | 0.3 |
| 2 | cast Mongoose Bite | 4.5 |
| 3 | cast Raptor Strike | 8.4 |
| 4 | cast Immolation Trap | 2.0 |
| 5 | use every other cooldown when ready | as ready |
| 6 | cast Strider Kick | 6.5 |
| 7 | cast Major Mana Potion | as ready |
| 8 | cast Wing Clip | 26.7 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) |
|---|---|
| Auto Attack | 49% |
| Raptor Strike | 13% |
| Immolation Trap | 10% |
| Strider Kick | 9% |
| Mongoose Bite | 8% |
| Wing Clip | 7% |
| Lacerating Strikes | 4% |

## Notes

- Report: hunter/research/talents/forever/optimizer/melee-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
