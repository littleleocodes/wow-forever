# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**[Frost — Winter's Chill](../research/raid/builds/frost-winters-chill-raid.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/mage/60/041215203000201--25353003002100105-12)

## How to play

**Press the first one that is ready**, top to bottom:

1. **Arcane Missiles** (rank 7) when Missile Barrage is active
2. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**
- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid is one spell and one proc: **Frostbolt** on every cast and a free, fast **Arcane Missiles** whenever **Missile Barrage** lights up, with **Presence of Mind** at the pull and one **Fire Blast** in the last 3 seconds. It is the weakest mage page in the simulator (526 DPS in a full raid against Fire's 869): the search's best Frost build, 612, fails the spec's signature rule and sits under Other builds.

**Why it works**

- **Frostbolt** is the list: 62 casts and 76% of the damage in a 3-minute raid fight. It casts in 2.5 seconds with **Improved Frostbolt**, costs 260 mana at the rank the list names (rank 10) less **Frost Channeling**'s 15%, crits for double with **Ice Shards**, and every one that lands has a 20% chance (**Missile Barrage**) to make your next **Arcane Missiles** free, half as long and twice as dense.
- **Arcane Missiles** on a **Missile Barrage** proc comes first: about 10 casts and 23% of the damage, each a 2.5-second channel that costs nothing, with **Arcane Impact**'s 6% crit. **Improved Channeling** at 4 points gives an 80% chance that a hit does not cut it short. The list names rank 7, as the simulator's rotation has since October; a free cast costs the same at any rank.
- **Fire Blast** only in the last 3 seconds (about one a fight): a **Frostbolt** started then is still in the air when the boss dies, while **Fire Blast** is instant. Earlier in the fight the search kept it out: it rolls for no proc, costs 340 mana against the **Frostbolt**'s 260, and no talent of this build improves it.
- **Presence of Mind** at the pull makes one **Frostbolt** instant; its cooldown is 3 minutes, so a 3-minute fight gets one.
- Mana is not a problem with a raid's buffs: the full list uses your mana gem (from **Conjure Mana Ruby**) below 80% mana and **Evocation** below 20% with more than 25 seconds left; the simulator used the gem in about one fight in six and never channeled **Evocation**. **Arcane Concentration** makes one cast in ten free and **Arcane Meditation** keeps a third of your regeneration going while you cast.
- **Winter's Chill**, the build's name, no longer helps this list: since the 2026-11-02 patch its stacks only make your next **Cone of Cold** hit harder (20% more damage and 7% of your spell damage per stack, up to 5), and no single-target list casts **Cone of Cold** on a boss. **Frostbite** does nothing on a boss either: bosses cannot be frozen. The build is a hand draft from before the change and stays until a Frost build that passes the signature rule is found.

**Caveats**

- The 612-DPS Frost build under Other builds (from the machine-learning search) takes Arcane Blast, Ice Lance, Shatter and Fingers of Frost in place of Winter's Chill, Ice Block, Presence of Mind and Arcane Meditation, and plays a longer list: two stacks of the Arcane Blast buff kept up and Ice Lance on a Fingers of Frost proc. It fails the signature check because Frost's own spells carry 53% of its damage, under the 60% the rule asks for (Arcane Blast and **Arcane Missiles** carry the rest). If the rule does not matter to you, it is 16% more damage.
- Several targets: **Blizzard**, **Cone of Cold** (five **Frostbolt** hits first: five **Winter's Chill** stacks double its damage and add 35% of your spell damage) and **Arcane Explosion**. The simulator's fights are one boss.
- Moving: **Fire Blast** is this build's only instant ranged attack (it takes no Ice Lance), and **Presence of Mind** makes one **Frostbolt** instant.
- Threat: **Frost Channeling** and **Arcane Subtlety** cut your Frost and Arcane threat by 30%; the simulator ignores threat, so give the tank a few seconds on a fresh pull.

**When to change it**

- In the last 3 seconds, **Fire Blast** instead of a **Frostbolt**.
- Without a paladin's or shaman's mana buffs, the simulator's list for playing alone channels **Evocation** only below 5% mana and with more than 50 seconds left, not at the raid list's 20%.
- On a pack, five **Frostbolt** hits and then **Cone of Cold** use the **Winter's Chill** stacks this list otherwise wastes.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 21 | Arcane Resilience 1, Improved Channeling 4, Arcane Concentration 5, Arcane Subtlety 2, Magic Absorption 1, Missile Barrage 2, Arcane Impact 3, Arcane Meditation 2, Presence of Mind 1 |
| Frost | 30 | Frost Warding 2, Improved Frostbolt 5, Precision 3, Frostbite 3, Ice Shards 5, Frost Channeling 3, Arctic Reach 2, Ice Block 1, Cold Snap 1, Winter's Chill 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 526 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 605 | [21/0/30](https://talentsforever.com/mage/60/0502251031001001--2535120301203012-12) |
| Phase 1 BiS | 620 | [21/0/30](https://talentsforever.com/mage/60/0502251031001001--2535120301203012-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 58.9; Phase 1 BiS 61.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellpower Goggles Xtreme Plus](https://www.wowhead.com/forever/item=15999) · *Engineering*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellpower Goggles Xtreme Plus](https://www.wowhead.com/forever/item=15999) · *Engineering*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Earthen Silk Slippers](https://www.wowhead.com/forever/item=254013) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Earthen Silk Slippers](https://www.wowhead.com/forever/item=254013) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Blessed Band of Light](https://www.wowhead.com/forever/item=272407) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* |
| Ranged/relic | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV1oHFUUx/fcmd29eyrZ9Vbr9JqH20DKunTk7my3bIO4kzypQRJ8Eh+0d3cn2ZEws8zM2hZEorQgAVPQSmmsIKVF8euhD9IGCiUgrIISBK3gS6gWRYT6FHzxg5ndNYG8mngYDvf+//cwv3NmmMFRCgUwQEARTkAbOrAI8DrAewAfALD7EpfEbg34N5TSAuUhZujfLxt396FO71wA1Omv5+P8znoBM7TnGT+OYJauXQXjhxHU6JqHOr17DjBDb3lxVZbevJU3zmVRp8u/FVCnF9bj/FmS/7yUxyy99ykYvf2o0bOPoU6vvA1jRwo9t/j1MsjNxuwbl2EJyBn3TSCbjRUgP09+CPT9S/DxEiy7G3DGnaIJN9iwSsZkVVpWtSwrZSnjyzStaqVatmRFDlKPwDrZd4d8n2EfATsLqtVyWsKS1jFTHjet2oSYDJrKc8TTbhi6C04ofE+o4U5MqSBQ847oBH7ziJjvqiAub5wWqhuoJ8Npzz/pidAXSjS67kJLnHSjtt+NdtR7zktOIJoqjELhRvwQGuwA5r7UM6jTr24YmLsGgyVPo0Z/mmFXgSnVWXjB70R93LI0rcqEaLaVN++0hB+Ifi+N0yJqOyLwIxW5vidCRwXNtiiGjiPmAj+MzEC5LXPom33/0RdD33uE23iMH0VeMqjGcqsJw80bBs+tkHh5/ttpPFB6IPbW/vXSqCFYfOCzUc7x/lKe6ow0UjyLadRqcjzuotB7nOmcTKRYhZexyA4n57Stc5YcT6Q0I08NpWoYl9K3nmeLezKAhxOCzDYCGSa9vfbHLHuQ7x8+mXdXjUS+d3uavbITTFr/NdhBLJRGBmAZ1JFU+pP5fIYtwV4AjONoiccAz6U4u0byVNsaUrksE5jbM4b2C+nB78R6VUslcdS+HL8qSCiM/UVysZRanLMPrlyM44v6obkkvqtbG8TQRb10naT+l4js4WpX4/Anu3af40l+5oo9ORDsE/H3/SIkm9RGvaTR6w9NbfsNSKiBDU/ALDwLbejAKThF/hkAdftG2w==); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV1oHFUUx/fcmd29eyrJeqt1es3DbSBlXTpyd7ZbtkHcSZ7UIAk+iQ/au7uT7EiYWWZmbQsiUVKQgC20zUOjgpQWxa+HPkgbKEhAWBUlIFpBhKAWxZf6VHyKMrO7SSCvJh6Gw7nnfw7zO2eGGRyhkAcDBBTgFLSgDQsAbwK8B/ABAHsgUUmsVoF/RynNUx5hhv7zqnH3AOp08yKgTv+8HPu31/OYoV3P+HUIs3TtOhg/DaFG1zzU6d0LgFn68zLEbVl6+/Nh40IWdfr1Mmz5z9bzqNPFS3HlvU/B6B5EjZ57AnV6bRlGj+W7buHb8yDv12feugpLQBbdi0Du11eA/D7xIdD334GPl+C8uwGL7iRNwMGGVTIqK9KyKiVZLkkZX6ZpVcqVkiXLsu+6BNbJgV/Ijxn2EbBzoJpNpyksaZ0w5UnTqo6LiaChPEc864ahO++EwveEGpzEpAoCNeeIduA3jom5jgri9vpZoTqBejqc8vzTngh9oUS94843xWk3avmdaFe/57ziBKKhwigUbsSPoMEOYe4rPYM6/eaWgbkb0A95GjX62zS7Dkyp9vxLfjvq4ZakaZXHRaOlvDmnKfxA9GapnxVRyxGBH6nI9T0ROipotEQhdBwxG/hhZAbKbZoD3ezpj78c+t5j3MYT/DjyokE1lltNGG7fMnhuhcTh5e+n8FDxoVhb29LSqCFYvK+zEc7xweIw1Rmpp3gW06hV5Vg8Rb77JNM5GU+xMi9hgR1N6rTtOkuOJak0I88MUpUwbqWXXmQL+7KARxOCzA4CGSazvfH3DHuYHxw8mXdXjSR9784Ue203mLT+a7DDmC8O9cEyqCMp9zbzxTRbgv0AGMORIo8BXkhxdoMMU217SaWSTGDuTBvaH6QLfxHrdS2V2HH7avyqIKEwuklycSq1MGsfXrkS25e1I7OJ/VCzNoihi1rxJkn9LxbZg2hP7egne3afk4l/7po90U/Yp+IP/BVIDqmNWlGjNx+Z3PEfkFAFG56CGXgeWtCGM3CG/DsAKhJGaw==).

**Points that do nothing for this spec:** **Cold Snap** (1) only counts toward the points the tree needs before **Winter's Chill**.

## Other builds of this spec

- [Frost — Raid](../research/raid/builds/frost-ml-raid.md) (21/0/30, 612 DPS in a full raid; fails the signature-spell check: core share 53% under 60% (Frostbolt, Ice Lance, Frost Blast, Cone of Cold, Blizzard)) — [open the talent tree](https://talentsforever.com/mage/60/0502252031000001--2535300301203012-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

