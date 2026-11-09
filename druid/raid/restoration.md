# Restoration Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Restoration

**[Restoration — Raid healing](../research/raid/builds/restoration-ml-heal.md)** (11/0/40) — [open the talent tree](https://talentsforever.com/druid/60/15022001--355300515311305-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Restoration — Raid Healer), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

Keep **Rejuvenation** on the tank and heal it with **Healing Touch** at the rank that covers the health it is missing. **Regrowth** is for raid members who drop under half health, **Swiftmend** and **Nature's Swiftness** are your emergency buttons, **Tranquility** your group heal, and mana is what runs out first.

**Why it works**

- **Healing Touch** is the biggest share of your healing in the healer lab. Start it on the tank when it is missing at least about half of what your top rank heals and the next boss hit is on its way: a 3.0-second cast with this build's 5 points in **Naturalist** (3.5 without), and a rank sized to the missing health saves mana over the top rank (840 mana, 10% less with **Tranquil Spirit**).
- **Rejuvenation** is the next biggest share. Keep it on the tank whenever it is missing more than 5% of its health, always at the top rank: it is instant and costs 360 mana, **Improved Rejuvenation**, **Gift of Nature** and **Genesis** (10% more periodic healing) add to it, and **Nature's Splendor** stretches it by 3 seconds. Its ticks can crit since the 24 Sep build (so can Wild Growth and **Tranquility**), which the lab counts since 2026-10-17.
- **Regrowth** is the fast heal: a 2-second cast with a direct heal and a heal over time (6 seconds longer with **Nature's Splendor**), and **Improved Regrowth** (5 points) adds 50% to its critical chance. The lab gives a raid member under half health a **Rejuvenation** first and a **Regrowth** if they still need it, and casts **Regrowth** on the tank when it is missing about a full one.
- **Bloom** (the build's newest point, in the healer lab since 2026-11-08): when a **Rejuvenation** or **Regrowth** of yours runs out by its duration, the target is healed for 100% of your Spirit (50% if it was dispelled). So let them run out where you can, and **Living Spirit** (+15% Spirit) feeds it.
- **Swiftmend** consumes the **Rejuvenation** or **Regrowth** on the target and heals at once for that spell's whole periodic amount, every 15 seconds (Forever's tooltip says "the consumed spell"). The lab presses it when anyone falls under 35% health. It only works on a target with your heal over time, one more reason to keep **Rejuvenation** on the tank.
- **Nature's Swiftness** (3-minute cooldown) makes your next Nature spell instant: the lab casts an instant top-rank **Healing Touch** on a tank under 35% health. This build has no Wild Growth: when three or more raid members are under half health, the lab channels **Tranquility** (5-minute cooldown).
- Mana shapes this build: **Reflection** (up to half your mana regeneration keeps going while you cast), **Living Spirit** and **Tranquil Spirit**, and **Nature's Focus** (42% at 3 points) keeps your heals from being pushed back. **Improved Wrath** (1 point) and **Improved Moonfire** (2) heal nothing: with **Genesis** 5 and **Nature's Majesty** 2 they are the 10 Balance points **Nature's Splendor** needs.

**Caveats**

- Mana runs out before cast time does. The lab drinks a mana potion as soon as you are 20% down, from the start of the fight, and casts **Innervate** on itself under 40% mana: for its 20 seconds all of your mana regeneration continues while you cast (its tooltip), which the lab models in full since 2026-10-17.
- Leave raid members above half health to their own regeneration and the other healers: the lab heals them only under 50%, the mana going to the tank.
- Forever gives low ranks less of your healing power (Blizzard's beta notes; the exact rule is not published). The lab assumes TBC's rule: **Healing Touch** ranks 9 to 11 keep their full bonus, rank 8 about 92% and rank 7 about 82%, so downrank only that far.
- **Swiftmend** uses up the heal over time it heals from, so press it on a target whose **Rejuvenation** is worth losing, and put a new one back after. The healer lab reads this from the tooltip.

**When to change it**

- A whole party hurt at once and standing together: **Tranquility** (a 10-second channel on your party within 20 yards).
- A tank or healer dies: **Rebirth** (30-minute cooldown) brings them back during the fight.
- Curses and poisons: **Remove Curse** and **Abolish Poison** are yours to cast. The lab does not model them, so dispel when the debuff would cost more health than your next heal restores.
- If your raid's damage comes in bursts on whole parties, the hand-made build under Other builds takes Wild Growth; in the lab's steady damage this build heals more.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Balance | 11 | Improved Wrath 1, Genesis 5, Improved Moonfire 2, Nature's Majesty 2, Nature's Splendor 1 |
| Restoration | 40 | Nature's Focus 3, Heart of the Wild 5, Naturalist 5, Reflection 3, Gift of Nature 5, Tranquil Spirit 5, Improved Rejuvenation 3, Swiftmend 1, Nature's Swiftness 1, Living Spirit 3, Improved Regrowth 5, Bloom 1 |

## The numbers

Healing capacity 0.69 (the raid damage it heals through in this project's healer lab), 405 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 59.1; Phase 1 BiS 62.8; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Wildheart Spaulders](https://www.wowhead.com/forever/item=16718) · *Gizrul the Slavener, Blackrock Spire* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Ironfeather Breastplate](https://www.wowhead.com/forever/item=15066) · *Leatherworking*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) | [Mooncloth Vest](https://www.wowhead.com/forever/item=14138) · *Tailoring*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) |
| Hands | [Wildheart Gloves](https://www.wowhead.com/forever/item=16717) · *The Unforgiven, Stratholme* | [Wildheart Gloves](https://www.wowhead.com/forever/item=16717) · *The Unforgiven, Stratholme* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Corehound Belt](https://www.wowhead.com/forever/item=19162) · *Leatherworking* |
| Legs | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* |
| Trinket | [Serenity Field](https://www.wowhead.com/forever/item=272439) · *sold by Pix Xizzix* | [Serenity Field](https://www.wowhead.com/forever/item=272439) · *sold by Pix Xizzix* |
| Trinket | [item 1713](https://www.wowhead.com/forever/item=1713) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) · *quest: Heroes of Old* |
| Main hand | [item 7721](https://www.wowhead.com/forever/item=7721)<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) | [item 7721](https://www.wowhead.com/forever/item=7721)<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) |
| Off hand | [Twisting Essence Jar](https://www.wowhead.com/forever/item=249456) · *Enchanting* | [Twisting Essence Jar](https://www.wowhead.com/forever/item=249456) · *Enchanting* |

**Points that do nothing for this spec:** **Improved Wrath** (1) and **Improved Moonfire** (2) only count toward the points the tree needs before **Nature's Splendor**.

## Other builds of this spec

- [Restoration — Raid Healer](../research/raid/builds/resto-raid-healer.md) (11/0/40) — [open the talent tree](https://talentsforever.com/druid/60/05302001--5553005053113031-12)
- [Restoration — Regrowth / Nature's Grace, with a Balance dip](../research/raid/builds/resto-regrowth-natures-grace.md) (21/0/30) — [open the talent tree](https://talentsforever.com/druid/60/1532223110001--505300500311205-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-09 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

