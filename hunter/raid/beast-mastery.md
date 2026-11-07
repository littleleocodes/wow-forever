# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid is **Auto Shot** and your pet with a short list on top: keep **Serpent Sting** ticking, fire **Arcane Shot** and **Aimed Shot** each time their cooldowns end, and send **Bestial Wrath** whenever it is ready.

**Why it works**

- **Serpent Sting** comes first so it never drops: on the training dummy it is about 15% of this build's damage, 20% more with **Improved Stings**. Recast it only as it runs out, since a new sting replaces the old one and its last ticks; the full-raid rotation recasts it only while you have 30% mana or more.
- **Arcane Shot** goes out every time its cooldown ends: 5.4 seconds with 2 points in **Improved Arcane Shot**, about 33 times in a 3-minute fight. **Summon Hawk** shares that cooldown, and the full-raid rotation gives all of it to **Arcane Shot**, so the build's **Summon Hawk** point is never cast.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) goes once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown, so the next **Aimed Shot** is cast under it.
- **Aimed Shot** is last on the list but it is not a spam filler: it goes out almost every time it can, a 2-second cast and then its 6-second cooldown, about 23 times a fight. The instants above it cost only a global cooldown.
- **Bestial Wrath** (+50% pet damage for 18 seconds) goes at the pull and on every 2-minute cooldown, twice a fight. **Intimidation** is in the build only because **Bestial Wrath** requires it; the full-raid list never presses it.
- Your pet is about a quarter of your damage on the training dummy. It takes 10% of your attack power and all of your crit (this project's model of Forever's pet scaling), so **Ferocity** and **Frenzy** keep it critting and attacking faster, and **Focused Fire** adds 2% to you both while it is out.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator's best rotation never casts **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** is the first thing to drop when you run low.
- Keep the pet alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead pet takes **Focused Fire** with it. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; players have measured this only at levels 20 and 30).
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant, so keep pressing them.
- The simulator starts **Aimed Shot** 2.5 seconds before the pull so it lands as the fight begins; in a real raid, start it once your tank has the boss.
- Watch your ranks: in the beta client (build 70425) **Hunter's Mark** rank 4 gives +71 ranged attack power against rank 3's +98, and **Trueshot Aura** rank 5 +50 against rank 4's +75 (if your build has it); cast the stronger lower rank from your spellbook until Blizzard fixes the numbers. **Aspect of the Hawk** rank 7 (+120) is the best at 60. The simulator's numbers use **Hunter's Mark** rank 4, so they read about 0.3% low (estimate).

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown, since it hits up to 3 targets for weapon damage each while **Aimed Shot** adds 166 to one. For a pack, **Volley**: a 6-second channel with no cooldown in Forever, which holds **Auto Shot** while you channel.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds. The simulator's other hunter rotations stop refreshing it 3 to 6 seconds before the end.
- Inside 8 yards your shots and **Auto Shot** stop. Step back out; if you cannot, **Summon Hawk** still works, as it has no minimum range.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 995 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 784 | [31/17/3](https://talentsforever.com/hunter/60/5420001505001251-225305-3-12) |
| Phase 1 BiS | 796 | [31/20/0](https://talentsforever.com/hunter/60/5220111505001251-20501513003--12) (ties this build) |

*From the previous search run (searched 2026-11-01); a new run is under way and will replace these numbers and the gear.*

**The gear** (average item level: Pre-BiS 66.6; Phase 1 BiS 66.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Field Marshal's Chain Breastplate](https://www.wowhead.com/forever/item=16466) · *sold by Sergeant Major Clate*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Field Marshal's Chain Breastplate](https://www.wowhead.com/forever/item=16466) · *sold by Sergeant Major Clate*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marshal's Chain Girdle](https://www.wowhead.com/forever/item=16464) | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Marshal's Chain Legguards](https://www.wowhead.com/forever/item=16467) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Chain Legguards](https://www.wowhead.com/forever/item=16467) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Trinket | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Grand Marshal's Bullseye](https://www.wowhead.com/forever/item=18833) · *sold by Lieutenant Jackspring*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Grand Marshal's Bullseye](https://www.wowhead.com/forever/item=18833) · *sold by Lieutenant Jackspring*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9oE1kczu/NJPPLb3e7YdpuJsOyzGahpIEJb6ad0nZZkva0JymePGmnTWqmaBOSHNqDMEIFKUX8g9AWoUIslqLgsXgRKoUKalqLClqxaAUPHnoTPYjMNAGxHlv8DsM338e87/vNezz6EyECCmiQgEHIQxFcgPMA1wEWAeRffZd5bjeoOxJiRFDPkIQbLig7v5CI1RkgETcfRkjC2kVQNkIk4RMXlLdNJOEjF5RXHqm5oLxuIhHXXSAJN/c+l/BxQ3+64K0zsx4hEe9c9fj9e96aHxd+Vz40UYAkvHQFlJfN8bbImpPYmYcpYJPOHISr9i17q29+AZZAmnZuXoMLzjZMOv3od4cM3GUxq9PknBsWtzg3TMvQTdPq4JbescbEdYZv2FaQWgjVkNdwFeJIIRJ1g5epta4uViEeJomCupmyyvI5kI/bxVMnCsWKZnKzSze4bnT1asN5e+xkLqsVSpqdzeay2tCEVsnntFKhYlecwphWztml4byWKOdy2tBpvWQ7Wb1h6ntmarRcGGtX/6FYMoqCjKNeq9oqqH4+T5lWWa1Lsqiy3oDs7C/Dew60jKQGScBaQZ74wdydBxoVpd9ehIhEXHEHZBYR/Vk9/p/6L5kyp5akjIIcXGEMg6pEQRJ4yiAl+QcKcngJ6rvVcCy/+buoPPpdc96jm90H2nzvpDz/dGRflsF1bh5C1mIVZE39i1qTzRhs/BL/8PKUVfYn32xRhPdsDXaZeVYI+EhkpiBGUWrFucsQ+TwNSqg94GM3PYjxLyzs8YA7konNzXp4kP57xMeztLnNFFFLJ5dZ4KegkmmwQ0Xb7UPL6fGfR29k+upCZtC7cWfBfwlsp5MCLkf7v7mYOXRDBv6HATgGeSjCOIyzrwMADZ8sww==); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IFG8Y3veb2Z13398vW0Ztx0Fi2kDWhVm+GRtRI3b11CmkU6dydNd2pNxldw96CDYwCJH+IqQEBiaJFHSULoEhGFSrSQVpJGXUoYO3qEPEjLsQ2VHpOQzPPA/zPc8738dHjQghUECDKPRABnJQArgMcAdgFkD+33OZ67aB+llCDAnqBZJwpQTK5n8k4uZVIBFXn4VIwvI1UFYCJOHLEigfa0jC5yVQ3rmkXALlfQ2JuDYOJOHq9ucSvqjqr2bcdW4th0jEh+Muf/LYXfPbzH7law35SMLrN0FZq400hZac6OYUjAIbcSYhOG3ft9c7p2ZgDqQx595tuOJswIjThV53SMIj1miZJjcMw+IW54ZpGbrJLW5YRgvnLUtMXGb4ga37qY5QDZCIy4sQQQqQqBu8QPUVdXYaIkGSyK+bcasgXwL5tJ07dyabK2omN1t1g+tGa4fWl7EHz6ZTWjav2alUOqX1DmvFTFrLZ4t20ckOaoW0ne/LaNFCOq31ntfztpPSq6a+bcYHCtnBZvUwNcTCKMg44LYqL4Lq5fO4aRXUiiSLKuvwyc7OMrx9V8tIqp8ELGfl4b/MfWRXo8K0722ASMSFUrfMQqI3q8uPqUfJlDnVxWQUZP8CY+hXJfKTwOMGKbEDKMjBOajsVtWxvOafwvLAH815u2627Wrz7ZPy5vuJHVkG17m5B1mz0yBr6kGqj9Wiv/pLvMPL41bBm3y1ThG+sCXYYuZFwechmhyFBgpTPU7egNCPMVACzT4PW4kejPxkQZf7Sv3JhskJF08Th/o9vE6YG0wRtURsnvn+CYrJKttTND3Ys5x273nybrKzIiR73Et3ArwX30YiJuB8uOu3u5lDGyThOHTDKchADoZgiP0aAHkVLbQ=).

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 7c3453f (client 1.60.1.70755)). Simulations, not in-game measurements. Do not hand-edit.*

