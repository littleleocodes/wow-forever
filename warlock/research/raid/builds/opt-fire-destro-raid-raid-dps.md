# Optimizer — Immolate 30%, filler nuke 30% (Shadow Bolt until Incinerate replaces it), Searing Pain 12%, Soul Fire 10%, Corruption 8%, Imp 10%; Conflagrate and Shadowburn arrive as talent effects (raid-dps) — 10/11/30

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/11/30 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-destro-raid` and profile `raid-dps`: score +96.9% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Fire and Brimstone** | 2/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 17%. |
| **Shadow and Flame** | 5/5 | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 10% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 10% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

## Core talents (priority order)

1. **Demonic Sacrifice** — Removing it costs 27.2 points of score in this model.
2. **Shadow and Flame** — Removing it costs 20.5 points of score in this model.
3. **Bane** — Removing it costs 20.1 points of score in this model.
4. **Shadowburn** — Removing it costs 13.4 points of score in this model.
5. **Conflagrate** — Removing it costs 12.7 points of score in this model.
6. **Suppression** — Removing it costs 11.1 points of score in this model.
7. **Agonizing Flames** — Removing it costs 11.0 points of score in this model.
8. **Improved Shadow Bolt** — Removing it costs 8.4 points of score in this model.

## Rank among our builds and the community simulator's

**3 of 10** for `fire-destro-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`shadow-bolt-hybrid-fire-open-raid`](shadow-bolt-hybrid-fire-open-raid.md) | ours: derived (open search) | 20/11/20 | 618 | +0.0% | 700 | +0.0% | 3 s |
| 2 | [`destruction-fire-raid`](destruction-fire-raid.md) | ours: hand draft | 22/11/18 | 613 | -0.8% | 689 | -1.5% | 8 s |
| 3 | **[`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md)** | ours: optimizer | 10/11/30 | 613 | -0.8% | 685 | -2.1% | 2 s |
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

| # | Priority (the first line whose condition holds is cast) | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 20s: cast Corruption | 3.3 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if time left in the fight ≤ 1.125: cast Shadowburn | 0.3 |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if time left on Bane of Agony ≤ cast time of Bane of Agony and time left in the fight ≥ 10s: cast Bane of Agony | 2.5 |
| 7 | if mana % < 10%: cast Life Tap | 6.3 |
| 8 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 9 | if time left on Immolate ≤ cast time of Immolate and time left in the fight ≥ 20s: cast Immolate | 3.4 |
| 10 | cast Conflagrate | 4.7 |
| 11 | if mana % ≥ 25%: cast Talisman of Ephemeral Power | as ready |
| 12 | cast Shadow Bolt | 12.0 |

Lines of the simulator's rotation these builds never cast: cast Eureka! (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-fire-destro-raid-raid-dps`](opt-fire-destro-raid-raid-dps.md) |
|---|---|
| Shadow Bolt | 45% |
| Corruption | 16% |
| Bane of Agony | 16% |
| Immolate | 11% |
| Conflagrate | 10% |
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
