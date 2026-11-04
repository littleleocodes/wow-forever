# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Nature's Grace](../research/raid/builds/balance-moonkin-raid.md)** (33/0/18) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051--5553-7)

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

- **Moonkin Form** first (the rotation shifts 10 seconds before the pull) and for the whole fight: it gives your party 3% critical strike chance and doubles how often **Omen of Clarity** makes your next spell free. The aura does not stack with **Leader of the Pack**, and you cannot heal while in the form.
- **Insect Swarm** and **Moonfire** each do close to a fifth of your damage for one instant cast every 14 to 15 seconds (**Nature's Splendor** makes them last that long, **Genesis** adds 5% to their ticks). Recast each one the moment it runs out, not before: recasting a running one throws away the ticks it had left.
- When both are due, **Insect Swarm** goes first: it costs 160 mana against 375 for **Moonfire**, and the simulator measured that order 0.3% better in a full raid (1.8% on a training dummy, where mana runs short).
- **Starfire** is your filler and about two thirds of your damage. It beats **Wrath** per second of casting at any gear: 350 to 412 damage plus all of your spell power in 3 seconds with **Improved Starfire**, against 92 to 102 plus 57% of it in 2 seconds. The raid build takes no **Eclipse**, so **Wrath** has no place in the list.
- Critical strikes feed the filler: **Vengeance** doubles their bonus damage, and every critical hit from **Starfire** or **Moonfire**'s first hit triggers **Nature's Grace**, 10% faster casts and global cooldown for 3 seconds.
- **Innervate** at 30% mana: for 20 seconds your mana regeneration is five times higher and all of it continues while you cast (6-minute cooldown). Not earlier, since regeneration is wasted once your bar is full. With a raid's Blessing of Wisdom and Mana Spring you need it in about 1 fight in 10.

**Caveats**

- Moving: **Starfire** needs 3 seconds standing still. Refresh **Insect Swarm** or **Moonfire** while you move, then go back to **Starfire**.
- Damage taken pushes your casts back. **Nature's Focus** gives you a 70% chance to ignore each push, and **Barkskin** (1-minute cooldown) stops pushback for 15 seconds without slowing your casts as it did in Classic: press it when the raid is taking damage.
- Without raid mana buffs (a small group, or alone) you run short. The training-dummy rotation then casts rank 1 **Starfire** (95 mana) whenever a full one is out of reach, which the simulator measured better than waiting for mana.
- **Eclipse** (each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts, at 3 points) is not in the raid build despite its name, and no rotation here weaves **Wrath**. A 3-point **Eclipse** with a **Wrath** whenever its charges run out has not been simulated.

**When to change it**

- When the boss will die before a 3-second **Starfire** can land, cast an instant **Moonfire** instead: its first hit lands at once.
- In the last 10 seconds of a fight, skip a new **Insect Swarm**: most of its 14 seconds would tick on nothing. The simulator measured that 0.2% better on the training dummy.
- On a pack that will live a while, **Hurricane** hits every enemy in the area each second for 10 seconds (1,495 mana); the list itself is for one target.
- If you end fights with mana to spare, your raid may want **Innervate** on a healer instead: it works on any target.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 647 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 642 | [36/0/15](https://talentsforever.com/druid/60/0532223115501051--055302-7) |
| Phase 1 BiS | 666 | [36/0/15](https://talentsforever.com/druid/60/0532223115501051--055302-7) (ties this build) |

**The gear** (average item level: Pre-BiS 63.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Dragonhide Helmet](https://www.wowhead.com/forever/item=16451) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) · *quest: Volunteer's Battlegear* | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) · *quest: Volunteer's Battlegear* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Earthen Silk Slippers](https://www.wowhead.com/forever/item=254013) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [High Warlord's War Staff](https://www.wowhead.com/forever/item=18874) · *sold by Sergeant Thunderhorn*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk0FLFV8Yxuc5c3TO//WPjqPROLU4CoUJIzNzmTA3d7yrFi2kVbuc6x27V+zeizML2ym4iCAtCkJpEZEEQa0iRAhFKW4bkRYtcnNRpKiIPkHEjEl9AelZvLzn+b2H85zFSz0COkxI9GMMZdQxC9wEHgHG/xliKRqCtaEKTW+zEtLE1izMgzbiYu8BiIsv99O6fQekifUVmPvtpInNFZi77cTF2kpKDxZT+vZlR3pRE683OsxFjbj4mNGFbzpx8WonrXfXddLE2j2YjS5SiIsXO3pfr96o9G8vYPT2Y9wCm68sg30aeYaWpw+xUGlivlIQWVoEWGOm4+c8z8u5ru87ruO7tu34fs7xGgw7rG2P7YK6SUy2EhfLm+gT1Ercdp3Y6LaMgk6q+HpJh6VRC6nO9dg4YXUVOtNoW/jb5hYbVow5GMWwPnW1Vk+k53jnbdexc+6wHC+H1WtRSdamZVgqRSVZvCGTciSna0mYVGpVGUfh9HhZ9sdRJIvhVFgdj+xSPbaPBuzDgcHJuFY9Z52izoEOwQ1WVA4TuM4ZK/3A930YZImsf/8GpvqZNfCDeXOqkmkwKLZanBgpfT/Zf6mjzE4EPctLqd7leycyfch7TWZymR9YZco/URIcdceqs8+P7Z0LWb38JBj5bQRj6SotITsozfyAKlZPFk7/2TgHQwhwEaO4gjLqmMEM+zUAB2CLDg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk89LFV8Yxuc5c3TO9/WLjqPROLU4CoUJIzNzmTA3d7yrFi2kVbuc6x27V+zeizML2ym4iCDNfiwUFxFJEBUtKsRNYRQ3ApEWbdxIIkVB9BdIzJjVPyB9Fg/veZ73cN6zeKlLQIcJiV6MoIw6poGrwF3A+D+LWBoNwHqlCk1vsRLSxMLzNnO3hbjYuwni4uvtVDdugDTxcgXmTitpYn0F5lYrcbG2kqa782n69ll2URNPH8Gc14iL93fwW2dvpfpiUydN7C7DbHSQQlw82dR7uvVGpXdjDsPX7+Ea2GxlCezz0EM0PVjGXGUbs5WCyKZFgDVmOn7O87yc6/q+4zq+a9uO7+ccr8GwyVo+sS1QJ4nxZuJiaR09gpqJ264TG52WUdBJFd/O6bA0aiLVuRwbR6yOQjtxsfAaf9vcYoOKMQOjGNYnLtbqifQc77TtOnbOHZSj5bB6KSrJ2qQMS6WoJItXZFKO5GQtCZNKrSrjKJwcLcveOIpkMZwIq6ORXarH9kGDvd/QPx7XqqesY9Te1ya4wYrK/gSuc8JKP/B9BwZZIqs/vIGpfmEN/GDejKpk9AfFZosTI6Vnj/2XOsr0WNC1tJjyLt89lvEx720zk8t83ypT/glJcFAdKicfH9o7ZzI9fz8Y+mUEI+kqLSI7KNv5PlWsHi0c/7NxDgYQ4CyGcQFl1DGFKfZzAN9qiqs=).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-04 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at bac92db (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

