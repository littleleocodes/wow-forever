# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-ffb-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-5550000123011303-2035010311013002-12)

## How to play

**Before the pull:** **Pyroblast**.

**Talents with no line below:** **Ice Lance**: taken because Fingers of Frost requires it.

**Then press the first one that is ready**, top to bottom:

1. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 5 seconds left and either the target has fewer than 4 stacks of Fire Vulnerability or you are not already casting Scorch
2. **Pyroblast** when you have exactly 3 stacks of Heating Up and you are not already casting Pyroblast
3. **Fire Blast** when you have fewer than 2 stacks of Fingers of Frost
4. **Frostfire Bolt**

**Frostfire Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire list whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost, so both trees' talents apply, its chill rolls **Fingers of Frost**, and its crits stack **Heating Up** for a 1.5-second **Pyroblast**. **Scorch** keeps Fire Vulnerability at 5 stacks and **Fire Blast** goes out on cooldown. **Ice Lance** is in the build only because **Fingers of Frost** requires it: the list never casts it. It is the official simulator's own Frostfire build and list (its FFB preset) since 2026-11-20; our tuned list was 0.46% ahead with these talents, under the 0.5% bar. In a 3-minute raid fight: **Frostfire Bolt** 40 casts, **Fire Blast** 21, **Pyroblast** 13, **Scorch** 13, **Evocation** 1; **Frostfire Bolt** 40% of the damage, **Pyroblast** 23%, **Fire Blast** 17%, **Ignite** 14%, **Scorch** 6%. 781 DPS in a full raid, 10% behind the Fire page.

**Why it works**

- **Scorch** comes first: with **Improved Scorch** each one adds a stack of Fire Vulnerability, 3% more Fire damage from you for 30 seconds, up to 5, and **Frostfire Bolt** counts as Fire. The list casts it while the boss has fewer than 5 stacks or they have under 5 seconds left, and from 4 stacks on never twice in a row. Trinkets and the other cooldowns wait for the fifth stack.
- **Pyroblast** at 3 stacks of **Heating Up**, never twice in a row: each crit of **Frostfire Bolt**, **Fire Blast** or **Scorch** takes 25% off your next Pyroblast's cast (the stacks last 20 seconds), and each **Fire Blast** that hits adds a stack of its own, so three stacks turn 6 seconds into 1.5. One full cast before the pull, timed to finish as the fight starts.
- **Fire Blast** whenever it is ready, every 6 seconds with **Improved Fire Blast**, except while both charges of **Fingers of Frost** are up. A proc (15% on each chill; every **Frostfire Bolt** that lands is one) treats your next 2 spells as cast on a frozen target, where **Shatter** adds 50% crit chance. Holding the instant **Fire Blast** sends the first charge to a cast spell: a **Frostfire Bolt**, whose critical bonus **Ice Shards** doubles, unless a **Scorch** or **Pyroblast** is due; with one charge left, **Fire Blast** may take it. **Incineration** gives **Fire Blast** 10% crit.
- **Frostfire Bolt** fills the rest: 2.5 seconds with **Accelerant**, 370 mana less **Frost Channeling**'s 15%, **Critical Mass**'s 6% crit and **Ice Shards**' doubled critical bonus; each crit adds **Ignite**, a **Heating Up** stack and **Master of Elements**' refund. Its 40% slow is the chill that rolls for **Fingers of Frost**.
- **Ice Lance** has no line: the talent is the point **Fingers of Frost** requires, and the charges go to your Fire and Frostfire spells.
- **Fire Power** adds 3% Fire damage per Fire effect of yours on the target, up to 12%: Fire Vulnerability, **Ignite** and **Pyroblast**'s burn count; **Frostfire Bolt**'s own burn, a mixed school, does not.
- Mana: **Evocation** when your mana falls below a **Pyroblast**'s 440, channelled back to 99%; its 8-minute cooldown makes it once a fight, and even with the raid's mana buffs the simulator channels it in every 3-minute fight. The rest comes with the cooldowns (two mana potions, your Mana Ruby from **Conjure Mana Ruby**, a Demonic Rune) and from **Master of Elements**: its one point refunds 10% of a spell's base cost on each Fire or Frost crit.

**Caveats**

- Fire Vulnerability is yours alone: in Forever it raises the Fire damage you deal (in Classic, everyone's), so another mage's **Scorch** does not hold your stacks; the simulator's raid debuffs bring none.
- **Fingers of Frost** charges go to your next 2 spells, whatever they are.
- Moving: **Fire Blast** is your only instant here; a 1.5-second **Scorch** or a 3-stack **Pyroblast** fits a short stop. Packs: **Flamestrike** and **Blizzard**; the simulator fights one boss.
- **Frostfire Bolt** is new in Forever: its numbers are the simulator's model, not measured in game. Against Fire resistance it keeps its damage (the lower of the target's Fire and Frost resistance counts), while **Fire Blast**, **Scorch** and **Pyroblast** lose some.
- The setting: a full raid, every raid buff and debuff, **Mage Armor** on.

