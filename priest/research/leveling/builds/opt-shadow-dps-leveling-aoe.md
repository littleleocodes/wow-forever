# Optimizer — Shadow leveling/raid: Shadow Word: Pain 28%, Mind Blast 27%, Mind Flay channel 30% (talent), wand 10%, Smite 5% before 20 (leveling-aoe) — 17/3/31

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/3/31 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `shadow-dps` and profile `leveling-aoe`: score +47.1% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Discipline (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 4/5 | **NEW** | Increases the damage and healing of your instant cast spells by 4%. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Martyrdom** | 2/2 | changed | Gives you a 100% chance to gain Focused Casting for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing casting time when taking damage and increases your resistance to Interrupt effects by 20%. |
| **Mental Strength** | 2/5 | changed | Increases your total Intellect by 4%. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Holy (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |

### Shadow (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Blackout** | 5/5 | moved | Gives your Shadow damage spells a 10% chance to stun the target for 3 sec. |
| **Shadow Focus** | 4/5 | changed | Improves your chance to hit with Shadow spells by 4%. |
| **Spirit Tap** | 2/5 | changed | Gives you a 40% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |
| **Improved Mind Flay** | 2/2 | **NEW** | Each instance of damage of Mind Flay deals 20% more damage than its previous instance of damage. |
| **Improved Psychic Scream** | 2/2 | moved | Reduces the cooldown of your Psychic Scream spell by 4 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Silence** | 1/1 | changed | Silences the target, preventing them from casting spells for 5 sec and interrupting their spellcasts for 3 sec. |
| **Darkness** | 3/5 | changed | Increases your Shadow damage done by 6%. |
| **Early Demise** | 2/2 | **NEW** | Increases Shadow Word: Death's critical strike chance on targets at or below 20% health by 30%. |
| **Shadowform** | 1/1 | changed | Assume Shadowform, increasing your Shadow damage by 10%, reducing the Mana cost of all Shadow spells by 50%, increasing the critical strike damage bonus of your Shadow spells by 100%, and reducing Physical damage taken by you by 15%. However, you may not cast healing spells while in this form. |

## Core talents (priority order)

1. **Shadowform** — Removing it costs 13.4 points of score in this model.
2. **Mind Flay** — Removing it costs 10.8 points of score in this model.
3. **Twilight Focus** — Removing it costs 9.6 points of score in this model.
4. **Improved Shadow Word: Pain** — Removing it costs 2.4 points of score in this model.
5. **Darkness** — Removing it costs 1.8 points of score in this model.
6. **Improved Mind Flay** — Removing it costs 1.8 points of score in this model.
7. **Shadow Weaving** — Removing it costs 1.5 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level: Power Word: Shield and Inner Fire before the pull, Mind Blast at 30 yd, Shadow Word: Pain, Mind Flay channels (50% slow) and Mind Blast on cooldown while the mob walks in and once it is on you (the shield stops pushback while it holds), Vampiric Embrace and Devouring Plague heal, Shadow Word: Death below 20%, wand to finish without overkill; Psychic Scream when health runs low. Between fights: 2 s loot, 6 s travel, Renew (not in Shadowform), conjured water below 35% mana, food below 65% health; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): SHIELD_BELOW = 0.5; never cast Smite; drink below 15% mana. Together +13.6% time per kill saved for `leveling-shadow` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/shadow-dps-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Wand | 13.9 | 5.8 | 6.5 | 4.2 | 5% |
| Mind Flay | 3.6 | 3.0 | 2.5 | 2.3 | 29% |
| Shadow Word: Pain | 1.9 | 1.9 | 1.9 | 1.9 | 35% |
| Mind Blast | 1.4 | 1.2 | 1.1 | 1.1 | 15% |
| Shadow Word: Death | 0.0 | 1.1 | 1.1 | 1.0 | 15% |
| Vampiric Embrace | 0.4 | 0.4 | 0.4 | 0.4 | 0% |
| Devouring Plague | 0.4 | 0.3 | 0.2 | 0.3 | 2% |
| Psychic Scream | 0.2 | 0.1 | 0.1 | 0.1 | 0% |
| Flash Heal | 1.2 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r1 on 2026-10-15: an earlier optimizer round beat the last export in the fight lab (50.1s vs 63.6s per kill, level-weighted).
- Report: priest/research/talents/forever/optimizer/shadow-dps-leveling-aoe.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 17/3/31 -> 17/3/31; Improved Fade 1 gone; +1 Shadow Weaving (tier gating for Darkness); order dropped (order_repair.py) (refill: the shadow-dps model, leveling-aoe).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Spell Warding dropped (not in the allocation).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
