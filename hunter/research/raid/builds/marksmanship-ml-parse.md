# Marksmanship — Full raid (parse) (machine-learning search) — 7/44/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 7/44/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

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
| **Improved Stings** | 3/3 | **NEW** | Increased the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Improved Arcane Shot** | 5/5 | changed | Reduces the cooldown of your Arcane Shot by 1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Hitting a target with your Serpent Sting ability grants you 50% and consuming Rapid Killing grants you 100% of your Mana regeneration while casting for the next 15 sec. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A steady snipe that increases ranged damage by 160. |

### Survival (0)

*No points.*

## Rank among our builds and the community simulator's

**3 of 8** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: hand draft | 11/40/0 | 447 | +0.0% | 894 | -4.4% | 100 s |
| 2 | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) | ours: optimizer | 5/38/8 | 446 | -0.3% | 898 | -4.0% | 100 s |
| 3 | **[`marksmanship-ml-parse`](marksmanship-ml-parse.md)** | ours: parse build | 7/44/0 | 446 | -0.3% | 935 | +0.0% | 100 s |
| 4 | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) | ours: hand draft | 11/40/0 | 443 | -1.0% | 834 | -10.8% | 87 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 367 | -18.0% | 625 | -33.2% | 75 s |
| 6 | *Marksmanship* | community simulator | - | 362 | -19.0% | 748 | -20.0% | 100 s |
| 7 | *Marksmanship 0/39/12* | community simulator | - | 347 | -22.4% | 697 | -25.5% | 97 s |
| 8 | *Survival 0/15/36* | community simulator | - | 316 | -29.2% | 590 | -36.9% | 84 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 5 passes, the last 2026-10-02, 6 changes to the base rotation; third-seed check: ml: Marksmanship 382 -> 455 DPS (+19.1%), opt-mm-lonewolf-raid-raid-dps 384 -> 446 DPS (+16.0%), sim preset: Marksmanship 304 -> 362 DPS (+19.2%)):
  1. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+3.3%, pass 1)
  2. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.4%, pass 1)
  3. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.7%, pass 1)
  4. threshold 1s -> 2s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting (+0.2%, pass 1)
  5. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+5.5%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 5 passes, the last 2026-10-02, 8 changes to the base rotation; third-seed check: ml: Marksmanship 670 -> 878 DPS (+31.1%), opt-mm-lonewolf-raid-raid-dps 683 -> 898 DPS (+31.4%), sim preset: Marksmanship 600 -> 749 DPS (+24.8%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.7%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 1)
  3. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.3%, pass 1)
  4. drop the condition: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.2%, pass 1)
  5. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+2.3%, pass 4)
  6. insert at the top: if time to the next auto attack > 1s: cast Aimed Shot (+2.7%, pass 5)
  7. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+1.5%, pass 5)
  8. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.9%, pass 5)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 3 | if time to the next auto attack > 0.5s: cast Aimed Shot | 3.9 |
| 4 | cast Arcane Shot | 8.3 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.1 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Multi-Shot (its condition never held in these fights).

Damage by ability:

| Ability | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) |
|---|---|
| Auto Shot | 50% |
| Arcane Shot | 26% |
| Serpent Sting | 15% |
| Aimed Shot | 9% |
| Multi-Shot | 0% |

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
