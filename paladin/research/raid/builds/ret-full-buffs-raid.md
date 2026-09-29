# Retribution — Seal of Command / Twist of Light (full raid buffs, 10/8/33) — 10/8/33

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/8/33 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `ret-raid-dps` |

## Summary

The build for a raid that brings Blessing of Wisdom and Mana Spring: `ret-raid-dps` until the training-dummy adoption of 2026-09-27, restored as its companion. In the community simulator's raid setting (full buffs, ElliotWood/Forever 40be98e, 3000 iterations) it does 748 DPS against `ret-raid-dps`'s 729 (+2.7%); on the training dummy, where our raid drafts are ranked (your own buffs only), it does 298 against 307 (-2.8%). Simulator numbers, not measurements. Seal of Command, Conviction, Vengeance (now a stacking buff), Two-Handed Weapon Specialization and Repentance survive; Sanctity Aura, Improved Blessing of Might and Improved Seal of the Crusader are gone. New: Sacred Arbiter (Holy Strike refreshes Judgements), Crusade, Champion of the Light (Intellect to spell damage), Instrument of Law and the Twist of Light capstone (seal twisting echoes). Improved Seals and Divine Strength from Holy, Precision (hit) from Protection.

## Point allocation

### Holy (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 2/5 | unchanged | Increases your total Intellect by 4%. |
| **Improved Seals** | 3/3 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |

### Retribution (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 2/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 133, and increase your Attack Power by 2% for 30 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with two-handed melee weapons by 6%. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage and healing by up to 100% of your Intellect. |
| **Instrument of Law** | 2/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 1 sec, and reduces all threat you generate by 20% while Righteous Fury is not active. |
| **Twist of Light** | 1/1 | **NEW** | Reduces the Mana cost of your Seal spells by 20%, and when you replace your Seal of Command, Seal of Righteousness, Seal of Fury, or Seal of Justice with a different Seal, gain an Echo of that Seal. Your next melee attack applies the replaced Seal's effects, consuming the Echo. |

## Core talents (priority order)

1. **Seal of Command** — Still the damage engine: 70% weapon damage Holy procs.
2. **Twist of Light** — New capstone: swapping seals grants an Echo that applies the replaced seal on the next hit — seal twisting.
3. **Improved Seals** — New: +5%/rank Seal and Judgement damage (est. 15%).
4. **Conviction** — +5% melee crit.
5. **Vengeance** — Reworked: +1%/rank Physical and Holy damage per crit, 5 stacks (est. 15% at 3/3); requires Sanctified Judgement 3.
6. **Precision** — +3% hit with all attacks and spells.
7. **Divine Strength** — +10% Strength.
8. **Champion of the Light** — New: spell damage from Intellect (est. 33%) — Judgements, Consecration, Exorcism scale.
9. **Sacred Arbiter** — New 16-point talent: Holy Strike +10% and refreshes Judgements — no more re-judging.
10. **Two-Handed Weapon Specialization** — +3% (est.) two-hander damage.
11. **Crusade** — +2% damage, +4% vs. Demons/Undead (est.).
12. **Sanctified Judgement** — Mana on Judgements; prerequisite for Vengeance.
13. **Instrument of Law** — Faster Hammer of Wrath and -10% threat.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Toughness | Redoubt | Tier-1 Protection filler to unlock Precision. |
| 3 | Divine Intellect 2 + Holy Conduit 1 | Divine Intellect 5 by dropping Instrument of Law | Mana vs. threat. |

## Rank among our builds and the community simulator's

