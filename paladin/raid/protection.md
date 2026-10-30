# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-2530503200301551-50223030001-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds; it beat the hand-made build (Protection — Tank), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Seal of Righteousness**, **Holy Shield**.

**Keep up all fight:** **Seal of Righteousness**, **Righteous Fury**.

**Then press the first one that is ready**, top to bottom:

1. **Lay on Hands**
2. **Templar's Bulwark** when you have at least 25% mana
3. **Holy Shield**
4. **Judgement**
5. **Consecration**
6. **Holy Strike**
7. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 90% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

**Why it works**

- Before the pull: **Righteous Fury** (it lasts 30 minutes, and **Improved Righteous Fury** and **Iron Creed** only work while it is up), then **Seal of Righteousness** and **Holy Shield** in the last seconds, so the first hits already meet both.
- **Holy Shield** lasts 10 seconds and comes back every 10, so keep it up all fight: 30% more block for 4 blocks, and every block deals Holy damage with 20% extra threat and can trigger **Redoubt** and **Shield Specialization**'s mana. The simulator measured 1.3% more tank value with it at the top of the list.
- Press **Judgement** on cooldown, whether or not the short list shows it: it is off the global cooldown, judges **Seal of Righteousness** for about a tenth of your threat, and no longer uses up the seal in Forever. Judging every time it is ready, instead of only before the seal runs out, measured 4.3% more tank value; **Swift Judgement** goes right after a **Judgement**, because it finishes the cooldown and makes the next one free.
- **Consecration** and **Holy Strike** fill the rest: **Consecration** threatens everything standing in it, and **Holy Strike** with **Iron Creed** makes 25% more threat and cuts your damage taken by 10% for 6 seconds. Refresh **Seal of Righteousness** when it has about a second left.
- **Templar's Bulwark** sits at the top because the simulator's 3-minute fight fits one use: it absorbs damage equal to your maximum health for 8 seconds, off the global cooldown, and using it at the pull measured 1.4% more tank value. It applies Forbearance for a minute, which locks you out of **Divine Protection**, **Divine Shield** and **Blessing of Protection**.
- **Lay on Hands** is last in the list with no health condition: in the simulator's fights nobody heals you, and casting it whenever nothing else is ready measured 0.4% more tank value than keeping it for 10% health (8% more than not using it). It heals you for your maximum health but drains all your mana, and its cooldown is 20 minutes: in a raid with healers, keep it for when you are about to die.

**Caveats**

- The simulator tanks with **Seal of Righteousness**. **Seal of Fury** (35 Holy damage a swing, plus an absorb of half of it while you hold a shield) is not part of its tuned rotation, so whether it is better for you was not measured.
- Mana: you run dry for a few seconds of each 3-minute fight in the simulator. **Consecration** is the expensive button (565 mana before **Holy Conduit**); blocks give mana back through **Shield Specialization** and judgements through **Sanctified Judgement**.
- The simulator measures one boss. **Consecration** and **Holy Shield** work on everything that hits you; **Holy Strike** and **Judgement** only on your target.

**When to change it**

