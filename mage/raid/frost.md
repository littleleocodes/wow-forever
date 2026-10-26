# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**[Frost — Raid](../research/raid/builds/frost-ml-raid.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/mage/60/0531005003000301--05350003012130025-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Frost — Winter's Chill), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Ice Lance** when Fingers of Frost is active
3. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**
- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid is a **Frostbolt** caster that cashes in two procs: free **Arcane Missiles** from **Missile Barrage** and instant **Ice Lance** casts on **Fingers of Frost**. One **Fire Blast** in the last seconds of the fight uses time no **Frostbolt** can fill.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** comes first. Each **Frostbolt** that lands has a 20% chance to make your next Missiles free and twice as fast (the full damage in 2.5 seconds), and they are about a fifth of your damage in the simulator.
- **Ice Lance** on **Fingers of Frost** comes next. Each **Frostbolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit chance, so spend both charges on **Ice Lance**. With both procs up, the simulator measured the free Missiles first slightly better (0.2%).
- **Frostbolt** fills everything else: 2.5 seconds with **Improved Frostbolt**, and the spell that rolls for both procs. **Winter's Chill** needs no button: in Forever it is your own debuff, each Frost hit adds a stack (+2% crit to your **Frostbolt** and **Ice Lance**, up to 5), and steady casting keeps it full.
- **Fire Blast** waits for the last 3 seconds. A **Frostbolt** started then would still be casting or in flight when the boss dies, while **Fire Blast** is instant; the simulator measured this 0.5% better. The rotation search kept it out of the rest of the fight: no Frost talent improves it, it costs more mana than a **Frostbolt** (340 against 290) and it rolls for neither proc.
- **Presence of Mind** at the pull makes your next spell instant. Its cooldown is 3 minutes, so a 3-minute fight gets one; in a longer fight press it again when it is back.
- Mana: the list uses your mana gem (from **Conjure Mana Ruby**) as soon as you are down to 80% mana, and **Evocation** only below 20% mana with more than 25 seconds left. With a raid's mana buffs the simulator never needed **Evocation** in a 3-minute fight.

**Caveats**

- Several targets: this list is for one boss, and the simulator's raid fights are single-target. For packs, **Blizzard**, **Cone of Cold** and **Arcane Explosion** are your area spells.
- Moving: **Frostbolt** needs you to stand still. **Ice Lance** and **Fire Blast** are instant, and **Presence of Mind** makes one **Frostbolt** instant.
- Threat: the simulator ignores it. On a fresh pull, give the tank a few seconds before your opener.

**When to change it**

