# Shadow Bolt hybrid — Fire (open talent search) — 20/11/20

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/11/20 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) raid build the open talent search found on 2026-11-01: every legal 51-point build with no tree rule, searched in the community simulator's fire-destro-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). 

## Point allocation

### Affliction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 3/5 | changed | Reduces the casting time of your Corruption spell by 1.2 sec and increases the damage it deals by 6%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 2/3 | changed | Reduces the Mana cost of your Destruction spells by 6%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — 88 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
2. **Bane** — 84 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Improved Shadow Bolt** — 59 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Agonizing Flames** — 47 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Ruin** — 43 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Malevolence** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Suppression** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Improved Corruption** — 24 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 8** for `fire-destro-raid` by training-dummy DPS in the community simulator (wowsims/forever 92c4c35 (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md)** | ours: derived (open search) | 20/11/20 | 663 | +0.0% | 742 | +0.0% | 1 s |
| 2 | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) | ours: optimizer | 20/11/20 | 655 | -1.3% | 733 | -1.3% | 1 s |
| 3 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 648 | -2.2% | 725 | -2.4% | 1 s |
| 4 | *SM/Ruin* | community simulator | - | 642 | -3.2% | 716 | -3.6% | 1 s |
| 5 | *Destro* | community simulator | - | 630 | -5.0% | 695 | -6.3% | 1 s |
| 6 | *Aff (Wrack)* | community simulator | - | 596 | -10.2% | 653 | -12.0% | 1 s |
| 7 | *Demo (Shadow Brand)* | community simulator | - | 563 | -15.1% | 635 | -14.4% | 1 s |
| 8 | *Demo (Fire Brand)* | community simulator | - | 551 | -16.9% | 612 | -17.6% | 1 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 10 passes, the last 2026-11-04, 12 changes to the base rotation; third-seed check: shadow-bolt-hybrid-fire-open-raid 746 -> 745 DPS (-0.1%), sim preset: SM/Ruin 722 -> 718 DPS (-0.6%), destruction-fire-raid 733 -> 727 DPS (-0.7%), opt-fire-destro-raid-raid-dps 744 -> 735 DPS (-1.2%)):
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
  12. insert before the filler: cast Weakness Analyzer (+0.4%, pass 10)

Before the pull: at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 20s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.3 |
| 5 | if time left on Bane of Agony ≤ cast time of Bane of Agony and time left in the fight ≥ 10s: cast Bane of Agony | 2.6 |
| 6 | if mana % < 10%: cast Life Tap | 6.8 |
| 7 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 8 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.5 |
| 9 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 10 | cast Shadow Bolt (rank 9) | 14.4 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Conflagrate (needs the Conflagrate talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md) |
|---|---|
| Shadow Bolt | 52% |
| Bane of Agony | 18% |
| Corruption | 17% |
| Immolate | 11% |
| Demonic Rune | 2% |
| Searing Pain | 0% |

## Notes

- The best fire build: +1.4% over opt-fire-destro-raid-raid-dps, the best of our builds in fire-destro-raid. The spec's raid pick may be another variant; the page lists this one among the spec's other builds.
- Open search result (fire-destro-raid, full raid): 20/11/20 (Shadow Bolt hybrid (an Affliction/Destruction hybrid)) at 767.3 DPS; opt-fire-destro-raid-raid-dps 756.5, destruction-fire-raid 749.2 in the same fights; 5,529 builds simulated, 2 independent runs reached the top.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.3%, sb-raid -0.1%, demonology-raid -0.3%, incinerate-raid -0.1%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Demonic Embrace, Demonic Aegis.
- Simulator numbers are the community's model of the beta (wowsims/forever 54ceac6 (client 70707) with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid build: check it against the community's Shadow Bolt hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/25300020035-0050203001-0550205003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
