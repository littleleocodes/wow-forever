# Elemental — PvP (derived) — 35/16/0

*[Shaman](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 35/16/0 (Elemental / Enhancement / Restoration) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Elemental PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Elemental (model elemental-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Elemental builds agree with (3007 builds).

## Point allocation

### Elemental (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Concussion** | 5/5 | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |
| **Call of Flame** | 2/3 | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 10%, as well as increases the duration of your Flame Shock spell by 6 sec. |
| **Elemental Alacrity** | 3/3 | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Reverberation** | 5/5 | changed | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Elemental Focus** | 1/1 | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Elemental Warding** | 3/3 | changed | Reduces damage taken from Fire, Frost, and Nature effects by 10%. |
| **Earthbound** | 1/1 | **NEW** | Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast. |
| **Eye of the Storm** | 3/3 | changed | Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 70% chance to not lose casting time when you take damage. |
| **Trial by Fire** | 1/2 | **NEW** | Increases the damage done by your Fire Nova spell by 10% and reduces its cooldown by 2 sec, and increases the duration of your Magma Totem by 10 sec. |
| **Elemental Reach** | 2/2 | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 6 yards and reduces the cooldown of Totemic Projection by 20 sec. |
| **Lava Burst** | 1/1 | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. |
| **Lightning Overload** | 3/3 | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |
| **Elemental Fury** | 5/5 | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Enhancement (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Earth's Grasp** | 2/2 | moved | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |

### Restoration (0)

*No points.*

## Core talents (priority order)

1. **Elemental Fury** — The scorer's value in this build: +17.8% of its score (model elemental-dps).
2. **Eye of the Storm** — The scorer's value in this build: +10.5% of its score (model elemental-dps).
3. **Reverberation** — The scorer's value in this build: +10.0% of its score (model elemental-dps).
4. **Improved Ghost Wolf** — The scorer's value in this build: +10.0% of its score (model elemental-dps).
5. **Earthbound** — The scorer's value in this build: +10.0% of its score (model elemental-dps).
6. **Lava Burst** — The scorer's value in this build: +7.5% of its score (model elemental-dps).

## Notes

- Scores +40.4% of the optimum's talent value above the hand draft pvp-elemental-ns, over the 2% replacement bar: this build is the spec's PvP pick, the hand draft stays as the alternative.
- Community tie-break moves: 1 point Elemental Warding -> Improved Fire Nova.
- Where we disagree with the community: most Elemental builds take Convection (76% take it), which the model values below this build's weakest point; this build takes Anticipation (5%), Earth's Grasp (12%), Guardian Totems (12%), Stormstrike (18%), which few Elemental builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 35/16/0 -> 35/16/0; Improved Fire Nova -> Trial by Fire (renamed); Call of Thunder 1 gone; refill +1 Elemental Warding (refill: the elemental-dps model, pvp).

## Open questions (verify in the live game)

- A derived Elemental PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
