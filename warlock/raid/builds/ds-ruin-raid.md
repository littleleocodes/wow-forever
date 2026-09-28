# DS/Ruin — Demonic Sacrifice + Ruin (simulator winner adopted 2026-09-26) — 22/11/18

*[Warlock](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/11/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `ds-ruin-raid` |

## Summary

Allocation adopted on 2026-09-26 from `opt-sb-raid-raid-dps`, the best build in the community simulator (+10.6% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Both halves of DS/Ruin got cheaper: Demonic Sacrifice is now a tier-3 Demonology talent (11 points) and Ruin a 5-rank tier-3 Destruction talent. That leaves room for Agonizing Flames (+9% Destruction damage), Shadow and Flame (Conflagrate hits buff Shadow damage) and Bane of Havoc, with Suppression now giving 5% hit to all spells plus threat reduction.

## Point allocation

### Affliction (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 1/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Improved Health Funnel** | 2/2 | changed | Increases the amount of health transferred by your Health Funnel spell by 40%, reduces its health cost by 30%, and reduces all threat your Health Funnel generates by 100%. Allows Health Funnel to be used regardless of your demon's health. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Sacrifice the Succubus for the Shadow damage buff (now lasts 2 hours); tier 3 — only 11 Demonology points. Raid sim (2026-09-26): removing it costs +13% DPS.
2. **Bane** — -0.5s Shadow Bolt/Immolate/Incinerate (est.). Raid sim (2026-09-26): removing it costs +11% DPS.
3. **Improved Shadow Bolt** — Shadow Bolt crits apply +20% Shadow damage taken (est. at 5/5) — the raid's shadow debuff. Raid sim (2026-09-26): removing it costs +7% DPS.
4. **Agonizing Flames** — New: +3% Destruction damage per rank (est. 9%) plus Searing Pain crit. Raid sim (2026-09-26): removing it costs +6% DPS.
5. **Suppression** — Reworked: +1% hit with ALL spells per rank and -4% threat per rank — mandatory. Raid sim (2026-09-26): removing it costs +6% DPS.
6. **Ruin** — +100% crit damage on Destruction spells at 5/5 (est.). Raid sim (2026-09-26): removing it costs +6% DPS.
7. **Malevolence** — Raid sim (2026-09-26): removing it costs +5% DPS.
8. **Improved Corruption** — Raid sim (2026-09-26): removing it costs +4% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Amplify Curse | any utility talent legal at that tier | Measures +0.7% DPS in the community simulator (noise): these points are free to move. |
| 5 | Demonic Embrace | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |
| 2 | Improved Health Funnel | any utility talent legal at that tier | Measures +0.0% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**2 of 9** for `sb-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-sb-raid-raid-dps`](opt-sb-raid-raid-dps.md) | ours: optimizer | 22/11/18 | 575 | +0.0% | 690 | -0.5% | 1 s |
| 2 | **[`ds-ruin-raid`](ds-ruin-raid.md)** | ours: hand draft | 22/11/18 | 574 | -0.1% | 693 | +0.0% | 1 s |
| 3 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 547 | -4.9% | 658 | -5.1% | 1 s |
| 4 | *DS/Ruin* | community simulator | - | 539 | -6.2% | 647 | -6.6% | 1 s |
| 5 | *Shadow and Flame 13/11/27* | community simulator | - | 516 | -10.3% | 615 | -11.3% | 1 s |
| 6 | *Deep Affliction 35/0/16* | community simulator | - | 474 | -17.5% | 562 | -18.9% | 1 s |
| 7 | *Demonic Pact 2/31/18* | community simulator | - | 471 | -18.1% | 567 | -18.3% | 0 s |
| 8 | *Affliction* | community simulator | - | 467 | -18.7% | 553 | -20.3% | 1 s |
| 9 | *Demonic Pact* | community simulator | - | 466 | -18.9% | 557 | -19.7% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 2 changes to the base rotation; third-seed check: opt-sb-raid-raid-dps 571 -> 575 DPS (+0.7%), sim preset: DS/Ruin Pandemic 24/11/16 544 -> 547 DPS (+0.5%)):
  1. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  2. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 1)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 2 passes, the last 2026-09-28, 4 changes to the base rotation; third-seed check: opt-sb-raid-raid-dps 683 -> 690 DPS (+1.0%), sim preset: DS/Ruin Pandemic 24/11/16 653 -> 658 DPS (+0.8%)):
  1. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  2. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  3. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  4. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 2)

Before the pull: at -5s: cast Amplify Curse; at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`ds-ruin-raid`](ds-ruin-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.6 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.7 |
| 6 | if mana % < 10%: cast Life Tap | 6.6 |
| 7 | cast Amplify Curse | 0.5 |
| 8 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.8 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.4 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.3 |
| 11 | cast Shadow Bolt | 13.7 |

Lines of the simulator's rotation these builds never cast: cast Shadowburn (needs the Shadowburn talent).

Damage by ability:

| Ability | [`ds-ruin-raid`](ds-ruin-raid.md) |
|---|---|
| Shadow Bolt | 51% |
| Bane of Agony | 20% |
| Corruption | 19% |
| Immolate | 10% |
| Searing Pain | 1% |

## Notes

- Adopted from the community simulator on 2026-09-26: opt-sb-raid-raid-dps beat the previous draft by +10.6% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Immolate -> Conflagrate (Shadow and Flame buff) -> Shadow Bolt spam; refresh Immolate/Conflagrate every 20s; Curse per raid assignment.
- Malevolence (+5% Shadow crit, Affliction tier 4) would need 15 Affliction points — see the Affliction build.
- 2026-09-27 scenario audit: Siphon Life 1 -> Improved Life Tap 1. The sacrificed-Succubus Shadow Bolt rotation never casts Siphon Life (simulator 0.0%). Improved Life Tap's +20% mana per tap means fewer taps and more Shadow Bolts in long fights (scorer +1.2 points).

## Open questions (verify in the live game)

- Demonic Sacrifice values per pet in Forever (Classic: Succubus +15% Shadow, Imp +15% Fire).
- Ruin rank scaling (only rank 1 = 20% was read).
- Whether Conflagrate uptime for Shadow and Flame is worth the Immolate casts versus more Shadow Bolts.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
