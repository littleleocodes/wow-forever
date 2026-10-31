# Shadow Bolt hybrid — Raid (open talent search) — 21/11/19

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/11/19 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) raid build the open talent search found on 2026-10-28: every legal 51-point build with no tree rule, searched in the community simulator's sb-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.6% over ds-ruin-raid, the best of our builds in that rotation.

## Point allocation

### Affliction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 3/5 | changed | Reduces the casting time of your Corruption spell by 1.2 sec and increases the damage it deals by 6%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 1/3 | changed | Reduces the Mana cost of your Destruction spells by 3%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — 93 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
2. **Bane** — 84 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Improved Shadow Bolt** — 62 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Agonizing Flames** — 48 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Ruin** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Malevolence** — 40 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Suppression** — 39 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Improved Corruption** — 24 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 9** for `sb-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md)** | ours: derived (open search) | 21/11/19 | 700 | +0.0% | 795 | +0.0% | 0 s |
| 2 | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) | ours: optimizer | 22/11/18 | 697 | -0.5% | 786 | -1.1% | 0 s |
| 3 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 696 | -0.6% | 789 | -0.7% | 0 s |
| 4 | *SM/Ruin* | community simulator | - | 686 | -2.0% | 772 | -2.9% | 0 s |
| 5 | [`destruction-ml-raid`](destruction-ml-raid.md) | ours: derived (ML search) | 9/11/31 | 681 | -2.7% | 770 | -3.1% | 0 s |
| 6 | *Aff (Wrack)* | community simulator | - | 671 | -4.2% | 752 | -5.4% | 0 s |
| 7 | *Destro* | community simulator | - | 615 | -12.3% | 683 | -14.0% | 0 s |
| 8 | *Demo (Shadow Brand)* | community simulator | - | 593 | -15.4% | 674 | -15.1% | 0 s |
| 9 | *Demo (Fire Brand)* | community simulator | - | 579 | -17.3% | 646 | -18.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 6 passes, the last 2026-10-11, 6 changes to the base rotation; third-seed check: open winner 649 -> 649 DPS (-0.0%), opt-sb-raid-raid-dps 646 -> 645 DPS (-0.3%), sim preset: DS/Ruin Pandemic 24/11/16 614 -> 612 DPS (-0.3%), ds-ruin-raid 642 -> 643 DPS (+0.1%), destruction-ml-raid 603 -> 634 DPS (+5.1%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 1)
  3. spell probe: insert before the filler: cast Conflagrate (+8.0%, pass 4)
  4. insert before the filler: cast Talisman of Ephemeral Power (+0.6%, pass 6)
  5. only above 25% mana: cast Talisman of Ephemeral Power (+0.4%, pass 6)
  6. insert before the filler: cast Eureka! (+0.2%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 10 passes, the last 2026-10-28, 7 changes to the base rotation; third-seed check: open winner 788 -> 794 DPS (+0.7%), ds-ruin-raid 784 -> 789 DPS (+0.7%), sim preset: SM/Ruin 769 -> 773 DPS (+0.5%), opt-sb-raid-raid-dps 787 -> 787 DPS (+0.1%), destruction-ml-raid 731 -> 764 DPS (+4.5%), shadow-bolt-hybrid-open-raid 787 -> 785 DPS (-0.2%)):
  1. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 2)
  5. spell probe: insert before the filler: cast Conflagrate (+7.7%, pass 4)
  6. threshold 60% -> 80%: if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune (+0.2%, pass 5)
  7. insert before the filler: cast Talisman of Ephemeral Power (+0.5%, pass 6)

Before the pull: at -5s: cast Amplify Curse; at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.3 |
| 6 | if mana % < 10%: cast Life Tap | 7.0 |
| 7 | cast Amplify Curse | 0.6 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.6 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 12 | cast Shadow Bolt (rank 9) | 14.3 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Conflagrate (needs the Conflagrate talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) |
|---|---|
| Shadow Bolt | 52% |
| Bane of Agony | 19% |
| Corruption | 17% |
| Immolate | 11% |
| Demonic Rune | 1% |
| Searing Pain | 0% |

## Notes

- +0.6% over the best hand draft of the spec, ds-ruin-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (sb-raid, full raid): 21/11/19 (Shadow Bolt hybrid (an Affliction/Destruction hybrid)) at 794.8 DPS; ds-ruin-raid 790.3, opt-sb-raid-raid-dps 788.1, shadow-bolt-hybrid-open-raid 786.0, destruction-ml-raid 763.7 in the same fights; 2,636 builds simulated, 1 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): opt-fire-destro-raid-raid-dps 755.8, destruction-fire-raid 749.0.
- The sb-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.1%, fire-destro-raid -1.0%, demonology-raid -1.2%, incinerate-raid -1.0%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Demonic Embrace, Demonic Aegis.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid build: check it against the community's Shadow Bolt hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/25300020135-0050203001-0550105003-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
