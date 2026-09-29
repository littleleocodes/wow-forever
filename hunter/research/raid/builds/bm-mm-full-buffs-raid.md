# Beast Mastery / Marksmanship (full raid buffs, 20/31/0) — 20/31/0

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/31/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `bm-mm-raid` |

## Summary

The build for a raid that brings Blessing of Wisdom and Mana Spring: `bm-mm-raid` until the training-dummy adoption of 2026-09-27, restored as its companion. In the community simulator's raid setting (full buffs, ElliotWood/Forever 40be98e, 3000 iterations) it does 687 DPS against `bm-mm-raid`'s 643 (+6.8%); on the training dummy, where our raid drafts are ranked (your own buffs only), it does 327 against 352 (-7.1%), out of mana 68 s of 120. Simulator numbers, not measurements. The Classic 20/31/0 maps well: Deadly Aspects replaces Improved Aspect of the Hawk (same 10% haste proc at max rank), Lethal Attacks replaces Lethal Shots, Careful Aim (Intellect to attack power) is the new Mortal Shots prerequisite, Trueshot Aura is cheaper at tier 4, and Sniper Shot is the capstone. Focused Fire and a stronger Unleashed Fury/Ferocity keep the pet worth its 20 points.

## Point allocation

### Beast Mastery (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 1/5 | changed | Increases the Health and Armor of your pets by 3%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Revive Pet** | 2/2 | unchanged | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |

### Marksmanship (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 4/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 12%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yards by 30. Lasts 30 min. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |
| **Sniper Shot** | 1/1 | **NEW** | A steady snipe that increases ranged damage by 160. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Trueshot Aura** — Group ranged attack power; now a 16-point talent (demo shows +30 RAP at level 38 — expect a higher rank at 60).
2. **Deadly Aspects** — Hawk: 2%/rank (est. 10%) chance per auto-shot for +30% ranged haste — the Improved Aspect of the Hawk replacement.
3. **Lethal Attacks** — +5% crit with all attacks (est.) — replaces Lethal Shots.
4. **Mortal Shots** — +30% ranged crit damage (est.); requires Careful Aim 5.
5. **Careful Aim** — New: attack power from Intellect (20%/rank read; scaling unknown).
6. **Ranged Weapon Specialization** — +5% ranged damage.
7. **Sniper Shot** — New capstone: 4s cast, +160 damage snipe on a 15s cooldown — the Aimed Shot replacement.
8. **Unleashed Fury** — +15% pet damage (est.).
9. **Ferocity** — +10% pet crit (est.).
10. **Focused Fire** — New: +2% all damage while the pet is out (est.).
11. **Efficiency** — Mana on shots/stings (3%/rank).
12. **Barrage** — Multi-Shot/Aimed Shot/Volley damage; gating filler for tier 6.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Rapid Killing | Improved Arcane Shot, Improved Stings | Tier-3 Marksmanship filler; Rapid Killing (-1 min Rapid Fire) also unlocks Rapid Recuperation if you find 2 more points. |
| 3 | Endurance Training 1 + Improved Revive Pet 2 | Improved Aspect of the Monkey, Pathfinding | Beast Mastery gating fillers. |
| 4 | Efficiency 4 | Efficiency 5 with Rapid Killing 1 | Mana vs. Rapid Fire uptime. |

## Rank among our builds and the community simulator's

