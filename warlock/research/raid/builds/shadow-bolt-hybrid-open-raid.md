# Shadow Bolt hybrid — Raid (open talent search) — 9/11/31

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/11/31 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) raid build the open talent search found on 2026-11-08: every legal 51-point build with no tree rule, searched in the community simulator's fire-destro-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +4.1% over shadow-bolt-hybrid-fire-open-raid, the best of our builds in that rotation.

## Point allocation

### Affliction (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 2/5 | changed | Reduces the casting time of your Corruption spell by 0.8 sec and increases the damage it deals by 4%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 1/5 | changed | Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

## Core talents (priority order)

1. **Shadow and Flame** — 145 DPS lost without it (18% of the build in a full raid; removal, 12,000 fights).
2. **Conflagrate** — 90 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Demonic Sacrifice** — 82 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
4. **Bane** — 77 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
5. **Agonizing Flames** — 50 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Ruin** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
7. **Suppression** — 42 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Improved Shadow Bolt** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 8** for `fire-destro-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md)** | ours: derived (open search) | 9/11/31 | 702 | +0.0% | 787 | +0.0% | 1 s |
| 2 | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) | ours: optimizer | 20/11/20 | 661 | -5.7% | 741 | -5.9% | 1 s |
| 3 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 654 | -6.8% | 733 | -6.8% | 1 s |
| 4 | *SM/Ruin* | community simulator | - | 648 | -7.7% | 722 | -8.3% | 1 s |
| 5 | *Destro* | community simulator | - | 638 | -9.1% | 706 | -10.4% | 1 s |
| 6 | *Aff (Wrack)* | community simulator | - | 602 | -14.2% | 660 | -16.2% | 1 s |
| 7 | *Demo (Shadow Brand)* | community simulator | - | 570 | -18.8% | 640 | -18.7% | 1 s |
| 8 | *Demo (Fire Brand)* | community simulator | - | 558 | -20.5% | 617 | -21.6% | 1 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 12 passes, the last 2026-11-07, 12 changes to the base rotation; third-seed check: open winner 711 -> 786 DPS (+10.7%), shadow-bolt-hybrid-fire-open-raid 764 -> 756 DPS (-1.1%), sim preset: SM/Ruin 739 -> 729 DPS (-1.4%), destruction-fire-raid 751 -> 738 DPS (-1.7%), opt-fire-destro-raid-raid-dps 762 -> 746 DPS (-2.1%)):
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

| # | Priority (the first line whose condition holds is cast) | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 20s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 5 | if time left on Bane of Agony ≤ cast time of Bane of Agony and time left in the fight ≥ 10s: cast Bane of Agony | 2.6 |
| 6 | if mana % < 10%: cast Life Tap | 6.5 |
| 7 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 8 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 9 | cast Conflagrate | 3.8 |
| 10 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 11 | cast Shadow Bolt (rank 9) | 12.4 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) |
|---|---|
| Shadow Bolt | 47% |
| Corruption | 16% |
| Bane of Agony | 16% |
| Immolate | 11% |
| Conflagrate | 8% |
| Demonic Rune | 2% |
| Searing Pain | 0% |

## Notes

- +1.1% over the best hand draft of the spec, ds-ruin-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (fire-destro-raid, full raid): 9/11/31 (Shadow Bolt hybrid (an Affliction/Destruction hybrid)) at 787.3 DPS; shadow-bolt-hybrid-fire-open-raid 756.3, opt-fire-destro-raid-raid-dps 745.7, destruction-fire-raid 738.4 in the same fights; 2,884 builds simulated, 1 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): ds-ruin-raid 779.1, opt-sb-raid-raid-dps 777.4.
- The fire-destro-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.3%, sb-raid -0.1%, demonology-raid -0.3%, incinerate-raid -0.1%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Demonic Embrace, Demonic Aegis.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid build: check it against the community's Shadow Bolt hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/252-0050203001-055031500310035-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
