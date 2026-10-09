# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (16/33/2) — [open the talent tree](https://talentsforever.com/rogue/60/00530310301-30531300001515231-002-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0), 704 DPS in a full raid — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--6)

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 3 seconds left).

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

- **Slice and Dice** comes first: 30% more attack speed for the whole fight is worth more than any single hit. Put it back up the moment it drops, even with 1 combo point: it lasts 9 seconds at 1 point and 21 at 5, and **Improved Slice and Dice** makes that 45% longer. With daggers you do not refresh it early, because 4 or more points go into **Eviscerate** while it is up; the swords rotation refreshes it at 5 points with under 3 seconds left.
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 735 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 672 | [16/33/2](https://talentsforever.com/rogue/60/00530310301-32330310001515231-002-6) |
| Phase 1 BiS | 720 | this build |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 63.3; Phase 1 BiS 64.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Hood](https://www.wowhead.com/forever/item=16908) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Shadowcraft Spaulders](https://www.wowhead.com/forever/item=16708) · *Cannon Master Willey, Stratholme* |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Shadowcraft Tunic](https://www.wowhead.com/forever/item=16721) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Shadowcraft Bracers](https://www.wowhead.com/forever/item=16710) · *Instructor Malicia, Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Aged Core Leather Gloves](https://www.wowhead.com/forever/item=18823) · *Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Shadowcraft Belt](https://www.wowhead.com/forever/item=16713) · *Blackrock Spire* |
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Shadowcraft Pants](https://www.wowhead.com/forever/item=16709) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Core Hound Tooth](https://www.wowhead.com/forever/item=18805) · *Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE9IHFcYn29mduf1q67Do8XpUMpoi6wL076Zca2rpbsKpaW9KO3BWx3d1V2ru8vu0movtf9swUrFQ1t7KC29WNqCmBCClxySwBomsBqTkyEk5iBhD0sgORkIM7u6JianxJDvMt/83u/3e7/3HnzYQEAGBTQIAgP6+sEfz6ALYtAPgzAEScjCDMCPAAsA6iwhvCyqX6FE7vwLys0XUSAnplAklxwZJfJHSVY2/CiRsyeblJ0ASuTbJVCuuo3jyMq1AIpkruQyVxY9tUR+LjdW8Xu/AIpkviyjQOYnUSR/LQBKZGtDVsquwbmS14hkc0NuDcnFlPJTKrg7wfZ6YtA/twmDq1uwCPxez2/wt/0n/Gcvw3ZvEaAP68dc41sYC1vMMpjFDN0yLa9nzAgbYdMydMbMIi/e4Gf99Feg43Z24tNMtqCZzOzUWUQ3u7q1kaSdHkvEtUxOs+PxRFwbntYKyYSWyxTsQiqT1vIJOzeS1IL5REIbyUwO2wU9bo+NJXJ5PWen4vo+Ua8S3xzPZ9Ltajtq9DWUQwHip8I3wKk+FBA6EFdBQl+QJ3c7XIhcT9MzzzbZAL5P33tEMkN963C6GoP/klP9KCL/dgSbQo1EoPyHNUmnu0CWbwP9AdTvAKfVLzBMrSPWBgZaGx6wdo38h4zwXfrOEVkYm0MvE4Hi2oGwSre8IL66PqLuE6h7iDb6hmcm1MOHIzVEuOCriQz3Q059RmU1cDhcN0c/fswdhZ/kjj5/6JENpjPj2B6ZePtWdj6iWOu3zoMi7PJFqPDm1wLn1UuxWyAij1zrP8ILLsDNjMZe+X3JrfVoy6hXV6JmhVckLRoq8txzVYXYfnes1fb/U98nctFxnIahlVhvDYgNuSN5CVKZyvfrn1yORjyUK0V7XabjlKMD1WY7GhLI6ea+V+tTsDreP/AGfBKyMAVT9P4AzCsgLA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVEFIHFcYnn9mduf1r90ujxanQymjLbIuTPtmx7Gulu4qlJb2orQHD4U6uqu7VneX3aXVHopZ3BgSQ4IeEkMOgRw0ECHxEIKXXGKyhg3EYHIyhEQPEjwsgeTkIczs6pqYnBJD/sv8873v+9733oMfawh4QQYVfMCAfr37xzNogTB0Qjf0QAxSMAZwBOAkgJInhPeKyv8okclxkDc+RpFsnAAUyfUcoJucjckrbpTISg7kdQ9K5EYO5Ad2MzEN8kMPimQ5ByiRpZyjlsjNXAWfzds2l48CCuT4MApk9k+UyNg0yFu2/tmU04hkPg/1fm8hLk/GfZtDbLstDJ3H7kL3wipMAb/ddhrOW+fgojUHa+0FgA6snnKRr2PMNJihM4PpmsFMQzcYY0w3dTNg6BpjgQIvPuYPu+kpoINWauivZCqrBligWWNBLdDSqvbFrMRANKIm06oViUQjau+omo1F1XQya2XjyYSaiVrpvpjqy0Sjal9yuNfKahFrYCCazmhpKx7RdohamfjtYCaZaFQaUaVfodfvIW4q5IBTXCggNCEugIQuH0+eN9kQeZSg195vsi78mf70mmS68t3edBUG/x+nuFFE/vsgfur/hAiU/7UiabYXyNxToBOgjAOOKv+iSY191jp66mtesraN3HuM8Ef6wz6ZibX+z4lAcXFXWKYbThBXVR9UdgjUPkQD/cYxE6rhzWAFEW65KiLd/pArf1Ov4tkbrpWjv7/hjsy3uaN/XnlknWlMP7BHJs6+pfXfKFb61SWQhU2+ACU+cEjgnPos/ARE5JGrvyB8ZAPcWH/4izMzdi2H6vqduh8KlHhZUkP+As99UJUN73QHWg3z73yf4O1isVjTcyncXgHCPfZEnoF4spRf/uNeKOig3J1Qu80sFrdCXeVmLeQXyNXaji+rU7A83X9x5nsMUjACI/TFAEe/G/U=).

## Other builds of this spec

- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (16/33/2, 728 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323102-30531300001515231-002-6)
- [Combat (optimized, daggers)](../research/raid/builds/opt-combat-daggers-raid-raid-dps.md) (17/32/2, 713 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323121-30531300000515231-002-6)
- [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0, 704 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--6)
- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (19/32/0, 703 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303125-32403300001515131--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

