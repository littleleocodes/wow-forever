# Discipline Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Discipline

**[Discipline — Raid healing](../research/raid/builds/discipline-ml-heal.md)** (30/21/0) — [open the talent tree](https://talentsforever.com/priest/60/10531503133001103-3150102323001--12)

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
- This build gives up **Power Infusion**, **Renewed Hope**, **Spiritual Guidance**, **Spiritual Healing** and **Prayer of Mending**; in the healer lab it holds about 9% less than the Holy page's build (0.63 against 0.69).

**When to change it**

- **Litany of Light** (1 point) gives back 5% of a heal's base cost when it differs from your previous heal: alternate heals when two fit equally well.
- With mana to spare, shield the tank more often: the lab's shields only went out in emergencies because mana ran out first.

## The numbers

Healing capacity 0.63 (the raid damage it heals through in this project's healer lab), 344 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 60.1; Phase 1 BiS 61.6; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Mooncloth Vest](https://www.wowhead.com/forever/item=14138) · *Tailoring*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) | [Mooncloth Vest](https://www.wowhead.com/forever/item=14138) · *Tailoring*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) |
| Hands | [Devout Gloves](https://www.wowhead.com/forever/item=16692) · *Archivist Galford, Stratholme* | [Devout Gloves](https://www.wowhead.com/forever/item=16692) · *Archivist Galford, Stratholme* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* |
| Legs | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11649) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) · *quest: The Grand Invoker* | [Cauterizing Band](https://www.wowhead.com/forever/item=19140) · *Majordomo Executus, Molten Core* |
| Trinket | [Serenity Field](https://www.wowhead.com/forever/item=272439) · *sold by Pix Xizzix* | [Serenity Field](https://www.wowhead.com/forever/item=272439) · *sold by Pix Xizzix* |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) · *quest: Heroes of Old* | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) · *quest: Heroes of Old* |
| Main hand | [item 7721](https://www.wowhead.com/forever/item=7721)<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) | [item 7721](https://www.wowhead.com/forever/item=7721)<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) |
| Off hand | [Twisting Essence Jar](https://www.wowhead.com/forever/item=249456) · *Enchanting* | [Twisting Essence Jar](https://www.wowhead.com/forever/item=249456) · *Enchanting* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

## Other builds of this spec

- [Discipline — Penance / Divine Aegis / Power Infusion](../research/raid/builds/disc-penance-healer.md) (31/20/0) — [open the talent tree](https://talentsforever.com/priest/60/005203031330011531-215050030301--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-07 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

