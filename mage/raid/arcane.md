# Arcane Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane

**[Arcane — Raid](../research/raid/builds/arcane-open-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/mage/60/023205203100211531-554000011001-003-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Arcane — Arcane Blast), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Wrath** until the last 10 seconds of the fight
3. **Arcane Blast**: keep its buff stacked on you
4. **Pyroblast** when Heating Up has 3 stacks
5. **Fire Blast**
6. **Arcane Blast** when you have at least 25% mana
7. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Arcane Power**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run out of mana (needed in about 9 of 10 fights)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arcane in a raid keeps its own **Arcane Blast** buff stacked (each cast gives you 12% of your Intellect as spell damage for 18 seconds, up to 4 stacks, at a doubling mana cost), fires **Arcane Wrath** every 6 seconds and **Fire Blast** every 7, spends every **Missile Barrage** proc on a free, fast **Arcane Missiles**, and casts **Pyroblast** once three crits have made it a 1.5-second cast. It is the hungriest mage list: even with a raid's mana buffs the simulator needs **Evocation** in 9 fights of 10. 756 DPS in a full raid.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** first (about 15 casts, 29%): **Arcane Blast** procs it 40% of the time, **Arcane Wrath** 20%; the proc makes the next Missiles free, 2.5 seconds long and twice as dense. **Arcane Impact** adds 6% crit, **Arcane Mind** 10% Intellect and a doubled Arcane crit bonus, **Arcane Instability** 3% damage and crit. The list names rank 7, as the simulator's rotation does; a free cast costs the same at any rank.
- **Arcane Wrath** whenever it is ready (17 casts, 28%): 3 seconds with **Accelerant**, a 6-second cooldown, 406-496 damage plus 5% of your maximum mana as spell damage, and a proc roll. Moving it to the top of the list was the search's biggest single gain (+8.9%). Not in the last 10 seconds.
- **Arcane Blast** (37 casts, 22%): keep its buff stacked on you. Cast it when the buff is gone or about to expire and until it has 3 stacks (the full list's conditions), then only while you have more than 25% mana, because the cost doubles with every stack. 1.5 seconds a cast, 10% crit from **Incineration**, and each one rolls 40% for a **Missile Barrage**.
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

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 31 | Improved Channeling 2, Arcane Resilience 3, Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Impact 3, Arcane Blast 1, Arcane Meditation 2, Arcane Wrath 1, Presence of Mind 1, Arcane Mind 5, Arcane Instability 3, Arcane Power 1 |
| Fire | 17 | Incineration 5, Accelerant 5, Ignite 4, Pyroblast 1, Improved Fire Blast 1, Heating Up 1 |
| Frost | 3 | Precision 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 790 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 714 | [32/16/3](https://talentsforever.com/mage/60/041205203100311531-553000011001-003-12) |
| Pre-BiS | 778 | [32/16/3](https://talentsforever.com/mage/60/041205203100311531-553000011001-003-12) |
| Raid BiS | 800 | [32/16/3](https://talentsforever.com/mage/60/041205203100311531-553000011001-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.2; Pre-BiS 62.3; Raid BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Shroud of the Exile](https://www.wowhead.com/forever/item=15421) · *quest: In Dreams* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sorcerer's Bindings](https://www.wowhead.com/forever/item=226929) · *sold by Mokvar*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Sorcerer's Gauntlets](https://www.wowhead.com/forever/item=226930) · *sold by Mokvar* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18468) · *quest: The Arcanist's Cookbook* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Cloud Stone](https://www.wowhead.com/forever/item=17737) · *Landslide, Maraudon* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9MG0cUxv1mF+/zM6XuFLXbbQ9bWgq4dTW7ayPKxYZL/x2w2kulHsoaG+wKbMv2gd6AoqpFLSBUVcXqoUJIRFEQUk6ARKREimQOiZJDgpRcUP6IHBMOJLkk0W5sghIU5QDOd9iZnU+7+9tv5unRBwgBUEGHduiHNORhDOB3gP8BTgDwRtdljtsF2m+NiAHUcqTg0hyot/0k468rQBKeSZOEG6Ok4OUZUG82kYJnZ0G93kQSnh8iCad/JAVXJtyHFNxaBnVGIQkf2yTheIIknB0hGRdngbz454haeZtk3JxyXr073PJZoJJpvzgNYi8R/2sBpoBNZuaA7SXKwHZ6TgIu/QenpmA6sw2TmV50mSEG6+wjETZMETGFZQhhGUbEMkKRiCWEEIYhhBESwqowuMT8N9gMcVlj3R7erHHynQYvyXhhTdUaSMJbfXwMuG3nh3/K5Uu6KczOkCFCZrhbH0jb2aFUUs8VdDuZTCX1xC96KZ3SC7mSXcrksnoxZRcG0np7MZXS7cKAnU2FkvliqOaHnvqf/1zMZTu09+mt4Jvo5ewbj6ZQA0mGKGoOycSDOC/XBSFCn2od5L/mRZJxY01VgbSgihL3rbuZbKypmq/MnOnfV77VqiP/4xA4yzhquI9fiWW1Lizf09f8S+rUwi9joneCzShz37l9r4EkApPeaPGTbxeeR/+3LugWdfA2Fw1qaPdqaNZBtIdzoFVHPvwimeg6ajLFgcCtPv5PXQ67QW28lQLBpmrNeUkmZhVrVZioVqEZad3fId8zxkMSMa3jSWSpj4/UIxB0/3PnflyV7rAK3GXmuORxFY4tOKeVGELLI+Zzljxjg7H3yvOONqMfDrq6GjW3mSrr0eAq87wWlWK12bHqk+Vj+84X7vW7xVhPdSHW7/TkeXBvPNvRoISr7/YeaN0CuiAGX0EcfoA05GEURtmTAQA6dNP7); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9MG0cUxv1mF/v5mVJ3itrttoctLQXcuprdtRHlYsOl/w5Y7aW3ssamdgW2ZftAb7Tl0KIWI4RQcXtoUSWiKCRSDhEgcQgnJ1IiXxKk5IKSIKJcknAgiSJF0W5sghIU5QDOd5iZnU+j/e238/ToPQQ/KKBBJwxCCnIwDvAbwL8AxwB4s+My2+0BdbIZ0Y9qgTz4cAmULR/J+OspIBlvzdrj31U/ubGSUa63kAfPToNytYUkXM+QjFslIDfuDNunPLixBErJQzLOVf0k4/n/7ONnqn6ScHqUPHj7JCiVN0nGP0pAEu6MtH3ir6Q7L06B2I3H/lyASWAT6Rlgu/EysO2+44CL/8CJSZhKb8JEuh8dbojCKvtAhHRDhA1h6kKYuh429WA4bAohhK4LoQeFMCsMqsx3jZWIyyrrdfFWlZP3NLhJxgsritpEEt4Y4OPALSs38n02V9QMYXQHdRE0Qr3aUMrK/JBMaNm8ZiUSyYQW/0krppJaPlu0iulsRiskrfxQSussJJOalR+yMslgIlcI1v3gE//THwvZTJf6Lr0ReB3dnH3lUj3URJIuCqpN8sv9GC83BCFMH6td5LviRpJxbUVRgNSAghL3rjqZrK0oqrfM7OXspa/V2sx/PwDO1A8b7sOXYlluCMu39CX/nLrV0IuY6K1AK8rcu77nNZFEYNBrbT7y7sCz6H81BN2kLt7hoEEd7W4dzdyP9mAG1NrMR54nEz2HTeaxIXBjgM815LLr1MHbyR9oqdWcm2RiZqFehfFaFRrh9r0/5H3KeEAihnk0iSwO8NFGBILOd27fiynSTVaBO8z4WXI5CkUX7NtKDKHtEfPaW67x4eg75Xlb5yLvDzu6HDE2mSJrkcAyc70SFaP11ZHqo6Uje89nzvjN/9G+2kZ00O7L8+A8uDYjAQmX3+7f174F9EAUvoAYfAcpyMEYjLHHAwByvdcN); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElU9ME1kcx/t7M3Ref6Vs9y3ZnZ3dwyy7LNDdbt7MtITl0sJl/x1odi97W6a0bGuwbdrG4A0NByVCE0Qi1YMhJhgjHjwYIOHiqcZoelESvRCVYAyJQiJqTIiZsUWixHiA+j383pv3zcx85jvvl4ffUvCCDCq0Qi8kIANDAMcAzgFcAGD1tksstwOU0XpKvVQ5hBJ9NQvyihtFujUOKNLHE1Y9U/aik5ZS8oMGlOj6mke+14Ai3VjzoEhXCoASfbbmse6T6NIsyAUJRTpZ9qJIb5yyHjB80qpXy16U6JPLIJe+QJGeKAAKdGOg6WdvKdl6awz4ZjQyOg0jQIaT40A2o0Ugq10Xgc6chUsjMJZchuFkN7XRIQwL5Hse0HQe1LmhcW5oWtDQ/MGgwTnnmsa55ufcKBEoE/d9UkAmKqTTwRoVhq4r4ESR3pyXlToU6MMeNgTMNDMD/6UzeVXnertf43490Kn2JczU//GYms6qZiwWj6nRw2o+EVez6byZT6ZTai5uZvsSamsuHlfNbJ+ZivtjmZy/6vvf+L8cyKVTbco3+LnvM+pk5E+HImEdChrPKRbJ0RcRVqwJQhB/UtrQfddJUaSL87IMqPhkKjDXgp3J4rysuIrEmk7c/kupjOz4LnCGttdwP3wUy1xNWP7BP9hv2K4EPsSEX/oaqchc17a9OhQQdPQ0udG1Ae+in64JuoFtrMVGgyraehXN2In2chyUysgG3ifjHXtNJlkQdKmHTdZks2vYwprR62uo9JwTRSRGrtqF0UoX6sHm7T/kesu4SyK6sT+JzPSwg7UIhNrfufo8IguPSAmeEv2I4LAVCE9buxUJhaYt4rKWHEP94a+LU5auh77rt3UnpC8TWVRDvjni+CTKh6uzfdWPs/v2nl/t+vf5cFdlIdxrHc1TYF84lkM+gc591b3jBOfQAWH4HSLwLyQgA4MwSF4PAI092W0=).

## Other builds of this spec

- [Arcane — Arcane Blast](../research/raid/builds/arcane-blast-raid.md) (31/13/7, 707 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/050205203100301531-505001002-043-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

