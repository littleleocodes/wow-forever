# Marksmanship — Raid (machine-learning search) — 7/39/5

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/39/5 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Marksmanship build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-11-02 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry mm-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |

### Marksmanship (39)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Improved Arcane Shot** | 5/5 | changed | Reduces the cooldown of your Arcane Shot by 1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 15. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

### Survival (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |

## Rank among our builds and the community simulator's

**3 of 4** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) | ours: optimizer | 31/16/4 | 414 | +0.0% | 736 | -5.9% | 37 s |
| 2 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 21/30/0 | 393 | -5.0% | 720 | -7.9% | 31 s |
| 3 | **[`marksmanship-ml-raid`](marksmanship-ml-raid.md)** | ours: derived (ML search) | 7/39/5 | 392 | -5.2% | 782 | +0.0% | 47 s |
| 4 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 375 | -9.2% | 719 | -8.1% | 25 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 10 passes, the last 2026-10-09, 12 changes to the base rotation; third-seed check: open winner 418 -> 452 DPS (+8.1%), bm-mm-full-buffs-raid 439 -> 473 DPS (+7.7%), sim preset: Marksmanship 417 -> 454 DPS (+8.9%), bm-mm-raid 443 -> 461 DPS (+3.9%)):
  1. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.3%, pass 1)
  2. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+1.7%, pass 1)
  3. threshold 0.5s -> 1s: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 1)
  4. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  5. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+6.4%, pass 5)
  7. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.3%, pass 6)
  8. only above 25% mana: if time to the next auto attack > 1s and time left in the fight ≥ 20s: cast Aimed Shot (+0.3%, pass 6)
  9. threshold 25% -> 20%: if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 25%: cast Aimed Shot (+0.2%, pass 9)
  10. threshold 10s -> 15s: if auraIsInactive and time left in the fight ≥ 10s: cast Summon Hawk + only above 10% mana: if time to the next auto attack > 1s: cast Multi-Shot (+0.2%, pass 9)
  11. insert in the middle: cast Intimidation + only above 60% mana: cast Intimidation (+0.3%, pass 9)
  12. threshold 20% -> 15%: if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 20%: cast Aimed Shot (+0.2%, pass 10)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 14 passes, the last 2026-11-01, 14 changes to the base rotation; third-seed check: marksmanship-open-raid 730 -> 786 DPS (+7.6%), bm-mm-raid 703 -> 719 DPS (+2.3%), bm-mm-full-buffs-raid 708 -> 720 DPS (+1.7%), opt-mm-raid-raid-dps 725 -> 736 DPS (+1.6%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.0%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  3. only with 6s or more of the fight left: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 1)
  4. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+1.3%, pass 5)
  5. insert in the middle: if time to the next auto attack > 1s: cast Aimed Shot (+0.8%, pass 6)
  6. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.3%, pass 6)
  7. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.3%, pass 6)
  8. insert before the filler: cast Intimidation (+0.2%, pass 6)
  9. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30% and time left in the fight ≥ 6s: cast Serpent Sting (+0.2%, pass 8)
  10. move to the top: cast Arcane Shot (+3.0%, pass 9)
  11. threshold 1 -> 3: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.7%, pass 12)
  12. move to the top: if time to the next auto attack > 0.5s: cast Aimed Shot (+0.5%, pass 12)
  13. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 3 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.5%, pass 12)
  14. insert at the end: cast Major Mana Potion (+0.2%, pass 13)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 9.7 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 15%: cast Aimed Shot | 3.4 |
| 5 | if time to the next auto attack > 1s and mana % ≥ 10%: cast Multi-Shot | 0.5 |
| 6 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.4 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) |
|---|---|
| Auto Shot | 39% |
| Arcane Shot | 20% |
| Pet: Auto Attack | 18% |
| Serpent Sting | 12% |
| Aimed Shot | 7% |
| Pet: Bite | 2% |
| Pet: Claw | 1% |
| Multi-Shot | 1% |
| spell 1295633 | 1% |

## Notes

- Against the best hand draft mm-lone-wolf-raid in a full raid, same gear and fights (100,000, one seed): +3.8% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Search result (full raid): 7/39/5 at 811.7 ± 0.08 DPS over 100,000 fights; runner-up 7/39/5 (+0.31%; the winner takes Improved Stings 3; the runner-up Barrage 1, Improved Stings 2); 3,144 builds simulated; certificate: none of its 345 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 54ceac6 (client 70707) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 7/39/5 at 820.5 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 21/30/0 at 397.4 DPS.

## Open questions (verify in the live game)

- A machine-searched Marksmanship build: check it against the community's Marksmanship builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
