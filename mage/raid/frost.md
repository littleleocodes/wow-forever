# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**[Frost — Winter's Chill and Cone of Cold](../research/raid/builds/frost-med-raid.md)** (18/0/33) — [open the talent tree](https://talentsforever.com/mage/60/2032250100003--053500001121331251-12)

## How to play

**Before the pull:** **Ice Barrier**, **Frostbolt**.

**Talents with no line below:** **Ice Block**: a defensive for emergencies, so it has no line.

**Then press the first one that is ready**, top to bottom:

1. **Cold Snap** when **Cone of Cold** is at least 7 seconds from ready; no global cooldown, so press it alongside the others
2. **Cone of Cold** when the target has exactly 5 stacks of Winter's Chill
3. **Ice Lance** when you have exactly 1 stack of Fingers of Frost and you are casting Frostbolt
4. **Ice Barrier** when Frigid Power has under 3 seconds left
5. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Evocation**: when you run out of mana (needed in about 1 of 12 fights)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid builds **Winter's Chill** on the boss with **Frostbolt** and spends it with **Cone of Cold**: every Frostbolt adds a stack, and at five stacks Cone of Cold deals twice its damage plus 35% of your spell damage, a quarter of the build's damage from one cast about every 15 seconds. **Ice Lance** takes the second charge of each **Fingers of Frost** proc, **Ice Barrier** keeps Frigid Power up, and **Cold Snap** buys one more Cone of Cold a fight. Cone of Cold is a cone in front of you: stand within 10 yards of the boss and face it (behind it, with the melee). 796 DPS in a full raid. This is the official simulator's own Frost build and list (wowsims/forever's Frost preset), which the page starts from since 2026-11-20.

**Why it works**

- **Frostbolt** is the base: 60 casts and 66% of the damage, at rank 10, the trainer's top rank. **Improved Frostbolt** takes its cast to 2.5 seconds, **Ice Shards** doubles its critical bonus and **Precision** adds 6% hit. With 5 points in **Winter's Chill** every Frostbolt that hits puts a stack on the boss: 20% more damage from your next **Cone of Cold** and 7% of your spell damage added to it, up to 5 stacks.
- **Cone of Cold** at five stacks (12 casts, 25% of the damage): twice its damage and 35% of your spell damage on top, and **Improved Cone of Cold** adds 35%. Its 10-second cooldown is shorter than five Frostbolts, so the list waits for the stacks, not for the cooldown. **Arctic Reach** stretches its reach by 20%.
- **Ice Lance** on the last charge of **Fingers of Frost** (6 casts, 8.5%): each chill has a 15% chance to give you two charges that make your next spells count as cast on a frozen target, which **Shatter** turns into 50% more critical chance. The first charge goes to a Frostbolt; the instant Ice Lance takes the second and adds a Winter's Chill stack of its own.
- **Ice Barrier** before the pull and whenever Frigid Power has under 3 seconds left (4 casts): 15% more Frost damage for a minute, and 5% more while the shield holds.
- **Cold Snap** once a fight, when **Cone of Cold** still has 7 seconds or more of its cooldown left: it ends every other Frost cooldown, so one more five-stack Cone. It also resets **Ice Block**, which this build takes.

**Caveats**

- Range: **Cone of Cold** reaches 10 yards in front of you (12 with **Arctic Reach**). Where you cannot stand that close or face the boss, it goes: cast **Frostbolt** instead, and the **Winter's Chill** points add nothing. The simulator's fights stand you at 10 yards.
- Our search's 17/2/32 (under Other builds) is 0.4% ahead in the same fights, under the 0.5% bar, and about 2% ahead in the Raid BiS set that was chosen for its talents (818 against 802), so the gear table shows it there. Which build is better gear by gear is settled in a later pass, each in a set made for it.
- Threat: this build has no **Frost Channeling**, so your Frost spells keep their full threat; **Arcane Subtlety** lowers Arcane threat only.
- Mana: below 5% the list uses your mana gem and channels **Evocation**. With a raid's mana buffs a 3-minute fight never gets there; a long fight does.
- Several targets: **Blizzard**, and **Cone of Cold** hits everything in the cone. The simulator's fights are one boss.

**When to change it**

