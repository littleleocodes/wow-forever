# Shockadin — Raid (open talent search) — 23/0/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 23/0/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) raid build the open talent search found on 2026-10-29: every legal 51-point build with no tree rule, searched in the community simulator's shockadin-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Holy (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Spiritual Focus** | 3/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 42% chance to not lose casting time when you take damage. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
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
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Deflection** | 1/5 | moved | Increases your Parry chance by 1%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Holy Shock** — 83 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
2. **Vengeance** — 58 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
3. **Consecrated Ground** — 46 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
4. **Improved Judgement** — 36 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
5. **Improved Seals** — 27 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
6. **Conviction** — 22 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Two-Handed Weapon Specialization** — 20 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 1** for `shockadin-raid` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shockadin-open-raid`](shockadin-open-raid.md)** | ours: derived (open search) | 23/0/28 | 418 | +0.0% | 784 | +0.0% | 70 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 2 changes to the base rotation; third-seed check: shockadin-open-raid 772 -> 784 DPS (+1.6%)):
  1. threshold 0.2s -> 1.2s: if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath (+1.0%)
  2. move to the top: if variableRef: groupReference (+0.5%)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -1.5s: if not variableRef: groupReference; at -1.5s: if variableRef: groupReference.

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
| Auto Attack | 22% |
| Judgement of Righteousness | 18% |
| Holy Strike | 17% |
| Seal of Righteousness | 14% |
| Holy Shock | 13% |
| Consecration | 12% |
| Demonic Rune | 2% |
| Hammer of Wrath | 2% |
| spell 16614 | 0% |

## Notes

- Open search result (shockadin-raid, full raid): 24/0/27 (Shockadin (a Holy/Retribution hybrid)) at 759.1 DPS;  in the same fights; 2,349 builds simulated, 1 independent runs reached the top.
- The shockadin-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- A phase-1 BiS set picked for this family (_reference/data/raidsim/gear_sets/forever/tiers/paladin-hybrid-holy-retribution-bis.gear.json, item level 64.6): 764.9 DPS against 759.2 in the rotation's standard set: a lead for the gear sets (not applied).
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Healing Light, Spiritual Focus, Unyielding Faith, Deflection, Pursuit of Justice.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.
- 2026-10-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Healing Light -> Divine Strength (+0.2% DPS); Spiritual Focus -> Voice of Truth (interrupt); Deflection -> Benediction (mana); Spiritual Focus -> Purifying Power (mana); Unyielding Faith -> Purifying Power (mana); Deflection -> Benediction (mana); Pursuit of Justice -> Deflection (survival); Benediction -> Vindication (+0.2% DPS); Pursuit of Justice -> Vindication (+0.2% DPS); Deflection -> Benediction (mana). Net +0.73% on a third seed.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 24/0/27 -> 23/0/28; Divine Intellect 5 gone (moved to Protection); Reverence 3 -> 2 (rank cap); Voice of Truth 1 gone; Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 1 gone; +1 Holy Conduit (tier gating for Divine Precision); +1 Holy Conduit (tier gating for Divine Precision); +1 Divine Precision (tier gating for Consecrated Ground); +1 Spiritual Focus (tier gating for Consecrated Ground); +1 Spiritual Focus (tier gating for Consecrated Ground); +1 Spiritual Focus (tier gating for Consecrated Ground); +1 Seal of Command (tier gating for Vengeance); +1 Two-Handed Weapon Specialization (tier gating for Vengeance); +1 Vindication (tier gating for Champion of the Light); +1 Deflection (tier gating for Champion of the Light); refill +2 Champion of the Light (refill: the ret-dps model, raid-dps).

## Open questions (verify in the live game)

- An open-search Shockadin build: check it against the community's Shockadin builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/paladin/60/451231030001112--2322503020123011-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
