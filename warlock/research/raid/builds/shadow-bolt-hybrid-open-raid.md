# Shadow Bolt hybrid — Raid (open talent search) — 20/11/20

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 20/11/20 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) raid build the open talent search found on 2026-10-12: every legal 51-point build with no tree rule, searched in the community simulator's sb-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.6% over opt-sb-raid-raid-dps, the best of our builds in that rotation.

## Point allocation

### Affliction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 2/5 | changed | Reduces the casting time of your Corruption spell by 0.8 sec and increases the damage it deals by 4%. |
| **Malediction** | 1/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 1%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |

### Destruction (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 1/3 | changed | Reduces the Mana cost of your Destruction spells by 3%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — 85 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
2. **Bane** — 78 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
3. **Improved Shadow Bolt** — 60 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Agonizing Flames** — 45 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Ruin** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Suppression** — 37 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Malevolence** — 36 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Pandemic** — 22 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 11** for `sb-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md)** | ours: derived (open search) | 20/11/20 | 641 | +0.0% | 723 | +0.0% | 1 s |
| 2 | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) | ours: optimizer | 22/11/18 | 637 | -0.6% | 718 | -0.6% | 1 s |
| 3 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 633 | -1.1% | 716 | -0.8% | 2 s |
| 4 | [`destruction-ml-raid`](destruction-ml-raid.md) | ours: derived (ML search) | 10/11/30 | 627 | -2.1% | 705 | -2.4% | 0 s |
| 5 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 604 | -5.7% | 679 | -6.0% | 1 s |
| 6 | *DS/Ruin* | community simulator | - | 595 | -7.1% | 668 | -7.5% | 1 s |
| 7 | *Shadow and Flame 13/11/27* | community simulator | - | 549 | -14.3% | 618 | -14.5% | 1 s |
| 8 | *Deep Affliction 35/0/16* | community simulator | - | 527 | -17.7% | 581 | -19.6% | 1 s |
| 9 | *Demonic Pact 2/31/18* | community simulator | - | 522 | -18.4% | 587 | -18.7% | 1 s |
| 10 | *Affliction* | community simulator | - | 520 | -18.8% | 573 | -20.7% | 1 s |
| 11 | *Demonic Pact* | community simulator | - | 517 | -19.3% | 580 | -19.8% | 0 s |

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

| # | Priority (the first line whose condition holds is cast) | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 1.5: cast Shadowburn | 0.2 |
| 6 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 7 | if mana % < 10%: cast Life Tap | 6.8 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.6 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 12 | cast Shadow Bolt | 14.5 |

Lines of the simulator's rotation these builds never cast: cast Amplify Curse (needs the Amplify Curse talent); cast Conflagrate (needs the Conflagrate talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) |
|---|---|
| Shadow Bolt | 54% |
| Bane of Agony | 18% |
| Corruption | 16% |
| Immolate | 11% |
| Shadowburn | 1% |
| Searing Pain | 1% |

## Notes

- +0.9% over the best hand draft of the spec, ds-ruin-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (sb-raid, full raid): 20/11/20 (Shadow Bolt hybrid (an Affliction/Destruction hybrid)) at 731.1 DPS; opt-sb-raid-raid-dps 726.6, ds-ruin-raid 724.5, destruction-ml-raid 711.9 in the same fights; 4,633 builds simulated, 2 independent runs reached the top.
- The spec's other builds on the pages (their best entry, full raid): destruction-fire-raid 692.5.
- The sb-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.4%, fire-destro-raid +0.2%, demonology-raid -0.7%, incinerate-raid -1.6%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Imp, Unholy Power, Improved Voidwalker.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-12 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Imp -> Demonic Embrace (survival); Improved Imp -> Demonic Embrace (survival); Improved Voidwalker -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Aegis (survival); Unholy Power -> Demonic Aegis (survival). Net -0.04% on a third seed.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Hybrid Affliction/Destruction: its full-raid winner is +0.02% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid build: check it against the community's Shadow Bolt hybrid builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/25210020035-0204013001-0550105103-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
