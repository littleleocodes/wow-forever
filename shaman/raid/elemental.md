# Elemental Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental

**✅ Recommended** for raid (the best shaman spec here, or within 3% of it).

**[Elemental — Lightning Overload / Elemental Fury](../research/raid/builds/elemental-raid-dps.md)** (29/22/0) — [open the talent tree](https://talentsforever.com/shaman/60/550233100200134-255000013400002--12)

## How to play

**Before the pull:** **Lightning Bolt**.

**Keep up all fight:** **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Flame Shock**: keep it on the target
2. **Lightning Bolt**

**Lightning Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Chain Lightning**: part of the rotation (about 13 times a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

**Lightning Bolt** fills every gap. Around it you keep a **Searing Totem** down and **Flame Shock** ticking, and cast **Chain Lightning** when two or more enemies stand together or when your mana is ahead of the time left. You play the same list from pull to kill. The official simulator ships no Elemental rotation, so this is the project's own: built on the deleted ElliotWood/Forever fork's preset and tuned in a full raid in 17 passes from 2026-09-28 to 2026-11-17; the play check of 2026-11-20 took out two lines that cast nothing (Lava Burst, no longer in Forever's spellbook, and an id the simulator does not know). This 29/22/0 build takes no **Lightning Mastery**. In a 3-minute raid fight: **Lightning Bolt** 68 casts, **Chain Lightning** 13, **Flame Shock** 9, **Searing Totem** 4; **Lightning Bolt** 68% of the damage, **Chain Lightning** 14%, **Flame Shock** 13%, **Searing Totem** 4%.

**Why it works**

- **Searing Totem** first: a new one when the old has 2 seconds or less left, so it never lapses (it lasts 55 seconds, 4 a fight), but none in the last 10 seconds. It shoots an enemy within 20 yards; the simulator stands you 15 yards from the boss. It is 4% of your damage, with **Call of Flame**'s 15% and **Elemental Fury**'s bigger crits on it.
- **Flame Shock** whenever it is off the boss: 13% of your damage. With 3 points in **Call of Flame** it lasts 21 seconds and hits 15% harder, so it is recast about every 21 seconds; the shocks' cooldown (5.6 seconds with 2 points in **Reverberation**) never holds it up.
- Then your cooldowns and a potion: the simulated gear's trinkets (Talisman of Ephemeral Power twice a fight, Weakness Analyzer once) and a Demonic Rune (twice) whenever ready, a Major Mana Potion below 80% mana (about twice). This build has no class cooldown on that line.
- **Chain Lightning** (6-second cooldown) on two or more targets whenever it is ready, and on one target while your mana is at least 50 for every second of the fight left (3,000 mana with a minute to go): 13 casts, 14% of your damage. On one target it deals about 8% more per cast than a **Lightning Bolt** in the same 2 seconds (this build's full-raid damage per cast), but costs 315 mana against 220, so on one target the list casts it only while you have mana to spare by that rule. Our rotation search lowered the threshold from 100 to 50 a second on 2026-11-04 (+2.2% on two seeds), and the list no longer saves Clearcasting for **Chain Lightning**.
- **Lightning Bolt** is the filler, 68 casts and 68% of your damage, at the top rank (rank 10); the list drops to rank 8 only when it cannot pay for rank 10, 0.2 casts a fight in a full raid. **Elemental Alacrity** (3 points) makes **Lightning Bolt** and **Chain Lightning** 2-second casts. Start the first **Lightning Bolt** 2 seconds before the pull so it lands as the fight starts.
- The rest of the build feeds the bolts: **Concussion** adds 5% to **Lightning Bolt** and **Chain Lightning**, **Call of Thunder** and **Thundering Strikes** 5% crit each, **Elemental Fury** (4 points) 80% to your crit bonus (a spell crit deals 190% instead of 150%), **Lightning Overload** a 30% chance of a second, half-damage copy at no cost, and **Elemental Focus** sometimes makes your next damage spell free. **Convection** and **Shamanistic Focus** cut your mana costs. From Enhancement, **Ancestral Knowledge** adds 10% Intellect and **Mental Quickness** turns up to 30% of your Intellect into spell damage. **Eye of the Storm**, **Earth's Grasp**, **Anticipation** and **Toughness** are there to reach the next tiers: the simulator finds no change without any of them.

**Caveats**

- **Lightning Overload** on **Chain Lightning**: in the simulator each target it hits rolls its own copy at a third of **Lightning Bolt**'s chance; the tooltip gives both 30%.
- Several targets: with two or more enemies close together the list casts **Chain Lightning** whenever it is ready (3 targets, each jump 30% weaker), and once your Fire totem has run out it drops a **Magma Totem** instead of a **Searing Totem**: 20 seconds, hitting enemies within 8 yards of it, at your feet.
- Mana: in a full raid the list almost never runs short in 3 minutes: it falls back to rank 8 **Lightning Bolt** 0.2 times a fight. Without a raid's mana buffs, or in a longer fight, the **Chain Lightning** rule spends less on its own, as long as you count the time left right.
- Your other totems: the simulated full raid already counts **Mana Spring Totem**, **Strength of Earth Totem** and **Windfury Totem** as up, so this list drops only your Fire totem. If you are your group's shaman, drop what your group needs at the pull: they last 5 minutes.
- Ranks: the list casts **Flame Shock** at rank 5, the trainer's top rank: rank 6 comes from a class book that is not in Forever on the evidence there is (2026-11-20; checked again when the raids open on 2026-12-09).
- Moving: **Flame Shock** (20 yards) and your totems are instant; the bolts are not.

**When to change it**

- In the last 10 seconds, do not drop a new **Searing Totem**: it would shoot only a few times. Cast a **Lightning Bolt** instead.
- On a boss that lives much longer than 3 minutes, count the real time left for the **Chain Lightning** rule: counted against a shorter fight, it spends mana you will need later.
- If the boss will die before a 2-second cast can finish, only an instant still lands: an **Earth Shock** hits harder at once than **Flame Shock** (the two share a cooldown).
- If you play one of the 31-point builds under Other builds (32/11/8 or 31/11/9), press Lightning Mastery whenever it is ready (3-minute cooldown, about once a fight in the simulator): for 15 seconds it takes 0.5 seconds off each **Lightning Bolt** and removes **Chain Lightning**'s cooldown.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Elemental | 29 | Concussion 5, Convection 5, Call of Flame 3, Elemental Alacrity 3, Reverberation 2, Elemental Focus 1, Eye of the Storm 2 (tier point: needed to reach Call of Thunder), Call of Thunder 1, Lightning Overload 3, Elemental Fury 4 |
| Enhancement | 22 | Ancestral Knowledge 5, Earth's Grasp 2 (tier point: needed to reach Toughness), Thundering Strikes 5, Anticipation 3 (tier point: needed to reach Toughness), Shamanistic Focus 1, Toughness 4 (tier point: needed to reach Mental Quickness), Mental Quickness 2 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** no talent search or short check of its own in this entry's current setup; one follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 741 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 670 | its own set |
| Pre-BiS | 733 | its own set |
| Raid BiS | 742 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.6; Pre-BiS 62.9; Raid BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Blue Dragonscale Helm](https://www.wowhead.com/forever/item=252604) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Blue Dragonscale Helm](https://www.wowhead.com/forever/item=252604) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Theramore Shoulderguards](https://www.wowhead.com/forever/item=272957) | [Theramore Shoulderguards](https://www.wowhead.com/forever/item=272957) |
| Back | [Shroud of the Exile](https://www.wowhead.com/forever/item=15421) · *quest: In Dreams* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Chestplate of Tranquility](https://www.wowhead.com/forever/item=18373) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Modest Armguards](https://www.wowhead.com/forever/item=18458) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Modest Armguards](https://www.wowhead.com/forever/item=18458) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Modest Armguards](https://www.wowhead.com/forever/item=18458) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Theramore Handguards](https://www.wowhead.com/forever/item=271950) | [Theramore Handguards](https://www.wowhead.com/forever/item=271950) |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18471) · *quest: Frost Shock and You* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Stoneflower Staff](https://www.wowhead.com/forever/item=18353) · *Tendris Warpwood, Dire Maul*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Quests and dungeons: Enchant Weapon - Spell Power (Molten Core); Pre-BiS: Enchant Weapon - Spell Power (Molten Core); Raid BiS: Choker of the Fire Lord, Ring of Spell Power, Talisman of Ephemeral Power, Enchant Weapon - Spell Power (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzElFFIFFsYx+c7Z9w5fl72rsfLvePcoGmhWhdGz8w6sS7BrkIQPbk+RT3krDu6W7q7OUvYm5IPIaTSSylBYYERSRQEEtSbsb2ET/VgD2JIvgThg48VMylI+rr0fxjOfOc73/c/v3M4eIRBBFTQIQb9UIAKjAPcBHgA8BiA/xXMEn82CdodxlhE0a5giH0qqJtNKLMbzwApe1NAyl6PocJWZkD9HEaFzc+CuhZGylaGkLLpixhi24P+GoV9XAJ1RkHKfjhI2UQOKZsdQZktzgIq7PkMqLUWlFBm919CtCNSK8beT4PYyfXeWoApIJPF20B2cvMQeug8db50PwFl8R5smtPFdZgs9rDAMmTgFTlq2yKRSJjCFEKYCds0hG0Lf2wIOyHMGqGrBDbIYgg5KloDUrZ1LapgA1LD8vgS8LxTGb5UrlR1S1inDNM0hJXSBwpOacjN6+VR3cnn3byeu65XC64+Wq461WK5pHuuMzpQ0GOe6+rusDvilqrOsJGveMZeivErpf2yVy61aWfwNE9hJB5mwOkGSL4TBBNb4s1M5g1TlDCqhVBGYnnYHP+bhTg5J2mBUVN4fjp7m+WdmoVt/GRQKLSvkHVIod1Va338X+0fbIo2omL5ZVazQXw1y2WNpCQ+cYCBMCy7Dgxag41RTnK7G0uK45qMRFX5wmHn0FkHDyk0tY5D8P0fb/WRX5C05hckzGhAP8BoiwDX1z5ePshJdNXB49415Vd/ayi6DCtZh4aN/nHECLubVekWqcE3kp+gUqD2zDbInKAU/U4a/YA0PphpnZ/z9S59bDDQh7S1TlRZT8eXifRHVM3sjeqqE0t169MVfPseZbp3A5l+/5Geg+BHWk/HKVv+r2ffWy4gCRk4C71wHgpQgTEYIz8HALYDMRQ=); Pre-BiS: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzEVE1oE1sUnnNnmrk9faTp7eO96bwHb15ATQPT3pk2kgYhaUEQV01X4sZOmqmJtElMgtRdq11Iwba4EFuLP1WoiEUQK0V0W6JIyUJ00U2pBLsRxEWXInNtodhug99i5s45537nu98dDv5LIQAaGBCCQchAAcYBrgHcA3gEwP4QWeJlo6DfoZQGVL2IKn210qzVmlChV58CKvT1+wAq9HY1gD56JaN98qNK52dB2/CjQtffecnaDKBK156LfSr9uAzajIoKvVn1sm/vA8p0dhQV+qIaQJXWFkCrtKKECr27AsHOQCUbWp8GvpPqv74IU0AmszeA7KTmwffAeeJ87n0M6tIC1Kzp7CZMZvuoUA4JeEn+i0S43dVlcW5zbnV1m3YkwrlYei+7QuQqgS2y5EOGqt6AMt2+FFSxAWXTLrFlYGmnMHIuXygbNrePm5ZlcjtmDGWc3Hk3beSLhpNOu2kjddkoZ1yjmC875Ww+Z5RcpziUMUIl1zXcEXfUzZWdETNdKJl7JebPko4LpXyuXT+JJ1gMA2E/BSZvgeQpQbCwNdxCFdYwJRMq6z5UkNglbAk3Ux8jpyVdCLV4ySuna0nWrdvYzo4JIt8+IvsQot1dGwPsL/1PbAo2omp7NNWkiFeTTNFJTGITBzzgph2pgwdt4mAyI6ndg0X5EV1Bomls8bB76K6Dhhhaeuch9v0TbvMsPyvpLc+In8rCfWFjhAu7vgyw/EGfeE8dNO79puziLw15j2lH69Cw0buOEKG3kpq8TSrwlaQnZEmgI/ENFEZQCn4njV5AGh9OtM3PeXgT/39Y4EPc3iSaYsTDq0T6LSgn9lZ1xdHluvXpEc+Bh4ne3UBi0JvVcyA+pM14WKarf/ftG+kcopCAU9APZyADBRiDMfJjAIMGNDc=); Raid BiS: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzEVEFIFF8Yn+/NuPP8/LOuzz///zgFTQvVujD6ZtaJdQl2FYLo5HqKLjnrju2G7m67S9hNw0MIqRhFmlRYYEReIkGirrJRyB6iDl7EWPISRAePEjMpSHpd+h2GN9/3vd/3e7/3+PA4hQAooEEIBiADBRgDuA3wBOA5APvHyxI3GwX1EaU0IKtFlOnblWal1oQS3Z0FlOi7TwGU6MNqAH30Vkb56keZzs+AsuFHia5/dJO1aUCZrr329sn0yzIo0zJK9H7VzX6459JM3AUU6cwIyrS2AEqlFQWU6OMVCHYGKtnQ+hTwnVTfnUWYBDKRnQWyk5oH31P7pf2t5wXISwtQM6aymzCR7aWeckjAG3LCsngkEjG4wTk3Ipahc8vi7lrnVoQbFSJWCWyRJR8ylNUGFOn2jaCMDSjqZoktA0vbheEr+UJZM7l5VjcMnZsxbTBj5646aS1f1Ox02klrqZtaOeNoxXzZLmfzOa3k2MXBjBYqOY7mDDsjTq5sD+vpQknfL9F/l3RcK+Vz7ep5PMdiGAj7KTBxCwRXCYKBreEWKrGGSZFQUfWhhMQsYUu4mfoYuSionlCDl9xyupZkXaqJ7eyMR+Q7QGQeQbS3a6Of/af+i03BRpRNl6aa9OLVJJNUEhPY+CEPuG5adfCgzTuYyEhq72BRfkqVkCgKWzzqHrrqoCGGhtp5hH3Hwm2u5ZcFteUV8VPRc9+z0eKeXd/7Wf6wT7y7Dhr3nym7/kdD3q2b0To0bHSvI0Tog6QibpMK/CDpcVHw0JH4CRIjKAR3SaMbEMaGEm3zcy7ex08OefgcNzeJImnx8CoR/grKif1VXXF6uW59ur1v/7NEz14gMeDO6jnwfoTNeFikq//3HhjpHKKQgAvQB5cgAwUYhVHyawCqijQJ).

**Points that do nothing for this spec:** **Anticipation** (3) and **Earth's Grasp** (2) only count toward the points the tree needs before **Toughness**; **Eye of the Storm** (2) only counts toward the points the tree needs before **Call of Thunder**; **Toughness** (4) only counts toward the points the tree needs before **Mental Quickness**.

## Other builds of this spec

- [Elemental — Raid](../research/raid/builds/elemental-ml-raid.md) (32/11/8, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5503331002001351-05500001-053-12)
- [Elemental (optimized)](../research/raid/builds/opt-elemental-dps-raid-dps.md) (31/11/9, 740 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5500331003011351-05500001-0522-12)
- [Elemental — Raid](../research/raid/builds/elemental-raid.md) (30/8/13, 717 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/550033100301135-053-05305-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows.*

