# Optimizer — Shadow Bolt 74%, Corruption 12%, Curse/Bane of Agony 6%, Immolate 4%, Imp 4% (a raid warlock's pet does little) (raid-dps) — 22/11/18

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/11/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `sb-raid` and profile `raid-dps`: score +91.6% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Improved Bane of Agony** | 1/2 | **NEW** | Increases the damage done by your Bane of Agony by 5%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Removing it costs 26.5 points of score in this model.
2. **Bane** — Removing it costs 17.8 points of score in this model.
3. **Agonizing Flames** — Removing it costs 12.0 points of score in this model.
4. **Suppression** — Removing it costs 10.8 points of score in this model.
5. **Malevolence** — Removing it costs 10.0 points of score in this model.
6. **Improved Corruption** — Removing it costs 9.0 points of score in this model.
7. **Improved Shadow Bolt** — Removing it costs 8.5 points of score in this model.
8. **Ruin** — Removing it costs 7.9 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 9** for `sb-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md)** | ours: optimizer | 22/11/18 | 566 | +0.0% | 675 | -0.4% | 1 s |
| 2 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 566 | -0.1% | 678 | +0.0% | 1 s |
| 3 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 540 | -4.6% | 643 | -5.2% | 1 s |
| 4 | *DS/Ruin* | community simulator | - | 533 | -5.9% | 635 | -6.3% | 1 s |
| 5 | *Shadow and Flame 13/11/27* | community simulator | - | 509 | -10.0% | 601 | -11.3% | 1 s |
| 6 | *Deep Affliction 35/0/16* | community simulator | - | 471 | -16.9% | 553 | -18.4% | 1 s |
| 7 | *Demonic Pact 2/31/18* | community simulator | - | 466 | -17.7% | 557 | -17.8% | 0 s |
| 8 | *Affliction* | community simulator | - | 464 | -18.0% | 545 | -19.5% | 1 s |
| 9 | *Demonic Pact* | community simulator | - | 461 | -18.5% | 549 | -19.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 2 changes to the base rotation; third-seed check: opt-sb-raid-raid-dps 571 -> 575 DPS (+0.7%), sim preset: DS/Ruin Pandemic 24/11/16 544 -> 546 DPS (+0.5%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 4 changes to the base rotation; third-seed check: opt-sb-raid-raid-dps 683 -> 689 DPS (+1.0%), sim preset: DS/Ruin Pandemic 24/11/16 653 -> 658 DPS (+0.8%)):
  1. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 2)

Before the pull: at -5s: cast Amplify Curse; at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.5 |
| 6 | if mana % < 10%: cast Life Tap | 6.7 |
| 7 | cast Amplify Curse | 0.5 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.7 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.4 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | cast Shadow Bolt | 13.9 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent).

Damage by ability:

| Ability | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 51% |
| Bane of Agony | 19% |
| Corruption | 19% |
| Immolate | 10% |
| Searing Pain | 1% |

## Notes

- Report: warlock/research/talents/forever/optimizer/sb-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
