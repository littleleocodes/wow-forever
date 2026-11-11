# Discipline Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Discipline

**[Discipline — Raid healing](../research/raid/builds/discipline-ml-heal.md)** (29/22/0) — [open the talent tree](https://talentsforever.com/priest/60/10431503133001103-3150102323002--12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Discipline — Penance / Divine Aegis / Power Infusion), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

The healer lab plays Discipline with the class's heal choices: **Penance** on the tank whenever it is ready, downranked **Greater Heal** on the tank, **Prayer of Healing** when the group drops below 60%, and **Power Word: Shield** and **Flash Heal** for emergencies. **Divine Aegis** and **Soul Warding** are what the deep Discipline points buy here; this build, the deep search's winner, takes neither **Power Infusion** nor **Renewed Hope**.

**Why it works**

- **Penance** goes on the tank whenever it comes off cooldown and he is missing most of what it heals: 425 healing at once and every second for 2 seconds, 385 mana less **Improved Healing**'s 15%. It heals more per mana than **Heal** and **Greater Heal**, and the healer lab measured about 4% more capacity than keeping it for emergencies.
- **Greater Heal** on the tank is your biggest heal. Start it when he is missing about half of what it heals and a boss swing is coming, at the lowest rank that covers the damage.
- In an emergency (anyone below 20% health): **Power Word: Shield** on the tank if Weakened Soul is gone, then **Penance** if it is ready, then a full-rank **Flash Heal**. **Soul Warding** removes the shield's 4-second cooldown and cuts its cost by 15%; **Improved Power Word: Shield** makes it absorb 20% more.
- Each critical direct heal leaves an absorb of 15% of the heal on the target (**Divine Aegis**, at most 1,200) and gives him 25% more armor for 15 seconds (**Inspiration**); **Holy Specialization** makes the crits more common.
- **Inner Focus** on a full-rank **Greater Heal** when the tank is missing more than half of one; **Prayer of Healing** when two or more of the group drop below 60% (the tuned policy; the default was 70%); **Renew** on the tank once he is missing a fifth of his health.

**Caveats**

- Mana runs out first. **Meditation** keeps half your regeneration going while you cast; the tuned policy takes a mana potion below 40% of your mana.
- The lab shields only in emergencies: shielding the tank every time Weakened Soul ends measured slightly worse there, because the shields cost mana the fight runs short of.
- Ranks far below your level get less from your healing power (a Forever change; the formula is our assumption). In our model **Greater Heal** ranks 3 to 5 lose nothing, so downranking within **Greater Heal** still pays.
- This build gives up **Power Infusion**, **Renewed Hope**, **Spiritual Guidance**, **Spiritual Healing** and **Prayer of Mending**; in the healer lab it holds about 6% less than the Holy page's build (0.65 against 0.69).
- **Silent Resolve** (3 points) cuts the threat your spells cause by 30%: the healer lab models no threat, so it measures nothing there.

**When to change it**

- **Litany of Light** (2 points) gives back 10% of a heal's base cost when it differs from your previous heal: alternate heals when two fit equally well. The second point measured +3.6% capacity in the healer lab (2026-11-09).
- With mana to spare, shield the tank more often: the lab's shields only went out in emergencies because mana ran out first.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 29 | Power in Light 1, Twin Disciplines 4, Silent Resolve 3, Holy Precision 1, Mental Strength 5, Mental Agility 3, Inner Focus 1, Improved Power Word: Shield 3, Meditation 3, Soul Warding 1, Penance 1, Divine Aegis 3 |
| Holy | 22 | Twilight Focus 3, Improved Renew 1, Holy Specialization 5, Divine Fury 1, Blessed Recovery 2, Inspiration 3, Holy Reach 2, Improved Healing 3, Litany of Light 2 |

## The numbers

Healing capacity 0.65 (the raid damage it heals through in this project's healer lab), 357 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 60.2; Phase 1 BiS 61.8; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Neck | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* |
| Shoulders | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Embrace of the Wind Serpent](https://www.wowhead.com/forever/item=12462) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) | [Embrace of the Wind Serpent](https://www.wowhead.com/forever/item=12462) · *Avatar of Hakkar, The Temple of Atal'Hakkar*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Mana Regeneration](https://www.wowhead.com/forever/spell=23795) |
| Hands | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Whipvine Cord](https://www.wowhead.com/forever/item=18327) · *Alzzin the Wildshaper, Dire Maul* |
| Legs | [Padre's Trousers](https://www.wowhead.com/forever/item=18386) · *Illyanna Ravenoak, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Padre's Trousers](https://www.wowhead.com/forever/item=18386) · *Illyanna Ravenoak, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Feet | [Ogreseer Tower Boots](https://www.wowhead.com/forever/item=13282) · *Spirestone Lord Magus, Blackrock Spire*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Finger | [Emerald Flame Ring](https://www.wowhead.com/forever/item=18395) · *Prince Tortheldrin, Dire Maul* | [Cauterizing Band](https://www.wowhead.com/forever/item=19140) · *Majordomo Executus, Molten Core* |
| Trinket | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* |
| Trinket | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* |
| Main hand | [Gift of the Elven Magi](https://www.wowhead.com/forever/item=13360) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) | [Gift of the Elven Magi](https://www.wowhead.com/forever/item=13360) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) |
| Off hand | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Ranged/relic | [Wand of Eternal Light](https://www.wowhead.com/forever/item=22254) · *Dark Coffer, Blackrock Depths* | [Wand of Eternal Light](https://www.wowhead.com/forever/item=22254) · *Dark Coffer, Blackrock Depths* |

## Other builds of this spec

- [Discipline — Penance / Divine Aegis / Power Infusion](../research/raid/builds/disc-penance-healer.md) (31/20/0) — [open the talent tree](https://talentsforever.com/priest/60/005203031330011531-215050030301--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

