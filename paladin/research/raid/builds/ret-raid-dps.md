# Retribution — Seal of Command (simulator winner adopted 2026-09-27) — 17/6/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/6/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `ret-raid-dps` |

## Summary

Allocation adopted on 2026-09-27 from `cand-ret-dps-r1`, the best build in the community simulator (+2.9% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. On today's trees (the 2026-10-31 repair for client 70707) it takes Seal of Command, Sacred Arbiter (Holy Strike refreshes Judgements), Champion of the Light (Intellect to spell damage), Conviction, Vengeance (a stacking buff), Two-Handed Weapon Specialization, Vindication, Improved Seals, Divine Strength and Precision (hit).

## Point allocation

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |

### Protection (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 1/3 | changed | Improves your chance to hit by 1%. |

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
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Champion of the Light** — New: spell damage from Intellect (est. 33%) — Judgements, Consecration, Exorcism scale. Raid sim (2026-09-27): removing it costs +12% DPS.
2. **Seal of Command** — Still the damage engine: 70% weapon damage Holy procs. Raid sim (2026-09-27): removing it costs +11% DPS.
3. **Sanctified Judgement** — Mana on Judgements; prerequisite for Vengeance. Raid sim (2026-09-27): removing it costs +8% DPS.
4. **Conviction** — +5% melee crit. Raid sim (2026-09-27): removing it costs +7% DPS.
5. **Improved Seals** — New: +5%/rank Seal and Judgement damage (est. 15%). Raid sim (2026-09-27): removing it costs +7% DPS.
6. **Vengeance** — Reworked: after a non-periodic crit, +1%/rank Physical and Holy damage for 30 s, stacking 3 times (+9% at 3/3, 70291 tooltip); requires Sanctified Judgement 3. Raid sim (2026-09-27): removing it costs +6% DPS.
7. **Reverence** — Raid sim (2026-09-27): removing it costs +4% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Vindication | any utility talent legal at that tier | Measures +0.8% DPS in the community simulator (noise): these points are free to move. |
| 1 | Divine Favor | any utility talent legal at that tier | Measures +0.4% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**4 of 7** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Unsealed Wrath* | community simulator | - | 510 | +0.0% | 821 | -0.1% | 13 s |
| 2 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 483 | -5.3% | 823 | +0.0% | 32 s |
| 3 | *Holy Shock* | community simulator | - | 465 | -8.9% | 715 | -13.1% | 0 s |
| 4 | **[`ret-raid-dps`](ret-raid-dps.md)** | ours: hand draft | 17/6/28 | 426 | -16.5% | 659 | -19.8% | 0 s |
| 5 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 426 | -16.5% | 659 | -19.8% | 0 s |
| 6 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 393 | -22.9% | 657 | -20.1% | 7 s |
| 7 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 391 | -23.3% | 658 | -20.0% | 8 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`ret-raid-dps`](ret-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if variableRef: cast Judgement | 7.7 |
| 3 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 1.3 |
| 5 | if variableRef and not Judgement is ready and variableRef: cast Holy Strike | 6.0 |
| 6 | if variableRef: cast Seal of Command | 2.3 |
| 7 | groupReference | as ready |
| 8 | groupReference | as ready |

Lines of the simulator's rotation these builds never cast: cast Seal of Righteousness (its condition never held in these fights).

Damage by ability:

| Ability | [`ret-raid-dps`](ret-raid-dps.md) |
|---|---|
| Auto Attack | 23% |
| Judgement of Command | 19% |
| Seal of Command | 17% |
| Consecration | 17% |
| Holy Strike | 16% |
| Hammer of Wrath | 5% |
| Demonic Rune | 2% |

## Notes

- Adopted from the community simulator on 2026-09-27: cand-ret-dps-r1 beat the previous draft by +2.9% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Seal of Command auto-attacks, Judgement on cooldown, Holy Strike (refreshes Judgements), Consecration/Exorcism (Holy Conduit) as mana allows, seal twists for Echoes.
- Consecration is baseline in Forever.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Vindication 2 (+2% attack power self-buff on melee hits), which also keeps the 20 points below tier 5.
- 2026-09-27 scenario audit: Repentance 1 -> Holy Conduit 1. Repentance incapacitates a Humanoid; raid bosses are immune and it gates nothing. Holy Conduit's second rank returns more mana on Consecration and Exorcism; the simulator's best Retribution build takes it (ElliotWood/Forever 40be98e: +1.8% with Vindication 3).
- Companion build `ret-full-buffs-raid` (restored 2026-09-27): in a raid with Blessing of Wisdom and Mana Spring it does 748 DPS against this build's 729 (+2.7%, ElliotWood/Forever 40be98e, 3000 iterations); this build wins on the training dummy (307 vs 298).
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 17/0/34 -> 17/6/28; Divine Intellect 5 gone (moved to Protection); Reverence 3 -> 2 (rank cap); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 2 gone; Twist of Light 1 gone; +1 Deflection (tier gating for Champion of the Light); refill +2 Holy Conduit, +2 Purifying Power, +2 Divine Precision, +5 Redoubt, +1 Precision (refill: the ret-dps model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Twist of Light; a tree change or a repair took them out).

## Open questions (verify in the live game)

- How Unsealed Wrath's stored seal copies (Twist of Light until build 70753) interact with Seal of Command procs.
- Holy Strike's damage/cooldown (new baseline ability) and whether Improved Holy Strike (Holy tier 1) beats Divine Strength.
- Vengeance stacking uptime with 5-10% crit.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