- In the last 3 seconds, cast **Fire Blast** instead of starting a **Frostbolt** (the Advanced line above).
- Without a paladin's or shaman's mana buffs you run dry sooner: below 20% mana with more than 25 seconds to go, channel **Evocation**. Any later and the mana comes back too late to spend.
- If you must move while **Fingers of Frost** is up, spend the charges on **Ice Lance** as you go: it is instant.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 544 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 579 | [21/0/30](https://talentsforever.com/mage/60/05212050031001001--25353000110030124-7) |
| Phase 1 BiS | 594 | [21/0/30](https://talentsforever.com/mage/60/05212050031001001--05353002110030124-7) |

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 64.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV1oHFUUx/fcmezePS3Jeqt1es3DbTElLh25M5staR7MJE9qkASfxAft3d1JdiTMLDOTfrxILBUkYAtalMYIWgx+1Q/6IO2CLwFhLSh50Yp9CdWi+FJBKL4ocmd3TaGvNh6Gy7nnf//M75wZZnCYQgksEDAKR6EJLVgGeAXgHYAPANjuTCVaHQd+nVJaovwYFmj7FFg3d6FJb7wJaNLfzun1rc0S5mkntH4axALdWAfr+iAadCNEk948C1ign3VtBfr5RbDOFtCkP65r59V39frFZglN+tfaEBborU/B6uxBk/7xhpY+XBs6cKjUCUa/PQPydm3u1QuwAuR08BqQ27VVIL9MfQT0/TW4uAJngi04HUzv3m7MgzZ5WFZdx5VVKSuOlPqybbdaqVaklI4jZUU67liHwCbZdYP8kGcfA3sZVKPhN4Qr3cO2PGK74xNiKq6r0BdPBUkSLPqJiEKh+jsxreJYLfiiFUf1Q2JhScXaXjsp1FKsnkhmwuh4KJJIKFFbChYb4niQNqOl9C5/6B/zY1FXSZqIIOX70WJ7sXjVzKNJv7liYfES9FI+gAb9eZatA1Oqtfh81Eq7uI603cqEqDdVuOA3RBSLbi+1kyJt+iKOUpUGUSgSX8X1phhNfF/Mx1GS2rEKGnZft7v6oy8kUfgI9/AwH0NetqjBiu2M4csrFi+uEp2e+24G95bv19rGv9oAGggu7+lsmHO8rzxETUZqOV7AATTG5YjuotR5jJmcTORYhTs4yg5m54ztc64cyUoDjDzZL1UTbaWvP8eWd2QAD2UE+TsIZJL1durPOfYA39N/Mm+3rax869oMe/FuMOn+12D7sFQe7IHl0URS6U7mq1m2AjsBMILDZa4Bns1xdokMUWN7SI4jM5hrs5bxK+nA78R9ychlMeZd0K8KEgoH/iZFXcotz3v7Vs/r+Hpy/3wW30+6W8QyxWT5Msn9L5F6/eyexsFP7tl9jmTr0+95U72Cd1R/6M9DtsltTZYNevnB6Tv+BxLGwYPHYQ6egSa04AScIP8MABKIR/8=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV1oHFUUx/fcmd29e1uS9Vbr9JqH22LKunTkzmy2bPPgTvKkBknwSXzQ3t2dZEfCzDIz248XiSWCBGyhrUJjBSkGv+oHfZB2wZeAsCpKXrRiX4JaFF8iCMGnIHd21wTyauJhONz7/9/D/M6ZYYaMYMiDARwKcBqa0IIFgNcA3gF4H4AeTFyk3AqwexjjPGZnSBZ3LoBx/wDR8dZlIDr+46rKb63lSQZ3feOXIZLFqytg3BsiGl71iY7vXwKSxZ/2yrL4s5tgXMoSHf+0oiq/eUPlxSsqf76WJ1m88QkY3UNEx3+9qcQPrg8fO5HveoXvLoLYrM28fgOWAC16lwFt1pYB/TbxIeD3rsPNJbjorcOiN3lwuzEHOuhRUbYtW5SFKFlCqMs0RblULglhW5YQJWHZY10Ea+jAz+jHDP0I6KsgGw23wW1hnzTFKdOujPOJsC59lz/jRZE370Y88Lkc7PikDEM55/JWGNRP8Lm2DFV57TyX7VA+FU35wVmfRwGXvNb25hv8rBc3g3a8q953z7ghr8sojrgXs6PEoIdJ7ms9Q3T87R2D5G5Bf8nSRMO/TtMVoFK25l8MWnEP1xKmXRrn9ab059wGD0Le66V2nsdNl4dBLGMv8HnkyrDe5IXIdflsGESxGUqvYQ58s+c//lIU+I8xh5xkY4QVDazRXCdh+OKOwXLLSC2vfj9FDhcfVN7qv16aaARs1vfpCGPkgeIw1imqpViWpIlWEaOqi3z3CaozNJ6iJWaRAj2enNO2z9liNJHSFD09kMqRKsVXXqAL+zKARxKCzA4CESW9Xfh7hj7EDg2ezNsdI5E37k7Rl3eDCfu/BjtC8sWhPliG6ASVepP5cpouwX4AjJKRIlMAz6cYvYWGsbY9JMsSCczdaUP7HXXhT2S/oqWSGHNuqFeFIAzHtlBOSamFWefI8jUVX1WPzibxQ9VeR4bOq8XbKPW/ROwMVnsaxz/es/ucSvKz7zoTfcE5rT701yDZpNarRQ3ffnhyx/9AQAUceBJm4DloQgvOwTn0zwAxdUd7).

## Other builds of this spec

- [Frost — Winter's Chill](../research/raid/builds/frost-winters-chill-raid.md) (21/0/30, 501 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0541005003000201--25353003002100105-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

