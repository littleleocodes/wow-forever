# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (17/29/5) — [open the talent tree](https://talentsforever.com/shaman/60/053303102-05303031005100224-05-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
2. **Stormstrike**
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova** when you have at least 10% mana

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman: Enhancement's **Stormstrike**, **Flurry** and **Maelstrom Weapon** with Elemental's **Elemental Devastation**, **Call of Flame** and **Trial by Fire**. It plays the Enhancement raid list: **Flame Shock**, **Stormstrike**, **Magma Totem**, an instant **Lightning Bolt** at 5 **Maelstrom Weapon** stacks, **Earth Shock** and **Fire Nova** between your swings, which with **Windfury Weapon** do the most damage.

**Why it works**

- Before the pull, drop **Strength of Earth Totem**, **Grace of Air Totem** and **Searing Totem**; the first two last 5 minutes, so one cast covers the fight.
- **Stormstrike** is your main button: 8% of your base mana, a hit for 100% of your weapon damage and 20% more on your next **Lightning Bolt**, **Chain Lightning** or **Earth Shock**; with **Improved Stormstrike** each one keeps half your mana regeneration going while you cast for 15 seconds.
- **Flame Shock** whenever the burn is off the target, **Earth Shock** on every other free shock. Your Elemental points shape them: 3 points in **Reverberation** bring the shared cooldown to 5.4 seconds, **Concussion** adds 5% to **Earth Shock** and your bolts, **Shamanistic Focus** makes them 45% cheaper, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and your Fire totems.
- **Lightning Bolt** only at 5 stacks of **Maelstrom Weapon**, when it is instant and free. This build takes 4 of the 5 points, so the stacks come a little slower than in the Enhancement build.
- **Magma Totem** replaces **Searing Totem** once the fight starts (one Fire totem at a time): it burns everything within 8 yards for 73 Fire damage every 2 seconds, and **Trial by Fire** stretches it to 40 seconds, so about 4 or 5 a fight. It costs 650 mana: drop it at the boss's feet whenever it is down while you have a quarter of your mana; below that, **Searing Totem** fills the gap.
- **Fire Nova** last: it erupts around your Fire totem, so keep the totem within 10 yards of the boss. **Trial by Fire** makes it 20% stronger on a 6-second cooldown; adding Fire Nova to the Enhancement list measured about 7% more damage in the rotation search.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a shock going between swings. The five Restoration points are **Tidal Focus**: 5% more chance to hit.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack, and **Elemental Weapons** makes the Windfury attacks 40% stronger. Keep it on: the re-tune of 2026-11-17 measured **Rockbiter Weapon** about 10% worse in a full raid.

**Caveats**

- No **Rage of the Farseer** in this build: use your trinkets and potion at the pull.
- Mana: **Improved Stormstrike** and **Shamanistic Focus** pay for the shocks; with only your own buffs the simulator's build still runs short for part of a 3-minute fight. Use a mana potion when low, and do not hold shocks back.
- Several targets: **Magma Totem** and **Fire Nova** hit every enemy within 8 and 10 yards of your Fire totem. You can have only one Fire totem out; **Totemic Call** brings it to you, with your other totems.
- For a **Lightning Bolt** caster, play Elemental: this split is a melee build.
- The page's full-raid number has no party **Windfury Totem**: in Forever your own **Windfury Weapon** switches it off for you (the imbue's tooltip), and since 2026-11-18 the simulator's full raid leaves it out for this build, which took about 12% off the number.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: you can keep only one Air totem down, and it does nothing for you while you use **Windfury Weapon**.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Elemental | 17 | Concussion 5, Elemental Devastation 3, Reverberation 3, Call of Flame 3, Elemental Focus 1, Trial by Fire 2 |
| Enhancement | 29 | Thundering Strikes 5, Ancestral Knowledge 3, Mental Dexterity 3, Elemental Weapons 3, Shamanistic Focus 1, Flurry 5, Stormstrike 1, Mental Quickness 2, Improved Stormstrike 2, Maelstrom Weapon 4 |
| Restoration | 5 | Tidal Focus 5 |

## The numbers

