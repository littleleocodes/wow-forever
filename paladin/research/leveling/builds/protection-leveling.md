# Protection — Leveling into the raid build — 0/23/28

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/23/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Protection raid build (prot-tank) so you arrive at 60 ready to tank; the order is the fastest of three the fight lab raced (own tree first: 31 s per kill over levels 20-60, the prot-leveling rotation).

## Point allocation

### Holy (0)

*No points.*

### Protection (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 20%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Improved Righteous Fury** | 3/3 | changed | While Righteous Fury is active, all damage taken is reduced by 6%. |
| **Shield Specialization** | 1/3 | changed | Increases the amount of damage absorbed by your shield by 10%, and gives your blocks a 33% chance to restore 6% of your maximum Mana. May only occur once every 3 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |
| **One-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with one-handed melee weapons by 10%. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |

### Retribution (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204, and increase your Attack Power by 3% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Eye for an Eye** | 1/2 | changed | All critical strikes against you cause 5% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 60% of your Intellect. |

## Core talents (priority order)

1. **Champion of the Light** — Raid sim (2026-09-26): removing it costs +8% tank value. Raid sim (2026-09-28): removing it costs +7% tank value.
2. **Deflection** — Raid sim (2026-09-26): removing it costs +4% tank value. Raid sim (2026-09-28): removing it costs +4% tank value.
3. **Improved Righteous Fury** — Reworked: -2%/rank damage taken while Righteous Fury is up (est. 6%). Raid sim (2026-09-26): removing it costs +3% tank value. Raid sim (2026-09-28): removing it costs +3% tank value.
4. **Vengeance** — Raid sim (2026-09-26): removing it costs +4% tank value. Raid sim (2026-09-28): removing it costs +3% tank value.
5. **Vindication** — Raid sim (2026-09-26): removing it costs +3% tank value. Raid sim (2026-09-28): removing it costs +3% tank value.
6. **Templar's Bulwark** — Raid sim (2026-09-28): removing it costs +3% tank value.
7. **Anticipation** — Raid sim (2026-09-28): removing it costs +2% tank value.
8. **Conviction** — Raid sim (2026-09-26): removing it costs +2% tank value. Raid sim (2026-09-28): removing it costs +2% tank value.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-09-30 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): own tree first 31 s; stats model's order 33 s; own tree last 33 s. First Protection point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved):  out;  in; to be re-optimized.

## Open questions (verify in the live game)

- Check the Protection leveling pace at launch; the raid build's talents may cost speed early.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
