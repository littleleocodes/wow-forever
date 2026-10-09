# Survival — PvP (derived) — 0/21/30

*[Hunter](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/21/30 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Survival (model melee-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Survival builds agree with (13808 builds).

## Point allocation

### Beast Mastery (0)

*No points.*

### Marksmanship (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Concussive Shot** | 5/5 | unchanged | Gives your Concussive Shot a 20% chance to stun the target for 3 sec. |
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party members within 45 yds by 30. |
| **Scatter Shot** | 1/1 | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. |

### Survival (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 3/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 3%. |
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Resourcefulness** | 2/2 | **NEW** | Reduces the mana cost of your Trap abilities and melee abilities by 60%. In addition, your critical strikes have a 60% chance to allow 50% of your Mana regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 1/5 | changed | Increases your Agility by 2%. |

## Core talents (priority order)

1. **Strider Kick** — The scorer's value in this build: +15.0% of its score (model melee-dps).
2. **Resourcefulness** — The scorer's value in this build: +11.5% of its score (model melee-dps).
3. **Surefooted** — The scorer's value in this build: +10.4% of its score (model melee-dps).
4. **Deterrence** — The scorer's value in this build: +10.2% of its score (model melee-dps).
5. **Careful Aim** — The scorer's value in this build: +8.5% of its score (model melee-dps).
6. **Scatter Shot** — The scorer's value in this build: +7.6% of its score (model melee-dps).

## Notes

- Community tie-break moves: 2 points Improved Tracking -> Clever Traps; 1 point Rapid Killing -> Trueshot Aura.
- Where we disagree with the community: most Survival builds take Lacerating Strikes (81% take it), Deadly Aspects (78% take it), Survivalist's Discipline (73% take it), which the model values below this build's weakest point; this build takes Improved Concussive Shot (10%), Improved Stings (8%), Scatter Shot (7%), Trueshot Aura (7%), which few Survival builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- Scored with the melee hunter model (the only Survival model): a ranged Survival PvP hunter is not modelled.

## Open questions (verify in the live game)

- A derived Survival PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
