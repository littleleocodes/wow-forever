# Arcane Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane

**[Arcane — Raid](../research/raid/builds/arcane-open-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/mage/60/023205203100211531-554000011001-003-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Arcane — Arcane Blast), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Wrath** until the last 10 seconds of the fight
3. **Arcane Blast**: keep it on the target
4. **Pyroblast** when Heating Up has 3 stacks
5. **Fire Blast**
6. **Arcane Blast** when you have at least 25% mana
7. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Arcane Power**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run out of mana (needed in about 9 of 10 fights)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arcane in a raid builds **Arcane Blast** stacks and spends them. Each **Arcane Blast** makes your next other spell stronger and the next **Arcane Blast** much dearer, so free **Arcane Missiles** from **Missile Barrage** and a **Fire Blast** every 6 seconds spend the stacks before the cost runs away.

**Why it works**

- **Arcane Blast** is the filler: a 2.5-second cast that adds a stack each time (up to 4, for 8 seconds). Each stack adds 10% to the damage of your other spells (15% to **Arcane Missiles**, fitted to beta logs) and 175% to the next **Arcane Blast**'s mana cost; casting any other damage spell spends them all.
- **Arcane Missiles** on **Missile Barrage** comes first. Each **Arcane Blast** that lands has a 40% chance to make your next Missiles free and twice as fast, and the Missiles spend your stacks at 15% each: about a third of your damage in the simulator.
- **Fire Blast** whenever it is ready is why this Arcane build spends 11 points in Fire: **Improved Fire Blast** brings it back every 6 seconds and **Incineration** adds crit. It is instant, it takes your stacks' bonus, and it puts **Arcane Blast** back to its base cost. Adding it was the biggest gain of the rotation search, about 8% over three steps.
- **Arcane Power** and **Presence of Mind** go at the pull: 30% more damage for 15 seconds (at 30% more mana cost) and one instant spell. Both have 3-minute cooldowns, so a 3-minute fight gets one of each.
- Mana: **Evocation** only below 15% mana with more than 20 seconds left. With a raid's mana buffs, your mana gems and a mana potion, the simulator almost never needed it.

**Caveats**

- Without a raid's mana buffs you run dry sooner. The simulator's list for playing without them also spends two stacks on a **Frostbolt** when **Fire Blast** is not ready, which keeps **Arcane Blast** cheap.
- Moving: **Arcane Blast** and **Arcane Missiles** both need you to stand. **Fire Blast** is your instant, and **Presence of Mind** makes one **Arcane Blast** instant.
- Threat: **Arcane Subtlety** cuts your Arcane threat by 30%, but the simulator ignores threat, and **Arcane Power** at the pull is when you are most likely to pull the boss.
- Several targets: this list is for one boss. **Arcane Explosion** hits everything within 10 yards.

**When to change it**

