# Prot-Ret Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Prot-Ret

*Retribution's melee talents with Protection's Seal of Fury, Swift Judgement and Toughness: a melee split short of 30 Retribution points.* (a hybrid: Protection/Retribution).

**[Prot-Ret — Raid](../research/raid/builds/prot-ret-ml-raid.md)** (10/12/29) — [open the talent tree](https://talentsforever.com/paladin/60/05005-532001001-1523312100130034-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Retribution — Seal of Command), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**.

**Talents with no line below:** **Templar's Bulwark**: a defensive for emergencies, so it has no line.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike** when Judgement is on cooldown

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Retribution Aura**: put it up at the start and keep it up
- **Seal of the Crusader**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 10 | Divine Strength 5, Improved Seals 5 |
| Protection | 12 | Divine Intellect 5, Redoubt 3 (tier point: needed to reach Templar's Bulwark), Precision 2, Templar's Bulwark 1, Toughness 1 |
| Retribution | 29 | Deflection 1 (tier point: needed to reach Champion of the Light), Benediction 5, Improved Judgement 2, Conviction 3, Sanctified Judgement 3, Vindication 1, Seal of Command 1, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Vengeance 3, Champion of the Light 4, Unyielding Faith 2 (tier point: needed to reach Champion of the Light) |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-11-13 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 655 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 636 | its own set |
| Pre-BiS | 662 | its own set |
| Raid BiS | 662 | the Pre-BiS set (its own set: 658) |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.8; Pre-BiS 62.0; Raid BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Wyrmhide Spaulders](https://www.wowhead.com/forever/item=12082) · *quest: A Taste of Flame* | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973) · *sold by Mokvar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Voone's Vice Grips](https://www.wowhead.com/forever/item=13963) · *quest: Warlord's Command*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Gauntlets of Elements](https://www.wowhead.com/forever/item=16672) · *Pyroguard Emberseer, Blackrock Spire*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Lamellar Girdle](https://www.wowhead.com/forever/item=20042) · *sold by Samuel Hawke* | [Brigam Girdle](https://www.wowhead.com/forever/item=13142) · *General Drakkisath, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Handcrafted Mastersmith Leggings](https://www.wowhead.com/forever/item=13498) · *Goraluk Anvilcrack, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Finger | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Main hand | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackfury](https://www.wowhead.com/forever/item=19167) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

*This build does better outside its own set in Raid BiS (658 in its own set, 662 in the Pre-BiS set): those columns show the set made for an earlier build.*

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Raid BiS: Talisman of Ephemeral Power, Blackfury (Molten Core); Raid BiS: Onyxia Tooth Pendant (Onyxia's Lair)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV11sFOUa3nd2d/bru93+fPRn+lFgzh4K7Z6zPbOz9ITTA3RpUfmxcS1RMBJk2p12F3d36sy0gRtTDf4hgvHGgAQMkEgaDQo3pJEbEiNiYjQaNESUrDfGYCS94GIvjJnZTveH/kiE+F20s+/3zvvzfN/zvBlsJVAHAojQDnsgCaMwAfAqwLsAZwFotb3LWbtrgX3eTDx1HNOQJ98nhZwf3eTT3egm53cjT44nha945MkXTws/1SBP3hkRblj/X88IJ33oIVePA/JkKmW9x5MjGeHHGvSQA7fq0EM+OgjoJu/tQjd5I4M+8subINyqQRd6yIUv64KddVdS7dPPSncG49cOw0HgDqTeAu7O4DHgTyvvK9c3ToLvUGryLBxO3YQDqV5iVw0xmOKWSV2S1BXukqMRKRKWu+SoLEUikhSJylJ0zRXOk+NuNOJqXJoDAZs2DpmpccVURcUwUiNZNSEqY7oSJMijJyxLBorYMAn1WJvnqxHjY+m0qCvZEbXEYyW25KAJG+K6OipuV5W0qA2LfVomo2QTQR960R2OGvhvXJGDVmRlXgOpkaSpamNGVjWMYBX60BuOdHYZ2IGtOWjB5j7FMIul7R1LjKgZNWuWuNKVLIg1wWrEaeJDbzshN+I5qMVAvzauiqYmZtS0qtIW1oyBPI9IdjwsjowpeoLx6CHnToAdYHmolfCU63axhjxfj7Wb1LSyX+xX9mq62LfJ6HbRXhbDNUzGllAzAeo/xhHk293k3CWwAiEnGdgYWkLc1Dvt44ib2fhInbLBZh1pmu5WRtPPaKOmKEvyf8MRKRyNdItDSQvRhKjpopJIqAlxcL9oJlVR10zFTGlZ0VAVfSgpthuqKuqqGU6MGmFnM1zY7NxraNkOhnY2L/n4NNBH2Vbsoesr2sZA0I9Vp2Cme1yW5xkKWy1kRV1V0ikjI47qmqkOWdGZAyltY//E5jzfgHR7UhtLJ0RdHdZVIylu1/pmkl48DQu5DdhuhHxyAugSVp+DGqzu07KGOqTbbdJaFsgBInlon6YPpYyM4A61zXdDqZ9V2cV5yaV4aNO8N4V2sNW4NM8L2LRZMeZwsIviyTcnIDQ09x2m29gWXE//jyuCyxYMhUKeb8QlTxhqZYgiQKEzsBAH6EvAXgQcp+bi2Zbn+aXYUpqtLBRG2H+wNcjmrwprgwH054hVHJC3T0LxgEI/eCoZdBvYr4CHgL4GC9dVGhH72bYFCggGxUXbmA13ZCJeIHqO86E3o42rEbrLeWicBIp1eT6A/n6L8AWVogHdj1XTxKE6mSW9L+hF95THRR3GWJe3Ri+TEXoN2NeABn1u4YYtaSiD0qq0EttFjqK8MdlpTP6rjRXoVtnYBLDnMUoji1+y8rqi9BHn4V7rqighlCjynO5kT+I2usUWUC/1XuZmBdQeBvWhWkucB10W4dEdkdoqRcyu8hQ4wS2/dp5cjYdSFRLzFNtxfzPNyq0cnA9Dasc39TFVXjHn4Zc4tC3AhBK3lrsmFJ0ZQnJD6ZQuWOUuuaH8lLzoRuiS1xXHApVop40KXzHAIoZjLgFL6owY8svcXLOA/gb01n3nfTdbi/7r/CxVsYOuRv95KBqEUBPxUP9U0cQKFwljbMPd9PwX7cDAdR4dZ6EQgaf+y0DQQ757JS4As3GKLDIj5atzATFAL3D0Q87Ovlird2lFWakb2Lp71PF5sbPVoBS7gqEMO9vkYPc4e+xPSFsJmPbbM2CCA+a3RTCji4HZO/8eXRVaSTy0atJhI2s8z1HC0apTPsdiafrP3BW4zSVecLvs1RCbAg9y6Ar+zlVZBtfEcKzl2FFrfdbzj2F7XeuRb3KCR+wJXeRcf8syY87TA12rPnhgef5n/x04E9s4Y4jtsT6sjoL9w3WzJ+QmF5t7S76/JFgLMdgMcdgJSRiFfbCP+2MAew3/Eg==); Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV11sU2UY7nvann57u27dx37OPgYcK4Ot2nl6ygxOYGVD5cfFOqJgQpSz9Wwttj3znG6BGzMNIhpA443AxTBAIllEDHhBFrlBTZCYiNFMQ4Iu9cYYjLgLLnqh5pyu6w/7kQjxu2hO3+8978/zfc/z5mATAS8IIEIL7IYYDMEowEGADwDOANBKa5czd9cC+6aBOLwcM5AnU31Cxo0OcuAsoJ38HUUXGbvmFb7l0UU+/7Ra+KUKeXJQFW5UoYt88bVXOOFCO5kcQBf582Mw3+XJUV34uQod5PBNLzrI0WtetJPDSbSTD3ehi/z2Lgg3q9CGDnLhmtfX5r0Sb5l+WbrdF5k8Am8Dtz/+HnC3+44Df0r5SLm+cRxch+LjZ+BIfAr2x7uIVTmEYYJbJrVLUnugXQ4FpWBAbpdDshQMSlIwJEuhNVc4R4a7UYercWkGBKzf2J+OjyhpVVQMIz6YUqOiMqwrPoI8OgKyZKCIteNQg9VZvhIxMpxIiLqSGlSLPFZiYwbqsTaiq0PidlVJiNqA2K0lk0oq6nOhE+2BkIEP44oMNCEr8eqND8bSqjZspFTD8FWgC52BYFu7ga3YlIFGbOhWjHShtD3D0UE1qabSRa50JfNhla8ScZq40NlCyI1IBqrR06ONqGJaE5NqQlVpI2tAT5ZHJDueFAeHFT3KeHSQc2NgBVjubyI85TpsrDbL12D1JjWh7BN7lD2aLnZvMjpstIuFcQ2TsdHfQIC6j3ME+RY7OXcJzEDISQbW+ZcQO3VOuzhiZxY+UptssFlHmqAvKkOJl7ShtChL8qOBoBQIBTvE/piJaFTUdFGJRtWo2LdPTMdUUdfSSjqupURDVfT+mNhiqKqoq+lAdMgI5DcDuc22PYaWamVoZXOSz04BfZptxU66vqxt9PjcWHESZrrHZVmeobDVRFbUVSURN5LikK6l1X4zOstDSpvZg9iQ5WuRbo9pw4moqKsDumrExO1a90zSi6dgIbdey42QL8eALmE1GajCym4tZaj9utUmrWaeDCCSJ/Zqen/cSAp2f/N8N5S6WYVVnJNcivg3zXtTaCtbjUuzvID1mxVjDgerKJ58Pwb+/rnvMN3GtuB6+jiu8C1bMBQKWb4OlzxnqOUhCgD5T8NCHKBvAHsdcISmF8+2PMsvxcbibCWhMMgewSYfm78qrPZ50J0hZnFA3j8BhQPy/+QoZ9AtYL8DHgL6FixcV3FE7GHbFijA5xMXbWM23DujkRzRM5wLnUltRA3SXfmHunGg6M3yHnT3mITPqRT16G6smCZ5qpNZ0rt8TrRPOGw0zxjz8lbpJTJCJ4F9B2jQVxZu2JSGEijNSsuxXeQoShuT843J/7WxHN3KGxsF9iqGaHDxS1ZaV4g+lX+427rKSvBHCzynO9nzuI1usQTUSZ2XuVkBtYZBjb/aFOc+m0l4tAel5nIRs6o8Cfngpl8LT65G/PEyiXmB7bi3mWblVvbNhyG14qf1YVVeMefhFzk0L8CEIrfGOyYUnRlCcm3xlM5Z5Xa5tvSUnGhHaJfXFcYClWibhQpfNsCCRt5cBJbUFjTkA9xcs4D+AfTmPed9B1uL7uv8LFWxla5G93koGAR/PXFQ90TBxHIXCcNsw530fIi2ouc6j3lnIReBp+7LQNBBfnwzIgCzcAouMiPlq3MB0UsvcPQTzsq+WKt3aEVJqRvYurvU8Xmxs9SgGLucoQQ7y5TH7ln2zL+QtiIwrbdnwIQ8mD8UwAwtBmbX/Ht0lX8lcdCK8TwbWd15jhKOVpx05S2mpv/KXYFbXPQ1u81ateEJcCCHNt9fXIVpsI0OhBuPHzPXV50PDFhrslOe4gSH2Om/yNn+l5UO55/u61p19r7lecz67T0d3jhjCO82P66OgfXHNtXpt5OLDV1F32ASrIUwbIYI7IQYDMFe2Mv9MwCe8QGc); Raid BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV0tsE9ca9j8ej09+x3kc8pgcAsz1JZD4XueOx+SKmwvEJLTl0ahuUAuVqpZJPIlNbU8646SwqVJEn+IhteoD2gICFigqpYINisoGqRJlRdUqrSJRIreLLkClWbDwoqpmHMcP8igqqGcxOv7PP//5/++c7/s92EygBkSQoBX2QAyGYQzgLYBTAOcAaKW9ylmr64FNNhK+hmOvoECm+8WMB3ny81FAnkx9AugmH9+oEb8R0E0+veMVf6pCN7l+AMSb1uTUARBPupEnP5y3PH/7HKzXBfKRId6qQp4cvl2DPPnghvU8+B6gkxxOopvceh/E21XoQJ5culHja6+5Fm+deUm+1x+ZPALvAHcw/i5w9/qPg3BG/Uyd2jwO7kPx8XNwJD4NB+PdxM4ewjDBSXKHLHcEOkKKLAdlORgIdiihUFCx5iFZDq27xvEZ7mY9rsXlGRCxYfNAOj6qpjVJNc34UEqLSuqIofoICsgHFNlECevGoRars0IlYmQkkZAMNTWkFXmsxqYMNGBdxNCGpZ2ampD0QalHTybVVNTnRhc6AyET/42rMtCMrMSrLz4US2v6iJnSTNNXgW50BYLtHSa2YXMGmrCxRzXThdT2jkSHtKSWShe50tXMh1W+SsQZ4kZXKyE3IxmoRm+vPqpJaV1KaglNo02sEb1ZAZHselwaGlGNKBOQJxdOgB1gpb+ZCJTrdLC6rFCL1Vu0hLpf6lX36obUs8XsdNBuFsZ1TMEmfyMB6jnOERRaneTCFbACISebWO9fRpzUNePmiJPZ+MjtisnmHGmCvqAOJ17Uh9OSIiv/DQTlQCjYKQ3ELESjkm5IajSqRaX+/VI6pkmGnlbTcT0lmZpqDMSkVlPTJENLB6LDZiC/GMgttu819VQbQ3s3F/nyDNAn2XbsohvLykavz4MVp2G2elyRFRiK2y1kJUNTE3EzKQ0belobsKKzPKS0hf0TG7NCHdKdMX0kEZUMbdDQzJi0U++Z3fTyGVjMrc92I+SrE0CXsdoMVGFlj54ytQHDLpNWM28GEMlj+3RjIG4mRae/ZaEbSj2swk7ORa5E/FsWvCm0ja3F5VlBxIatqjmPg52UQL47Af6B+e8w3cG24Ub6f1zlW7FoKBSzQj0ue8bUykMUAPKfhcU4QF8HdgBwlKaX3m1lVliOTcW7lYTCIPsPNvvYwllhtc+LngyxkgPy4UkoHJD/R76cQXeB3QE8BPRtWDyv4ojYy3YskoDPJy1Zxly4o2ORHNEznBtdSX1UC9Ln85P6caBYkxW86Om1CJ9TKeo1PFgxQ/JUJ3Okd/tc6JzgHTTPGOvyVhklMkIngX0LaNKXFy/YkoYSKK1My7Fd4ihKC1PyhSl/tbAc3coLGwP2KoZocOlLVppXiD6RnzxoXmUp+KMFntPd7FncQbfZAuqirqvcnIDazaDWX22Jc7/DIjw6g3JLuYjZWZ6GfHDLr1Ug1yP+eJnEPMd2Pdyd5uRW8S2EIbXjp40RTVk17+EXObQswoQit6b7OhSdbUJKXXGXzlmVDqWu9JRc6EToUDYU2gKVabuNilDWwIJm3lwEltweNJU3uPl6Af0V6O2HzvtOth49U8IcVbGNrkXPRSgYRH8D4alnomBiuYuEYbbpfnr+i7ahd0rAvLOYiyBQz1Ug1h+4NyMiMBun4BI9Urk+HxB99BJHv+Ds3Zcq9T6tKEl1E9vwgDq+IHa2GhRjlzOUYGeb8tg9zZ76E9JWBKb99iyYkAfz+wKYoaXA7F54ja7xryY8rRjPs5HVX+Qo4WjFaXfeYmn6L9w1uMtFX3M67FEXngAeOXT4fucqLINjbDDcdPyYNb7u+segPSa7lGlO5KUu/2XO8beMdDg/e6RjzflHts//7Gff2fDmWUN4j/WNdQzsH47pLr+TXG7sLvoUk2E9hGErRGA3xGAY9sE+7o8BAODtAto=).

**Points that do nothing for this spec:** **Deflection** (1) and **Unyielding Faith** (2) only count toward the points the tree needs before **Champion of the Light**; **Redoubt** (3) only counts toward the points the tree needs before **Templar's Bulwark**; **Toughness** (1) does nothing here, and no more useful legal talent was found for its point.

## Other builds of this spec

- [Retribution — Seal of Command](../research/raid/builds/ret-full-buffs-raid.md) (8/15/28, 628 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05003-053020005-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Windfury Totem's buff changed in client 1.60.1.71037 and the raid simulator used here predates it: full-raid numbers of melee builds assume the old totem.*

