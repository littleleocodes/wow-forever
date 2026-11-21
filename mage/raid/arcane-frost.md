# Arcane-Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Arcane-Frost

*Arcane's Missile Barrage, Arcane Wrath, Arcane Mind and Arcane Instability on a Frostbolt filler (Improved Frostbolt, Ice Shards).* (a hybrid: Arcane/Frost).

**[Arcane-Frost — Raid](../research/raid/builds/arcane-frost-open-raid.md)** (28/10/13) — [open the talent tree](https://talentsforever.com/mage/60/03222420310001053-55-0535-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Frost — Arcane Power / Frostbolt), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Arcane Blast**: keep its buff stacked on you
3. **Arcane Wrath** until the last 20 seconds of the fight
4. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arcane-Frost is an Arcane list with a **Frostbolt** filler: keep two stacks of your **Arcane Blast** buff up, **Arcane Wrath** whenever it is ready, a free **Arcane Missiles** on every **Missile Barrage** proc, and **Frostbolt** in every gap, which rolls for the proc too. There is no cooldown to press: the build takes neither Presence of Mind nor Arcane Power. 692 DPS in a full raid, in its own entry (arcane-frost-raid, the rotation its search tuned), 16% behind the Arcane page.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** comes first: 14 casts and 29% of the damage. **Arcane Blast** gives a 40% chance per cast, **Arcane Wrath** and **Frostbolt** 20% each, so with three sources the proc is up often; it makes the next Missiles free, 2.5 seconds long and twice as dense. **Arcane Impact** adds 6% crit, **Arcane Mind** doubles the crit bonus of your Arcane spells, and **Arcane Instability** adds 3% damage and 3% crit to everything.
- **Arcane Blast**, 24 casts and 16%: keep its buff stacked on you. Each cast gives you 12% of your Intellect as spell damage for 18 seconds, stacking to 4, and adds 100% to its mana cost per stack; the list casts it when the buff is missing or about to run out and until it has 2 stacks, then lets **Frostbolt** fill. Adding that line was the raid search's biggest gain for this entry (+6.1%).
- **Arcane Wrath** whenever it is ready (14 casts, 25%): 3 seconds with **Accelerant**, a 6-second cooldown, 406-496 damage plus 5% of your maximum mana as spell damage, and its own **Missile Barrage** roll. The list stops it with 20 seconds left: late casts and their flight time overrun the fight (+0.4% in the search).
- **Frostbolt** fills everything else (26 casts, 29%): 2.5 seconds with **Improved Frostbolt**, 260 mana at the rank the list names (rank 10), **Precision**'s 6% hit, **Ice Shards**' doubled crit bonus, and a 20% **Missile Barrage** roll of its own. The Frost half ends at **Ice Shards**: this build has no Ice Lance, Shatter or Fingers of Frost.
- **Fire Blast** only in the last 3 seconds, when a **Frostbolt** would land too late; **Incineration** gives it 10% crit.
- Mana: your mana gem (from **Conjure Mana Ruby**) below 80% mana, a mana potion, **Arcane Concentration** at 5 points (10% free casts) and **Magic Absorption** (1% of your mana back for each spell you fully resist). With a raid's buffs the simulator almost never needed **Evocation** here (one fight in 750); its line fires below 20% mana with more than 25 seconds left.

**Caveats**

- The Arcane page's build (the official simulator's Arcane Fire, since 2026-11-20) is the same Arcane core with Arcane's cooldowns and a Fire half: it takes Presence of Mind, Arcane Power, Pyroblast and Heating Up, casts **Fire Blast** on cooldown and a 1.5-second Pyroblast at three Heating Up stacks: 826 against 692. This page exists because the hybrid split is its own spec on these pages.
- Several targets: **Arcane Explosion**, **Blizzard** and **Cone of Cold**; the simulator fights one boss.
- Moving: **Fire Blast** is your only instant. Threat: **Arcane Subtlety** cuts Arcane threat by 30%; the simulator ignores threat.

**When to change it**

- In the last 20 seconds no **Arcane Wrath**; in the last 3 seconds **Fire Blast** instead of a **Frostbolt**.
- Without raid mana buffs, the simulator's list for playing alone channels **Evocation** only below 5% mana while more than 50 seconds remain; later, the mana comes back too late to spend.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 28 | Improved Channeling 3, Arcane Resilience 2, Arcane Subtlety 2, Arcane Concentration 4, Missile Barrage 2, Arcane Impact 3, Arcane Blast 1, Arcane Wrath 1, Arcane Mind 5, Arcane Instability 3, Magic Absorption 2 |
| Fire | 10 | Incineration 5, Accelerant 5 |
| Frost | 13 | Improved Frostbolt 5, Precision 3, Ice Shards 5 |

