# Beast Mastery — PvP (derived) — 31/0/20

*[Hunter](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/0/20 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Beast Mastery (model bm-leveling, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Beast Mastery builds agree with (7452 builds).

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 3/3 | changed | Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Spirit Bond** | 2/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 5 sec. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 1/5 | unchanged | Gives your pet a 20% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (0)

*No points.*

### Survival (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Entrapment** | 5/5 | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 5 sec. |
| **Improved Wing Clip** | 3/3 | changed | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |

## Core talents (priority order)

1. **Deterrence** — The scorer's value in this build: +11.4% of its score (model bm-leveling).
2. **Deflection** — The scorer's value in this build: +10.0% of its score (model bm-leveling).
3. **Bestial Wrath** — The scorer's value in this build: +10.0% of its score (model bm-leveling).
4. **Intimidation** — The scorer's value in this build: +9.1% of its score (model bm-leveling).
5. **Improved Wing Clip** — The scorer's value in this build: +9.1% of its score (model bm-leveling).
6. **Entrapment** — The scorer's value in this build: +9.1% of its score (model bm-leveling).

## Notes

- Community tie-break moves: 2 points Improved Mend Pet -> Bestial Discipline; 2 points Improved Concussive Shot -> Entrapment.
- Where we disagree with the community: most Beast Mastery builds take Lethal Attacks (78% take it), Endurance Training (75% take it), which the model values below this build's weakest point; this build takes Counterattack (10%), Deflection (19%), Deterrence (17%), Entrapment (15%), Improved Wing Clip (6%), Surefooted (17%), Survival Tactics (3%), which few Beast Mastery builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Beast Mastery PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
