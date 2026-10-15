# Discipline Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Discipline

**[Discipline — Raid healing](../research/raid/builds/discipline-ml-heal.md)** (30/21/0) — [open the talent tree](https://talentsforever.com/priest/60/00521303131510113-2250300323001--6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Discipline — Penance / Divine Aegis / Power Infusion), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

The healer lab plays Discipline with the class's heal choices: **Penance** on the tank whenever it is ready, downranked **Greater Heal** on the tank, **Prayer of Healing** for the group, and **Power Word: Shield** and **Flash Heal** for emergencies. **Renewed Hope** and **Divine Aegis** are what the Discipline points buy; this build takes no **Power Infusion**.

**Why it works**

- **Penance** goes on the tank whenever it comes off cooldown and he is missing most of what it heals. Since 2026-10-08 it heals more per mana than **Heal** and **Greater Heal**, and the healer lab measured about 4% more capacity than keeping it for emergencies.
- **Greater Heal** on the tank is your biggest heal (0.3 seconds faster with 3 points in **Divine Fury**). Start it when he is missing about half of what it heals and a boss swing is coming, at the lowest rank that covers the damage.
- In an emergency (anyone below 20% health): **Power Word: Shield** on the tank if Weakened Soul is gone, then **Penance** if it is ready, then a full-rank **Flash Heal**. **Soul Warding** removes the shield's 4-second cooldown and cuts its cost by 15%.
- After a shield, heal the tank directly: with **Renewed Hope** your **Flash Heal**, **Greater Heal** and **Penance** crit 10% more often on a target with Weakened Soul, and each cuts 5 seconds off it, so the next shield comes sooner. Each crit also leaves an absorb of 15% of the heal (**Divine Aegis**) and 25% more armor for 15 seconds (**Inspiration**).
- **Inner Focus** on a full-rank **Greater Heal** when the tank is missing more than half of one; **Prayer of Healing** when two or more of the group drop below 70%; **Renew** on the tank once he is missing a fifth of his health.

**Caveats**

- Mana runs out first. **Meditation** keeps half your regeneration going while you cast; the tuned policy takes a mana potion below 40% of your mana.
- The lab shields only in emergencies: shielding the tank every time Weakened Soul ends measured slightly worse there, because the shields cost mana the fight runs short of. With mana to spare, extra shields feed **Renewed Hope**; the lab did not find that.
- Ranks far below your level now get less from your healing power (a beta change; the formula is our assumption). In our model **Greater Heal** ranks 3 to 5 lose nothing, so downranking within **Greater Heal** still pays.
- This build gives up **Power Infusion**, **Spiritual Guidance**, **Spiritual Healing** and **Prayer of Mending**; in the healer lab it holds less than the Holy page's build.

**When to change it**

- When the tank takes a big hit while Weakened Soul is still on him, cast **Penance** or **Flash Heal** at once: each also takes 5 seconds off Weakened Soul (**Renewed Hope**), so you can shield again sooner.
- **Litany of Light** gives back 10% of a heal's base cost when it differs from your previous heal: alternate heals when two fit equally well.

## The numbers

Healing capacity 0.61 (the raid damage it heals through in this project's healer lab), 346 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 58.5; Phase 1 BiS 62.2; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Devout Crown](https://www.wowhead.com/forever/item=16693) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) | [Halo of Transcendence](https://www.wowhead.com/forever/item=16921) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) |
| Neck | [Amulet of the Redeemed](https://www.wowhead.com/forever/item=22327) · *Stratholme* | [Amulet of the Redeemed](https://www.wowhead.com/forever/item=22327) · *Stratholme* |
| Shoulders | [Mantle of the Scarlet Crusade](https://www.wowhead.com/forever/item=22405) · *Cannon Master Willey, Stratholme* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Mooncloth Vest](https://www.wowhead.com/forever/item=14138) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Ghostweave Vest](https://www.wowhead.com/forever/item=14141) · *Tailoring*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Mana Regeneration](https://www.wowhead.com/forever/spell=23795) |
| Hands | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Blackrock Depths* | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Blackrock Depths* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* |
| Legs | [Devout Skirt](https://www.wowhead.com/forever/item=16694) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) | [Leggings of Transcendence](https://www.wowhead.com/forever/item=16922) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11649) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Boots of Prophecy](https://www.wowhead.com/forever/item=16811) · *Shazzrah, Molten Core*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Band of Mending](https://www.wowhead.com/forever/item=22334) · *Stratholme* | [Band of Piety](https://www.wowhead.com/forever/item=22681) |
| Finger | [Emerald Flame Ring](https://www.wowhead.com/forever/item=18395) · *Prince Tortheldrin, Dire Maul* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) · *quest: Holy Bologna: What the Light Won't Tell You* | [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Main hand | [Death Speaker Scepter](https://www.wowhead.com/forever/item=2816) · *Death Speaker Jargba, Razorfen Kraul*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) | [Death Speaker Scepter](https://www.wowhead.com/forever/item=2816) · *Death Speaker Jargba, Razorfen Kraul*<br>+ [Enchant Weapon - Mighty Spirit](https://www.wowhead.com/forever/spell=23797) |
| Off hand | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Thaurissan's Royal Scepter](https://www.wowhead.com/forever/item=11928) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

## Other builds of this spec

- [Discipline — Penance / Divine Aegis / Power Infusion](../research/raid/builds/disc-penance-healer.md) (31/20/0) — [open the talent tree](https://talentsforever.com/priest/60/005203031303101531-215050030301--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

