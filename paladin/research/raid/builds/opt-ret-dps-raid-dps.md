# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (raid-dps) — 9/8/34

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/8/34 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `raid-dps`: score +91.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 1/5 | unchanged | Increases your total Intellect by 2%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 200, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage and healing by up to 100% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Core talents (priority order)

1. **Champion of the Light** — Removing it costs 24.2 points of score in this model.
2. **Holy Conduit** — Removing it costs 18.7 points of score in this model.
3. **Seal of Command** — Removing it costs 15.4 points of score in this model.
4. **Vengeance** — Removing it costs 12.9 points of score in this model.
5. **Conviction** — Removing it costs 12.4 points of score in this model.
6. **Twist of Light** — Removing it costs 10.5 points of score in this model.
7. **Improved Seals** — Removing it costs 9.2 points of score in this model.
8. **Sanctified Judgement** — Removing it costs 8.0 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 5** for `ret-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md)** | ours: optimizer | 9/8/34 | 350 | +0.0% | 802 | +0.0% | 21 s |
| 2 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/0/34 | 349 | -0.5% | 779 | -2.9% | 4 s |
| 3 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 10/8/33 | 346 | -1.2% | 802 | -0.0% | 22 s |
| 4 | *P4/P5 Ret* | community simulator | - | 341 | -2.7% | 776 | -3.2% | 11 s |
| 5 | *Retribution 9/0/42* | community simulator | - | 338 | -3.4% | 768 | -4.3% | 21 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 12 changes to the base rotation; third-seed check: opt-ret-dps-raid-dps 348 -> 369 DPS (+5.8%), sim preset: P4/P5 Ret 353 -> 366 DPS (+3.7%)):
  1. only above 40% mana: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Righteousness is up: cast Seal of Command (+2.5%, pass 1)
  2. threshold 0.4s -> 0.9s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.1%, pass 1)
  3. threshold 70% -> 60%: if mana % ≥ 70%: cast Consecration + threshold 0.4s -> 0.2s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Righteousness is up and mana % ≥ 40%: cast Seal of Command (+0.3%, pass 1)
  4. always rank 2 instead of rank 5: if mana % ≥ 60%: cast Consecration (+0.3%, pass 1)
  5. threshold 60% -> 40%: if mana % ≥ 60%: cast Consecration (+1.5%, pass 1)
  6. always rank 1 instead of rank 2: if mana % ≥ 40%: cast Consecration (+1.5%, pass 1)
  7. drop the condition: if mana % ≥ 40%: cast Consecration (+1.5%, pass 1)
  8. threshold 40% -> 60%: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 40%: cast Seal of Command (+1.4%, pass 1)
  9. insert before the filler: cast Consecration (+4.1%, pass 2)
  10. threshold 60% -> 70%: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 60%: cast Seal of Command (+0.6%, pass 2)
  11. threshold 0.9s -> 0.4s: if mana % ≥ 15% and time to the next auto attack < 0.9s and Seal of Command is up: cast Seal of Righteousness (+0.6%, pass 2)
  12. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 6 changes to the base rotation; third-seed check: opt-ret-dps-raid-dps 730 -> 779 DPS (+6.8%), sim preset: P4/P5 Ret 727 -> 777 DPS (+6.8%)):
  1. drop 'time left on Seal of Righteousness ≤ 1s' from the condition: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+2.4%, pass 1)
  2. threshold 70% -> 50%: if mana % ≥ 70%: cast Consecration (+1.4%, pass 1)
  3. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  4. threshold 0.4s -> 1.4s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.5%, pass 2)
  5. move to the top: cast Hammer of Wrath (+1.4%, pass 2)
  6. move down below 'if mana % ≥ 50%: cast Consecration': cast Holy Strike (+0.6%, pass 2)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness | 2.8 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command | 3.0 |
| 4 | if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command | 3.0 |
| 5 | cast Hammer of Wrath | 1.0 |
| 6 | cast Holy Strike | 5.8 |
| 7 | cast Consecration | 5.7 |
| 8 | cast Consecration | 1.0 |

Lines of the simulator's rotation these builds never cast: cast Judgement (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) |
|---|---|
| Auto Attack | 23% |
| Consecration | 17% |
| Judgement of Righteousness | 16% |
| Holy Strike | 15% |
| Seal of Righteousness | 14% |
| Seal of Command | 6% |
| Hammer of Wrath | 4% |
| Dragonbreath Chili | 2% |
| Judgement of Command | 2% |

## Notes

- Report: paladin/research/talents/forever/optimizer/ret-dps-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
