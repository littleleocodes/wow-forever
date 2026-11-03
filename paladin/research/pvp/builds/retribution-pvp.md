# Retribution — PvP (derived) — 22/0/29

*[Paladin](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/0/29 (Holy / Protection / Retribution) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Retribution (model ret-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Retribution builds agree with (5070 builds).

## Point allocation

### Holy (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (0)

*No points.*

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 2/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 4%. |
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Conviction** | 1/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 2%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Repentance** | 1/1 | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |
| **Vengeance** | 2/3 | changed | Increases your Physical and Holy damage dealt by 2% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Sanctified Judgement** — The scorer's value in this build: +9.4% of its score (model ret-dps).
2. **Seal of Command** — The scorer's value in this build: +9.0% of its score (model ret-dps).
3. **Unyielding Faith** — The scorer's value in this build: +8.1% of its score (model ret-dps).
4. **Voice of Truth** — The scorer's value in this build: +7.5% of its score (model ret-dps).
5. **Spiritual Focus** — The scorer's value in this build: +7.5% of its score (model ret-dps).
6. **Repentance** — The scorer's value in this build: +7.5% of its score (model ret-dps).

## Notes

- Community tie-break moves: 2 points Deflection -> Benediction; 1 point Conviction -> Vengeance.
- Where we disagree with the community: most Retribution builds take none, which the model values below this build's weakest point; this build takes Deflection (20%), Infusion of Light (15%), which few Retribution builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 21/0/30 -> 22/0/29; Unyielding Faith 2 gone (moved to Retribution); Voice of Truth 1 gone; Reverence 3 -> 2 (rank cap); Holy Conduit 2 gone (moved to Holy); Instrument of Law 2 gone; +1 Spiritual Focus (tier gating for Holy Shock); +1 Spiritual Focus (tier gating for Holy Shock); +1 Spiritual Focus (tier gating for Holy Shock); +1 Holy Conduit (tier gating for Holy Shock); +1 Unyielding Faith (tier gating for Champion of the Light); +1 Unyielding Faith (tier gating for Champion of the Light); refill +1 Vengeance, +1 Holy Conduit (refill: the ret-dps model, pvp).

## Open questions (verify in the live game)

- A derived Retribution PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
