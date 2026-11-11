# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Nature's Grace](../research/raid/builds/balance-moonkin-raid.md)** (33/0/18) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051--5553-12)

## How to play

**Before the pull, then keep up all fight:** **Moonkin Form**.

**Then press the first one that is ready**, top to bottom:

1. **Moonfire**: keep it on the target
2. **Insect Swarm**: keep it on the target
3. **Starfire**

**Starfire** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid Moonkin keeps **Insect Swarm** and **Moonfire** ticking on the boss and casts **Starfire** the rest of the time. **Moonkin Form** goes up before the pull, and **Innervate** is your mana button.

**Why it works**

- **Moonkin Form** first (the rotation shifts 10 seconds before the pull) and for the whole fight: it gives all party or raid members within 45 yards 3% spell critical strike chance and doubles how often **Omen of Clarity** makes your next spell free. A feral druid's **Leader of the Pack** adds melee and ranged crit instead of competing with it, and you cannot heal while in the form.
- **Insect Swarm** and **Moonfire** each do close to a fifth of your damage for one instant cast every 14 to 15 seconds (**Nature's Splendor** makes them last that long, **Genesis** adds 2% to their ticks a point, 10% at 5 points). Recast each one the moment it runs out, not before: recasting a running one throws away the ticks it had left.
- Both sit at the top of the list, above your cooldowns, and when both are due **Moonfire** goes first: its direct hit lands at once and can crit into **Nature's Grace** for the next **Starfire**. The rotation search of 2026-11-01 measured that order about 0.5% better in a full raid than the old **Insect Swarm** first.
- **Starfire** is your filler and about two thirds of your damage. It beats **Wrath** per second of casting at any gear: 350 to 412 damage plus all of your spell power in 3 seconds with **Improved Starfire**, against 92 to 102 plus 57% of it in 2 seconds. The raid build takes no **Eclipse**, so **Wrath** has no place in the list.
- Critical strikes feed the filler: **Vengeance** doubles their bonus damage, and every critical hit from **Starfire** or **Moonfire**'s first hit triggers **Nature's Grace**, 10% faster casts and global cooldown for 3 seconds.
- **Innervate** at 10% mana: for 20 seconds your mana regeneration is five times higher and all of it continues while you cast (6-minute cooldown). The 2026-11-01 search moved it down from 30% (about 0.2% better in a full raid): pressed late, none of it is wasted on a full bar. With a raid's Blessing of Wisdom and Mana Spring you need it in about 1 fight in 10.

**Caveats**

- Moving: **Starfire** needs 3 seconds standing still. Refresh **Insect Swarm** or **Moonfire** while you move, then go back to **Starfire**.
- Damage taken pushes your casts back. **Nature's Focus** gives you a 14% chance a point (70% at 5 points) to ignore each push, and **Barkskin** (1-minute cooldown) stops pushback for 15 seconds without slowing your casts as it did in Classic: press it when the raid is taking damage.
- Without raid mana buffs (a small group, or alone) you run short. The training-dummy rotation then casts rank 1 **Starfire** (95 mana) whenever a full one is out of reach, which the simulator measured better than waiting for mana.
- **Eclipse** (each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts, at 3 points) is not in the raid build despite its name, and no rotation here weaves **Wrath**. A 3-point **Eclipse** with a **Wrath** whenever its charges run out has not been simulated.

**When to change it**

- When the boss will die before a 3-second **Starfire** can land, cast an instant **Moonfire** instead: its first hit lands at once.
- In the last 10 seconds of a fight, skip a new **Insect Swarm**: most of its 14 seconds would tick on nothing. The simulator measured that 0.2% better on the training dummy.
- On a pack that will live a while, **Hurricane** hits every enemy in the area each second for 10 seconds (1,495 mana); the list itself is for one target.
- If you end fights with mana to spare, your raid may want **Innervate** on a healer instead: it works on any target.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Balance | 33 | Genesis 5, Improved Moonfire 2, Moonglow 3, Nature's Majesty 2, Nature's Reach 2, Nature's Splendor 1, Improved Starfire 5, Insect Swarm 1, Vengeance 5, Nature's Grace 1, Moonfury 5, Moonkin Form 1 |
| Restoration | 18 | Heart of the Wild 5, Nature's Focus 5, Naturalist 5, Reflection 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 711 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 642 | [36/0/15](https://talentsforever.com/druid/60/0532223115501051--055302-12) |
| Phase 1 BiS | 666 | [36/0/15](https://talentsforever.com/druid/60/0532223115501051--055302-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.4; Phase 1 BiS 62.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) · *quest: Volunteer's Battlegear* | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) · *quest: Volunteer's Battlegear* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk8FLFG8Yx+f7zqvz/h5/6DgajVOHV6EwYWRmlgnzsuOeOnSQTt1y1h3bFd1dnD3YTcFDBGlFEJqHikQI6hQhQhhGsXWIpUMXL6IsRUX0F0TMmNQ/IH0OD8/7fL8v7/c9PNQjoMOERD/GUEQVc8A14D5g/J9KLJGGYG2pQtPbrJg0sX4bZrONuNi7C+Liy52k3mvopImtNZj77aSJ7TWYO+3ExeZaojaXQJp486wjuaiJFy87zCWNuFj8phMX7x4knucNnVRxc5o00VyFWe8ihbh42tD7evV6qf/9IkZvPMR1sIXSCtinkcdoWV/FYmkXC6WcSMMiwCYzHT/jeV7GdX3fcR3ftW3H9zOOV2dosLY9tgPqJjHZSlysbKNPUCtx23Vio9syckmGrxd0WBq1kOpMx8YxqyvXSVzceoW/x9xiw4oxDyMfVqcuV6o16TneWdt17Iw7LMeLYflKVJCVGRkWClFB5q/KWjGSM5VaWCtVyjKOwpnxouyPo0jmw6mwPB7ZhWpsHxrsA8PgZFwpn7FOUOdAh+AGyysHCVznlJV84Ps+DLJE2n94DVP9zOr4wbx5VUkZDPKtFidGSt9P9l8yUeYmgp6V5YS32d6JlI9Zb5eZXGYHNpjyT6gFh92RcvrJkb1zLq0XHwUjvwfBWLJJy0gPym52QBUbx3Mn/yycgyEEOI9RXEIRVcxilv0aAEzrito=); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk8FLFVEUxue7c3Vux9BxNBqnFlehMGFkZh4T5uaNb9WihbRql/N8Y++JvfdwZmE7BRcRpGS10FxEJEJQqwgRIjGKF0FIizZuJJGiIvoLJGZM6h+QfovDN9935t5zF4e6BHSYkOjFCMqoYxq4CTwEjONZxNJoANaGKjS9xUpIE6sLMPdaiIv9BRAX3+6l9cGWTpp4tQJzt5U0sbkCc7uVuFhfSdO9eZAm3j5vS3/UxMuNNnNeIy7e30/TuR86cTF7N9UvsnP2lmE2OkghLp5t6T3deqPS+2EOw7cf4RbYbGUJ7MvQEzStLmOusoPZSkFk0yLAOjMdP+d5Xs51fd9xHd+1bcf3c47XYNhiLZ/ZNqiTxHgzcbG0iR5BzcRt14mNTsso6KSK75d0WBo1kepcj40TVkehnbi48xr/2txig4oxA6MY1ieu1uqJ9BzvvO06ds4dlKPlsHotKsnapAxLpagkizdkUo7kZC0Jk0qtKuMonBwty944imQxnAiro5Fdqsf2YYN90NA/Hteq56xT1N7XJrjBisrBBK5zxkof8HMXBlki0x/fwFS/sgZ+MW9GVTL6g2KzxYmR0rPPjqWOMj0WdC0tprzLd49lfMp7O8zkMt+3xpT/QhIcqiPl7NMju+dCVi8/Dob+GMFIukqLyD6UnXyfKtZOFk7/3TgHAwhwEcO4gjLqmMIU+z0A7qeLBA==).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

