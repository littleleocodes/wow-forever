# Feral Combat Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Feral Combat

**✅ Recommended** for raid (the best druid spec here, or within 3% of it).

**[Feral Combat — Raid](../research/raid/builds/feral-combat-open-raid.md)** (9/33/9) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000032021031212051-054-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Feral — Cat DPS), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Faerie Fire**.

**Keep up all fight:** **Cat Form**.

**Then press the first one that is ready**, top to bottom:

1. **Ferocious Bite** (rank 4)
2. **Rake**: keep it on the target
3. **Faerie Fire**: keep it on the target
4. **Rip**: keep it on the target, when you have 4 or more combo points
5. **Shifting Power**
6. **Shred**

**Shred** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserk**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid cat keeps **Rip** bleeding on the boss, turns mana into energy with **Shifting Power**, and spends the rest on **Shred** from behind. **Faerie Fire** opens the fight, **Berserk** goes on the pull.

**Why it works**

- **Faerie Fire** takes 505 armor off the boss for 40 seconds, so your **Shred** and white hits land harder, and in **Cat Form** it costs nothing. Cast it on the pull. In a full raid the simulator assumes the raid keeps it up and casts it once a fight; if nobody else does, refresh it before it runs out.
- **Rip** does a large share of your damage (close to 40% on the training dummy). Put it back up as soon as it falls off, at 4 or more combo points: its attack power bonus stops growing at 4 points (the simulator's model, as in Classic), so the fifth point adds only a flat 153 damage while the boss goes without a bleed. The simulator measured Rip at 4 or more about 1% better in a full raid than waiting for 5.
- **Shred** is the filler: 42 energy with **Shredding Attacks**, 1 combo point, 2 on a critical strike with **Blood Frenzy**, and 10% more damage from **Rend and Tear** while **Rip** bleeds. **Rip** lasts 12 seconds, about the time three Shreds take, and those Shreds bring about 4 combo points with their critical strikes. So when Rip falls off, you usually hold the points to put it straight back.
- **Ferocious Bite** is not in the list: the simulator measured the rotation 1% better in a full raid without it, the energy going to **Shred** instead. With **Rip** up and 5 combo points, keep shredding; points beyond 5 are lost.
- **Shifting Power** turns 55% of your base mana into 40 energy every 8 seconds with **Improved Shifting Power**: cast it whenever it is ready and your energy is 60 or less, so none of the 40 spills over your 100 cap. A raid's mana buffs pay for it, and in the simulator's full raid this build (694 DPS) and the 9/35/7 build (688) both take it and do about 17% more than the 9/31/11 build without it (590).
- Tiger's Fury was removed (Blizzard's notes of 1 Oct; the 70425 spellbook lacks it), but the community simulator still reads it from the client as granted and casts it on every cooldown, so the raid numbers on this page run about 2-3% high until the simulator drops it.

**Caveats**

- **Shred** only works from behind. If the boss faces you, or you have to tank, build with **Claw** instead (110% weapon damage plus 126 for 45 energy, less with **Ferocity**).
- Without a raid's mana buffs (a dungeon group, or alone) each **Shifting Power** costs more than half your base mana and you run dry fast: keep the mana for a shift and a **Regrowth**. Solo, the fight lab found that drinking the mana back costs more time than the energy saves.
- Powershifting is nearly gone in Forever: instead of granting a flat 40, this build's 4 points in **Furor** give back 80% of the energy you left with, plus 8 a second spent out of form. The rotation shifts out only with Clearcasting up and under 14 energy, about twice a fight, and the simulator found almost nothing in it: skip it if it costs you attention.
- The bear builds under Other builds are tank builds: they play **Lacerate**, **Maul** and **Barkskin** in **Dire Bear Form**, not this list (the research rotation page has their priority).

**When to change it**

