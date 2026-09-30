# Optimizer — Immolate 30%, filler nuke 30% (Shadow Bolt until Incinerate replaces it), Searing Pain 12%, Soul Fire 10%, Corruption 8%, Imp 10%; Conflagrate and Shadowburn arrive as talent effects (raid-dps) — 22/11/18

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/11/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-destro-raid` and profile `raid-dps`: score +82.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Improved Bane of Agony** | 1/2 | **NEW** | Increases the damage done by your Bane of Agony by 5%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Ruin** | 4/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 80%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Removing it costs 22.7 points of score in this model.
2. **Bane** — Removing it costs 16.4 points of score in this model.
3. **Suppression** — Removing it costs 10.3 points of score in this model.
4. **Malevolence** — Removing it costs 9.4 points of score in this model.
5. **Agonizing Flames** — Removing it costs 9.2 points of score in this model.
6. **Improved Shadow Bolt** — Removing it costs 8.3 points of score in this model.
7. **Improved Corruption** — Removing it costs 7.8 points of score in this model.
8. **Pandemic** — Removing it costs 7.2 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 9** for `fire-destro-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 612 | +0.0% | 725 | +0.0% | 3 s |
| 2 | **[`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md)** | ours: optimizer | 22/11/18 | 612 | +0.0% | 725 | +0.0% | 3 s |
| 3 | *DS/Ruin Pandemic 24/11/16* | community simulator | - | 586 | -4.3% | 693 | -4.4% | 3 s |
| 4 | *DS/Ruin* | community simulator | - | 577 | -5.7% | 686 | -5.4% | 3 s |
| 5 | *Shadow and Flame 13/11/27* | community simulator | - | 552 | -9.8% | 651 | -10.2% | 2 s |
| 6 | *Deep Affliction 35/0/16* | community simulator | - | 515 | -15.9% | 602 | -16.9% | 3 s |
| 7 | *Affliction* | community simulator | - | 507 | -17.2% | 594 | -18.0% | 3 s |
| 8 | *Demonic Pact 2/31/18* | community simulator | - | 505 | -17.5% | 602 | -17.0% | 3 s |
| 9 | *Demonic Pact* | community simulator | - | 501 | -18.2% | 593 | -18.2% | 3 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 6 changes to the base rotation; third-seed check: destruction-fire-raid 543 -> 559 DPS (+3.0%), sim preset: DS/Ruin Pandemic 24/11/16 519 -> 534 DPS (+2.9%)):
  1. drop: cast Shadowburn (+0.6%, pass 1)
  2. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if not Curse of the Elements is up: cast Curse of the Elements (+0.4%, pass 1)
  3. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if mana % < 10%: cast Life Tap (+0.5%, pass 1)
  4. only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.2%, pass 1)
  5. only above 10% mana: if time left in the fight ≤ 3.5: cast Searing Pain (+0.2%, pass 2)
  6. threshold 1.5 -> 1.125: if time left in the fight ≤ 1.5: cast Shadowburn (+0.2%, pass 2)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-27, 3 passes, the last 2026-09-29, 3 changes to the base rotation; third-seed check: destruction-fire-raid 651 -> 665 DPS (+2.1%), sim preset: DS/Ruin Pandemic 24/11/16 622 -> 635 DPS (+2.0%)):
  1. drop: cast Shadowburn (+0.8%, pass 1)
  2. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  3. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)

Before the pull: at -1.5s: cast Life Tap.

| # | Priority (the first line whose condition holds is cast) | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 1.125: cast Shadowburn | 0.3 |
| 5 | if time left in the fight ≤ 3.5 and mana % ≥ 10%: cast Searing Pain | 0.4 |
| 6 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.9 |
| 7 | if mana % < 10%: cast Life Tap | 6.7 |
| 8 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 9 | if time left on Corruption ≤ cast time of Corruption: cast Corruption | 3.3 |
| 10 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.3 |
| 11 | cast Shadow Bolt | 13.9 |

Damage by ability:

| Ability | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 50% |
| Bane of Agony | 19% |
| Corruption | 18% |
| Immolate | 11% |
| Shadowburn | 1% |
| Searing Pain | 1% |

## Notes

- Report: warlock/research/talents/forever/optimizer/fire-destro-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
