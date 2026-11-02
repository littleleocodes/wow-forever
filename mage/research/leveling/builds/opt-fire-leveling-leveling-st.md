# Optimizer — Single-target Fireball leveling: Fireball ~60%, Fire Blast, Scorch (22+), wand (leveling-st) — 4/31/16

*[Mage](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 4/31/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `fire-leveling` and profile `leveling-st`: score +68.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 2/3 | changed | Increases your Armor by an amount equal to 50% of your Intellect. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Impact** | 3/3 | changed | Gives your Fire spells a 10% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 1/3 | changed | Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Blast Wave** | 1/1 | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Permafrost** | 3/3 | changed | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |

## Core talents (priority order)

1. **Ice Lance** — Removing it costs 20.9 points of score in this model.
2. **Ignite** — Removing it costs 5.1 points of score in this model.
3. **Pyroblast** — Removing it costs 2.6 points of score in this model.
4. **Heating Up** — Removing it costs 2.5 points of score in this model.
5. **Improved Fire Blast** — Removing it costs 2.3 points of score in this model.
6. **Combustion** — Removing it costs 2.1 points of score in this model.
7. **Fire Power** — Removing it costs 1.8 points of score in this model.
8. **Elemental Precision** — Removing it costs 1.4 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level: pull at max range, the mob walks in at 7 yd/s (slowed by chills), swings every 2 s once in melee (pushing casts back), Frost Nova when it arrives, a 2-second step back, Ice Lance/Frostbolt into the freeze, Fire Blast and wand to finish without overkill. Between fights: 2 s loot, 6 s travel, Evocation when low, conjured water below 35% mana, food below 65% health; a death costs 90 s. Every hit, miss, crit, partial resist, chill, freeze, proc and pushback is rolled.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-11-02, on top of the priority below): Fireball only while the mob has more than 35% health; Scorch only while the mob has more than 35% health; Pyroblast only while the mob has more than 35% health; drink below 15% mana. Together +5.1% time per kill saved for `opt-fire-leveling-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/fire-leveling.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Wand | 0.8 | 1.1 | 1.8 | 1.9 | 2.1 | 5% |
| Fire Blast | 1.4 | 1.7 | 2.0 | 1.9 | 1.9 | 26% |
| Fireball | 2.6 | 1.5 | 1.8 | 1.7 | 1.6 | 25% |
| Ice Lance | 0.8 | 0.9 | 1.1 | 1.2 | 1.1 | 16% |
| Frost Nova | 0.5 | 0.6 | 0.8 | 0.7 | 0.7 | 1% |
| Pyroblast | 0.0 | 0.6 | 0.7 | 0.6 | 0.6 | 11% |
| Blast Wave | 0.0 | 0.2 | 0.3 | 0.3 | 0.3 | 4% |
| Scorch | 0.0 | 0.1 | 0.2 | 0.2 | 0.2 | 1% |
| Counterspell | 0.0 | 0.1 | 0.1 | 0.1 | 0.1 | 0% |

## Notes

- Report: mage/research/talents/forever/optimizer/fire-leveling-leveling-st.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 2/33/16 -> 4/31/16; Improved Fireball -> Accelerant (renamed); Critical Mass 5 -> 3 (rank cap); Elemental Precision -> Precision (renamed); +1 Accelerant (tier gating for Flame Throwing); +1 Accelerant (tier gating for Flame Throwing); +1 Arcane Resilience (tier gating for Missile Barrage); +1 Arcane Resilience (tier gating for Missile Barrage); +1 Wand Specialization (tier gating for Missile Barrage); +1 Wand Specialization (tier gating for Missile Barrage); +1 Improved Channeling (tier gating for Missile Barrage); -1 Improved Scorch (over 51); -1 Improved Scorch (over 51); -1 Missile Barrage (over 51); -1 Missile Barrage (over 51); -1 Improved Channeling (over 51); order dropped (order_repair.py) (refill: the fire-leveling model, leveling-st).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