- When the boss will die before a new **Rip** can tick most of its 12 seconds (the last 6 seconds or so), spend the points on **Ferocious Bite**: its damage lands at once.
- On an add that dies within a few seconds, the same: **Ferocious Bite** rather than **Rip**.
- If you pull the boss off the tank, **Cower** (20 energy, 10-second cooldown) lowers your threat by a large amount.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 754 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 753 | this build |
| Phase 1 BiS | 754 | [9/33/9](https://talentsforever.com/druid/60/050022-55000032021031212051-144-7) |

**The gear** (average item level: Pre-BiS 63.9; Phase 1 BiS 63.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Shifter's Belt](https://www.wowhead.com/forever/item=272396) | [Shifter's Belt](https://www.wowhead.com/forever/item=272396) |
| Legs | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Molten Heart of the Mountain](https://www.wowhead.com/forever/item=249470) · *Enchanting* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Idol of the Moon](https://www.wowhead.com/forever/item=23197) | [Idol of the Moon](https://www.wowhead.com/forever/item=23197) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/feralcat/#eJzEVV1oHFUUnnN3dubuSdxMbtNmelEyWVS2o7Pcmc3G3SBkU3+q4kJIH/x5sbPZjbslZJfsCm2fFtuHUopgwWKKPthaCBohRBtqXxWskoc0asFSMf5QCiqIYMCXInMz28SQB19iz8Ny9px7v/m+c7/Lxb0UDDDBgiQcggrUoQVwEmAWgHXKFglaWeB/I9WNDn4UdfrXh2D+0oEqvfA2oEq/XjJQp59dBPOahjr9/JMu8+c46vT4DJjfB8nSkmH+EEeVnl42UKPfvRbs1umv78F6+duLAczcfDeq9NKygSq9804X6vSba4b5WxwVVOm7lyDxiPFFNXl7UqwVR6+/AaeAnKieAbJWPAf0gj/n3xw5e/ADIKerq3Ciur9zQ1cerpA+kRHC85xMRggh0p7wXJF2PdcTGdcRmYGrRF0m9CdyMoY9qPMoRujHhUQMdYw6bko07lZ/TIbVdCrTYGeAlfz65Cu1etPyhDfouMJxB4es8Yo/9Wq5ZNWmLb9UKpes4lGrWSlb07Wm36zWpqxG2Z8er1jJRrlsTZSn/Uln3G86pXrDaS9x1pekDjdqU/u4jf2sDzuCb3sBufkCGnacRhl5TuEaqkgGG5LffIHFeJsq6+d9uOcG2SXlMGJEOUUN1UBRqJE9wUcwywaRLkBQaWlIV9QgW6xiZwLb9cUqMtugEUaGlHWQnEgJCbJYZXHeuQEwpLArW+cico6X3YG5jOGz7IBkpjHyssLpn5FQReQUKPgoszH2laqhSm8dB4wtQDsNxRwLxbjpVG5sfSd76/8i7+CDLIG77G6qscjrEFJJpx7LbDrp2YIc8myBvbmVlysckdsBXvuwjz2AsRU5t99vjkqrqYwca1tN8LBz12u3nmcJbmHvDdKz4TV5UdyBTWbr5bs3m6qlBZuNswfZAf4UPs6G/t1E205Sle1eIIyCPF5EipqbEYH17lsgSFVZJkVFAq0V2dP8yf8M5HmZbYBUJKbJynwcX2IvbMHptruClUWF6xjFSFY8hAMJDwVP4R7WE94cY62I9DyEWQ9jqK+oEhX18yATOb+5T2H7gdCWZkZuk6vwB/EOE64k7pCYEkRrIr/33EwQXw73T8i4PuytElO1hu3LRLkn0cy3sx2Nhz/ase/k5O/Y+/mRsJA/FLyBMyD/KKvDdoRe7t1//8aTIiALeXgGRuFFqEAdjsAR8s8A+JtUcA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/feralcat/#eJzEVV1oHFUUnnN3dubuSdxOb9NmelEyWVS2o7Pcmc3E3SBkU3+q4kJIH/x5sbPZjbslZJfsCm2fFluhlCJYaTEFH2wtBK0Qog21rwpWyUMatWCpGH8oBRVEMOCLyNzMNjH0wZfoeRjOnHPvN9935rtc3E3BABMsSMMBqEID2gDHAWYBWLdskbCVA/4nUt3o4odRp3+8D+ZPXajS828BqvTLRQN1+skFMK9pqNNPP9pm/phEnR6dAfPbMFlcNMzvkqjSk0sGavSbV8LdOv35HVgrf30hhHntzfB5aclAlc6dBtTpV9cM85ckKqjSty9B6iHjs1r69qRYLY1efx1OADlWOwVktXQW6PngYnBz5Mz+94CcrK3Asdre7nVdBbhC+oQvhOc5vi+EEFlPeK7Iup7rCd91hD9wlahLhP5AjiewB3Uexxj9sJhKoI5xx82I5p3q9+moms34TXYKWDloTL5Ub7QsT3iDjiscd3DIGq8GUy9XylZ92grK5UrZKh22WtWKNV1vBa1afcpqVoLp8aqVblYq1kRlOph0xoOWU240nc4SZ21J5mCzPrWH29jP+rAr/LYXkpsromEnaZyRZxSuoYpksCn5zRVZgneosn7eh7tukB1SDiNGnFPUUA0VRRrZY3wEc2wQ6TyElbaGdFkNs4UadqewU1+oIbMNGmNkSFkDyYuMkCALNZbk3esAQwq7snkuIu94uS2Yyxg+zfZJZhojLyqc/h6LVMROgIIPMxsTX6gaqvTWUcDEPHTSSMyRSIybzeTH1nay0/8VeQfvZyncYW+nGou9ChGVbOYRf8Ofni3KIc8W2RubebnCEfkt4LUH+9h9mFiWc/v15qi0msrIkY7VBI86d7x261mW4hb23iA9616TB8Ud2GC2Xr5zo6naWrjZOLOf7eNP4KNs6J9NtO00VdnOecIoyN+LSFFzfRFa7555glSVZVJSJNBqiT3JH//XQJ7n3wVIRWKarMLH8QX23Cac7fa2cGVJ4TrGMZYTD+BAykPBM7iL9UQnx1gtIT0HUdbDGOrLqkRF/RzIRM7v4sdw94HQtmbGbpOr8BvxDhKupP4iCSWM9kRh99mZMD4f7p+QcX3YWyGmag3bl4nyv0Sr0Mm2NB78YMu+k5fPsXcLI1GhcCC8A2dAvigrw3aMXu7de+/6lSIgBwV4CkbheahCAw7BIfL3ACojU7k=).

## Tanking

**[Feral Combat (optimized, tank)](../research/raid/builds/opt-feral-bear-tank-raid-tank.md)** (9/42/0) — [open the talent tree](https://talentsforever.com/druid/60/050022-5520033212013201255--7)

Tank value 1.046 (threat and damage taken under a boss, relative to our reference tank build): 3139 threat and 360 damage taken per second in a full raid.

**The gear** (average item level: Pre-BiS 63.5; Phase 1 BiS 64.3; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cloak of Warding](https://www.wowhead.com/forever/item=18413) · *Tailoring*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Cloak of Warding](https://www.wowhead.com/forever/item=18413) · *Tailoring*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Shifter's Belt](https://www.wowhead.com/forever/item=272396) | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Stormshroud Pants](https://www.wowhead.com/forever/item=15057) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Sentinel's Leather Pants](https://www.wowhead.com/forever/item=22749)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Mongoose Boots](https://www.wowhead.com/forever/item=18506) · *Leatherworking*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Darkmantle Boots](https://www.wowhead.com/forever/item=22003)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Idol of the Moon](https://www.wowhead.com/forever/item=23197) | [Idol of the Moon](https://www.wowhead.com/forever/item=23197) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/feralbear/#eJzEVEFIFFEYnv/N7M7vb23TEDW+lCYPsS2MvEZHVi+7SodAhOjULUd3tl2T3WV2A70JIgQJdYrWCg8qxFaXSrGOFWHhwYg6eMnKQ4cCQzoWMbNaQV2l7/C//33/997/vXf4qQlBAwNMiMMA5KAE4wCXAG4D6HvCEgtKSeATEVS1Rj5GKn67A8ZGIyk4ex1IwdcrGqn45QoY72Ok4tOH+4yPQTJRBeOGSiqurGjGuxgpOLWqURRfXQxOq/jyKtTpN/PBNd+vBXFhVSMFNy8DqfhsHozPMZJIwVsL0NqsPc/HN2ZgGhpm3bvuWs/MPNQgOpX/2jKZ76XQLcQhDY9Zi3CEsC1H2EK0t9sngsUWwnYcSzgdy0xZZfiBzcm6wlm3pB/hLXRgje0nGR/060yL8CgpxOwyj9SpPwS1vwW1fv0k76Uk7ySeMFDW9z4BIgW3FvtCbYRkAoeMxEFUdByO1kscKUpKR5tT5tuMThzD/NFynz4JetYtjZwrliqmLexOS3RZdrLbHMq5hfNexiz6ppvJeBlzcMys5DzTL1bcSr5YMMue6w/lzHjZ88ys57sj1qDn+lbFLVywdkRWXdQ2XC4WjvPDpCViGNWZLwXtiTmCqxQxAav9uv8PG127YqP+9pv34dc/bC32GfIntgybzK7JjEutP1iDFGA8m26argZ4kTqaDfE2Za8zQzFTiSUm/RdU0jvZruLYvV3r0xXGM3Ppnm0iPRBMgyqEG2k9lZBx6VA306C3+ffgEJCENJyC03AWclCCURhlPwcAGFTBXQ==); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/feralbear/#eJzEVE1oE0EU3je7yU5fNa6D6HZscexBYmDLuO2WtJekxYNQCuLJm902G5NakrDJoXoqaMGD0IsKqUoPtiCpHvxpqR5VpEIPBdFDRazagwcFpXhUZDetCnoNfoc3b773zbxv5vCwhYIBJgiIwxDkoAQTABcBbgGwHWGJBKUk8AsRqhvN/Bzq9Ns8mBvNqNGNKUCNvlgxUKefp8B8F0OdPnmwy/wQJOerYF7TUacrK4b5NoYafX0FUKdv7obHdbo5D3X+5Vxwz/erQVxYNVCjq5cD5dM5MD/FUEGN3liA9lbjWT6+MQPT0HTTve2u9c3MQQ2il/Jf2ybz/RjahTik4RFpk46UtuVIW8rOTvtIsNhS2o5jSadrmWirhL4nsyrTOOlV2AHehnvWyG5U6f1BRowIj6KGxC7zSJ36Q1D7W1AbZEd5PyZ5N/KESVW28zEganRzcSDURlBFcNBM7KUao6PReolTjKLW1eGU+RbDkNMwf7g8wCaBZd3S2KliqSJsaXdbsseyk71iJOcWTnsZUfSFm8l4GTF8VlRynvCLFbeSLxZE2XP9kZyIlz1PZD3fHbOGPde3Km7hjLUtsuqijtFysXCY70cjEaNRRnwlaI/EkVzHiABaHWT+P2z0NMRG/e3X78Gvf9hcHDDVj2QZvhC7phKutP8gTUqAiWy6Zboa4HnqYDbEq5S9TkxNpBJLRPkvqKS3s4bi0J2G9ekJ44nZdN8WkR4KxkEVwo2ynkqodGlfLzGgv/X35JCQhDQcg+NwEnJQgnEYJz8HAAPTwhM=).

## Other builds of this spec

- [Feral Combat — Shifting Power](../research/raid/builds/feral-combat-shifting-power-raid.md) (9/35/7, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000032121032212051-052-7)
- [Feral Combat (optimized)](../research/raid/builds/opt-feral-cat-dps-raid-dps.md) (9/31/11, 643 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-25000332020032012051-055001-7)
- [Feral — Cat DPS](../research/raid/builds/feral-cat-dps.md) (9/32/10, 630 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000332120032012021-055-7)
- [Feral Combat (optimized, tank)](../research/raid/builds/opt-feral-bear-tank-raid-tank.md) (9/42/0) — [open the talent tree](https://talentsforever.com/druid/60/050022-5520033212013201255--7)
- [Feral — Bear Tank](../research/raid/builds/feral-bear-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-054-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

