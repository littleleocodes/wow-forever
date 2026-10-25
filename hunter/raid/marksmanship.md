# Marksmanship Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Marksmanship

**[Marksmanship — Raid](../research/raid/builds/marksmanship-open-raid.md)** (7/39/5) — [open the talent tree](https://talentsforever.com/hunter/60/502-0053352501522051-5-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Marksmanship — Lone Wolf), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the With a pet setup. The spec's best build for each other setup, in a full raid:

- Lone Wolf: [Marksmanship — Lone Wolf](../research/raid/builds/mm-lone-wolf-raid.md) (5/41/5, 759 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-0053452511513051-5-7)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Aimed Shot**
2. **Arcane Shot**
3. **Rapid Fire**
4. **Multi-Shot**
5. **Serpent Sting**: keep it on the target
6. **Sniper Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Marksmanship plays without a pet: **Lone Wolf** adds 20% to everything you do while no pet is out. **Auto Shot** is about half your damage; **Aimed Shot**, **Arcane Shot** and **Sniper Shot** go out as soon as their cooldowns allow, biggest first.

**Why it works**

- Before the pull: **Dismiss Pet**, cast **Trueshot Aura** (in Forever a buff you cast, 30 minutes for your party) and **Aspect of the Hawk**, and track the boss's creature type, since **Improved Tracking** adds 5% only against the tracked type. In the simulator **Lone Wolf** is about 16% of this build's damage, more than any other talent.
- **Aimed Shot** comes first: it is your biggest regular hit (weapon damage plus 166, 10% more with **Barrage**), and its 6-second cooldown starts only when the 2-second cast ends, so any delay pushes every later cast back. The simulator measured about 4% more damage with it at the top.
- **Rapid Fire** gives 40% faster attacks for 15 seconds; **Rapid Killing** cuts its cooldown to 3 minutes, so it comes once in a 3-minute fight, at the pull. The full rotation presses it right before an **Auto Shot**.
- **Serpent Sting**: recast it in its last second, but not when **Aimed Shot** is half a second from ready. Each sting also starts **Rapid Recuperation** (a quarter of your mana regeneration keeps going while you cast, for 15 seconds), so it pays back some mana.
- **Arcane Shot** comes back every 4.5 seconds with 5 points in **Improved Arcane Shot**: about 33 casts a fight, more than any other button, filling the gaps between **Aimed Shot** casts.
- **Sniper Shot** hits hardest (weapon damage plus 295) but takes 4 seconds, so it goes last: start it only when **Aimed Shot** is at least a second from ready. It is not a true filler: it has a 15-second cooldown and comes about 9 times a fight, and between casts **Auto Shot** does the work.

**Caveats**

- **Multi-Shot** is on the list but shares **Aimed Shot**'s cooldown, so on one target it almost never comes up (the simulator cast it about once in five fights). It is there for groups of targets.
- Mana is tight even in a full raid: the simulator's hunter uses two mana potions a fight and still runs dry for a few seconds. With only your own buffs its rotation never casts **Sniper Shot** (365 mana) and casts **Aimed Shot** only above 10% mana.
- Moving: **Auto Shot**, **Aimed Shot** and **Sniper Shot** need you to stand still, while **Arcane Shot** and **Serpent Sting** are instant. Do not start a 4-second **Sniper Shot** when you know you must move.
- **Rapid Killing**'s other half (a kill makes your next Shot within 20 seconds hit 20% harder) never happens on a boss; on trash, let the next pull's first **Aimed Shot** spend it.
- Watch your ranks: in the beta client (build 70425) **Hunter's Mark** rank 4 gives +71 ranged attack power against rank 3's +98, and **Trueshot Aura** rank 5 +50 against rank 4's +75 (if your build has it); cast the stronger lower rank from your spellbook until Blizzard fixes the numbers. **Aspect of the Hawk** rank 7 (+120) is the best at 60. The simulator's numbers use **Hunter's Mark** rank 4, so they read about 0.3% low (estimate).

**When to change it**

- Two or three targets close together: **Multi-Shot** instead of **Aimed Shot** (same cooldown, up to 3 targets for weapon damage each). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last seconds, skip the **Serpent Sting** refresh and do not start a **Sniper Shot** that will not finish; **Arcane Shot** instead.
- With a pet out **Lone Wolf** does nothing: if you want the pet, take the pet build linked above, whose rotation puts **Arcane Shot** first.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 781 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 748 | [7/39/5](https://talentsforever.com/hunter/60/502-0053252501523051-5-7) |
| Phase 1 BiS | 777 | this build |

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 64.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Pendant of Celerity](https://www.wowhead.com/forever/item=22340) · *Lord Valthalak, Blackrock Spire* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Giantstalker's Epaulets](https://www.wowhead.com/forever/item=16848) · *Sulfuron Harbinger, Molten Core* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Giantstalker's Breastplate](https://www.wowhead.com/forever/item=16845) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/item=273470) | [Giantstalker's Bracers](https://www.wowhead.com/forever/item=16850) · *Molten Core*<br>+ [Enchant Bracer - Minor Agility](https://www.wowhead.com/forever/item=273470) |
| Hands | [Gauntlets of Elements](https://www.wowhead.com/forever/item=16672) · *Pyroguard Emberseer, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Giantstalker's Gloves](https://www.wowhead.com/forever/item=16852) · *Shazzrah, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Giantstalker's Belt](https://www.wowhead.com/forever/item=16851) · *Molten Core* |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Dragonstalker's Legguards](https://www.wowhead.com/forever/item=16938) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Giantstalker's Boots](https://www.wowhead.com/forever/item=16849) · *Gehennas, Molten Core*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) | [Barbarous Blade](https://www.wowhead.com/forever/item=18520) · *King Gordok, Dire Maul*<br>+ [Enchant 2H Weapon - Superior Impact](https://www.wowhead.com/forever/spell=20030) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVV1o82QU7knS5vT42fV7132NQSH2QmogNcmM2s+Ldt+VKMoEQe9cXLs1Y2tKU3CCF1MmjKEy75wIG2zVbUyZoCCCCHWDDirrNvwBh4JO2IUXu1K8k6Q/Y+KlGz5XJ8973vc85zlJXrqBEAcJFEiDDizZf+J0eAzyMAoVmAOQv4oixnn5VRLxy88GpNO7SMDdj4EEPG7FScSv6yAdRvzg0wHp1xiJ2KiD9CeQiKuvg/RzjAT86Y+7ScR3PgF/u4g7213+qO6fs74eIx7fmiEBN5f8fT8sgXQWoxCJeHQYl34cTGVw3ok3HelNR/nwfUifrsAicPPOu7Bmr8K2vQEnIzuwUocmQBvedu7QRW9fcAlL03VreNgyLcOwzGHdMjSryQltDn/hdkVKEMoRErC9BymkCAmaoXs01GU31iAVJZHCmpmxPLYCbNKuTL/oVmqKqZuPaIau6dnbynjJLk8WC4pbVexCoVhQXnpFqZWKStWt2TXHLSte0a6Ol5S0VywqMzPatFsuvuxOT2hV2ylovSytk5WZ8tzyg/LDpLI0Dao3MczCDY7DsK+IOMOjm+oARhj3ZEgWKUy8qXv+En7/1zPM+xeB5tUI7DvEBJm7HWIL/zRHz2rmo1dT+z5KqAz5njGBDXrGkMPE429JVr0+JWJQ8zjBGnB91j9PT7On6JaaQJ7hlD+Ggz3ovx6SegsjLLoF3fn07LEoqQ5hhOEWdDT3F+TuESza7efAZR9c4zgfJ4M9FPRzSXeYeAKDhtTBS6o7dKC5MTcq8WdcE8458zU+FCCdX4TgS8ZIHFObfNQnQ3MT+XveW/axn7t/IsB3OfOckwQlpza50P8KtXwvulI88NF/Xif7TavVujG2kx/pEvkxWABYBsc9f2P/uW9z2YANtXMjfmar9Xvu2U5wklN5/Dx5596Lv3fnLnoCRuEFKEEFZmGW/T0ASct7/A==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/hunter/dps/#eJzMVU1IPHUY3ndmdufdN9H15+pOQ8G0h9gGZpsZm2rtsKunKAqDoG45uas7ojvLzkIGHYxVEOlDOmUFBmJ+UOAliCACSVhhxVX7goSgDDx08BbdYmY/xPgf/8r/Of3m+T3ze5/3eeeDehBiIIECKdCBJbpXnA7PQg7GoQwLAPL3UcQYL79DIn73dZ908RAJePEhkIDNGpCInzZj0kmERDyqgfRnL4l4WgPpH3/rxxpIv/eSgGeBcncR/NtFPOnwW0v+OaebQDy+P0cC7qz6wl9XQbrspRCJuPYRSL8NJNO46MTqjvSeo2x9BqmLdVgBbtH5GDbsz+FLexvOR/dgfRPqAE34wBmj696+5eKWpuvW8LBlWoZhmcO6ZWhWnROaHP7B/SBSnFCO+P0cQBIpQoJm6B4NttntDUhGSaSwZqYtj60Dm7bLs2+45api6ubTmqFremZEmSzapelCXnErip3PF/LKm28r1WJBqbhVu+q4JcUr2JXJopLyCgVlbk6bdUuFt9zZKa1iO3mto9JaqvSM55aekJ8ilaVoQO3HMAvvcxyGfUfEGR71q30YYdwLIVmkMPGm7vlb+Mu/LzPvHgbN2zHYTYgJMjcSYsv/D0fPaOYzt1P7UYqrDPlOMEEMetqQw8TjXwlWuTsnYlDzLM724e6if41eYi/SkBpHnuGMP4bjA+g+HpI6hBEW3YX2fDrxWJRQBzHCcBdanrsbcvsIFm33c+yyL+5wnM+RwZ4M+rnhO0w8gUGD6sAN1y068Ly/MC7xl1wdrjjzXT4UIJVbgeBNxkgMkzt81CdDC1O5hz9Z83GYfWwqwM9Z84qTBCWr1rnQA4VqrrO6VTz+1X2vkzlqNBo9E3u50TaRm4BlgDVw3Kulw1d/ymYCNtTMjvrKRuPv7CutxXlW5fGbxNgj11/v1r/oeRiH16EIZZiHefbfALkGekw=).

## Other builds of this spec

- [Marksmanship with Beast Mastery support](../research/raid/builds/bm-mm-full-buffs-raid.md) (21/30/0, 715 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005050001-005155000150305--7)
- [Marksmanship (optimized, lone wolf)](../research/raid/builds/opt-mm-lonewolf-raid-raid-dps.md) (7/41/3, 706 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/500002-3053552011523051-3-7)
- [Marksmanship — Raid](../research/raid/builds/marksmanship-ml-raid.md) (11/40/0, 684 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5501-305355041150305--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