**4 of 7** for `mm-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-mm-raid-raid-dps`](opt-mm-raid-raid-dps.md) | ours: optimizer | 22/29/0 | 415 | +0.0% | 761 | -3.4% | 78 s |
| 2 | [`bm-mm-raid`](bm-mm-raid.md) | ours: hand draft | 22/29/0 | 413 | -0.5% | 758 | -3.8% | 76 s |
| 3 | *Marksmanship* | community simulator | - | 388 | -6.4% | 788 | +0.0% | 99 s |
| 4 | **[`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md)** | ours: hand draft | 20/31/0 | 386 | -7.0% | 784 | -0.5% | 93 s |
| 5 | *Beast Mastery 35/16/0* | community simulator | - | 370 | -10.7% | 691 | -12.4% | 92 s |
| 6 | *Marksmanship 0/39/12* | community simulator | - | 356 | -14.3% | 719 | -8.8% | 94 s |
| 7 | *Survival 0/15/36* | community simulator | - | 335 | -19.2% | 640 | -18.8% | 91 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 395 -> 428 DPS (+8.5%), sim preset: Marksmanship 360 -> 399 DPS (+10.9%)):
  1. drop 'mana % ≥ 30%' from the condition: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+2.3%, pass 1)
  2. drop: if time to the next auto attack > 1s and time until Aimed Shot is ready ≥ 1 and time until Multi-Shot is ready ≥ 1: cast Sniper Shot (+1.7%, pass 1)
  3. threshold 0.5s -> 1s: if time to the next auto attack > 0.5s: cast Multi-Shot (+0.6%, pass 1)
  4. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  5. only with 20s or more of the fight left: if time to the next auto attack > 1s: cast Aimed Shot (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-mm-raid-raid-dps 644 -> 766 DPS (+19.0%), sim preset: Marksmanship 681 -> 817 DPS (+20.0%)):
  1. drop: if time to the next auto attack > 1s: cast Aimed Shot (+1.0%, pass 1)
  2. drop 'time until Aimed Shot is ready < 0.5' from the condition: if time to the next auto attack < 0.1 and time until Aimed Shot is ready < 0.5: cast Rapid Fire (+0.3%, pass 1)
  3. only with 6s or more of the fight left: if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5 and mana % ≥ 30%: cast Serpent Sting (+0.2%, pass 1)

Before the pull: at -10s: cast Aspect of the Hawk; at -2.5s: cast Aimed Shot.

| # | Priority (the first line whose condition holds is cast) | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) casts/min |
|---|---|---|
| 1 | cast Arcane Shot | 7.4 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time to the next auto attack < 0.1: cast Rapid Fire | 0.3 |
| 4 | if time to the next auto attack > 1s and time left in the fight ≥ 20s: cast Aimed Shot | 3.9 |
| 5 | if time to the next auto attack > 1s: cast Multi-Shot | 0.1 |
| 6 | if time left on Serpent Sting < 1s and time until Aimed Shot is ready ≥ 0.5 and time until Multi-Shot is ready ≥ 0.5: cast Serpent Sting | 2.0 |

Damage by ability:

| Ability | [`bm-mm-full-buffs-raid`](bm-mm-full-buffs-raid.md) |
|---|---|
| Auto Shot | 50% |
| Arcane Shot | 19% |
| Serpent Sting | 10% |
| Aimed Shot | 9% |
| Pet: Auto Attack | 8% |
| Pet: Claw | 2% |
| Pet: Bite | 0% |
| Multi-Shot | 0% |

## Notes

- Restored 2026-09-27 (user choice: keep both builds). Take `bm-mm-raid` when you bring your own mana (the dummy, small groups, no paladin or shaman in your party) and this one when a raid supplies Blessing of Wisdom and Mana Spring. The reasons under core and flex predate the 2026-09-27 training-dummy calibration.
- Aimed Shot is no longer a talent — either baseline or gone; Barrage's tooltip still names it, which suggests baseline.
- Compare with the Lone Wolf build: +20% own damage without a pet vs. ~25-30% more pet damage plus Focused Fire.
- Summon Hawk (new-builds survey, 2026-09-28): this draft does not take Summon Hawk, and the Marksmanship rotation never casts it. In the simulator one point in it, under a rotation that casts it on cooldown, is worth +47% to bm-mm-raid on the training dummy: see mm-hawk-raid, whose lead rests on the simulator's guess at the hawks' follow-up attacks.

## Open questions (verify in the live game)

- Trueshot Aura value at level 60 and whether it still stacks with other AP buffs.
- Careful Aim scaling (20% of Intellect per rank would be enormous; likely 20% total).
- Sniper Shot in a shot rotation: a 4s cast for +160 damage vs. two Auto Shots.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
