# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (16/33/2) — [open the talent tree](https://talentsforever.com/rogue/60/00530310301-30531300001515231-002-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat — Swords](../research/raid/builds/combat-swords-open-raid.md) (19/32/0, 607 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303103004-32403300001515221--7)

## How to play

**Before the pull:** **Blade Flurry**, **Stealth**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**
3. **Adrenaline Rush** when Slice and Dice is active
4. **Blade Flurry**
5. **Cold Blood** right before your finisher
6. **Eviscerate** (rank 8) when you have 5 combo points
7. **Backstab** (rank 8) when Cutthroat is not active

Between these, your white swings do the rest.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 651 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 741 | [16/33/2](https://talentsforever.com/rogue/60/005303103001-32030320201515231-002-7) |
| Phase 1 BiS | 744 | this build |

**The gear** (average item level: Pre-BiS 66.5; Phase 1 BiS 66.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Grand Marshal's Dirk](https://www.wowhead.com/forever/item=18838)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Dirk](https://www.wowhead.com/forever/item=18838)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Razor](https://www.wowhead.com/forever/item=18840)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Razor](https://www.wowhead.com/forever/item=18840)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (16/33/2, 645 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323102-30531300001515231-002-7)
- [Combat (optimized, daggers)](../research/raid/builds/opt-combat-daggers-raid-raid-dps.md) (17/32/2, 630 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323121-30531300000515231-002-7)
- [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (20/31/0, 598 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005323101005-32502300000514231--7)
- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (19/32/0, 592 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/005303125-32403300001515131--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

