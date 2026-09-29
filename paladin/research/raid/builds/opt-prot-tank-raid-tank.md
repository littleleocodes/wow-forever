# Optimizer — Shield tank: Consecration 25%, Holy Strike 20% (Forever; Classic uses Seal/Judgement of Righteousness instead), seal+judgement 15%, Retribution Aura 10%, white 20%, Holy Shield blocks via talent (raid-tank) — 0/23/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/23/28 (Holy / Protection / Retribution) |
| **Role** | TANK — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `prot-tank` and profile `raid-tank`: score +46.9% (tank score: 0.5 x threat gain + 0.5 x mitigation gain + 0.1 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (0)

*No points.*

### Protection (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Improved Righteous Fury** | 3/3 | changed | While Righteous Fury is active, all damage taken is reduced by 6%. |
| **Shield Specialization** | 1/3 | changed | Increases the amount of damage absorbed by your shield by 10%, and gives your blocks a 33% chance to restore 6% of your maximum Mana. May only occur once every 3 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |
| **One-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with one-handed melee weapons by 10%. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |

### Retribution (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Benediction** | 3/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 6%. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 200, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage and healing by up to 100% of your Intellect. |

## Core talents (priority order)

1. **Champion of the Light** — Removing it costs 8.4 points of score in this model.
2. **Deflection** — Removing it costs 5.5 points of score in this model.
3. **Improved Righteous Fury** — Removing it costs 5.0 points of score in this model.
4. **Vengeance** — Removing it costs 4.7 points of score in this model.
5. **Vindication** — Removing it costs 3.6 points of score in this model.
6. **Templar's Bulwark** — Removing it costs 3.0 points of score in this model.
7. **Anticipation** — Removing it costs 3.0 points of score in this model.
8. **Conviction** — Removing it costs 3.0 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 5** for `prot-tank` by tank value in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |
|---|---|---|---|---|---|---|---|
| 1 | [`prot-tank`](prot-tank.md) | ours: hand draft | 0/23/28 | 1.000 | +0.0% | 537 | 993 |
| 2 | **[`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md)** | ours: optimizer | 0/23/28 | 1.000 | +0.0% | 537 | 993 |
| 3 | *Protection 0/45/6* | community simulator | - | 0.910 | -9.0% | 459 | 1027 |
| 4 | *P4 Prot* | community simulator | - | 0.890 | -11.0% | 472 | 1100 |
| 5 | *P5 Prot* | community simulator | - | 0.883 | -11.7% | 465 | 1103 |

## Rotation (community simulator, raid setting)

- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 5 changes to the base rotation; third-seed check: prot-tank 451 -> 496 DPS (+10.0%), sim preset: Protection 0/45/6 371 -> 405 DPS (+9.1%)):
  1. insert before the filler: if health % < 10%: cast Lay on Hands (+7.8%, pass 1)
  2. drop the condition: if time left on Seal of Righteousness < 2s: cast Judgement (+4.3%, pass 1)
  3. insert at the top: cast Holy Shield (+1.3%, pass 1)
  4. insert at the top: cast Templar's Bulwark (+1.4%, pass 2)
  5. insert before the filler: cast Retribution Aura (+0.2%, pass 3)

Before the pull: at -30s: cast Righteous Fury; at -3.5s: cast Seal of Righteousness; at -2s: cast Holy Shield.

| # | Priority (the first line whose condition holds is cast) | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) casts/min |
|---|---|---|
| 1 | cast Templar's Bulwark | 0.3 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time left on Seal of Righteousness ≤ 1s: cast Seal of Righteousness | 2.3 |
| 4 | cast Consecration | 6.6 |
| 5 | cast Holy Strike | 5.7 |
| 6 | if health % < 10%: cast Lay on Hands | 0.3 |
| 7 | cast Retribution Aura | 25.4 |

Lines of the simulator's rotation these builds never cast: cast Holy Shield (needs the Holy Shield talent); cast Judgement (its condition never held in these fights).

Damage by ability (threat for tanks):

| Ability | [`opt-prot-tank-raid-tank`](opt-prot-tank-raid-tank.md) |
|---|---|
| Auto Attack | 27% |
| Seal of Righteousness | 16% |
| Consecration | 15% |
| Judgement of Righteousness | 12% |
| Holy Strike | 11% |
| Lay on Hands | 9% |
| Retribution Aura | 5% |
| OtherActionManaGain | 4% |
| Thorns | 1% |

## Notes

- Report: paladin/research/talents/forever/optimizer/prot-tank-raid-tank.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
