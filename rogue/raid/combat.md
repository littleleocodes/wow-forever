# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (16/33/2) — [open the talent tree](https://talentsforever.com/rogue/60/00530310301-30531300001515231-002-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat — Swords](../research/raid/builds/combat-swords-open-raid.md) (18/33/0, 679 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303103003-32403300001515231--6)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point).

**Then press the first one that is ready**, top to bottom:

1. **Cold Blood** right before your finisher
2. **Eviscerate** when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
3. **Adrenaline Rush**
4. **Backstab**

**Backstab** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Blade Flurry**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
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

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 695 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 644 | [16/33/2](https://talentsforever.com/rogue/60/005303103001-30531300001515231-002-6) |
| Phase 1 BiS | 696 | this build |

**The gear** (average item level: Pre-BiS 63.4; Phase 1 BiS 64.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Hood](https://www.wowhead.com/forever/item=16908) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Shadowcraft Spaulders](https://www.wowhead.com/forever/item=16708) · *Cannon Master Willey, Stratholme* |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Shadowcraft Tunic](https://www.wowhead.com/forever/item=16721) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Shadowcraft Bracers](https://www.wowhead.com/forever/item=16710) · *Instructor Malicia, Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Aged Core Leather Gloves](https://www.wowhead.com/forever/item=18823) · *Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Shadowcraft Belt](https://www.wowhead.com/forever/item=16713) · *Blackrock Spire* |
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Shadowcraft Pants](https://www.wowhead.com/forever/item=16709) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Core Hound Tooth](https://www.wowhead.com/forever/item=18805) · *Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVU+IG1UYzzczTV6f23QYBKdB5HMPkg07+ibTbJvtIdnFouhlSz30ZmczL5nXZmfCzEvc9SBVEYRahB7UFQ+Cl4oWSv2DePGgQgoRduvqqSJaD4vkEAQ9VZCZZO2q9aQrfqdvfu/3vd/3/d5jHp0ioIMJCEVgYBz6/UthcBTqsASnoAPnAAqj/UTRtcIzNEd+fgfMH+6iKnlvlWrky4FOs+QN39zM0hz59P2D5s08zZHn18H8JkkGA938Nk81cn5Dpzly5WJanCMvDw+M8V9fAaqRC0OdquTCCtXIBylxa1M3h8kGn22kiUaub+rTJb0vzJdEcbvNbh2rw9L563Dq6hZcBOXWsdfgLfdNeNe9BDcW+gCL9PZsHyvTjFUc5tjMYcy2HFZxbIcxxuyKXSk7tsVYua9o3yujnPEqGGfcTvvJsCOxzMpzFqta5aPz2PDdoMU9DCN0PY97uLyG0ucYhdKVIgww5m7U8LEYc46NcGXZlZbntlo8iq3IFZ61Q7TGxAfPxGEwU5ihaNxH9VKeZA31OcgU9lGVwmFKr0KO7isq5JfDCUS+C4xP/tvOTtBHjON36MwuPLS7uwlDeTpTyFKNKkeq9GDpAFEN5bFJyVyyQC79BMZlxdiG1FSbWfYcdtwWR7frCYmL9pH51E/uRu01jHgz4rGPxUrqZYidUAQynsVu4PEIHYyxzZtyBiO+Eva4N6493hNxg0eu5NgWAY/RXQ57HKV7lqP0w5hPtsGmiGI5i3GIQmLAezxKIO5hscxmGWPYFC0/kYs599CexYSyhstd0fYwbKZiPJDR2jwKjwdSNNw2Prx0Ep8S0g+7EoWcKdRpxXD+YqBN89NTfzAwsSu7266dFaP7pwO3mcWqe3bguUSffHjW0Av53Q3OZ4yTf3MbKv/kNvTuMJ29Z9ORVHd083GDTvKtz8FUt5U+jJTys2omjbvrP4JGFZqZflvdnwCZc836odfXk7hWu7+Zxte18kgxNayV+krmfxWyvpPtaTxw+V/XqX4xGAymTl+pL0yA+ml4EWAdRDh64doTX9WqKZrZqC0kzMFgWDsxTm7USir56J7Fe2//8MfP16PpA+ZDB1Zh1fhtAEaNiL0=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVUGIG1UYzj8zzbw+1xgGwWkQ+bsHyYYdfZNpts32kOxiUfSypR56EOxs5iXz2uxMmHmJXQ+yBhdFK0J70IoHwUMruKA9iHjxYjULEaxUTxXR9rBIwSDoqQeZSdauWk+64n/653vf/77//95jHp0ikAcTEIrAwNj3+5fC4BDUYQmOQwfWAAo/7SVKXis8R3Vy5gUwb9xFNXLjNaAa+bQPNEve8s0rWaqTK30wr+eoTj7rg/ltkrx4DszvclQjm32gOrncT6t18nl/gl9YT7b54GWgKnl1harkwlNUJ2vnwLyZ1P9yNk00srEO06X8QJhnRHGrzW4drsPSK1/B8UtX4Swotw6/Ae+4b8N77kW4tjAAWKS3Z/tY2c9YxWGOzRxmWw6rOLbDGGN2xa6UHdtirDxQtB+UkW68DsZJt9N+OuxILLPynMWqVvnQPDZ8N2hxD8MIXc/jHi6vovQ5RqF0pQgDjLkbNXwsxpxjI1xZdqXlua0Wj2IrcoVnbROtMfGhk3EYzBRmKBoP0HwpR7KG2odMYQ9VKRyg9BLodE9RIb8eSCDyfWB88t92dpQ+ahy5Q2d24eGd3U0YyrOZQpZqVDlYpfeU7iaqoTw+KZlLFsjFn8HYUIwtSE21mWXPYcdtcXS7npC4aB+cT/3kbtRexYg3Ix77WKykXobYCUUg41nsBh6P0MEY27wpZzDiK2GPe+PaIz0RN3jkSo5tEfAY3eWwx1G6pzhKP4z5ZBtsiiiWsxiHKCQGvMejBOIeFstsljGGTdHyE7mYcw/tWUwoq7jcFW0Pw2YqxgMZrc6j8HggRcNt4yNLx/AZIf2wK1HImUKdVgznLwbaNDc99QcDE7uyO+3aXjG6fzpwm1msumsHrif65MNTRr6Q29ngfMY49je3ofJPbkPvDtPZuzYdSXVH158w6CS/ehlMdUsZwEgpP69m0ri3/iNoVKGZ6XfVvQmQWWvW9715PonN2v5mGt/UyiPF1LBWGiiZ/1XI+na2q/Hgxr+uU/1iOBxOnXi/vjAB6ifgJYDzIMLR+uaTX9eqKZr5sraQMIfDm7Wj4+RaraSSj+5bvP/2/378ej2Wvl8+dOA0nDZ+GwBXK4Ru).

## Other builds of this spec

- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (16/33/2, 688 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323102-30531300001515231-002-6)
- [Combat (optimized, daggers)](../research/raid/builds/opt-combat-daggers-raid-raid-dps.md) (17/32/2, 673 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323121-30531300000515231-002-6)
- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (19/32/0, 667 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303125-32403300001515131--6)
- [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0, 666 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-16 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

