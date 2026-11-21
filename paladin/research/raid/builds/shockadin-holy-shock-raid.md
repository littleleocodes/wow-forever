# Shockadin — Holy Shock (the simulator's own build) — 23/0/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 23/0/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Holy Shock paladin build (23/0/28), played with our Shockadin rotation: 808.8 / 808.5 DPS against our 803.8 / 804.3 (full raid, 2026-11-20). The simulator's own Holy Shock rotation swaps in the Manual Crowd Pummeler before the pull, which our bench cannot do.

## Point allocation

### Holy (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Consecrated Ground** | 2/2 | **NEW** | Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (0)

*No points.*

### Retribution (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Pursuit of Justice** | 1/2 | changed | Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Champion of the Light** — Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec
2. **Vengeance** — Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike
3. **Holy Shock** — Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally
4. **Consecrated Ground** — Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration
5. **Two-Handed Weapon Specialization** — Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped

## Rank among our builds and the community simulator's

**1 of 2** for `shockadin-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shockadin-holy-shock-raid`](shockadin-holy-shock-raid.md)** | ours: derived (simulator preset) | 23/0/28 | 479 | +0.0% | 808 | +0.0% | 48 s |
| 2 | [`shockadin-open-raid`](shockadin-open-raid.md) | ours: derived (open search) | 23/0/28 | 479 | -0.1% | 803 | -0.6% | 48 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 4 passes, the last 2026-11-10, 2 changes to the base rotation; third-seed check: shockadin-open-raid 820 -> 833 DPS (+1.6%)):
  1. threshold 0.2s -> 1.2s: if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath (+1.0%, pass 1)
  2. move to the top: if variableRef: groupReference (+0.5%, pass 1)

Before the pull: at -20s: groupReference; at -30s: if Manual Crowd Pummeler is known: swap to the Swap1 item set; at -20s: move to “Pull range” yd; at -1.5s: if not “Has assigned judgement”: groupReference; at -1.5s: if “Has assigned judgement”: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`shockadin-holy-shock-raid`](shockadin-holy-shock-raid.md) casts/min |
|---|---|---|
| 1 | if time into the fight ≥ “Delay Major CDs”: use every other cooldown when ready | as ready |
| 2 | if “Should swap from MCP”: swap to the Main item set | as ready |
| 3 | if “Should swap to MCP”: swap to the Swap1 item set | as ready |
| 4 | cast Judgement | 6.9 |
| 5 | cast Consecration | 5.6 |
| 6 | if “Should refresh seal” and “Is using Seal of Righteousness”: cast Seal of Righteousness | 2.7 |
| 7 | cast Holy Strike | 6.0 |
| 8 | if Holy Shock is ready: cast Divine Favor | 0.6 |
| 9 | cast Holy Shock | 4.3 |
| 10 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.8 |

Lines of the simulator's rotation these builds never cast: cast Seal of Command, cast Exorcism (its condition never held in these fights).

Damage by ability:

| Ability | [`shockadin-holy-shock-raid`](shockadin-holy-shock-raid.md) |
|---|---|
| Auto Attack | 20% |
| Seal of Righteousness | 18% |
| Judgement of Righteousness | 16% |
| Consecration | 14% |
| Holy Strike | 14% |
| Holy Shock | 13% |
| Hammer of Wrath | 3% |
| Demonic Rune | 2% |

## Notes

- The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% ahead on two seeds and passing the spec's rules.
- Simulator numbers are the community's model of the game, not in-game measurements.

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/paladin/retribution/builds/holy_shock.siml>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
