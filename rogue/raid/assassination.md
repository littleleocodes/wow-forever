# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**[Assassination — Raid](../research/raid/builds/assassination-ml-raid.md)** (30/19/2) — [open the talent tree](https://talentsforever.com/rogue/60/0053031052150005-305313000013-002-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 3 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Cold Blood** right before your finisher
2. **Eviscerate** when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
3. **Backstab**

**Backstab** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Assassination in a raid is a Seal Fate dagger rotation: **Backstab** from behind builds combo points, often two at a time, **Slice and Dice** stays up, and every 4 or more points go into **Eviscerate**. **Cold Blood** goes in front of an **Eviscerate** whenever it is ready.

**Why it works**

- **Slice and Dice** is 30% more attack speed: more white hits, and more chances for your poisons, which can proc on every weapon strike. Put it back up the moment it drops, even with 1 combo point. With 5 points and under 3 seconds left on it, refresh it before you **Eviscerate**.
- **Eviscerate** goes at 4 or more points because a **Backstab** often brings two: **Seal Fate** adds a point to every **Backstab** crit, and **Puncturing Wounds** raises its crit chance by 30% and adds a point 45% of the time. From 4 points that second point would be lost at the cap of 5, and **Ruthlessness** adds a free point after 60% of your finishers.
- **Cold Blood** spends no combo points: it turns your next **Sinister Strike**, **Backstab**, **Ambush**, **Eviscerate** or **Mutilate** into a critical strike. Press it with 4 or more points and **Slice and Dice** up, then **Eviscerate** right away, so the crit lands on your biggest hit instead of a **Backstab**.
- **Backstab** is your only builder and your filler: 60 energy, from behind the target, with a dagger in your main hand. **Malice** and **Lethality** make its crits more frequent and bigger, and every crit also feeds **Seal Fate**.
- Poisons are a real share of your damage: **Instant Poison** on the main hand, **Deadly Poison** on the off hand, where it stacks up to 5 times. **Improved Poisons** raises their chance to land and **Vile Poisons** their damage; **Deadly Poison** alone did 8% of your damage in the simulator's training-dummy runs.

**Caveats**

