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

Arcane in a raid keeps its own **Arcane Blast** buff stacked (each cast gives you 12% of your Intellect as spell damage for 18 seconds, up to 4 stacks, at a doubling mana cost), fires **Arcane Wrath** every 6 seconds and **Fire Blast** every 7, spends every **Missile Barrage** proc on a free, fast **Arcane Missiles**, and casts **Pyroblast** once three crits have made it a 1.5-second cast. It is the hungriest mage list: even with a raid's mana buffs the simulator needs **Evocation** in 9 fights of 10. 756 DPS in a full raid.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** first (30 casts, 29%): **Arcane Blast** procs it 40% of the time, **Arcane Wrath** 20%; the proc makes the next Missiles free, 2.5 seconds long and twice as dense. **Arcane Impact** adds 6% crit, **Arcane Mind** 10% Intellect and a doubled Arcane crit bonus, **Arcane Instability** 3% damage and crit. The list names rank 7, as the simulator's rotation does; a free cast costs the same at any rank.
- **Arcane Wrath** whenever it is ready (17 casts, 28%): 3 seconds with **Accelerant**, a 6-second cooldown, 406-496 damage plus 5% of your maximum mana as spell damage, and a proc roll. Moving it to the top of the list was the search's biggest single gain (+8.9%). Not in the last 10 seconds.
- **Arcane Blast** (37 casts, 22%): the page's line "keep it on the target" means keep the buff on yourself. Cast it when the buff is gone or about to expire and until it has 3 stacks (the full list's conditions), then only while you have more than 25% mana, because the cost doubles with every stack. 1.5 seconds a cast, 10% crit from **Incineration**, and each one rolls 40% for a **Missile Barrage**.
- **Fire Blast** on cooldown (14 casts, 10%): instant, every 7 seconds with one point of **Improved Fire Blast**, 10% crit from **Incineration**, and every hit adds a **Heating Up** stack.
- **Pyroblast** at 3 stacks of **Heating Up** (4 casts, 7%, plus **Ignite**'s 2%): crits from **Fire Blast** and **Fireball** cut its 6-second cast by 25% each, and **Fire Blast** adds a stack on every hit, so three stacks come about every 45 seconds and the cast takes 1.5 seconds. Never hard-cast it otherwise.
- **Arcane Power** and **Presence of Mind** at the pull: 30% more damage for 15 seconds at 30% more mana, and one instant **Arcane Wrath**; both have 3-minute cooldowns.
- Mana: **Evocation** when nearly dry (0.9 casts a fight in the simulator), a mana potion about every 2 minutes, your mana gem (from **Conjure Mana Ruby**) and a Demonic Rune; **Arcane Concentration** makes one cast in ten free, **Arcane Meditation** at 2 points keeps a third of your regeneration going. When nothing above is affordable, **Fireball** rank 11 fills, about once a fight.

**Caveats**

- A 6-minute fight is a different list: the simulator's DPS falls from 756 at 3 minutes to 412 at 6, because the mana runs out. Longer fights want fewer **Arcane Blast** stacks and an earlier **Evocation**.
- Moving: **Arcane Blast**, **Arcane Wrath** and **Arcane Missiles** all need you to stand. **Fire Blast** is your instant, and **Presence of Mind** makes one cast instant.
- Threat: **Arcane Subtlety** cuts Arcane threat by 30%, but the simulator ignores threat, and **Arcane Power** at the pull is when you are most likely to pull the boss.
- Several targets: **Arcane Explosion** hits everything within 10 yards; **Flamestrike** and **Blizzard** are the rest.

**When to change it**

- In the last 10 seconds no **Arcane Wrath**, in the last 3 no **Arcane Blast**: **Fire Blast**, and a free **Arcane Missiles** if you have one.
- Without a raid's mana buffs the simulator's list for playing alone spends two **Arcane Blast** stacks on a **Frostbolt** instead of a fourth cast and casts **Fire Blast** only on cooldown: cheaper and slower.
- In a fight longer than 3 minutes, use **Arcane Power** and **Presence of Mind** again when they are back, and channel **Evocation** below 15% mana while more than 20 seconds remain.

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

