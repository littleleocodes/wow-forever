# Holy Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Holy

**[Holy — Raid Healer](../research/raid/builds/holy-raid-healer.md)** (22/29/0) — [open the talent tree](https://talentsforever.com/priest/60/005305001330011-3350110303012043--12)

## How to heal

The healer lab's Holy priest heals the tank with **Penance** every time it is ready and with **Greater Heal** downranked to the damage he has taken, heals the rest of the group only once they drop below 60% health (**Prayer of Healing** when two or more are that low), and keeps **Power Word: Shield** and **Flash Heal** for emergencies. Mana is the limit: even so, the lab's Holy priest spends part of its five-minute fight out of mana. The heal-choice policy was re-tuned on 2026-11-03 and did not move.

**Why it works**

- **Penance** goes on the tank whenever it comes off cooldown and he is missing most of what it heals: 425 healing at once and every second for 2 seconds, 385 mana less **Improved Healing**'s 15%, on a 12-second cooldown. It heals more per mana than **Heal** and **Greater Heal**, and the healer lab measured about 6% more capacity than keeping it for emergencies.
- **Greater Heal** is still your biggest heal. Start it on the tank when he is missing about half of what it heals and a boss swing is coming, at the lowest rank that covers what he is missing: the rest of a bigger rank would be overheal.
- **Prayer of Healing** when two or more of your group are below 60% health (the class's tuned heal policy: two, not three, and 60%, not 70%); one hurt member below 60% gets **Renew** or a **Flash Heal**. In Forever **Prayer of Healing** heals the target and the target's party, so aim it at the group that is hurt.
- **Renew** goes on the tank once he is missing a fifth of his health (the tuned policy, rather than a tenth), and on a raid member below 60% before a direct heal; **Improved Renew** adds 15% to it.
- **Inner Focus** goes on a full-rank **Greater Heal** when the tank is missing more than half of one: the heal is free and 25% more likely to crit, and a critical heal gives the tank 25% more armor for 15 seconds through **Inspiration**.
- In an emergency (anyone below 20% health): **Power Word: Shield** on the tank if Weakened Soul is gone, then **Penance** if it is ready, then a full-rank **Flash Heal**. That threshold is the class's tuned heal policy (the default was 35%); **Soul Warding** takes the shield's 4-second cooldown away and cuts its cost by 15%.

**Caveats**

- Mana runs out before healing power does: **Meditation** keeps half your regeneration going while you cast, **Improved Healing** makes **Greater Heal** and **Penance** 15% cheaper, and **Spiritual Guidance** at 4 points turns a fifth of your Spirit into healing. The tuned policy takes a mana potion below 40% of your mana.
- This build has no **Prayer of Mending** (it needs 31 points in Holy).
- Ranks far below your level get less from your healing power (a Forever change; the formula is our assumption). In our model **Greater Heal** ranks 3 to 5 lose nothing and rank 1 about 15%, so downranking within **Greater Heal** still pays.
- The lab is one healer keeping a tank and four players alive for five minutes. It does not model movement, dispels or other healers.
- **Silent Resolve** (3 points) cuts the threat your spells cause by 30%: the healer lab models no threat, so it measures nothing there.

**When to change it**

- **Litany of Light** gives back 10% of a heal's base cost when it differs from your previous heal, so when two heals fit equally well, alternate them.
- **Holy Nova** heals everyone around you; the lab never casts it, so use it only when your group stands together and is hurt.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 22 | Twin Disciplines 5, Mental Strength 5, Improved Power Word: Shield 3, Inner Focus 1, Meditation 3, Soul Warding 1, Penance 1, Silent Resolve 3 |
| Holy | 29 | Holy Specialization 5, Improved Renew 3, Twilight Focus 3, Divine Fury 1, Holy Nova 1, Inspiration 3, Holy Binding 1, Improved Healing 3, Litany of Light 2, Spiritual Guidance 4, Spiritual Healing 3 |

## The numbers

Healing capacity 0.69 (the raid damage it heals through in this project's healer lab), 391 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 60.2; Phase 1 BiS 61.6; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Neck | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* |
| Shoulders | [Mantle of the Scarlet Crusade](https://www.wowhead.com/forever/item=22405) · *Cannon Master Willey, Stratholme* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Embrace of the Wind Serpent](https://www.wowhead.com/forever/item=12462) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Embrace of the Wind Serpent](https://www.wowhead.com/forever/item=12462) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) |
| Hands | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* |
| Waist | [Whipvine Cord](https://www.wowhead.com/forever/item=18327) · *Alzzin the Wildshaper, Dire Maul* | [Whipvine Cord](https://www.wowhead.com/forever/item=18327) · *Alzzin the Wildshaper, Dire Maul* |
| Legs | [Padre's Trousers](https://www.wowhead.com/forever/item=18386) · *Illyanna Ravenoak, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Padre's Trousers](https://www.wowhead.com/forever/item=18386) · *Illyanna Ravenoak, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Feet | [Ogreseer Tower Boots](https://www.wowhead.com/forever/item=13282) · *Spirestone Lord Magus, Blackrock Spire*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Ogreseer Tower Boots](https://www.wowhead.com/forever/item=13282) · *Spirestone Lord Magus, Blackrock Spire*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) |
| Finger | [Rosewine Circle](https://www.wowhead.com/forever/item=13178) · *Urok Doomhowl, Blackrock Spire* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* |
| Trinket | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* |
| Main hand | [Gift of the Elven Magi](https://www.wowhead.com/forever/item=13360) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) | [Gift of the Elven Magi](https://www.wowhead.com/forever/item=13360) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) |
| Off hand | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Ranged/relic | [Wand of Eternal Light](https://www.wowhead.com/forever/item=22254) · *Dark Coffer, Blackrock Depths* | [Wand of Eternal Light](https://www.wowhead.com/forever/item=22254) · *Dark Coffer, Blackrock Depths* |

## Other builds of this spec

- [Holy (optimized)](../research/raid/builds/opt-holy-heal-raid-heal.md) (21/30/0) — [open the talent tree](https://talentsforever.com/priest/60/005305031030001-3351010303012053--12)
- [Holy — Raid healing](../research/raid/builds/holy-ml-heal.md) (21/30/0) — [open the talent tree](https://talentsforever.com/priest/60/113113031330001-0350510303002053--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

