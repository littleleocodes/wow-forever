# Marksmanship — PvP (derived) — 0/31/20

*[Hunter](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/31/20 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Marksmanship PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Marksmanship (model mm-raid, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Marksmanship builds agree with (7556 builds).

## Point allocation

### Beast Mastery (0)

*No points.*

### Marksmanship (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Hawk Eye** | 3/3 | moved | Increases the range of your ranged weapons by 6 yards. |
| **Improved Concussive Shot** | 5/5 | unchanged | Gives your Concussive Shot a 20% chance to stun the target for 3 sec. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Rapid Killing** | 2/2 | **NEW** | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Improved Arcane Shot** | 5/5 | changed | Reduces the cooldown of your Arcane Shot by 1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 15. |
| **Mortal Shots** | 2/5 | changed | Increases the critical strike damage bonus on all ranged abilities by 12%. |
| **Scatter Shot** | 1/1 | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |
| **Ranged Weapon Specialization** | 2/5 | unchanged | Increases the damage you deal with ranged weapons by 2%. |
| **Sniper Shot** | 1/1 | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. |

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

1. **Surefooted** — The scorer's value in this build: +11.0% of its score (model mm-raid).
2. **Deterrence** — The scorer's value in this build: +10.9% of its score (model mm-raid).
3. **Deflection** — The scorer's value in this build: +9.6% of its score (model mm-raid).
4. **Scatter Shot** — The scorer's value in this build: +8.7% of its score (model mm-raid).
5. **Improved Wing Clip** — The scorer's value in this build: +8.7% of its score (model mm-raid).
6. **Improved Concussive Shot** — The scorer's value in this build: +8.7% of its score (model mm-raid).

## Notes

- Scores +16.4% of the optimum's talent value above the hand draft pvp-mm-surv, over the 2% replacement bar: this build is the spec's PvP pick, the hand draft stays as the alternative.
- Community tie-break moves: 1 point Ranged Weapon Specialization -> Lone Wolf; 2 points Ranged Weapon Specialization -> Rapid Killing.
- Where we disagree with the community: most Marksmanship builds take Lethal Attacks (95% take it), Barrage (78% take it), which the model values below this build's weakest point; this build takes Survival Tactics (10%), which few Marksmanship builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Marksmanship PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
