# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (16/33/2) — [open the talent tree](https://talentsforever.com/rogue/60/00530310301-30531300001515231-002-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0, 629 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--7)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point).

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Cold Blood** right before your finisher
3. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
4. **Backstab** (rank 8) when Cutthroat is not active
5. **Adrenaline Rush**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Blade Flurry**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- **Vanish**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Combat in a raid is an energy rhythm: build combo points with **Backstab**, keep **Slice and Dice** up for its attack speed, and spend everything else on **Eviscerate**. **Adrenaline Rush** and **Blade Flurry** go on cooldown.

**Why it works**

- **Slice and Dice** comes first: 30% more attack speed for the whole fight is worth more than any single hit. Put it back up the moment it drops, even with 1 combo point: it lasts 9 seconds at 1 point and 21 at 5, and **Improved Slice and Dice** makes that 45% longer. Do not refresh it early: while it is up, 4 or more points go into **Eviscerate**, and the simulator found no gain from refreshing it at 5 points before it runs out.
- **Eviscerate** goes at 4 or more combo points, not only at 5: its damage grows by the same amount per point, so the fifth point adds no bonus. A **Backstab** at 4 points often wastes a point, since **Puncturing Wounds** gives it a 45% chance to add a second one, and **Ruthlessness** adds a point after 60% of your finishers, so finishing more often collects more of them. The simulator measured finishing at 4 or more 0.9% better than waiting for 5 with daggers, 0.7% with swords.
- **Cold Blood** spends no combo points. It makes your next attack a sure critical strike, so the rotation times it right before an **Eviscerate** at 4 or more points, your biggest hit.
- **Adrenaline Rush** doubles your energy regeneration for 15 seconds: press it whenever it is ready. The rotation used to hold it for low energy, and pressing it on cooldown measured 1.5% better.
- **Backstab** is your only combo point builder and your filler: everything above it only spends what it builds.

**Caveats**

- **Backstab** needs a dagger in your main hand and you behind the target. If you cannot get behind the boss, or you hold a sword, build with **Sinister Strike** instead (the swords setup on this page plays that way).
- When your energy is nearly full (79 or more) and you hold 4 or more points, **Eviscerate** even if **Slice and Dice** is down so no energy goes to waste, then put **Slice and Dice** back up with the next points.
- **Blade Flurry** copies your hits to a second target for 15 seconds. On a single boss it is still worth pressing on cooldown for its 20% attack speed; with adds, it is your best cleave.

**When to change it**

