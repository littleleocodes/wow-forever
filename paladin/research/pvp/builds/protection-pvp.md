# Protection — PvP (derived) — 0/30/21

*[Paladin](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/30/21 (Holy / Protection / Retribution) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Protection PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Protection (model ret-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Protection builds agree with (3796 builds).

## Point allocation

### Holy (0)

*No points.*

### Protection (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Guardian's Favor** | 2/2 | changed | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Improved Righteous Fury** | 3/3 | changed | While Righteous Fury is active, all damage taken is reduced by 6%. |
| **Shield Specialization** | 3/3 | changed | Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 6% of your maximum Mana. May only occur once every 3 sec. |
| **Sacred Duty** | 2/2 | **NEW** | Increases your total Stamina by 4% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |
| **One-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with one-handed melee weapons by 10%. |
| **Improved Hammer of Justice** | 3/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 15 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Reckoning** | 3/5 | changed | Gives you a 24% chance to gain an extra attack after Blocking a melee attack and a 60% chance to gain an extra attack after being the victim of a non-periodic critical strike. |

### Retribution (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Benediction** | 1/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 2%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 200, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
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

## Open questions (verify in the live game)

- A derived Protection PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
