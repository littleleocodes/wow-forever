# Marksmanship — Lone Wolf (simulator winner adopted 2026-09-26) — 11/40/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/40/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Allocation adopted on 2026-09-26 from `opt-mm-lonewolf-raid-raid-dps`, the best build in the community simulator (+13.8% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Lone Wolf (+20% damage with no pet) plus the full Marksmanship core, with Survival for Improved Tracking (+5% vs. the tracked creature type), Surefooted (+3% hit) and Deterrence. The petless alternative to the BM/MM build; no Classic baseline.

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
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yds by 30. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Hitting a target with your Serpent Sting ability grants you 50% and consuming Rapid Killing grants you 100% of your Mana regeneration while casting for the next 15 sec. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Lone Wolf** — +20% damage with all attacks while no pet is active. Raid sim (2026-09-26): removing it costs +20% DPS.
2. **Deadly Aspects** — Raid sim (2026-09-26): removing it costs +11% DPS.
3. **Sniper Shot** — Capstone snipe. Raid sim (2026-09-26): removing it costs +8% DPS.
4. **Careful Aim** — AP from Intellect. Raid sim (2026-09-26): removing it costs +6% DPS.
5. **Mortal Shots** — Ranged crit damage. Raid sim (2026-09-26): removing it costs +6% DPS.
6. **Lethal Attacks** — Crit. Raid sim (2026-09-26): removing it costs +5% DPS.
7. **Ranged Weapon Specialization** — Ranged damage. Raid sim (2026-09-26): removing it costs +4% DPS.
8. **Improved Stings** — Raid sim (2026-09-26): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Hawk Eye | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 3 | Efficiency | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Rapid Killing | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Trueshot Aura | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Rapid Recuperation | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 5 | Endurance Training | Improved Tracking, any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**4 of 8** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) | ours: optimizer | 5/38/8 | 431 | +0.0% | 862 | -4.4% | 99 s |
| 2 | [`marksmanship-ml-parse`](marksmanship-ml-parse.md) | ours: parse build | 7/44/0 | 431 | -0.1% | 901 | +0.0% | 100 s |
| 3 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: hand draft | 11/40/0 | 428 | -0.6% | 859 | -4.7% | 97 s |
| 4 | **[`mm-lone-wolf-raid`](mm-lone-wolf-raid.md)** | ours: hand draft | 11/40/0 | 427 | -0.9% | 805 | -10.7% | 89 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 370 | -14.2% | 629 | -30.2% | 67 s |
| 6 | *Marksmanship* | community simulator | - | 350 | -18.7% | 723 | -19.8% | 99 s |
| 7 | *Marksmanship 0/39/12* | community simulator | - | 326 | -24.3% | 673 | -25.4% | 97 s |
| 8 | *Survival 0/15/36* | community simulator | - | 300 | -30.3% | 559 | -38.0% | 90 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-10-04, 9 changes to the base rotation; third-seed check: deep: Marksmanship (dummy) 399 -> 486 DPS (+21.9%), deep: Marksmanship (raid) 381 -> 432 DPS (+13.5%), marksmanship-ml-raid 392 -> 428 DPS (+9.1%), sim preset: Beast Mastery 35/16/0 289 -> 370 DPS (+27.8%), mm-lone-wolf-raid 388 -> 427 DPS (+10.0%), opt-mm-lonewolf-raid-raid-dps 391 -> 430 DPS (+10.0%)):
  1. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+3.3%, pass 1)
  2. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.4%, pass 1)
  3. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.7%, pass 1)
  4. threshold 1s -> 2s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting (+0.2%, pass 1)
  5. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 2)
  6. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+5.5%, pass 4)
  7. move down below 'cast Arcane Shot': if time to the next auto attack > 0.5s: cast Aimed Shot (+0.4%, pass 6)
  8. only with 10s or more of the fight left: if auraIsInactive: cast Summon Hawk (+0.2%, pass 6)
  9. drop: if time to the next auto attack > 0.5s: cast Multi-Shot + only above 10% mana: if time to the next auto attack > 0.5s: cast Aimed Shot (+0.2%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-10-04, 9 changes to the base rotation; third-seed check: deep: Marksmanship (dummy) 792 -> 858 DPS (+8.3%), deep: Marksmanship (raid) 872 -> 911 DPS (+4.4%), marksmanship-ml-raid 835 -> 859 DPS (+2.8%), sim preset: Beast Mastery 35/16/0 564 -> 629 DPS (+11.6%), mm-lone-wolf-raid 796 -> 805 DPS (+1.1%), opt-mm-lonewolf-raid-raid-dps 838 -> 862 DPS (+2.9%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.7%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 1)
  3. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.3%, pass 1)
  4. drop the condition: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.2%, pass 1)
  5. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+2.3%, pass 4)
  6. insert at the top: if time to the next auto attack > 1s: cast Aimed Shot (+2.7%, pass 5)
  7. drop the condition: if time to the next auto attack > 1s: cast Aimed Shot (+1.5%, pass 5)
  8. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.9%, pass 5)
  9. move down below 'if auraIsInactive: cast Summon Hawk': cast Aimed Shot (+0.3%, pass 6)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 3 | cast Arcane Shot | 7.8 |
| 4 | if time to the next auto attack > 0.5s and mana % ≥ 10%: cast Aimed Shot | 4.0 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.3 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent).

Damage by ability:

| Ability | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) |
|---|---|
| Auto Shot | 52% |
| Arcane Shot | 22% |
| Serpent Sting | 16% |
| Aimed Shot | 10% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-mm-lonewolf-raid-raid-dps beat the previous draft by +13.8% DPS; the rationale below predates the adoption where it names talents no longer taken.
- No pet means no Focused Fire, no pet damage, but also no pet management, no Growl pulls and no dead-pet downtime.
- 2026-09-27 scenario audit: Improved Revive Pet 2 -> Efficiency 2. Improved Revive Pet speeds up reviving a pet this build never has out (Lone Wolf). Efficiency's cheaper shots and stings are mana over a long fight (scorer +0.4 points; the simulator's 120 s fight shows no mana shortage).
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Tracking -> Endurance Training (survival); Improved Tracking -> Endurance Training (survival); Improved Tracking -> Endurance Training (survival); Improved Tracking -> Endurance Training (survival); Improved Tracking -> Endurance Training (survival); Sniper Shot -> Improved Aspect of the Monkey (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Lone Wolf +20% vs. a Ferocity/Unleashed Fury pet: needs a sim or parse comparison at 60.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
