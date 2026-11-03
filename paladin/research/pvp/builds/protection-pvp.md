# Protection — PvP (derived) — 5/25/21

*[Paladin](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/25/21 (Holy / Protection / Retribution) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Protection PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Protection (model ret-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Protection builds agree with (3796 builds).

## Point allocation

### Holy (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |

### Protection (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Guardian's Favor** | 2/2 | changed | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Improved Hammer of Justice** | 3/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 15 sec. |
| **Shield Specialization** | 2/2 | changed | Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Improved Righteous Fury** | 3/3 | changed | While Righteous Fury is active, all damage taken is reduced by 9%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |
| **Reckoning** | 3/5 | changed | Gives you a 24% chance after Blocking and a 60% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec. |

### Retribution (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 1/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 2%. |
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Repentance** | 1/1 | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |

## Core talents (priority order)

1. **Sanctified Judgement** — The scorer's value in this build: +11.0% of its score (model ret-dps).
2. **Seal of Command** — The scorer's value in this build: +9.6% of its score (model ret-dps).
3. **Repentance** — The scorer's value in this build: +8.8% of its score (model ret-dps).
4. **Pursuit of Justice** — The scorer's value in this build: +8.8% of its score (model ret-dps).
5. **Improved Hammer of Justice** — The scorer's value in this build: +8.8% of its score (model ret-dps).
6. **Guardian's Favor** — The scorer's value in this build: +8.8% of its score (model ret-dps).

## Notes

- Community tie-break moves: 5 points Toughness -> Redoubt; 3 points Anticipation -> Shield Specialization; 3 points Reckoning -> One-Handed Weapon Specialization; 1 point Anticipation -> Precision; 1 point Anticipation -> Reckoning.
- Where we disagree with the community: most Protection builds take Iron Creed (87% take it), Holy Shield (85% take it), Anticipation (75% take it), which the model values below this build's weakest point; this build takes Guardian's Favor (20%), Improved Hammer of Justice (12%), Repentance (4%), Seal of Command (12%), which few Protection builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- Scored with the Retribution damage model (PvP values damage, not threat), keeping 30+ points in Protection.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved):  out;  in; to be re-optimized.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 0/30/21 -> 5/25/21; Improved Seal of Fury 1 gone; Shield Specialization 3 -> 2 (rank cap); One-Handed Weapon Specialization 3 gone; Holy Conduit 2 gone (moved to Holy); +1 Unyielding Faith (tier gating for Repentance); +1 Unyielding Faith (tier gating for Repentance); refill +5 Spiritual Focus (refill: the ret-dps model, pvp).

## Open questions (verify in the live game)

- A derived Protection PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