- In the last 40 seconds, stop resetting with **Fire Blast** and keep casting **Arcane Blast**. Its cost climbs, but mana left when the boss dies is wasted and your free Missiles spend bigger stacks; the simulator measured these end-of-fight rules about 1% better together.
- In the last 3 seconds an **Arcane Blast** cannot finish: cast the **Fire Blast** you saved.
- In a fight longer than 3 minutes, use **Arcane Power** and **Presence of Mind** again when they are back, and channel **Evocation** below 15% mana while more than 20 seconds remain.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 756 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 5ad0894 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 1000 | [32/16/3](https://talentsforever.com/mage/60/023205203100311531-553000011001-003-7) |
| Phase 1 BiS | 1003 | [32/16/3](https://talentsforever.com/mage/60/131205203100311531-553000011001-003-7) (ties this build) |

**The gear** (average item level: Pre-BiS 78.8; Phase 1 BiS 78.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Frostfire Circlet](https://www.wowhead.com/forever/item=22498) · *quest: Frostfire Circlet*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Frostfire Circlet](https://www.wowhead.com/forever/item=22498) · *quest: Frostfire Circlet*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Charm of the Shifting Sands](https://www.wowhead.com/forever/item=21504) · *quest: The Fall of Ossirian* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Frostfire Shoulderpads](https://www.wowhead.com/forever/item=22499) · *quest: Frostfire Shoulderpads* | [Frostfire Shoulderpads](https://www.wowhead.com/forever/item=22499) · *quest: Frostfire Shoulderpads* |
| Back | [Drape of Vaulted Secrets](https://www.wowhead.com/forever/item=21415) · *quest: Drape of Vaulted Secrets* | [Drape of Vaulted Secrets](https://www.wowhead.com/forever/item=21415) · *quest: Drape of Vaulted Secrets* |
| Chest | [Frostfire Robe](https://www.wowhead.com/forever/item=22496) · *quest: Frostfire Robe*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Frostfire Robe](https://www.wowhead.com/forever/item=22496) · *quest: Frostfire Robe*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Frostfire Bindings](https://www.wowhead.com/forever/item=22503) · *quest: Frostfire Bindings*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Frostfire Bindings](https://www.wowhead.com/forever/item=22503) · *quest: Frostfire Bindings*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Frostfire Gloves](https://www.wowhead.com/forever/item=22501) · *quest: Frostfire Gloves* | [Frostfire Gloves](https://www.wowhead.com/forever/item=22501) · *quest: Frostfire Gloves* |
| Waist | [Frostfire Belt](https://www.wowhead.com/forever/item=22502) · *quest: Frostfire Belt* | [Frostfire Belt](https://www.wowhead.com/forever/item=22502) · *quest: Frostfire Belt* |
| Legs | [Frostfire Leggings](https://www.wowhead.com/forever/item=22497) · *quest: Frostfire Leggings*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Frostfire Leggings](https://www.wowhead.com/forever/item=22497) · *quest: Frostfire Leggings*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Enigma Boots](https://www.wowhead.com/forever/item=21344) · *quest: Enigma Boots*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Enigma Boots](https://www.wowhead.com/forever/item=21344) · *quest: Enigma Boots*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* | [Ring of the Fallen God](https://www.wowhead.com/forever/item=21709) · *quest: The Savior of Kalimdor* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Trinket | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) · *quest: Epic Armaments of Battle - Friend of the Dawn* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Blade of Vaulted Secrets](https://www.wowhead.com/forever/item=21413) · *quest: Blade of Vaulted Secrets*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Blade of Vaulted Secrets](https://www.wowhead.com/forever/item=21413) · *quest: Blade of Vaulted Secrets*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* | [Master Dragonslayer's Orb](https://www.wowhead.com/forever/item=19366) · *quest: The Lord of Blackrock* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1sUxntuh87tKQ/67iPvzZv3FvN4jwf0vZo7M5QgmxY2/lvQ6MadTGmxNdg2bRe4q4aFkggJMSgNC0OEgtE0ujBAwsZVXWjYqAluKoi4VBeoG2NmaJEoMS6gfotz75wvk/nNuffk4J8U3CCBAi3QC1FIQhbgIsB1gFkAVmu5xHQ7QB6tpdRN5UEU6WoBpHUXCjQ7CyjQtYIZ83lAkZYKIK3VoUg3CiA9q0OBrlvuy4LpPt96UaSlGZBGRRTowznTXZk24/gdM95bdqNIp/MgFX9Bgc5cNZNzk/WN/7uLsZZHI8A3Q8HLUzAMZCg2BmQzlAOy0XUTaH4Sbg3DSKwEQ7FuasFDABbJ31zTNe7TuK5yrquqT1e9Pp/OOeeqyrnq5VwvElgmrlUyikyQSaeNNcgMnXfBYTIuSHIN2umLHpYFZhjJgVOJZEbRuNbuVblXa+tU+qJG/HQkrCRSihEOR8JK6JySiUaUVCJjZGKJuJKOGKm+qNKSjkQUI9VnxCPecDLtrfjeLf/AmXQi3ir/gT976qmDkaM2WcQatKs8LZskF94HWa4qCD78T25F14qDokCXFiQJUPZI1M6ci1ZNlhYk2Zkj5vbK42NyeWWXdoHT1b2G++e7WOarwnICj7BD2C63fYsJf/U0UIE57297NWhH0PCnRhc638KX6Neqgq5jK2u20KCC9qaCpu9E+zAGcnllA1+T8Y69JhNNCPq0h41X5bKr2Mya0O2pK/ecAwUkerrShaFyF2q+pu0Tcn5m3KUimr4/Fcn3sLPVKAi1/nPjXVCyvyJFeE2083abpbbAlHlbkVBo/EicZsqW7Q/8npsw9cD/V7+lJ36tRCRB8Xvmie2HKBOo7PZV/97et+8ctOLxG4GuciLQaw7nCbAebCW/x07nf+veMcM5dEAADkMQTkIUkjAIg+TTACDB2Go=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1sUxntuh/b2lAd995H35s17i3m8xwP6Xs2dGUqQTQsb/y1odONOprTYGmybtgvcoWGhJEKCBqVhYYhSMZpGV0DCxlVdaNioiW4qiLhUF6gbYu7QIlFiXED9FueeOd9M5jdn7snFPyl4QAYVWqAXYpCCIYDzANcAbgKwWsslwu0AZayWUg9VBtFJlwsgr7pRohvjgBJdKYiYzwM6aakA8kodOulaAeTndSjRVct9VRDui80HnbQ0A/KYEyX6cFa4E0seEe+KfPiSuPNGHuTiLyjRmSuiODtV3/i/pxhveTQKfD0cujgNI0CG4+NA1sM5IGtdt4Dmp+D2CIzGSzAc76YWPARhgfytGZrO/To3NM4NTfMbms/vNzjnXNM413ycG0UCS8S9TMaQSQrptLEGhaHrHjgE47ys1KCdvuxhQ8BMMzVwIpnKqjrX230a9+ltnWpfzEycjEbUZFo1I5FoRA2fUbOxqJpOZs1sPJlQM1Ez3RdTWzLRqGqm+8xE1BdJZXwV37fp7zuVSSZalT/wZ289dTBy2KY4sQbtGs8oguTchxDLVQXBj/8preh+5qAo0cV5WQZUvDK1M9eC1ZPFeVlx5YhILz8+opRXdmEHOEPbbbh/votlriosx/AQO4DtStu3mPBXbwOVmOv+lleDdgQdf2p0o+sdfIl+tSroBrayZgsNKmhvK2jGdrSP46CUVzbwNRnv2G0yp4CgT3vYRFU2u4bNrAk93rryzDlQQmJkKlMYLk+h7m/a+kOuz4w7dEQ39qYj+R52uhoNodZ3rr0PyfbXpAhviH7WbrPUFpwWuxUJhcYN4hIl21B/8PfcpNCDwF/9lp4E9BKRJTXgnSO2H6JssJLtqf69s2fv2W/Fo9eDXeVCsFcczpNgXdhKAa+dzv3Wve0M59ABQTgIITgOMUjBIAySTwMAWKXYSg==).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (31/13/7, 683 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/050205203100301531-505001002-043-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 5ad0894 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

