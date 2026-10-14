# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Frost — Raid](../research/raid/builds/frost-ml-raid.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/mage/60/053005003000311--055500031100030025-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (frost-winters-chill-raid), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Arcane Missiles** when Missile Barrage is active
2. **Ice Lance** when Fingers of Frost is active
3. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**
- **Presence of Mind**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid is a **Frostbolt** caster that cashes in two procs: free **Arcane Missiles** from **Missile Barrage** and instant **Ice Lance** casts on **Fingers of Frost**. One **Fire Blast** in the last seconds of the fight uses time no **Frostbolt** can fill.

**Why it works**

- **Arcane Missiles** on **Missile Barrage** comes first. Each **Frostbolt** that lands has a 20% chance to make your next Missiles free and twice as fast (the full damage in 2.5 seconds), and they are about a fifth of your damage in the simulator.
- **Ice Lance** on **Fingers of Frost** comes next. Each **Frostbolt** chill has a 15% chance to treat your next 2 spells as if the target were frozen; a frozen target takes 300% more damage from **Ice Lance** and **Shatter** adds 50% crit chance, so spend both charges on **Ice Lance**. With both procs up, the simulator measured the free Missiles first slightly better (0.2%).
- **Frostbolt** fills everything else: 2.5 seconds with **Improved Frostbolt**, and the spell that rolls for both procs. **Winter's Chill** needs no button: in Forever it is your own debuff, each Frost hit adds a stack (+2% crit to your **Frostbolt** and **Ice Lance**, up to 5), and steady casting keeps it full.
- **Fire Blast** waits for the last 3 seconds. A **Frostbolt** started then would still be casting or in flight when the boss dies, while **Fire Blast** is instant; the simulator measured this 0.5% better. The rotation search kept it out of the rest of the fight: no Frost talent improves it, it costs more mana than a **Frostbolt** (340 against 290) and it rolls for neither proc.
- **Presence of Mind** at the pull makes your next spell instant. Its cooldown is 3 minutes, so a 3-minute fight gets one; in a longer fight press it again when it is back.
- Mana: the list uses your mana gem (from **Conjure Mana Ruby**) as soon as you are down to 80% mana, and **Evocation** only below 20% mana with more than 25 seconds left. With a raid's mana buffs the simulator never needed **Evocation** in a 3-minute fight.

**Caveats**

- Several targets: this list is for one boss, and the simulator's raid fights are single-target. For packs, **Blizzard**, **Cone of Cold** and **Arcane Explosion** are your area spells.
- Moving: **Frostbolt** needs you to stand still. **Ice Lance** and **Fire Blast** are instant, and **Presence of Mind** makes one **Frostbolt** instant.
- Threat: the simulator ignores it. On a fresh pull, give the tank a few seconds before your opener.

**When to change it**

