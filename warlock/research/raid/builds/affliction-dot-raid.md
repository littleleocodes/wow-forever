# Affliction — DoT / Malevolence / Nightfall (simulator winner adopted 2026-09-27) — 30/0/21

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `sm-ruin-raid` |

## Summary

Allocation adopted on 2026-09-27 from `opt-affliction-raid-raid-dps`, the best build in the community simulator (+4.7% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Allocation adopted on 2026-09-26 from `opt-affliction-raid-raid-dps`, the best build in the community simulator (+3.2% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: The SM/Ruin successor is a real DoT spec: Corruption, Bane of Agony and Siphon Life buffed by Malediction (replaced by Grim Reach in build 70425), Pandemic (DoT crit damage) and Malevolence (Shadow crit), Shadow Mastery, and the Drain Hope capstone (+10% Shadow DoT damage on the target), with Shadow Bolt as the filler backed by Improved Shadow Bolt and a 5-rank Ruin. Keeps a pet.

## Point allocation

### Affliction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
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
| **Aftermath** | 3/5 | changed | Increases the initial damage of your Immolate spell by 30% and your Conflagrate spell has a 60% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Bane** — Shadow Bolt cast time. Raid sim (2026-09-26): removing it costs +11% DPS. Raid sim (2026-09-27): removing it costs +10% DPS.
2. **Improved Shadow Bolt** — Shadow vulnerability debuff for the raid. Raid sim (2026-09-26): removing it costs +7% DPS. Raid sim (2026-09-27): removing it costs +6% DPS.
3. **Agonizing Flames** — Raid sim (2026-09-26): removing it costs +6% DPS. Raid sim (2026-09-27): removing it costs +5% DPS.
4. **Ruin** — Crit damage for the Shadow Bolt filler. Raid sim (2026-09-26): removing it costs +5% DPS. Raid sim (2026-09-27): removing it costs +5% DPS.
5. **Suppression** — 5% hit, -20% threat. Raid sim (2026-09-26): removing it costs +5% DPS. Raid sim (2026-09-27): removing it costs +5% DPS.
6. **Malevolence** — New: +5% Shadow crit (est.) — DoTs crit in Forever. Raid sim (2026-09-26): removing it costs +5% DPS. Raid sim (2026-09-27): removing it costs +5% DPS.
7. **Shadow Mastery** — Raid sim (2026-09-27): removing it costs +4% DPS.
8. **Improved Corruption** — Raid sim (2026-09-26): removing it costs +4% DPS. Raid sim (2026-09-27): removing it costs +4% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Aftermath | any utility talent legal at that tier | Measures +0.9% DPS in the community simulator (noise): these points are free to move. |
| 1 | Amplify Curse | any utility talent legal at that tier | Measures +0.5% DPS in the community simulator (noise): these points are free to move. |
| 2 | Nightfall | any utility talent legal at that tier | Measures +0.3% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**2 of 7** for `affliction-raid` by training-dummy DPS in the community simulator (wowsims/forever 92c4c35 (client 70755)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-affliction-raid-raid-dps`](opt-affliction-raid-raid-dps.md) | ours: optimizer | 30/0/21 | 709 | +0.0% | 812 | +0.0% | 0 s |
| 2 | **[`affliction-dot-raid`](affliction-dot-raid.md)** | ours: hand draft | 30/0/21 | 702 | -1.0% | 808 | -0.5% | 0 s |
| 3 | *SM/Ruin* | community simulator | - | 698 | -1.5% | 808 | -0.5% | 0 s |
| 4 | *Demo (Shadow Brand)* | community simulator | - | 649 | -8.4% | 753 | -7.3% | 0 s |
| 5 | *Demo (Fire Brand)* | community simulator | - | 633 | -10.7% | 724 | -10.9% | 0 s |
| 6 | *Destro* | community simulator | - | 603 | -14.9% | 685 | -15.7% | 0 s |
| 7 | *Aff (Wrack)* | community simulator | - | 592 | -16.5% | 662 | -18.5% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 4 passes, the last 2026-10-02, 4 changes to the base rotation; third-seed check: ml: Affliction 638 -> 642 DPS (+0.5%), opt-affliction-raid-raid-dps 637 -> 641 DPS (+0.5%), sim preset: Demonic Pact 2/31/18 590 -> 593 DPS (+0.5%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. threshold 75% -> 55%: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.2%, pass 2)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 2)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 9 passes, the last 2026-11-04, 9 changes to the base rotation; third-seed check: opt-affliction-raid-raid-dps 810 -> 815 DPS (+0.6%), sim preset: SM/Ruin 800 -> 810 DPS (+1.2%), affliction-dot-raid 804 -> 810 DPS (+0.8%)):
  1. only with 6s or more of the fight left: if mana % < 10%: cast Life Tap (+0.2%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 1)
  3. insert before the filler: cast Talisman of Ephemeral Power (+0.4%, pass 5)
  4. only above 25% mana: cast Talisman of Ephemeral Power (+0.2%, pass 5)
  5. insert before the filler: cast Eureka! (+0.2%, pass 5)
  6. threshold 75% -> 65%: if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion (+0.4%, pass 7)
  7. only with 10s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 7)
  8. drop: if time left on Siphon Life ≤ cast time of Siphon Life: cast Siphon Life (+0.4%, pass 8)
  9. insert before the filler: cast Weakness Analyzer (+0.3%, pass 9)

Before the pull: at -5s: cast Amplify Curse.

| # | Priority (the first line whose condition holds is cast) | [`affliction-dot-raid`](affliction-dot-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 55%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.3 |
| 6 | if mana % < 10%: cast Life Tap | 7.3 |
| 7 | cast Amplify Curse | 0.7 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.6 |
| 9 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 11 | cast Shadow Bolt (rank 9) | 14.2 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent); cast Siphon Life (needs the Siphon Life talent).

Damage by ability:

| Ability | [`affliction-dot-raid`](affliction-dot-raid.md) |
|---|---|
| Shadow Bolt | 48% |
| Bane of Agony | 18% |
| Corruption | 16% |
| Immolate | 11% |
| Pet: Auto Attack | 4% |
| Demonic Rune | 1% |
| Pet: Lash of Pain | 1% |
| Searing Pain | 0% |

## Notes

- Adopted from the community simulator on 2026-09-27: opt-affliction-raid-raid-dps beat the previous draft by +4.7% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Adopted from the community simulator on 2026-09-26: opt-affliction-raid-raid-dps beat the previous draft by +3.2% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Improved Corruption now reduces cast time by 0.4s per rank instead of 0.4s total — 5/5 is instant; not taken here because tier-1 Affliction already holds Suppression + Improved Life Tap. Add it by dropping Malediction if Corruption is cast on every target.
- Debuff-slot limits decide this build's value: it wants Corruption, Bane of Agony, Siphon Life and Drain Hope on the boss.

## Open questions (verify in the live game)

- Shadow Mastery per-rank value (1% or 2%).
- Does Forever keep a raid debuff cap? Four DoTs per warlock would not fit a Classic-style 16-slot limit.
- Nightfall (Shadow Trance) at 2%/rank — worth 2 points over the fillers?

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
