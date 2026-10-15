# Retribution — Seal of Command / Twist of Light (simulator winner adopted 2026-09-27) — 17/0/34

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/0/34 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `ret-raid-dps` |

## Summary

Allocation adopted on 2026-09-27 from `cand-ret-dps-r1`, the best build in the community simulator (+2.9% DPS vs the previous draft with the simulator's gear, rotation and buffs; the previous draft is kept under raid/raidsim/candidates/). Core talents are ranked by the simulator's removal cost. Previous summary: Seal of Command, Conviction, Vengeance (now a stacking buff), Two-Handed Weapon Specialization and Repentance survive; Sanctity Aura, Improved Blessing of Might and Improved Seal of the Crusader are gone. New: Sacred Arbiter (Holy Strike refreshes Judgements), Crusade, Champion of the Light (Intellect to spell damage), Instrument of Law and the Twist of Light capstone (seal twisting echoes). Improved Seals and Divine Strength from Holy, Precision (hit) from Protection.

## Point allocation

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |

### Protection (0)

*No points.*

### Retribution (34)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204, and increase your Attack Power by 3% for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 60% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1.0 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, you gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Core talents (priority order)

1. **Twist of Light** — New capstone: swapping seals grants an Echo that applies the replaced seal on the next hit — seal twisting. Raid sim (2026-09-27): removing it costs +13% DPS.
2. **Champion of the Light** — New: spell damage from Intellect (est. 33%) — Judgements, Consecration, Exorcism scale. Raid sim (2026-09-27): removing it costs +12% DPS.
3. **Seal of Command** — Still the damage engine: 70% weapon damage Holy procs. Raid sim (2026-09-27): removing it costs +11% DPS.
4. **Sanctified Judgement** — Mana on Judgements; prerequisite for Vengeance. Raid sim (2026-09-27): removing it costs +8% DPS.
5. **Conviction** — +5% melee crit. Raid sim (2026-09-27): removing it costs +7% DPS.
6. **Improved Seals** — New: +5%/rank Seal and Judgement damage (est. 15%). Raid sim (2026-09-27): removing it costs +7% DPS.
7. **Vengeance** — Reworked: +1%/rank Physical and Holy damage per crit, 5 stacks (est. 15% at 3/3); requires Sanctified Judgement 3. Raid sim (2026-09-27): removing it costs +6% DPS.
8. **Reverence** — Raid sim (2026-09-27): removing it costs +4% DPS.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Vindication | any utility talent legal at that tier | Measures +0.8% DPS in the community simulator (noise): these points are free to move. |
| 1 | Divine Favor | any utility talent legal at that tier | Measures +0.4% DPS in the community simulator (noise): these points are free to move. |

## Rank among our builds and the community simulator's

**3 of 6** for `ret-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 12/8/31 | 533 | +0.0% | 979 | -0.3% | 1 s |
| 2 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: hand draft | 11/8/32 | 523 | -1.8% | 982 | +0.0% | 6 s |
| 3 | **[`ret-raid-dps`](ret-raid-dps.md)** | ours: hand draft | 17/0/34 | 522 | -1.9% | 954 | -2.8% | 2 s |
| 4 | *P4/P5 Ret* | community simulator | - | 514 | -3.6% | 952 | -3.1% | 7 s |
| 5 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 10/8/33 | 509 | -4.5% | 979 | -0.3% | 20 s |
| 6 | *Retribution 9/0/42* | community simulator | - | 489 | -8.3% | 940 | -4.2% | 16 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-14, 18 changes to the base rotation; third-seed check: ):
  1. only above 40% mana: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Righteousness is up: cast Seal of Command (+2.5%, pass 1)
  2. threshold 0.4s -> 0.9s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.1%, pass 1)
  3. threshold 70% -> 60%: if mana % ≥ 70%: cast Consecration + threshold 0.4s -> 0.2s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Righteousness is up and mana % ≥ 40%: cast Seal of Command (+0.3%, pass 1)
  4. always rank 2 instead of rank 5: if mana % ≥ 60%: cast Consecration (+0.3%, pass 1)
  5. threshold 60% -> 40%: if mana % ≥ 60%: cast Consecration (+1.5%, pass 1)
  6. always rank 1 instead of rank 2: if mana % ≥ 40%: cast Consecration (+1.5%, pass 1)
  7. drop the condition: if mana % ≥ 40%: cast Consecration (+1.5%, pass 1)
  8. threshold 40% -> 60%: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 40%: cast Seal of Command (+1.4%, pass 1)
  9. insert before the filler: cast Consecration (+4.1%, pass 2)
  10. threshold 60% -> 70%: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 60%: cast Seal of Command (+0.6%, pass 2)
  11. threshold 0.9s -> 0.4s: if mana % ≥ 15% and time to the next auto attack < 0.9s and Seal of Command is up: cast Seal of Righteousness (+0.6%, pass 2)
  12. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 2)
  13. spell probe: insert at the top: cast Holy Shock (+8.0%, pass 4)
  14. drop 'time to the next auto attack < 0.2s' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command (+1.8%, pass 5)
  15. drop 'mana % ≥ 15%' from the condition: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 5)
  16. threshold 70% -> 65%: if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command (+0.5%, pass 5)
  17. threshold 1s -> 2s: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+0.2%, pass 5)
  18. spell probe: insert at the end: cast Divine Favor (+3.9%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-14, 12 changes to the base rotation; third-seed check: ):
  1. drop 'time left on Seal of Righteousness ≤ 1s' from the condition: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+2.4%, pass 1)
  2. threshold 70% -> 50%: if mana % ≥ 70%: cast Consecration (+1.4%, pass 1)
  3. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  4. threshold 0.4s -> 1.4s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.5%, pass 2)
  5. move to the top: cast Hammer of Wrath (+1.4%, pass 2)
  6. move down below 'if mana % ≥ 50%: cast Consecration': cast Holy Strike (+0.6%, pass 2)
  7. spell probe: insert at the end: cast Holy Shock (+6.6%, pass 4)
  8. insert in the middle: cast Consecration (+7.1%, pass 5)
  9. insert in the middle: cast Demonic Rune (+0.2%, pass 5)
  10. rotation replaced by seal-of-fury-raid's raid rotation (keeps Seal of Righteousness up and judges it, Holy Strike, almost no seal twisting), which the open search's re-tune on a Retribution build produced (+2.0% on one seed, pass 6)
  11. always rank 4 instead of rank 5: if mana % ≥ 15% and Seal of Righteousness is up: cast Seal of Command (+0.3%, pass 8)
  12. spell probe: insert in the middle: cast Holy Shock (+9.3%, pass 11)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`ret-raid-dps`](ret-raid-dps.md) casts/min |
|---|---|---|
| 1 | if time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness | 5.0 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Judgement can be cast: cast Judgement | 7.7 |
| 4 | if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 2s: cast Seal of Command | 5.0 |
| 5 | if mana % ≥ 15% and Seal of Righteousness is up and mana % ≥ 65%: cast Seal of Command | 5.0 |
| 6 | cast Hammer of Wrath | 2.0 |
| 7 | cast Holy Strike | 6.0 |
| 8 | cast Consecration | 6.3 |
| 9 | cast Consecration | 0.6 |
| 10 | cast Divine Favor | 0.7 |

Lines of the simulator's rotation these builds never cast: cast Holy Shock (its condition never held in these fights).

Damage by ability:

| Ability | [`ret-raid-dps`](ret-raid-dps.md) |
|---|---|
| Auto Attack | 19% |
| Seal of Righteousness | 19% |
| Consecration | 16% |
| Holy Strike | 14% |
| Judgement of Righteousness | 14% |
| Hammer of Wrath | 6% |
| Seal of Command | 5% |
| Judgement of Command | 4% |
| Dragonbreath Chili | 3% |

## Notes

- Adopted from the community simulator on 2026-09-27: cand-ret-dps-r1 beat the previous draft by +2.9% DPS; the rationale below predates the adoption where it names talents no longer taken.
- Rotation hypothesis: Seal of Command auto-attacks, Judgement on cooldown, Holy Strike (refreshes Judgements), Consecration/Exorcism (Holy Conduit) as mana allows, seal twists for Echoes.
- Consecration is baseline in Forever.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Vindication 2 (+2% attack power self-buff on melee hits), which also keeps the 20 points below tier 5.
- 2026-09-27 scenario audit: Repentance 1 -> Holy Conduit 1. Repentance incapacitates a Humanoid; raid bosses are immune and it gates nothing. Holy Conduit's second rank returns more mana on Consecration and Exorcism; the simulator's best Retribution build takes it (ElliotWood/Forever 40be98e: +1.8% with Vindication 3).
- Companion build `ret-full-buffs-raid` (restored 2026-09-27): in a raid with Blessing of Wisdom and Mana Spring it does 748 DPS against this build's 729 (+2.7%, ElliotWood/Forever 40be98e, 3000 iterations); this build wins on the training dummy (307 vs 298).

## Open questions (verify in the live game)

- How Twist of Light Echoes interact with Seal of Command procs — the core of a Forever Ret rotation.
- Holy Strike's damage/cooldown (new baseline ability) and whether Improved Holy Strike (Holy tier 1) beats Divine Strength.
- Vengeance stacking uptime with 5-10% crit.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
