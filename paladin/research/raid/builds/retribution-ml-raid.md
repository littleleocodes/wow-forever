# Retribution — Raid (machine-learning search) — 9/14/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/14/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry ret-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Holy (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Reverence** | 1/2 | **NEW** | Allows 15% of your Mana regeneration to continue while casting. |

### Protection (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Toughness** | 4/5 | moved | Increases your armor value from items by 8%. |

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

## Rank among our builds and the community simulator's

**5 of 6** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Unsealed Wrath* | community simulator | - | 447 | +0.0% | 837 | +0.0% | 32 s |
| 2 | *Holy Shock* | community simulator | - | 437 | -2.2% | 728 | -13.0% | 1 s |
| 3 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 402 | -10.0% | 675 | -19.3% | 0 s |
| 4 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 401 | -10.2% | 675 | -19.3% | 1 s |
| 5 | **[`retribution-ml-raid`](retribution-ml-raid.md)** | ours: derived (ML search) | 9/14/28 | 358 | -19.9% | 670 | -19.9% | 22 s |
| 6 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 355 | -20.5% | 670 | -19.9% | 24 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 1 changes to the base rotation; third-seed check: ret-full-buffs-raid 662 -> 672 DPS (+1.5%), sim preset: Unsealed Wrath 829 -> 837 DPS (+1.0%), ret-raid-dps 663 -> 674 DPS (+1.6%), opt-ret-dps-raid-dps 663 -> 674 DPS (+1.6%), retribution-ml-raid 662 -> 672 DPS (+1.6%)):
  1. insert in the middle: cast Consecration (+1.2%)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`retribution-ml-raid`](retribution-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if variableRef: cast Judgement | 7.2 |
| 3 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.6 |
| 5 | if variableRef and not Judgement is ready and variableRef: cast Holy Strike | 5.8 |
| 6 | if variableRef: cast Seal of Command | 2.2 |
| 7 | groupReference | as ready |
| 8 | groupReference | as ready |

Lines of the simulator's rotation these builds never cast: cast Seal of Righteousness (its condition never held in these fights).

Damage by ability:

| Ability | [`retribution-ml-raid`](retribution-ml-raid.md) |
|---|---|
| Auto Attack | 25% |
| Judgement of Command | 21% |
| Seal of Command | 19% |
| Holy Strike | 18% |
| Consecration | 12% |
| Hammer of Wrath | 3% |
| Demonic Rune | 3% |
| spell 16614 | 1% |

## Notes

- Against the best hand draft ret-full-buffs-raid in the same gear and fights (100,000, one seed): +1.7% (under the 2% bar: the hand draft stays the pick).
- Search result: 11/8/32 at 554.6 ± 0.07 DPS over 100,000 fights; runner-up 11/8/32 (+0.00%; the winner takes Toughness 5; the runner-up Redoubt 5); 1,631 builds simulated; certificate: none of its 211 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 12/8/31 at 520.4 DPS on the dummy (other talents: _reference/dps-rankings.md).
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Retribution: its full-raid winner is +0.06% against it, under the 0.5% bar for a new build.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 11/8/32 -> 9/14/28; Divine Intellect 5 gone (moved to Protection); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 2 gone; Twist of Light 1 gone; +1 Divine Strength (tier gating for Improved Seals); +1 Divine Strength (tier gating for Improved Seals); +1 Divine Strength (tier gating for Improved Seals); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Sacred Duty (tier gating for Toughness); +1 Sacred Duty (tier gating for Toughness); +1 Vindication (tier gating for Vengeance); +1 Vindication (tier gating for Champion of the Light); +1 Deflection (tier gating for Champion of the Light); -1 Toughness (over 51) (refill: the ret-dps model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Retribution build: check it against the community's Retribution builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
