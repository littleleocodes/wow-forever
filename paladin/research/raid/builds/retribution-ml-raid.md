# Retribution — Raid (machine-learning search) — 11/8/32

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/8/32 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry ret-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Holy (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 2/5 | unchanged | Increases your Strength by 4%. |
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Reverence** | 1/3 | **NEW** | Allows 10% of your Mana regeneration to continue while casting. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68, and increase your Attack Power by 1% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 30% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1.0 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Rank among our builds and the community simulator's

**2 of 6** for `ret-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever b7083fa); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 12/8/31 | 517 | +0.0% | 948 | -0.4% | 2 s |
| 2 | **[`retribution-ml-raid`](retribution-ml-raid.md)** | ours: derived (ML search) | 11/8/32 | 509 | -1.4% | 952 | -0.0% | 7 s |
| 3 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/0/34 | 507 | -1.9% | 925 | -2.8% | 2 s |
| 4 | *P4/P5 Ret* | community simulator | - | 501 | -3.0% | 923 | -3.0% | 4 s |
| 5 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 10/8/33 | 500 | -3.2% | 952 | +0.0% | 21 s |
| 6 | *Retribution 9/0/42* | community simulator | - | 476 | -7.9% | 914 | -3.9% | 16 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-14, 18 changes to the base rotation; third-seed check: ):
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
  13. spell probe: insert at the top: cast Holy Shock (+8.0%, pass 4)
  14. drop 'time to the next auto attack < 0.2s' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command (+1.8%, pass 5)
  15. drop 'mana % ≥ 15%' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 5)
  16. threshold 70% -> 65%: if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command (+0.5%, pass 5)
  17. threshold 1s -> 2s: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+0.2%, pass 5)
  18. spell probe: insert at the end: cast Divine Favor (+3.9%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 12 passes, the last 2026-10-16, 12 changes to the base rotation; third-seed check: retribution-ml-raid 858 -> 951 DPS (+10.9%), sim preset: P4/P5 Ret 833 -> 924 DPS (+10.9%), ret-raid-dps 836 -> 927 DPS (+10.9%), ret-full-buffs-raid 864 -> 953 DPS (+10.4%), opt-ret-dps-raid-dps 853 -> 948 DPS (+11.1%)):
  1. drop 'time left on Seal of Righteousness ≤ 1s' from the condition: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+2.4%, pass 1)
  2. threshold 70% -> 50%: if mana % ≥ 70%: cast Consecration (+1.4%, pass 1)
  3. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  4. threshold 0.4s -> 1.4s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.5%, pass 2)
  5. move to the top: cast Hammer of Wrath (+1.4%, pass 2)
  6. move down below 'if mana % ≥ 50%: cast Consecration': cast Holy Strike (+0.6%, pass 2)
  7. spell probe: insert at the end: cast Holy Shock (+6.6%, pass 4)
  8. insert in the middle: cast Consecration (+7.1%, pass 5)
  9. insert in the middle: cast Demonic Rune (+0.2%, pass 5)
  10. rotation replaced by seal-of-fury-raid's raid rotation (keeps Seal of Righteousness up and judges it, Holy Strike, almost no seal twisting), which the open search's re-tune on a Retribution build produced (+2.0% on one seed, pass 6)
  11. always rank 4 instead of rank 5: if mana % ≥ 15% and Seal of Righteousness is up: cast Seal of Command (+0.3%, pass 8)
  12. spell probe: insert in the middle: cast Holy Shock (+9.3%, pass 11)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`retribution-ml-raid`](retribution-ml-raid.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness | 5.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Judgement can be cast: cast Judgement | 7.4 |
| 4 | if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 2s: cast Seal of Command | 5.0 |
| 5 | if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 65%: cast Seal of Command | 5.0 |
| 6 | cast Hammer of Wrath | 2.0 |
| 7 | cast Holy Strike | 5.9 |
| 8 | cast Consecration | 5.9 |
| 9 | cast Consecration (rank 1) | 0.6 |

Lines of the simulator's rotation these builds never cast: cast Holy Shock (needs the Holy Shock talent); cast Divine Favor (needs the Divine Favor talent).

Damage by ability:

| Ability | [`retribution-ml-raid`](retribution-ml-raid.md) |
|---|---|
| Auto Attack | 20% |
| Seal of Righteousness | 18% |
| Consecration | 16% |
| Holy Strike | 14% |
| Judgement of Righteousness | 12% |
| Seal of Command | 6% |
| Hammer of Wrath | 6% |
| Judgement of Command | 5% |
| Dragonbreath Chili | 3% |

## Notes

- Against the best hand draft ret-full-buffs-raid in the same gear and fights (100,000, one seed): +1.7% (under the 2% bar: the hand draft stays the pick).
- Search result: 11/8/32 at 554.6 ± 0.07 DPS over 100,000 fights; runner-up 11/8/32 (+0.00%; the winner takes Toughness 5; the runner-up Redoubt 5); 1,631 builds simulated; certificate: none of its 211 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 12/8/31 at 520.4 DPS on the dummy (other talents: _reference/dps-rankings.md).
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Retribution: its full-raid winner is +0.06% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- A machine-searched Retribution build: check it against the community's Retribution builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
