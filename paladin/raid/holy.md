# Holy Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Holy

**[Holy — Raid healing](../research/raid/builds/holy-ml-heal.md)** (32/5/14) — [open the talent tree](https://talentsforever.com/paladin/60/55320015101111141-5-251310101-7)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Holy — Raid Healer), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

You heal with two spells: **Holy Light** on the tank, in the rank that covers what he is missing, and **Flash of Light** on everyone else. This build takes no **Holy Shock**: **Divine Favor** and **Lay on Hands** are your emergency buttons, and your critical heals pay part of their mana back.

**Why it works**

- Keep **Blessing of Light** on the tank: it adds up to 400 to each **Holy Light** and 115 to each **Flash of Light** he receives. Start a **Holy Light** when he is missing at least half of one and more hits are coming; in the healer lab the two spells do almost all your healing.
- Downrank: cast the smallest rank that heals about what the target is missing. Forever gives ranks far below your level less of your +healing (TBC's rule, our assumption): **Holy Light** ranks 7 to 9 and **Flash of Light** ranks 5 and 6 lose nothing or almost nothing, while rank 6 **Holy Light** keeps 85% of the bonus and lower ranks less, so stay near the top.
- **Flash of Light** is your raid heal and your emergency heal: the lab heals other raid members once they fall below half health, and anyone under a quarter of their health gets a **Flash of Light** first.
- **Divine Favor** (2-minute cooldown) goes before a top-rank **Holy Light** on a tank who is missing most of one: a sure critical heal, which **Illumination** then refunds. **Infusion of Light** (one point) makes your next **Holy Light** within 15 seconds half a second faster after a critical **Flash of Light**.
- Mana: **Illumination** returns half the base cost of each critical **Holy Light** or **Flash of Light**, **Holy Power** adds 5% crit to your heals, **Healing Light** 12% healing, and **Reverence** keeps 30% of your mana regeneration going while you cast. Drink a mana potion as soon as you are below 80% mana (after the first 45 seconds).
- **Lay on Hands** is for a tank about to die (the lab uses it under 20% health): it heals him for your maximum health but drains all your mana, and its 20-minute cooldown makes it once a fight.

**Caveats**

- The healer lab is this project's model of stated assumptions: one tank under boss melee and four raid members under raid damage for five minutes, with no dispels and no spell pushback. Check its numbers at launch.
- The deep search's winner (re-run 2026-10-21, about 2% more capacity than the hand draft) takes neither **Holy Shock** nor **Light's Vigil**: the healer lab measured more capacity without them. The build therefore has no group heal; **Flash of Light** on the lowest member is your answer to raid damage.
- **Spiritual Focus** (one point) keeps 35% of your **Holy Light** and **Flash of Light** casts from being pushed back; the lab has no pushback, so its value there is unmeasured.

**When to change it**

- When a whole party is taking damage, heal the lowest member with **Flash of Light**; you have no group heal in this build.
- **Cleanse** a harmful magic, poison or disease effect when it would cost more healing than the cast; the lab has no debuffs, so when is your call.

*This guide was written for the rotation of 2026-10-22; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Healing capacity 0.63 (the raid damage it heals through in this project's healer lab), 369 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 62.3; Phase 1 BiS 64.4; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Beads of Ogre Mojo](https://www.wowhead.com/forever/item=22149) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* | [Devout Mantle](https://www.wowhead.com/forever/item=16695) · *Solakar Flamewreath, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Breastplate of Salvation](https://www.wowhead.com/forever/item=250601) · *Blacksmithing*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) | [Breastplate of Salvation](https://www.wowhead.com/forever/item=250601) · *Blacksmithing*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Devout Bracers](https://www.wowhead.com/forever/item=16697) · *Stratholme*<br>+ [Enchant Bracer - Mana Regeneration](https://www.wowhead.com/forever/spell=23795) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Mana Regeneration](https://www.wowhead.com/forever/spell=23795) |
| Hands | [Mooncloth Gloves](https://www.wowhead.com/forever/item=18409) · *Tailoring* | [Mooncloth Gloves](https://www.wowhead.com/forever/item=18409) · *Tailoring* |
| Waist | [Wisdom of the Timbermaw](https://www.wowhead.com/forever/item=19047) · *Tailoring* | [Corehound Belt](https://www.wowhead.com/forever/item=19162) · *Leatherworking* |
| Legs | [Martyr's Legplates](https://www.wowhead.com/forever/item=250600) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Martyr's Legplates](https://www.wowhead.com/forever/item=250600) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Soulforge Boots](https://www.wowhead.com/forever/item=22087)<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Warden's Signet of Resolve](https://www.wowhead.com/forever/item=275983) | [Cauterizing Band](https://www.wowhead.com/forever/item=19140) · *Majordomo Executus, Molten Core* |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| Trinket | [Serenity Field](https://www.wowhead.com/forever/item=272439) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Mighty Intellect](https://www.wowhead.com/forever/spell=23798) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Mighty Intellect](https://www.wowhead.com/forever/spell=23798) |
| Off hand | [Evergreen Shield](https://www.wowhead.com/forever/item=279262) · *Blacksmithing*<br>+ [Enchant Shield - Superior Spirit](https://www.wowhead.com/forever/item=16222) | [Sunderbark Vigil](https://www.wowhead.com/forever/item=276754)<br>+ [Enchant Shield - Superior Spirit](https://www.wowhead.com/forever/item=16222) |

## Other builds of this spec

- [Holy — Raid Healer](../research/raid/builds/holy-raid-healer.md) (31/2/18) — [open the talent tree](https://talentsforever.com/paladin/60/53320215002001151-2-352330002-7)
- [Holy (optimized)](../research/raid/builds/opt-holy-heal-raid-heal.md) (31/10/10) — [open the talent tree](https://talentsforever.com/paladin/60/53320215002001151-51022-25003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707). Simulations, not in-game measurements. Do not hand-edit.*