**3 of 5** for `ret-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/0/34 | 368 | +0.0% | 778 | -3.3% | 0 s |
| 2 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/0/34 | 367 | -0.4% | 779 | -3.2% | 0 s |
| 3 | **[`ret-full-buffs-raid`](ret-full-buffs-raid.md)** | ours: hand draft | 10/8/33 | 365 | -0.8% | 804 | +0.0% | 3 s |
| 4 | *P4/P5 Ret* | community simulator | - | 365 | -0.8% | 777 | -3.5% | 0 s |
| 5 | *Retribution 9/0/42* | community simulator | - | 353 | -4.2% | 771 | -4.2% | 5 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 12 changes to the base rotation; third-seed check: opt-ret-dps-raid-dps 348 -> 369 DPS (+5.8%), sim preset: P4/P5 Ret 353 -> 366 DPS (+3.7%)):
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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-29, 6 changes to the base rotation; third-seed check: opt-ret-dps-raid-dps 730 -> 779 DPS (+6.8%), sim preset: P4/P5 Ret 727 -> 777 DPS (+6.8%)):
  1. drop 'time left on Seal of Righteousness ≤ 1s' from the condition: if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command (+2.4%, pass 1)
  2. threshold 70% -> 50%: if mana % ≥ 70%: cast Consecration (+1.4%, pass 1)
  3. move to the top: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+0.2%, pass 1)
  4. threshold 0.4s -> 1.4s: if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness (+1.5%, pass 2)
  5. move to the top: cast Hammer of Wrath (+1.4%, pass 2)
  6. move down below 'if mana % ≥ 50%: cast Consecration': cast Holy Strike (+0.6%, pass 2)

Before the pull: at -1.5s: cast Seal of Command.

| # | Priority (the first line whose condition holds is cast) | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≥ 15% and time to the next auto attack < 0.4s and Seal of Command is up: cast Seal of Righteousness | 3.2 |
| 2 | use every other cooldown when ready | as ready |
| 3 | if time left on Seal of Command ≤ 1s and time left on Seal of Righteousness ≤ 1s: cast Seal of Command | 3.5 |
| 4 | if mana % ≥ 15% and time to the next auto attack < 0.2s and Seal of Righteousness is up and mana % ≥ 70%: cast Seal of Command | 3.5 |
| 5 | cast Hammer of Wrath | 1.3 |
| 6 | cast Holy Strike | 6.0 |
| 7 | cast Consecration | 6.5 |
| 8 | cast Consecration | 0.5 |

Lines of the simulator's rotation these builds never cast: cast Judgement (its condition never held in these fights).

Damage by ability:

| Ability | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) |
|---|---|
| Auto Attack | 22% |
| Consecration | 18% |
| Holy Strike | 15% |
| Judgement of Righteousness | 15% |
| Seal of Righteousness | 13% |
| Seal of Command | 8% |
| Hammer of Wrath | 4% |
| Dragonbreath Chili | 2% |
| Judgement of Command | 2% |

## Notes

- Restored 2026-09-27 (user choice: keep both builds). Take `ret-raid-dps` when you bring your own mana (the dummy, small groups, no paladin or shaman in your party) and this one when a raid supplies Blessing of Wisdom and Mana Spring. The reasons under core and flex predate the 2026-09-27 training-dummy calibration.
- Rotation hypothesis: Seal of Command auto-attacks, Judgement on cooldown, Holy Strike (refreshes Judgements), Consecration/Exorcism (Holy Conduit) as mana allows, seal twists for Echoes.
- Consecration is baseline in Forever.
- Build 1.60.1.70009 removed Crusade: its 2 points go to Vindication 2 (+2% attack power self-buff on melee hits), which also keeps the 20 points below tier 5.
- 2026-09-27 scenario audit: Repentance 1 -> Holy Conduit 1. Repentance incapacitates a Humanoid; raid bosses are immune and it gates nothing. Holy Conduit's second rank returns more mana on Consecration and Exorcism; the simulator's best Retribution build takes it (ElliotWood/Forever 40be98e: +1.8% with Vindication 3).

## Open questions (verify in the live game)

- How Twist of Light Echoes interact with Seal of Command procs — the core of a Forever Ret rotation.
- Holy Strike's damage/cooldown (new baseline ability) and whether Improved Holy Strike (Holy tier 1) beats Divine Strength.
- Vengeance stacking uptime with 5-10% crit.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
