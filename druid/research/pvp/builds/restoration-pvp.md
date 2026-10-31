# Restoration — PvP (derived) — 0/11/40

*[Druid](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/11/40 (Balance / Feral Combat / Restoration) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Restoration PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Restoration (model resto-heal, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Restoration builds agree with (1920 builds).

## Point allocation

### Balance (0)

*No points.*

### Feral Combat (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Brutal Impact** | 2/2 | changed | Increases the stun duration of your Bash and Pounce abilities by 1 sec and reduces the cooldown of Bash by 30 sec. |
| **Feral Instinct** | 1/3 | changed | Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |

### Restoration (40)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Gift of Nature** | 5/5 | changed | Increases the effect of all your healing spells by 10%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell becomes an instant cast spell. |
| **Improved Regrowth** | 5/5 | unchanged | Increases the critical effect chance of your Regrowth spell by 50%. |
| **Wild Growth** | 1/1 | **NEW** | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. |

## Core talents (priority order)

1. **Swiftmend** — The scorer's value in this build: +16.8% of its score (model resto-heal).
2. **Wild Growth** — The scorer's value in this build: +13.5% of its score (model resto-heal).
3. **Nature's Focus** — The scorer's value in this build: +9.9% of its score (model resto-heal).
4. **Feral Swiftness** — The scorer's value in this build: +8.8% of its score (model resto-heal).
5. **Naturalist** — The scorer's value in this build: +8.0% of its score (model resto-heal).
6. **Nature's Swiftness** — The scorer's value in this build: +7.8% of its score (model resto-heal).

## Notes

- Scores +22.5% of the optimum's talent value above the hand draft pvp-resto, over the 2% replacement bar: this build is the spec's PvP pick, the hand draft stays as the alternative.
- Community tie-break moves: 2 points Feral Instinct -> Improved Regrowth; 1 point Furor -> Improved Regrowth.
- Where we disagree with the community: most Restoration builds take Nature's Majesty (89% take it), Genesis (88% take it), Nature's Splendor (83% take it), Moonglow (71% take it), which the model values below this build's weakest point; this build takes Feral Instinct (12%), which few Restoration builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 0/11/40 -> 0/11/40; Gift of the Earthmother 1 gone; +1 Furor (tier gating for Brutal Impact) (refill: the resto-heal model, pvp).

## Open questions (verify in the live game)

- A derived Restoration PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
