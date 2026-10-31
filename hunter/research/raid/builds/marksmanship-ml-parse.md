# Marksmanship — Full raid (parse) (machine-learning search) — 7/44/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/44/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Marksmanship build the machine-learning talent search found in a full raid (every raid buff and debuff) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry mm-lonewolf-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |
| **Improved Revive Pet** | 1/2 | unchanged | Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%. |

### Marksmanship (44)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Hawk Eye** | 1/3 | moved | Increases the range of your ranged weapons by 2 yards. |
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Improved Arcane Shot** | 5/5 | changed | Reduces the cooldown of your Arcane Shot by 1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 15. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**4 of 11** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *MM* | community simulator | - | 371 | +0.0% | 723 | -4.8% | 45 s |
| 2 | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) | ours: optimizer | 7/41/3 | 361 | -2.7% | 706 | -7.1% | 28 s |
| 3 | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) | ours: hand draft | 5/41/5 | 360 | -3.0% | 759 | +0.0% | 53 s |
| 4 | **[`marksmanship-ml-parse`](marksmanship-ml-parse.md)** | ours: derived (ML search) | 7/44/0 | 354 | -4.5% | 724 | -4.7% | 45 s |
| 5 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 11/40/0 | 341 | -8.0% | 684 | -10.0% | 47 s |
| 6 | *SV* | community simulator | - | 329 | -11.2% | 630 | -17.0% | 37 s |
| 7 | *SV Weave* | community simulator | - | 320 | -13.6% | 624 | -17.8% | 43 s |
| 8 | *MM Weave* | community simulator | - | 313 | -15.6% | 641 | -15.6% | 51 s |
| 9 | *BM Weave* | community simulator | - | 250 | -32.7% | 506 | -33.4% | 30 s |
| 10 | *BM* | community simulator | - | 250 | -32.7% | 506 | -33.4% | 30 s |
| 11 | *SV Melee* | community simulator | - | 219 | -40.8% | 474 | -37.6% | 50 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 9 passes, the last 2026-10-07, 9 changes to the base rotation; third-seed check: open winner 396 -> 444 DPS (+12.2%), opt-mm-lonewolf-raid-raid-dps 422 -> 463 DPS (+9.5%), sim preset: Beast Mastery 35/16/0 298 -> 381 DPS (+27.8%), mm-lone-wolf-raid 405 -> 457 DPS (+12.8%), marksmanship-ml-raid 403 -> 444 DPS (+10.3%)):
  1. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+3.3%, pass 1)
  2. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.4%, pass 1)
  3. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.7%, pass 1)
  4. threshold 1s -> 2s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting (+0.2%, pass 1)
  5. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+5.5%, pass 4)
  7. move down below 'cast Arcane Shot': if time to the next auto attack > 0.5s: cast Aimed Shot (+0.4%, pass 6)
  8. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.2%, pass 6)
  9. drop: if time to the next auto attack > 0.5s: cast Multi-Shot + only above 10% mana: if time to the next auto attack > 0.5s: cast Aimed Shot (+0.2%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 13 passes, the last 2026-10-22, 14 changes to the base rotation; third-seed check: mm-lone-wolf-raid 697 -> 760 DPS (+8.9%), sim preset: Marksmanship 540 -> 590 DPS (+9.3%), opt-mm-lonewolf-raid-raid-dps 671 -> 727 DPS (+8.5%), marksmanship-ml-parse 667 -> 724 DPS (+8.5%), marksmanship-ml-raid 639 -> 684 DPS (+7.0%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.7%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 1)
  3. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.3%, pass 1)
  4. drop the condition: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.2%, pass 1)
  5. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+2.3%, pass 4)
  6. insert at the top: if time to the next auto attack > 1s: cast Aimed Shot (+2.7%, pass 5)
  7. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+1.5%, pass 5)
  8. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.9%, pass 5)
  9. move down below 'if auraIsInactive: cast Summon Hawk': cast Aimed Shot (+0.3%, pass 6)
  10. drop: if auraIsInactive: cast Summon Hawk (+0.7%, pass 10)
  11. insert at the top: if time to the next auto attack > 1s: cast Summon Hawk (+0.3%, pass 10)
  12. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Summon Hawk (+0.2%, pass 10)
  13. insert at the end: cast Major Mana Potion (+0.6%, pass 13)
  14. threshold 1 -> 2: if time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.5%, pass 13)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 3 | cast Arcane Shot | 10.0 |
| 4 | if time to the next auto attack > 0.5s and mana % ≥ 10%: cast Aimed Shot | 3.9 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.6 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) |
|---|---|
| Auto Shot | 49% |
| Arcane Shot | 26% |
| Serpent Sting | 14% |
| Aimed Shot | 11% |
| spell 1295633 | 1% |

## Notes

- In a full raid it does +4.6% over the training-dummy winner (909.4 vs 869.2 DPS, 100,000 fights, one seed, BiS gear).
- Search result: 7/44/0 at 909.6 ± 0.10 DPS over 100,000 fights; runner-up 8/43/0 (+0.00%; the winner takes Hawk Eye 1; the runner-up Focused Fire 1); 3,426 builds simulated; certificate: none of its 241 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.

## Open questions (verify in the live game)

- A machine-searched Marksmanship build: check it against the community's Marksmanship builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
