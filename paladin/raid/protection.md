# Protection Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Protection

**[Protection — Raid tank](../research/raid/builds/protection-ml-tank.md)** (0/35/16) — [open the talent tree](https://talentsforever.com/paladin/60/-05311102513301531-52233000001-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value (threat and damage taken), then raced against the spec's builds. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Righteous Fury**, **Retribution Aura**, **Seal of the Crusader**.

**Keep up all fight:** **Righteous Fury**, **Retribution Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**
2. **Consecration**
3. **Holy Shield**
4. **Holy Strike**
5. **Lay on Hands**
6. **Hammer of Wrath** when the target is below 20% health

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Fury**: a cooldown, use it at the start of the fight and again whenever it is ready (about 6 times a fight)
- **Templar's Bulwark**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

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

Tank value 1.022 (threat and damage taken under a boss, relative to our reference tank build).

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 63.2; chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values (our assumption: Forever may have changed some); each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Enriched Thorium Helm](https://www.wowhead.com/forever/item=250597) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Superior Defense](https://www.wowhead.com/forever/spell=20015) |
| Chest | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Enriched Thorium Breastplate](https://www.wowhead.com/forever/item=250595) · *Blacksmithing*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) | [Warder's Wristguards](https://www.wowhead.com/forever/item=250583) · *Blacksmithing*<br>+ [Enchant Bracer - Deflection](https://www.wowhead.com/forever/spell=13922) |
| Hands | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Warder's Gloves](https://www.wowhead.com/forever/item=250553) · *Blacksmithing*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) · *quest: Just Compensation* | [Belt of Heroism](https://www.wowhead.com/forever/item=21994) · *quest: Just Compensation* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673) · *sold by Kelm Hargunth*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673) · *sold by Kelm Hargunth*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Warder's Sabatons](https://www.wowhead.com/forever/item=250563) · *Blacksmithing*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* |
| Finger | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) | [Warden's Signet of Vigilance](https://www.wowhead.com/forever/item=275984) |
| Trinket | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) · *sold by Pix Xizzix* |
| Trinket | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) · *quest: The Eye of Command* | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) · *quest: The Eye of Command* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Greater Stamina](https://www.wowhead.com/forever/item=16217) |
| Ranged/relic | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) | [Libram of Fervor](https://www.wowhead.com/forever/item=23203) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVd+LG1UUzrlzM3PmTLeJ19adXlSmg9Q0MGFm0uh2X3baJ0GQ4JNv7thNTdyyCZsg9a0rFARF6j7ZVbLSNFDWH8FFYbu4UBRrWx/0oSoErP0liBSs/gEid9I0uvjgg91+D5dzv3PvmW++c+DSwwhZsMGBHExDFRpwDOA1gPcAzgCIbUmWqewEyHMm8iyTC0AG/tzN2Dct4th5G4hj/11FfnMC7GvbycAb3Yx9QwU/dDP2OwYZeLabsX/aThx/fV+dfOtjUNcN/GLIf9dVdU7cyhLHtW/Vevt1dfK3j8C+pUpdOf6AfUWd7HwK7u7s+Vru5jIsgdmJP4j7B5a7sALWG7XfH1k5A2/WjtcOYqIdIlhnj3p+qRgEgR+WgmLRD0rFwCuFYbHoKwQXGL/OvjZoB6HUieMnF8FF0ol7od+kcTKlQelcGjfKLhGS7gUThZJKkETSczpeboNrkkFpLyiUmqIPYjpuHHm+3mg5oR8+4QW+VwwmnUPVeO7FyoxTn3fimZnKjPPCK06rWnHm6624VavPOc1KPH+o6uSalYrTmK+3vFY8N+sN094gXXipWZ/bK1+mWVEjXxRoZ/5B1EX6D4OhpgQR9wtBc0h/zv5Jj7kWmadA/WevDbQn/xhyYa4MCblzlQlkwjxlDBltnacSBxB/LAsu2WRKkBxY1WuDCKX/n8uozeKrZfGkLNFe8TjZ+YdQE9Y6KCMN/GoZ5EAxWX19xN2NxH6Ef7uK+GV789UBdzcS2+SgX2n8rAPiyOYeBZ6/73/u0cCjxctPC18WyJUOZdwxsq6jkgF4dqFMY6tAxPHa4jOCZdOJPo69SyO1Gp7rgLCkOWrB7BaMlyHTpOH5sji9FcMc0T4Z0q78OIKwlphyQcPeBij/iPmDYdY2zXjYvGNQb2NkkI6Xyrb2C7sAt1m4oKUS7IhWgROjlPsnMxWROnY42rV0UuHi1O7DCb6fCq8ymztT+TWWui9oRcPonmLPh/fsO/uT9dnT0YE7RDStXpOTkGxSV6fyGq6NT7IsHPzbw+PDBETwFJThOahCA47CUfbXAN0SQMU=); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/protection/#eJzEVd+LG1UUzrlzM3PmTLeJ19adXlSmg9Q0MGFm0uh2X3baJ0GQ4JNv7thNTdyyCZsg9a0rFARF6oJgV8lK00BZleCisF1cKIq1rQ/6UBUC1u0PQaQP1T9A5E6aRhcffLDr93A59zv3nvnmOwcuPYyQBRscyME0VKEBJwBeA3gf4ByA2JFkmcpOgLxgIs8yuQBk4M/djH3LIo6dd4A49t9T5DenwL6+kwy82c3YN1XwQzdjv2uQgee7GfunncTx1w/Uybc+BnXdwC+G/HddVefU7SxxXPtWrXdeVyc33wb7tip17eQD9jV1svMpuHuzF2u5W8uwBGYn/jDuH1ruwgpYb9R+e2TlHLxZO1k7jIl2iGCdPer5pWIQBH5YCopFPygVA68UhsWirxBcYvwG+9qgXYRSJ46fXAYXSSfuhX6TxsmUBqVzadwou0RIuhdMFEoqQRJJz+l4tQ2uSQalvaBQaoo+iOm4cez5eqPlhH74hBf4XjGYdI5U47kXKzNOfd6JZ2YqM84LrzitasWZr7fiVq0+5zQr8fyRqpNrVipOY77e8lrx3Kw3THuDdOGlZn1uv3yZZkWNfFGg3fkHURfp3w2GmhJE3C8EzSH9Ofs7PeZaZJ4B9Z+9NtC+/GPIhbkyJOTuVSaQCfOMMWS0dZ5KHED8sSy4ZJMpQXJgVa8NIpT+vy6jNouvlsWTskT7xeNk5x9CTVjroIw08KtlkAPFZPX1EXcvEgcR/ukq4pftrVcH3L1I7JCDfqXxsw6IY1t7FHj+gf+4RwOPFq8+LXxZIFc6lHHHyLqBSgbg+YUyja0CEcfri88Ilk0n+jj2rozUanihA8KS5qgFs9swXoZMk4YXy+LsdgxzRAdkSHvy4wjCWmLKBQ17G6D8I+YPhlnbMuNh865BvY2RQTpeKdvaL+wS3GHhgpZKsCtaBU6MUu4fzFRE6sTRaM/SaYXLU3uPJvh+KtxkNnem8mss9b+gFQ2j+4p9H9237xxM1mfPRofuEtG0ek1OQ7JJbU7lNVwbn2RZOPyXh8eHCYjgKSjDc1CFBhyH4+zPAQDuhECd).

## Other builds of this spec

- [Protection — Tank](../research/raid/builds/prot-tank.md) (0/33/18) — [open the talent tree](https://talentsforever.com/paladin/60/-15310112513501031-50233300011-7)
- [Protection (optimized)](../research/raid/builds/opt-prot-tank-raid-tank.md) (1/34/16) — [open the talent tree](https://talentsforever.com/paladin/60/01-25300132503501031-50033310001-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at d97252f (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

