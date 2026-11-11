# Holy Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Holy

**[Holy — Raid healing](../research/raid/builds/holy-ml-heal.md)** (32/5/14) — [open the talent tree](https://talentsforever.com/paladin/60/54320215001101151-5-250300202-12)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Holy — Raid Healer), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

You heal with **Holy Light** on the tank, in the rank that covers what he is missing, and **Flash of Light** on everyone else: in the healer lab they do 82% of your healing. **Light's Vigil** and then **Holy Shock** on the same target is your group heal (14%). **Divine Favor** and **Lay on Hands** are your emergency buttons, and your critical heals pay part of their mana back.

**Why it works**

- Keep **Oath of Light** on the tank: it adds up to 400 to each **Holy Light**, 115 to each **Flash of Light** and 229 to each **Holy Shock** the tank receives. It is the build's most valuable talent in the healer lab (about a fifth of its capacity). Start a **Holy Light** when the tank is missing at least half of one and more hits are coming.
- Downrank: cast the smallest rank that heals about what the target is missing. Forever gives ranks far below your level less of your +healing (TBC's rule, our assumption): **Holy Light** ranks 7 to 9 and **Flash of Light** ranks 5 and 6 lose nothing or almost nothing, while rank 6 **Holy Light** keeps 85% of the bonus and lower ranks less, so stay near the top.
- **Flash of Light** is your raid heal: the lab heals other raid members once they fall below half health. Anyone under a quarter of their health gets **Holy Shock** if it is ready, else a **Flash of Light**.
- Group heal: when two or more raid members are below half health, cast **Light's Vigil** (1.5 s, 1,340 mana, 6-second cooldown) on the lowest of them, then **Holy Shock** that target. This **Holy Shock** starts no cooldown and heals the target and their party for 684 to 724 each, plus 14.3% of your +healing. The pair costs about 1,665 mana for five heals, so keep it for real group damage: the lab casts it about four times in a five-minute fight.
- **Divine Favor** (2-minute cooldown) goes before a top-rank **Holy Light** on a tank who is missing most of one: a sure critical heal, which **Illumination** then refunds. **Infusion of Light** (one point) makes your next **Holy Light** within 15 seconds half a second faster after a critical **Flash of Light** or **Holy Shock**.
- Mana and crits: **Illumination** returns half the base cost of each critical **Holy Light**, **Flash of Light**, **Holy Shock** or **Light's Vigil**. **Holy Power** (five ranks) makes a critical heal heal 225% instead of 150%, as the community simulator reads hotfix 113554. **Conviction** adds 6% critical strike chance, **Healing Light** 12% healing, and **Reverence** keeps 30% of your mana regeneration going while you cast. Drink a mana potion as soon as you are below 80% mana (after the first 45 seconds).
- **Lay on Hands** is for a tank about to die (the lab uses it under 20% health): it heals him for your maximum health but drains all your mana, and its 20-minute cooldown makes it once a fight.

**Caveats**

- The healer lab is this project's model of stated assumptions: one tank under boss melee and four raid members under raid damage for five minutes, with no dispels and no spell pushback. Check its numbers at launch.
- The build is the deep search's winner: capacity 0.636 in the healer lab, against 0.502 for the hand-made build below (2026-11-09 report). The hand-made build predates **Oath of Light** and does not take it.
- **Infusion of Light** and **Benediction** measure under 1% in the lab, and **Boundless Light** nothing: the lab casts **Holy Shock** about four times a fight, almost always right after **Light's Vigil**. A second rank of **Infusion of Light** or **Boundless Light** measured 1% lower than the ranks this build takes instead.
- **Divine Strength** (4 points) fills the tiers: Holy needs 30 points before **Light's Vigil**. **Deflection** (2) and **Benediction** (5) open **Conviction** and the third Retribution row. **Purifying Power** (2: **Cleanse** and **Purify** 20% cheaper), **Unyielding Faith** (2: fears 30% shorter) and **Pursuit of Justice** (2: 15% movement speed) are raid utility the lab does not measure; they cost no capacity there.
- **Spiritual Focus** keeps 14% a point (70% at five) of your **Holy Light**, **Flash of Light** and **Light's Vigil** casts from being pushed back; the lab has no pushback, so its value there is unmeasured.

**When to change it**

- When a whole party is taking damage, put **Light's Vigil** and **Holy Shock** on its lowest member; between them, **Flash of Light** the lowest.
- **Cleanse** a harmful magic, poison or disease effect when it would cost more healing than the cast; the lab has no debuffs, so when is your call.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 32 | Spiritual Focus 5, Divine Strength 4, Healing Light 3, Reverence 2, Purifying Power 2, Divine Favor 1, Illumination 5, Infusion of Light 1, Oath of Light 1, Holy Shock 1, Boundless Light 1, Holy Power 5, Light's Vigil 1 |
| Protection | 5 | Divine Intellect 5 |
| Retribution | 14 | Deflection 2, Benediction 5, Conviction 3, Unyielding Faith 2, Pursuit of Justice 2 |

## The numbers

Healing capacity 0.64 (the raid damage it heals through in this project's healer lab), 370 healing per second. Healers are not in the community simulator.

**The gear** (average item level: Pre-BiS 60.0; Phase 1 BiS 63.3; chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; healers are in no community simulator, so this is our model; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Living Crown](https://www.wowhead.com/forever/item=252561) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* | [Wavefront Necklace](https://www.wowhead.com/forever/item=20685) · *Lord Skwol, Silithus* |
| Shoulders | [Mantle of Lost Hope](https://www.wowhead.com/forever/item=22234) · *Lord Roccor, Blackrock Depths* | [Wildheart Spaulders](https://www.wowhead.com/forever/item=16718) · *Gizrul the Slavener, Blackrock Spire* |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* |
| Chest | [Mindsurge Robe](https://www.wowhead.com/forever/item=18532) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) | [Breastplate of Salvation](https://www.wowhead.com/forever/item=250601) · *Blacksmithing*<br>+ [Enchant Chest - Major Intellect](https://www.wowhead.com/forever/spell=19991) |
| Wrist | [Loomguard Armbraces](https://www.wowhead.com/forever/item=13969) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Bracer - Mana Regeneration](https://www.wowhead.com/forever/spell=23795) | [Flarecore Wraps](https://www.wowhead.com/forever/item=18263) · *Tailoring*<br>+ [Enchant Bracer - Healing Power](https://www.wowhead.com/forever/spell=23796) |
| Hands | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* | [Hands of the Exalted Herald](https://www.wowhead.com/forever/item=12554) · *Princess Moira Bronzebeard, Blackrock Depths* |
| Waist | [Whipvine Cord](https://www.wowhead.com/forever/item=18327) · *Alzzin the Wildshaper, Dire Maul* | [Corehound Belt](https://www.wowhead.com/forever/item=19162) · *Leatherworking* |
| Legs | [Padre's Trousers](https://www.wowhead.com/forever/item=18386) · *Illyanna Ravenoak, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Martyr's Legplates](https://www.wowhead.com/forever/item=250600) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Mooncloth Boots](https://www.wowhead.com/forever/item=15802) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Rosewine Circle](https://www.wowhead.com/forever/item=13178) · *Urok Doomhowl, Blackrock Spire* | [Cauterizing Band](https://www.wowhead.com/forever/item=19140) · *Majordomo Executus, Molten Core* |
| Finger | [Ring of Demonic Guile](https://www.wowhead.com/forever/item=18314) · *Alzzin the Wildshaper, Dire Maul* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832) · *Ambassador Flamelash, Blackrock Depths* |
| Trinket | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* | [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) · *Magister Kalendris, Dire Maul* |
| Main hand | [Hammer of the Grand Crusader](https://www.wowhead.com/forever/item=18717) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Mighty Intellect](https://www.wowhead.com/forever/spell=23798) | [Hammer of the Grand Crusader](https://www.wowhead.com/forever/item=18717) · *Balnazzar, Stratholme*<br>+ [Enchant Weapon - Healing Power](https://www.wowhead.com/forever/spell=22748) |

## Other builds of this spec

- [Holy — Raid Healer](../research/raid/builds/holy-raid-healer.md) (31/2/18) — [open the talent tree](https://talentsforever.com/paladin/60/53320215002001151-2-352330002-12)
- [Holy (optimized)](../research/raid/builds/opt-holy-heal-raid-heal.md) (31/10/10) — [open the talent tree](https://talentsforever.com/paladin/60/53320215002001151-51022-25003-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753). Simulations, not in-game measurements. Do not hand-edit.*

