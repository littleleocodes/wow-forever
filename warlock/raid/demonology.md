# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Demonology in a raid is a **Shadow Bolt** caster with two demons' worth of bonuses: you sacrifice the Imp for 15% more Shadow damage, and **Demonic Pact** keeps that buff while your Succubus fights. Then you keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it; the simulator measured about 10% less damage without the sacrifice.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add about 9% of your damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% about 0.5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so none of your Shadow bonuses reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die (6 seconds with **Master Summoner**) and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Summon her after your buffs, wizard oil and Spellstone (**Create Spellstone**) are on: in this project's model a demon copies its share of your spell damage when it is summoned. Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** is not in this build, so keep it for when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 832 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 801 | this build |
| Phase 1 BiS | 836 | this build |

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 65.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire* |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire* | [Nemesis Leggings](https://www.wowhead.com/forever/item=16930) · *Ragnaros, Molten Core* |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlE9II1ccx/N7M8k8f/VPfKU4vrYwTVHS0JE3E8YaL4mepCcLPRQ81MRMTEQzIclBb7ZaWkqx0ksxtLRCxQq1pO3F9tQWwkbILl52Ydd1d/Gye9iDuJDLXpaZxBXWyx5Wdr+Hme983+8383nz4IedFIKgggZhEMDeffpEBIxAAibhE5iGLBRgGeArgHUA/odCpWAHd1Cmj3cBZXr8vXu996gLFXpzE9RlggG6n1d/VlCh/2+BetiNEq3NokzvNLtQoqcZVGj1N1C/VVCmP54GUaZXtt2iz22U6PoCKvTWJqj111Gmf/8Obst86H26mgvWc9r2DxC+tgaimfoayGruOyDN1K9wf6wKP23BHlQnDmAtN47nG/uHhIRh6EKYlhBRETVMU0SFEbUMXViWEMKN60Q6IK8dk7/87G3+JvaGerDrT0CU6b9fTjIS9PNA25tcYJgNYm+khwYY+dDHFfSjZFglL5IZSbWjD6wBLiNRe1mUG8/ZMywGuB+lYDPFZE5GfS2a1nvP2qJDlkez8g2wFWCZZGH+U6dQ1kxhDusippsjo9pMNpmftdOaU9SS6bSd1lJLWjlra0WnnCznnLxWspPFmawWLtm2lrYXnLwz78wu6cVkLq2fFemtoqG5kpN/j/djMNJNJW9/AZSRWB4q3ZliIa5hX+QNKjNlzo3+m+K0QtqudWO/PEtqCF2Yl0I6ioINYX+kj8qMzrm/6m4NeEeFtO2FcxAl3l56uZhH55hHFzHNNuZRDRhy6vnDGqjSA1KHE2J+Jvk8xRIV0omIlEoaGSEJCO1IHe6CbzmT6K9suNqPv5PxdCNunhBV0eKROvG9UionztylanD3hX8ndrXRaHROVxNj7SAx7U7PDcg5J1/sf3w9HvNS30F8zK1sNB7GP2qZ2/GIRPf6xt86H1+tSTzhzeIsFGARFtmTAQB/5BSA) · [training dummy](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMUU1oE1sYnXtnkrn9Xn/S+3h0eh8P7ouk1uCUOxOmNt0k7UpcKbjrwibNpE1pMyXJwu6qVhTRKm6kQdGCpRasBN1UVyoUU4jSjYLWP7rRhYtSIRs3MsmUom5cWPEs5juc73wzhzMgUYktqEQONDAHFPJlCYFCNq64z/efm0AlL+eQNoXBT1az2g0VVPJ4HmnrzSCTlWFQyNtqE8hkKw0qKd1G2kUVFHJtKwAKebLgmk7aIJNL46CSV3NIK/8NCrl/B7knY8H9ZDoTKGf4wlXU+WwGiWryHMLTmcsIV5O30Ie+Ero+j5ZR6eAamsn0Sw9w0BCGLoRpCREREcM0RUQYEcvQhWUJIVy5jOU1/NcGvuej/7F/oTXYAk13EYBCHp45THHAx/weN5mATtoBreEW4qf4kMRU8IFsWPmapFCc9KQDVogpgLVWGmHGT950ixDzgRyoJqnCcK9UT1N/7/ZZpMuqpTl1HtEg49AW/ocoVB31gUweDTBSxB6rD3oT0XRiYuyYM1HgpjC7dUPowuzlQyOJ7LCd4k6OJ1IpO8WTk7wwYvOcU0gUMk6W5+1EbmiEd+Ztm6fscSfrjDnDk3oukUnp2ya9buoazTvZfawXBO2C9nAbUSgZdUO+W0GsoYg9+kMDIs+8FS1+H1NEdbNnV2IK2EtDtSzyTvWGFYJAuNmL5wcFcHfe/RlkcYBe+H0d7vmmvzc7/bnUmxQYqRW3voI0+SMuo01snpClGqLxIm4EAEJkjntwHAUX5QZ3IU2l4+3FWRersf/TNbyImZtYU3ksXMbSH4VCfJvtKjqWfvl3ok8rlUrjYCne5wnxQXQWoVmUcTZPrx59HovWVGkt1uc6K5VPsSN18joWlslyW790nH4dAOsVCs8=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlE9oG0cUxvVmV97xq//IU4rX0xa2Kjaq6JrZFetavkj2yfTkQg8FH2rJWlsyrlZIOtg3t5ZpKcUtLj5YtPQPNY0hDiLJwckpCQhkoiS+JBAck5BLcsjBOOBLIIRdyTHElxxiku+w++333uz+ZgcetlEIgAoahEAA+/TlExEwCHEYg29gAtKQgwWAnwB+A+AXFSoFWnkeZfpsE1Cmz1fc64On7ajQu/+AukBQoduroP6toEKvrYO624ESrU6jTK+sur3/lgAVWjkL6q8KyvTPgwDK9LpXKv0OKNEfbFTorSVQa++jTC+dc7OD2eDntJQJ1DLa/39A6OYyiMPkz0BKmRUgh8kz8Gi4An+twxZURndgOTOCx3u7TILCMHQhTEuIiIgYpikiwohYhi4sSwjhxjUi7ZD3HpILfvYx/xC7gp3Yfh7Qpf5xjJGAn7c0vckFhlgfdoU7aQsjX/q4gn6UDKvgRTIjyWb0hdXLZSRqF4tw4zXXDIhe7kcpcJhkMidDvgZN471HyyL9lkez+AuwRWBTidzst06uqJnCHNBFVDcHh7TJdCI7bac0J68lUik7pSXntWLa1vJOMVHMOFmtYCfyk2ktVLBtLWV/52SdWWd6Xs8nMin9qElvNPXPFJzsZ7wHA+EOKnn7a0EZieWh0o1xFuQadoc/oDJTZtzo6jinZdJ0jRv771VSQ+jCPBXSIRSsH3vC3VRmdMb9VferwFvLpGlPnIMo8Gbp7WLuHWPuncQ0m5h7VWDIqed3q6BKj0kN9on5veTzFI2XSRsiUippZJDEIbghtboF38JUvKe85mo79smUpzsxc5+oihYL14jvnVIxfuROVX2bb/w70Rv1er1tohIfbgbxCXeArkHG2V/a/vp2LOqlvp3YsNtZrz+JfdUw92JhiW51j3x0PL4aw3jUG8dpyMEczLEXAwCivRPl) · [training dummy](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMkU9IFFEcx+e9mXWev/yzvgjHF8G0sWZLI29mGXO97OopOhV085C77qgjtiO7e8ib1UoRZWB4cCn6Q1JGxlIX61SBsNJWXgrCouhShw5i4CWImNkRqS4dMvoe5n35/n5v5sN3QKACuyMTMVjLsiCRb/MIJPJ9yn1++FoPMnlzHSnjGGSyNI2UazLI5OksUlYaQCSLgyCRx9Pu7o0CApmU7iLlogwSubIWBIk880aFSwhEcsoCmbycQEp5O0jk4T03WxsJ7ScFO1i21VuXUduLScTXU+cQLthTCK+nbqNP3SV0dRYtoNLBZTRp9wiPcEjnusa5YXIe5VHdMHiU61FT17hpcs7duIzFZbztI34QoLvYTmgKNUL9fQQu65nDFAcDrMb3BuPQRluhKdJIaig+JDAZAiDqZs6LJIpTfnTADDMJsNJEo0z/wzsdPMwCIAbXU1RiuEuo0lTfu3Et2m56NKfPIxpiKjRHdhCJysMBEMmTXkaK2HfVg95EdCA5OnLMGc2rBjc6NJ1r3OhS+4eSmUErrTpZNZlOW2k1Nabmhyw16+STedvJqDkrme0fUttylqWmreNOxhlxBse0bNJOaxtLWnWpfTjnZPaxLuC0HVoizUSiZNiFfL+IWG0R+/a3BniO+SNa/BWTxzSjc0swOeylYY9F3KxeN8MQjDT4eDUgAe7IuT+DzPXSC/+uwz0/9fdusz/X+icFRrziVhaRIn7GZbSKjZOi4CmWKOI6ACBEVHEnTqDQnFjrDoTxgURLccbVUnz3gKfXcWMVK7Iaj5Sx8F8pn9hwW6rW+b/+ndjzSqVS11dKdPtBog+dRWgG2c7qxNLRV/GYlwrL8W53s1L5Ej9SNW/jEZEsNPcIJ+iPAQAURgo0).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 827 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

