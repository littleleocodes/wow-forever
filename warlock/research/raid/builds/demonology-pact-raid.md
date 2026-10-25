# Demonology — Demonic Pact (raid) — 2/31/18

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/31/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Demonology to Demonic Pact, a Forever talent that keeps Demonic Sacrifice's effect when another demon is summoned: the Imp is sacrificed before the pull (+15% Shadow damage) and the Succubus stays out for Master Demonologist, Soul Link, Demonic Knowledge and Unholy Power. Destruction for Improved Shadow Bolt, Bane, Ruin and Agonizing Flames; Shadow Bolt is the filler. From the simulator's Demonic Pact preset, tuned by the simulator talent search under the Demonology rotation.

## Point allocation

### Affliction (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 1/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 10%. |
| **Improved Corruption** | 1/5 | changed | Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%. |

### Demonology (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Improved Sayaad** | 2/3 | unchanged | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 20%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 20%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Decimation** | 2/2 | **NEW** | Reduces the cooldown of your Soul Fire spell by 90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 40% and costs no Soul Shards. |
| **Demonic Brand** | 3/3 | **NEW** | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Master Demonologist** | 5/5 | changed | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 10%.  Voidwalker - Reduces Physical damage taken by 10%.  Succubus/Incubus - Increases Shadow damage done by 10%.  Felhunter - Reduces Magic damage taken by 10%. |
| **Demonic Pact** | 1/1 | **NEW** | Your Demonic Sacrifice effect is no longer cancelled by summoning a different Demon pet. Resummoning the sacrificed pet will still cancel the effect. |
| **Demonic Embrace** | 3/5 | changed | Increases your total Stamina by 9%. |

### Destruction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Core talents (priority order)

1. **Demonic Sacrifice** — The Imp's sacrifice: +15% Shadow damage. Simulator removal run (2026-09-28): the build loses 13.7% of its DPS on the training dummy without it.
2. **Demonic Pact** — Keeps the sacrificed Imp's +15% Shadow damage with the Succubus summoned. Simulator removal run (2026-09-28): the build loses 13.7% of its DPS on the training dummy without it.
3. **Master Demonologist** — The Succubus's bonus for warlock and demon. Simulator removal run (2026-09-28): the build loses 9.3% of its DPS on the training dummy without it.
4. **Bane** — -0.5 s on Shadow Bolt. Simulator removal run (2026-09-28): the build loses 8.7% of its DPS on the training dummy without it.
5. **Demonic Knowledge** — Spell damage while a demon is out. Simulator removal run (2026-09-28): the build loses 5.7% of its DPS on the training dummy without it.
6. **Agonizing Flames** — +10% Destruction damage. Simulator removal run (2026-09-28): the build loses 5.6% of its DPS on the training dummy without it.
7. **Improved Shadow Bolt** — Shadow Bolt crits raise the Shadow damage the target takes by 20%. Simulator removal run (2026-09-28): the build loses 4.3% of its DPS on the training dummy without it.
8. **Soul Link** — +3% damage for warlock and demon. Simulator removal run (2026-09-28): the build loses 3.0% of its DPS on the training dummy without it.
9. **Ruin** — +100% crit damage on Destruction spells (Shadow Bolt). Simulator removal run (2026-09-28): the build loses 2.9% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Decimation | any talent legal at that tier | Worth 0.9% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 5 | Unholy Power | any talent legal at that tier | Worth 0.7% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Improved Sayaad | any talent legal at that tier | Worth 0.2% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Demonic Embrace | Demonic Energies, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Master Summoner | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Demonic Brand | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 1 | Demonic Embrace | Improved Felhunter, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**1 of 4** for `demonology-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever fork 2ce8265 (client 70291)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`demonology-pact-raid`](demonology-pact-raid.md)** | ours: hand draft | 2/31/18 | 702 | +0.0% | 816 | -0.8% | 2 s |
| 2 | [`demonology-ml-raid`](demonology-ml-raid.md) | ours: derived (ML search) | 2/31/18 | 700 | -0.2% | 822 | +0.0% | 2 s |
| 3 | *Demonic Pact 2/31/18* | community simulator | - | 678 | -3.4% | 788 | -4.1% | 2 s |
| 4 | *Demonic Pact* | community simulator | - | 670 | -4.6% | 778 | -5.3% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 10 changes to the base rotation; third-seed check: ml: Demonology 681 -> 688 DPS (+0.9%), demonology-pact-raid 682 -> 688 DPS (+0.8%), sim preset: Demonic Pact 2/31/18 660 -> 665 DPS (+0.7%)):
  1. drop: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.5%, pass 1)
  2. only with 6s or more of the fight left: if mana % < 10%: cast Life Tap (+0.4%, pass 1)
  3. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 1)
  4. move down below 'if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony': if mana % < 10% and time left in the fight ≥ 6s: cast Life Tap (+0.2%, pass 1)
  5. threshold 10% -> 15%: if mana % < 10% and time left in the fight ≥ 6s: cast Life Tap (+0.4%, pass 2)
  6. move down below 'if time left on Corruption ≤ cast time of Corruption: cast Corruption': if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 3)
  7. insert before the filler: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 5)
  8. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.3%, pass 5)
  9. move down below 'if time left on Corruption ≤ cast time of Corruption: cast Corruption': if mana % < 15% and time left in the fight ≥ 6s: cast Life Tap (+0.2%, pass 5)
  10. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-09, 7 changes to the base rotation; third-seed check: demonology-ml-raid 837 -> 832 DPS (-0.5%), sim preset: Demonic Pact 2/31/18 805 -> 798 DPS (-0.9%), demonology-pact-raid 833 -> 827 DPS (-0.7%)):
  1. drop: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.6%, pass 1)
  2. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.5%, pass 1)
  3. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 5)
  4. insert before the filler: if time left on Immolate ≤ cast time of Immolate: cast Immolate + only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 5)
  5. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 5)
  6. insert before the filler: cast Talisman of Ephemeral Power (+0.4%, pass 6)
  7. insert before the filler: cast Eureka! (+0.2%, pass 6)

| # | Priority (the first line whose condition holds is cast) | [`demonology-pact-raid`](demonology-pact-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.8 |
| 7 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption | 3.4 |
| 8 | if mana % < 15% and time left in the fight ≥ 6s: cast Life Tap | 7.1 |
| 9 | if time left on Immolate ≤ cast time of Immolate: cast Immolate | 3.8 |
| 10 | cast Shadow Bolt | 13.5 |

Damage by ability:

| Ability | [`demonology-pact-raid`](demonology-pact-raid.md) |
|---|---|
| Shadow Bolt | 48% |
| Bane of Agony | 16% |
| Corruption | 15% |
| Immolate | 11% |
| Pet: Auto Attack | 7% |
| Pet: Lash of Pain | 2% |
| Searing Pain | 1% |
| Pet: Demonic Brand | 0% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `sim preset: Demonic Pact 2/31/18`: 2 points Improved Corruption -> Agonizing Flames, 1 point Suppression -> Agonizing Flames.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Demonic Energies -> Demonic Embrace (survival); Demonic Energies -> Demonic Embrace (survival); Improved Felhunter -> Demonic Embrace (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Demonic Pact in the game: does a demon summoned after Demonic Sacrifice leave the sacrifice's effect in place, as the tooltip and the simulator's preset say, and do Master Demonologist and Soul Link then work in full?
- The Succubus in a raid: the simulator's preset keeps her out; check her survival and threat on bosses that cleave.

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/warlock/dps/presets.ts>
- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