- **Backstab** needs you behind the boss with a dagger in your main hand. When the boss turns to face you or you have to stand in front, build with **Sinister Strike** until you are behind it again.
- There is no **Expose Armor** in the list: in a full raid a warrior keeps Sunder Armor on the boss, and the two do not stack (only the stronger one counts).
- Poisons now go on a weapon together with a sharpening stone (Blizzard's rogue deep dive, 2026-10-07), so use both.
- This build has no **Mutilate** or **Venom**, though Blizzard built Forever's Assassination around them. In the simulator **Backstab** with **Puncturing Wounds** out-damaged **Mutilate**, the talent search dropped **Venom**, and the simulator's own Mutilate build did about 5% less than this one in a full raid: check it at launch.

**When to change it**

- In the last 6 seconds, start no **Slice and Dice**: put 4 or more points into **Eviscerate** even with it down. If the boss is about to die with 1 to 3 points, an **Eviscerate** still beats keeping them.
- If no warrior keeps Sunder Armor on the target (a small group or a dungeon), keep **Expose Armor** up with 4 or more points, refreshing it before it runs out. On the training dummy, where nothing else lowers armor, the simulator measured that about 9% better.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 707 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 647 | [30/19/2](https://talentsforever.com/rogue/60/0053031052150005-304313100013-002-6) |
| Phase 1 BiS | 703 | this build |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 63.1; Phase 1 BiS 67.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Hood](https://www.wowhead.com/forever/item=16908) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Nightslayer Gloves](https://www.wowhead.com/forever/item=16826) · *Gehennas, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Pants](https://www.wowhead.com/forever/item=16909) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE1oE2kYnndmknx9N02Hjy2dDssy7WFJs8zuN5mm27TLJi0su+xeWnYPvW1nm3STpWZCkmIrCLUqCrUoHsSKouKlooJUD9KrWlIYoa21B6mI1kORHIKgp4oyk/4E69GKz+mZ93ue94/hRT8BCWRQIQgMaOP2F8+gHeLQA32QhTEA5YKP8JKoHEQfeX0N5BdfoUBujaBIHtoSesn5lLzoRR+5e7tOXgugjxyeAvmJQ2xbkp8GUCQTC45wZdjx+sjJUm0l/PYMoEgmSxIKZHIfiuTyKUAfWV6U5JLjv7fgEpEsLUrNIamYlk+kg+tDbKMzDj0TS9A3swyngd/oPAtXzEtw3ZyG1a4iQDfujDbLNzEWMZihs0hYjzDGIprBWg3d0BljuqExFi7y4nP+ooceA+UI4KiyHyPUQCkUIF4qjAOneFBA0DHQ7EecAR96gjx504p1oVripfwfm4I2/IX+vMsWwYZQPREozm4bK3LD9Xt2/FFlS0AlJVBdqYOj3ystqNJvd6VvrdY5ecizDB0HmjazQ/9Y2YIaZuE2TWca0zvUgZSZ+S+ZUK2caiYSyYT676haSCXVnFUwC2kro+aTZm4gpQbzyaRq5vNmPp/OuC9azkwntC2dVtH98H/eyrQo9eh/7K1BgcxZ1PlRnCbmLPqX0ou/0V8/0rGu/Fjd9aaCP8ApXhSR/ynqbkao2qzzQKZfAUWFuLy89icd/mBIFtXC7Xs1ZKXs8n2gw59zt5Wy78ZAFtb5IpT58CGBc/F1/CWIyCPXfFWocQLc2GC88dyUg/lY06CLlVi4zMuiGgsVee6LQiG+xfYU39345HWiD2zb9vffjHdtBuL9cBxgCtJW+ej8349iUTfKLcS6HKVtl2K9FbIaCwnkTkP3NzvnqXJrf3evbQqyMAIj9P0Au+IUVA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE1IHGcYnndmdufz7bouHxXHoZTRQ1m3TPvNjmtdLd1VKC3tRWkP3urUXbtb7M6yu1LtpVt1aUFFqZcYAibkEAMRguQQvIbIChswickhGEKiBwkelhxyEhJmxp8l5hhDntMz7/c87x/Diz4CAZBBhSAwoM3HXzyDTohDHwxAFooAypJE+ICo/I0SmZkCefcjFMnuHKBI7lcC6CUXUvJdL0rk1o0GecePEplcBPmxTdYmQX7iR5FMbwZQIrOuWyJz+/Vu/ErJTlNaABTI7B8okkvzgBIpLoC8byeYd4lIVkrQGgqU0/JMOrg3wg6649A3fQ8GVrfgf+APus/BZfMiXDOXYbunDNCLJ8Ot8S2MRQxm6CwS1iOMsYhmsIihG4wxphsaY+EyLz7jlzz0X1CmAMeVPzFCDQyE/MRLhQngFA8KCDr6W32IqyChJ8iTl+3YEKonXsr/cCjowG/o16dsEWwKNRKB4tqx0ZUbjt9z4o8qRwIaUPy1lbo4+rnShir99FT69lqdnYc8zdAJoGkzO/KLlS2oYRbu0HSmMb1LHUqZmd+SCdXKqWYikUyov46rhVRSzVkFs5C2Mmo+aeaGUmown0yqZj5v5vPpjPOi5cx0QjvSaa7ui9/zVqZNaUTfI28dCmTdovavYjexbtGflH78jn77lo515cvarg8V/F+c4kUR+a+izmaEms3aD2T5BVBUiMOrOz/S0TeGZFEt3HlWQ7plt24DHX2fu3XLviqCLOzxZajy4X8EzsHH8ecgIo9c61Whzg5wxeF48/lFGxuxlmEHD2PhKi+LaixU5rkPCoX4ETtTfLbyzutE71QqFd/g9XjPYSA+CP8BLELaqpY2fn4QizpRbjPWYysrlf1Yv0u2YyGB3Gzq/eTkPLnX9nvn3qYgC2MwRl8PANFEEPg=).

## Other builds of this spec

- [Assassination — Seal Fate daggers](../research/raid/builds/assassination-seal-fate-raid.md) (30/19/2, 702 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031232150005-305313000013-002-6)
- [Assassination — Seal Fate / Vigor](../research/raid/builds/assassination-mutilate-raid.md) (30/21/0, 690 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031252112005-305313000015--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-10 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

