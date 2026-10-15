# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/32/19) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513301301151-50222230021-6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds; it beat the hand-made build (Protection — Tank), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Seal of Righteousness**, **Holy Shield**.

**Keep up all fight:** **Seal of Righteousness**, **Righteous Fury**.

**Then press the first one that is ready**, top to bottom:

1. **Templar's Bulwark**
2. **Holy Shield**
3. **Judgement**
4. **Consecration**
5. **Holy Strike**
6. **Lay on Hands**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Swift Judgement**: whenever it is ready: it finishes the cooldown on **Judgement** and makes the next one free, so judge again at once
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Most of your threat is Holy damage, and **Righteous Fury** makes it 60% more threat. Keep **Holy Shield** up, judge **Seal of Righteousness** on cooldown and press **Consecration** and **Holy Strike** whenever they are ready; **Templar's Bulwark** and **Lay on Hands** are your big defensive buttons.

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

## The numbers

Tank value 1.042 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 59.5; Phase 1 BiS 62.2; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five, so these sets were chosen with Classic's armor values filled in for the rest, our assumption: Forever may have changed some; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Helm of Awareness](https://www.wowhead.com/forever/item=18313) · *Zevrim Thornhoof, Dire Maul*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Helm of Awareness](https://www.wowhead.com/forever/item=18313) · *Zevrim Thornhoof, Dire Maul*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Evil Eye Pendant](https://www.wowhead.com/forever/item=18381) · *Immol'thar, Dire Maul* | [Medallion of Steadfast Might](https://www.wowhead.com/forever/item=17065) · *Magmadar, Molten Core* |
| Shoulders | [Stoneform Shoulders](https://www.wowhead.com/forever/item=13955) · *Kirtonos the Herald, Scholomance* | [Stoneform Shoulders](https://www.wowhead.com/forever/item=13955) · *Kirtonos the Herald, Scholomance* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Deathbone Chestplate](https://www.wowhead.com/forever/item=14624) · *Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Deathbone Chestplate](https://www.wowhead.com/forever/item=14624) · *Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Wristguards of True Flight](https://www.wowhead.com/forever/item=18812) · *Molten Core*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* | [Warder's Waistguard](https://www.wowhead.com/forever/item=250573) · *Blacksmithing* |
| Legs | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Blackrock Depths*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Legplates of the Eternal Guardian](https://www.wowhead.com/forever/item=11927) · *Blackrock Depths*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shalehusk Boots](https://www.wowhead.com/forever/item=11787) · *Panzor the Invincible, Blackrock Depths*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shalehusk Boots](https://www.wowhead.com/forever/item=11787) · *Panzor the Invincible, Blackrock Depths*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Dire Maul* | [Ring of Awareness](https://www.wowhead.com/forever/item=272409) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) |
| Main hand | [Bone Slicing Hatchet](https://www.wowhead.com/forever/item=18737) · *Maleki the Pallid, Stratholme*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Drillborer Disk](https://www.wowhead.com/forever/item=17066) · *Garr, Molten Core*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/protection/#eJzMVN9LFG0U3jMzu3P2KLrffMqOwyfMt/B9bcbI/GhDvZnVqy436KKLIid3bbd0Z9mZC4MurBCKfihBlEUqyJJFkVkXJl14UbLCShJUEGW/JLrowv6DmF11o2uTnqvzPs953/Oc98ChWoQQiCBDFFQQmjZPjAptEIcEHIAcDAJIHwLIhRjpJPF4bhjE1RricGkYiMUz/cTj8xEQP9ZRACfy4uc64vF1oV68wROPjwv14vs6L7tQTwG8esi7G8DzByvsiwIQh09HvJcu9hOH01eAeHxwGcTi38TjytBf4oqX+HA5FNkVWsiIFzLy9+bo6jhcg0lrAu5aU/CmcxrGCzALd6ZgHoYyy3Ap00XV1uaYZkWNGWpMMwxVM1RNi2lKTNV1XTdUVdeKDPeJ+cJRA6EUIA4fLUIEKUCcYqgOhYkkpEAU8dkYRILEk18xWmMONa4LLM5PQoQnP7GK7gh9QreV6zts51xZV/U9itqu6G0dck/ayh5NJWU7L1vJZCopHzkhu+mUnLddy83YWdlJWfmetBx1Uik5l7ddxbWyx5UNWanIrcccO7tTqvi8dTohZLeh2k9tCpzEdPi2scf7YyDskP6jppYwckLNHGyOwpOJ0ZzqcITadat+fDIJQo0UlHjyRxHfJYT+XxxrqqLt3mLHlXIsLiSEsNRIwRnwpjRxE6r/J7JfmSKsMfop1ldGQ3wGOGLIF7nNBj3CN9gbb7o+6mHR/Le3jFemvsaInGy2FBnfHwU3vhH9Vvx/b8vrtC+VSqXa7ul45zoR74azAKOQsdeGFve/NNvLrG/Z7PQyS6Vv5r5K8NZsYXE23MGEoOuf6paprMy95aWZhhwMwIDwYwD0rRuW); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/protection/#eJzMVE9o03AU7kvS5vVtbCVuNAsOYkGtk4wktbLtkm4njxU8eFBcXDtb3ZrS5DAPwlQKiqIiik5xG4ziNhTH9DCHh10cHXRYBD2I/6ZDPHiYdw+SdlvF8xx+p5fve+F97/fgo3qEAIggQxhUEFo2vxgVOiAGcTgKWRgGkFZ8yAUY6RzxePk6iKt1xOFUHojFi4PE46sbIK40kA/Hc+LXBuLx100Q7/PE4/NCo/ipgThcLjSSD+8cd//14ZVjVfZ1AYjDkXKAOCzfcuu5coB4/HwbxOIO4nE6D+JHt/NpORDaH1hMi1fT8s/W8OoY3IUJcxwemZPwrnsGxgowB9OTsAD5dBmupXuotts806qo0Yga1SIRVYuomhbVlKiq67oeUVVdKzLcF+YbR02Eko84fLYEISQfcUpEtSlIJCH5wogvRyHkJ568SqQ9alPzusDiwgSEePISq+i2MCD0mtmBE1bWkXVVP6ionYre0SX3pczMqWRCtnKymUgkE/LJs7KTSso5yzGdtJWR7aSZ60vJYTuZlLM5y1EcM3NG2ZCVqtx+2rYy+6Sqz4cX4kJmG6b9sabASUyXZxt3fDIKwl5pN7W0BZET6uZh8xSuTIxm144j1K9b9eKLCRDqJL/EkzeM+CEuDP7lWFMV7cAWO66OY3ExLgSlZvLPgnul8QdQez+R/c4UYY3Rz7OeCppis8ARQ57QFOt3Cc9wf6zl3oiLJWNXfwVvDX2NETnZaCsynv8KTmyj+qfY83jL53Qul0ql+t6ZWPc6EeuFSwAjkLbW8ktH3hidFdZTNrrdzlLph3G4Wrw32licC3YxAejZWUuZamYeqqRmCrIwBEPC7wEAMkccPg==).

## Other builds of this spec

- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (0/32/19) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513301311051-50025330001-6)
- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/23/28) — [open the talent tree](https://talentsforever.com/paladin/60/-0530513101301-502253300110303-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

