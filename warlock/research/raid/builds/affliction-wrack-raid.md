# Affliction — Wrack (the simulator's own build) — 35/11/5

*[Warlock](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 35/11/5 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Affliction build (its aff_wrack build file, added upstream on 2026-11-11): 35/11/5 around Wrack, the 31-point channel that makes Siphon Life, Corruption and Bane of Agony tick twice as fast while it lasts, with Demonic Sacrifice of the Imp (Forever: +15% Shadow damage) and Improved Shadow Bolt. Added on 2026-11-19 from the independent audit's D1: our warlock entries had raced the simulator's talents under rotations from the deleted ElliotWood fork, which never channel Wrack, so every search valued it at nothing.

## Point allocation

### Affliction (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Nightfall** | 2/2 | changed | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 3/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 10%. |
| **Wrack** | 1/1 | **NEW** | Tears the target apart from within for 6 sec, inflicting 60 Shadow damage every 1 sec. While channeling, your Siphon Life, Corruption, and Bane of Agony effects on the target deal their periodic damage 100% faster. |

### Demonology (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 5/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |

## Core talents (priority order)

1. **Wrack** — the 31-point channel the rotation is built around: Siphon Life, Corruption and Bane of Agony tick twice as fast while it lasts
2. **Demonic Sacrifice** — the Imp sacrificed before the pull: +15% Shadow damage
3. **Shadow Mastery** — +Shadow damage on every dot and Wrack
4. **Malevolence** — dot damage
5. **Improved Corruption** — instant Corruption

## Rank among our builds and the community simulator's

**1 of 2** for `affliction-wrack-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`affliction-wrack-raid`](affliction-wrack-raid.md)** | ours: derived (simulator preset) | 35/11/5 | 869 | +0.0% | 941 | +0.0% | 1 s |
| 2 | *Aff (Wrack)* | community simulator | - | 869 | +0.0% | 941 | +0.0% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-11-20, 1 changes to the base rotation; third-seed check: ml: Affliction 869 -> 871 DPS (+0.2%), affliction-wrack-raid 868 -> 870 DPS (+0.2%)):
  1. move to the top: if (number of targets = 1 or “Amount of Dooms left” < 1 and not Bane of Doom is on the target or Bane of Doom is on the target): groupReference (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-11-20, 3 passes, the last 2026-11-20, 2 changes to the base rotation; third-seed check: ml: Affliction 938 -> 943 DPS (+0.5%), affliction-wrack-raid 935 -> 940 DPS (+0.6%)):
  1. move to the top: if number of targets = 1: groupReference + move to the top: groupReference (+0.4%, pass 1)
  2. insert in the middle: cast Weakness Analyzer (+0.2%, pass 1)

Before the pull: cast Shadow Bolt; at -1s: petAttack.

| # | Priority (the first line whose condition holds is cast) | [`affliction-wrack-raid`](affliction-wrack-raid.md) casts/min |
|---|---|---|
| 1 | if (number of targets = 1 or “Amount of Dooms left” < 1 and not Bane of Doom is on the target or Bane of Doom is on the target) and (time left on Bane of Doom < 15s and Bane of Doom is on the target or not Bane of Doom is on the target) and (number of targets > 1 or “Wrack Dots Up” and (“Amp Agony Up” or “Waiting Costs Frozen Heart”)): cast Frozen Heart of the Mountain | as ready |
| 2 | if (number of targets = 1 or “Amount of Dooms left” < 1 and not Bane of Doom is on the target or Bane of Doom is on the target) and (time left on Bane of Doom < 30s and Bane of Doom is on the target or not Bane of Doom is on the target) and (number of targets > 1 or “Wrack Dots Up” and (“Amp Agony Up” or “Waiting Costs Potion”)): cast Major Spellblasting Potion | as ready |
| 3 | use every other cooldown when ready | as ready |
| 4 | if not warlockAssignedCurseIsActive: castWarlockAssignedCurse | as ready |
| 5 | if warlockAssignedCurseIsActive and not warlockAssignedCurseIsActiveOnAllTargets and number of targets > 1: change target | as ready |
| 6 | if number of targets = 1 and not Bane of Agony is on the target and time left in the fight > 12: cast Amplify Curse | 0.3 |
| 7 | if number of targets = 1 and not Bane of Agony is on the target and time left in the fight > 12: cast Bane of Agony | 2.6 |
| 8 | if number of targets = 1 and not Corruption is on the target and time left in the fight > 9: cast Corruption | 3.3 |
| 9 | if number of targets = 1 and not Siphon Life is on the target and time left in the fight > dotBaseDuration and not Shadow Vulnerability is on the target and not Blood Fury is up and not spellIsChanneling: cast Siphon Life | 1.8 |
| 10 | if number of targets > 1 and not Bane of Doom is on the target and (not Bane of Doom is ready or time left in the fight < “Doom tick”) and not Bane of Agony is on the target and number of targets < 5: cast Amplify Curse | 0.3 |
| 11 | if number of targets > 1 and not Bane of Doom is on the target and not Bane of Agony is on the target and number of targets < 5: cast Bane of Agony | 2.6 |
| 12 | if number of targets > 1 and (Bane of Agony is on the target or Bane of Doom is on the target) and not warlockBaneIsActiveOnAllTargets and (warlockAssignedCurseIsActive or warlockIsAssignedCurse) and number of targets < 5: change target | as ready |
| 13 | if number of targets > 1 and not Corruption is on the target and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: cast Corruption | 3.3 |
| 14 | if number of targets > 1 and Corruption is on the target and not dotIsActiveOnAllTargets and (warlockAssignedCurseIsActive or warlockIsAssignedCurse) and ((Bane of Agony is on the target or Bane of Doom is on the target) or not (number of targets < 5)) and time left in the fight > dotBaseDuration and not “in 5y range of 3T”: change target | as ready |
| 15 | if number of targets > 1 and (warlockAssignedCurseIsActiveOnAllTargets or warlockIsAssignedCurse) and (warlockBaneIsActiveOnAllTargets or not (number of targets < 5)) and (dotIsActiveOnAllTargets or time left in the fight > dotBaseDuration): change target | as ready |
| 16 | if (Shadow Trance is up or “Improved Shadow Bolt Known” and Revelation is known and Revelation is up and (not Shadow Vulnerability is on the target or time left on Shadow Vulnerability < (cast time of Shadow Bolt + spellTravelTime))): cast Shadow Bolt | 2.6 |
| 17 | if (Shadow Trance is up or “Improved Shadow Bolt Known” and Revelation is known and Revelation is up and (not Shadow Vulnerability is on the target or time left on Shadow Vulnerability < (cast time of Shadow Bolt + spellTravelTime))): cast Shadow Bolt | 2.6 |
| 18 | if (cast time of Shadow Bolt + spellTravelTime) > time left in the fight: cast Death Coil | 0.3 |
| 19 | if mana % < 30% and time left in the fight > 60s: cast Life Tap | 1.8 |
| 20 | channel Wrack (stop it when (ticks of Wrack channeled ≥ 2 and not Corruption is on the target or ticks of Wrack channeled ≥ 2 and not Bane of Agony is on the target and not Bane of Doom is on the target or ticks of Wrack channeled ≥ 2 and “Blood Fury Ready” and (number of targets = 1 or time left on Bane of Doom ≤ 15))) | as ready |
| 21 | cast Life Tap | 1.8 |

Lines of the simulator's rotation these builds never cast: cast Eureka!, cast Blood Fury, cast Bane of Doom (its condition never held in these fights).

Damage by ability:

| Ability | [`affliction-wrack-raid`](affliction-wrack-raid.md) |
|---|---|
| Wrack | 36% |
| Bane of Agony | 26% |
| Corruption | 23% |
| Siphon Life | 7% |
| Shadow Bolt | 6% |
| Demonic Rune | 1% |
| Death Coil | 0% |

## Notes

- The Imp is sacrificed before the pull (the entry affliction-raid's sacrificedDemon: Imp); builds without Demonic Sacrifice keep the Succubus out.
- Raced, its rotation tuned and its talents searched in audit step 2 (deep-runs/warlock_raid_1119.sh); numbers on the raid page.
- Simulator numbers are the community's model of the game, not in-game measurements.

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/warlock/dps/builds/aff_wrack.build.json>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
