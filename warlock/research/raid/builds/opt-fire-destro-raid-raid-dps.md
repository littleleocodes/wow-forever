# Optimizer — Immolate 30%, filler nuke 30% (Shadow Bolt until Incinerate replaces it), Searing Pain 12%, Soul Fire 10%, Corruption 8%, Imp 10%; Conflagrate and Shadowburn arrive as talent effects (raid-dps) — 20/11/20

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/11/20 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-destro-raid` and profile `raid-dps`: score +95.3% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Health Funnel** | 2/2 | changed | Increases the amount of health transferred by your Health Funnel spell by 40%, reduces its health cost by 30%, and reduces all threat your Health Funnel generates by 100%. Allows Health Funnel to be used regardless of your demon's health. |
| **Improved Imp** | 3/3 | changed | Increases the damage of your Imp's Firebolt spell by 30% and the effect of its Fire Shield spell by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Ruin** | 4/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 80%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Removing it costs 27.2 points of score in this model.
2. **Shadow and Flame** — Removing it costs 19.9 points of score in this model.
3. **Bane** — Removing it costs 19.8 points of score in this model.
4. **Shadowburn** — Removing it costs 13.5 points of score in this model.
5. **Agonizing Flames** — Removing it costs 11.0 points of score in this model.
6. **Suppression** — Removing it costs 11.0 points of score in this model.
7. **Ruin** — Removing it costs 9.1 points of score in this model.
8. **Conflagrate** — Removing it costs 8.4 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 7** for `fire-destro-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md)** | ours: optimizer | 20/11/20 | 674 | +0.0% | 756 | +0.0% | 1 s |
| 2 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 668 | -0.9% | 749 | -0.9% | 2 s |
| 3 | *SM/Ruin* | community simulator | - | 664 | -1.5% | 742 | -1.8% | 3 s |
| 4 | *Aff (Wrack)* | community simulator | - | 649 | -3.7% | 722 | -4.5% | 3 s |
| 5 | *Destro* | community simulator | - | 600 | -10.9% | 662 | -12.4% | 2 s |
| 6 | *Demo (Shadow Brand)* | community simulator | - | 581 | -13.8% | 658 | -13.0% | 3 s |
| 7 | *Demo (Fire Brand)* | community simulator | - | 568 | -15.7% | 633 | -16.3% | 3 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 5 passes, the last 2026-10-11, 15 changes to the base rotation; third-seed check: open winner 624 -> 627 DPS (+0.5%), destruction-fire-raid 615 -> 620 DPS (+0.8%), sim preset: DS/Ruin Pandemic 24/11/16 587 -> 593 DPS (+1.0%), opt-fire-destro-raid-raid-dps 592 -> 619 DPS (+4.5%)):
  1. drop: cast Shadowburn (+0.6%, pass 1)
  2. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if not Curse of the Elements is up: cast Curse of the Elements (+0.4%, pass 1)
  3. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if mana % < 10%: cast Life Tap (+0.5%, pass 1)
  4. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  5. only above 10% mana: if time left in the fight ≤ 3.5: cast Searing Pain (+0.2%, pass 2)
  6. threshold 1.5 -> 1.125: if time left in the fight ≤ 1.5: cast Shadowburn (+0.2%, pass 2)
  7. spell probe: insert before the filler: cast Conflagrate (+8.3%, pass 4)
  8. move to the top: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.9%, pass 5)
  9. insert before the filler: cast Talisman of Ephemeral Power (+0.3%, pass 5)
  10. only above 25% mana: cast Talisman of Ephemeral Power (+0.3%, pass 5)
  11. drop 'mana % ≥ 10%' from the condition: if time left in the fight ≤ 3.5 and mana % ≥ 10%: cast Searing Pain (+0.3%, pass 5)
  12. insert before the filler: cast Eureka! (+0.2%, pass 5)
  13. drop: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.2%, pass 5)
  14. only with 20s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 5)
  15. only with 10s or more of the fight left: if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-10-28, 11 changes to the base rotation; third-seed check: shadow-bolt-hybrid-fire-open-raid 768 -> 767 DPS (-0.1%), sim preset: DS/Ruin Pandemic 24/11/16 714 -> 709 DPS (-0.6%), destruction-fire-raid 754 -> 749 DPS (-0.6%), opt-fire-destro-raid-raid-dps 714 -> 745 DPS (+4.3%)):
  1. drop: cast Shadowburn (+0.8%, pass 1)
  2. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  3. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  4. spell probe: insert in the middle: cast Conflagrate (+8.2%, pass 4)
  5. insert before the filler: cast Talisman of Ephemeral Power (+0.9%, pass 5)
  6. insert before the filler: cast Eureka! (+0.2%, pass 5)
  7. only with 10s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 7)
  8. threshold 3.5 -> 5.25: if time left in the fight ≤ 3.5: cast Searing Pain (+0.2%, pass 7)
  9. only above 10% mana: cast Talisman of Ephemeral Power + threshold 10% -> 15%: if mana % ≥ 10%: cast Talisman of Ephemeral Power (+0.3%, pass 7)
  10. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption + move down below 'if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption': if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 7)
  11. drop: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.3%, pass 8)

Before the pull: at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 20s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.3 |
| 5 | if time left on Bane of Agony ≤ cast time of Bane of Agony and time left in the fight ≥ 10s: cast Bane of Agony | 2.6 |
| 6 | if mana % < 10%: cast Life Tap | 6.4 |
| 7 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 8 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.6 |
| 9 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 10 | cast Shadow Bolt (rank 9) | 14.6 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Conflagrate (needs the Conflagrate talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 53% |
| Corruption | 18% |
| Bane of Agony | 16% |
| Immolate | 11% |
| Demonic Rune | 2% |
| Searing Pain | 0% |

## Notes

- Allocation taken from cand-fire-destro-raid-r8 on 2026-10-28: the optimizer's earlier round beat its last export in the community simulator (674 vs 667 DPS; the calibration moved the model past the better build).
- Report: warlock/research/talents/forever/optimizer/fire-destro-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
