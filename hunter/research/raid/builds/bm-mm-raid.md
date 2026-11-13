# Beast Mastery / Marksmanship (simulator winner adopted 2026-10-02) — 22/29/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/29/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `bm-mm-raid` |

## Summary

Allocation adopted on 2026-10-02 from `opt-mm-raid-raid-dps`, the best build in the community simulator (+5.1% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Allocation adopted on 2026-09-27 from `opt-mm-raid-raid-dps`, the best build in the community simulator (+7.6% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: The Classic 20/31/0 maps well: Deadly Aspects replaces Improved Aspect of the Hawk (same 10% haste proc at max rank), Lethal Attacks replaces Lethal Shots, Careful Aim (Intellect to attack power) is the new Mortal Shots prerequisite, Trueshot Aura is cheaper at tier 4, and Sniper Shot is the capstone. Focused Fire and a stronger Unleashed Fury/Ferocity keep the pet worth its 20 points.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Ferocity** | 4/5 | changed | Increases the critical strike chance of your pets and hawks by 8%. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Improved Arcane Shot** | 1/5 | changed | Reduces the cooldown of your Arcane Shot by 0.3 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Ranged Weapon Specialization** | 4/5 | unchanged | Increases the damage you deal with ranged weapons by 4%. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Efficiency** — Mana on shots/stings (3%/rank). Raid sim (2026-09-27): removing it costs +4% DPS. Raid sim (2026-10-02): removing it costs +6% DPS.
2. **Unleashed Fury** — Raid sim (2026-10-02): removing it costs +5% DPS.
3. **Summon Hawk** — Raid sim (2026-10-02): removing it costs +5% DPS.
4. **Lethal Attacks** — +5% crit with all attacks (est.) — replaces Lethal Shots. Raid sim (2026-09-27): removing it costs +5% DPS. Raid sim (2026-10-02): removing it costs +5% DPS.
5. **Deadly Aspects** — Hawk: 2%/rank (est. 10%) chance per auto-shot for +30% ranged haste — the Improved Aspect of the Hawk replacement. Raid sim (2026-09-27): removing it costs +6% DPS. Raid sim (2026-10-02): removing it costs +4% DPS.
6. **Bestial Discipline** — Raid sim (2026-09-27): removing it costs +5% DPS. Raid sim (2026-10-02): removing it costs +4% DPS.
7. **Careful Aim** — New: attack power from Intellect (20%/rank read; scaling unknown). Raid sim (2026-09-27): removing it costs +4% DPS. Raid sim (2026-10-02): removing it costs +3% DPS.
8. **Mortal Shots** — +30% ranged crit damage (est.); requires Careful Aim 5. Raid sim (2026-09-27): removing it costs +4% DPS. Raid sim (2026-10-02): removing it costs +3% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Endurance Training | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 1 | Improved Arcane Shot | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**7 of 11** for `mm-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) | ours: optimizer | 31/16/4 | 551 | +0.0% | 945 | -5.5% | 29 s |
| 2 | [`marksmanship-ml-raid`](marksmanship-ml-raid.md) | ours: derived (ML search) | 7/39/5 | 519 | -5.8% | 1000 | +0.0% | 28 s |
| 3 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 21/30/0 | 517 | -6.2% | 921 | -7.9% | 23 s |
| 4 | *BM Weave* | community simulator | - | 506 | -8.2% | 964 | -3.6% | 35 s |
| 5 | *BM* | community simulator | - | 494 | -10.4% | 989 | -1.2% | 40 s |
| 6 | *MM* | community simulator | - | 490 | -11.1% | 972 | -2.8% | 39 s |
| 7 | **[`bm-mm-raid`](bm-mm-raid.md)** | ours: hand draft | 22/29/0 | 478 | -13.4% | 910 | -9.0% | 15 s |
| 8 | *SV* | community simulator | - | 447 | -19.0% | 834 | -16.6% | 36 s |
| 9 | *SV Weave* | community simulator | - | 443 | -19.7% | 824 | -17.6% | 35 s |
| 10 | *MM Weave* | community simulator | - | 431 | -21.9% | 834 | -16.6% | 44 s |
| 11 | *SV Melee* | community simulator | - | 399 | -27.6% | 817 | -18.3% | 43 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 17 passes, the last 2026-11-10, 17 changes to the base rotation; third-seed check: marksmanship-ml-raid 890 -> 963 DPS (+8.3%), sim preset: BM 911 -> 955 DPS (+4.9%), bm-mm-raid 863 -> 878 DPS (+1.7%), bm-mm-full-buffs-raid 876 -> 889 DPS (+1.4%), opt-mm-raid-raid-dps 899 -> 912 DPS (+1.4%)):
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
  17. drop: cast Major Mana Potion (+1.6%, pass 17)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`bm-mm-raid`](bm-mm-raid.md) casts/min |
|---|---|---|
| 1 | if auraIsInactive and time left in the fight ≥ 15s: cast Summon Hawk | 8.3 |
| 2 | cast Arcane Shot | 0.8 |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 5 | if time to the next auto attack > 1s and time left in the fight ≥ 20s and mana % ≥ 15%: cast Aimed Shot | 4.2 |
| 6 | if time to the next auto attack > 1s and mana % ≥ 10%: cast Multi-Shot | 1.0 |
| 7 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.8 |

Lines of the simulator's rotation these builds never cast: cast Intimidation (needs the Intimidation talent).

Damage by ability:

| Ability | [`bm-mm-raid`](bm-mm-raid.md) |
|---|---|
| Auto Shot | 36% |
| Pet: Auto Attack | 30% |
| Serpent Sting | 14% |
| Aimed Shot | 9% |
| Summon Hawk | 4% |
| Pet: Bite | 2% |
| Arcane Shot | 2% |
| Pet: Claw | 2% |
| Multi-Shot | 1% |

## Notes

- Adopted from the community simulator on 2026-10-02: `opt-mm-raid-raid-dps` beat the previous draft by +5.1% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Adopted from the community simulator on 2026-09-27: opt-mm-raid-raid-dps beat the previous draft by +7.6% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Aimed Shot is no longer a talent — either baseline or gone; Barrage's tooltip still names it, which suggests baseline.
- Compare with the Lone Wolf build: +20% own damage without a pet vs. ~25-30% more pet damage plus Focused Fire.
- Companion build `bm-mm-full-buffs-raid` (restored 2026-09-27): in a raid with Blessing of Wisdom and Mana Spring it does 687 DPS against this build's 643 (+6.8%, ElliotWood/Forever 40be98e, 3000 iterations); this build wins on the training dummy (352 vs 327).
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Mend Pet -> Ferocity (+0.2% DPS); Improved Mend Pet -> Ferocity (+0.2% DPS). Net +0.49% on a third seed.

## Open questions (verify in the live game)

- Trueshot Aura value at level 60 and whether it still stacks with other AP buffs.
- Careful Aim scaling (20% of Intellect per rank would be enormous; likely 20% total).
- Sniper Shot in a shot rotation: a 4s cast for +160 damage vs. two Auto Shots.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
