# Beast Mastery / Marksmanship (simulator winner adopted 2026-09-27) — 22/29/0

*[Hunter](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/29/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `bm-mm-raid` |

## Summary

Allocation adopted on 2026-09-27 from `opt-mm-raid-raid-dps`, the best build in the community simulator (+7.6% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: The Classic 20/31/0 maps well: Deadly Aspects replaces Improved Aspect of the Hawk (same 10% haste proc at max rank), Lethal Attacks replaces Lethal Shots, Careful Aim (Intellect to attack power) is the new Mortal Shots prerequisite, Trueshot Aura is cheaper at tier 4, and Sniper Shot is the capstone. Focused Fire and a stronger Unleashed Fury/Ferocity keep the pet worth its 20 points.

## Point allocation

### Beast Mastery (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Improved Mend Pet** | 2/2 | changed | Gives your Mend Pet spell a 50% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 20%. |
| **Ferocity** | 3/5 | changed | Increases the critical strike chance of your pets and hawks by 6%. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Marksmanship (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Improved Stings** | 2/3 | **NEW** | Increased the damage of your Serpent Sting ability by 13%, reduces the cooldown of your Viper Sting ability by 4 sec, and increases the duration of your Scorpid Sting ability by 30 sec. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Barrage** | 2/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 7%. |
| **Ranged Weapon Specialization** | 4/5 | unchanged | Increases the damage you deal with ranged weapons by 4%. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Deadly Aspects** — Hawk: 2%/rank (est. 10%) chance per auto-shot for +30% ranged haste — the Improved Aspect of the Hawk replacement. Raid sim (2026-09-27): removing it costs +6% DPS.
2. **Bestial Discipline** — Raid sim (2026-09-27): removing it costs +5% DPS.
3. **Lethal Attacks** — +5% crit with all attacks (est.) — replaces Lethal Shots. Raid sim (2026-09-27): removing it costs +5% DPS.
4. **Mortal Shots** — +30% ranged crit damage (est.); requires Careful Aim 5. Raid sim (2026-09-27): removing it costs +4% DPS.
5. **Efficiency** — Mana on shots/stings (3%/rank). Raid sim (2026-09-27): removing it costs +4% DPS.
6. **Careful Aim** — New: attack power from Intellect (20%/rank read; scaling unknown). Raid sim (2026-09-27): removing it costs +4% DPS.
7. **Ranged Weapon Specialization** — +5% ranged damage. Raid sim (2026-09-27): removing it costs +3% DPS.
8. **Trueshot Aura** — Group ranged attack power; now a 16-point talent (demo shows +30 RAP at level 38 — expect a higher rank at 60). Raid sim (2026-09-27): removing it costs +2% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Ferocity | any utility talent legal at that tier | Measures +0.9% DPS in the community simulator (noise): these points are free to move. |
| 3 | Endurance Training | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Mend Pet | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**2 of 7** for `mm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) | ours: optimizer | 22/29/0 | 428 | +0.0% | 766 | -6.1% | 45 s |
| 2 | **[`bm-mm-raid`](bm-mm-raid.md)** | ours: hand draft | 22/29/0 | 425 | -0.5% | 769 | -5.8% | 44 s |
| 3 | *Marksmanship* | community simulator | - | 400 | -6.4% | 816 | +0.0% | 60 s |
| 4 | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) | ours: hand draft | 20/31/0 | 395 | -7.6% | 809 | -0.9% | 54 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 381 | -10.9% | 698 | -14.4% | 53 s |
| 6 | *Marksmanship 0/39/12* | community simulator | - | 368 | -14.0% | 740 | -9.3% | 54 s |
| 7 | *Survival 0/15/36* | community simulator | - | 343 | -19.9% | 649 | -20.4% | 52 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 5 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 397 -> 404 DPS (+1.9%), sim preset: Marksmanship 360 -> 386 DPS (+7.2%)):
  1. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.3%, pass 1)
  2. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+1.7%, pass 1)
  3. threshold 0.5s -> 1s: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 1)
  4. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  5. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 3 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 647 -> 654 DPS (+1.0%), sim preset: Marksmanship 681 -> 695 DPS (+2.0%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.0%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  3. only with 6s or more of the fight left: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 1)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`bm-mm-raid`](bm-mm-raid.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 8.8 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.5 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s: cast Aimed Shot | 5.0 |
| 5 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.5 |

Lines of the simulator's rotation these builds never cast: cast Multi-Shot (its condition never held in these fights).

Damage by ability:

| Ability | [`bm-mm-raid`](bm-mm-raid.md) |
|---|---|
| Auto Shot | 46% |
| Arcane Shot | 20% |
| Serpent Sting | 13% |
| Aimed Shot | 10% |
| Pet: Auto Attack | 7% |
| Pet: Claw | 2% |
| Pet: Bite | 1% |
| Multi-Shot | 0% |

## Notes

- Adopted from the community simulator on 2026-09-27: opt-mm-raid-raid-dps beat the previous draft by +7.6% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Aimed Shot is no longer a talent — either baseline or gone; Barrage's tooltip still names it, which suggests baseline.
- Compare with the Lone Wolf build: +20% own damage without a pet vs. ~25-30% more pet damage plus Focused Fire.
- Companion build `bm-mm-full-buffs-raid` (restored 2026-09-27): in a raid with Blessing of Wisdom and Mana Spring it does 687 DPS against this build's 643 (+6.8%, ElliotWood/Forever 40be98e, 3000 iterations); this build wins on the training dummy (352 vs 327).
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.

## Open questions (verify in the live game)

- Trueshot Aura value at level 60 and whether it still stacks with other AP buffs.
- Careful Aim scaling (20% of Intellect per rank would be enormous; likely 20% total).
- Sniper Shot in a shot rotation: a 4s cast for +160 damage vs. two Auto Shots.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
