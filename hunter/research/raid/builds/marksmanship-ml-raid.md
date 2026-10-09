# Marksmanship — Raid (machine-learning search) — 11/40/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/40/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Marksmanship build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry mm-lonewolf-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Improved Aspect of the Monkey** | 1/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |

### Marksmanship (40)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Arcane Shot** | 4/5 | changed | Reduces the cooldown of your Arcane Shot by 1.2 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yds by 30. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 8** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) | ours: optimizer | 5/38/8 | 463 | +0.0% | 858 | -4.3% | 92 s |
| 2 | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) | ours: hand draft | 5/41/5 | 457 | -1.2% | 897 | +0.0% | 97 s |
| 3 | **[`marksmanship-ml-raid`](marksmanship-ml-raid.md)** | ours: hand draft | 11/40/0 | 444 | -4.0% | 815 | -9.1% | 89 s |
| 4 | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) | ours: parse build | 7/44/0 | 441 | -4.7% | 855 | -4.6% | 92 s |
| 5 | *Marksmanship* | community simulator | - | 359 | -22.5% | 692 | -22.9% | 92 s |
| 6 | *Marksmanship 0/39/12* | community simulator | - | 359 | -22.5% | 672 | -25.0% | 90 s |
| 7 | *Survival 0/15/36* | community simulator | - | 323 | -30.2% | 557 | -37.9% | 75 s |
| 8 | *Beast Mastery 35/16/0* | community simulator | - | 315 | -32.0% | 544 | -39.4% | 52 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 10 passes, the last 2026-10-09, 12 changes to the base rotation; third-seed check: opt-mm-lonewolf-raid-raid-dps 793 -> 859 DPS (+8.2%), sim preset: Beast Mastery 35/16/0 534 -> 544 DPS (+1.9%), mm-lone-wolf-raid 819 -> 896 DPS (+9.4%), marksmanship-ml-parse 789 -> 855 DPS (+8.4%), marksmanship-ml-raid 756 -> 815 DPS (+7.8%)):
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

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 3 | cast Arcane Shot | 8.7 |
| 4 | if time to the next auto attack > 0.5s and mana % ≥ 10%: cast Aimed Shot | 3.9 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.3 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) |
|---|---|
| Auto Shot | 52% |
| Arcane Shot | 23% |
| Serpent Sting | 15% |
| Aimed Shot | 10% |

## Notes

- Against the best hand draft mm-lone-wolf-raid in the same gear and fights (100,000, one seed): +2.4% (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow mm-lone-wolf-raid: Focused Fire → Endurance Training, Survivalist → Endurance Training (3 points), Improved Tracking → Endurance Training, Improved Tracking → Improved Aspect of the Monkey, Improved Tracking → Hawk Eye (3 points) (the same DPS as the search winner 6/37/8 on one seed, 30,000 fights).
- Search result: 6/37/8 at 452.0 ± 0.05 DPS over 100,000 fights; runner-up 6/37/8 (+0.00%; the winner takes Improved Tracking 5; the runner-up Deflection 1, Improved Tracking 4); 3,029 builds simulated; certificate: none of its 412 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 21/30/0 at 437.0 DPS on the dummy (other talents: _reference/dps-rankings.md).

## Open questions (verify in the live game)

- A machine-searched Marksmanship build: check it against the community's Marksmanship builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
