# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-open-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-2255000013012503-2135000301203002-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 7.5 seconds left
4. **Frostfire Bolt** when your mana is below 30%
5. **Frostfire Bolt** when you have at least 10% mana

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Improved Fire Blast**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest single gain of the full-raid rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5.
- **Frostfire Bolt** is the main spell: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the full rotation casts Rank 2 (285 mana against 370): the page's line "when your mana is below 30%". The simulator measured this about 2% better than the old rule of stopping at 10% mana.
- **Fireball** (Rank 2 in the full rotation) is last: a stopgap for when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only part of your spell power; keep your mana up with gems and a potion so it rarely comes up.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds 30% of the base cost on each Fire or Frost crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.
- The full rotation also opens with **Arcane Power** for builds that take it; this build does not, so skip it.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 802 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 789 | [0/29/22](https://talentsforever.com/mage/60/-2355000013011503-2035020301013002-7) |
| Phase 1 BiS | 793 | [0/29/22](https://talentsforever.com/mage/60/-2355000013011503-1135001321003002-7) |

**The gear** (average item level: Pre-BiS 62.7; Phase 1 BiS 63.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Arcanist Crown](https://www.wowhead.com/forever/item=16795) · *Garr, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Inferno Gloves](https://www.wowhead.com/forever/item=18408) · *Tailoring* | [Gloves of the Hypnotic Flame](https://www.wowhead.com/forever/item=18808) · *Molten Core* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Arcanist Boots](https://www.wowhead.com/forever/item=16800) · *Lucifron, Molten Core*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Maiden's Circle](https://www.wowhead.com/forever/item=13001) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVV1IW2cYzvudY/Lm82fZ56bHM4UzhyMLy/iSk4h6YRJ3M3Cgg12MXWwm5mQ5wyVZkgsHu1BxY3hhhgyGY7tQGLWlVqkU1CsbShslLd60gi1tsRS9KNT+IJTelHOi5qJeNtLn5nzneZ/D+z3PeeGlNQgOkEABJ3BgTcdvhEMHBKEfvoEUjADIOYroQPlnasOX8yA9rKYi7vwNVMT7z2qpgLvfUiuOxaUHddSG+f9Bul1HRdzLGYq7B7XUimsJ4ysbLp4HKWejAq5rVMSNGaACjmlUwD9/ojbcngGpUE9FXLlgFJ4OtX6K47qjoCtn/gXnjUngB5H+2SswAWRcnwJyEJmD3dAynJuDTZjUe2jZ0Cr5yM1Vv9/DOfeo3KOq3Ofm3O/nnKuqwaqcewsENkn1DvkLWYpp4dTQ98lUVvFyb7vbw90eX5cyGA8nftCiSjKthKNRLapEflGycU1JJ7PhrJ5MKBktnB6MK86MpimxdDKTjelpzZ0O61H3kcZd0nz2YyaZ+ES2yVVUwInv2K+vd+TtlehYT+0XwUpF/G9Vko3n461e1iortMH1HgKz583ikxXJuBkF1dS8mIKTMuH+ymWy1ccuwWmF8iX9nIWofUM0zC4sAfXJXjMQ4SiQhSUoBeKnkqsBRWZfPeZttIoKHn/GEOC9PtYsy/Rd1zsoMhKxlKodvM2oOgrdLHVapswcHde6mSiTLgv7/aQ0OyvRuMV0L5Tdq7xNRmp1ElzL97IW+QNTYC0LPLzNnLPL+V72fnlEn28Tkx69Cix9WrHZjSs5CeaA2Q9ncbxREvZIAfaJd1SwmPAFZ43/TwlC61nBblCWkViw6Z9pA+uBD2MmbgW8+0QSlYCrQCxvFbLBo1NF8fH8G+/Teb1YLNYMLAZDh0RwAP4AmAY9uf/b+tc3A50ma9kMhAxlsfgo8FXpcCfgEnC5sae5vBpK2+0Lc7/FIQXDMMxeDQAMoZ4u); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVU9ME1kY7/dmoK8Plu0+dmGYhWSWDZtus9286bQEONCWvWzCJrDJHvaktHRqxyBt2sZg4gFCMYYDGP4c8E9iSIxoohiJBjhhNVq0KhclURONxujBRPwTohdj5hXoQY6W+B3aN7/fb/K932++5CPlGOwggQIOYEBrtp4QgybwQyf8D3HoB5AnCMZ2LO8nVnxsEKTnZUTEn8aAiPjJu++IiC8PAbHi5UmQnlUQK86cAulhBRHxB65ZmjTZ8TR/0YpPDoI0aiUivjVpslfPAxHwkX1ExOlxU3h3CKRsJRHxAmfe9tT/gdOGPWsop4+D484IsPVQ5/Q1GAaUNsYArYdm4EVgHs7OwAqMGG2k4GoR/epSNa+XMcZUjamaxjwuxjigaar5y5g7i2AFlT1FE5jGqR6M9+yOxVOKm7kbXSpzqZ4WpTsa7N2jh5VYQgmGw3pYCR1QUlFdScRSwZQR61WSejDRHVUcSV1XIolYMhUxErorETTCrk2NK6/5c28y1vu7bJVLiICHd9GDX3ZkjcXoWElsF6GUiPjEoiSb/69X22m9rJAq548YqC3DyTcLknkzAhrXfByD7TJh3uJlstpBL8FOhfIP+YsGiO2maJqdnQPikd08EGEzkNk5yAfiJZKzCovUtriFW0kJEVRv0hTgxx20VpbJD87vsUhRyJJnm1iDydqzrTS+U6Z4jvYbrVSUUYuFHtouzeZiNK7j7oWCe401yJiUOhBeyrTTOvlnLigtCFTWwOfsSqad/lQY0fcPEIcHrgNN7FRsNvNKDoRHgdo2ZjFdLQkvURbWkHtAsPDy+KfN708Qhvozgs2ELP0Rf83RKbOWfb9EeN33udeQJCo+ZxZZvqlK+TdPRa3fzn31Ps23c7lcedcFf2AD8HfBYYApMGJrQ8v/3fM1c9Sy4guYylzule/f/OGRzyng+eq22sJqyK+4v/mSi0Ic+qCPfh4ASgSdtg==).

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 764 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-1355100013013303-2135000301113002-7)
- [Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md) (6/32/13, 760 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0042-20552030130115031-20350003-7)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (5/33/13, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0041-23251030130135031-20350003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

