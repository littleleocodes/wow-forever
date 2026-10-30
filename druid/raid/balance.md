# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Nature's Grace](../research/raid/builds/balance-moonkin-raid.md)** (33/5/13) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051-05-505003-7)

## How to play

**Before the pull, then keep up all fight:** **Moonkin Form**.

**Then press the first one that is ready**, top to bottom:

1. **Moonfire**: keep it on the target
2. **Insect Swarm**: keep it on the target
3. **Starfire**

**Starfire** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Innervate**: when you run out of mana (needed in about 1 of 10 fights)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 624 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 608 | this build |
| Phase 1 BiS | 631 | this build |

**The gear** (average item level: Pre-BiS 63.2; Phase 1 BiS 65.0; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Ironbark Staff](https://www.wowhead.com/forever/item=20069)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Swarming Idol](https://www.wowhead.com/forever/item=272430) | [Swarming Idol](https://www.wowhead.com/forever/item=272430) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEkrFrFEEUxvd7O7l9vgvJZhNxMyokB0o4OJndYyHa3OYqC4tgZRlShJwgBBIkZYQUInghIEjOFCIegqhYqIQ0gYhyNnJYWGizJByKivgXiMyqxH8g+BUfb74f82YePBll+AgxhgnMYB4LWAGuA3eBoD9HZNEkdEbs+UW9JB6vPx8Me0VRvHcbovjLLet3ur54vNNGuD8gHu+2EX4cEMXbbUt7axCPXz/LL3r89BHCNU8Uf8hp85svil90ra/v2D69TYSdYXFE8ZOuXxr3O42Jt01M37yHG6DVRgv0aeoh+h5sotnIsNqo9x8MkmKbtEmqcRybKEoSE5kkqpikkpjEmGqH0KXiHl2VEeHLBVHc2kWJpSCqEpnFYEQHdV9c/nrBh/akT1xzZTE4qofrQ/Z/L/FvrDSdc4KT+rgMlQdZBTTr/IZVc0rb3t/3EYjmvH73CqH7mTr4QfE118l1Jp0taCUkTuknHbGJszKXjrY2rN7Uxudyva/FGYVqrFbeIue/aCn9Wx2qTj8+tHfO5n7xfjr1J0hn7KpvID84Wa3s8tax+omDRTKYRIrzmMYlzGMBy1imXwMAP4Jo8Q==); Phase 1 BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEkj9rFFEUxefcedm53g3JZBJx8lRIFpSwsPJmloFos5OtLCyClWVIEbKCEEiQlBG2EMGE+KfImkLERRAVC5WQRogoK4IsFhbaLIZFURA/QZB5KvELLDnF4b7ze+8+LlwZZfgIMYYJzGAeC1gBrgJ3gaDfIsrQJHSH2PPzekk8Xn8+GHbzonjvBkTx91uZ32n74vHLJsLdAfF4p4nw84Ao3m5mtLsG8fjNM/vQ46ePEK55ovjd7Yx+snfqNzN/Yft0NxG2hsURxU/afmHcb9Um3q9i+vo9XAPVaw3Q16mH6HuwidVaB/VatX9/kBTbpE1SjuPYRFGSmMgkUckkpcQkxpRbhDblv9BlGRG+mBPFjR0UWHKiSpFZDEZ0UPXF5R/nfGhP+sQ1lxaDw3q4OiSK11/h/1hpOuMEx/VRGSoOsgpo1vkDy+aEznr/3EUgmm394TVC9xu18IviK65jdSqdzWklJE5hjw5libMyl442NjK9rYzPWX2sxB0K1ViluEXOgWgp/Vf1VCcf9+yf09bP30+n/gbpTLbqG7AHp1Mpurx1pHpsf5EMJpHiLKZxAfNYwDKW6fcAVelolw==).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

