# Retribution — Raid (open talent search) — 9/8/34

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/8/34 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution raid build the open talent search found on 2026-10-07: every legal 51-point build with no tree rule, searched in the community simulator's shockadin-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

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
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 200, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 60% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Core talents (priority order)

1. **Twist of Light** — 172 DPS lost without it (18% of the build in a full raid; removal, 12,000 fights).
2. **Seal of Command** — 136 DPS lost without it (14% of the build in a full raid; removal, 12,000 fights).
3. **Champion of the Light** — 84 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
4. **Vengeance** — 74 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
5. **Improved Seals** — 56 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Instrument of Law** — 48 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Holy Conduit** — 48 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Precision** — 38 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 1** for `shockadin-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`retribution-open-raid`](retribution-open-raid.md)** | ours: hand draft | 9/8/34 | 505 | +0.0% | 966 | +0.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-05, 4 passes, the last 2026-10-07, 6 changes to the base rotation; third-seed check: open winner 482 -> 505 DPS (+4.8%)):
  1. drop 'time to the next auto attack < 0.2s' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 60%: cast Seal of Command (+1.8%, pass 1)
  2. threshold 0.9s -> 0.4s: if mana % ≥ 15% and time to the next auto attack < 0.9s and Seal of Command is up: cast Seal of Righteousness (+1.7%, pass 1)
  3. threshold 60% -> 40%: if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 60%: cast Seal of Command (+1.4%, pass 1)
  4. threshold 40% -> 30%: if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 40%: cast Seal of Command (+0.7%, pass 1)
  5. threshold 0.4s -> 0.3s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  6. threshold 30% -> 25%: if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 30%: cast Seal of Command (+0.8%, pass 3)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-05, 5 passes, the last 2026-10-07, 10 changes to the base rotation; third-seed check: open winner 843 -> 964 DPS (+14.5%)):
  1. insert in the middle: cast Consecration (+4.5%, pass 1)
  2. always rank 7 instead of rank 8: if mana % ≥ 15% and time to the next auto attack < 0.9s and Seal of Command is up: cast Seal of Righteousness (+3.4%, pass 1)
  3. insert in the middle: cast Demonic Rune (+0.8%, pass 1)
  4. only with 10s or more of the fight left: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+0.2%, pass 1)
  5. insert before the filler: if not Seal of Command is up and not Seal of Righteousness is up: cast Seal of Righteousness (+0.3%, pass 1)
  6. threshold 0.9s -> 0.675s: if mana % ≥ 15% and time to the next auto attack < 0.9s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  7. drop 'mana % ≥ 15%' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.675s and Seal of Command is up: cast Seal of Righteousness + move to the top: cast Hammer of Wrath (+0.3%, pass 1)
  8. rotation replaced by seal-of-fury-raid's raid rotation (the open search's cross-race of every build under every sibling rotation) (+3.1%, pass 4)
  9. always rank 3 instead of rank 5: if mana % ≥ 15% and Seal of Righteousness is up: cast Seal of Command (+0.8%, pass 5)
  10. insert in the middle: if time left on Seal of Righteousness ≤ 1.5s: cast Seal of Righteousness (+0.2%, pass 5)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`retribution-open-raid`](retribution-open-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command | 8.0 |
| 3 | if mana % ≥ 15% and time to the next auto attack < 0.3s and Seal of Command is up: cast Seal of Righteousness | 8.0 |
| 4 | if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 25%: cast Seal of Command | 8.0 |
| 5 | cast Hammer of Wrath | 2.0 |
| 6 | cast Holy Strike | 6.0 |
| 7 | cast Consecration | 6.3 |

Lines of the simulator's rotation these builds never cast: cast Holy Shock, cast Judgement (its condition never held in these fights).

Damage by ability:

| Ability | [`retribution-open-raid`](retribution-open-raid.md) |
|---|---|
| Seal of Righteousness | 20% |
| Auto Attack | 18% |
| Holy Strike | 14% |
| Consecration | 12% |
| Judgement of Righteousness | 10% |
| Seal of Command | 9% |
| Judgement of Command | 8% |
| Hammer of Wrath | 6% |
| Dragonbreath Chili | 3% |

## Notes

- Open search result (shockadin-raid, full raid): 9/8/34 (Retribution) at 963.6 DPS;  in the same fights; 4,930 builds simulated, 2 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): retribution-ml-raid 957.1, opt-ret-dps-raid-dps 955.5, ret-full-buffs-raid 953.8, ret-raid-dps 935.2.
- Against the spec's best hand draft ret-full-buffs-raid: +1.0% (under the 2% bar: the hand draft stays the pick unless the re-race says otherwise).
- The shockadin-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): ret-dps +3.0%, seal-of-fury-raid +3.1%; seal-of-fury-raid's rotation adopted (+3.1%).
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Toughness.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Retribution build: check it against the community's Retribution builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/paladin/60/51003-503-05225331001330321-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
