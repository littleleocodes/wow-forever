# Melee Survival leveling (dual wield, pet kept) — 9/10/32

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/10/32 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Leveling as a melee hunter with the pet as the tank: Survival's melee package first (Improved Tracking, Savage Strikes, Surefooted, Predator's Edge, Strider Kick at 30, Expose Prey, Resourcefulness), then Lethal Attacks, Lightning Reflexes, Careful Aim, Deadly Aspects and Focused Fire, and Lacerating Strikes at 58. No Lone Wolf, Improved Wing Clip or Improved Aspect of the Monkey: the pet holds the mob, so the hunter never needs to root, kite or dodge it. Adopted 2026-09-27 from opt-melee-dps-leveling-st, the fight lab's fastest melee build: 18.0/24.1/27.3/29.4/33.7 s per kill at 20/30/40/50/60 against 18.4/24.6/34.2/36.1/42.0 s for the previous Lone Wolf draft.

## Point allocation

### Beast Mastery (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Pathfinding** | 2/2 | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |

### Marksmanship (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |

### Survival (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 4/5 | unchanged | Increases your Parry chance by 4%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 10%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Survival | Improved Tracking | 5 | 0/0/5 |
| 15-16 | Survival | Savage Strikes | 2 | 0/0/7 |
| 17-19 | Survival | Deflection | 3 | 0/0/10 |
| 20-22 | Survival | Surefooted | 3 | 0/0/13 |
| 23 | Survival | Deterrence | 1 | 0/0/14 |
| 24 | Survival | Deflection | 1 | 0/0/15 |
| 25-29 | Survival | Predator's Edge | 5 | 0/0/20 |
| 30 | Survival | Strider Kick | 1 | 0/0/21 |
| 31-32 | Survival | Expose Prey | 2 | 0/0/23 |
| 33 | Survival | Resourcefulness | 1 | 0/0/24 |
| 34-38 | Marksmanship | Lethal Attacks | 5 | 0/5/24 |
| 39 | Survival | Resourcefulness | 1 | 0/5/25 |
| 40-44 | Survival | Lightning Reflexes | 5 | 0/5/30 |
| 45-48 | Marksmanship | Careful Aim | 4 | 0/9/30 |
| 49-53 | Beast Mastery | Deadly Aspects | 5 | 5/9/30 |
| 54-55 | Beast Mastery | Focused Fire | 2 | 7/9/30 |
| 56 | Marksmanship | Careful Aim | 1 | 7/10/30 |
| 57 | Survival | Counterattack | 1 | 7/10/31 |
| 58 | Survival | Lacerating Strikes | 1 | 7/10/32 |
| 59-60 | Beast Mastery | Pathfinding | 2 | 9/10/32 |

## Core talents (priority order)

1. **Strider Kick** — 100% weapon damage every 8 s: the biggest single talent at 60 (fight lab: +10.9% time per kill without it).
2. **Resourcefulness** — -60% mana on melee abilities and regen on crits: the melee loop runs out of mana without it (fight lab +11.5% at 60, almost all downtime).
3. **Lethal Attacks** — +5% crit with all attacks, worth double with Predator's Edge (fight lab +6.1% at 60).
4. **Expose Prey** — Mongoose Bite procs against the marked target: the second strike of the loop (fight lab +6.0% at 60).
5. **Predator's Edge** — +30% melee crit damage and +50% off-hand damage: the reason to dual-wield (fight lab +5.6% at 60).
6. **Careful Aim** — Attack power from Intellect (fight lab +4.8% at 60).
7. **Improved Tracking** — +5% damage against the tracked creature type: every leveling mob has one (fight lab +3.6% at 60).
8. **Lightning Reflexes** — +15% Agility (fight lab +3.0% at 60).
9. **Savage Strikes** — Crit on Raptor Strike, Mongoose Bite and Strider Kick (fight lab +2.9% at 60).
10. **Focused Fire** — Pet damage: the pet tanks and still does a fifth of the damage (fight lab +2.2% at 60).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Deflection | Survivalist | Survival points on the way to Lacerating Strikes: with the pet tanking the hunter is rarely hit (fight lab +0.6% at 60). |
| 2 | Deterrence 1 + Counterattack 1 | Survivalist | Tier fillers for the capstone; the pet takes the hits, so parry procs are rare (fight lab 0.0% and -0.1% at 60). |
| 2 | Pathfinding | Endurance Training, Improved Revive Pet | +run speed between pulls; the fight lab uses a fixed 6 s travel, so only the scorer's travel value counts it. |

