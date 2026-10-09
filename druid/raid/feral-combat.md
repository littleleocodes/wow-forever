# Feral Combat Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Feral Combat

**✅ Recommended** for raid (the best druid spec here, or within 3% of it).

**[Feral Combat — Shifting Power](../research/raid/builds/feral-combat-shifting-power-raid.md)** (9/35/7) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000032121032212051-052-6)

> 🔬 Derived build: the community simulator's own preset talents (Feral Cat 9/35/7), raced against this project's builds in a full raid, where they came out ahead. A model of the beta, to check at launch.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 691 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 570 | [9/35/7](https://talentsforever.com/druid/60/050022-35000232120032012051-142-6) |
| Phase 1 BiS | 576 | [9/35/7](https://talentsforever.com/druid/60/050022-25000332120032012051-052-6) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme* | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme* |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking* | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking* |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948) |
| Waist | [Ferocity of the Timbermaw](https://www.wowhead.com/forever/item=227805) | [Ferocity of the Timbermaw](https://www.wowhead.com/forever/item=227805) |
| Legs | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking* | [Warbear Woolies](https://www.wowhead.com/forever/item=15065) · *Leatherworking* |
| Feet | [Blood Guard's Dragonhide Treads](https://www.wowhead.com/forever/item=227181) | [Blood Guard's Dragonhide Treads](https://www.wowhead.com/forever/item=227181) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| Main hand | [Idol of Ferocity](https://www.wowhead.com/forever/item=22397) · *Lord Roccor, Blackrock Depths* | [Idol of Ferocity](https://www.wowhead.com/forever/item=22397) · *Lord Roccor, Blackrock Depths* |
| Off hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/feralcat/#eJzMVV1oHFUUnnPnZvbuaWInt2mzXkQni8o6OMud2WzNBmE39ffBgNaCP1DMbHbiTkmzS3aF6NNiW5CiUASLER9KRYhYRaIEf14VUxmhxh+w1Ad9KEVUguK+CXJnZ5soefBBpedlv/vdc749536XuTjIwIQMWJADCXyst8oRCRNQgQfhUZiBOjShA/AcwCkA8RFjKXOXOIyU/f4moM7eXULKvoxM1NmrdaTs4/d2I2XHlgEpiyITKfvutyHU2bdPIWU//zKElG28rjb/OK3KXziKOjt1VK3fVuxXX5ioZW12PDQ/DTPPh7kr87JbrcBJIMfDF4F0qy/Da/4ZOOevwKWpdYADuDXCh+RGWZTS85xCUapf1yvIgue5BVl0HXfcWyf0AmE/kB8NHMGUGFD9T2fTmMIBx83L1lX2+1zCFvLFFk+LPsvHxE247yLZE1dyYg4IhgZSVZzI8bvEFE7w/chWQTEdA9kGVWgtxMEs9vm1ELltMp2TSa0nUpJ5GYushfw6MbglMKnxT4DX/Ob8E41m2/Kkt9+RJcebmLRm6/7Ck0HNaixafq0W1Kzq01a7HliLjbbfDhsLVivwF2frVq4VBNZcsOjPO7N+26k1W04/xeml5I+0Ggu3icN4iB/E9GfUQMrOnIC4SYOTxzXBftWTgfSToOHt3O7nXT4GmF6FPkzmeiaZyy3kSwd7lfyl/2sOB2/mWdxjDzOD689C0kohf0cRdylvPdXQynR83ivTVy2+/ADPCgtHL5KRLYvjq+COb/N4VOzd7mXHUMXm6Yf5feIevJNP/nUTbTvHKN+7SjiD+CgRGRpuUSrHh1YJMhrTpKrFQt0qv1fc/Y+FPK+4gxBFkhnmgZjFx/gjf9MZtnerzKomUjiA+oS8BcezHkqRx318JLmwZreK7CwkaIRzTG3QWBVTZyEGQll+7gPY+UBYx8joV8g6bBLvCBFa9g09ranozFWuf2VZxfny2Fwc35S9TZJJWWV7nWjXVLQrffSfxq1v/ev/U/o8iqLBmXcqUwlRmVHf8WUIG5snzh/6ulyKWe1CeUplRtFP5Yd64FLZ1tn7owdu2P4+qDfh/vhVqEMTlmCJ/zkABUkNNQ==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/druid/feralcat/#eJzMVV1oHFUUnnPnZvbuaWInt2mzXkQni8o6OMvdu92aDcJu6u+DAa0Ff0DNbHbiTkmzS3aF6tNiG5CiWBTFiA+lPhixikQJKj4qpjJCrT9gqQ+KlCIqQTFvgtzZ2SZKH3xQ6XkYvvnuOd/cc7/LHBxkYEMGHMiBBD7We8sRCeNQhbvhfpiGBrSgC/AUwDEA8SFjKXubeBgp+/0NQMp+eFY/v4hsNNkrDaTso3e3I2WHlzQdRTZS9u1vQ2iybx5Dyn7+ZQgpW3xeL762CGiyZw6iyY4dRMr+eEuzX35uo5F12ZHQ/iTMPB3mLszJjVoVjgI5Ej4HZKP2ErzqH4eT/jKcm1wD2IubPXxArpYlKZXyVElKWVQFVZRFpQpFWSp4sqTWCD1N2PfkRwtHMCUG0GTvTGXTmMIBr5CX7Yvsd7mELeZLbZ4WfZaPiWtw11myI67kxB4QDC2kujiR47eISRzne5CtgGa6FrIzVKPVEAez2OdXQ+SuzUxOJoyeSFnmZSyyGvIrxOCmwITBPwZe91tzjzRbHUdJtceTZU+NTzgzDX/+0aDuNBccv14P6k7tcafTCJyFZsfvhM15px34CzMNJ9cOAmc2WPDnvBm/49Vbba+f4vVS8gfazfkbxEO4n+/D9KfUQsqOL0K8SYuTBw3BfjWThsyjYOCN3O3nnT8MmF6BPkz6eiLpq1DMl/f1KvkL/1cfHl7Ls7jDHWYWN5+EZCvF/E0l3Ka9VXpDy1PxeS9PXbT4/F08KxwcPUtGNi2Or0Jh9xaPR8XOrV52LV1sv3gvv0Pchjfzib8uouvmGOU7VwhnEB8lIkOrUJLa8aEVgozGNKkZsdBGjd8ubv3HQkqVLiFEkWSGeSBm8AF+3990ht3tOrNmiBQOoDkur8PdWYVS5HEXH0kurL1RQ3YCEjTCOabO0FgVUycgBkJbfvJ9uPSBsK6VMS+QNVgn6gARRvZ1M23o6M5Wr3x5ScepythsHF9X1DrJpJyKu0aMyyo61T76T+P6N//175Q/i6JocPrt6mRCVKf1j3wJwub64qn9X1XKMWucrkzqzCj6qXJPD5yruCZ7b3TvVVsHhB4Kd8ZjoQEtOASH+J8DAF7LDLs=).

## Other builds of this spec

- [Feral Combat (optimized)](../research/raid/builds/opt-feral-cat-dps-raid-dps.md) (9/31/11, 594 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-25000332020032012051-055001-6)
- [Feral — Cat DPS](../research/raid/builds/feral-cat-dps.md) (9/32/10, 579 DPS in a full raid) — [open the talent tree](https://talentsforever.com/druid/60/050022-55000332120032012021-055-6)
- [Feral — Bear Tank](../research/raid/builds/feral-bear-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-054-6)
- [Feral Combat (optimized, tank)](../research/raid/builds/opt-feral-bear-tank-raid-tank.md) (7/35/9) — [open the talent tree](https://talentsforever.com/druid/60/05002-5020033212003200255-504-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

