# Feral Combat Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Feral Combat

**✅ Recommended** for raid (the best druid spec here, or within 3% of it).

**[Feral Combat — Raid](../research/raid/builds/feral-combat-open-raid.md)** (9/33/9) — [open the talent tree](https://talentsforever.com/druid/60/050022-25000332021031212051-144-6)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (feral-cat-dps), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Faerie Fire**.

**Keep up all fight:** **Cat Form**.

**Then press the first one that is ready**, top to bottom:

1. **Faerie Fire**: keep it on the target
2. **Rip**: keep it on the target, when you have 4 or more combo points
3. **Shifting Power**
4. **Shred**

**Shred** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserk**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid cat keeps **Rip** bleeding on the boss, turns mana into energy with **Shifting Power**, and spends the rest on **Shred** from behind. Tiger's Fury and **Berserk** go on cooldown, and **Faerie Fire** opens the fight.

**Why it works**

- **Faerie Fire** takes 505 armor off the boss for 40 seconds, so your **Shred** and white hits land harder, and in **Cat Form** it costs nothing. Cast it on the pull. In a full raid the simulator assumes the raid keeps it up and casts it once a fight; if nobody else does, refresh it before it runs out.
- **Rip** does a large share of your damage (close to 40% on the training dummy). Put it back up as soon as it falls off, at 4 or more combo points: its attack power bonus stops growing at 4 points (the simulator's model, as in Classic), so the fifth point adds only a flat 153 damage while the boss goes without a bleed. The simulator measured Rip at 4 or more about 1% better in a full raid than waiting for 5.
- **Shred** is the filler: 42 energy with **Shredding Attacks**, 1 combo point, 2 on a critical strike with **Blood Frenzy**, and 10% more damage from **Rend and Tear** while **Rip** bleeds. **Rip** lasts 12 seconds, about the time three Shreds take, and those Shreds bring about 4 combo points with their critical strikes. So when Rip falls off, you usually hold the points to put it straight back.
- **Ferocious Bite** is not in the list: the simulator measured the rotation 1% better in a full raid without it, the energy going to **Shred** instead. With **Rip** up and 5 combo points, keep shredding; points beyond 5 are lost.
- **Shifting Power** turns 55% of your base mana into 40 energy every 8 seconds with **Improved Shifting Power**: cast it whenever it is ready and your energy is 60 or less, so none of the 40 spills over your 100 cap. A raid's mana buffs pay for it, and in the simulator the builds that take it do 12-16% more damage in a full raid than the 9/31/11 build without it.
- Tiger's Fury costs no energy and no combo points and adds 15% physical damage for 6 seconds every 30 seconds (about 7 times a fight; the beta's trainer list no longer shows it, the simulator reads it from the client), so it is the top line. **Berserk** (3-minute cooldown) makes every **Shred** a critical strike for 15 seconds, each worth 2 combo points with **Blood Frenzy**: press it on the pull.

**Caveats**

- **Shred** only works from behind. If the boss faces you, or you have to tank, build with **Claw** instead (110% weapon damage plus 126 for 45 energy, less with **Ferocity**).
- Without a raid's mana buffs (a dungeon group, or alone) each **Shifting Power** costs more than half your base mana and you run dry fast: keep the mana for a shift and a **Regrowth**. Solo, the fight lab found that drinking the mana back costs more time than the energy saves.
- Powershifting is nearly gone in Forever: **Furor** keeps your energy through a shift, plus 10 a second out of form, instead of granting a flat 40, and leaving **Cat Form** ends Tiger's Fury. The rotation shifts out only with Clearcasting up and under 14 energy, about twice a fight, and the simulator found almost nothing in it: skip it if it costs you attention.
- The bear builds under Other builds are tank builds: they play **Lacerate**, **Maul** and **Barkskin** in **Dire Bear Form**, not this list (the research rotation page has their priority).

**When to change it**

- When the boss will die before a new **Rip** can tick most of its 12 seconds (the last 6 seconds or so), spend the points on **Ferocious Bite**: its damage lands at once.
- On an add that dies within a few seconds, the same: **Ferocious Bite** rather than **Rip**.
- If you pull the boss off the tank, **Cower** (20 energy, 10-second cooldown) lowers your threat by a large amount.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 698 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 570 | [9/35/7](https://talentsforever.com/druid/60/050022-35000232120032012051-142-6) |
| Phase 1 BiS | 576 | [9/35/7](https://talentsforever.com/druid/60/050022-25000332120032012051-052-6) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Ferocity of the Timbermaw](https://www.wowhead.com/forever/item=227805) | [Ferocity of the Timbermaw](https://www.wowhead.com/forever/item=227805) |
| Legs | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Blood Guard's Dragonhide Treads](https://www.wowhead.com/forever/item=227181)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Blood Guard's Dragonhide Treads](https://www.wowhead.com/forever/item=227181)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Idol of Ferocity](https://www.wowhead.com/forever/item=22397) · *Lord Roccor, Blackrock Depths* | [Idol of Ferocity](https://www.wowhead.com/forever/item=22397) · *Lord Roccor, Blackrock Depths* |

## Other builds of this spec

- [Feral Combat — Shifting Power](../research/raid/builds/feral-combat-shifting-power-raid.md) (9/35/7, 691 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000032121032212051-052-6)
- [Feral Combat (optimized)](../research/raid/builds/opt-feral-cat-dps-raid-dps.md) (9/31/11, 594 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-25000332020032012051-055001-6)
- [Feral — Cat DPS](../research/raid/builds/feral-cat-dps.md) (9/32/10, 579 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000332120032012021-055-6)
- [Feral — Bear Tank](../research/raid/builds/feral-bear-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-054-6)
- [Feral Combat (optimized, tank)](../research/raid/builds/opt-feral-bear-tank-raid-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-504-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-12 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

