# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (leveling-st) — 10/11/30

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/11/30 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `leveling-st`: score +38.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |

### Protection (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |

### Retribution (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Repentance** | 1/1 | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Seal of Command** — Removing it costs 3.9 points of score in this model.
2. **Conviction** — Removing it costs 2.8 points of score in this model.
3. **Improved Seals** — Removing it costs 2.5 points of score in this model.
4. **Vengeance** — Removing it costs 2.3 points of score in this model.
5. **Pursuit of Justice** — Removing it costs 2.3 points of score in this model.
6. **Sanctified Judgement** — Removing it costs 2.2 points of score in this model.
7. **Instrument of Law** — Removing it costs 1.8 points of score in this model.
8. **Two-Handed Weapon Specialization** — Removing it costs 1.5 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level with a two-hander: Blessing of Might and Devotion Aura up, a Seal recast before each pull (Seal of Command once talented, Seal of Righteousness before), the mob walks in (paladins have no charge), Judgement and Holy Strike on cooldown, Consecration while mana allows, Hammer of Justice into a doubled Seal of Command judgement or when hurt, Hammer of Wrath under 20%; Divine Protection and a Holy Light when low, Lay on Hands in an emergency. Between fights: 2 s loot, 6 s travel, Holy Light or Flash of Light back to 80% health, water below 35% mana; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-23, on top of the priority below): never cast Consecration; drink below 15% mana. Together +6.1% time per kill saved for `leveling-retribution` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/ret-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee | 3.6 | 4.5 | 5.7 | 5.2 | 6.2 | 35% |
| Judgement | 1.6 | 2.2 | 2.6 | 2.4 | 2.8 | 20% |
| Holy Strike | 1.3 | 1.6 | 2.1 | 1.9 | 2.2 | 15% |
| Seal of Command | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 17% |
| Hammer of Wrath | 0.0 | 0.0 | 0.0 | 0.9 | 1.0 | 13% |
| Hammer of Justice | 0.3 | 0.3 | 0.4 | 0.4 | 0.5 | 0% |

## Notes

- Report: paladin/research/talents/forever/optimizer/ret-dps-leveling-st.md
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 15/0/36 -> 10/11/30; Divine Intellect 5 gone (moved to Protection); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 2 gone; refill +5 Divine Intellect, +3 Precision, +2 Sacred Duty, +1 Templar's Bulwark; order dropped (order_repair.py) (refill: the ret-dps model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
