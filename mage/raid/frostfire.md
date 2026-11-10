# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 10 seconds left and the target has fewer than 4 stacks of Fire Vulnerability
2. **Pyroblast** when Heating Up has 3 stacks
3. **Fire Blast** when the target has fewer than 2 stacks of Fingers of Frost
4. **Frostfire Bolt**

**Frostfire Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Scorch**: in the last 3 seconds of the fight, when there is no time left for another **Frostfire Bolt**
- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire list whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost, so both trees' talents apply, its chill rolls **Fingers of Frost**, and its crits stack **Heating Up** for a 1.5-second **Pyroblast**. **Scorch** keeps Fire Vulnerability at 5 stacks and **Fire Blast** fills between casts. **Ice Lance** is in the build only because **Fingers of Frost** requires it: the list never casts it. 759 DPS in a full raid, 8% behind the Fire page.

**Why it works**

- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds, and **Frostfire Bolt** counts as Fire) and refreshes it under 10 seconds left, a wider margin than the Fire list's 5 (+2.2% in the search), between casts unless the stacks are under 4. About 14 casts and 7% of the damage. Trinkets and the other cooldowns wait for the fifth stack.
- **Pyroblast** at 3 stacks of **Heating Up** (12 casts, 22%, and most of **Ignite**'s 13%): crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** cut its cast by 25% each and **Fire Blast** adds a stack on every hit. One hard cast before the pull.
- **Fire Blast** (21 casts, 17%) every 6 seconds with **Improved Fire Blast**, but only while fewer than 2 **Fingers of Frost** charges are up. A proc treats your next 2 spells as cast on a frozen target, where **Shatter** adds 50% crit chance: the list spends both charges on **Frostfire Bolt**, whose crit starts **Ignite** and a **Heating Up** stack, and holds **Fire Blast** until a charge is gone.
- **Frostfire Bolt** fills everything else (40 casts, 41%): 2.5 seconds with **Accelerant**, 370 mana less **Frost Channeling**'s 15%, a 40% slow, **Ice Shards**' doubled crit bonus and **Critical Mass**'s 6% crit, and one cast rolls for **Fingers of Frost**, **Heating Up**, **Ignite** and **Master of Elements**' refund at once. It is checked against the lower of the target's Fire and Frost resistance.
- **Ice Lance** has no line: on the same **Fingers of Frost** charge a **Frostfire Bolt** is worth more than its 136-160 damage, and the search dropped the **Ice Lance** line in its last passes. The talent is the one point **Fingers of Frost** requires.
- **Fire Power** adds 3% Fire damage per Fire effect of yours on the target, up to 12%: Fire Vulnerability, **Ignite** and **Pyroblast**'s burn count; **Frostfire Bolt**'s own burn, a mixed school, does not.
- Mana: your mana gem (from **Conjure Mana Citrine**) whenever it is ready, two mana potions, a Demonic Rune, **Master of Elements**, and **Evocation** once a fight (an 8-minute cooldown). In a 6-minute fight the simulator's DPS falls to 306: this list is the mage's most front-loaded.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not spend one on a **Scorch** refresh if a **Frostfire Bolt** fits.
- Moving: **Fire Blast** and the 1.5-second **Scorch**. For packs, **Flamestrike** and **Blizzard**.
- **Frostfire Bolt** is new in Forever: its numbers are the simulator's model of the tooltip, not checked in game.
- The simulator's boss resists nothing. Against Fire resistance **Frostfire Bolt** keeps working (the lower of the two resistances), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

**When to change it**

- In the last 3 seconds, **Scorch** instead of starting a **Frostfire Bolt**.
- Out of mana with the fight going on: **Evocation** if it is back, else **Scorch** (150 mana) keeps the stacks and **Heating Up** moving until a gem or potion returns.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Fire | 29 | Accelerant 5, Incineration 3, Ignite 5, Improved Fire Blast 2, Pyroblast 1, Heating Up 1, Improved Scorch 3, Master of Elements 3, Critical Mass 3, Fire Power 3 |
| Frost | 22 | Frost Warding 2, Improved Frostbolt 1, Precision 3, Ice Shards 5, Frost Channeling 3, Ice Lance 1, Arctic Reach 1, Ice Block 1, Shatter 3, Fingers of Frost 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 785 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) |
| Phase 1 BiS | 842 | [0/29/22](https://talentsforever.com/mage/60/-4550000123012303-2135000301113002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.2; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Red Mageweave Headband](https://www.wowhead.com/forever/item=10033) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Red Mageweave Headband](https://www.wowhead.com/forever/item=10033) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Cindercloth Pants](https://www.wowhead.com/forever/item=14045) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Truesilver Conduit](https://www.wowhead.com/forever/item=249455) · *Enchanting* | [Truesilver Conduit](https://www.wowhead.com/forever/item=249455) · *Enchanting* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG8UX95vdxuOXNHGm/3/ZbnOYGkKSTZzsR1IlQSJuJUQphVScEAfo2rsbLzhey7up2luBHlAlElEqqoQgQQSCovJVJNTkgvAFwwFFHOCAUKKgCoSQSnKoxAWhWSdtuPTWcMiTvDPz3vzem/m955nBDgppUIBDN5yCIlTgHMArAG8DfADAWmIrEdZhUGfaKU1TNcIm+tmTyo1mlOnaZUCZ/n5JfN9cTmMTrZeVX1oxSWvvgfJTK0q0VkaZ3pgBbKI/TwpUkn56FZSZJMp0+o80yvTbdwT8i2XRf+3LNCbpzY9Bqe9Dmd6cb0OZXplvy/Sl6373d9Og38qffHUBLgA5718Ecis/B+TXIx8CfX8erl6AaX8VzvtHabxwyMESyWQHh4Z0XdcN04p/VtY0LKGxdMMwLF036wSWSfMaudSGDyBVm1Cmf12EjHKN/J9KLDVHNjXCgiRrsApz7UrpuaAScVM3D2cNPWsZo7xQtMsTrsODKrcdx3V4/iyPii6vBpEd+UGZh65dLRR5d+i63KsGYeT5VTdbtX0nuzUn25jT/3wYlHvUpLoHpfTXD7NZwtZheyzhN/A8v+DbJR76k1MlOwqqXSGftCfcAacSDtiVUjjgefl+u1KK3XE74kODBdcuHLaGue0Elch1ePftyCV7gttTjh9x24vcamPpbrbil0d5r9mvd3IvaGjdclQ92xXyvBtGPD/llxzul7nNvalSiYvt9PFeo9/o5FEgkGYD6UchL/mhCBpjwj5u6H26rnPPnyhGIY8Zcp2Qm9wuO9zqUe/HfVo7lRh5JqGmNqTNPKxBM6YeOR0UYlbZCuxUOk7jJHsBH1JHUNUUKrG9NUCU6SefAyNpInKFMIQHtQPCtvQvW1w6ho59qnYX8CC2ZBDpBuxBia6MC490ZZy9sTuzz7FDUymwthq03GFKgU2iRxPsyu4kxsIe1oX7tf9RYKkaiL/F+qLSoMXCvZlmTG3AtkNLtOzy7uTqECrafiqx5hpQlOlbS8pWAZmioT+Os5d37ABRMa210iZGjidEXpBYoWjpV7XHd/hSoSvjiqQtwPaD9DH1UexgaqOArsUFtFR/AlPfy6K7uH7C7Nq8HhfXT+DBl0BBib7+rNqutYk95RNqEvegNDLSyY6rx7BX7Wm4uo1vDBdga3gnyF18/Ubq8CcxX5QSsQzmYjwSCpm/SUqoEue83IG5WSHfjB3yYvlhzFwliszHtOsk8Z9IlNvq3VN58KN7Fmck/j71bu7IpiJ3SjwOZyEeJFbHNIlev+/otjekDsOQg2NwEp6GIlTgDJwh/wwALReGqQ==); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkVk1sG8UX95vdxuOXNHGm/3/ZbnOYGkKSTZzsR1IlQSJuJUQphVScEAfo2rsbLzhey7up2luBHFAlWpS2oIQgoQgEReWrSKjJDV8wQkIRBzgglKioAnEpyaESlwrNOknDpbeGQ57kmZ335vfezO89zwx2UEiDAhy64RQUoQLnAN4AeB/gYwDWEluJsA6D+lY7pWmqTmET/fJZ5VYzyvTuDKBM/7ws2neX09hE62Xlt1ZM0tqHoPzSihKtlVGmty4CJumvV0DAkvSLa6BcTKJMv78CW+3Xy2mU6fQlMfP2Z6DU96FMb8+3oUyvzrdl+tJ1v/uHC6DfyZ98cwHOA5n2Z4Dcyc8B+f3IJ0A/modr5+GCvwrT/lEarxxysEQy2cGhIV3XdcO04p+VNQ1LaCzdMAxL1806gWXSfJNcbsNHkKpNKNO/ZyCjXCf/pxJLzZENjbAgyRqswly7UnopqETc1M3DWUPPWsYoLxTt8oTr8KDKbcdxHZ4/y6Oiy6tBZEd+UOaha1cLRd4dui73qkEYeX7VzVZt38luzsk25vS/HAblHjWp7kEp/e3jbJawNdgeS/gNPM8v+HaJh/7kVMmOgmpXyCftCXfAqYQDdqUUDnhevt+ulGJ33I740GDBtQuHrWFuO0Elch3evRW5ZE9we8rxI257kVttLN3NVvzyKO81+/VO7gUNrVuOqme7Qp53w4jnp/ySw/0yt7k3VSpxsZ0+3mv0G508CgTSbCD9KOQlPxRBY0zYxw29T9d17vkTxSjkMUOuE3KT22WHWz3qw7hPa6cSIy8k1NS6tJGHm9CMqSdOB4WYVbYCO5WO0zjJXsHH1BFUNYVKbG8NEGX6+VfASJqIXCEM4UHtgLAt/csWl46hY5+q3Qc8iC0ZRLoOe1CiK+PCI10ZZ2/vzuxz7NBUCqytBi33mFJgg+jRBLu6O4mxsId14X7tfxRYqgbib7G2qDRosXBvphlT67Dt0BI9e2d3cnUIFW0/lVhzDSjK9L0lZbOATNHRn8fZ6zt2gKiY1lppEyPHEyIvSKxQ9PSb2tM7fKnQlXFF0hZg+0H6lPokdjC1UUDX4wJaqj+DqR9l8bm4dsLs2rgeF9dO4MHXQEGJXnpRbdfaxJ7yCTWJe1AaGelkx9Vj2Kv2NFxt4RvDBdgc3gtyH19/kDr8RcxXpUQsg7kYj4RC5i5JCVXinJc7MDcr5LuxQ14sP42Zq0SR+Zh2gyT+E4lym18PVB799IHFGYnb5z7IHdlQ5E6J1+EsxIPE6pgm0RsPHd32iNRhGHJwDE7C81CECpyBM+SfAQAepYZw).

**Points that do nothing for this spec:** **Improved Frostbolt** (1) only counts toward the points the tree needs before **Arctic Reach**, **Fingers of Frost**, **Ice Block** and **Shatter**; **Ice Block** (1) only counts toward the points the tree needs before **Fingers of Frost**.

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 776 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3551000113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 716 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