**When to change it**

- The list has no end-of-fight rule: in the last 3 seconds a **Frostfire Bolt** (2.5 seconds plus its flight) may land after the boss dies; **Fire Blast** if it is ready, else **Scorch**.
- Out of mana with **Evocation** spent: **Scorch** (150 mana, half a **Frostfire Bolt**) keeps Fire Vulnerability and **Heating Up** going until a potion or your gem is back.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Fire | 29 | Incineration 5, Accelerant 5, Ignite 5, Pyroblast 1, Improved Fire Blast 2, Improved Scorch 3, Heating Up 1, Master of Elements 1, Critical Mass 3, Fire Power 3 |
| Frost | 22 | Frost Warding 2 (tier point: needed to reach Ice Shards), Precision 3, Ice Shards 5, Improved Frost Nova 1 (tier point: needed to reach Fingers of Frost), Frost Channeling 3, Improved Blizzard 1 (tier point: needed to reach Fingers of Frost), Ice Lance 1 (needed for Fingers of Frost), Ice Block 1 (tier point: needed to reach Fingers of Frost), Shatter 3, Fingers of Frost 2 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a short check on 2026-11-20 (the simulator's build; every one-move and chain-move neighbour raced in a full raid, two rounds; nothing better). A full search, talents and rotation in turns until stable, follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 781 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 701 | its own set |
| Pre-BiS | 789 | its own set |
| Raid BiS | 807 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.2; Pre-BiS 61.9; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Netherflame Cuffs](https://www.wowhead.com/forever/item=254065) · *Tailoring*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Don Mauricio's Band of Domination](https://www.wowhead.com/forever/item=22433) · *Darkmaster Gandling, Scholomance* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Tracker's Signet of Brilliance](https://www.wowhead.com/forever/item=275973) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Flarethorn](https://www.wowhead.com/forever/item=22266) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* |

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Quests and dungeons: Enchant Weapon - Spell Power (Molten Core); Pre-BiS: Enchant Weapon - Spell Power (Molten Core); Raid BiS: Choker of the Fire Lord, Flarecore Leggings, Ring of Spell Power, Talisman of Ephemeral Power, Enchant Weapon - Spell Power (Molten Core)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVE1IXFcUnu/eNzNnzvgzXlv7eutCx1r1VeHNjAPqZkah1LYWpatSabG2qFPa6sK2Lm1roQhVma6UClYChhAjmI0zOwcCk01IskgWWSgmIVlkobMQzCKE92YmugjuJB+8e+853/2+++65cLieEIKJBrRiBBOYwizwN7AGXAZUhcsKh+2CPvQShUhPsZ820jAfB9mgP7fABq2lnfHaIthPdxZhPqxiP+0uwXxQxZJujLOkhWH2UWHMUfkoM2Eu+tmg/131X89CLGnpJ5a0Os5+er4JM1/Lkma/ZkmPhsPtoXyq9dYC7OPRoX/WMQ8xl0pDHI+uQDzpvQLa+A9X57GQ2sdcqo/cn0YSWRHu6IzHbdu2I9GY+8U6onYsbtuRmB2JRGK2Hc0L3BbBA3Ei+X0m7WODTtIIm9vibZIqsCJKGYdh0RFRzbqJa60akkp85dGBgixtOECQAx/9Ovndt9OpyZ/Vb/oX/lH9wD26i7VlklSVOTAbtHUdSoSE9rJkxMtc9nVcu7bO0XZyRZiZCvCypL1BR0R7gyqsG7je0gRVnUPFqchEybbHo+I6xm2qheustwgqkINzh6OMWdwR48pwkAMFnLm6M6sm3cimVUdSBXMgNmg1a5Zto85E9wcV62IVd3OfmdJax9mifKI/5nqli/7brn82/zkH7hrOMnM0EG0pvUHmaIDf+wMmS/r3G11jVZNPiVGP9rOXZXd3s/pU9/OHuq1o9UpfDNdRDk8POcfrqcjjUHz/u/S46Ey6ehaE8AsRcFKe2bHkuyvLDm4mGsdc3EtE94VpNCSsHeF5I5hOllcXig82L+ycbnf84lKyt5RIjjjdZxlu4NlPWJJ23uk706RsdCGJfgzhS0xgCjOYES8HANvisUI=); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVE1IXFcUnu/eNzNnzvgzXlv7eutCx1r1VeHNjAPqZkah1LYWpavSQrG2iFNalWJbl7Z1UaRVsSGgSSBIICHECAaCMztnNdmEIYtkkYViIgkhkDgLQQIhvDcz0UVwJ/ngnXvP+e733XfvhcP1hBBMNKAVwxjDJGaAf4CLwBVAVbiscNgu6IKXKET6V/bTizWYe0E26O91sEFPzjjxXD7EPsqNmw+q2E9bizDvV7Gk7DgbtLcA9lFh1FH5KD1mLvjZoPmnITbobN6JN/MhlrT4C/vp2XWYuVo26N8FsKSH34bbQ7lU6+152AcjQ/+tYg5iNrUEcTCyAvGo9yro8nlcm8N8agezqT5yfxtJZES4ozMet23bjkRj7hfriNqxuG1HYnYkEonZdjQnkBfBXXEo+UMm7WODDpcQNjfEuyRVYEWUKg7DoiOimnUT11o1JJX4xqMDBVlasIsgBz75feKH76dSE+PqD/0b/6x+4h7dxdoySarKLJgNWr8BJUJCe1ky4mUu8yauXVsnaDu5IsxMBXhZ0vagI6LtQRXWDVxvaYKqzqLiSGSiZNvjUXEd4zbVwnXWOwQVyMI5w37aLK6IcWU4yIECjh3dGVWTbmTTqiOpglkQG3QhY5Zto85A9wYV6+ItbmW/MKW1iuOX8pn+lOuVLvpvuP6Z3JccuGM40/T+QLSl9Abp/QH+4C+YLOn/73SNVU0+JUY82s9elt3dzepz3c8f67ai1Wt9MV1FOT3a5ASvxyKH5+LHP6XHRWfS1bMghF+KgFPyzIwm319ZdnAr0Tjq4m4iuiNMoyFhbQrPW8FUsjw7VXy0dmr7dLvxq0vJ3lIhOez0n2W4iWcnYUnafK/vWJuy0YUk+jGErzGGSUxjWrwaAFt2s5o=); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVE1IW1kUznffS3Jy4k+8zjhv7rjQOI76RuElMaBuEoVhnBkHZVbDDAyOLWJKq0Jt69IWF0WoFq0LbQtFCi2lWrAbk1WbVUqhSBftohTFVlq6aWNBkIKU95Koi+JO+sE7957z3e+7794LhysJARioQj16MYBhjAEXgRvAbUAWOayw2Raoj26iAKnT7KVPizA2/azT7jRYp3dX7Hh1NcAeygwar0rYS9kHpcaLEtYoPcg6bU6BvfRy1pF5KDlgTHlZp8ez2IvjM2CNLp9iL71fgpEpZ52SS3bt9b/BxkAmUf9kEtZ2X8+lBUxAjCemIbb75iHetN8B3bqGuxOYTKxjPNFBzn8jjpQINjVHo5ZlWaFwxPkiTWErErWsUMQKhUIRywpnBFaFf0PsaPwjk/KwTjvTCBrL4lvSpG9e5Cs2w6IpJGtVDZebZaRJ8Y9L+ba0/IIN+Nn3y9mhY/+PJIYG5Tl1hk/KE9ymWliZBmmyOA1mne7dhxQBodysMaIFLvUlrlGZh2ibuSjITFtws0Zr3baI1rplUFVxpakIsjSNon2Rgbxtm0tGVYQbZB1XmN8QpC8N+wzZpJFbEeHioJ99WzhwdHuUNaqaDbOCNOlPg1in6ymjYBu2B3reLVnlbvFh+g9DMxdw8FJ+U79ypVQ5/2XHP5X5k31PdXuazHaF6/JvkMx28Q8XYLBGM/+pMrOUPFL0uZSX3ay1ttbK31Un/6waclZ7+ly6gEK6v8khXm9FBh/E8fOay0Fz3NGzIAR3hc8uucb649/Pz9l4FKvud/AsFl4Xhl4VM1eE66tgJF6YHSl+WjyyfVqd+NfNeHu+EO+1G9AcnMS1HjM1Wvmu40CfstCCODrRg78xgGGMYlR8HgCkBrQU).

**Points that do nothing for this spec:** **Frost Warding** (2) only counts toward the points the tree needs before **Ice Shards**; **Ice Block** (1), **Improved Blizzard** (1) and **Improved Frost Nova** (1) only count toward the points the tree needs before **Fingers of Frost**; **Ice Lance** (1) is needed for **Fingers of Frost**.

## Other builds of this spec

- [Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md) (0/29/22, 778 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3550000123013303-2135000301113002-12)
- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 768 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-3550010113013303-2135000301113002-12)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (7/31/13, 704 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0410011-32510301230133031-20350003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows.*

