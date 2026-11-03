# Enhancement — PvP (derived) — 18/33/0

*[Shaman](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/33/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Enhancement PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Enhancement (model enhancement-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Enhancement builds agree with (5577 builds).

## Point allocation

### Elemental (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Call of Flame** | 2/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock and Fire Nova spells by 10%, as well as increases the duration of your Flame Shock spell by 6 sec. |
| **Reverberation** | 5/5 | changed | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Elemental Warding** | 3/3 | changed | Reduces damage taken from Fire, Frost, and Nature effects by 10%. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt and Chain Lightning spells a 70% chance to not lose casting time when you take damage. |

### Enhancement (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Mental Dexterity** | 3/3 | **NEW** | Increases your Attack Power by an amount equal to 150% of your Intellect. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Elemental Weapons** | 1/3 | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 7%, your Windfury Weapon effect by 13% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 5%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Flurry** | 4/5 | changed | Increases your attack speed by 24% for your next 3 swings after dealing a melee critical strike. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Stormstrike** | 1/1 | changed | Instantly strike for 150% normalized weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |
| **Toughness** | 4/5 | changed | Increases your Stamina by 8%. |
| **Improved Stormstrike** | 2/2 | **NEW** | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |
| **Mental Quickness** | 2/2 | **NEW** | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Maelstrom Weapon** | 2/5 | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 8%. Stacks up to 5 times. Lasts 30 sec. |
| **Rage of the Farseer** | 1/1 | **NEW** | Increases your attack speed by 30% for 25 sec. |

### Restoration (0)

*No points.*

## Core talents (priority order)

1. **Stormstrike** — The scorer's value in this build: +15.3% of its score (model enhancement-dps).
2. **Rage of the Farseer** — The scorer's value in this build: +11.3% of its score (model enhancement-dps).
3. **Reverberation** — The scorer's value in this build: +11.1% of its score (model enhancement-dps).
4. **Shamanistic Focus** — The scorer's value in this build: +9.8% of its score (model enhancement-dps).
5. **Improved Ghost Wolf** — The scorer's value in this build: +9.8% of its score (model enhancement-dps).
6. **Eye of the Storm** — The scorer's value in this build: +9.8% of its score (model enhancement-dps).

## Notes

- Community tie-break moves: 2 points Maelstrom Weapon -> Improved Stormstrike; 1 point Guardian Totems -> Elemental Weapons; 1 point Maelstrom Weapon -> Flurry.
- Where we disagree with the community: most Enhancement builds take Ancestral Knowledge (76% take it), Elemental Devastation (74% take it), which the model values below this build's weakest point; this build takes Elemental Warding (16%), Eye of the Storm (2%), which few Enhancement builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-11-03 (repair_builds.py, client build 1.60.1.70753 trees): 18/33/0 -> 18/33/0; +1 Guardian Totems (tier gating for Anticipation); +1 Guardian Totems (tier gating for Anticipation); -1 Spirit Weapons (over 51); -1 Toughness (over 51) (refill: the enhancement-dps model, pvp).

## Open questions (verify in the live game)

- A derived Enhancement PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