- To taunt (a tank swap, a loose add), put up **Seal of Fury** and judge: its judgement taunts for 4 seconds. Use **Swift Judgement** if **Judgement** is on cooldown, then go back to **Seal of Righteousness**.
- Hold **Templar's Bulwark** for a known damage spike or a healer death when the fight has one: the simulator spends it at the pull only because its fight fits a single use.
- Undead or Demon packs: **Holy Wrath** (a 2-second cast) hits and stuns every Undead and Demon within 20 yards, and **Exorcism** hits one hard. Neither was measured: the simulator's boss is an Elemental.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Tank value 1.068 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 63.2; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Stalwart Watcher's Signet](https://www.wowhead.com/forever/item=275984) | [Stalwart Watcher's Signet](https://www.wowhead.com/forever/item=275984) |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) |
| Trinket | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVN9LHFcU3nNndufuWXHXW2XHaYVxwXa7MHJ31m3Vlx196uPSp77V0V2729rdZWcf7FO1IBRain0p1bYqrEvF/JBIAkYiBEJEn5KXJCDEmGggBCEmf0AId1yjJK9qvofLnfOdud93zz0c/IRCCFTQIQoDkIMSjAH8CjAHsADAGlyWCLYbtL8olUNEGwdU6NNaUN0LoEyrfwPKdOtfEbwzCerjRlTobi2o7orNg1pQ/UdBhV6vBdVHjSjT5xdE5p9XQPyu0FtH8Xs1cc7kfghlunJXrAe/icwXl0HdF0dtTzSp2yKzeg0i7aH1fHRvFqbBX7Uv2lt9szVYhMDv+ZdtiwvwR34i34+ud4iCBaukzTCTCZ7kCZPzBI8nk3EjyU0zwROc8/gGkZ+QOR82I9V8KNOrmxCh6EPZSHAHw4gaRV+U0tszEPGjgl4j0Zl0sKVOSPRmFSIKelEyTIf9yAbs0si3xVJFN7n5hRHnRryrVx/K2YXvshm9WNbtTCab0Qd/0iu5rF4uVuxKvljQnaxdHsrpUSeb1UvlYsWo2IUfjCPaOKQ7v3eKhc81v6agNyrR9TT7+X0588tTlvsYm2JB6mNk0COEUTKTHW6l/v8lzQrvGOA9htl9ygZOFJrJGun1sJFzUD3shqUZYJ9pHdgaC1OZBVbhbTMIGkncOW4P1lC36qU3qsAC9Yei9GGazcM5vJSFXZrpWgUWmCbCikSX1upWuYMtsY+oxLyvFEIl4RRl3mk69fIurQELay3oXwZx87n/4LjuqvSMbMABMcclj4tmaxlkJOiJvCZ+EfCMDVut01MCm6n2YRf3U+YOUWU9FVshng+CinW0O1N8eunMdHrc9et5q68esAbEjJ4C98Ozk4pJdCXcS0LQf2Kcc+gGC76CNHwDOSjBKIySNwMA7wc1lw==); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVNFLW1cYz3fuTe7JFzHxTMn1bsI14JYFrpzcmE19ydWnPYY97W1eTVyyuSTk5sE9TQfCYGO4h43pWhViqNgWqbRgpUKhVPSpfWkLQq2tFkrxwfYPKOVcY5X2Ve3v4XDu9/vu+f3Odz4+/IxCCFTQIQoDkIMSjAH8DjAHsADAGlyWCLYbtH8plUNEGwdU6PNaUN0LoEyr/wHKdOuCCN6bBPVpIyp0txZUd8XmUS2o/q+gQm/WguqTRpTpy8si8+9rIH5X6J2j+IOaOGdyP4QyXbkv1oM/RObOP6Dui6O2J5rUbZFZvQGR9tB6Pro3C9Pgr9pX7K2+2RosQuDP/Ku2xQX4Kz+R70fXO0TBglXSZpjJBE/yhMl5gseTybiR5KaZ4AnOeXyDyM/InA+bkWo+lOn1TYhQ9KFsJLiDYUSNoi9K6d0ZiPhRQa+R6Ew62FInJHq7ChEFvSgZpsN+ZgN2aeT7Yqmim9z8yohzI97Vqw/l7MIP2YxeLOt2JpPN6IO/6JVcVi8XK3YlXyzoTtYuD+X0qJPN6qVysWJU7MJPxhFtHNKdPzrFwpeaX1PQG5Xoepr9+qGc+fUpy32KTbEg9TEy6BHCKJnJDrdSl35Ls8J7BniPYXafsoEThWayRno9bOQcVA+7YWkG2BdaB7bGwlRmgVV41wyCRhJ3jtuDNdSteumtKrBA/aEofZxm83AOL2Vhl2a6VoEFpomwItGltbpV7mBL7BMqMe9rhVBJOEWZd5pOvbxLa8DCWgv6l0HcfO4iHNddlV6QDTgg5rjkcdFsLYOMBD2RN8QvAp6xYat1ekpgM9U+7OJhytwhqqynYivE81FQsY52Z4rPr56ZTo+7fjtv9dUD1oCY0VPgfnh2UjGJroR7SQj6T4xzDt1gwTeQhu8gByUYhVHydgAbGDVv).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-5530513300301051-50025030001-7)
- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/31/20) — [open the talent tree](https://talentsforever.com/paladin/60/-5531513101301011-50225220011-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

