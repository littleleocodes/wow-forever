# Marksmanship — Lone Wolf (simulator winner adopted 2026-09-26) — 5/41/5

*[Hunter](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/41/5 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Allocation adopted on 2026-09-26 from `opt-mm-lonewolf-raid-raid-dps`, the best build in the community simulator (+13.8% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Lone Wolf (+20% damage with no pet) plus the full Marksmanship core, with Survival for Improved Tracking (+5% vs. the tracked creature type), Surefooted (+3% hit) and Deterrence. The petless alternative to the BM/MM build; no Classic baseline.

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (41)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increased the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Rapid Recuperation** | 2/2 | **NEW** | Hitting a target with your Serpent Sting ability grants you 50% and consuming Rapid Killing grants you 100% of your Mana regeneration while casting for the next 15 sec. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A steady snipe that increases ranged damage by 160. |

### Survival (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |

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
| 5 | Improved Tracking | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**1 of 6** for `mm-lonewolf-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`mm-lone-wolf-raid`](mm-lone-wolf-raid.md)** | ours: hand draft | 5/41/5 | 424 | +0.0% | 762 | +0.0% | 14 s |
| 2 | [`opt-mm-lonewolf-raid-raid-dps`](opt-mm-lonewolf-raid-raid-dps.md) | ours: optimizer | 5/36/10 | 424 | -0.0% | 762 | -0.0% | 14 s |
| 3 | *Marksmanship* | community simulator | - | 339 | -20.1% | 619 | -18.8% | 14 s |
| 4 | *Marksmanship 0/39/12* | community simulator | - | 323 | -23.8% | 584 | -23.3% | 11 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 299 | -29.5% | 483 | -36.6% | 0 s |
| 6 | *Survival 0/15/36* | community simulator | - | 299 | -29.5% | 481 | -36.8% | 11 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 5 changes to the base rotation; third-seed check: mm-lone-wolf-raid 388 -> 424 DPS (+9.4%), sim preset: Marksmanship 315 -> 339 DPS (+7.6%)):
  1. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+3.3%, pass 1)
  2. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.4%, pass 1)
  3. threshold 1s -> 0.5s: if time to the next auto attack > 1s: cast Aimed Shot (+0.7%, pass 1)
  4. threshold 1s -> 2s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting (+0.2%, pass 1)
  5. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 4 changes to the base rotation; third-seed check: mm-lone-wolf-raid 741 -> 762 DPS (+2.7%), sim preset: Marksmanship 602 -> 619 DPS (+2.7%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.7%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.5%, pass 1)
  3. drop 'time to the next auto attack > 1s' from the condition: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.3%, pass 1)
  4. drop the condition: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.2%, pass 1)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.5 |
| 3 | if time to the next auto attack > 0.5s: cast Aimed Shot | 7.5 |
| 4 | if time to the next auto attack > 0.5s: cast Multi-Shot | 0.5 |
| 5 | if time left on Serpent Sting < 2s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 4.0 |

Damage by ability:

| Ability | [`mm-lone-wolf-raid`](mm-lone-wolf-raid.md) |
|---|---|
| Auto Shot | 55% |
| Serpent Sting | 24% |
| Aimed Shot | 19% |
| Multi-Shot | 1% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-mm-lonewolf-raid-raid-dps beat the previous draft by +13.8% DPS; the rationale below predates the adoption where it names talents no longer taken.
- No pet means no Focused Fire, no pet damage, but also no pet management, no Growl pulls and no dead-pet downtime.
- 2026-09-27 scenario audit: Improved Revive Pet 2 -> Efficiency 2. Improved Revive Pet speeds up reviving a pet this build never has out (Lone Wolf). Efficiency's cheaper shots and stings are mana over a long fight (scorer +0.4 points; the simulator's 120 s fight shows no mana shortage).
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.

## Open questions (verify in the live game)

- Lone Wolf +20% vs. a Ferocity/Unleashed Fury pet: needs a sim or parse comparison at 60.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
