# Restoration — PvP (derived) — 0/20/31

*[Shaman](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/20/31 (Elemental / Enhancement / Restoration) |
| **Role** | HEALER — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Restoration PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Restoration (model resto-heal, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Restoration builds agree with (1730 builds).

## Point allocation

### Elemental (0)

*No points.*

### Enhancement (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Earth's Grasp** | 2/2 | moved | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Thundering Strikes** | 5/5 | changed | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Guardian Totems** | 2/2 | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Improved Ghost Wolf** | 2/2 | changed | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Shamanistic Focus** | 1/1 | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. |
| **Anticipation** | 3/3 | changed | Increases your chance to dodge by an additional 6%. |
| **Toughness** | 4/5 | changed | Increases your Stamina by 8%. |
| **Stormstrike** | 1/1 | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. |

### Restoration (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Healing Wave** | 5/5 | changed | Reduces the casting time of your Healing Wave spell by 0.5 sec. |
| **Mindfulness** | 2/3 | **NEW** | Allows 33% of your Mana regeneration to continue while casting. |
| **Tidal Focus** | 4/5 | changed | Reduces the Mana cost of your healing spells by 4% and improves your chance to hit by 4%. |
| **Improved Reincarnation** | 2/2 | changed | Reduces the cooldown of your Reincarnation spell by 20 min, increases your maximum health by 4%, and increases the amount of health and Mana you reincarnate with by an additional 20%. |
| **Ancestral Healing** | 3/3 | moved | Increases your target's armor value by 25% for 15 sec after getting a critical effect from one of your healing spells. |
| **Healing Focus** | 3/3 | changed | Gives your healing spells a 70% chance to not lose casting time when you take damage. |
| **Restorative Totems** | 1/5 | changed | Increases the effect of your Mana Spring Totem by 5% and increases the effect of your Healing Stream Totem by 10%. |
| **Mana Tide Totem** | 1/1 | changed | Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards. |
| **Healing Way** | 3/3 | changed | Increases the amount healed by your Healing Wave spell by 25%. |
| **Nature's Swiftness** | 1/1 | unchanged | When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell. |
| **Purification** | 5/5 | unchanged | Increases the effectiveness of your healing spells by 10%. |
| **Riptide** | 1/1 | **NEW** | Heals a friendly target for 485 to 533, an additional 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%. |

## Core talents (priority order)

1. **Healing Way** — The scorer's value in this build: +17.0% of its score (model resto-heal).
2. **Riptide** — The scorer's value in this build: +16.9% of its score (model resto-heal).
3. **Improved Healing Wave** — The scorer's value in this build: +14.2% of its score (model resto-heal).
4. **Purification** — The scorer's value in this build: +9.0% of its score (model resto-heal).
5. **Nature's Swiftness** — The scorer's value in this build: +8.8% of its score (model resto-heal).
6. **Improved Ghost Wolf** — The scorer's value in this build: +7.8% of its score (model resto-heal).

## Notes

- Community tie-break moves: 1 point Restorative Totems -> Mana Tide Totem; 2 points Restorative Totems -> Mindfulness; 1 point Restorative Totems -> Ancestral Healing.
- Where we disagree with the community: most Restoration builds take Water Shield (96% take it), Tidal Mastery (88% take it), Ancestral Knowledge (85% take it), which the model values below this build's weakest point; this build takes Anticipation (7%), Earth's Grasp (5%), Guardian Totems (18%), Toughness (8%), which few Restoration builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.

## Open questions (verify in the live game)

- A derived Restoration PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/shaman>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
