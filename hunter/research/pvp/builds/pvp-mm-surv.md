# Marksmanship with Survival support (PvP, 0/31/20) — 0/31/20

*[Hunter](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/31/20 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `pvp-mm-surv` |

## Summary

Improved Concussive Shot stuns, Scatter Shot, Lethal Attacks and Mortal Shots, Trueshot Aura; Survival for Improved Wing Clip roots, Surefooted, Deterrence, Survival Tactics (trap hit) and Counterattack. Improved Feign Death and Wyvern Sting are gone.

## Point allocation

### Beast Mastery (0)

*No points.*

### Marksmanship (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Concussive Shot** | 5/5 | unchanged | Gives your Concussive Shot a 20% chance to stun the target for 3 sec. |
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 1/3 | **NEW** | Increases the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yds by 30. |
| **Mortal Shots** | 5/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 30%. |
| **Barrage** | 3/3 | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 10%. |
| **Scatter Shot** | 1/1 | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |
| **Ranged Weapon Specialization** | 5/5 | unchanged | Increases the damage you deal with ranged weapons by 5%. |

### Survival (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 5/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Entrapment** | 2/5 | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 2 sec. |
| **Survivalist** | 2/5 | changed | Increases your total Health by 4%. |
| **Improved Wing Clip** | 3/3 | changed | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |
| **Clever Traps** | 1/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 15% and the damage of Immolation and Explosive trap effects by 15%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |

## Core talents (priority order)

1. **Scatter Shot** — Disorient for trap setups.
2. **Improved Concussive Shot** — Stun procs on Concussive Shot (4%/rank est. 20%).
3. **Improved Wing Clip** — Root procs (7%/rank est. 21%).
4. **Counterattack** — Root after a parry; requires Deterrence.
5. **Survival Tactics** — +10% hit with traps and Feign Death (est.).
6. **Deterrence** — +25% dodge/parry for 10s.
7. **Improved Tracking** — +5% vs. Humanoids while tracking them.
8. **Mortal Shots** — Ranged crit damage.
9. **Lethal Attacks** — Crit.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 4 | Entrapment 2 + Survivalist 2 | Deflection, Savage Strikes | Gating fillers in Survival. |
| 1 | Improved Stings | Efficiency | Thirty-first Marksmanship point. |

## Notes

- Sniper Shot's 4s cast is not taken for PvP.
- 2026-09-30: renamed from "Marksmanship / Survival (PvP, 0/31/20)" so the name matches the spec the pages file it under (the point split decides the spec, spec_modes.py).

## Open questions (verify in the live game)

- Whether Aimed Shot exists baseline for PvP burst.

## Sources

- <https://warcraftforever.games/talents/hunter>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