- If you cannot stand within 10 yards of the boss: **Frostbolt** in place of **Cone of Cold**.
- Keep **Cold Snap** for a second **Ice Block** on a fight that needs one.
- When raid damage breaks the shield, recast **Ice Barrier** as soon as its 30-second cooldown allows: the extra 5% lasts only while the shield holds.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 18 | Wand Specialization 2 (tier point: needed to reach Arcane Subtlety), Arcane Resilience 3 (tier point: needed to reach Arcane Subtlety), Arcane Subtlety 2, Magic Absorption 2, Arcane Concentration 5, Arcane Geometry 1 (tier point: needed to reach Arcane Meditation), Arcane Meditation 3 |
| Frost | 33 | Improved Frostbolt 5, Precision 3, Ice Shards 5, Improved Blizzard 1 (tier point: needed to reach Arctic Reach), Ice Lance 1, Arctic Reach 2 (tier point: needed to reach Improved Cone of Cold), Ice Block 1, Shatter 3, Improved Cone of Cold 3, Cold Snap 1, Fingers of Frost 2, Winter's Chill 5, Ice Barrier 1 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** raced against a full search's best (2026-11-20, Frost — Raid: ours +0.36% and +0.54% on two seeds, 10,000 fights, a tie under the 0.5% bar).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 796 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 714 | its own set |
| Pre-BiS | 777 | its own set |
| Raid BiS | 807 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 59.6; Pre-BiS 62.2; Raid BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Boreal Mantle](https://www.wowhead.com/forever/item=11782) · *Warder Stilgiss, Blackrock Depths* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Coldtouch Phantom Wraps](https://www.wowhead.com/forever/item=13535) · *Baroness Anastari, Stratholme*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sorcerer's Bindings](https://www.wowhead.com/forever/item=226929) · *sold by Mokvar*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Sorcerer's Gauntlets](https://www.wowhead.com/forever/item=226930) · *sold by Mokvar* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Riptide Shoes](https://www.wowhead.com/forever/item=18307) · *Hydrospawn, Dire Maul*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Venomspew Footpads](https://www.wowhead.com/forever/item=275606) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* |

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Quests and dungeons: Enchant Weapon - Spell Power (Molten Core); Pre-BiS: Enchant Weapon - Spell Power (Molten Core); Raid BiS: Choker of the Fire Lord, Ring of Spell Power, Talisman of Ephemeral Power, Enchant Weapon - Spell Power (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVE1oY1UUznfvy8vJyZDJ3DqdlzujpjEdy8PKywtxJm6SDgqCSoq4EPxhEmxnAtYWdNFla4tI0bZUBBssSC1U6h/NqnZnIRARRDcKurBERLtSu+iyyn1JrIp0VzyLd8875zv3ft/H5fIVQgIOUhjCTdzGFGaA14B3gfcBdS7oCtO9Dt20iRKkJzhCmytwfoqxRXOfgCW9+gxb9PES2KYfas6PcY7QZ8twvo+zpOYtlrT4NNt0OG5mIjS3BGcpwpL+qLCk2SpLWp5gSWu32KbXJ5xWH0uaeZYt2ngL6fsSrdrQl4vwjqqjb6xjAWK+tgJxVK1D/DyyBdp8Bx8uYLG2j/naDQoYo4Rdkfazvu/nvazneZ4/7A97+Vze87ycqeRyWT+fbQl8JWJt8bXFD3FEh1nSwVi60BAPkFRuQ9xLUMmG6CcoqgvTbpY1bf2V1SMmOxjTNlsshrOc6+7SLKeHGmKQ5Gnj3SF1jx7ghBsnS4lqqLNVfrCNc8yPV16spJ6cnHzhJXVBn+dYA8QWre06Dh4MqStaB3O2km2EzLmMXBthliPlh1VK38UX3T6yFW2ZGm2XO5BrZqGdirqqM3zZTRJUfA8xlvReVYlE2IEBMPJmoe2y8vT9nFFp7nfvIKjoHuwOCdNnZJkOcaKIfv32UTWg7w7QloruBugPjke7/Lomq6juOeVI99o/pLIm4wJ9+vtj6k59+RU4LOnN5/QF9zzZgUcRDrMsFAbdt9ERayx03H6yVWzvxKMuwZ6OjE6fAupxN6ikuvTf3uV73l3Ufczf2eYWH4w5+LeqL8q/iBZ+E8/PylAQmdK6MYIFIX0soqYUmhkvJeurJj4vDowH8U3R3xeOlSq6OyL0v8TLpV52pnH1ozM7pxB8n9gojXQLpZvmSVtF8BPaL7qSdi7d+NvL5+E6SngEo3gKtzGFaUyLPwcAAAa3cw==); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVE1oY1UUznffy3snJ0Pmza3TebkzahrTsTysvLwQZ+Im6aAgqKSIC1cyDU6ZgHYKdtFl1S6kaFv8KTYqSC0o1SrNQmp3BgoRReJGQTclUrQiVLvoRihyXxKrIt2VOYtzzz3nO+ee71tcvkRw4CKFIVzHTUxiBngZeA/4EJBnwqrQ1atQX1tEDqkptunPdbi7cTbppU/BJv36hvZvtxy2qDnh/pRgm75YhPtjgg1qTLBJuwtgiw7GdZdNS3uOu2CzSfO/OWzSUkv7z1oOG7T4HNu0/wncZh+b9MqCHrz6JtL3Oc3q0Dfz8A8ro6+uYA5itvoaxGGlBvHzyBrog3fw8RzmqzuYrV6jcHGUsCXSQTYIgryf9X3fD4aDYT+fy/u+n9OZXC4b5LNNgZaIt8W3Jj/EtoqyQXs30oW6eIAM6dXFvQSZrIt+gqSa0OXtsqK1v6OaraO9G8pik8VwlnPdKdvl9FBdDJJxUnu3Sd6jBtjxEmRKUYl0RuUH2zjD/PjYxFjqyVu3nn1enlNnOV4HsUnvbrkuHozIS0qFfZY02ojodxm5NqJsjJQflil1F5/3+siStKZztFHuQK7ogzbH5GWV4YtekiATDcTZoPcrUjhRFxrAyOuDNsrSV/dzRqa537uDIGMNWJ0ldJ2RZTrAMSPa//5ROaDuDtGmjG2F6I+ORrv7dUWWMdVTyjW8K/+iyoq0CvT5H4/JO9XFF+GyQa8/rc55Z8kKNbI5ykahMOi9hQ5ZLaHr9ZMl441jjboL9nhkVPoEUG93jUrKC/+vXb6n3XnVx/yDZYdkXPyX1VflX0QTv4tnXjAioWVKK1oIFoT0kYjpVGRmvJSsLWv7sjgwHtp3xWBHuGaq6G2KyG2xqVIvOlW7vH5q7xRC/8RqaaSbKF3XP9sywktkp+gZtHnh2j8+QB9XUcIjGMVTuIlJTGNa/DUA8Gm7/g==); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVEFoY1UUzXn/5/+bm2nmz6vT+XkzahrTsXys/PwQZ+Im6aAgqKSIC1cyDc4wAZkZUHCWo3QhA06htWKjgtSCUm2hWUjbZaEQKWjcWNBNiRStFGoLdiMUeT+JVZHuytzFfffde+5995zF4wsEBy5SGMRV3MBt3AXeBT4FvgDkqbAqdPUy1HcWkUPqLbbpz3m4W3E26XACbNJv72v/UdNhixo33Z8TbNPeTo/7U4JN2t/pYZO2xsE2/bHTo/ts2piHO26zSR80HTZpfUoPGJvU/uumwzbtLsBt9LJJyws6OTuF9BNOozr47X34B5WR92ZwD2KsOgFxUKlB/DI8B/r8Y3x1D/ermxirXqFwd5SwItJBNgiCvJ/1fd8PhoIhP5/L+76f05lcLhvksw2Bpoi3xPcmP8O2irJB29fShbp4igzp1cXjBJmsiz6CpJrQ5bWyorm/o5qto+1rymKTxVCWc50pa+X0YF0MkHFce6dJPqb62fESZEpRibRH5QdaOMX84ujN0dTLt269/oY8o05zvA5ikz5ZcV08HZEXlAr7LGm0ENHvMnItRNkYLj8rU+oRPuv1kiVpTudosdyGXNIHLY3KiyrD570kQSZWEWeDPqtI4URdaAAjrw9aLEtfPckZmeY+7yGCjK3Cai+h64ws0z6OGNHuxvOyXz0aok0ZWwnRXx6OdPbriCxjqquUa3iX/kWVFWkVaHnvBfmwOv8OXDZo8lV1xjtNVqiRzVE2CoUB70O0yWoJXa+PLBlfPdKos2CXR0aljwF1d9eopDz3/9rlu9qdVb3MP1p2SMbFf1mtl38VDfwuXnvbiISWKc1oIVgQ0ociplORu9dLydq0tm+K/ddD+6EYbArXTBW9JRF5IPZmqRudqF2cP7F3CqF/abY03EmUrurPbRrhJbJZ9AxaOnflH3+gj8so4TmM4BXcwG3cwR3x1wAlv76C).

**Points that do nothing for this spec:** **Arcane Geometry** (1) only counts toward the points the tree needs before **Arcane Meditation**; **Arcane Resilience** (3) and **Wand Specialization** (2) only count toward the points the tree needs before **Arcane Subtlety**; **Arctic Reach** (2) only counts toward the points the tree needs before **Improved Cone of Cold**; **Improved Blizzard** (1) only counts toward the points the tree needs before **Arctic Reach**.

## Other builds of this spec

- [Frost — Raid](../research/raid/builds/frost-ml-raid.md) (17/2/32, 800 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0412152000002-2-053500030100331251-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows.*

