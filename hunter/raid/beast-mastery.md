# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**; no global cooldown, so press it alongside the others
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: on the training dummy it is about 15% of this build's damage, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks. The full-raid rotation recasts it whatever your mana: the search of 2026-11-10 dropped the old 30% mana guard (about 0.2% better).
- **Arcane Shot** goes out every time its cooldown ends: 5.4 seconds with 2 points in **Improved Arcane Shot**, about 33 times in a 3-minute fight. **Summon Hawk** shares that cooldown, and the full-raid rotation gives all of it to **Arcane Shot**, so the build's **Summon Hawk** point is never cast.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) goes once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown, so the next **Aimed Shot** is cast under it.
- **Aimed Shot** is last on the list but it is not a spam filler: it goes out almost every time it can, a 2-second cast and then its 6-second cooldown, about 23 times a fight. The instants above it cost only a global cooldown.
- **Bestial Wrath** (+50% pet damage for 18 seconds) goes at the pull and on every 2-minute cooldown, twice a fight. **Intimidation** is in the build only because **Bestial Wrath** requires it; the full-raid list never presses it.
- Your pet is about a quarter of your damage on the training dummy. It takes 10% of your attack power and all of your crit (this project's model of Forever's pet scaling), so **Ferocity** and **Frenzy** keep it critting and attacking faster, and **Focused Fire** adds 2% to you both while it is out.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator's best rotation never casts **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** is the first thing to drop when you run low.
- Keep the pet alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead pet takes **Focused Fire** with it. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; players have measured this only at levels 20 and 30).
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant, so keep pressing them.
- The simulator starts **Aimed Shot** 2.5 seconds before the pull so it lands as the fight begins; in a real raid, start it once your tank has the boss.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98), **Trueshot Aura** rank 5 +100 (rank 4 +75; if your build has it) and **Aspect of the Hawk** rank 7 +120 (rank 6 +110). Cast the highest rank you have.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 350 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 31 | Deadly Aspects 5, Endurance Training 3, Focused Fire 2, Bestial Swiftness 1, Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1, Bestial Discipline 2, Frenzy 5, Bestial Wrath 1 |
| Marksmanship | 20 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 2, Mortal Shots 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 1016 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 934 | this build |
| Pre-BiS | 1011 | this build |
| Raid BiS | 1022 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.9; Pre-BiS 62.6; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Backwood Helm](https://www.wowhead.com/forever/item=18421) · *quest: The Treasure of the Shen'dralar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Ogre Forged Hauberk](https://www.wowhead.com/forever/item=18530) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Leggings of Destruction](https://www.wowhead.com/forever/item=18524) · *King Gordok, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Beastslayer's Trident](https://www.wowhead.com/forever/item=279910) · *quest: Mapping the Way Forward*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFG0Y3veb2Zl33///l/1H/Xcc5Gf+/UHWhVm+GRtRI3b11CmkUydzdFd3JN1ldyG9GRiEWLvUSRMMLDLJu3ToIEl20ggqysjMooMHLx3qELHjLkR2VHoOwzvPM8PzvN/38lITQghU0CEKfZCBHEwAXAG4BbAIoPzpqayitoP2TkYMCdpFkvFzCdTdP0jAx70k4MMMSTiXUZ9KJONOGdT3QZLw5pD6JkgyLpdAfRskEV8uA8m4VfZ+lbA0ckA/KgOJOLkXIgGvjpCI98qV7z5O/a3uBclHMt4ogfq6LtIcWneju/MwBWzSnYXAgnPf2eqavwNLIE+7d+fgmrsNk243eqkhCQ9Yk91qcc5Nm9smNy3bNDi3W7nNLc7tdSZuMtxhW36qJ9QkEnFzDSJIEomGyQvUUGUXFyASIJn8hhW3C8plUHqd3IXz2VxRt7jVZpjcMNs69YGMMzqUTunZvO6kUumU3j+uFzNpPZ8tOkU3O6oX0k5+IKNHC+m03j9i5B03ZdRE40CMDxeyoy3a/9QYC6Og4HAl1cYaaJ4/j1t2QatSiqixTp/iHg7DO440jKz5ScCNrDL+i75PHKlVmP56JRGJuDrRo7CQ6PVaqU9pJ8lSONXHFBQU/ypj6Ndk8pPA4yapsX9QUAJLUL2tmmJ7yT+EleGfkvMOw2o/0uQHk/Liy5lDXiY3uHUMXosLoOjav9QQq0N/7Ui84eVxu+B1/qxeFT6xddhn1iXB5yGanIJGClMDzl6H0NdpUKUWn4f9RB9GvrFApfZNDCYbZ2cqeJL4b9DD84S1zVRRT8RWmO+3oJisVceK5uVj8+nwnmdvJ7uqRLKvsm5nwHvxbSdiAq6Eu3/YyhzaIQmnoQfOQQZyMAZj7PsAWd0rTw==); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IHHcU3veb2Zm3r+06jNodBynTLci6MMtvxo6opezqqaciPfXUOrqrO1LdZXcP682ChSLaP56qFSxYqZUKhSQggVwMggFBg5CExBAxBnLw4DF/IIQZdyHEHJV8h+HN983wfe/3ezxqRVBAAwMSMAB5KMIkwM8AfwGsAqgfBirz1S7Qj2RERdCrJOONaw3a8Qck4JUqibi/o5CEi3nttkQy3rzaoD2OkoR/jmgPoyTjzo6iPYqSiPfWgWT8fw78fyX8deyM/mNPIRFnTxQScHaMRPz3N/+7lysN2kmUQiTjs99Be9AYb1O2vcTxEkwDm/IWILLs/uce9C6twBrIM94/i/CLdwhTXh8GsSED11mr02Fzzi2HOxa3bMcyOXc6uMNtzp1tJu4xPGIHYWoi1CUScW8L4kgSiabFy9RcY1eXIR4hmcKmnXLK6k+gfucWf/i+UKwYNrc7TYubVmePMZR3x0dyWaNQMtxsNpc1BieMSj5nlAoVt+IVxo1yzi0N5Y1EOZczBsfMkutlzbponomp0XJhvF3/jFqSMRRUHPVT7W6BHvjzlO2U9RqlijrrCane+TC8+0LDyHqYBNwtqBPv6PvzC7WK0Uf3JSIRNyf7VaaIQa9+/aX+Bdkqp6akioIa3mQMw7pMYRJ4yiIt+TEKamQNardVV5wg+ZOYOvpWct5t2l0XmvxsUu4+//qcl8VNbl+C1+oyqIb+CTUnGzFcP5JgeHnKKQed7zdpwlO2DafM/lEIBUhkpqGFYtSMC3OgvJgBTWoPBThND2D8FYv4dWhyONOyMO/jVvrT4QB30vYh00QjndxgofeCSqZeXSra1i/Npzt4fvN3prdGZAb8fTsPwUvoMJ0UcCPW98Za5tAFGfgK+uFbyEMRqlBlrwcABFos8g==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIG2kUzvtnknl5uxuHUTfjIMtsFiQGJvwz7oi6LIme9rTInva062iiGVlNSHLQPbngwiK6Fk/VllqwUisVemhBCr1YBAsFU4S2tJZKm0IPHry2hVJmTKDUHpV+h+HN983wfe//H49aEWRQQYc4DEAOCjAF8B/AZYA1AOVrX2We2gVaVUKUBe1vkvDOrQa1+hWJWJ0HEnHvvkwSXqrI6oMQSXj3ZoP6MkIhvDCiPouQhBvzoD6PkIiPN4AkvLEA3t8hnB87ps9XZBJx7lAmAefGSMRr57zv3q02qIcRCpCEiwugPm2Mtck7bry6DDPApt0lCK8415393uVVWAdp1r16Ef53D2Da7UM/OKThNmu1OyzOuWlz2+SmZZsG53YHt7nFub3DxArDF2w/SE2EWohErGxDDClEomHyEjXX2LUViIVJoqBhJe2S8i8ofziFv/7MF8q6xa1Ow+SG2dmjD+Wc8ZFsRs8XdSeTyWb0wUm9nMvqxXzZKbv5cb2UdYpDOT1eymb1wTGj6LgZoy4ax2JytJQfb9d+oJZEFAUFR71Uu9ug+f48adklrUYposZ6Aop7MgzvPtUwkhYkAXfzyuRn+v7xVK2i9M2TEJGIW1P9CpNFv1ev/ln7iSyFU1NCQUEJbjGGQU2iIAk8aZKa+BYFJbwOtduqK7af/FVUGf0kOe82rK5TTX48KY/e/HrCy+QGt87Aa20FFF37jpoTjRisH4k/vDxpl/zO95pU4TXbgSNm/SMEfMTTM9BCUWrGpQWQ386CGmoP+DhKDWDsPQt7dWBqON2ytOjhXur7YR8PU9YBU0U9ldhkgS+CcrpenSnaNs7Mp9t//nYl3Vsj0gPexl0E/yVwkEoIuBnt+2gxc+iCNPwC/fA75KAAEzDBPgwATNIs8g==).

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

