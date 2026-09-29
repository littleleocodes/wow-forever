# Optimizer — Corruption 28%, Agony 18%, Shadow Bolt 30%, Drain Life 12%, Immolate 6%, Imp 6%; Siphon Life and Wrack arrive as talent effects (raid-dps) — 30/0/21

*[Warlock](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `affliction-raid` and profile `raid-dps`: score +58.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Malediction** | 2/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 2%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 5%. |

### Demonology (0)

*No points.*

### Destruction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Aftermath** | 3/5 | changed | Increases the initial damage of your Immolate spell by 30% and your Conflagrate spell has a 60% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Bane** — Removing it costs 13.6 points of score in this model.
2. **Agonizing Flames** — Removing it costs 9.0 points of score in this model.
3. **Suppression** — Removing it costs 6.9 points of score in this model.
4. **Malevolence** — Removing it costs 6.7 points of score in this model.
5. **Shadow Mastery** — Removing it costs 6.4 points of score in this model.
6. **Improved Shadow Bolt** — Removing it costs 6.3 points of score in this model.
7. **Improved Corruption** — Removing it costs 6.0 points of score in this model.
8. **Ruin** — Removing it costs 5.9 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 9** for `affliction-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md)** | ours: optimizer | 30/0/21 | 571 | +0.0% | 697 | +0.0% | 2 s |
| 2 | [`affliction-dot-raid`](affliction-dot-raid.md) | ours: hand draft | 30/0/21 | 571 | -0.0% | 697 | -0.0% | 2 s |
| 3 | *Demonic Pact 2/31/18* | community simulator | - | 536 | -6.1% | 655 | -6.1% | 0 s |
| 4 | *Demonic Pact* | community simulator | - | 531 | -7.1% | 645 | -7.4% | 1 s |
| 5 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 520 | -9.0% | 632 | -9.4% | 1 s |
| 6 | *Deep Affliction 35/0/16* | community simulator | - | 514 | -10.0% | 618 | -11.3% | 2 s |
| 7 | *DS/Ruin* | community simulator | - | 511 | -10.5% | 626 | -10.2% | 0 s |
| 8 | *Affliction* | community simulator | - | 507 | -11.3% | 609 | -12.6% | 1 s |
| 9 | *Shadow and Flame 13/11/27* | community simulator | - | 496 | -13.1% | 605 | -13.2% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: opt-affliction-raid-raid-dps 568 -> 572 DPS (+0.8%), sim preset: Demonic Pact 2/31/18 533 -> 537 DPS (+0.8%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. threshold 75% -> 55%: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.2%, pass 2)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 2 changes to the base rotation; third-seed check: opt-affliction-raid-raid-dps 696 -> 698 DPS (+0.4%), sim preset: Demonic Pact 2/31/18 652 -> 655 DPS (+0.5%)):
  1. only with 6s or more of the fight left: if mana % < 10%: cast Life Tap (+0.2%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 1)

Before the pull: at -5s: cast Amplify Curse.

| # | Priority (the first line whose condition holds is cast) | [`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.6 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 55%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.7 |
| 6 | if mana % < 10%: cast Life Tap | 6.2 |
| 7 | cast Amplify Curse | 0.5 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.9 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.4 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | cast Shadow Bolt | 13.7 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Siphon Life (needs the Siphon Life talent).

Damage by ability:

| Ability | [`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 46% |
| Bane of Agony | 19% |
| Corruption | 17% |
| Immolate | 11% |
| Pet: Auto Attack | 6% |
| Searing Pain | 1% |
| Pet: Lash of Pain | 1% |

## Notes

- Allocation taken from cand-affliction-raid-r7 on 2026-09-29: the optimizer's earlier round beat its last export in the community simulator (571 vs 566 DPS; the calibration moved the model past the better build).
- Report: warlock/talents/forever/optimizer/affliction-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
