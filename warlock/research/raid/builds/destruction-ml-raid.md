# Destruction — Raid (machine-learning search) — 9/11/31

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/11/31 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry sb-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

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
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 10% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 10% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

## Rank among our builds and the community simulator's

**5 of 9** for `sb-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`shadow-bolt-hybrid-open-raid`](shadow-bolt-hybrid-open-raid.md) | ours: derived (open search) | 21/11/19 | 700 | +0.0% | 795 | +0.0% | 0 s |
| 2 | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) | ours: optimizer | 22/11/18 | 697 | -0.5% | 786 | -1.1% | 0 s |
| 3 | [`ds-ruin-raid`](ds-ruin-raid.md) | ours: hand draft | 22/11/18 | 696 | -0.6% | 789 | -0.7% | 0 s |
| 4 | *SM/Ruin* | community simulator | - | 686 | -2.0% | 772 | -2.9% | 0 s |
| 5 | **[`destruction-ml-raid`](destruction-ml-raid.md)** | ours: derived (ML search) | 9/11/31 | 681 | -2.7% | 770 | -3.1% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`destruction-ml-raid`](destruction-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if mana % < 10%: cast Life Tap | 6.6 |
| 7 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.6 |
| 8 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.4 |
| 9 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.3 |
| 10 | cast Conflagrate | 4.5 |
| 11 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 12 | cast Shadow Bolt (rank 9) | 11.9 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Amplify Curse (needs the Amplify Curse talent); cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`destruction-ml-raid`](destruction-ml-raid.md) |
|---|---|
| Shadow Bolt | 45% |
| Corruption | 16% |
| Bane of Agony | 16% |
| Immolate | 11% |
| Conflagrate | 10% |
| Demonic Rune | 2% |
| Searing Pain | 1% |

## Notes

- Against the best hand draft destruction-incinerate-raid in a full raid, same gear and fights (100,000, one seed): +7.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow destruction-incinerate-raid: Unholy Power → Demonic Embrace (5 points), Improved Voidwalker → Demonic Aegis (the same DPS as the search winner 9/11/31 on one seed, 30,000 fights).
- Search result (full raid): 9/11/31 at 769.9 ± 0.13 DPS over 100,000 fights; runner-up 9/11/31 (+0.00%; the winner takes Demonic Aegis 1; the runner-up Improved Health Funnel 1); 4,208 builds simulated; certificate: none of its 200 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 9/11/31 at 736.9 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 10/11/30 at 681.5 DPS.

## Open questions (verify in the live game)

- A machine-searched Destruction build: check it against the community's Destruction builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
