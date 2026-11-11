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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 514 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 605 | [21/0/30](https://talentsforever.com/mage/60/0502251031001001--2535120301203012-12) |
| Phase 1 BiS | 620 | [21/0/30](https://talentsforever.com/mage/60/0502251031001001--2535120301203012-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.0; Phase 1 BiS 61.3; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Blessed Band of Light](https://www.wowhead.com/forever/item=272407) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Skull of Burning Shadows](https://www.wowhead.com/forever/item=13524) · *Maleki the Pallid, Stratholme* | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* |
| Ranged/relic | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV+IG1UUxnPuTJKbU9kdb7VOr/twu7Alho7cTJqS7oOZ3Sd1kV18Eh+0N8lkM7LOhJmJbV9k1Qqy4FZqRboqSGmp+Bf6IO1CQRaEKChB1Aq+LGpRRKj4UHwSmUliC3217WE43Pt99zC/c2aYwSkKBpggoAiHoANdWAV4BeBdgPcA2F2pSxK3BvwbSqlBeYR5eu4EmFd2oE5f+gRQp7+fTPJbAwNztO+bP09gnm6dBfPHCdTolo86vXIcMEf/aidVeXrps0nzeB51uv6HgTp9c5DkTwcGavS1ZzFPr34MZn8navRbD3V65g2Y3mf0veLX6yCvNZZePQ1rQI55J4Bca2wA+XXufaDn3oYP12Dd24Zj3jxNucGBTTItq9K2q2VZKUuZXJZlVyvVsi0rcpT6BAZkx0/khxz7ANjLoFottyVsaR+w5EHLrs2KubCpfFc85kWRt+JGIvCFGu/EvApDteyKbhg094nlngqT8sZRoXqheiRa8IPDvogCoUSj5620xGEv7gS9+KZ6333ODUVTRXEkvJjvQZPtwsKXeg51+tVFEwvnYbTkWdToL4vsLDCluitPB914iFuWll2ZFc2O8pfdlghCMeylcVTEHVeEQaxiL/BF5Kqw2RHFyHVFOwyi2AqV17LGvjX0H3wmCvwHuIMH+H7kJZNqrLCZMly6aPLCBkmWJ79bwF2lexJv6z8vixqCzUc+m+Ic7y5NUp2RRobnMYtaTc4kXRj9h5jOyWyGVXgZi2xvek67fs6WM6mUZeTRsVSNklL6+lNs9bYM4P6UIHcDgYzS3l78e4ndy3eOn8w7m2YqX728wJ6/GUza/zfYbjRKEyOwHOpIKsPJfL7I1uB2AMzgVIknAE9mODtPJql2fUjlskxhLi+a2m+kD38S+wUtk8Z+53TyqiChMP0PKSRSZrXt7N44lcQX9T3tNL6v29vE1EW9dIFk7kjEznh1S2PvR7fsPgfT/PgZZ24kOIeS7/spSDeZ7XpJoxfum7/hNyChBg48DEvwBHSgC0fgCPl3ABwVRk4=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElV9oHFUUxvfcmd29eyrJeqt1es3DbSBlXTpyd7ZbtkHcSZ7UIAk+iQ/au7uT7EicWWZmbfsiUVKQgK2kzUOjgpSWiv8e+tQGChIQVkUpiFYQIahF8aU+FZ+CzOxuEsiriYfhcO/33cP8zplhBkco5MEAAQU4BS1owwLA2wAfAnwEwB5KXBK7VeDfU0rzlEeYpdeXwbh3AHW6uQyo078uxfm9O3nM0K5n/DaEWbp+DYyfh1Cj6x7q9N4FwCz9ZSUpy9LbXwwbF7Ko029WYCsvXgTU6LuvYZbe/xyM7kHU6LmnUKdXV2D0WL7rFr47D/JBfeadK7AEZNFdBvKgvgrkj4mPgV5/Hz5dgvPuBiy6kzQBBxvWyKisSMuqlGS5JGV8maZVKVdKlizLfuoSuEMO/Ep+yrBPgJ0D1Ww6TWFJ64QpT5pWdVxMBA3lOeJ5NwzdeScUvifUYCcmVRCoOUe0A79xTMx1VBCX188K1QnUs+GU55/2ROgLJeodd74pTrtRy+9Eu+o953UnEA0VRqFwI34EDXYIc1/rGdTpt7cMzN2A/pKnUaO/T7NrwJRqz7/it6MebkmaVnlcNFrKm3Oawg9Er5f6WRG1HBH4kYpc3xOho4JGSxRCxxGzgR9GZqDcpjnwzZ7/5Kuh7z3BbTzBjyMvGlRjubWE4fYtg+dWSby89MMUHio+EnvrW14aNQSL9302wjk+XBymOiP1FM9iGrWqHIu7yHefZjon4ylW5iUssKPJOW37nCXHEinNyHMDqRLGpfTiy2xhXwbweEKQ2UEgw6S3t/6ZYY/yg4Mn88Gakcj3706xN3aDSeu/BjuM+eJQHyyDOpJybzJfTrMl2A+AMRwp8hjgpRRnN8gw1baHVCrJBObutKH9SbrwN7He1FJJHLevxK8KEgqjmyQXS6mFWfvw6uU4vqodmU3ix5q1QQxd1Io3Sep/icgerPY0jn62Z/c5meQXrtoTfcE+FX/gL0OySW3Uihq9+djkjv+AhCrY8AzMwIvQgjacgTPk3wEAN29FkQ==).

**Points that do nothing for this spec:** **Cold Snap** (1) only counts toward the points the tree needs before **Winter's Chill**.

## Other builds of this spec

- [Frost — Raid](../research/raid/builds/frost-ml-raid.md) (21/0/30, 601 DPS in a full raid; fails the signature-spell check: core share 53% under 60% (Frostbolt, Ice Lance, Frost Blast, Cone of Cold, Blizzard)) — [open the talent tree](https://talentsforever.com/mage/60/0502252031000001--2535300301203012-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

