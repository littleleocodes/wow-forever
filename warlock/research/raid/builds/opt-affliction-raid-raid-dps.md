# Optimizer — Corruption 28%, Agony 18%, Shadow Bolt 30%, Drain Life 12%, Immolate 6%, Imp 6%; Siphon Life and Wrack arrive as talent effects (raid-dps) — 30/0/21

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `affliction-raid` and profile `raid-dps`: score +66.9% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Nightfall** | 2/2 | changed | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 10%. |

### Demonology (0)

*No points.*

### Destruction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Bane** — Removing it costs 14.6 points of score in this model.
2. **Shadow Mastery** — Removing it costs 13.2 points of score in this model.
3. **Agonizing Flames** — Removing it costs 9.8 points of score in this model.
4. **Improved Shadow Bolt** — Removing it costs 8.6 points of score in this model.
5. **Suppression** — Removing it costs 7.3 points of score in this model.
6. **Malevolence** — Removing it costs 7.2 points of score in this model.
7. **Improved Corruption** — Removing it costs 6.6 points of score in this model.
8. **Ruin** — Removing it costs 6.5 points of score in this model.

## Rank among our builds and the community simulator's

**1 of 7** for `affliction-raid` by training-dummy DPS in the community simulator (wowsims/forever bac92db (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md)** | ours: optimizer | 30/0/21 | 711 | +0.0% | 813 | +0.0% | 0 s |
| 2 | [`affliction-dot-raid`](affliction-dot-raid.md) | ours: hand draft | 30/0/21 | 704 | -1.0% | 808 | -0.6% | 0 s |
| 3 | *SM/Ruin* | community simulator | - | 701 | -1.5% | 809 | -0.5% | 0 s |
| 4 | *Aff (Wrack)* | community simulator | - | 689 | -3.2% | 796 | -2.2% | 0 s |
| 5 | *Demo (Shadow Brand)* | community simulator | - | 650 | -8.6% | 754 | -7.3% | 0 s |
| 6 | *Demo (Fire Brand)* | community simulator | - | 634 | -10.9% | 725 | -10.9% | 0 s |
| 7 | *Destro* | community simulator | - | 605 | -14.9% | 686 | -15.7% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-10-02, 4 changes to the base rotation; third-seed check: ml: Affliction 638 -> 642 DPS (+0.5%), opt-affliction-raid-raid-dps 637 -> 641 DPS (+0.5%), sim preset: Demonic Pact 2/31/18 590 -> 593 DPS (+0.5%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. threshold 75% -> 55%: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.2%, pass 2)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 2)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 8 passes, the last 2026-11-01, 8 changes to the base rotation; third-seed check: opt-affliction-raid-raid-dps 811 -> 815 DPS (+0.4%), sim preset: SM/Ruin 804 -> 813 DPS (+1.0%), affliction-dot-raid 805 -> 808 DPS (+0.3%)):
  1. only with 6s or more of the fight left: if mana % < 10%: cast Life Tap (+0.2%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 1)
  3. insert before the filler: cast Talisman of Ephemeral Power (+0.4%, pass 5)
  4. only above 25% mana: cast Talisman of Ephemeral Power (+0.2%, pass 5)
  5. insert before the filler: cast Eureka! (+0.2%, pass 5)
  6. threshold 75% -> 65%: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.4%, pass 7)
  7. only with 10s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 7)
  8. drop: if time left on Siphon Life ≤ cast time of Siphon Life: cast Siphon Life (+0.4%, pass 8)

Before the pull: at -5s: cast Amplify Curse.

| # | Priority (the first line whose condition holds is cast) | [`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 55%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if mana % < 10%: cast Life Tap | 6.5 |
| 7 | cast Amplify Curse | 0.7 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.7 |
| 9 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | cast Shadow Bolt (rank 9) | 14.7 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Siphon Life (needs the Siphon Life talent).

Damage by ability:

| Ability | [`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 49% |
| Bane of Agony | 18% |
| Corruption | 16% |
| Immolate | 10% |
| Pet: Auto Attack | 4% |
| Demonic Rune | 1% |
| Pet: Lash of Pain | 1% |
| Searing Pain | 0% |

## Notes

- Report: warlock/research/talents/forever/optimizer/affliction-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