**How this pick was checked:** a full search on 2026-11-17 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 719 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 702 | its own set |
| Pre-BiS | 757 | its own set |
| Raid BiS | 757 | the Pre-BiS set (its own set: 709) |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 61.1; Pre-BiS 62.0; Raid BiS 62.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Truestrike Shoulders](https://www.wowhead.com/forever/item=12927) · *Pyroguard Emberseer, Blackrock Spire* |
| Back | [Heliotrope Cloak](https://www.wowhead.com/forever/item=18496) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Voone's Vice Grips](https://www.wowhead.com/forever/item=13963) · *quest: Warlord's Command*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Bloodmail Gauntlets](https://www.wowhead.com/forever/item=14615) · *Instructor Malicia, Scholomance*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Clutch of Andros](https://www.wowhead.com/forever/item=13956) · *Kirtonos the Herald, Scholomance* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Pristine Scorpid Leggings](https://www.wowhead.com/forever/item=252606) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Ring of Demonic Guile](https://www.wowhead.com/forever/item=18314) · *Alzzin the Wildshaper, Dire Maul* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Nightfall](https://www.wowhead.com/forever/item=19169) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

*This build does better outside its own set in Raid BiS (709 in its own set, 757 in the Pre-BiS set): those columns show the set made for an earlier build.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElV9II1cUxnPuTGZujmLjrdDpVGSMWGzshDuTRKIviT6VPhl9EVpaRzM6aWsSMqHYN1vtH2y1vrSgFSy0YCm1fSrYPpTSB2ulFAvFgrasuAiy+LC7LLuwD8syY7KLuq/Z/R5m7pzvDPd37jnMoEohDApo0AWj4MAMwEcAXwJ8A8AafY94XgrUY0qlsKyWUaL/OcpRAwr099dQoL84KNNfl0D5W0KJ/vWKcrUJJfrFpPK/d/94SlmTUaR/rgLK9If3wHtTpv9ugHKlCUU6/ymgSOdOwyjQhSkU6PqrKNNrS6CcNmEARbr2I0S6w9v5rptvDu4twsit0Xkgc/kVkL6yvrP2+7+F0Cf59VU4NhbzhzCXH6A+NWTgZ9LGk/EEjxvc1HkyzuPekicNzk0zofPENoFdIhyRGxK2oKwGUaA72UgIZQzqiVjSRVaNzg5HZAyioMfdB5lbtUwjlnTZZ8AmrNJbrxdLFc3kZo/Oe3Uz1aeNO1Zh0s5pxbJm5XJ2Tht7R6s4tlYuVqxKvljQXNsqjztal2vbml1wrMK4PWUXKnqu5Oq1JP0sKfaGWyy8oHZjhGnY4O1uesi7WWyOPkUlRl4OqD6mwV0fcTfL2tRWfDraTEUWnBcIBVVCEUnV37nkk3P+7DATVdIXYKhSz6D/fAjs84uVGlw3e+pS6YvYwdqxcV8KoUAPhhgJi7VSx6qlmslOH/VgiC08Aoz31gWsA9WoQiUW+g28Y/npjqL6s5CImUbK5zl5m33w+EbiXA+Fcz3cyrKQejbF32fZ+5fOyNB5oi5Mz11slcE7PTK6fFtRhBOyDddJ7l0h4KslcxckVURCIXKPhLxQYGYi8+zKsqc/0u0TvvbS5iFRRC0d3SSBJ6JKpraqq57fqNs+vf516OtMfzWQGfU++cvgPwQO01GBbj4z0Prwv8AhBRl4CQZhBBwowTRMk/sDAEjGQkc=); Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElU9MK1UUxnvuTGduD6SUK4njSMhQgsHiNHemHVLYtLAyrihsWJjIQAdblbbpVIM7FPwTIuhCUdAEE00wRt0oCZrowhiCrGpiWECMBENCCAs1L+8lb/HyMkP7XoC37XvfYjJzv29yf+eekxlUKURAAQ36YBLyMA/wLsDnAF8BsFbfI56XAvWUUikiq6+iTH/ealOOW1Cg38+hSM8+BJTpp7WI8oeEMv3thzblnzDKdO9NUP4Ko0Q/rigbMor05H0v+MvFyxL9pKL8HUaRrtYiKNKV8wgKdPN5FOjyLMr07ANQzsMYQJFubEG0P7Jb6Pv/5dH9FZi4MbkEZLGwDtIX9jf2wfDXEHqvsPkZnBgrhSNYLIxQHxwy8BPp4lYiwRMGN3VuWTzBDYNzy+DcNJM6t3YJ1IhwTP6TsANlNYgC3ctGQyhjUE/GLRdZfXVhPCpjEAU94d5L7jSSRtxy2UfAZuzyKy+UylXN5OaAzgd1MzWkTeft4otOTitVNDuXc3La1OtaNe9olVLVrhZKRc117Mp0XutzHUdzinm7OO3MOsWqniu7eiOkX4TiL7ml4tNqP0aZhi3e7qaHXMtie6yNSow8F1B9TIO7PmIty7rUTnws1k5FFlwSCAVVQhFJ3d+75pNL/sI4E1UyFGCoUs+gf74DbPVqpQbXzYGmVPoM9rBubD2QQijQwzFGImKj1Kl6qabV66MejrHlB4DxwaaA9aAaU6jEQr+Cdyw/3lJUfxaScdNI+Tynr7G3H95IXOqhcKmHO1kWUi+m+Lsse+vaGRk6TzaF6cmrrTJ4r0dG124qinBKduFfkntDCPjqyNwGSRWRUIjeISFvKTA/k3lifc3T7+nuGV/7afOIKKKWjm2TwCNRNdO4a6qe+rZp+wz617EvM8P1hcyk99VfA/8hcJSOCXT78ZHO+78GDinIwLMwChOQhzLMwRy5OwAVckQX); Raid BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElU9MK1UUxnvuTGduD6QMVxLHkZChBIPFae5MW1LYtLAyrihs2MlAB1qVtuk0BncY8E+I4AoiYMREo8aoK0jQpSYEWdXEsACNiBpZsFBj3kve4r2XGdr3Arxt3/sWkzvnO5P7O/eczEWNggIq6NAHk5CHBYB3AT4G+AKAtfoe8bwUaH9TKimyVkWJ/pJXz1pQpH++DyjQezmU6VZNUX+SUKY/7LSpf4RRoluz6q9hlOlHn4G6LaNAl+ZQpvs7bd63Ev2gov4WRpGu1xQU6cqFggJdmUOR7tYUlOnva6BehDGAIt3ehUi/clDo++/V0aNVmPh/chnIUmETpE/sr+zj4S8h9F7h8w/hL3O1cApLhRHqc0MGviNdPBlP8LjJLYMn4zzuLXnS5NyyEgZPHBCoEeGM/CthB8paEAV6mI2EUMagkYglXWT16OJ4RMYgCkbcfZC538g0Y0mXrQGbscuvvVwqV3WLWwMGHzSs1JA+nbeLs05OL1V0O5dzcvrUG3o17+iVUtWuFkpF3XXsynRe73MdR3eKebs47cw5xaqRK7tGI8m4TIq94paKz2v9GGE6tni7Wx5yLYvt0TYqMfJSQPMxTe76iLUs69I68aloOxVZcFkgFDQJRSR1//CGT674i+NM1MhQgKFGPYP+/A6w9euVmtywBppS6QvYw7qx9VgKoUBPxhhRxEapU/VSrWSvj3oyxlYeAcYHmwLWg1pUpRILfQ/esXx7W9X8WUjELDPl85y/zt5+fCNxpYfClR7uZ1lIu5zib7LsrRtnZBo80RSmZ6+3yuS9HhnduKWqwjk5gH9I7k0h4KsjcwckTURCIXKXhLxQYGEm88zmhqcf090zvo7S1ilRRT0d3SOBJ6JqprFqqp77umn7DPrPsU8zw/VAZtL76W+A/xI4TUcFuvf0SOfDm4FDCjLwIozCBOShDPMwT+4PAIwnRAQ=).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