## The numbers

**How this pick was checked:** a short check on 2026-11-20 (every one-move and chain-move neighbour raced in a full raid, two rounds; nothing better). A full search, talents and rotation in turns until stable, follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 692 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 629 | its own set |
| Pre-BiS | 685 | its own set |
| Raid BiS | 702 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.3; Pre-BiS 62.3; Raid BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Shroud of the Exile](https://www.wowhead.com/forever/item=15421) · *quest: In Dreams* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sorcerer's Bindings](https://www.wowhead.com/forever/item=226929) · *sold by Mokvar*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18468) · *quest: The Arcanist's Cookbook* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzElk+MFMUXx/d1z+7WFr8frI3A0HJ4bLI4O+4sPT3MZlkTdkBjRKJs9KDRKNRM12yX6emadNUwcDGLYmKIAkEvEE0MwWAEYsIJSDDBhGQ10aiJcvBC/BP1pOFAPKGpnl4Ww1WwDp3q96333qfee500XUdgGPKAUIDdEEIb5gHeAHgf4EMA53+pahl1Ctwz/ydkmLgtOkhOHYX8z8tojrz2MVCbfBJSm1zaSwfJ14ch/+NyOkguH4H898upTa7MUZsceoEOkOtN4zNIrp6F/OFBapO/GLXJ/jq1yZEWzZGTR4AOkDdb+YWV1CbzL1KbXI9GxocXROHLQ+DdqM++dQIOgnVAHAXrRv04WL9s/QjIqXfhzEE4JK7BAbGNpMRQg4vWWs+v+P4m36uUPc8re9VKqVotedVKdcGCr6xlP1iXl1GHDrr91Ca/8ZFB2k/tkq+cb3LO2RwLAh6g7/mTpXK5VN6MhY7iyTSOhLKLQuH2BsdtLEkETzCWGrsy0SEKjU2Z4GOJVBonJiZwu0YRNxLOFFcYsBab4xjImGN9H/reKHZDEXEUWiFraLGHj4xN/yN0N+Qx38NNSDEnApyVXZ6Mpw4PlaujWaYssEldxpaIxzFkCjtxwBP0UWHEm/ph1CFHFQoeBciCQGF1KT2GMgoUFpRobTShNooG31XvMUzMSWzJgEcK61KHYxP4lMREaqaFjFE2UXYShSELsMGURqHHUUk00PtQcZY0QtzDog4PUgDNIh5rZBo9ZHHP1rtEvSMMg9Ky3eaBOVHxMqktRawVFoQ2pTculXIpNWbxxqZRxhy3Jg0Wc+wpItYypTHnnxWx5smDCh8JRRT1cmHVr2BpC1anpvDR2WdSnKbJV2pFpYSJACfL6YHJSQ9FjAybnSjCVClMjnueh00xF2o15iJdU1xFbGfoIgzQHDl9c9YdoDlq+SqbLuc0OK/DbUPlbS75U9OLxE8KpUTEFUqTJntLh8D0tZ3IxjjOdVhi3Ov7kHUStl3tiGU3NrVm2X26Qoeyo+/w702Q6Y5Cod31NO+spkOf5wzqFxfydOgcZNuU9qedzgfgMNaOdsm2zr4Br+RXprERsniOBygTM0I9GFPeW+OQNbygOM9qacpVWtRLPX3iZSXjMbdGJ91N1C3mlyp36ULeHTpume073+6gq4v3G+3TW1o/tSn4bqY761yX3ldcQXKOVe9z0y94yhs1txhe2OLkXGu6z6m4ZVpwNqTn7KVzvjeamvod64lFU7XXrrdfcubvSQEeSAkGbiPwVHq3V/+cdVa5Kxc7897FfGr+/eoO55U7wTz/3wZbS4eLyzOwdJArvcpc2ekchHsBMErXFV0D8Hyf65yzVhB7qUjlspfCXN2Zt3+1FuAPK9hv96VrU+2EGRVqERi5aQ0ZU998s7b2+DGzPptZ30zXdzP+NSufw5nieavvP1m6tri7q2vD2buWZ3P6fPpkbWtmqO02fw7HIH3puzZTtMn5Ndtu+8HwYApq8DjMwnMQQhv2wl7r7wEAWggEEA==); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElk2MFEUUx/f19O7UFgpjIzC0HB6bLM6O20tPD7NZ1oQd0BiRKBs9aDwIPdM122V6uyZdNQxcDComhigQJSagJko0GnE14WCAxAMkJiuJZmOiHLwQlfhxwXAgJibEVE8vi+EqWIdO9fvXe+9X771Omq4jUIAiIJRgN4TQhv0ArwK8B/AxgHVXqhpanQD71N2EFIgtaZ78PQfFy8uoSV7+HKhJ/jiqn28vFOgAmY+LPy+neXLuCBR/XE5z5HxMTXL5MNABcrWlvfLk4hwUD+epSd5aKFCTXHhfu3+xUKA5cmSW5smVz6A4v5Ka5LXDQHPkajQ0WpjnpW8PgXutMf36CTgIxgH+BhjXGsfB+HXrJ0A+egc+PQiH+CU4wLeRlBvqcNZY61arnlvz3GrFdd2KW6s6tZrj1qq1eQMWjGU/GeeWUYvm7X6aI7+zoTztpznHk9Z3pjVn+kHAAvRcb9ypVJzKZix1JEsmcSgUXeQStzcZbvOThLMEY6GwKxIVIlfYEgk+kgipcGxsDLcr5HEzYb5kEgN/1p9hGIiYYWMfeu4wdkMeMeRKot9UfA8bGpn8V+huyGK2h+mQfIYHOC26LBlNHR6o1IazTFlgnbqCszwexdCX2IkDlqCHEiPWUg+iChnKkLMoQD8IJNaW0mMookBiSfLZjTrURt5kuxo9hrEZgbMiYJHEhlDhyBg+ITARyldcxChaKDqJxNAPsOlLhVyNohSoofehZH7SDHGPH3VYkAIoP2KxQl+hi37cs/Uu0ehwzSCVaLdZoE9U3UxqCx4riSWudOm1S7XipMYs3sgkipjh1qTpxwx7Co+VSGn0+ad5rFhyv8SHQh5FvVxY86robMHaxAQ+PP1UitPS+ZzZyEl8HuB4JT0wPu4ij9HHVieKMFVK46Ou62KLz4RKjthI15RXkZw1eBYGqElOXp+2B6hJDU9m02WdBOsVuGmo3M2ONzG5SPw4l5JHTKLQabK3dAh0X9uJaI7iTMdPtHtjH/qdxN8ud8SiG+ta+9l9ulyFoqNu8e9NkO6ORK7s9bRoraaDF0yN+s2ZIh08Bdk2pf1lp/UhWL7fjnaJtsq+AdfxqpPYDP14hgUoEj1CPRhd3hvjkDW8JBnLaqnL5SzqTk8fe16KeMSu03F7E7XLxaXKfXmmaA8eN/T26Pc76OryvVo7f0PrpzkKnp3p1jrbpveUVxDTMhp9dvoFT7jD+haF+S2WaRuTfVbVrtCStSE9l1s657nDqanfMh5bNNV67XrzOWv/HSnAfSnBwE0Erkzv9tJf09Yqe+ViZ949W0zNVy7usF64Fcz1/muwtbRQXp6BpYNc7VXmq53WQbgTAMN0XdnWAM/22dYpYwXJLRWpUnFTmIs7i7nfjHn40whezPWla1P9hB4VahAYum4MalPf/lZ97fFjen09tb6Vrh+mvEtG0cSp8mmj739Zqr64u61rw9xty7M5fT75QX1rZqjv1v8PxyB96bs0Vc6R02u23fSb4cIE1OFRmIZnIIQ27IW9xj8DAHbrB3k=); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElk2MFEUUx/f19O7UFgJjIzC0HB6bLM6O20tPD7NZ1oQd0BiRKBs9aDwIPdM122V6uyZdNQxcDBpMDFEwgCagJoZoNOJ6wAuQeJDEZNVoiIly8EJU4kdIUBOJiQkx1dPLYrgK1qFT/f713vvVe6+TpmsJFKAICCXYBSG0YR/AiwBvAbwHYN2RqoZWJ8D+aCkhBWIrmid/z0Hx0hJqkmuHgZrk16P6+fr5Ah0g83Hxh2U0T36/vLT43TKaI+diapJLh4DmyZ+Xl2q3PLkwB8VDeWqS184XqEm+eFX77z8CNEdemaV5cuVDKM6voCZ56ZC2/RENjRbmeemrg+BebUy/fAIOgLGfHwbjauM4GD9teR/Iu2/ABwfgIL8I+/lWkoJDHc4aa1yv6nkbPbdacV234taqTq3muLVqbd6A88aS741PllCL5u1+miO/sKE87ac5x5PW16Y1Z/pBwAL0XG/cqVScyiYsdSRLJnEoFF3kErc1GW71k4SzBGOhsCsSFSJX2BIJPpgIqXBsbAy3KeRxM2G+ZBIDf9afYRiImGFjL3ruMHZDHjHkSqLfVHw3GxqZ/FfobshitpvpkHyGBzgtuiwZTR3urdSGs0xZYJ26grM8HsXQl9iJA5aghxIj1lL3oQoZypCzKEA/CCTWFtNjKKJAYkny2Q061AbeZDsbPYaxGYGzImCRxIZQ4cgYPiowEcpXXMQoWig6icTQD7DpS4VcjaIUqKH3omR+0gxxtx91WJACKD9isUJfoYt+3LP1LtHocM0glWi3WaBPVN1MagseK4klrnTptUu14qTGLN7IJIqY4Zak6ccMewqPlUhp9PkneKxYco/E+0MeRb1cWPOq6GzG2sQEPjD9eIrT0vmc2chJfB7geCU9MD7uIo/Rx1YnijBVSuOjrutii8+ESo7YSFeXV5KcNXgWBqhJTl6btgeoSQ1PZtNlnQTrBbhhqNxNjjcxuUD8CJeSR0yi0Gmyt3QIdF/biWiO4kzHT7R7Yy/6ncTfJrfHohvrWvvZfbpchaKjbvLvTZDujkSu7HW0aK2ig5+bGvXLM0U6eAqybUr74w7rHbB8vx3tFG2VfQOu41UnsRn68QwLUCR6hHowurzXxyFreEkyltVSl8tZ0J2ePvaMFPGIXafj9kZql4uLlfv4TNEePG7o7dFvttNV5bu0du661k9zFDw70621tk3vLC8npmU0+uz0C55wh/UtCvObLdM2Jvusql2hJWt9ei63eM5zh1NTv2U8vGCq9dp15Glr320pwN0pwcANBK5M7/b8X9PWSnvFQmfePFtMzVcubLeevRnM9f5rsDW0UF6WgaWDXO1V5tMd1gG4HQDDdG3Z1gBP9dnWKWM5yS0WqVJxU5gLO4q5n415+M0Insv1pWtj/YQeFWoQGLpmDGpT375Wfc3xY3p9NrWula5vp7yLRtHEqfJpo+9/Waq+sLula/3cLcuzKX0+9nZ9S2ao79I/EMcgfem7OFXOkdOrt97wn+HCBNThIZiGJyGENuyBPcY/AwAEWwh/).

## Other builds of this spec

- [Frost — Arcane Power / Frostbolt](../research/raid/builds/frost-arcane-power-raid.md) (32/3/16, 680 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/050205203100311531-3-053500020001-12)
- [Frost — Fingers of Frost / Ice Lance / Shatter](../research/raid/builds/frost-fingers-of-frost-raid.md) (22/0/29, 623 DPS in a full raid; fails the signature-spell check: never casts Arcane Missiles) — [open the talent tree](https://talentsforever.com/mage/60/0322052030003011--05350003012130024-12)
- [Arcane-Frost (optimized)](../research/raid/builds/opt-frost-raid-raid-dps.md) (29/0/22, 599 DPS in a full raid; fails the signature-spell check: never casts Arcane Missiles) — [open the talent tree](https://talentsforever.com/mage/60/05022520310000153--0535000201013002-12)
- [Arcane-Frost (optimized, another mage's Winter's Chill)](../research/raid/builds/opt-frost-raid-raid-dps-extwc.md) (28/1/22, 598 DPS in a full raid; fails the signature-spell check: never casts Arcane Missiles) — [open the talent tree](https://talentsforever.com/mage/60/20320520310011143-1-0535000301003002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

