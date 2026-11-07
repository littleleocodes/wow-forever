# Marksmanship with Beast Mastery support (full raid buffs, 20/31/0) — 21/30/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `bm-mm-raid` |

## Summary

The build for a raid that brings Blessing of Wisdom and Mana Spring: `bm-mm-raid` until the training-dummy adoption of 2026-09-27, restored as its companion. In the community simulator's raid setting (full buffs, ElliotWood/Forever 40be98e, 3000 iterations) it does 687 DPS against `bm-mm-raid`'s 643 (+6.8%); on the training dummy, where our raid drafts are ranked (your own buffs only), it does 327 against 352 (-7.1%), out of mana 68 s of 120. Simulator numbers, not measurements. The Classic 20/31/0 maps well: Deadly Aspects replaces Improved Aspect of the Hawk (same 10% haste proc at max rank), Lethal Attacks replaces Lethal Shots, Careful Aim (Intellect to attack power) is the new Mortal Shots prerequisite, Trueshot Aura is cheaper at tier 4, and Sniper Shot is the capstone. Focused Fire and a stronger Unleashed Fury/Ferocity keep the pet worth its 20 points.

## Point allocation

### Beast Mastery (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Bestial Discipline** | 1/2 | changed | Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting. |

### Marksmanship (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 15%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Improved Stings** | 1/3 | **NEW** | Increases the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Trueshot Aura** — Group ranged attack power; now a 16-point talent (demo shows +30 RAP at level 38 — expect a higher rank at 60).
2. **Deadly Aspects** — Hawk: 2%/rank (est. 10%) chance per auto-shot for +30% ranged haste — the Improved Aspect of the Hawk replacement.
3. **Lethal Attacks** — +5% crit with all attacks (est.) — replaces Lethal Shots.
4. **Mortal Shots** — +30% ranged crit damage (est.); requires Careful Aim 5.
5. **Careful Aim** — New: attack power from Intellect (20%/rank read; scaling unknown).
6. **Ranged Weapon Specialization** — +5% ranged damage.
7. **Unleashed Fury** — +15% pet damage (est.).
8. **Ferocity** — +10% pet crit (est.).
9. **Focused Fire** — New: +2% all damage while the pet is out (est.).
10. **Efficiency** — Mana on shots/stings (3%/rank).
11. **Barrage** — Multi-Shot/Aimed Shot/Volley damage; gating filler for tier 6.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Improved Stings | Improved Arcane Shot, Improved Stings, Rapid Killing | Tier-3 Marksmanship filler; Rapid Killing (-1 min Rapid Fire) also unlocks Rapid Recuperation if you find 2 more points. |
| 3 | Endurance Training 1 + Improved Revive Pet 2 | Improved Aspect of the Monkey, Pathfinding | Beast Mastery gating fillers. |
| 4 | Efficiency 4 | Efficiency 5 with Rapid Killing 1 | Mana vs. Rapid Fire uptime. |

## Rank among our builds and the community simulator's

**2 of 11** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever 7c3453f (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) | ours: optimizer | 31/16/4 | 530 | +0.0% | 937 | -4.5% | 38 s |
| 2 | **[`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md)** | ours: hand draft | 21/30/0 | 499 | -5.9% | 916 | -6.7% | 32 s |
| 3 | *BM Weave* | community simulator | - | 489 | -7.8% | 956 | -2.6% | 46 s |
| 4 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 11/35/5 | 478 | -9.9% | 943 | -3.9% | 64 s |
| 5 | *BM* | community simulator | - | 477 | -10.1% | 982 | +0.0% | 52 s |
| 6 | *MM* | community simulator | - | 471 | -11.1% | 969 | -1.3% | 50 s |
| 7 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 461 | -13.0% | 906 | -7.7% | 26 s |
| 8 | *SV* | community simulator | - | 434 | -18.2% | 838 | -14.7% | 47 s |
| 9 | *SV Weave* | community simulator | - | 429 | -19.0% | 827 | -15.7% | 47 s |
| 10 | *MM Weave* | community simulator | - | 415 | -21.8% | 834 | -15.0% | 53 s |
| 11 | *SV Melee* | community simulator | - | 388 | -26.8% | 814 | -17.0% | 51 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 16 passes, the last 2026-11-04, 16 changes to the base rotation; third-seed check: marksmanship-ml-raid 925 -> 1004 DPS (+8.6%), sim preset: BM 936 -> 981 DPS (+4.8%), bm-mm-raid 890 -> 905 DPS (+1.7%), bm-mm-full-buffs-raid 903 -> 916 DPS (+1.4%), opt-mm-raid-raid-dps 924 -> 937 DPS (+1.4%)):
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
  15. threshold 1s -> 0.75s: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and time left in the fight ≥ 6s: cast Serpent Sting (+0.2%, pass 15)
  16. threshold 3 -> 2.25: if time until Aimed Shot is ready ≥ 3 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+0.2%, pass 16)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 8.3 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 15%: cast Aimed Shot | 3.6 |
| 5 | if time to the next auto attack > 1s and mana % ≥ 10%: cast Multi-Shot | 0.9 |
| 6 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.4 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) |
|---|---|
| Auto Shot | 34% |
| Pet: Auto Attack | 24% |
| Arcane Shot | 18% |
| Serpent Sting | 10% |
| Aimed Shot | 8% |
| Pet: Claw | 2% |
| Pet: Bite | 1% |
| Multi-Shot | 1% |
| spell 1295633 | 0% |

## Notes

- Restored 2026-09-27 (user choice: keep both builds). Take `bm-mm-raid` when you bring your own mana (the dummy, small groups, no paladin or shaman in your party) and this one when a raid supplies Blessing of Wisdom and Mana Spring. The reasons under core and flex predate the 2026-09-27 training-dummy calibration.
- Aimed Shot is no longer a talent — either baseline or gone; Barrage's tooltip still names it, which suggests baseline.
- Compare with the Lone Wolf build: +20% own damage without a pet vs. ~25-30% more pet damage plus Focused Fire.
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Sniper Shot -> Bestial Discipline (+3.6% DPS); Rapid Killing -> Efficiency (+0.8% DPS); Rapid Killing -> Improved Stings (+0.7% DPS); Improved Revive Pet -> Endurance Training (survival); Improved Revive Pet -> Endurance Training (survival). Net +5.25% on a third seed.
- 2026-09-30: renamed from "Beast Mastery / Marksmanship (full raid buffs, 20/31/0)" so the name matches the spec the pages file it under (the point split decides the spec, spec_modes.py).

## Open questions (verify in the live game)

- Trueshot Aura value at level 60 and whether it still stacks with other AP buffs.
- Careful Aim scaling (20% of Intellect per rank would be enormous; likely 20% total).
- Sniper Shot in a shot rotation: a 4s cast for +160 damage vs. two Auto Shots.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
