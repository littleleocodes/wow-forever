# Destruction — Incinerate (open talent search) — 10/11/30

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/11/30 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction raid build the open talent search found on 2026-11-08: every legal 51-point build with no tree rule, searched in the community simulator's incinerate-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +5.3% over destruction-incinerate-raid, the best of our builds in that rotation.

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
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |

### Destruction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Fire and Brimstone** | 3/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 25%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

## Core talents (priority order)

1. **Shadow and Flame** — 144 DPS lost without it (18% of the build in a full raid; removal, 12,000 fights).
2. **Conflagrate** — 95 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
3. **Demonic Sacrifice** — 83 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
4. **Bane** — 81 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
5. **Agonizing Flames** — 50 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
6. **Suppression** — 44 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
7. **Ruin** — 43 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Improved Shadow Bolt** — 40 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 3** for `incinerate-raid` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`destruction-incinerate-open-raid`](destruction-incinerate-open-raid.md)** | ours: derived (open search) | 10/11/30 | 703 | +0.0% | 793 | +0.0% | 1 s |
| 2 | [`destruction-incinerate-raid`](destruction-incinerate-raid.md) | ours: hand draft | 9/11/31 | 676 | -3.8% | 755 | -4.8% | 1 s |
| 3 | *Destro* | community simulator | - | 639 | -9.0% | 712 | -10.1% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-12, 4 changes to the base rotation; third-seed check: open winner 294 -> 625 DPS (+112.5%), destruction-incinerate-raid 550 -> 593 DPS (+7.8%)):
  1. insert before the filler: cast Shadow Bolt (+110.0%)
  2. move to the top: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.8%)
  3. threshold 3.5 -> 5.25: if time left in the fight ≤ 3.5: cast Searing Pain (+0.2%)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption + threshold 5.25 -> 3.938: if time left in the fight ≤ 5.25: cast Searing Pain (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-09, 7 passes, the last 2026-11-08, 12 changes to the base rotation; third-seed check: open winner 414 -> 788 DPS (+90.1%), destruction-incinerate-raid 697 -> 749 DPS (+7.4%), sim preset: Destro 703 -> 708 DPS (+0.7%)):
  1. insert before the filler: cast Shadowburn (+6.9%, pass 1)
  2. insert before the filler: cast Shadow Bolt (+1.8%, pass 1)
  3. insert at the top: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.4%, pass 1)
  4. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.5%, pass 1)
  5. move to the top: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.3%, pass 1)
  6. only with 10s or more of the fight left: cast Shadowburn (+0.2%, pass 1)
  7. only above 60% mana: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.4%, pass 2)
  8. only with 6s or more of the fight left: if mana % < 10%: cast Life Tap (+0.2%, pass 2)
  9. only with 20s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 3)
  10. drop: if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune (+0.2%, pass 4)
  11. move down below 'if time left on Immolate ≤ cast time of Immolate and mana % ≥ 60%: cast Immolate': if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 6)
  12. threshold 20s -> 10s: if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate (+0.2%, pass 6)

Before the pull: at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`destruction-incinerate-open-raid`](destruction-incinerate-open-raid.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.938: cast Searing Pain | 0.5 |
| 6 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.7 |
| 7 | if mana % < 10%: cast Life Tap | 6.4 |
| 8 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 9 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.5 |
| 10 | if Immolate is on the target: cast Conflagrate | 3.9 |
| 11 | cast Shadow Bolt (rank 9) | 12.3 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Incinerate (needs the Incinerate talent).

Damage by ability:

| Ability | [`destruction-incinerate-open-raid`](destruction-incinerate-open-raid.md) |
|---|---|
| Shadow Bolt | 46% |
| Corruption | 17% |
| Bane of Agony | 16% |
| Immolate | 11% |
| Conflagrate | 8% |
| Demonic Rune | 2% |
| Searing Pain | 1% |

## Notes

- The best incinerate build: +5.3% over destruction-incinerate-raid, the best of our builds in incinerate-raid. The spec's raid pick may be another variant; the page lists this one among the spec's other builds.
- Open search result (incinerate-raid, full raid): 10/11/30 (Destruction) at 789.0 DPS; destruction-incinerate-raid 749.2 in the same fights; 2,507 builds simulated, 1 independent runs reached the top.
- The incinerate-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): affliction-raid -0.2%, fire-destro-raid +0.1%, sb-raid -0.0%, demonology-raid -0.2%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Unholy Power, Improved Voidwalker.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.
- 2026-11-08 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Voidwalker -> Demonic Embrace (survival); Improved Voidwalker -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Embrace (survival); Unholy Power -> Demonic Aegis (survival); Unholy Power -> Demonic Aegis (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Destruction build: check it against the community's Destruction builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/warlock/60/253-0005023001-055030500310035-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
