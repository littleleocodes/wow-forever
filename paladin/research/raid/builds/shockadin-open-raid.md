# Shockadin — Raid (open talent search) — 23/0/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 23/0/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) raid build the open talent search found on 2026-11-04: every legal 51-point build with no tree rule, searched in the community simulator's shockadin-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.5% over shockadin-open-raid, the best of our builds in that rotation.

## Point allocation

### Holy (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spiritual Focus** | 1/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14% chance to not lose casting time when you take damage. |
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Consecrated Ground** | 2/2 | **NEW** | Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (0)

*No points.*

### Retribution (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 4/5 | moved | Increases your Parry chance by 4%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Holy Shock** — 98 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
2. **Vengeance** — 61 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
3. **Consecrated Ground** — 50 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
4. **Holy Conduit** — 46 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Improved Judgement** — 40 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Conviction** — 35 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Two-Handed Weapon Specialization** — 31 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
8. **Champion of the Light** — 30 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 1** for `shockadin-raid` by training-dummy DPS in the community simulator (wowsims/forever d97252f (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shockadin-open-raid`](shockadin-open-raid.md)** | ours: derived (open search) | 23/0/28 | 450 | +0.0% | 839 | +0.0% | 70 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 3 passes, the last 2026-11-03, 2 changes to the base rotation; third-seed check: shockadin-open-raid 826 -> 839 DPS (+1.6%)):
  1. threshold 0.2s -> 1.2s: if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath (+1.0%, pass 1)
  2. move to the top: if variableRef: groupReference (+0.5%, pass 1)

Before the pull: at -20s: groupReference; at -30s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -20s: move to variableRef yd; at -1.5s: if not variableRef: groupReference; at -1.5s: if variableRef: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`shockadin-open-raid`](shockadin-open-raid.md) casts/min |
|---|---|---|
| 1 | groupReference | as ready |
| 2 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 3 | groupReference | as ready |
| 4 | cast Judgement | 6.5 |
| 5 | cast Consecration | 4.7 |
| 6 | if variableRef: groupReference | as ready |
| 7 | cast Holy Strike | 5.9 |
| 8 | if Holy Shock is ready: cast Divine Favor | 0.6 |
| 9 | cast Holy Shock | 3.8 |
| 10 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.5 |

Lines of the simulator's rotation these builds never cast: cast Exorcism (its condition never held in these fights).

Damage by ability:

| Ability | [`shockadin-open-raid`](shockadin-open-raid.md) |
|---|---|
| Auto Attack | 21% |
| Judgement of Righteousness | 18% |
| Holy Strike | 16% |
| Seal of Righteousness | 15% |
| Holy Shock | 13% |
| Consecration | 13% |
| Hammer of Wrath | 2% |
| Demonic Rune | 2% |
| spell 16614 | 0% |

## Notes

- Open search result (shockadin-raid, full raid): 23/0/28 (Shockadin (a Holy/Retribution hybrid)) at 796.2 DPS; shockadin-open-raid 784.3 in the same fights; 2,020 builds simulated, 1 independent runs reached the top.
- The shockadin-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): ret-dps -8.6%; none adopted.
- A phase-1 BiS set picked for this family (_reference/data/raidsim/gear_sets/forever/tiers/paladin-hybrid-holy-retribution-bis.gear.json, item level 64.0): 815.0 DPS against 796.5 in the rotation's standard set: a lead for the gear sets (not applied).
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Spiritual Focus, Purifying Power, Infusion of Light, Deflection, Unyielding Faith, Seal of Command, Turn Evil.
- Simulator numbers are the community's model of the beta (wowsims/forever 5ad0894 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-04 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Deflection -> Benediction (mana); Infusion of Light -> Purifying Power (mana); Deflection -> Benediction (mana); Deflection -> Benediction (mana); Turn Evil -> Deflection (survival); Unyielding Faith -> Deflection (survival); Unyielding Faith -> Deflection (survival). Net -0.04% on a third seed.

## Open questions (verify in the live game)

- An open-search Shockadin build: check it against the community's Shockadin builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/paladin/60/15025110221021--4223302100131033-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
