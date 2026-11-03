# Survival — Melee (Strider Kick / Lacerating Strikes) — 9/11/31

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/11/31 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The demo Survival tree is a melee tree: Predator's Edge (melee crit damage, off-hand damage), Expose Prey (Mongoose Bite procs), Strider Kick, Resourcefulness, Lightning Reflexes (+10% Agility) and the Lacerating Strikes capstone (Mongoose Bite bleed), with Lethal Attacks and Careful Aim from Marksmanship and Deadly Aspects (Aspect of the Beast melee variant) from Beast Mastery. Entirely new; listed so it can be tested.

## Point allocation

### Beast Mastery (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 2/5 | changed | Increases the Health and Armor of your pets by 6%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |

### Marksmanship (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Efficiency** | 1/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 3%. |

### Survival (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Clever Traps** | 1/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 15% and the damage of Immolation and Explosive trap effects by 15%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Core talents (priority order)

1. **Lacerating Strikes** — Capstone: Mongoose Bite bleeds for 40% of its damage over 21s.
2. **Expose Prey** — Attacks on Hunter's Marked targets activate Mongoose Bite (5%/rank est.).
3. **Predator's Edge** — +6%/rank melee crit damage and +10%/rank off-hand damage (est.).
4. **Strider Kick** — 100% weapon damage instant on an 8s cooldown.
5. **Lightning Reflexes** — +10% Agility (est.).
6. **Savage Strikes** — Melee ability crit.
7. **Lethal Attacks** — Crit with all attacks.
8. **Careful Aim** — AP from Intellect.
9. **Deadly Aspects** — Aspect of the Beast: melee haste procs (demo text truncated).
10. **Resourcefulness** — Cheaper melee abilities/traps, regen on crits.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Survivalist 3 + Clever Traps 1 | Deflection, Improved Wing Clip | Gating fillers. |
| 4 | Endurance Training 2 + Focused Fire 2 | Improved Revive Pet | Beast Mastery fillers with the pet kept. |

## Rotation

Not simulated in the community simulator (no spec model of this playstyle there); see the [raid README](../README.md).

## Notes

- Dual-wield hunter melee did not exist in Classic; Predator's Edge's off-hand damage implies it does now.
- 2026-09-27 scenario audit: Counterattack 1 -> Efficiency 1. Counterattack strikes after you parry; behind a raid boss you are never attacked, so it never fires. Efficiency makes Raptor Strike, Mongoose Bite and Serpent Sting cheaper (scorer +0.6 points).

## Open questions (verify in the live game)

- Whether melee Survival is competitive at all — pure test build.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
