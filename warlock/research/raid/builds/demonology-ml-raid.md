# Demonology — Raid (machine-learning search) — 2/31/18

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 2/31/18 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Demonology build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-03 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry demonology-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Affliction (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 1/5 | changed | Improves your chance to hit by 1% and reduces all threat you generate by 4%. |
| **Improved Corruption** | 1/5 | changed | Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%. |

### Demonology (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 2/5 | changed | Increases your total Stamina by 6%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Improved Sayaad** | 3/3 | unchanged | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 30%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Decimation** | 2/2 | **NEW** | Reduces the cooldown of your Soul Fire spell by 90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 40% and costs no Soul Shards. |
| **Demonic Brand** | 3/3 | **NEW** | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target generate high threat and deal 65 to 68 Fire or Shadow damage based on the pet. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Master Demonologist** | 5/5 | changed | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 10%.  Voidwalker - Reduces Physical damage taken by 10%.  Succubus/Incubus - Increases Shadow damage done by 10%.  Felhunter - Reduces Magic damage taken by 10%. |
| **Demonic Pact** | 1/1 | **NEW** | Your Demonic Sacrifice effect is no longer cancelled by summoning a different Demon pet. Resummoning the sacrificed pet will still cancel the effect. |

### Destruction (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Rank among our builds and the community simulator's

**2 of 4** for `demonology-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`demonology-pact-raid`](demonology-pact-raid.md) | ours: hand draft | 2/31/18 | 646 | +0.0% | 786 | -0.4% | 1 s |
| 2 | **[`demonology-ml-raid`](demonology-ml-raid.md)** | ours: hand draft | 2/31/18 | 646 | -0.0% | 789 | +0.0% | 1 s |
| 3 | *Demonic Pact 2/31/18* | community simulator | - | 625 | -3.3% | 756 | -4.1% | 1 s |
| 4 | *Demonic Pact* | community simulator | - | 619 | -4.3% | 746 | -5.5% | 1 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 5 changes to the base rotation; third-seed check: ml: Demonology 825 -> 832 DPS (+0.9%), demonology-pact-raid 825 -> 831 DPS (+0.8%), sim preset: Demonic Pact 2/31/18 795 -> 801 DPS (+0.8%)):
  1. drop: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.6%, pass 1)
  2. threshold 10% -> 5%: if mana % < 10%: cast Life Tap (+0.5%, pass 1)
  3. only with 10s or more of the fight left: if time left on Corruption ≤ cast time of Corruption: cast Corruption (+0.2%, pass 5)
  4. insert before the filler: if time left on Immolate ≤ cast time of Immolate: cast Immolate + only with 20s or more of the fight left: if time left on Immolate ≤ cast time of Immolate: cast Immolate (+0.3%, pass 5)
  5. move to the top: if not Curse of the Elements is up: cast Curse of the Elements (+0.2%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`demonology-ml-raid`](demonology-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not Curse of the Elements is up: cast Curse of the Elements | 0.4 |
| 2 | if time left in the fight ≥ 15s and mana % ≤ 75%: cast Potion | as ready |
| 3 | if time left in the fight ≥ 15s and mana % ≤ 60%: cast Demonic Rune | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if time left in the fight ≤ 3.5: cast Searing Pain | 0.4 |
| 6 | if time left on Bane of Agony ≤ cast time of Bane of Agony: cast Bane of Agony | 2.7 |
| 7 | if time left on Corruption ≤ cast time of Corruption and time left in the fight ≥ 10s: cast Corruption | 3.4 |
| 8 | if mana % < 15% and time left in the fight ≥ 6s: cast Life Tap | 7.1 |
| 9 | if time left on Immolate ≤ cast time of Immolate: cast Immolate | 3.9 |
| 10 | cast Shadow Bolt | 13.0 |

Damage by ability:

| Ability | [`demonology-ml-raid`](demonology-ml-raid.md) |
|---|---|
| Shadow Bolt | 48% |
| Bane of Agony | 16% |
| Corruption | 16% |
| Immolate | 12% |
| Pet: Auto Attack | 6% |
| Pet: Lash of Pain | 1% |
| Searing Pain | 1% |
| Pet: Demonic Brand | 0% |

## Notes

- Against the best hand draft demonology-pact-raid in a full raid, same gear and fights (100,000, one seed): +0.5% (under the 2% bar: the hand draft stays the pick).
- Where the simulator measured no difference, the points follow demonology-pact-raid: Improved Imp → Demonic Embrace (the same DPS as the search winner 2/31/18 on one seed, 30,000 fights).
- Search result (full raid): 2/31/18 at 836.2 ± 0.16 DPS over 100,000 fights; runner-up 2/31/18 (+0.29%; the winner takes Improved Corruption 1, Suppression 1; the runner-up Improved Corruption 2); 1,739 builds simulated; certificate: 1 confirmed move first, then none of its 266 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 2/31/18 at 800.6 DPS in a full raid (the same talents).
- Alone on the training dummy (only your own buffs) the search's best is 2/31/18 at 688.7 DPS.

## Open questions (verify in the live game)

- A machine-searched Demonology build: check it against the community's Demonology builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
