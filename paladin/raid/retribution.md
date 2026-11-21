# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**[Retribution — Unsealed Wrath](../research/raid/builds/retribution-unsealed-wrath-raid.md)** (14/6/31) — [open the talent tree](https://talentsforever.com/paladin/60/050250002-501-05233011201301351-12)

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

**Talents with no line below:** **Repentance**: taken because Unsealed Wrath requires it.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Retribution Aura**: put it up at the start and keep it up
- **Seal of the Crusader**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Unsealed Wrath**, your swings store a copy of your active seal, and landing a swing under a different seal spends the copies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: it takes 1 second to cast, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Unsealed Wrath**: your swings store up to 3 copies of your active seal for 15 seconds, and landing a swing under a different seal spends them. This rotation dates from before that talent replaced Twist of Light, and the raid runs test it again.
- All those swaps cost mana. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 14 | Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2 |
| Protection | 6 | Divine Intellect 5, Precision 1 |
| Retribution | 31 | Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Unyielding Faith 1, Seal of Command 1, Pursuit of Justice 2, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Repentance 1, Vengeance 3, Champion of the Light 5, Unsealed Wrath 1 |

## The numbers

**How this pick was checked:** no talent search or short check of its own in this entry's current setup; one follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 768 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 742 | [17/3/31](https://talentsforever.com/paladin/60/0502500122-3-05233011201301351-12) |
| Pre-BiS | 760 | [16/4/31](https://talentsforever.com/paladin/60/0502510021-4-35233001001301351-12) |
| Raid BiS | 771 | [17/3/31](https://talentsforever.com/paladin/60/0502510022-3-35233001001301351-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.1; Pre-BiS 62.4; Raid BiS 62.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Wyrmhide Spaulders](https://www.wowhead.com/forever/item=12082) · *quest: A Taste of Flame* | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* |
| Back | [Heliotrope Cloak](https://www.wowhead.com/forever/item=18496) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973) · *sold by Mokvar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Voone's Vice Grips](https://www.wowhead.com/forever/item=13963) · *quest: Warlord's Command*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Gauntlets of Elements](https://www.wowhead.com/forever/item=16672) · *Pyroguard Emberseer, Blackrock Spire*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Lamellar Girdle](https://www.wowhead.com/forever/item=20042) · *sold by Samuel Hawke* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Handcrafted Mastersmith Leggings](https://www.wowhead.com/forever/item=13498) · *Goraluk Anvilcrack, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Dragonslayer's Signet](https://www.wowhead.com/forever/item=18403) · *quest: For All To See* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Main hand | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackfury](https://www.wowhead.com/forever/item=19167) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV11sFOUa3nd2dvbru93+fPRn+lFgzh4K7Z6zPTOzpyecHqBLy1F+bFxLFIwGmXan3cXdnTKzbeDGVIN/iEC8MaABA1yQRoNCTEgjiSExIhcEo0FDRMl6YwxG0gsu9sKYme12f+iPRIjfRTv7fu+8P8/3Pc+bwVYCdSCCBO2wC+IwChMArwG8B3AGgFY7u5y9uwbY1WbC13FsDwrku7iY9aGbfL4T3eTcTvSST4+A+KWAArn6jPhjDQrknRHxpv3/jZR4wos8ufIuoECmEvaLAjmcEn+oQZ7sv12HPPnoAKCbvJlCnnx8rQ695OcjIN6uQRfy5Py1ukBn3eVE+/Tz8t3B6PVDcAC4/Ym3gLs7eAyEU9r72o0Nk+A9mJg8A4cSt2B/opc4dUMEprjlcpesdsmyoqqhcEjuUsNhWVFUWQnLSrhLuczxWe5mI67GpVkQsWnDUCYxrmV0SbOsxEhaj0namKkFCArIh1TZQgkbJqEea3NCNWJ0LJmUTC09opd4rMSWLDRhQ9TUR6VtupaUjGGpz0iltHQs4EUPukNhC/+JK7LQiqzMayAxEs/oxpiV1i0rUIVe9ISUzi4LO7A1Cy3Y3KdZmWJpu8diI3pKT2dKXOlKFsCaQDXiNPGip52Qm9Es1KK/3xjXpYwhpfSkrtMW1oz+nIBItj8ijYxpZowJyJOzx8EJsDzYSgTKdbtYQ06ox9qNelLbJ/Vruw1T6ttodbtoL4vgv5mKLcFmAtR3jCMotLvJ2YtgB0JOtrAxuIS4qWfayxE3c/CRO1WLzTrSJN2pjSafM0Yzkiqr/wkpciisdEtDcRvRmGSYkhaL6TFpcJ+UieuSaWS0TMJIS5aumUNxqd3SdcnUM6HYqBUqbIbym527LSPdwdDJ5iGfnAL6GNuCPXRdRdvoD/iw6iTMdI/LcgJDcYuNrGTqWjJhpaRR08joQ3Z0VoCUtrG/Y3NOaEC6LW6MJWOSqQ+buhWXthl9M0kvnIKF3AYcN0I+Ow50CavPQg1W9xlpSx8ynTZpLfNnAZH8f69hDiWslOgOts13Q6mPVTnFecjFaHDjvDeFdrDVuDQniNi0SbPmcHCKEsjXxyE4NPcdplvZZlxH/4crAssWDIViTmjEJU9aemWIIkDB07AQB+jLwF4CHKeZxbMtzwlLsaU0W1koVNi/sDXA5q8KawN+9GWJXRyQt09A8YCC3/OVDLoD7BfAg0Bfh4XrKo2I/WzrAgUEAtKibcyGOzwRzRM9y3nRkzLGdYU+W3honASKdTnBj75+m/B5laJ+04dV06RAdTJLem/Ag+4p3kULjLEvb41ZJiP0OrCvAC26Z+GGbWkog9KutBLbRY6ivDG10Jj6ZxvL062ysQlgL2CYKotfsvK6wvTRwsP91lVRQjBW5DndwZ7CrXSzI6Ae6rnEzQqoMwzqg7W2OA+6bMKjW5HbKkXMqfIkFILbfu0CuRINJiok5mm2/cFmmpVbNTAfhtSJnzHHdHXFnIdf4tC2ABNK3FrumVB0ZgipDaVTOm9Vu9SG8lPyoBuhS11bHAtUpp0OKkLFAFOsgrkELLlTsdRXuLlmAf0V6O0HzvtutgZ9N4RZqmIHXY2+c1A0iMEmwlPfVNHE8hcJI2z9vfT8B+1A/w0BC85iPoJAfZeAIE++fTUqAnNwUhaZkeqVuYAYoOc5+iHnZF+s1Xu0oqzU9Wztfer4vNg5alCKXd5Qhp1jKmD3BHv8D0hbCZjO2zNgQgHMb4pghhcDs3f+PboquJLwtGqywEbWeI6jhKNVJ70Fi63pP3GX4Q4Xe9HtclZDZAp45NAV+I2rsg2uieFIy7Gj9vqi52/Dzrreo97iRF7qCV7gXH/JykQKTw91rfrgoeX5r/N34HRkw4whssv+tjoKzg/XrZ6gm1xo7i35BJNhDURgE0RhB8RhFPbCXu73AQAj1AA4); Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV11sFNcV3jO7O3t91muvL/4ZXwxMtxjsbdedmcUVdQEvNm35qdWtUQuVEGXsHXuXrnfcmbEFL5Vb0ZZEhER5SAKRTAQoQVYIESQSssILURTCk1EiEiGRWJuXKCIK8QMP+5BEM+v1/uCfoIByH1bjc8+cn+/e7zsebCEQBAFEaINDkIRRmAA4DvAKwAUAWu3scvbuZmC3mognyDELeTI7IGT96CbvH0Q3+S6BPvLyTFC4xaOPvPtWrfB5DfLkuCbcrUEfmXwVhDM+9JBPLgL6yDdvgP0uT14yhM9q0ENemAmihzxzz/59eyaIbvLaAfSRL58D4V4NutBDrswEQx3BG6m2uX9IDwbit0/C08AdSz0P3IOB08CfU19X72yfAt+J1NQFOJmahWOpHuKUDjGY5tZKnZLSKUuSIkc2RaKdSjQqSbIkyVFJjnbKNzhPlrvbgBtxdRYEbNw+aKXGVUsTVdNMDWe0hKiOGWqIII+eiCKZKGL9FNRhbY6vRoyPpdOioWaGtRKP9dichUasjxvaqLhXU9OiPiT26iMjaiYR8qEX3ZGoib/EdVloQVbm1Z8aTlqaPmZmNNMMVaEPvRG5o9PEdmzJQjM29aqmVSzt8FhiWBvRMlaJK13PQlgTqkacIz70thFyN56FWgz06eOaaOniiJbWNNrMmjCQ4xHJvt+Lw2OqkWA8esilSXACrA23EJ5yXS5Wn+PrsHaHllaPin3qYd0Qe3eYXS7aw2K4iSnYHG4iQP2nOYJ8m5tcugZ2IOQkExvCq4ibeud8HHEzBx+pQzHZgiNN04PqaPrv+qglKpLy64gsRaJylziYtBFNiLohqomElhAHjopWUhMN3VKtlJ4RTU01BpNim6lpoqFZkcSoGSlsRvKbHYdNPdPO0MnmJe+cA/pHthu76daKtjEQ8mPVWZjvHtfkeIbCbhtZ0dDUdMocEUcN3dIG7eisACltZT/Hphxfj3RvUh9LJ0RDGzI0Mynu1Xvnk149B8u59TtuhLw3CXQVq8tCDVb36hlTGzScNmktC2QBkfzuiG4MpswRwR1uXeqGUj+rcorzkmvx8I4lbwptZxtxdY4XsHGnai7i4BTFk48mITy4+B2me9gu3Ep/i+tCa5YNhUKOb8BVfzG1yhBFgMLnYTkO0P8C+w/gOLVWzrY2x6/G5tJsZaFQZr/ClhBbuiqsDQXQnyV2cUBePAPFAwp/6qlk0H1gXwGeAPoULF9XaUTsY3uWKSAUEldsYyHcsxPxPNGznA+9I/q4JtMDhYeGKaAYzPEB9PfZhM+rFA0YfqyaIwWqkwXS+0JedE97XLTAGPvy1hhlMkJvA/sQ0KT/XL5hWxrKoLQrrcR2haMob0wpNKb82MbydKtsbALYvzBK5ZUvWXldUfqHwsOj1lVRQjhR5Dndz/6Ke+guR0C91HudWxBQZxjUhWttcR5w2YRHtyy1VoqYU+VZKAS3/dp4cjMeTlVIzN/YvsebaUFuldBSGFInvmWMacq6RQ+/xKF1GSaUuDU/NKHo/BBS6kundN6qdCr15afkRTdCp7KlOBaoRDscVPiKASabBXMJWFKHbCr/4xabBfRroPceO++72Gb03+EXqIrtdCP6L0PRIIQbiYf6p4smlr9IGGPbHqbnL2g7Bu7wWHAW8hF46r8OxP737f9xAZiDk7zCjFRuLgZEP73C0Tc5J/tKrT6kFWWlbmNbHlHHl8TOUYNS7PKGMuwcUwG7P7M//QBpKwHTeXseTCiA+XERzOhKYPYsvUc3hNcTD62aKrCRNVzmKOFo1VlfwWJr+hfcDbjPJf7tdjmrPjYNHuTQFfqWq7INromhWPPpU/b6oPtnQ8663a3McoJH7A5f5Vw/ybJihacnujZcfGJ5fuP89p+PbZ83xA7Zn1enwPnDNdsddpOrTT0lX2ESbIYY7IQ47IckjMIROMJ9PwCouQJH); Raid BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsE1ca9j8ez5z8jnM55DI5BJj1Eki86+x4vFmxWSAmYXe5bLTeoF1YabXLJJ7EZm1PdsaJwssqRfQqSqRWbQVVAQGVUFRKBS8oKn1AqkR5omoLFRIFmVbtA6g0Dzz4oapmHMcXcikqqOchOvnP7//ynfN9vwZbCdSBBDK0w16IwyhMArwAcALgDACtdk45+3QDsM+aCV/HsQkUyddv10pZL/LkyylAN/kgjiJ581qd9LGAInnrvk+6W4MiuXoApFv25sQBkI6LyJOvpgBF8t27YP9aJDfOgnS7Bnny+rU65MndKUCeHHzVDvlyCkVy+zWQ7tWgC3ly4Vqdv7PuSqJ99r/Kw8Ho9cPwEnAHE68A93DwKAintHe0m1umQTyUmD4DhxN34GCilzjlQwRmuNVKl6J2hRRFVYPhYLhLDYcVJaQoobASCneFrnB8lrvViOtxZRYkbNoylEmMaxld1iwrMZLWY7I2Zmp+ggLyQVWxUMaGaajH2pxQjRgdSyZlU0uP6CUea7ElC03YEDX1UXmXriVlY1juM1IpLR3zi+hBdzBs4a9xTRZakZV5DSRG4hndGLPSumX5q1BETzDU2WVhB7ZmoQWb+zQrUyxt31hsRE/p6UyJK13L/Fjjr0acJSJ62gm5Fc1CLfr6jXFdzhhySk/qOm1hzejLCYhk95/kkTHNjDEBeXLuGDgBVgdaiUC5bhdryAn1WLtVT2r75X5tn2HKfVutbhftZRH8LVOxJdBMgHqPcgSFdjc5dwnsQMgpFjYGVhA39cyKHHEzBx+lU7XYvCNN0n9ro8n/GKMZWVXU3wVDSjAc6paH4jaiMdkwZS0W02Py4H45E9dl08homYSRli1dM4ficrul67KpZ4KxUStYOAzmDzv3WUa6g6GTzUPePwX0L2wH9tBNFW2jz+/FqpMw1z2uygkMpR02srKpa8mElZJHTSOjD9nRWQFS2sZ+ic05oQHprrgxlozJpj5s6lZc3mX0zSW9eAqWchtw3Aj58BjQFaw+CzVY3WekLX3IdNqktcyXBUTyxwnDHEpYKckdaFvshVIvq3KK85BL0cDWRV8K7WDrcWVOkLBpm2Yt4OAUJZBPj0FgaOE3THey7biJ/gHX+FctGQqlnNCIK/5u6ZUhigAFTsNSHKDPAjsAOE4zy2dbnRNWYktptrJQGGK/wVY/W7wqrPX70JsldnFA3jgOxQsKfMFXMugBsPuAh4C+CEvXVRoR+9nOJQrw++Vl25gPNzUZzRM9y4noSRnjeoj+q7BpnAaKdTnBh95+m/B5laI+04tVs6RAdTJPetHvQfcM76IFxtiPt8YskxF6HdgngBb939IN29JQBqVdaSW2y1xFeWNqoTH1pzaWp1tlY5PA/o9hGlr+kZXXFaZ/Lmwet66KEgKxIs/pHvYP3Em3OwLqoZ7L3LyAOsOgPlBri/OgyyY8ukNKW6WIOVWehEJw269dIFejgUSFxPyT7X6ymeblVvUvhiF14mfMMV1ds+Dllzi0LcGEEreWRyYUnRtCakPplM5b1S61ofyWPOhG6FI3FscCVWing4pQMcBCVsFcApbSGbLU57iFZgH9Fui9J877brYBvTeFeapiB12P3vNQNEiBJsJT70zRxPIPCSNs86P0/BXtQN9NAQvOUj6CQL2XgSBPPn8+KgFzcAotMyPVqwsBMUAvcPQ9zsm+XKuPaEVZqZvZxsfU8UWxc9SgFLu8oQw7x1TA7m/srz9C2krAdH49ByYUwLxRBDO8HJi9i5/RdYG1hKdV0wU2ssbzHCUcrTopFiy2pn/DXYEHXOwZt8tZDZEZ4JFDl/97rso2uCaHIy1Hj9jro55fDDvreo96h5N4uSdwkXP9LCsTKeye6lp39qnl+b3zd+B0ZMucIbLX/sQ6As4/rjs9ATe52Nxb8iWmwAaIwDaIwh6IwyhMwAT3wwBvsgLV).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-open-raid.md) (16/4/31, 769 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-14232021201301351-12)
- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 629 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-20 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

