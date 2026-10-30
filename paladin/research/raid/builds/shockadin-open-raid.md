# Shockadin — Raid (open talent search) — 24/0/27

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 24/0/27 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) raid build the open talent search found on 2026-10-29: every legal 51-point build with no tree rule, searched in the community simulator's shockadin-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Holy (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Divine Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Consecrated Ground** | 2/2 | **NEW** | Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration. |
| **Voice of Truth** | 1/1 | **NEW** | Grants you immunity to Silence and Interrupt effects for 6 sec. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |

### Protection (0)

*No points.*

### Retribution (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 2/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 4%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 1/3 | **NEW** | Increases your spell damage by up to 10% of your Intellect. |
| **Instrument of Law** | 1/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 0.5 sec, and reduces all threat you generate by 10% while Righteous Fury is not active. |
| **Vindication** | 2/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 136, and increase your Attack Power by 2% for 30 sec. |

## Core talents (priority order)

1. **Holy Shock** — 83 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
2. **Vengeance** — 58 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
3. **Consecrated Ground** — 46 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
4. **Improved Judgement** — 36 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
5. **Improved Seals** — 27 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
6. **Conviction** — 22 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Two-Handed Weapon Specialization** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 1** for `shockadin-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shockadin-open-raid`](shockadin-open-raid.md)** | ours: derived (open search) | 24/0/27 | 355 | +0.0% | 778 | +0.0% | 80 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-29, 3 passes, the last 2026-10-29, 8 changes to the base rotation; third-seed check: shockadin-open-raid 724 -> 778 DPS (+7.5%)):
  1. insert at the top: cast Consecration (+3.1%, pass 1)
  2. drop: if mana % ≥ 15% and time to the next auto attack < 0.4s and mana % < 50%: cast Seal of Righteousness (rank 7) (+0.8%, pass 1)
  3. insert at the top: if time left on Seal of Righteousness < time to the next auto attack and auraIsInactive: cast Seal of Righteousness (+1.5%, pass 1)
  4. drop: if mana % ≥ 15% and time to the next auto attack < 0.4s: cast Seal of Righteousness (+0.4%, pass 1)
  5. drop: if time left on Seal of Righteousness ≤ 1s: cast Seal of Righteousness (+0.5%, pass 1)
  6. move to the top: use every other cooldown when ready (+0.3%, pass 1)
  7. drop: cast Consecration (+0.6%, pass 2)
  8. insert at the top: cast Weakness Analyzer (+1.8%, pass 3)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`shockadin-open-raid`](shockadin-open-raid.md) casts/min |
|---|---|---|
| 1 | cast Holy Shock | 3.7 |
| 2 | cast Hammer of Wrath | 1.3 |
| 3 | if mana % ≥ 15% and time to the next auto attack < 0.4s and mana % < 50%: cast Seal of Righteousness (rank 7) | 1.4 |
| 4 | if mana % ≥ 15% and time to the next auto attack < 0.4s: cast Seal of Righteousness | 3.6 |
| 5 | if Seal of Righteousness is up: cast Judgement | 4.9 |
| 6 | if mana % ≥ 25%: cast Consecration | 3.0 |
| 7 | cast Holy Strike | 5.8 |
| 8 | cast Holy Shock | 3.7 |
| 9 | use every other cooldown when ready | as ready |
| 10 | if Judgement can be cast and time left in the fight ≥ 20s: cast Judgement | 4.9 |
| 11 | cast Consecration (rank 1) | 3.1 |
| 12 | if time left on Seal of Righteousness ≤ 1s: cast Seal of Righteousness | 3.6 |

Lines of the simulator's rotation these builds never cast: cast Seal of Command (rank 2), cast Seal of Command (rank 4) (needs the Seal of Command talent).

Damage by ability:

| Ability | [`shockadin-open-raid`](shockadin-open-raid.md) |
|---|---|
| Auto Attack | 24% |
| Holy Strike | 17% |
| Judgement of Righteousness | 15% |
| Holy Shock | 13% |
| Consecration | 12% |
| Seal of Righteousness | 12% |
| Hammer of Wrath | 5% |
| Demonic Rune | 3% |
| spell 16614 | 0% |

## Notes

- Open search result (shockadin-raid, full raid): 24/0/27 (Shockadin (a Holy/Retribution hybrid)) at 759.1 DPS;  in the same fights; 2,349 builds simulated, 1 independent runs reached the top.
- The shockadin-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- A phase-1 BiS set picked for this family (_reference/data/raidsim/gear_sets/forever/tiers/paladin-hybrid-holy-retribution-bis.gear.json, item level 64.6): 764.9 DPS against 759.2 in the rotation's standard set: a lead for the gear sets (not applied).
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Healing Light, Spiritual Focus, Unyielding Faith, Deflection, Pursuit of Justice.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.
- 2026-10-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Healing Light -> Divine Strength (+0.2% DPS); Spiritual Focus -> Voice of Truth (interrupt); Deflection -> Benediction (mana); Spiritual Focus -> Purifying Power (mana); Unyielding Faith -> Purifying Power (mana); Deflection -> Benediction (mana); Pursuit of Justice -> Deflection (survival); Benediction -> Vindication (+0.2% DPS); Pursuit of Justice -> Vindication (+0.2% DPS); Deflection -> Benediction (mana). Net +0.73% on a third seed.

## Open questions (verify in the live game)

- An open-search Shockadin build: check it against the community's Shockadin builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/paladin/60/451231030001112--2322503020123011-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