- In the last 3 seconds, cast **Fire Blast** instead of starting a **Frostbolt** (the Advanced line above).
- Without a paladin's or shaman's mana buffs you run dry sooner: below 20% mana with more than 25 seconds to go, channel **Evocation**. Any later and the mana comes back too late to spend.
- If you must move while **Fingers of Frost** is up, spend the charges on **Ice Lance** as you go: it is instant.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 684 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 716 | [21/0/30](https://talentsforever.com/mage/60/0552220030000101--055500031100030025-6) |
| Phase 1 BiS | 739 | [21/0/30](https://talentsforever.com/mage/60/0550050030001101--055500031100030025-6) (ties this build) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 65.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Netherwind Pants](https://www.wowhead.com/forever/item=16915) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMVE9MM0UU75td2mHAUoeoy4bDSITUhjWzW2uAg205qcSIiQejiTJtt+2ault3twInQSExHNDoCaMHSAwaQQgn5KiixVTDRVH0YDRGDyYSNFy8mN1Se/Dq9+X7HXbf+733y7w/ySP9GBKgAIMkcKBD/3qIwwTkYBaehDosAagfRDFOYPUFEsN/74LySx+R8St7QGT845+3ERl/twkkipu28nOcxPDH74LyfZxI+LhCJLz+NIniy3IgiuH9HVBeixEZf74dJzL+5EMgEn7ZJBJ+/XkSw+eboDQHiYw/CgOXtZFxvGIlmhbbfhuSX60DvyrMbn0Ka4BWrDcAXRXeg1/zh7CzBqewbk2TbkNH6B6eyRiGwXmac851rmsaz2QynPO0rgdfzo1ME8Ep6vsJ7cl0WFXJ7akBLFNUiKgx0kOkCT6q9hAp0XyQyiqaitC0qpMkHQvzpG6ewUdDqoeiRzpUxguk+M1n6A7QVRClklliBjce0PikZkxMsbxbFLbJHrU8z6qZHnNsJjoemxauKyomq7tOcZxVGsIN5IVFJhqueNibsZ15m3kOE6zQsGolNm/5Vafh/0dvmy+aLisKz/eY5asjRKF3kt4v5CiR8V/niPQewLWpBv/lz4DeoQ526HeOlJD+42yGvkSFqNeedep+uwuda9yYYsWqsCtmiTkua7dYWGR+1WSu4wvfcmzmmcItVlnSM01Wdh3P11xhlbROXGvH73vOc+x7VZUkUnEcDccYJTJBaS8s4NtjoGtwMyoYJcMpNajgqYhKD9AAlro71XUe7vTsMUX6DTXhAhnLUiTE/bmtYJAEYRh5X+oNqMhSOTf01kaAk+zd5RDfZI0LpMgsm2qiyC0FP9exbijGdv/3dya/bLVa/XP7ufw1kZuDVwE2wHIuVk+e+Do7GbKR02w+yGy1fs8+3jZ+yKYkfHjX9HD3bLQv30Ph7atCHRZggf4zAJBhBQ8=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/mage/dps/#eJzMlE1MK1UUx3vuDO3lglAvUYcJiysRUhvG3JlaAyxsy0olRkxcGBfKbTu0Y5qZZmYqsBJMSQwLTCAsMLqQxKgJX2GFrIyKKVqVjeLXwmiMLkwkati85OVlpvR18bbvvbz/4s65v3PO3HPuTQ7pxRAHBRgkgAMdvLlDHMYhCzPwIlRhCUDdj2Icx2qNxPC1XVD+6CEyvr4ORMa//ncfkfGP7wGJ4dNNUH7vIzH86fug/NxHJHxSIjL+ZDNwbtTDvBg+2AHlrRiR8VebwQ8+2wvW+gYQCb9hkhj+dgWUxgCR8cd7Afu3MjyG61a8YbEP3oHEN2vAL/Mz25/DKqC6tQ7oMv8h/Jk7gp1VOIM1a4p0mjpGj/B0mvM05ynOua5zXdN4OkA8pevByrmRbiA4Qz2/oX2ZDqkquT/Zj2WK8hE1RrqINM5H1C4ixRtPUllFkxGaUnWSoKNhnNSJM/hIiLooeqaN0l6QijdepjtAV0AUi2aRGdx4QuMTmjE+yXJuQdgme9byPKtiesyxmWjv2JRwXVEyWdV1CmOsVBNukJ5fZKLmiqe9aduZt5nnMMHyNatSZPOWX3Zq/i35tvma6bKC8HyPWb46TBT6IOn+Uo4SGf//EyLdh3BlqsF3+QugD6gDbfzusRLif86n6etUiGrlFafqt7rQucaNSVYoC7tkFpnjslaL+UXml03mOr7wLcdmnincQpklPNNkc67j+ZorrKLW9mst/2Oveo79qKqSeLIPR8NrjBKZoJQXFvDDCdBVuBsVjJChpBpU8FJEpYeoH0udN9V1Hr7p+XOK9BdqwAUylqVIqMez28FFEoRh+COpO0CRpbns4NtbgU4zD8+F+j5jXCBFZplkA0XuKfnZtnVHNbp728+Z+LrZbPbOHmRzVyA7C28CbIHlXKycvvBdZiKkkbNMLohsNv/OPN8yfskkJXz00NRQZ2y0pt9T4fwrQxUWYIHeGADaTQWo).

## Other builds of this spec

- [Frost (optimized, another mage's Winter's Chill)](../research/raid/builds/opt-frost-raid-raid-dps-extwc.md) (1/13/37, 650 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/1-2330203-0555000331021301251-6)
- [Frost — Winter's Chill](../research/raid/builds/frost-winters-chill-raid.md) (21/0/30, 619 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/054005003000211--055500033002100105-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-14 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

