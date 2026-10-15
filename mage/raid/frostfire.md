# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-0355100013013304-00550003310003002-6)

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Ice Lance** when Fingers of Frost is active
2. **Pyroblast** when Heating Up has 3 stacks
3. **Fire Blast**
4. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 15 seconds left
5. **Frostfire Bolt** when your mana is below 30%
6. **Frostfire Bolt** when you have at least 10% mana
7. **Fireball**

**Fireball** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Wake of Fire**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest gain of the rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5; the line above shows only the stack count.
- **Frostfire Bolt** is the filler: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the list casts Rank 2 instead (285 mana against 370): it is learned at level 50, close enough to 60 that the low-rank penalty the simulator assumes leaves its spell power alone, and the simulator measured this about 2% better than the old rule of stopping at 10% mana.
- The Rank 2 **Fireball** at the bottom of the list only matters when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only a small part of your spell power and fewer talent procs; with that penalty in, the simulator measured dropping the old Fireball fallback 1.0% better, so keep your mana up with gems and a potion instead.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds part of every crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a Rank 2 **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 675 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 622 | this build |
| Phase 1 BiS | 689 | [0/29/22](https://talentsforever.com/mage/60/-1355000013013304-00550003310003002-6) (ties this build) |

**The gear** (average item level: Pre-BiS 60.4; Phase 1 BiS 67.4; each item opens its Wowhead page, with where it drops and its enchant):

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
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Maiden's Circle](https://www.wowhead.com/forever/item=13001) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Searing Golden Blade](https://www.wowhead.com/forever/item=12260) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVV1IW2cYzvudY/Lm82fZ56bHM4UzhyMLy/iSk4h6YRJ3M3Cgg12MXUwTc7Kc4ZKQ5MLBLlTcGF7okMGwtBcVSm2pVSoF9cqG0kZJizet0Ja22Ba9KNT+IJTelHOi5qJeNtLnIvnO8z6H93ue88JLqxAcIIECTuDAGg6fCIc2CEIv/AQpGAaQJyiiA+UUteGbOZCeVFIRt/4HKuLDl9VUwO2fqRVH49KjGmrD3BmQ7tZQEXcmDcX9vWpqxdWE8ZYNFy6ANGmjIq6fBirgmkYFHDV+/v2dWvFxn5SvpSIuXzSKLwabv8Yx3ZHXlbMnwXlzAvhepHfmKowDGdOngOxFZmE7tATnZ2EDJvQuWvKzQr5wc9Xv93DOPSr3qCr3uTn3+znnqmqwKufePIENUrlF/kOWYlo4NdiXTGUVL/e2uj3c7fF1KAPxcOJXLaok00o4GtWiSuQPJRvXlHQyG87qyYSS0cLpgbjizGiaEksnM9mYntbc6bAedR9o3EXNN79lkomvZJtcQQUc/4X9+W5H3lqOjrXUfgmsVMRTK5Js/D/b7GbNskLrXJ8gMHvOLD5floybUVBNzespOCoT7i9fJps97DIcVyjf029ZiNrXRcPs/CJQn+w1AxEOAplfhGIgfiq56lBk9pVD3kYrqODxZwwBPuhhjbJMP3Z9hCIjEUux2sZbjKoj38lSx2XKzNFxvZOJMumwsL+PSrO9HI2bTPdCyb3KW2SkVifB1Vw3a5I/MwXWksDDW8w5u5LrZp+WRvTVHWLSI9eApY8rNrtxJSfBSWD2/Vkcq5eEHZKHXeIdESwmfMEZ4/tTgtB8TrAblGU4Fmw4MW1gLfB5zMTtgHeXSKIScOWJ5YNCNnhwKiu+nHvvfdpvFAqFqv6FYGifCPbDPwDToCd3/1r78Vag3WQtG4GQoSwUngZ+KB7uBVwCLtV3NZZWQ3G5fWeutzikYAiG2NsBAGfqnfI=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVU9ME1kY7/dmoK8Plu0+dmGYhWSWDZtus9286bQEONCWvWzCJrDJHvaktHRqxyBt2sZg4gFCMYYDGP4c8E9iSIxoohiJBjhhNVq0KhclURONxujBRPwTohdj5hXoQY6W+B3aN7/fb/K932++5CPlGOwggQIOYEBrtp4QgybwQyf8D3HoB5AnCMZ2LO8nVnxsEKTnZUTEn8aAiPjJu++IiC8PAbHi5UmQnlUQK86cAulhBRHxB65ZmjTZ8TR/0YpPDoI0aiUivjVpslfPAxHwkX1ExOlxU3h3CKRsJRHxAmfe9tT/gdOGPWsop4+D484IsPVQ5/Q1GAaUNsYArYdm4EVgHs7OwAqMGG2k4GoR/epSNa+XMcZUjamaxjwuxjigaar5y5g7i2AFlT1FE5jGqR6M9+yOxVOKm7kbXSpzqZ4WpTsa7N2jh5VYQgmGw3pYCR1QUlFdScRSwZQR61WSejDRHVUcSV1XIolYMhUxErorETTCrk2NK6/5c28y1vu7bJVLiICHd9GDX3ZkjcXoWElsF6GUiPjEoiSb/69X22m9rJAq548YqC3DyTcLknkzAhrXfByD7TJh3uJlstpBL8FOhfIP+YsGiO2maJqdnQPikd08EGEzkNk5yAfiJZKzCovUtriFW0kJEVRv0hTgxx20VpbJD87vsUhRyJJnm1iDydqzrTS+U6Z4jvYbrVSUUYuFHtouzeZiNK7j7oWCe401yJiUOhBeyrTTOvlnLigtCFTWwOfsSqad/lQY0fcPEIcHrgNN7FRsNvNKDoRHgdo2ZjFdLQkvURbWkHtAsPDy+KfN708Qhvozgs2ELP0Rf83RKbOWfb9EeN33udeQJCo+ZxZZvqlK+TdPRa3fzn31Ps23c7lcedcFf2AD8HfBYYApMGJrQ8v/3fM1c9Sy4guYylzule/f/OGRzyng+eq22sJqyK+4v/mSi0Ic+qCPfh4ASgSdtg==).

## Other builds of this spec

- [Frostfire — Frostfire Bolt / Hot Streak](../research/raid/builds/frostfire-raid.md) (4/31/16, 630 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/004-03251030130133051-005500033-6)
- [Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md) (4/31/16, 597 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/004-10452131130103051-005500033-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

