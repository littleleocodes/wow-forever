# Destruction — Raid (machine-learning search) — 10/11/30

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/11/30 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry sb-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Affliction (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 3/5 | changed | Reduces the casting time of your Corruption spell by 1.2 sec and increases the damage it deals by 6%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 2/3 | changed | Reduces the Mana cost of your Destruction spells by 6%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 10% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 10% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

## Rank among our builds and the community simulator's

**4 of 11** for `sb-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever fork 2ce8265 (client 70291)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) | ours: derived (open search) | 20/11/20 | 641 | +0.0% | 723 | +0.0% | 1 s |
| 2 | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) | ours: optimizer | 22/11/18 | 637 | -0.6% | 718 | -0.6% | 1 s |
| 3 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 633 | -1.1% | 716 | -0.8% | 2 s |
| 4 | **[`destruction-ml-raid`](destruction-ml-raid.md)** | ours: derived (ML search) | 10/11/30 | 627 | -2.1% | 705 | -2.4% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`destruction-ml-raid`](destruction-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 1.5: cast Shadowburn | 0.3 |
| 6 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 7 | if mana % < 10%: cast Life Tap | 6.7 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.5 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.2 |
| 11 | cast Conflagrate | 4.4 |
| 12 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 13 | cast Shadow Bolt | 12.0 |

Lines of the simulator's rotation these builds never cast: cast Amplify Curse (needs the Amplify Curse talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`destruction-ml-raid`](destruction-ml-raid.md) |
|---|---|
| Shadow Bolt | 46% |
| Corruption | 16% |
| Bane of Agony | 16% |
| Immolate | 10% |
| Conflagrate | 10% |
| Shadowburn | 1% |
| Searing Pain | 1% |

## Notes

- Against the best hand draft destruction-incinerate-raid in the same gear and fights (100,000, one seed): +12.0% (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow destruction-incinerate-raid: Demonic Energies → Demonic Aegis (2 points) (the same DPS as the search winner 10/11/30 on one seed, 30,000 fights).
- Search result: 10/11/30 at 627.7 ± 0.10 DPS over 100,000 fights; runner-up 10/11/30 (+0.00%; the winner takes Demonic Energies 2; the runner-up Demonic Energies 1, Improved Voidwalker 1); 3,993 builds simulated; certificate: the neighbours ahead on the short run (of 392) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 10/11/30 at 597.9 DPS on the dummy (other talents: _reference/dps-rankings.md).
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Destruction: its full-raid winner is +0.46% against it, under the 0.5% bar for a new build.

## Open questions (verify in the live game)

- A machine-searched Destruction build: check it against the community's Destruction builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
