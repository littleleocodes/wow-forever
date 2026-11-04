# Retribution — Seal of Command / Twist of Light (full raid buffs, 10/8/33) — 8/15/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 8/15/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `ret-raid-dps` |

## Summary

The build for a raid that brings Blessing of Wisdom and Mana Spring: `ret-raid-dps` until the training-dummy adoption of 2026-09-27, restored as its companion. In the community simulator's raid setting (full buffs, ElliotWood/Forever 40be98e, 3000 iterations) it does 748 DPS against `ret-raid-dps`'s 729 (+2.7%); on the training dummy, where our raid drafts are ranked (your own buffs only), it does 298 against 307 (-2.8%). Simulator numbers, not measurements. Seal of Command, Conviction, Vengeance (now a stacking buff), Two-Handed Weapon Specialization and Repentance survive; Sanctity Aura, Improved Blessing of Might and Improved Seal of the Crusader are gone. New: Sacred Arbiter (Holy Strike refreshes Judgements), Crusade, Champion of the Light (Intellect to spell damage), Instrument of Law and the Twist of Light capstone (seal twisting echoes). Improved Seals and Divine Strength from Holy, Precision (hit) from Protection.

## Point allocation

### Holy (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |

### Protection (15)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |

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

1. **Seal of Command** — Still the damage engine: 70% weapon damage Holy procs.
2. **Twist of Light** — New capstone: swapping seals grants an Echo that applies the replaced seal on the next hit — seal twisting.
3. **Improved Seals** — New: +5%/rank Seal and Judgement damage (est. 15%).
4. **Conviction** — +5% melee crit.
5. **Vengeance** — Reworked: after a non-periodic crit, +1%/rank Physical and Holy damage for 30 s, stacking 3 times (+9% at 3/3, 70291 tooltip); requires Sanctified Judgement 3.
6. **Precision** — +3% hit with all attacks and spells.
7. **Divine Strength** — +10% Strength.
8. **Champion of the Light** — New: spell damage from Intellect (est. 33%) — Judgements, Consecration, Exorcism scale.
9. **Sacred Arbiter** — New 16-point talent: Holy Strike +10% and refreshes Judgements — no more re-judging.
10. **Two-Handed Weapon Specialization** — +3% (est.) two-hander damage.
11. **Sanctified Judgement** — Mana on Judgements; prerequisite for Vengeance.
12. **Instrument of Law** — Faster Hammer of Wrath and -10% threat.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Toughness | Redoubt | Tier-1 Protection filler to unlock Precision. |
| 3 | Divine Intellect 2 + Holy Conduit 1 | Divine Intellect 5 by dropping Instrument of Law | Mana vs. threat. |

## Rank among our builds and the community simulator's

**7 of 7** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever d97252f (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 470 | +0.0% | 876 | +0.0% | 32 s |
| 2 | *Unsealed Wrath* | community simulator | - | 469 | -0.1% | 872 | -0.5% | 32 s |
| 3 | *Holy Shock* | community simulator | - | 461 | -2.0% | 759 | -13.4% | 1 s |
| 4 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 424 | -9.8% | 703 | -19.8% | 0 s |
| 5 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 423 | -10.0% | 703 | -19.8% | 1 s |
| 6 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 376 | -20.1% | 697 | -20.4% | 22 s |
| 7 | **[`ret-full-buffs-raid`](ret-full-buffs-raid.md)** | ours: hand draft | 8/15/28 | 372 | -20.8% | 697 | -20.4% | 24 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 4 passes, the last 2026-11-03, 1 changes to the base rotation; third-seed check: retribution-open-raid 865 -> 874 DPS (+1.0%), sim preset: Unsealed Wrath 863 -> 873 DPS (+1.2%), ret-raid-dps 690 -> 702 DPS (+1.7%), ret-full-buffs-raid 689 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 690 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 700 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if variableRef: cast Judgement | 7.1 |
| 3 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.6 |
| 5 | if variableRef and not Judgement is ready and variableRef: cast Holy Strike | 5.8 |
| 6 | if variableRef: cast Seal of Command | 2.2 |
| 7 | groupReference | as ready |
| 8 | groupReference | as ready |

Lines of the simulator's rotation these builds never cast: cast Seal of Righteousness (its condition never held in these fights).

Damage by ability:

| Ability | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) |
|---|---|
| Auto Attack | 25% |
| Judgement of Command | 20% |
| Seal of Command | 19% |
| Holy Strike | 18% |
| Consecration | 12% |
| Hammer of Wrath | 3% |
| Demonic Rune | 3% |
| spell 16614 | 0% |

## Notes

- Restored 2026-09-27 (user choice: keep both builds). Take `ret-raid-dps` when you bring your own mana (the dummy, small groups, no paladin or shaman in your party) and this one when a raid supplies Blessing of Wisdom and Mana Spring. The reasons under core and flex predate the 2026-09-27 training-dummy calibration.
- Rotation hypothesis: Seal of Command auto-attacks, Judgement on cooldown, Holy Strike (refreshes Judgements), Consecration/Exorcism (Holy Conduit) as mana allows, seal twists for Echoes.
- Consecration is baseline in Forever.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Vindication 2 (+2% attack power self-buff on melee hits), which also keeps the 20 points below tier 5.
- 2026-09-27 scenario audit: Repentance 1 -> Holy Conduit 1. Repentance incapacitates a Humanoid; raid bosses are immune and it gates nothing. Holy Conduit's second rank returns more mana on Consecration and Exorcism; the simulator's best Retribution build takes it (ElliotWood/Forever 40be98e: +1.8% with Vindication 3).
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 10/8/33 -> 8/15/28; Divine Intellect 2 gone (moved to Protection); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 2 gone; Twist of Light 1 gone; +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Redoubt (tier gating for Precision); +1 Sacred Duty (tier gating for Toughness); +1 Sacred Duty (tier gating for Toughness); +1 Vindication (tier gating for Champion of the Light); +1 Deflection (tier gating for Champion of the Light) (refill: the ret-dps model, raid-dps).

## Open questions (verify in the live game)

- How Twist of Light Echoes interact with Seal of Command procs — the core of a Forever Ret rotation.
- Holy Strike's damage/cooldown (new baseline ability) and whether Improved Holy Strike (Holy tier 1) beats Divine Strength.
- Vengeance stacking uptime with 5-10% crit.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
