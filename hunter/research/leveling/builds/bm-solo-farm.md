# Beast Mastery (solo / farming, 31/20/0) — 31/20/0

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/20/0 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `bm-solo-farm` |

## Summary

Bestial Wrath, Frenzy, Ferocity, Unleashed Fury, Endurance Training (pet health and armor), Focused Fire and Summon Hawk (a second attacker), with Lethal Attacks, Efficiency, Careful Aim and Mortal Shots from Marksmanship. Improved Revive Pet and Bestial Discipline are left out in favour of a pet that dies less in the first place.

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5/5 | changed | Increases the Health and Armor of your pets by 15%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1/1 | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |

### Survival (0)

*No points.*

## Core talents (priority order)

1. **Bestial Wrath** — +50% pet damage, CC immunity; requires Intimidation (which requires Bestial Swiftness).
2. **Frenzy** — Pet haste on crits.
3. **Summon Hawk** — New 16-point talent: a second attacker for 18s; Unleashed Fury/Ferocity buff hawks too.
4. **Ferocity** — Pet/hawk crit.
5. **Unleashed Fury** — Pet/hawk damage.
6. **Intimidation** — Pet stun.
7. **Mortal Shots** — Your own crit damage.
8. **Endurance Training** — +15% pet health and armor (est.) — a pet that survives is a pet that tanks.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Endurance Training 5 + Focused Fire 2 (the last 4 of them) | Improved Revive Pet 2 + Bestial Discipline 2, Improved Mend Pet 2 | Pet durability vs. faster revives / regen while casting. |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Thick Hide is gone; Endurance Training now also gives pet armor.

## Open questions (verify in the live game)

- Hawk damage at 60 and whether two hawks plus a pet make BM a raid spec.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
