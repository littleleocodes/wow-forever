# Shadow Bolt hybrid — Fire (open talent search) — 20/11/20

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/11/20 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) raid build the open talent search found on 2026-10-12: every legal 51-point build with no tree rule, searched in the community simulator's fire-destro-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.8% over destruction-fire-raid, the best of our builds in that rotation.

## Point allocation

### Affliction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 1/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 2/5 | changed | Reduces the casting time of your Corruption spell by 0.8 sec and increases the damage it deals by 4%. |
| **Malediction** | 2/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 2%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |

### Destruction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 2/3 | changed | Reduces the Mana cost of your Destruction spells by 6%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — 81 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
2. **Bane** — 81 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Improved Shadow Bolt** — 57 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Agonizing Flames** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Ruin** — 43 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Suppression** — 35 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Malevolence** — 35 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Pandemic** — 21 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 10** for `fire-destro-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md)** | ours: derived (open search) | 20/11/20 | 618 | +0.0% | 700 | +0.0% | 3 s |
| 2 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 613 | -0.8% | 689 | -1.5% | 8 s |
| 3 | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) | ours: optimizer | 10/11/30 | 613 | -0.8% | 685 | -2.1% | 2 s |
| 4 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 586 | -5.1% | 657 | -6.1% | 5 s |
| 5 | *DS/Ruin* | community simulator | - | 578 | -6.4% | 650 | -7.2% | 3 s |
| 6 | *Shadow and Flame 13/11/27* | community simulator | - | 536 | -13.2% | 596 | -14.9% | 5 s |
| 7 | *Deep Affliction 35/0/16* | community simulator | - | 513 | -17.0% | 567 | -19.0% | 4 s |
| 8 | *Demonic Pact 2/31/18* | community simulator | - | 509 | -17.6% | 572 | -18.3% | 4 s |
| 9 | *Affliction* | community simulator | - | 507 | -18.0% | 559 | -20.2% | 4 s |
| 10 | *Demonic Pact* | community simulator | - | 503 | -18.6% | 562 | -19.7% | 4 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 7 passes, the last 2026-10-11, 10 changes to the base rotation; third-seed check: open winner 707 -> 709 DPS (+0.2%), destruction-fire-raid 691 -> 697 DPS (+0.8%), sim preset: DS/Ruin Pandemic 24/11/16 661 -> 667 DPS (+0.9%), opt-fire-destro-raid-raid-dps 663 -> 693 DPS (+4.5%)):
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

Before the pull: at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 20s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.3 |
| 5 | if time left on Bane of Agony ≤ cast time of Bane of Agony and time left in the fight ≥ 10s: cast Bane of Agony | 2.5 |
| 6 | if mana % < 10%: cast Life Tap | 7.0 |
| 7 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 8 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.5 |
| 9 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 10 | cast Shadow Bolt | 14.4 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Conflagrate (needs the Conflagrate talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md) |
|---|---|
| Shadow Bolt | 53% |
| Bane of Agony | 18% |
| Corruption | 17% |
| Immolate | 12% |
| Searing Pain | 0% |

## Notes

- The best fire build: +1.8% over destruction-fire-raid, the best of our builds in fire-destro-raid. The spec's raid pick may be another variant; the page lists this one among the spec's other builds.
- Open search result (fire-destro-raid, full raid): 20/11/20 (Shadow Bolt hybrid (an Affliction/Destruction hybrid)) at 709.6 DPS; destruction-fire-raid 697.1 in the same fights; 4,669 builds simulated, 2 independent runs reached the top.
- The fire-destro-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.6%, sb-raid -0.5%, demonology-raid -0.5%, incinerate-raid -0.9%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Health Funnel, Improved Imp, Unholy Power, Demonic Aegis.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-12 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Health Funnel -> Demonic Aegis (survival); Improved Health Funnel -> Demonic Embrace (survival); Improved Imp -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival). Net +0.01% on a third seed.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid build: check it against the community's Shadow Bolt hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/15220020035-2103103001-0550205003-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
