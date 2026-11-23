# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Smite — Raid](../research/raid/builds/smite-open-raid.md)** (17/17/17) — [open the talent tree](https://talentsforever.com/priest/60/50203003103-10505121002-502520010002-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Discipline/Holy — Smite), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Holy Fire**.

**Talents with no line below:** **Holy Nova**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Mind Blast**
3. **Inner Focus**, then straight away **Devouring Plague**; no global cooldown, so press it alongside the others
4. **Holy Fire**: keep it on the target, when you have at least 40% mana
5. **Inner Focus**, then straight away **Smite**; no global cooldown, so press it alongside the others
6. **Shadow Word: Death** (rank 3)
7. **Smite** when you have at least 25% mana
8. **Smite** (rank 7)

**Smite** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Mind Flay**: now and then (in about 1 of 12 fights)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps **Shadow Word: Pain** on the boss, fires **Mind Blast** every time it is ready, keeps **Holy Fire** burning while your mana holds, casts **Shadow Word: Death** on cooldown and **Smite** in every gap. **Power in Light** is the tree's reason: your **Smite** deals 10% more while your **Holy Fire** or **Shadow Word: Pain** is on the target. 602 DPS in a full raid against the Shadow page's 788.

**Why it works**

- **Shadow Word: Pain** (8 casts, 19%) comes first: instant, 762 damage over 24 seconds with **Improved Shadow Word: Pain**, and the cheapest way to keep **Power in Light** on. Recast it when it falls off, not in the last 10 seconds.
- **Mind Blast** whenever it is ready (22 casts, 19%): 477-503 damage in a 1.5-second cast every 5.5 seconds with **Improved Mind Blast**. It costs more than a **Smite** but lands far more per cast; **Shadow Focus** gives it hit.
- **Inner Focus** goes into **Devouring Plague** at the pull: the plague is free that once (985 mana otherwise, which this build cannot halve) and runs 24 seconds. In a longer fight the second **Inner Focus** goes into a **Smite** for its 25% crit bonus.
- **Holy Fire** (6 casts, 8%): 184-232 damage plus 75 over 10 seconds in a 3-second cast with **Divine Fury**; one goes out 3 seconds before the pull, and the list recasts it as its burn ends while you have at least 40% mana. **Searing Light** adds 5% Holy damage, **Holy Specialization** 5% crit, **Holy Precision** 18% hit.
- **Shadow Word: Death** (10 casts, 8%) on its 18-second cooldown: the list casts rank 3 (the search measured it 0.5% ahead of rank 4: less mana for nearly the same hit).
- **Smite** is the filler (60 casts, 45%): 2 seconds with **Divine Fury**, 280 mana less **Mental Agility**'s 10%, 10% more under your **Shadow Word: Pain** or **Holy Fire**. The page's **Smite** lines are mana gates: the top rank above 25% mana; below that rank 4, the lowest rank the trainer teaches at level 20 or above (cheaper, about 29 of your 54 **Smite** casts); in the last 10 seconds the top rank again while you have 20% mana, else rank 7; only when you cannot afford even that does it channel **Mind Flay** (almost never in the simulator's raid fights).
- Mana: **Meditation** keeps half your regeneration going while you cast; the simulator's priest also uses two mana potions and two Demonic Runes a fight and still runs dry late. In a 6-minute fight its DPS falls from 602 to 280.

**Caveats**

- This build has no **Penance** (it needs 20 Discipline points) and no **Power Infusion** or **Shadowform**: the full list's lines for them never fire. The Smite page is a showcase for the tree, 24% behind Shadow.
- **Shadow Word: Death** hits you for 30% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Mind Blast** all need you to stand still.
- Ranks taught below level 20 get much less from your spell power (Classic's rule: 3.75% less a level below 20, so rank 2 at level 6 gets under half). The simulator does not model that yet, so the page uses rank 4 (level 22) as the cheap **Smite**: rank 2 had looked 2.5% better only because of that gap, and without a cheap rank the build runs out of mana for 50 seconds of a 3-minute fight.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** rather than a new **Holy Fire**: only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does.
- Packs: **Holy Nova** hits everything within 10 yards and heals your party, and **Searing Light** gives each **Holy Fire** tick a 10% chance to make your next **Holy Nova** cost no mana.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 17 | Power in Light 5, Twin Disciplines 2, Holy Precision 3, Mental Agility 3, Inner Focus 1, Meditation 3 |
| Holy | 17 | Holy Specialization 5, Divine Fury 5, Holy Nova 1 (tier point: needed to reach Searing Light), Blessed Recovery 2 (tier point: needed to reach Searing Light), Inspiration 1 (tier point: needed to reach Searing Light), Searing Light 2, Twilight Focus 1 (tier point: needed to reach Searing Light) |
| Shadow | 17 | Shadow Focus 5, Improved Mind Blast 5, Improved Shadow Word: Pain 2, Mind Flay 1 (tier point: needed to reach Shadow Weaving), Shadow Weaving 2, Spirit Tap 2 (tier point: needed to reach Shadow Weaving) |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-11-03 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 588 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 555 | its own set |
| Pre-BiS | 588 | its own set |
| Raid BiS | 611 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 61.0; Pre-BiS 61.9; Raid BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Thuzadin Mantle](https://www.wowhead.com/forever/item=22412) · *Baron Rivendare, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) · *quest: Holy Bologna: What the Light Won't Tell You* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Quests and dungeons: Enchant Weapon - Spell Power (Molten Core); Pre-BiS: Enchant Weapon - Spell Power (Molten Core); Raid BiS: Choker of the Fire Lord, Flarecore Leggings, Ring of Spell Power, Talisman of Ephemeral Power, Enchant Weapon - Spell Power (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/priest/dps/#eJzElk1sG0UUx/1mN97xSz/MUJrtqkJTU5BrWDM7jlESDnF7qnqACskSB1Cyttfxtvau5d2QFC6p1EOFihMFCdSqKAiBipAoXIgqblAhBQlBuSAkLlERgiP0kN4KWm8cUNJjYt5hPH5vZ9///d5bafAohTTowCEL09CANiwAXAZ4H+BjALavFyVRdAyMywcpTQ8ZPmr0xjLovw2jSu++C6jSK59F681FQI3+uAj6rwdQo18tgf7LAVToNzOo0h+uAybpvXp0LElvvqIvaqjQv21U6MUKKnSphSr9aCl66EpLX3sUFbrwKir0XjPzdHrNzX7fBbFROfvWB/AmkEvuMpCNyjUgv5/8BLQb1+Hz0113HS65p2hPMpTgS3K8KKQoCFGwRMG0RFEULWkJIc2iEEUphCWFkGsE7pDhu+Tt/XgIU4aGQ1lK35vLaDiEilkI2DKwabvdnPLbIZdCPmeKcVOOTfBqw/ZmnBr3O9yu1Zwar1zgYcPhHT+0Q9f3eODYnWqDZwPH4UHLDR2z1g7MftiMw/lzge+dMPL4BDuG+zPDmJKxhG4Z07kDNMnImYSRRBWJJTbVdcusNQBNMYwUvV1mbwwg3Yh8DDVjCBW6EiAaFJPZJL3zDjDVIBMJtrK9DZYw5fgua3geBcvjkdwIVVjqXH8WIi2oinwxwEdyB6OWVBIRG1RGxZNbE8N047A89G8J/VlaLTNvAPhiYgq9ff9Fdn4nKrHb+eI6v3uBLQyiMUe3k5fFPvnVMrOMZ/E4y2z/frYdKWw1q1tmK4Q9gBiOZUrBsxF4e7bmhjxwgsD1vQnu+bxje+d5aM/ONEJecZr+HJeCzzXcptOrJXBbs0079Dt8xn3NCbgb9tz12WaTV32nXnerruOFJybiF41y1+Ptpl11uF+PXfKZuLNTNX/OizxTliVFvn0hzwcH9cwmIUsE0Sar0p819vhDoG8RXC2zYSOecI1+UX7oxFm7LDeeuL/mdyazTFHYi2TpjQp7fWdl1uguJzuM+zKIVCZRpfeXwdj81ZU/yBr8SWoXlUTPRktfg2oQTGQekFTkSCzUS0euXY3s28lj9Z79NCnXia7yydwtkvhfLCz1d3tqT326Z3nGe+tLH5ZObjpK09Gt6Cr0/iTWJ3MKvTVy6j+XJwFjUILTcBZehga0YR7myT8DAE5eQQ8=); Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEll1oHFUUx/fcmezcPWnT9Vqb6VDkdq2yXZ31zt2sJPEh2z6VPmgRFnwQktnd2ey0m5llZ2JSfYmlD+LHRqIorZWoCIpQ8cVQfNMiRBHJkwi+hEpVxAftQ/ogFJmdbJSkj8n2PNy5cw53zv/8zhm4eIRCGnTgkIUpaEALFgBeBngf4BMAtq8bJVF0FIxXD1CaHjDaqNF/roJ+cxBVeuMdQJX+8Va0vruWxiS90NB/GUKNfvUG6D8PoUK/mUaV3lwETNJb9ehUkn72nL6ooUq/+yA61/kzjSpdWUujQi84qNFfr4C+ej+q9LVFQIXeamYeTa+62R86IDYqZ17/EF4BctFdArJRuQzktxOfgvbxFfj8VMddh4vuSdpVDSX4khwrCikKQhQsUTAtURRFS1pCSLMoRFEKYUkh5CqBNTJ4g7y5Hw9iytBwIEvpe3MZDQdQMQsBWwI2Zbeak34r5FLIJ0wxZsrRcV5t2N60U+N+m9u1mlPjlfM8bDi87Yd26PoeDxy7XW3wbOA4PJhxQ8estQKzFzbjcP5s4HvHjTw+xI7i/swgpmQsoVPGdG6IJhk5nTCSqCKxxKa6TpnN9EFTDCNFr5fZi31INywfQM0YQIUuB4gGxWQ2SdfeBqYaZDzBlre3wRKmHNtlDU+iYHk8nBumCkud7c1CpAVVkS8GeF/uQNSSSiJig8qIeHhrYphuHJIH/yuhN0srZeb1AV9MTKHXbz/Nzu1EJXY7X1zn90+xhX405sh28rLYI79SZpbxOB5jme3/z7Yjha1mdcpsmbA7EMOxTCl4NgJvz9bckAdOELi+N849n7dt7xwP7dnpRsgrTtOf41LwuYbbdLq1BO7MbNMO/Tafdp93Au6GXXd9ttnkVd+p192q63jh8fH4QyPc9XiraVcd7tdjl3ws7uxkzZ/zIs+kZUmRb53P8/5BPb1JyBJBtMmq9CeNPXgX6FsEV8ps0IgnXKNflO86cdYuy40n7u/5ncksUxT2Ill6o8Je2FmZNbLLyQ7hvgwilUlU6e0lMDafuvI7WYW/SO0lJdG1kdLXoBoEE5k7JBU5Egv10uHLlyL7duJovWs/Tsh1oqt8IneNJO6JhaXebk/tkat7lmesuz7zUenEpqM0FV2MLkH3JbE+kVPoteGT/7s/CRiFEpyCM/AsNKAF8zBP/h0ASQdDXw==); Raid BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEll1oHFUUx/fcmezcnLTpeq3Ndihyu1bZrs56525WkviQbZ9KH7QICz4IyezubHbazcyyMzGpvkTJg4jdSGqF1kpUBEWo+GIovmkR4geSJxFECEpVfFIf0gchyMxkoyR9TLbn4ezdc7h7/ud3zsLFYxRSkAYOWZiEBrRgHuAVgHcAPgRgB6IsCbMjoF86RGmqTw9Qo//cgPTtAVTp5hKgSv94I/RvraUwSV9upH8ZRI1+/jqkfxxEhX45hSq9vQio0Z+uRNeS9OPn0osaqvSbK+HFr98N/cLl0K+spVCjv16H9Or9qNLXFgEV+ncz82hq1cl+1wGxUTl36T14FciCswRko3INyG+nPgLtg+vwyZmOsw4Lzmka6YYSfEZOFIUUBSEKpigYpiiKoilNIaRRFKIohTClEHKVwBoZ+JlcPoiHsV/XsC9L6duzGQ37UDEKPlsCNmm1mhNeK+BSyCcMMWrIkTFebVjulF3jXptbtZpd45WLPGjYvO0FVuB4Lvdtq11t8Kxv29yfdgLbqLV8o5s24nT+vO+5J/U8PsSO48HMAPbLWEKnjKncIE0ycjahJ1FFYootdZ0ym+6BphhGP71VZi/2oNyQfAA1vQ8Vuuwj6hST2SRdexOYqpOxBFveOQZTGHJ0jzU8iYLl8WhuiCqs/3x3F0ItqIp80cf7cofCkVQSIRtUhsXD2xvD0voRefi/Frq7tFJmbg/wxcQUeuvO0+zCblRir+vFfX77FJvvxWCO7SQvi13yK2Vm6o/jCZbZ+f/ZcaWwPaxOmS0TtgkxHNOQgmdD8NZMzQm4b/u+47lj3PV423Iv8MCamWoEvGI3vVkuBZ9tOE076sV3pmeaVuC1+ZTzvO1zJ4jC9Zlmk1c9u153qo7tBifH4h8a5o7LW02ranOvHofkY/FkJ2rerBtGJkxTinzrYp73DurZLUKm8MNDVqU/aOzBu0DfJrhSZgN6vOEa/bR8140z91huvHF/ze0uZhqisB/FUhsV9sLuzszhPS52BA9kEKlMokrvLIG+9ZlWfier8CepvaQkIhsufQGqTjCR2ST9YSAxXy8dvXY1tK/Gj9cj+35crpO0ysdzN0ninlhQ6p721R65sW91RiP/zPulU1uB0mT4NLoK0ZfE+nhOoTeHTv/vBSVgBEpwBs7Bs9CAFszBHPl3ALqrQ58=).

**Points that do nothing for this spec:** **Blessed Recovery** (2), **Holy Nova** (1), **Inspiration** (1) and **Twilight Focus** (1) only count toward the points the tree needs before **Searing Light**; **Mind Flay** (1) and **Spirit Tap** (2) only count toward the points the tree needs before **Shadow Weaving**.

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 574 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Vampiric Embrace heals the party for 10% of your Shadow damage since client 1.60.1.71037 (20% before; you still get 20%); the raid numbers here predate it.*

