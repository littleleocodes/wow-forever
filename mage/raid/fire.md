# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12)

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

**Fireball** is your filler: cast it whenever nothing above is ready.

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
| Arcane | 17 | Wand Specialization 2, Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Blast 1, Arcane Meditation 2, Arcane Resilience 3 |
| Fire | 31 | Incineration 5, Accelerant 5, Ignite 5, Pyroblast 1, Improved Fire Blast 2, Improved Scorch 3, Heating Up 1, Master of Elements 2, Critical Mass 3, Fire Power 3, Combustion 1 |
| Frost | 3 | Precision 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 873 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 778 | this build |
| Pre-BiS | 853 | this build |
| Raid BiS | 884 | this build |

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV01sG0UU9pt17eeX/oTpD8uSwzRQkjhxsl7HVRIh4lYCAi1yxQkJAVl71/aWjdfyblB6S0sOCEFShV4ailRFSEGVSqVwaSLlQBCSOYAAqUSUQyKgwJHkEIkLoF07bQ5VT1Qc/CR7Zt7T997MN2/e7FAbQivIIKATRqEEFZgEeAfgKsAnAHxvYGW+dQCU24cRW1EZoyguzIJ8p4XC+PYNoDBenQWScGWCovjdDMi/7Kcofn4R5J/2k4RfFknC6VcpglsFHxTFtesgz0RJwn90kvB8jiS8OEYSflSkCL43JtcOkoSTr5GEW3Z7d2vN6vxmGtTt3Jn35+FdYFPWLLDt3Byw309cg+jCFbiTnLY2YMo6icGEIQPL7AlNTWlqWlPVpKpqiXQ6raqqmtRSwS+VTKhqqsbgW9byM/vtID1JqEQojH/NQru8yA6jxGNzrKHxLcQSSf4mH9Ur9htOxROaqh1PJJMJNTkk8iW9XDQN4VSFbhimIXLnhFcyRdXxdM9yysI19Wq+JDpd0xQFq2omqrplJHbMibq596zrlLuUqLKHpNYpi3/K+DbUw6iJVHIocOkUClbe0m3hWmPjtu451Q5XjOlFs8+ouH16xXb7DNOsPGdVzV69Ygc+he6JdH/e1PPHUwNCN5yKZxqi8254Wy8KfdywPKEXPLMaxKmaiYpVHhLdWu/AMVFw6lqz7FXPdbgiZ7qeyI1btiGsstBFYdy2hb+mngbAc0R3f2+6jrQ8V9iW6wcNMG6PSKo9qqqKglUsea4IGDINV2hCLxsi1aWkqIt30JH4IQQeWwV/HzaXZJ8ZghTta2+h2Bbs2h2/5ReamLAga3Aty3+E++Ro6j/O0XGy+VkaUgZIicso8X2rQBTGG58BZ63MnwpBese2fD9bjxJ/AFajve1EuAX+otazPgjXs/zDJt5gQW1xBYEfWIW99+iSoUHoUIh/0cTsjNAz/GnqVrqo5XYEKYwrS7IMjQyLLQelYmVJVho1/dKtU7uLyKVbp5RGy2eamMVD1LIIPntf++z5mYW/ZvmVJmbkKMnxIxjheC0oRWtZBeeY31uoF6WFbJPfOv6ts56Vpfg8UOzZt5x8MFf+gvI8tXGlfsgWg+O3XHuJYt+H/e7S5mmto/HBtbR5mh6/ADJJ+MHryiPxAxjhLBdSorSHpMHBY/xFZSQ42IGru/i653nYGd4L8gBff7Aa/Mm081IokP5MgCeG0P43i/mq0GQh89jcZV++Gj5aCOSHYW2DyWExHL/JQv+LeJmd3kOVp64/tDiDwf/LH2dONBSZUf+dcRmCQWhjOC7hzUdP7nqOqDAAGRiBM/AKlKACEzDB/h0APlE7+w==); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV19oHNUX3nN3unv3pH/2d/vnN459uI3WJJtscnc2W5IgZltQo61s8UkQNLM7s9mpk51lZyLtW615ENGk1CA07YMEIVJoCxGkG+iD8WV9UIJQi/qQoI0WETR5CIggcmc3bR5Knyw+7IGduXM+vnPufPfcM3vxIIU4qMChE0ahBBU4C/AOwEcAnwCwnQFKJDoA2up+SuNU8zBK/7oK6lobKvTt64AK/XVGXi8txzFC62X1p90YpZ+fB/WH3ajQu9MSXJsGjNCNoqRFaK2kTkdRoR8ux1GhU7/FMUzPj6NCP1uOY5T+fg3U+l5U6HvTgGF659X27njd7vx6CsRm/uT7c/AukEn7ApDN/CyQX45egej8ZVhLTdmrMGkfo8G0IQuL5AldpHWR0YVICaEnM5mMEEKk9HTwS6eSQqTrBJZJ24/k5734JFItggr98wK0qwtkPw2z2CxpeiSCJJlib7BRo+K87lZ8rgv9SDKVSorUEC+UjPKYZXK3yg3TtEyeP8P9ksWrrm/4tlvmnmVUCyXe6VkWL9pVK1k1bDO5BScbcO8pzy13aVFtB4bjkza7RtgmNNKIZDo1FIR0i0W7YBsO9+zxCcfw3WqHx8eNMavPrHh9RsXx+kzLqjxnV61eo+IEMbnh80x/wTIKR9ID3DDdim+ZvPNeescY48aEafvcKPpWNchTtZIVuzzEu/XegcO86Da8VtmvnunweN7yfJ6fsB2T22Vu8OKE43D5Tj1Ngu/y7v7eTINp+x53bE8mDTheD0+JHiEEL9pjJd/jgUKW6XGdG2WTp7u0NHaxDjyQ2EeBxZZArsN6TZXKIKRxV3sbxjZg2+rIOzvXwoIFVUNv59h38IAaTf/LNTqBDjuFQ9oAagmVhtmuJUBU6PVPgZE4kVNByGxhiw/CerTEQ7g67mxHpBsgX2olJ0l0JccutfACczyY0CiwPUuw875cKjQFHQqxL1pYnRF8hj2N3VoXtn0foajQmzVVhWaFxRaDVnGzpmrNnj5z6/j2JjJz67jWvLPpFlZxH7YtgFTvK6merCx6J8cut7Aih1BNHKARRq8Ereh2TqOzRI7mG01pPtfiXx351VnJqeHEHGDs2TfdQjBX9oL2PB5kWmOTLQTbb7H+Esa+UeSwtn5C72j+4aqtn8DHz4GKYfrBa9r/EntohJF8SIviDgwPDh5mL2ojwcYOQt3jNyLPwdbj/SQPiXWX1OEPor8VDgXWnw34SCi0/01i0hU6W8w+NntR2pfDh4qBfTusrxJV4cOJGyT0n5if3Ro9Unvq6iPLMxhcX/44e7TpyI7K08ZFCB5Cq8OJML3x/2PbDiUCBiALI3ASXoESVOA0nCb/DAD/4z9r); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV01sG0UU9hu78fglac30h2XJYRooSZw4Ga/jKokQcSsBgRa54sQJsvau4y0br+Vdo/ZWqhwQggal4dC0BxQhBVVKkcKlidRLuBghUIVUIuCQqBBAKBIkEpEQUoVm7aQ5VD1R9eAneXbmPX3vzXzz5o0H2yhEQQEOnTAKBSjBBYD3AD4B+AyAtfhWIq0DoN49TGmUqhUM03/nQVlvxhC9NwUYon9My/bq7Sg20WpR+Xk/hunmRqvy034M0a2NVgzR9UnAMP17o1XiwnRlHpTJMIbo1x/DbjtxGTBIPxrHMP3zBijVgxiiH0xK3Zbd3h2tWp3fXgKxnT3z4Sy8D2TCmgKynZ0B8tuJ6xCeuwbriUvWGkxYJ6k/cUjDEnlGE0lNpDQhEkJo8VQqJYQQCS3p/5KJuBDJKoHbpPku+fUgPotUbcIQ/WcK2pUFcpgGWWSG1DXSgiSeYG+zUb1kv+WUPK4J7Xg8kYiLxBDPFfTimGlwp8x1wzANnj3PvYLJy46ne5ZT5K6pl3MF3umaJs9bZTNe1i0jvmOO18y9Z12n2KWG1X0YjE5Y7AZh21ALI+LJxJDv0snnrZyl29y1xiu27jnlDpeP62Nmn1Fy+/SS7fYZpll6ySqbvXrJ9n1y3eOp/pyp544nB7huOCXPNHjnbnhbH+N6xbA8ruc9s+zHKZvxklUc4t1a78AxnndqWrPolc93uDxruh7PVizb4FaR6zxfsW0u19RTB3gO7+7vTdWQludy23JlUB/j9vCE6BFC8Lw1VvBc7jNkGi7XuF40eLJLTWIX68AjsUMUWGQZ5D5sLiqSGYQktrY3Y2QL9uyO/LKLDUyYnzV0JcN+gAfkaPJ/ztEK2uwsDqkDqMYUGmSty4AYop9/AYxEiZwKQmrHtvQgW48aewhWw5Z2RLoFclGrGQmiqxl2tYE3mGNbTKXADixDy326FKgTOhRgXzYwOyP4Anseu9UubP6xiWKI3lpUFKhnWGTJLxW3FhW1XtOn75zaW0Sm75xS61822cAsHsLmBZDsfSPZk5lFf8mwaw3MyFFUYkdoE6PX/VK0klHpDJG9uVpRmss0+K0jb53VjBKMzQJGXnzHyflzZa+oL2MbU2uHbME/fkvV1zDyXUh2FzdPax31P1yLm6fx6YugYJBeflN9InaANjGSDahh3IfBwcFj7FV1xD/YvqtdfM3zLOwM7wd5iK/fSRX+Itq7wYAv/Wkfj4RC+z0SkarAhXz6qZkrUr4aPpr35fthbY0oIT4cu0kCj0W89E7vkcpz848szqDfvv5p+kRdkR6V740r4A8Ca8OxIL355Mk9zxIBA5CGETgDb0ABSnAOzpH/BgBw8UE3).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 837 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-12)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 828 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

