# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/0502052001002-55500001230123031-003-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fire — Ignite / Heating Up), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 5 seconds left and the target has fewer than 2 stacks of Fire Vulnerability
4. **Arcane Blast**: keep its buff stacked on you
5. **Arcane Missiles** (rank 7) when Missile Barrage is active
6. **Fireball** (rank 11)
7. **Scorch**

**Scorch** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** every 6 seconds, casts **Pyroblast** whenever three crits have made it a 1.5-second cast, keeps one stack of its **Arcane Blast** buff up, spends **Missile Barrage** procs on free **Arcane Missiles**, and fills with **Fireball** or **Scorch**. The best mage page in the simulator: 869 DPS in a full raid.

**Why it works**

- **Pyroblast** at 3 stacks of **Heating Up** is the first spell on the list (14 casts, 25%; its crits also feed **Ignite**, 10%): crits from **Fireball**, **Fire Blast** and **Scorch** each cut its 6-second cast by 25%, and **Fire Blast** adds a stack on every hit, so three stacks come about every 13 seconds and the cast takes 1.5 seconds. One hard cast before the pull lands as the fight starts.
- **Fire Blast** on cooldown (29 casts, 21%): every 6 seconds with **Improved Fire Blast**, instant, 10% crit from **Incineration** and 6% from **Critical Mass**; its crits start **Ignite** (40% of the hit over 4 seconds) and every hit feeds **Heating Up**.
- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds) and refreshes it under 5 seconds left. It is also the short filler (23 casts in all, 11%): when **Fire Blast** will be back before a 3-second **Fireball** could land, the list casts a 1.5-second **Scorch** instead.
- **Fire Power** is why the burns matter: 3% more Fire damage per Fire effect of yours on the target, up to 12%, and Fire Vulnerability, **Ignite**, **Pyroblast**'s burn and **Fireball**'s burn are four. **Fireball** (18 casts, 20%) casts in 3 seconds with all five points of **Accelerant**; the list names rank 11 (rank 12 comes from a tome).
- The 17 Arcane points: one **Arcane Blast** about every 20 seconds (9 casts, 4%) keeps its buff on you (12% of your Intellect as spell damage for 18 seconds) and rolls 40% for **Missile Barrage**, which **Fireball** rolls at 20%; the proc's free, fast **Arcane Missiles** are 9% of the damage (6 casts). **Arcane Concentration** makes one cast in ten free.
- **Combustion** once Fire Vulnerability has 5 stacks (the list holds every cooldown until then; one a fight on its 3-minute cooldown): each Fire hit adds 10% Fire crit until you land 3 crits, which fills **Heating Up** fast.
- Mana: a mana potion whenever it is ready (2 a fight, the list's top line), your mana gem (from **Conjure Mana Ruby**) and a Demonic Rune (about one each), and **Master of Elements**' 20% refund on every Fire crit. The raid list no longer channels **Evocation**: the search dropped that line on 2026-11-10 (+0.4%). Without a raid's mana buffs the simulator's DPS falls 23% from a 3-minute to a 6-minute fight: the mana runs out.

**Caveats**

- Mana without a raid's buffs: the simulator's list for playing alone adds **Evocation** below 10% mana with more than 25 seconds left.
- Several targets: **Flamestrike** (this build has no Blast Wave); **Fire Blast** hits one target only.
- Fire resistance: the simulator's boss resists nothing. Against a target that resists Fire, **Frostbolt** is your fallback and most of this list loses value.
- Threat: this build skips Burning Soul, so only **Arcane Subtlety** lowers your threat, and only for the Arcane spells; the simulator ignores threat.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: **Scorch** or **Fire Blast**.
- Moving: **Fire Blast** and the 1.5-second **Scorch** keep the stacks and **Heating Up** going; **Pyroblast** and **Fireball** wait.
- The list has no 2-stack **Pyroblast** line (the simulator's own Fire rotation, which this list is built on, dropped it): with 2 stacks and the boss about to die, a **Scorch** and a **Fire Blast** in the same 3 seconds are its choice.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 17 | Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Blast 1, Arcane Meditation 2, Improved Channeling 5 |
| Fire | 31 | Incineration 5, Accelerant 5, Ignite 5, Pyroblast 1, Improved Fire Blast 2, Improved Scorch 3, Heating Up 1, Master of Elements 2, Critical Mass 3, Fire Power 3, Combustion 1 |
| Frost | 3 | Precision 3 |

## The numbers

**How this pick was checked:** a full search on 2026-11-11 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 869 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 778 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12) |
| Pre-BiS | 853 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12) |
| Raid BiS | 884 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.4; Pre-BiS 61.9; Raid BiS 63.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Shroud of the Exile](https://www.wowhead.com/forever/item=15421) · *quest: In Dreams* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sorcerer's Bindings](https://www.wowhead.com/forever/item=226929) · *sold by Mokvar*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Inferno Gloves](https://www.wowhead.com/forever/item=18408) · *Tailoring* | [Sorcerer's Gauntlets](https://www.wowhead.com/forever/item=226930) · *sold by Mokvar* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Sorcerer's Leggings](https://www.wowhead.com/forever/item=226933) · *sold by Mokvar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Fire Striders](https://www.wowhead.com/forever/item=13369) · *Balnazzar, Stratholme*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Pyric Caduceus](https://www.wowhead.com/forever/item=11748) · *Pyromancer Loregrain, Blackrock Depths* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzkl19sFFUXwHtmlu7tKX/KfHww33x9OJSvX9ttt8zMsqRUYxcSsQhmG59MjMrdnbu7F6Yzm5lZC2+APBijQCovVEwIManBIAm+0CY8iDGpDxolQaI+QFT88yZ9IPEFzcxuARPCk8SHnmR37tyT82d+59x7Z7CbQRfoQNAPe6EGdTgE8DrAGYD3AbSViVaJtSNgnNQZ62LGJKbZ7DTotzoxxV67AJhiZ6YBVXb5AKbZV8dB/2E1ptnHJ0D/bjWq7NMqquzYi9jOFiuxUZpdPw/68TSq7A+OKjtcQpWdmESVvVvFdvbmpL7wL1TZoZdQZYtuz2DXguz/4hiYd0oTb52FN0A5KqdBuVOaAeXn7ecgPXsablnH5E04KnewJGEowLyyyTZztpm3TdMyTTubz+dN0zQtO5f8clbWNHMLCnypdH6vnFmP3bgW2dXUClTZr8JoXnrSuALVrB3i/5AZ7Zhiv09Dj35R+TdTtY4ZpTUTa1DJWtopRfsJuOMIh2zT3pq1rKxtUn9UEyQ9R9SF5wgvIt5wZNQX0rg1MEq7yoJ28CCQIiBe5dKjqZrwaGcgq9KhCX9KBEMko5AGrXwv7Qz8MCKHT/KqoIofkEWT0huiGg+p4TkiIJtCckUleoKqDR44wqHSwb8EKQnpVWm/5095QxT6VGpI1wlpSkY1vxFRnGzOytZ96UWtcBF3k7QDQQ2vXONeVTjGMPZqm+4Tww2ZBMo8xFA+uDvRhGKHLZTafm0vr7uv+PXoHhvTGqWWO/IDaoIrHUxSCPyIR9L3KBQ8KNeoPxSCKjIQ2YBLJ7ukzjbVw/tC3xsw0nGwrqNS+1DR7kAzjJnNWaOJS79SkWXJXQrlZMPlkR/0hRSD3OzUw8287oabHSHqO2UghnndTXwSjyi/pSx4eWtuhLjj1yPhUP+98C6vNstJvBKJIIkTiGxdeqM0aA+P9CZFimeFFwUH+0IqiTBqMifpEadKw3UpfqahlkHk0+CW4XzTMi68K8M4aGITDpFlDpmmSRVZrUUhJYSEE5JN3HMoN2DkcEDrw/WZdQy0jitJOW7P6TEZhByu6unEjkV4oHPjq3ZkGQNLuoZdL2rfwEN6NPc392gDXW0fjhojaGR0pmqrrgBiil34CDSlS4lTQcgv6eYfphsyMo+wtXFlDyJbhPihbhRjI3ajqL2zjAtM2J0xGGhrrsDK+7h0aAEdbdM+WcZ0xvEp7UkcNAaw89t2hil2eU7XodVhrf388pxutM67k9d2P7iJnLy222hdtePLmOI67LwIMb3PY3pxZ7Efi9rpZUxkI+qZ9axdY+eSreh60WAzSjyabW5Ks8VlfurEp86Noq5mzgJ2PP2qX05y1XYZz2C3ZjQX2cVk+c0vPIcdV1PxcO72Hruv9TI6d3sP/vcI6Kiyt1821mbWsHZNKbUZyVvrtm292rPGeLKwE1f37Juez8LS7f0gj/D1i7IAvynOYbUtkS2FxB4VBj13lY54qu1QpfCfmVOxfDa2sZLI12P2TUVP0VjmktL2j0hUWBo9Vvn/+ccWZ1vy//x7he2ticLe+AvtFCQ3bTfHMiq7tGHHAx9yJoxAAcZhAl6AGtThABxQ/hwA1ymYfQ==); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkl19oFFcXwHNm192bE/+s8/npfPPl4RibJtnsxplZV2JamlWojdWyoU+FQuvszt3dq5uZZWa20TdrfSilNWKlYPRBpGCxqGChmIAPtS/pQ0sQrLR9UFptbSm0+iCUgpQ7u1EL4lOlD7kwc+/cw/kzv3PuvTPYzSAFGhD0w06oQQP2AbwNcALgIwB1aSRVpHQY9GmNsRTTA0yyP8+AdrML4+ytc4Bx9ssReT82n8IEm3O1H5Zjkn12CLTvlmOc3ZqSwptTgAl2pyLVEmympk0lMc4+mE9hnB38NYUxdmgC4+zT+RQm2W9nQZv7D8bZu1OAMXbj1Z7B1Jzo/+ogGHdL4++dhHdAOSAOg3K3NA3KT5tPQ/LUcbhpHhTX4YDYwqKwoQCzyjrLyFlG3jIM0zCsbD6fNwzDMK1cdOXMrGHk5hSYV7q+V06sxm5ciexyfAnG2M9cb3U9SVyCsawV4FPI9ATG2R+HoUc7r/yXxdTOaaU9IyWoZE31qKL+CLbjcIcsw9qYNc2sZVB/WOMkXIc3uOtwNyS76YiwL6Axc2CEtpU5bbF9X3Cf7KotXJqscZe2+qIqHBr3JrmfIREGNGjme2mr7wUhOfaEXeVU8XwyaUK4GarZATVdh/tkUUB1XgmfoWrT9h3uUGnv35yUuHCrtNv1Jt0MBR6VmqLuBDQpwprXDEkGmzOzDU+4YdtdaNejsH1OTbdcs90qd/Qh7FXXPSCGa9IRlFmQUD6+N96CYgVtlOpudafdqL/uNcL7bAxzhNrmyPOpBa60NwrB90I7FJ5LAbf9co36A86pInye9W3hZBfE2ZZ4aFfguQN6UjpLHRDqWUW9Cy03RjZnjkQmvUpFlIVdp0BMNOt26Pl9AUmQ651GsN5u1IP1DueNrcLnQ3ajHtkkO6T8hjK3yxtzw2Q7XiPkDvXfd1+3q610kl0JuR/58Xm2IdwRGrSGhnujJMlZ7ob+3r6ASjwIW8xJuGRTpVmvk3ynTFsh9Ghww1C+pSkTXxeBdBrpBBkyjYxhGFQR1VoYUESIOwFZZLsO5Qb0HA6ofbg6vYqB2nkpSsftGU2SQcjhsp4u7LwDD1Wu7NX9ixhYVDXsalH9Bh5Ro7l/uEabWFd34Yg+jHpaYzF12SVAjLNzn4CqpBQZCkJ+QTb7KFlGTz9G18KlPYjsDsiXulaUSuxaUT22iBNM2J3WGagrLsHSB7g0aAMd6VA/X8R0xvA59Vkc1Aew69sEwzi7OKNp0K6w9n5+cUbT2+fdkSvbH95EjlzZrrd7dWoRU1yFXedB0vtS0pOVxW4U1eOLmMha1NKrWUJlp6Ot6GpRZ9OKHJ1qbUqniov81JGnzrWiFkufBOx8/g2vHMWqbtNfwG5Vby2y89Hym517CTsvx+Vw5vYOq6/9MTpzewf+fz9oGGPvv6avTK9gCVUpdejRV+umTb3qi/pYtLAjU/f1W5ZPwsLjAyePsXVLmYPfFefNWEfUNhQifVQY9NxTOuVUx75K4X/TR2X7YnRtJWpfj1rXFS1Oo+kLSse/0sLCwuiJtqfPPDE/m6L7yx8WNrcnCjvlf9pRiB46ro+mY+zCmi0P/c4ZMAwFGINxeAVq0IA9sEf5awDO1Jvt); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkl19sFFUXwHtml+7tLYVyPz6Yb74+HIq17bZbZmZZUqqxC4lYBLONTz4pd3fu7l6YzmxmZi28IemDMUoN4AOFB0JMMBgwwRfahBd8qTEaQoJEfYCo+C8k2iaSGBNi7uy2YEJ4kvjQm+y9d+/J+TO/c+69M7SLQCfogNAH+6AKNTgM8CbAGYAPANjqWKop6TAYp3VCOolRpyny5wXQ77TTJLl/DGiS/HJC9aeuddJWMu/p362hKbJwt0P/Zg1NksW7HTRJ7kwDTZHf73YovRS5eQH06RRNks/eg+V+6jjQBHl3gqbIrxdBn/8PTZK3p9Xaots90Dkv+744Cua94vg7Z+Et0KbkMdDuFWdA+3HHeUidOw13rKPyNkzJnSQOHPIwp222zaxt5mzTtEzTzuRyOdM0TcvOxr+slTHN7LwG17T2b7UzG2gXXUfJ9eQqmiA/C6MxdKfoKprI2CF9ihKjlSbJH8egW7+k/ZckWNuM1lxREqplLHZSYz8AdxzhoG3a2zKWlbFN7IuqAqXniJrwHOFFyOuOjHpDHLP6R3B3SeBOHgRSBMgrXHo4WRUe7gpkRTo47k+KYBBlFOKAlevBXYEfRujwCV4RWPYDtHBCeoNY5SHWPUcEaGOIrihHz2ClzgNHOFg89DcnRSG9Ch7w/ElvEEMfi3XpOiFOyqjq1yNUwWatTM2XXtR0F3E3DjsQWPdKVe5VhGMM0R62+QExujEdQ5kDBeXD++MNKHbYRMkOsH285r7m16JlNqY1gk1z6AfYAFc8FIcQ+BGPpO9hKHhQqmJfKASWZSAyAZdOZkmcaYiH9oe+12+klLPOKckuauweNNyYmaw1Epv0y2VZktzFUE7UXR75QW+ICuQWpxZu4TU33OIIUdslAzHEa25sE3mEua0lwUvbssPIHb8WCQf7lt27vNJIJ/JyJILYTyAyNemN4IA9NNwTJ0mtCi8KDvWGWBRh1GCO0kOO5brronqmwaZC5OPA1qFcQ1Ml3pWhchrrhINomYOmaWJZVqpRiDEh4YRoI/cczPYbWdrPeumG9HoCrO1qnI6FWV2RoZClHd3ttG0RHqpcNbIjKxhYXDXkZoF9BY+o0ew/XKN16rL9dMQYpkZaJwnWcRUoTZKPPgamdWoqFAq5Jdnco2SDRvoxujZd3U0pWQT1ULcKSoncKrBTKzjBSLvSBgG29iqsfoBLhybQkRb2yQqmM0afY8/SAaOftn/dSmiSXJnVdWhWWPM8vzKrG8377sSNPQ8fIidu7DGaI5tewRTX0/ZLoOh9ruipyiLfF9jpFUxkE9XTG0grI+fjo+hmwSAzmpqdaxxK5wor/NZRt86tgp5InwXa9vzrfimOle02XqBdzGhsskvx9pubf4m2XU+q6ezCXru3+TI6u7CX/v8I6DRBjr9qrEuvJa1MK7YY8Vvr9u097EVjLN7Ysall/Ybls7D094GTx9j6SZuH3zTnjURL3LbmY32qEei+r7WppZbD5fz/Zk6q9unopnLcvhy1b2t6EkfTl7WWf6VF+aXZE21PX3hifrbH/cvv53c0F/L71JfaSYj/tNweTSfI5Y07H/qgM2EY8jAG4/AKVKEGB+Gg9tcAc7KduQ==).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 838 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-12)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 827 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-12)

## Builds that play as a hybrid

- Frostfire — Frostfire Bolt (7/31/13): 30+ points in Fire, but it plays as the [Frostfire](frostfire.md); it is ranked there

---
*Generated by `_reference/data/render_modes.py` on 2026-11-20 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

