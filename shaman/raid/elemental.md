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
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Wyrmhide Spaulders](https://www.wowhead.com/forever/item=12082) · *quest: A Taste of Flame* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking* | [item 17721](https://www.wowhead.com/forever/item=17721) |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Greaves of Withering Despair](https://www.wowhead.com/forever/item=22240) · *High Interrogator Gerstahn, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Greaves of Withering Despair](https://www.wowhead.com/forever/item=22240) · *High Interrogator Gerstahn, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Greaves of Withering Despair](https://www.wowhead.com/forever/item=22240) · *High Interrogator Gerstahn, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18471) · *quest: Frost Shock and You* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Headmaster's Charge](https://www.wowhead.com/forever/item=13937) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzEVUFII1cYnv+9ceblt6TxWdpxWug00DYGRt9MnBJDIVEolPZiPBULrRMzmpSYpCYUe1PqoQhVaS/VCi22xWVZWRAWZO+7ZPewuJe9uLDBRfSysOvBve0uMxtBVq/Z/Q7h5X//+/5vvm+Ghx8wiIAGBsRgHApQhTmAXwH+AbgEwN8Kdom/mwT9jxBjEVUvosLuF7SDTpTZL1cBKdv+Dik7HEOV3V0G7WEYFfbXlLYXRspuTCFlS9+iwo4n/SMqa26BtqwiZc9dpGw+hzLbXPFZVqZRYU9KWqMbJZTZ39cg2h9pFGN3lkCc5EZ+24BFIAvF34Gc5NZA+de94h4OXQZ1cx0OrKViExaKwywQDBm4Tj50HJFIJCxhCSGshGOZwnGEvzaFkxBWg9BdAvvkfxU5qnoHUnb0U1TFDqSmXeNbwPNutfR9pVo3bGF/ZlqWKeyUMVFwy1Ne3qjMGG4+7+WN3M9GveAZM5W6Wy9WykbNc2cmCkas5nmGV/KmvXLdLZn5as08bTFftvT9UKuUe/Uv8HOewkg8zIDTfZB8JQgWdse7mMw7FilhVFdQRmLXsCv+NlM4+UrSA6GWqPnt7GaWD+g29vJPAyLlDJF9AVHr1N4of1d/BzujIVRtn2Y3G9R3s1zWSUri1ddkAfOfjz14OsLnz7kuTNtpw8iewErKSa5lZVJ8rMtINI1jS8/67a/5xkVvwUAb9KTQ0vsvCO/9eI8f+Jikd22TMKNB9kGIjgjCejTKK+c9E4Nt0Hj6kfAfXxkoBk072YaBIT+aGGF/ZjV6RBrwmOTnqRSgL3MMMicoRZ+RkF+Q5iYzPWurPm6lP5oMcC9tN4kmG+n4DpHeCOqZ01Vb8clW2+YMBr+j/2WGWoXMuH9BrELwR2qm45TtvDd85h4RkIQMfAkj8A0UoAqzMEteDACToVl2); Pre-BiS: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzEVc9rE1sUnnNnmrk5faTp7eO96bzHY17gPdPAtHcmjaRBSFoQRDdNV+LGTpppE2mT2ASpu1a7kIKtiIj9AUpVFDEIolL8A0p0IVmJ0IWhEiyiIC7qQhCZMYViu41+i8Odc88955vvm+Hi3xT8oIAGQRiGDBRgGuACwA2AuwDsN3eXOLtRUBe9lPpltYAy/VIGpd6KEj3/AFCi7644cbnqRw89l1He+NBDl8eUDR+K9FUKJVpfAJTp+qM255RMa2VQFmSU6NWqHyU6/96JT6p+FOmlCZRpfQWUSgcKKNHrjyHQ469kgy/mgW+nBi+uwhyQ2exlINupJfDctO5bb/vvgXxnBerGfLYGs9kB6vKGBDwl/0Qi3AyHDc4NbhjhiKHzSIRzzp1F2KgQsUpgk9yWkaGstqBIt84EZGxBUTeLrAwsbRXGT+YLJc3k5kHdMHRuxrSRjJUbs9NaflKz0mk7raXOaqWMrU3mS1Ypm89pRduaHMlowaJta/a4PWHnSta4ni4U9Z0S/XtJ96liPtelHsZDLIb+kI8CEzdBcJggGNgRaqcSa5kTCRVVD0pIzCK2h9qoh5GjguoSNXjRKafrSdarmtjFDriNPLsamfs0apzaGGJ/qL9ja8CLsum0qSbdfDXJJJXEBFb4SRJQ5/3o68+DbGaP6lw3I00Y2elKKTKSakgZ5f+pEhJFYdjgs/L8GFvd7yvobQKfGBpqzz7m/RXqdAw/IajtD4mPiq73rokR7pr1YYjl92rG+5rAcecnYad/GMj7dDPahIFex5ogodeSirhFKvCRpGdEwUV34hNIjKAQ+Eq8TkKYHk10Li06eBb/d9TFy7hZI4qkxUNrRPglKCV2Vk3F/+Wmzelz49CtRH8jkRh2rolFcB+EWjwk0rU/B3bdJhyikIAjMAjHIQMFmIIp8m0AImlb+w==); Raid BiS: [full raid](https://wowsims.com/forever/shaman/elemental/#eJzEVU1oG0cU3je71o6eiyyPS7veFroVtJUFa8+uvEUWBcmGQmkvlk+ll3plrSsVW1IlUdybXXwohtrG+SF2BAlOQkKILiEBJ7dcjJJA0CkXHyIcREwgEHJwDgETdiODiX1V8h2G2ffevPft9+0y+CWFICigQRgmIQtFmAf4D+AiwDUA9omXJW42BmrVT2lQVkso0zc1UFrdKNGDNUCJPj/trucbQfTRf7PK0wDK9N4qKDsBlOidJTfZWgGU6fatHvecTJs1UFZklOjDM272bCOIEl08BSjS1VmUaasKSr0PBZTohdsQGgrWc+FHy8D30+P/b8ISkMXcGpD99Ab4Ltk37Gej10G+WoWWsZxrwmJujHrMIQl3yVeWxaPRqMENzrkRtQydWxZ39zq3otyoE7FBYJdckZGhrHahSPf+DsnYhaJullkNWMYuzvxeKFY0k5vf64ahczOuTWXt/B9ORiuUNDuTcTJa+h+tknW0UqFiV3KFvFZ27NJUVguXHUdzZpxZJ1+xZ/RMsawflujvSgb/LBfyA+qP+AOLYzASoMDEXRBcJggG9kV6qcS6lkRCRdWHEhKzjL2RHupj5GdB9YgavOyW0+0UG1ZNHGDfeY18RxqZJzRqn9qZYJ+pn2J3yI+y6bZppLx4I8UklcQFVvxAElD3/eiT1+Ns4ZjqXDetDozs96QUGUm3pYzxb1QJiaIwbPOpPviFbZ70FQx3gE8cDXXoBPO+iPS7hv8mqL03SYCKnveeiRb3zHoxwQrHNeMjHeB4+JOwv94byEd0M9aBgX7XmjCh51KKuEfq8JJkFkTBw2DyFUiMoBA6IH43IMxPJ/s31l3cT3w97eFxwmwSRdISkS0ifBRUkoe7juLbWsfmjHjrxOXkaDuQnHRvinXwHoRmIiLSrc/HjlwoHGKQhJ9gHH6FLBRhDubI2wEAS2xcRA==).

**Points that do nothing for this spec:** **Anticipation** (3) and **Earth's Grasp** (2) only count toward the points the tree needs before **Toughness**; **Eye of the Storm** (2) only counts toward the points the tree needs before **Call of Thunder**; **Toughness** (4) only counts toward the points the tree needs before **Mental Quickness**.

## Other builds of this spec

- [Elemental — Raid](../research/raid/builds/elemental-ml-raid.md) (32/11/8, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5503331002001351-05500001-053-12)
- [Elemental (optimized)](../research/raid/builds/opt-elemental-dps-raid-dps.md) (31/11/9, 740 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5500331003011351-05500001-0522-12)
- [Elemental — Raid](../research/raid/builds/elemental-raid.md) (30/8/13, 717 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/550033100301135-053-05305-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

