# Arcane — Fire filler (the simulator's own build) — 32/16/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/16/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Arcane build (Arcane Fire) for its arcaneFireFill rotation: Arcane Blast and Arcane Missiles with the Arcane cooldowns, Fire spells as the filler.

## Point allocation

### Arcane (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 2/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.2 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |

## Core talents (priority order)

1. **Arcane Power** — For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast
2. **Arcane Instability** — Increases the damage done by your spells by 3% and your critical strike chance by 3%
3. **Presence of Mind** — When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell
4. **Arcane Mind** — Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%
5. **Heating Up** — Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 

## Rank among our builds and the community simulator's

**2 of 4** for `arcane-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`arcane-open-raid`](arcane-open-raid.md) | ours: derived (open search) | 31/17/3 | 579 | +0.0% | 822 | -0.4% | 4 s |
| 2 | **[`arcane-fire-raid`](arcane-fire-raid.md)** | ours: derived (simulator preset) | 32/16/3 | 578 | -0.2% | 826 | +0.0% | 3 s |
| 3 | *Arcane Fire* | community simulator | - | 578 | -0.2% | 826 | +0.0% | 3 s |
| 4 | [`arcane-blast-raid`](arcane-blast-raid.md) | ours: hand draft | 31/13/7 | 557 | -3.8% | 693 | -16.1% | 4 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-24, 14 changes to the base rotation; third-seed check: open winner 519 -> 562 DPS (+8.3%), arcane-blast-raid 524 -> 539 DPS (+2.9%), sim preset: Arcane Frost 546 -> 565 DPS (+3.5%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+2.2%, pass 1)
  2. drop 'mana % < 40%' from the condition: if (stacks of Arcane Blast ≥ 1.5 or mana % < 40%): cast Frostbolt (+0.4%, pass 1)
  3. insert at the top: if mana ≥ (time left in the fight × 110): cast Fire Blast + threshold 110 -> 220: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  4. drop the condition: if mana ≥ (time left in the fight × 220): cast Fire Blast (+2.9%, pass 2)
  5. move down below 'use every other cooldown when ready': cast Fire Blast (+0.4%, pass 2)
  6. drop: if mana % < 15% and time left in the fight > 20s: cast Evocation (+0.9%, pass 5)
  7. insert at the end: cast Fireball (+0.6%, pass 5)
  8. insert in the middle: cast Arcane Wrath (+4.8%, pass 6)
  9. insert in the middle: if Arcane Blast is up and time left on Arcane Blast < cast time of Arcane Blast: cast Arcane Blast (+1.0%, pass 6)
  10. insert at the end: cast Frost Blast (+0.9%, pass 6)
  11. insert before the filler: cast Robe of the Archmage (+0.5%, pass 6)
  12. move down below 'if Missile Barrage is up: cast Arcane Missiles (rank 7)': cast Fire Blast (+0.2%, pass 6)
  13. only with 10s or more of the fight left: if stacks of Arcane Blast ≥ 1.5: cast Frostbolt (rank 10) (+0.2%, pass 6)
  14. insert before the filler: cast Mana Citrine (+0.3%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 16 passes, the last 2026-11-20, 29 changes to the base rotation; third-seed check: arcane-fire-raid 826 -> 826 DPS (+0.0%), arcane-blast-raid 693 -> 693 DPS (+0.0%), arcane-open-raid 823 -> 823 DPS (+0.0%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+0.2%, pass 1)
  2. insert in the middle: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.3%, pass 2)
  3. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.4%, pass 2)
  4. move down below 'if Missile Barrage is up: cast Arcane Missiles': cast Fire Blast (+3.3%, pass 6)
  5. drop: if (stacks of Arcane Blast ≥ 1.5 or mana % < 40%): cast Frostbolt (+0.3%, pass 6)
  6. only with 20s or more of the fight left: cast Fire Blast (+0.2%, pass 6)
  7. threshold 20s -> 40s: if time left in the fight ≥ 20s: cast Fire Blast (+0.2%, pass 6)
  8. insert at the end: if stacks of Arcane Blast ≥ 2: cast Fire Blast (+0.2%, pass 6)
  9. only with 3s or more of the fight left: cast Arcane Blast (+0.2%, pass 6)
  10. drop the condition: if stacks of Arcane Blast ≥ 2: cast Fire Blast (+0.3%, pass 6)
  11. insert at the end: cast Fireball (rank 11) (+207.8%, pass 8)
  12. insert before the filler: cast Arcane Wrath (+7.4%, pass 8)
  13. insert at the end: cast Mana Citrine (+0.2%, pass 8)
  14. move to the top: cast Arcane Wrath (+8.9%, pass 9)
  15. insert in the middle: if (auraIsInactive or time left on Arcane Blast < cast time of Arcane Blast): cast Arcane Blast (+1.5%, pass 9)
  16. move to the top: if Missile Barrage is up: cast Arcane Missiles (rank 7) (+1.1%, pass 9)
  17. move to the top: use every other cooldown when ready (+1.4%, pass 9)
  18. insert before the filler: cast Frost Blast (+0.4%, pass 9)
  19. only with 10s or more of the fight left: cast Arcane Wrath (+0.3%, pass 9)
  20. threshold 20s -> 40s: if mana % < 15% and time left in the fight > 20s: cast Evocation (+0.2%, pass 9)
  21. threshold 40s -> 80s: if mana % < 15% and time left in the fight > 40s: cast Evocation (+0.3%, pass 9)
  22. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+0.2%, pass 9)
  23. only above 25% mana: if time left in the fight ≥ 3s: cast Arcane Blast (+0.2%, pass 9)
  24. drop: if mana % < 15% and time left in the fight > 80s: cast Evocation (+3.8%, pass 10)
  25. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast ≤ 2) and not spellIsCasting: cast Arcane Blast (+0.2%, pass 11)
  26. drop 'stacks of Arcane Blast < 2' from the condition: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+0.5%, pass 11)
  27. insert in the middle: if stacks of Heating Up = 3 and not spellIsCasting: cast Pyroblast (+1.9%, pass 12)
  28. drop the condition: if time left in the fight ≥ 40s: cast Fire Blast (+0.5%, pass 13)
  29. drop: cast Mana Citrine (+0.2%, pass 13)

Before the pull: at -2s: if Ice Barrier is known: cast Ice Barrier.

| # | Priority (the first line whose condition holds is cast) | [`arcane-fire-raid`](arcane-fire-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 3.6 |
| 3 | cast Fire Blast | 7.9 |
| 4 | if Arcane Blast is up and time left on Arcane Blast < cast time of Arcane Blast: cast Arcane Blast | 6.8 |
| 5 | cast Arcane Wrath | 5.3 |
| 6 | if stacks of Arcane Blast ≥ 1.5 and time left in the fight ≥ 10s: cast Frostbolt (rank 10) | 2.6 |
| 7 | cast Arcane Blast | 6.8 |
| 8 | cast Robe of the Archmage | as ready |
| 9 | cast Mana Citrine | as ready |

Lines of the simulator's rotation these builds never cast: cast Ice Barrier (needs the Ice Barrier talent); cast Fireball (rank 11) (its condition never held in these fights).

Damage by ability:

| Ability | [`arcane-fire-raid`](arcane-fire-raid.md) |
|---|---|
| Arcane Wrath | 29% |
| Arcane Missiles | 24% |
| Fire Blast | 20% |
| Arcane Blast | 14% |
| Frostbolt | 8% |
| Ignite | 3% |
| Demonic Rune | 1% |
| Fireball | 0% |

## Notes

- The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% ahead on two seeds and passing the spec's rules.
- Simulator numbers are the community's model of the game, not in-game measurements.

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/mage/dps/presets.ts>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
