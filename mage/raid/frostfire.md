# Frostfire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frostfire

*Built around Frostfire Bolt, a new Forever spell that uses both trees.* (a hybrid: Fire/Frost).

**[Frostfire — Raid](../research/raid/builds/frostfire-open-raid.md)** (0/29/22) — [open the talent tree](https://talentsforever.com/mage/60/-2255000013012503-2135000301203002-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Frostfire — Fingers of Frost / Ice Lance), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 7.5 seconds left
4. **Frostfire Bolt** when your mana is below 30%
5. **Frostfire Bolt** when you have at least 10% mana

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Evocation**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frostfire is a Fire mage whose main spell is **Frostfire Bolt**: it counts as both Fire and Frost damage, so both trees' talents apply, and its chill lights up **Fingers of Frost** for **Ice Lance**. The Fire side adds **Fire Blast**, **Scorch** upkeep and **Pyroblast** at full **Heating Up**.

**Why it works**

- **Ice Lance** on **Fingers of Frost** comes first. Each **Frostfire Bolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit, so spend both charges on **Ice Lance**.
- **Pyroblast** at 3 stacks of **Heating Up**: crits from **Frostfire Bolt**, **Fire Blast** and **Scorch** each take 25% off its 6-second cast, so 3 stacks make it 1.5 seconds. Unlike the Fire list, this one never casts it at 2 stacks; the simulator measured dropping that line 0.3% better.
- **Fire Blast** on cooldown (every 8 seconds: this build has no **Improved Fire Blast**): instant, and its crits feed **Heating Up** and **Ignite**. Using it without a mana condition was the biggest single gain of the full-raid rotation search, about 5%.
- **Scorch** keeps Fire Vulnerability (from **Improved Scorch**) at 5 stacks, +15% to your Fire damage, and **Frostfire Bolt** counts as Fire. This list refreshes it once 15 seconds or less of its 30 are left, a wider margin than the Fire list's 7.5.
- **Frostfire Bolt** is the main spell: 2.5 seconds with **Improved Fireball**, and one cast rolls for **Fingers of Frost**, **Heating Up** and **Ignite** at once. Below 30% mana the full rotation casts Rank 2 (285 mana against 370): the page's line "when your mana is below 30%". The simulator measured this about 2% better than the old rule of stopping at 10% mana.
- **Fireball** (Rank 2 in the full rotation) is last: a stopgap for when you cannot afford even a Rank 2 **Frostfire Bolt**. Forever gives ranks that far below your level only part of your spell power; keep your mana up with gems and a potion so it rarely comes up.

**Caveats**

- **Fingers of Frost** charges go to the next 2 spells you cast, whatever they are: do not let a **Frostfire Bolt** use one up.
- Mana: **Frostfire Bolt** costs 370 at top rank. The list uses both of your mana gems (from **Conjure Mana Ruby** and **Conjure Mana Citrine**), **Master of Elements** refunds 30% of the base cost on each Fire or Frost crit, and below 30% mana the cheaper Rank 2 stretches what is left.
- Moving: **Ice Lance** and **Fire Blast** are instant. For packs, **Flamestrike** and **Blizzard** are your area spells.
- **Frostfire Bolt** is new in Forever: its numbers here are the simulator's model of the beta tooltip, not yet checked in game.
- The full rotation also opens with **Arcane Power** for builds that take it; this build does not, so skip it.

**When to change it**

- Below 30% mana, switch to Rank 2 **Frostfire Bolt** rather than stop casting it; a **Fireball** is a weak stopgap only for when even that is out of reach.
- Against a target that resists Fire, **Frostfire Bolt** keeps working (it is checked against the lower of the target's Fire and Frost resistance), while **Fire Blast**, **Scorch** and **Pyroblast** lose damage.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 802 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 789 | [0/29/22](https://talentsforever.com/mage/60/-2355000013011503-2035020301013002-7) |
| Phase 1 BiS | 793 | [0/29/22](https://talentsforever.com/mage/60/-2355000013011503-1135001321003002-7) |

**The gear** (average item level: Pre-BiS 62.7; Phase 1 BiS 63.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) · *Alchemy* |
| Trinket | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) · *Alchemy* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVV1oI1UUzrkzzZyc/o3XouO0hTFQicGUm5mmthWbtE+CYIpP+qJNmokZkSQkEepblVKkYAtFlNY+SLFUpVpRkNoXMS9mF3bp0y7sPrR0t+yyLOwuC4V9WZaZtLTL5jXd83CZe77v8p3zceZe6kFQQQMDQjAJOSjCDMDXAD8C/AzA2zyUuegQ6HOtiCrqn5OCO1+BdthKMh58DyTjnW/d9YddlfxYy2s3OkjB6jpo1ztIwmqeZDxcBFJwq35MwT82QVtUSMZr6+7Jhbsqyfj3rkoS/uuQgvd+B632Isn48DsX/2W1M/iGWnNClxdAHKUnvlmDeWCzzhKwo/QKsFtjvwJurMLmPCw4+zDrjLed9pWAHRaMmFYsJoQQUUtEozFhRUxhxYQpLBF1c8KsMdhlrQdsLsCL3E4VP/u4UKwYpjAHI1ERMa0RYyqXyn9iZ4xCyUhlMnbGSH9hVHK2USpUUhWnkDfKdqo0lTNCZds2sqVCuZJ1SnaklHIykRNOpM7p/7RcyL+uK3oLSepRupFidKBpijj/EQ/qBr0U7kLggSr4ScYH/2huNQSW7m4fLUGjqkSseVVdTfIqPCtpNsWID2mCv0ftF2UiGbf+As7UFnpbf4v0sIYSb6/CGaBuTIx6w90o8/adpzAkP8lv9sfKLgv3krxH1+mFcCfKnKV9ukItJA2JPhdVa6MNTR1smqnq/6Nc1tmIj881sFYMN0O41+teOu3eEn06kj/E8L/qu7xX7/YI/lNCVPR5Q+fCXTqnwJ/eSF6qjyTeTPLSebkWcCsKMdxInvc1UMvzwPGfsJfUpNusBveZ+aXk82IgseZ6Qgwh+JgF3JRvJpt4ZWXZjQvxV7NeXImb+0yTjXh4m/meS1QSJ19Njdd+a5rOsLe+/1Ni7DiRmHTfxGXwNr79eFjC7ZfHzzydAoYgAe/ABHwAOSjCNEyzJwMAWr6v3g==); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVU1oK1UUzrkzTU5O/8Zr0XHawhioxGDKnZmmthWbtCtBMMWVbrRJMzEjkoQkQt1VKUUKtlCl0NqFFEtVqhXd1G7EbIyC0pWCLlrUorjRx4PC25THnbS0j5dt+s7iMud+3+U75+PMvTSAoIEOJkRhFgpQhgWAdwE+AvgEgHf5KJPoGBhLnYgaGm9SCA/fAf20k1Q8XwNS8d8P5PrhkUZBbBT1P3sohPUd0H/vIQXrRVLxdBUohPvNYyH8cg/01RCp+NuOPLl+pJGC33qk4uL7kvjfF6A3HiYVb69L/NOt3shTWsOL/rwC4iw78942LANb9NaAnWU3gf099Rng7hbsLcOKdwKL3nTXVV8pOGSRuO0kEkIIYTnCshLCiVuWk5CpbQnhCGE3GByxzj/YUpiXuZspv/FqqVwzbWGPxi0Rt50Jc66QKb7m5sxSxczkcm7OzL5l1gquWSnVMjWvVDSrbqYyVzCjVdc185VStZb3Km68kvFy8UtOvMkZfr1aKj5phIwOUrSzbCtFa6Rtirj8Co8YJj0S60Pg4ToEScVb3+iyGgLHkOmdNWhVlUi0r6pf07wO90vabTHiZZrhL1D3jyqRivtfA2daBz1rPENGTEeFd9fhGtA0JkGDsX5UeffhPRhSkNSnhxNVycLjNB8wDHoo1osqZ9mAEaIOUsbEkES1xmRLU0fbZqr2/SRXDTYR4EstrBXj7RAe9LtXrrp3xJCBFIwy/K7+PB80+n1C8IpgiSF/6CTcZ3AKf+WP5E/NkcS/0rxyU66FZUVRhrvpm74GGkUevvgTjtO68g9rwP/MflsJ+DGS2paeEEOInLOw3Aos5FOPbW7I+CH5eN6PX5L2CdNVMxk7YIEHErXU5Vdb44nP26Yz7q8vfpyauthIzco3cQP8JHCSjCl48Oj0tadTwBik4DmYgZegAGWYh3l2dwAd9a9j).

## Other builds of this spec

- [Frostfire — Fingers of Frost / Ice Lance](../research/raid/builds/frostfire-fingers-of-frost-raid.md) (0/29/22, 764 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/-1355100013013303-2135000301113002-7)
- [Frostfire — Raid](../research/raid/builds/frostfire-ml-raid.md) (6/32/13, 760 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0042-20552030130115031-20350003-7)
- [Frostfire — Frostfire Bolt](../research/raid/builds/frostfire-raid.md) (5/33/13, 743 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0041-23251030130135031-20350003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

