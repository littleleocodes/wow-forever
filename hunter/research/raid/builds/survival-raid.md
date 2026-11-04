# Survival — Raid (derived) — 5/16/30

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/16/30 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival raid damage build derived on 2026-09-30 (derive_raid.py): the community simulator's talent search (raidsim/talent_opt.py, entry melee-dps, training dummy) from the spec's best build opt-melee-dps-raid-dps, 30+ points kept in Survival.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 3/5 | changed | Increases your Agility by 9%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |

## Rank among our builds and the community simulator's

**2 of 5** for `melee-dps` by training-dummy DPS in the community simulator (wowsims/forever 7c3453f (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 359 | +0.0% | 734 | +0.0% | 0 s |
| 2 | **[`survival-raid`](survival-raid.md)** | ours: derived (simulator search) | 5/16/30 | 336 | -6.3% | 688 | -6.2% | 0 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 313 | -12.7% | 682 | -7.0% | 0 s |
| 4 | [`survival-ml-parse`](survival-ml-parse.md) | ours: derived (ML search) | 5/14/32 | 260 | -27.7% | 694 | -5.5% | 99 s |
| 5 | *SV Melee* | community simulator | - | 211 | -41.1% | 610 | -16.8% | 120 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 15 passes, the last 2026-11-04, 7 changes to the base rotation; third-seed check: melee-survival-raid 472 -> 733 DPS (+55.3%), sim preset: SV Melee 364 -> 606 DPS (+66.7%), opt-melee-dps-raid-dps 472 -> 682 DPS (+44.6%), survival-raid 447 -> 690 DPS (+54.2%), survival-ml-parse 450 -> 695 DPS (+54.4%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)
  3. move down below 'cast Strider Kick': if auraIsInactive: cast Summon Hawk (+0.3%, pass 10)
  4. move to the top: cast Raptor Strike (+0.3%, pass 10)
  5. move to the top: cast Explosive Trap (+0.6%, pass 12)
  6. only above 60% mana: cast Explosive Trap (+0.2%, pass 13)
  7. only with 20s or more of the fight left: if mana % ≥ 60%: cast Explosive Trap (+0.2%, pass 14)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`survival-raid`](survival-raid.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive: cast Aspect of the Beast | 0.3 |
| 2 | cast Mongoose Bite | 4.2 |
| 3 | cast Raptor Strike | 8.1 |
| 4 | cast Immolation Trap | 3.3 |
| 5 | use every other cooldown when ready | as ready |
| 6 | cast Strider Kick | 6.6 |
| 7 | cast Major Mana Potion | as ready |
| 8 | cast Wing Clip | 25.5 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`survival-raid`](survival-raid.md) |
|---|---|
| Auto Attack | 46% |
| Immolation Trap | 22% |
| Raptor Strike | 13% |
| Strider Kick | 8% |
| Wing Clip | 6% |
| Mongoose Bite | 6% |

## Notes

- About +3.3% over the hand draft melee-survival-raid (over the 2% replacement bar): this build is the spec's raid pick, the hand draft stays as the alternative.
- Simulator talent search from opt-melee-dps-raid-dps: 2 points Survivalist -> Clever Traps; 1 point Lacerating Strikes -> Efficiency; 2 points Lightning Reflexes -> Survivalist's Discipline (+3.2% DPS on the search's third seed).
- Simulator numbers are the community's model of the beta (ElliotWood/Forever), not in-game measurements.

## Open questions (verify in the live game)

- A derived Survival raid build: check it against the community's Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
