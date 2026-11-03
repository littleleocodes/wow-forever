# Balance — PvP (derived) — 32/11/8

*[Druid](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/11/8 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Balance PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Balance (model balance-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Balance builds agree with (2194 builds).

## Point allocation

### Balance (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 5/5 | changed | Reduces the cast time of your Wrath spell by 0.5 sec and its Mana cost by 50%. |
| **Improved Moonfire** | 2/2 | changed | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Moonglow** | 3/3 | changed | Reduces the Mana cost of your damaging spells by 25%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 1/2 | changed | Increases the range of your offensive Balance spells by 10% and improves your chance to hit by 2%. |
| **Improved Entangling Roots** | 2/3 | changed | Increases the damage done by your Entangling Roots spell by 50%, and its victims can take up to 50% more damage without interrupting the effect. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |
| **Improved Starfire** | 5/5 | changed | Reduces the cast time of Starfire by 0.5 sec and Starfire has a 15% chance to stun its target for 3 sec. |
| **Vengeance** | 5/5 | changed | Increases the critical strike damage bonus of your Arcane and Nature spells by 100%. |
| **Eclipse** | 3/3 | **NEW** | Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges. Lasts 15 sec. |
| **Nature's Grace** | 1/1 | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. |
| **Moonfury** | 1/5 | changed | Increases the damage done by your Arcane and Nature spells by 2%. |
| **Moonkin Form** | 1/1 | changed | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. |

### Feral Combat (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Brutal Impact** | 2/2 | changed | Increases the stun duration of your Bash and Pounce abilities by 1 sec and reduces the cooldown of Bash by 30 sec. |
| **Feral Instinct** | 1/3 | changed | Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |

### Restoration (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |

## Core talents (priority order)

1. **Improved Starfire** — The scorer's value in this build: +13.6% of its score (model balance-dps).
2. **Vengeance** — The scorer's value in this build: +13.0% of its score (model balance-dps).
3. **Moonkin Form** — The scorer's value in this build: +11.3% of its score (model balance-dps).
4. **Eclipse** — The scorer's value in this build: +11.1% of its score (model balance-dps).
5. **Feral Swiftness** — The scorer's value in this build: +9.2% of its score (model balance-dps).
6. **Nature's Focus** — The scorer's value in this build: +6.9% of its score (model balance-dps).

## Notes

- Community tie-break moves: 1 point Improved Entangling Roots -> Nature's Reach.
- Where we disagree with the community: most Balance builds take Insect Swarm (91% take it), which the model values below this build's weakest point; this build takes Brutal Impact (10%), Feral Charge (9%), Feral Instinct (5%), Feral Swiftness (10%), which few Balance builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 32/11/8 -> 32/11/8; +1 Furor (tier gating for Brutal Impact); +1 Furor (tier gating for Brutal Impact); +1 Furor (tier gating for Brutal Impact); +1 Furor (tier gating for Brutal Impact); +1 Furor (tier gating for Brutal Impact); -1 Heart of the Wild (over 51); -1 Heart of the Wild (over 51); -1 Heart of the Wild (over 51); -1 Heart of the Wild (over 51); -1 Heart of the Wild (over 51) (refill: the balance-dps model, pvp).

## Open questions (verify in the live game)

- A derived Balance PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
