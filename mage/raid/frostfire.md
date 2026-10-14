# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-0355100013013304-00550003310003002-6)

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Ice Lance** when Fingers of Frost is active
2. **Pyroblast** when Heating Up has 3 stacks
3. **Fire Blast**
4. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 15 seconds left
5. **Frostfire Bolt** when your mana is below 30%
6. **Frostfire Bolt** when you have at least 10% mana
7. **Fireball**

**Fireball** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Wake of Fire**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest gain of the rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5; the line above shows only the stack count.
- **Frostfire Bolt** is the filler: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the list casts Rank 2 instead (285 mana against 370): it is learned at level 50, close enough to 60 that the low-rank penalty the simulator assumes leaves its spell power alone, and the simulator measured this about 2% better than the old rule of stopping at 10% mana.
- The Rank 2 **Fireball** at the bottom of the list only matters when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only a small part of your spell power and fewer talent procs; with that penalty in, the simulator measured dropping the old Fireball fallback 1.0% better, so keep your mana up with gems and a potion instead.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds part of every crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a Rank 2 **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 680 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 722 | [5/31/15](https://talentsforever.com/mage/60/005-20452030130013051-005500032-6) |
| Phase 1 BiS | 740 | [4/31/16](https://talentsforever.com/mage/60/004-10451231130003051-005500033-6) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 61.1; Phase 1 BiS 66.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Inferno Gloves](https://www.wowhead.com/forever/item=18408) · *Tailoring* | [Gloves of the Hypnotic Flame](https://www.wowhead.com/forever/item=18808) · *Molten Core* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Searing Golden Blade](https://www.wowhead.com/forever/item=12260) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

## Other builds of this spec

- [Frostfire — Frostfire Bolt / Hot Streak](../research/raid/builds/frostfire-raid.md) (4/31/16, 632 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/004-03251030130133051-005500033-6)
- [Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md) (4/31/16, 608 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/004-10452131130103051-005500033-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-14 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

