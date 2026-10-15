# Holy Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Holy

**[Holy — Raid healing](../research/raid/builds/holy-ml-heal.md)** (21/30/0) — [open the talent tree](https://talentsforever.com/priest/60/113113031303001-0350510303002053--6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds. A model of the beta, to check at launch.

## How to heal

The healer lab's Holy priest heals the tank with **Penance** every time it is ready and with **Greater Heal** downranked to the damage he has taken, uses **Prayer of Healing** when two or more of the group are hurt, and keeps **Power Word: Shield** and **Flash Heal** for emergencies. Mana is the limit: even so, the lab's Holy priest spends part of its five-minute fight out of mana.

**Why it works**

- **Penance** goes on the tank whenever it comes off cooldown and he is missing most of what it heals. Since 2026-10-08 it heals more per mana than **Heal** and **Greater Heal**, and the healer lab measured about 6% more capacity than keeping it for emergencies.
- **Greater Heal** is still your biggest heal. Start it on the tank when he is missing about half of what it heals and a boss swing is coming, at the lowest rank that covers what he is missing: the rest of a bigger rank would be overheal.
- **Prayer of Healing** when two or more of your group are below 70% health (the class's tuned heal policy: two, not three). In Forever it heals the target and the target's party, so aim it at the group that is hurt.
- **Renew** goes on the tank once he is missing a fifth of his health (the tuned policy, rather than a tenth), and on a hurt raid member before a direct heal. It can crit since the beta's 2026-10-08 build.
- **Inner Focus** goes on a full-rank **Greater Heal** when the tank is missing more than half of one: the heal is free and 25% more likely to crit, and a critical heal gives the tank 25% more armor for 15 seconds through **Inspiration**.
- In an emergency (anyone below 20% health): **Power Word: Shield** on the tank if Weakened Soul is gone, then **Penance** if it is ready, then a full-rank **Flash Heal**. That threshold is the class's tuned heal policy (the default was 35%).

**Caveats**

- Mana runs out before healing power does: **Meditation** keeps half your regeneration going while you cast, and **Improved Healing** makes **Greater Heal** and **Penance** 15% cheaper. The tuned policy takes a mana potion below 40% of your mana.
- This build has no **Prayer of Mending** (it needs 31 points in Holy) and no **Soul Warding**, so your shield keeps its 4-second cooldown.
- Ranks far below your level now get less from your healing power (a beta change; the formula is our assumption). In our model **Greater Heal** ranks 3 to 5 lose nothing and rank 1 about 15%, so downranking within **Greater Heal** still pays.
- The lab is one healer keeping a tank and four players alive for five minutes. It does not model movement, dispels or other healers.

**When to change it**

- **Litany of Light** gives back 10% of a heal's base cost when it differs from your previous heal, so when two heals fit equally well, alternate them.
- **Holy Nova** heals everyone around you; the lab never casts it, so use it only when your group stands together and is hurt.

## The numbers

Healing capacity 0.69 (the raid damage it heals through in this project's healer lab), 385 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 58.1; Phase 1 BiS 62.6; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) | [Halo of Transcendence](https://www.wowhead.com/forever/item=16921) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) |
| Neck | [Heart of the Fiend](https://www.wowhead.com/forever/item=13960) · *Kirtonos the Herald, Scholomance* | [Heart of the Fiend](https://www.wowhead.com/forever/item=13960) · *Kirtonos the Herald, Scholomance* |
| Shoulders | [Mantle of the Scarlet Crusade](https://www.wowhead.com/forever/item=22405) · *Cannon Master Willey, Stratholme* | [Mantle of the Scarlet Crusade](https://www.wowhead.com/forever/item=22405) · *Cannon Master Willey, Stratholme* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Embrace of the Wind Serpent](https://www.wowhead.com/forever/item=12462) · *The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Ghostweave Vest](https://www.wowhead.com/forever/item=14141) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Superior Spirit](https://www.wowhead.com/forever/item=16218) | [Vambraces of Prophecy](https://www.wowhead.com/forever/item=16819) · *Molten Core*<br>+ [Enchant Bracer - Superior Spirit](https://www.wowhead.com/forever/item=16218) |
| Hands | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Blackrock Depths* | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Blackrock Depths* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* |
| Legs | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) | [Leggings of Transcendence](https://www.wowhead.com/forever/item=16922) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Boots of Prophecy](https://www.wowhead.com/forever/item=16811) · *Shazzrah, Molten Core*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Band of Mending](https://www.wowhead.com/forever/item=22334) · *Stratholme* | [Cauterizing Band](https://www.wowhead.com/forever/item=19140) · *Majordomo Executus, Molten Core* |
| Finger | [Emerald Flame Ring](https://www.wowhead.com/forever/item=18395) · *Prince Tortheldrin, Dire Maul* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) · *quest: Holy Bologna: What the Light Won't Tell You* | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Main hand | [Death Speaker Scepter](https://www.wowhead.com/forever/item=2816) · *Death Speaker Jargba, Razorfen Kraul*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) | [Death Speaker Scepter](https://www.wowhead.com/forever/item=2816) · *Death Speaker Jargba, Razorfen Kraul*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) |
| Off hand | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

## Other builds of this spec

- [Holy — Raid Healer](../research/raid/builds/holy-raid-healer.md) (22/29/0) — [open the talent tree](https://talentsforever.com/priest/60/205003011305101-3350110303012043--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

