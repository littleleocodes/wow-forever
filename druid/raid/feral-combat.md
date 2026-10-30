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
| Phase 1 BiS | 754 | [9/33/9](https://talentsforever.com/druid/60/050022-55000032021031212051-144-7) (ties this build) |

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/feralcat/#eJzEVV9oHNUXnnN3MnP3JL9kcpM008tPMllqSabOcmc2E5MgZFP/VMVASJGqL3Y2u3G3hOySXaHt02L7IKUIFiym6IOthaAphNWG2lcVW8lDGmvBUjH+oRRUEME8Fpmb3W6MefBl9TwsZ8+995vvfOe7M7ibggEmWNAHhyELBSgDvA6wAMBa5BIJl4aAf95CdaOZH0Od/vEhmD81o0ovvA2o0q9WDNTppxfBvKGhTj/7uM38sRV1emIezG/DZGXFML9rRZWeXjVQo9+8Gp7W6c/vwWb564shzOJSO6r08qqBKr3/Thvq9OYNw/ylFRVU6buXIbbP+CLXd29GbKQmbr0Bp4CczJ0BspE6B/RCsBjcGTt78AMgp3PrcDK3v6XeVxKukh7hC+F5ju8LIUTCE54rEq7nesJ3HeEPXCPqKqE/kJuInajzJozQj8ZjUdSxyXHjovig+n1ftZqI+0V2HVg6KMy8nC+ULE94g44rHG9wxJrKBrOvZNJWfs4K0ulM2kods0rZjDWXLwWlXH7WKmaCuams1VfMZKzpzFww40wFJSddKDq1Lc7mlviRYn62nwd4iD+P+1g/GnYr1VjkNVBCPgg+dsU6sN1uoxojzypcxyaMuKKIe9mev21OyEpEbtRQRZIocg1VeqkC7MwOvbiN6MXGXtaDzaGOXij00rhk1VRnNVgMe6NL4yzKa7KzXt6Du26TDjkaRowmTlFDNZxOdV7scT6GQ2wQaQXCSllDuqaG2XIOW2JYqy/nkNkGjTAyomyCDIu4kCDLOdbKW+oAIwq7ul0XMex4Qw3QZRKfYQckM42RlxROf49Uu4icAgUfYTZGv1TDcd09ARitQC2tNnO82oybiA9Pbp5kb/1b5B3cw2LYYbfX/CapJOKP+lsmvTAuRV4YZ29u5+UKRww3gFc/9rCHMLomdfv1zoS0msrI8ZrVBK+uPPDa3edYjFvYfZt01r0mL707sMVs3bxrq6nKWnjYOHuQHeBP4mNs5K+LaNt9VGVdFcIoyPEiUtRcX4TW+1+FIFVlmaTkXTU2Uuwp/sQ/BvI8fwcgFYlpsgyfwhfZoW044StDZeHj5CtjSDyMAzEPBY/jLtZZvTnGRgrpeahmnYyhvqZKVNTPg0ykfoufwM6C0LJmRu6Ra/Ab8Y4QrsTuk6gSRnk6ufvcfBjXR3unZdwa9daJqVqj9hWi/CdRStayhsbeSw17zrD8nXw/OVYtJA+H3/N5kH+U9VE7Qq907/9//fMoYAiS8DRMwAuQhQIchaPkzwEAqsuCqA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/feralcat/#eJzEVV1oHFUUnnN3MnP3JKbTm6SZXpRMllqSqbPcmc3GJAjZ1J+qGAgpUvXFzmY3ZkvILtkV2j4ttoKUIlhpMQUfbC0EbSGsNtS+qthKHtJYC5aK8YdSUEEE8yhyb3a7MebBl9XzMJw599wz3/nOd+fiTgoW2OBADxyEKShAGeANgHkA1qKWiFwaAP55CzWtZn4ETfrHh2D/1Iw6Pf8OoE6/WrLQpJ9eAPuGgSb97ONt9o+taNJjc2B/K52lJcv+rhV1enLZQoN+86rcbdKf34P18NcXZJnX35bPy8sW6nThNKBJb96w7F9aUUOdvnsZYnusL3I996bFWnrs1ptwAsjx3Ckga+mzQM+HF8M7I2f2fwDkZG4Vjuf2ttT7SsFV0iWSQgSBl0wKIUQiEIEvEn7gByLpe35f3zWiLxP6A7mJ2I4mb8II/Wg0FkUTmzw/Lor3o9/3VKOJeLLIrgPLhIXpl/OFkhOIoN/zhRf0DzkTU+HMK9mMk591wkwmm3HSR5zSVNaZzZfCUi4/4xSz4ezElNNTzGadyexsOO1NhCUvUyh6tRRvPSV+qJif6eUhHuDP4x7Wi5bbSg0WeQ00iQchiR2xNtzubqMGI89q3MQmjPiiiLvZrn8kJ1QkohIN1JEkitxAnV6qADu1RS9+I3pxsZt1YbPkMZBEL4wqVE11VP1F2RtdGGVRXqOddfMu3HGbtKnRMGI1cYoG6nI61Xmxx/kIDrB+pBWQkbKBdEWX3mIOW2JYiy/mkLkWjTAypK0XGRRxoYos5lgrb6kXGNLY1c28iEEvGGgAL+P4DNunkBmMvKRx+nuk2kXkBGj4CHMx+qUux3X3GGC0AjW32szRajN+Ij44vr6Tnf6vwHu4i8Wwzd1e05uCkog/mtww6flRRfL8KHtrMy5feGKwAbh6sYs9hNEVxduvd8aU1HRGjtakJnh15b7W7j7HYtzBztukva41dej9vg1i6+QdG0VVNuRm68x+to8/iY+xob8vouv2UJ11VAijoMaLSNHwk0JK74EKQaqrMEmrs2qtpdlT/Il/XSgIklsU0pHYNsvyCXyRHdhUR/4ydCY/p34ZA+Jh7IsFKHgcd7D26smx1tJIz0HVa2cMzRVdVUXzHChH8XfxE9iaEFo27Mg9cg1+I8EhwrXYnySqSStPpnaenZN2fbh7Utmt4WCV2Loz7F4h2v9ipVTNa6jtvtSw7wyq5/j7qZFqIHVQ3udzoF601WE3Qq907n2wfj0KGIAUPA1j8AJMQQEOw2Hy1wBKcYHx).

## Tanking

**[Feral Combat — Raid tank](../research/raid/builds/feral-combat-ml-tank.md)** (9/35/7) — [open the talent tree](https://talentsforever.com/druid/60/500022-5020033202003201255-052-7)

Tank value 1.056 (threat and damage taken under a boss, relative to our reference tank build): 4045 threat and 364 damage taken per second in a full raid.

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/feralbear/#eJzEVEFIFGEUnvfv7M7vM9bxJ2qclP48xLYw8vvrmnrZ1VMUQnTqlqM7267J7jI7gd4EEYKEOkVrhQcTYiuCypCuRVh42Ig6eMnKQ4cEIzoWMeNaUV3XvsM/b773zbxv3hsetlDQwQAOMRiGLBRhCuACwC0AtidIET/VC+Y9jWp6ozmJGv16G4yNRlTpwlVAlb5a1VGjm5fAeBdFjT552GR88IPpMhjXNNTo6qpuvI2iSmerOkboy/P+0xp9cRm26deL/mu+XfHPpaqOKt26CKjRp4tgfIqigiq9sQTtrfqzXGxjHuagYcG+Y68NzC9CBSKzuc9tM7lBDNxCDFLwmLSJhBDSSggpRFeX7PQvUgiZSFgi0b1C1Cqh70k1zFST9CvsoNmGe9dIM4bogyFG9LAZQRWJLJnhbeo3QeVvQWWIzQLL2MXxM4Wix6WQPVansOTRfj6atfNnnTQvuNxOp500H5nkXtbhbsGzvVwhz0uO7Y5meazkODzjuPa4NeLYruXZ+XPWjsjaFnWMlQr5I2Y7GvF9VGV0LIIq/fLohEkxgmp3R6Jk1hhW2jU3DaaGYQ60PMTcP4qKPkv21aUoDT70+n1g07vX9xbU41EaYsRVatMXwe+xGWMz/3LRUxcXB7A53kQjjBxX/M5jSIqfYzdCH8kKbBFZCRFTaf9OGhQfU5lUy1zZx/PkoUyAN0m5TgyVJ+PLRPkv8FI7UV1x+G7d6vQF56mbqYEakRr2N2cZghtlPRkP0eX9/USHwdZfS1ZAL6TgGJyE05CFIkzABPkxANxVKtE=); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/feralbear/#eJzEVE9IFGEUn/ft7M7nM9bxI2qclL48xLYw8vnpmnrZ1VMUQnTqlqM7267J7jI7B+skiNBB8FLBWuGhhFgL+mdI1yIMPCxEHYzIykOHhEI6FjHjWlFd136Hb9783m/m/ea94WELBR0M4BCDYchCESYBLgLcAmB7ghTxU71g3tWopjeaF1CjXxfB2GhElW7MAqr0xaqOGt2cBeNdFDX65GGT8cEPpspgXNVQo6uruvE2iip9fRlQo2/uBY9rdGsRtvmXC/57vl3xz6WqjiqtXvKVTxfA+BRFBVV6fQnaW/VnudjGPMxBww37tr02ML8AFYjM5L60TecGMbALMUjBY9ImEkJIKyGkEF1dstO/SCFkImGJRPcKUauEvifVMFNN0q+wg2Yb7l0jzRiiD4YY0cNmBFUksmSGt6nfBJW/BZUhNgMsYxfHzxSKHpdC9lidwpJH+/lo1s6fddK84HI7nXbSfOQ897IOdwue7eUKeV5ybHc0y2Mlx+EZx7XHrRHHdi3Pzp+zdkTWtqhjrFTIHzHb0YjvoyqjYxFU6dajEybFCKrdHYmSWWNYadfcNJgahjnQ8hBz/ygq+izZV5eiNPjQa/eBTe1e31tQj0dpiBFXqU1fBL/HZoxN/8tFT11cHMDmeBONMHJc8TuPISl+jt0IfSQr8JnISoiYSvt30qD4mMykWubKPp4nD2UCvErKdWKoPBlfJsp/gZfaieqKw3fqVqcvOE/dTA3UiNSwvzrLENwo68l4iC7v7yc6DLb+2rICeiEFx+AknIYsFGECJsiPAQCdWSuH).

## Other builds of this spec

- [Feral Combat — Shifting Power](../research/raid/builds/feral-combat-shifting-power-raid.md) (9/35/7, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000032121032212051-052-7)
- [Feral Combat (optimized)](../research/raid/builds/opt-feral-cat-dps-raid-dps.md) (9/31/11, 643 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-25000332020032012051-055001-7)
- [Feral — Cat DPS](../research/raid/builds/feral-cat-dps.md) (9/32/10, 630 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000332120032012021-055-7)
- [Feral Combat — Raid tank](../research/raid/builds/feral-combat-ml-tank.md) (9/35/7) — [open the talent tree](https://talentsforever.com/druid/60/500022-5020033202003201255-052-7)
- [Feral Combat (optimized, tank)](../research/raid/builds/opt-feral-bear-tank-raid-tank.md) (9/42/0) — [open the talent tree](https://talentsforever.com/druid/60/050022-5520033212013201255--7)
- [Feral — Bear Tank](../research/raid/builds/feral-bear-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-054-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

