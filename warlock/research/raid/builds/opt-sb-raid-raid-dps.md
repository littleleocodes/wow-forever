# Optimizer — Shadow Bolt 74%, Corruption 12%, Curse/Bane of Agony 6%, Immolate 4%, Imp 4% (a raid warlock's pet does little) (raid-dps) — 22/11/18

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/11/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `sb-raid` and profile `raid-dps`: score +106.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
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

1. **Conflagrate** — Removing it costs 27.2 points of score in this model.
2. **Demonic Sacrifice** — Removing it costs 27.0 points of score in this model.
3. **Shadow and Flame** — Removing it costs 26.3 points of score in this model.
4. **Bane** — Removing it costs 21.2 points of score in this model.
5. **Agonizing Flames** — Removing it costs 13.9 points of score in this model.
6. **Suppression** — Removing it costs 11.6 points of score in this model.
7. **Improved Shadow Bolt** — Removing it costs 11.0 points of score in this model.
8. **Fel Vitality** — Removing it costs 8.5 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 11** for `sb-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) | ours: hand draft | 20/11/20 | 649 | +0.0% | 731 | +0.0% | 0 s |
| 2 | **[`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md)** | ours: optimizer | 22/11/18 | 646 | -0.6% | 726 | -0.7% | 1 s |
| 3 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 642 | -1.1% | 725 | -0.9% | 2 s |
| 4 | [`destruction-ml-raid`](destruction-ml-raid.md) | ours: hand draft | 10/11/30 | 634 | -2.3% | 710 | -2.9% | 0 s |
| 5 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 612 | -5.7% | 686 | -6.2% | 1 s |
| 6 | *DS/Ruin* | community simulator | - | 602 | -7.3% | 676 | -7.5% | 1 s |
| 7 | *Shadow and Flame 13/11/27* | community simulator | - | 557 | -14.3% | 623 | -14.8% | 1 s |
| 8 | *Deep Affliction 35/0/16* | community simulator | - | 534 | -17.7% | 589 | -19.4% | 1 s |
| 9 | *Demonic Pact 2/31/18* | community simulator | - | 530 | -18.4% | 595 | -18.7% | 0 s |
| 10 | *Affliction* | community simulator | - | 526 | -19.0% | 581 | -20.5% | 1 s |
| 11 | *Demonic Pact* | community simulator | - | 523 | -19.5% | 586 | -19.8% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 6 passes, the last 2026-10-11, 6 changes to the base rotation; third-seed check: open winner 649 -> 649 DPS (-0.0%), opt-sb-raid-raid-dps 646 -> 645 DPS (-0.3%), sim preset: DS/Ruin Pandemic 24/11/16 614 -> 612 DPS (-0.3%), ds-ruin-raid 642 -> 643 DPS (+0.1%), destruction-ml-raid 603 -> 634 DPS (+5.1%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Conflagrate (+8.0%, pass 4)
  4. insert before the filler: cast Talisman of Ephemeral Power (+0.6%, pass 6)
  5. only above 25% mana: cast Talisman of Ephemeral Power (+0.4%, pass 6)
  6. insert before the filler: cast Eureka! (+0.2%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-10-11, 7 changes to the base rotation; third-seed check: open winner 732 -> 731 DPS (-0.2%), opt-sb-raid-raid-dps 727 -> 726 DPS (-0.1%), sim preset: DS/Ruin Pandemic 24/11/16 690 -> 686 DPS (-0.6%), ds-ruin-raid 724 -> 725 DPS (+0.1%), destruction-ml-raid 679 -> 712 DPS (+4.8%)):
  1. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 2)
  5. spell probe: insert before the filler: cast Conflagrate (+7.7%, pass 4)
  6. threshold 60% -> 80%: if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune (+0.2%, pass 5)
  7. insert before the filler: cast Talisman of Ephemeral Power (+0.5%, pass 6)

Before the pull: at -5s: cast Amplify Curse; at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if mana % < 10%: cast Life Tap | 6.8 |
| 7 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.6 |
| 8 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.3 |
| 9 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 10 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 11 | cast Eureka! | 0.7 |
| 12 | cast Shadow Bolt | 14.4 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Amplify Curse (needs the Amplify Curse talent); cast Conflagrate (needs the Conflagrate talent).

Damage by ability:

| Ability | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 54% |
| Bane of Agony | 18% |
| Corruption | 17% |
| Immolate | 11% |
| Searing Pain | 0% |

## Notes

- Allocation taken from cand-sb-raid-r9 on 2026-10-03: the optimizer's earlier round beat its last export in the community simulator (594 vs 581 DPS; the calibration moved the model past the better build).
- Report: warlock/research/talents/forever/optimizer/sb-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