## Leveling rotation (fight lab)

The melee hunter: Serpent Sting from range, then stand and fight beside the pet: Raptor Strike queued on the next swing whenever it is ready, Deterrence when low, Counterattack after a parry, Mongoose Bite when a dodge or Expose Prey activates it, Strider Kick on cooldown, Immolation Trap at your feet, then (with Expose Prey) Hunter's Mark in a free global cooldown; Mend Pet for the pet.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): never cast Serpent Sting. Together +1.7% time per kill saved for `leveling-melee` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/melee-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|
| Melee (off-hand) | 3.2 | 4.2 | 5.5 | 6.4 | 7.6 | 12% |
| Claw | 3.6 | 4.1 | 4.7 | 5.0 | 5.5 | 6% |
| Melee | 1.8 | 2.4 | 3.4 | 3.9 | 4.8 | 13% |
| Growl | 1.9 | 2.4 | 3.1 | 3.4 | 3.9 | 0% |
| Raptor Strike | 1.4 | 1.8 | 2.2 | 2.4 | 2.8 | 14% |
| Strider Kick | 0.0 | 1.7 | 2.0 | 2.3 | 2.5 | 9% |
| Mongoose Bite | 0.0 | 0.0 | 0.9 | 1.1 | 1.4 | 6% |
| Auto Shot | 1.2 | 1.2 | 1.2 | 1.2 | 1.1 | 5% |
| Bite | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 2% |
| Hunter's Mark | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 | 0% |
| Immolation Trap | 0.5 | 0.5 | 0.5 | 0.6 | 0.7 | 9% |
| Counterattack | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0% |
| Mend Pet | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Pull with Hunter's Mark and Serpent Sting and send the pet; the pet holds the mob while you strike beside it: Mongoose Bite when active, Strider Kick on cooldown, Raptor Strike on the next swing.
- Why no Improved Wing Clip, Improved Aspect of the Monkey or Lone Wolf (2026-09-27 scenario audit): a melee hunter stands next to the mob, so a root to open distance does nothing (fight lab 0.0% at 30 and 60); the pet keeps the mob off you, so dodge talents add nothing (0.0%); and dropping the pet at 51 made the hunter take every hit (downtime 3.4 s -> 10.3 s per kill at 60).
- Fight lab: hunter/leveling/fightlab/melee-dps.md compares this build with the Beast Mastery and Marksmanship leveling builds under their own models.

## Open questions (verify in the live game)

- Melee hunter numbers are the scorer's assumptions and the fight lab's rotation, not measurements: the community simulator has no melee hunter rotation, so the raid build has no simulator DPS.
- Expose Prey's proc rate against a marked target (5%/rank per attack assumed) decides how often Mongoose Bite is available; check the actual rate in the beta.
- Whether Aspect of the Beast (+110 melee attack power) and the Deadly Aspects melee haste proc work as the tooltips read.
- Counterattack after a parry: the base parry chance of a hunter in the beta (5% assumed, +2%/rank Deflection).
- Lacerating Strikes: 40% of Mongoose Bite over 21 s; whether the bleed can crit or stack.
- Whether the pet holds melee-hunter threat as well as the fight lab assumes (it Growls every 5 s and loses the mob when your threat passes 130% of its own).

## Sources

- <https://warcraftforever.games/talents/hunter>
- <beta client 1.60.1.70009 tooltips (_reference/data/forever-talents/hunter.json)>
- <hunter/raid/optimizer/melee-dps-raid-dps.md>
- <hunter/leveling/optimizer/melee-dps-leveling-st.md>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