- In the last 6 seconds of a fight, skip **Slice and Dice** and put every combo point into **Eviscerate**: a buff that outlives the boss does nothing.
- If the boss is about to die and you hold only 1 to 3 points, an **Eviscerate** still beats keeping them.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 683 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 685 | [16/33/2](https://talentsforever.com/rogue/60/005303103001-30531300001515231-002-7) |
| Phase 1 BiS | 682 | [17/32/2](https://talentsforever.com/rogue/60/005303103002-30531300001514231-002-7) |

**The gear** (average item level: Pre-BiS 63.7; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVl1sFNUX3zO7zN5eynaZ//8Py/B12L/RtunCzG4XaBvTbWlFlGhD1fRNbnfu7gzdndnM3C2sTygJMfETEz/ggfiBiVFJCH4RHnzBGEx4AFSeNKKYSJQHgsrDhqi501bKh/hgiudh5s65597zO7/zkaHLCCQhBQjtsBVsqMFOgCcBXgV4C0BrDXcVubse9FcWEiUZ03cCjZNf34HU9/NpjOw+CDRGPj+RpHGy/2QydUqlcXLs/bbUuQSNk117IfW1XJw4kUx9k6Ax8tTJJFXJmbo8HSc/vQZT6i/flNc8cyFJY+SDk/J56EXp54tTydSFxNVFjJw+lUyvTh532s9XjCt9I2eehbFftr4AypW+fUDeYO+yrwZeGn0blKedQ3B2+AhceB0GW69GWYCjStow8jkjZxo5wzAzOSOfM3OGYRhm3sxnc2bGMLLHldh3ynNt2g+gbWO1yqNeTWDWyK7NmEYm292LRZu5ZW6h5yOzLG7heAOFzdH3BBOO52LAmV+0sT3gHItedZyJjMXKZe4HGZ85VmbGMDNluHpb4LkdeoPWNJfq6RRd1FT/Qxc+HHAcqI7XAxsfrHGX+zTdVFfS5VI/KjirCHvNI8x1AhtLno9DrMrKnK5sqsuovqHu+9wVOOI5rgiwwoMAhc1czNP56RYaz86jUbJvTJ96ab/f3kifB7obtF1AB/UCTXYmSExTHovoKo1RxczTLq2TtpyOqTRGDlzafL1BNk/nHwYytZkCerfeF5pEtegTEJERUchRvakupv8b3lHzAo4Z3Oxtx6G6H4K+5ri0T17p016+ngGjJ5NdP2cMdFDUVoSw1Vmwuyk9DHE6r10hl7slMvKtq318e5GN0I3a8E2Qmfqa2eimLf7Myroe2ta5gEQ15b7pI2vlixwY0w4q2nmYqSpzLdZYmSOrW47AQXNdbwiaM7/SQJ+XfB7Y2J4PqfSwFpZvF9Zdi/uYQ1nJJdGBPq96k9yaOjs86QRF7jPBseK4PEA27k1yFGyCo7Bl/qeuwZLjB6ILAw8dgS6f5L5UcQvbs0aXYRhYcsq2CLow4NxCswulSQPH607FQq8UOuOu8Bu96FjcFU6RVXBoZBS3O8L26gId0aEXaF7L3cCfSRPp1mv4k2yps9ma2dHei97WZvxEoUcV7SOFtqUXzLTGz/uXpYAubKoJ2irHzSArTgSCjf/9dPkU9GMwa4iNukN4D6tUcFO16rjcFXSDNkD/37mKzAtbeslhZREBjVyKymq53K1Pr/aM3fKSdBrpiqa6lC4ZCJMt3YSzDh+yZQl5FYtiU11Ol25ycUjy5ssMDrvcLzdwA6vVHLd8yyFxV1O9g6Y3ul6V43Dd5xMMMzhQFM4kly33gCdwC2dWQ6aP7BnT6jcmzeiZs6TFQ7cfTmhJPTG7rHoj2pa/aOH8P2jhyZsEZ85ZcEQOenLx3P1aix6f5jcVPa8ch4tK9vFoJJT/Fn6EGFVoJP2b0iIVkZ2lwpJ9e6V81r+qFMqZ/uxZJRXD/s4jSuRfEVGYWc2p3Hlwzvz0hM8tBwoD04rCVvmXuBfCj8jZ/s4oObJ4cNbPpAHroQD3wgiMgQ012AE7lD8GABFcg5U=); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVl1sFNUX3zO7zN4eSrvM/y8sw9dhNdo2XZjd7QJtY7otrYgSbaiavsl05+7O0O3MZuZuob6IEo2JRkSDBh6IH5gYlYTgF+HBF4zBhAdA5UkjColESSSoPGyImjtttXyID6Z4HubeOffce3/ndz5ycQmDBCSBoAU2gw1V2A7wDMCrAG8BaI3hqiJX14K+ez5TEjH9cYyzX9+B5Lm5GGPndgLG2OfHExhn+04kkidVjLOj7zcnzzZhnO3YA8mv5eT48UTymyaMsWdPJFBlp2tyd5z9+BpMqr98Ux7z1Evy+8GJBMbYwd2AcfbFyUTyQhOq7KeiHGPs1MlEamXimNNyvmJc6R48/TwM/7L5RVCudO8F9ob5rvlV78tDb4PynHMQzgwchguvQ1/jXz4W4IiywjDyOSOXMXJGJp0z8rlMzjAMI5PP5LO5TNowsseU2HfKzmbte9C2mNXKo15VUNbIrk5njHS2o4uKtumWuUWeT6ZlcYtGJkjYnHxPmMLxXAq46Rdtagk4p6I3NmKKtGWWy9wP0r7pWOlpw/Sk4cotgee26hNY1VzUU0lcUFf/h/MfDjj1jo3UApserHKX+5iqq8txqdQPCW5WhL3qEdN1AptKnk/95phZ5ri8ri5BfV3N97kraNBzXBFQhQcBCdt0KY9zUw0Yz87BKNs7rE8O2u+31tMXAJ8GbQdgn17ARFsTi2nKYxFdxRgqmTy2a23YcCqmYoztv7TxWoNsHuceAja5mAS8W+8OTaJa9EmISI8QcqjX1YV428C2qhdwStNGbyv11/wQ9FXbpX3iSrf2yrUMGJ3p7NpZY6AVSVsWwlZnwO5APARxnNOisMsdEhn71tU+vrXIBnG9NnADZBl91Ux0UxZ/RmVNJza3zWNRTblvastqObD9w9oBRTsP01mVWU1Vs8zJrFmOoL7Mmq4QNDf9ygT5vOTzwKaWfEilR9Uwfdup5lrcpxzJTC6JVvL5mDfOrcm9A+NOUOS+KThVHJcHZI5445yEOcpJ2DL+k8dQyfED0U6BR44gl49zX6q4RS1Zo90wDCo5ZVsE7RRwblGmnaTJBI3UnIpFXim8jLvCn+gix+KucIpmhfoHh2irI2yvJsgRrXoB81ruOv4y2JRqvIo/yZY6k63pFe296C0txk8UPKJoHynYnJo3XRo/71uSBJxfV5uwUbabPrM4Gghz5J+7y6egH4UZTWzI7ad7zEqFNoyNOS53Ba7TevH2thVsTljSiw4pCxho7FJUZsvlDn1qtmv4poekUoTL6upiXNQbBlteE/Y6esiWKeRVLKS6uhQXb3CpX/LmywgOuNwvT9A6s1p13PJNm8RddfUOTK13vTFOAzWfj5qUpt6icMa5LLkHPEGbuGlNyPCxXcNa7fqgGZ2zFrR4eO2Ho1pCb5qZVl0RbdPflHD+X5Tw+A2cy8yac0w2enbx7P1agx6f4jcZPa8cg4tK9oloJJT/F36AGCoYSf2mNEhFZHupsGjvHimf9awohXK6J3tGScaop+2wEvlPRBSmZ7Mqdx6YtXs6w++m/YXeKUVhs3wi7oHwJ3Kmpy3KDi/sm/GSNGAtFOBeGIRhsKEK22Cb8scACnKCyw==).

## Other builds of this spec

- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (16/33/2, 677 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323102-30531300001515231-002-7)
- [Combat (optimized, daggers)](../research/raid/builds/opt-combat-daggers-raid-raid-dps.md) (17/32/2, 663 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323121-30531300000515231-002-7)
- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (19/32/0, 625 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303125-32403300001515131--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

