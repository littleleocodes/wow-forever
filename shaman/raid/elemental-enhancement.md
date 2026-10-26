# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (15/24/12) — [open the talent tree](https://talentsforever.com/shaman/60/5033031-0550300110051021-05205-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

> **Signature spells: this build fails the check** in a full raid (core share 45% under 45% (melee, Stormstrike, Windfury Weapon, Earth Shock, Flame Shock); Elemental-Enhancement is defined by **Stormstrike** cast every fight and melee, Stormstrike, Windfury Weapon, Earth Shock, Flame Shock carrying 45% of the damage). It stays on the page until a build of this spec that passes is found; the raid searches since 2026-10-22 look only for such builds (signature_spells.json).

## How to play

**Before the pull:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Stormstrike**
2. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

This hybrid is a melee shaman: Enhancement's **Stormstrike** and **Flurry** with Elemental's shock and **Fire Nova** talents. It plays the Enhancement raid list without its **Maelstrom Weapon** bolt: **Stormstrike**, **Flame Shock**, **Earth Shock** and **Fire Nova** between your swings, which with **Windfury Weapon** do about half the damage.

**Why it works**

- Before the pull, drop **Strength of Earth Totem**, **Grace of Air Totem** and **Searing Totem**; the first two last 5 minutes, so one cast covers the fight.
- **Stormstrike** first: 125 mana, a weapon hit and 20% more on your next **Earth Shock**; with **Improved Stormstrike** each one keeps half your mana regeneration going while you cast for 15 seconds.
- **Flame Shock** whenever the burn is off the target, **Earth Shock** on every other free shock. Your Elemental points shape them: 3 points in **Reverberation** bring the shared cooldown to 5.4 seconds, **Convection** and **Shamanistic Focus** cut their cost, and **Call of Flame** adds 15% to **Flame Shock**, **Fire Nova** and **Searing Totem**.
- **Fire Nova** last: it erupts around your Fire totem, so keep **Searing Totem** within 10 yards of the boss and replace it when it expires. **Trial by Fire** makes it 20% stronger on a 6-second cooldown; adding Fire Nova to this list measured about 7% more damage in the rotation search.
- **Elemental Devastation** turns every spell crit into 9% more melee crit chance for 10 seconds, which feeds **Flurry**: another reason to keep a shock going between swings.
- Put **Windfury Weapon** on your weapon with a sharpening stone on top: in Forever an imbue and a stone stack.

**Caveats**

- No **Maelstrom Weapon** and no **Rage of the Farseer** (26 Enhancement points): the list's **Lightning Bolt** line never fires for this build. Use your trinkets and potion at the pull.
- Mana: **Improved Stormstrike**, **Mindfulness** and **Totemic Focus** pay for the shocks; with only your own buffs the simulator's build is out of mana for about 12 seconds of a 3-minute fight. Use a mana potion when low, and do not hold shocks back.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem.
- For a **Lightning Bolt** caster, play Elemental: this split is a melee build.

**When to change it**

- In the last 10 seconds, skip **Flame Shock** (its burn would not finish) and use **Earth Shock**.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**: a party gets only one, and it does nothing for you while you use **Windfury Weapon**.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 437 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | - | none as a split (the search ended at 17/31/3, 30 points in Enhancement: that tree's build, not a split) |
| Phase 1 BiS | - | none as a split (the search ended at 17/31/3, 30 points in Enhancement: that tree's build, not a split) |

**The gear** (average item level: Pre-BiS 61.7; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Blue Dragonscale Helm](https://www.wowhead.com/forever/item=252604) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Magister's Robes](https://www.wowhead.com/forever/item=16688) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Magister's Robes](https://www.wowhead.com/forever/item=16688) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVF9IFF0U33Nndufu+UTX0Y9vvsFoXCFsY5aZWTdWX3b0KXrSnnzLyR3b7c/usrOE9WQiFpJKL8VaZNBfYg0fEiyIIGLZfDIIH4JITEHCh4goCIq4s2uZ79rv4XLuub97zu/eczjYRCEAEijQCn2QhCwMAVwEuAlwH0CscU8JO42BXBaoLyDI51CgT+fqpJV/kKejM4A8LXwIoECvLQakVz4U6OwwSO9rUaALwyC9ZcaNuyBNC8jTtUlAgZYeudcFOlsE6V0t8vT7FRZnfCOAPJ1bZOvlZyzmizsgbdSiB3k6PQfBA4FyqvXTye6lCej93DcGZCQ1Bb5bVtF60/kA/JdS967Dmj6RWoaRVFfN77eZ8IQ0RbVIVIvomqFq0TYtojFbi+qaYUT1MoFFwq2QBS/+i1T2MQElCPpRQK/aFo462FB1T5YgKKAXOTXiYCMKshc5WuqpUvVw1BH3ynuwIVRPedE7xhEK7B4SzdkMu51A/iBMlkDkZdLhEVGupHx9AcSrIA5Y2VNHM9m8YmjGQVVrV41Yh9KftNLH7YSSySlWImEnlGNnlXzSVnKZvJVPZdKKY1u5/qTS6ti2YqeTVrrfPm2n82oi66ibJLVCCp9wMun9sootYjPWBBGpwdIXVwHrQ3XUJ5LDHtl9u17VWlwFcXy7Ml1TtfYdUdaCckiiPtH/HJiwx18l2f32trChx9xCrJ8RR3fvp5q2VpH7VUUmpNQj+uVKczzsEXO7JqnSMYUvksStkzJ8JMZ5zuOi0fwGPplHQiH4g/iZyzM0YP4/VWB4GW8ecLEUN5aJxCvx0Dzx/BXkzU1rR7FvZsfytLvrkdtmZ9Vh9rGpWgB341mOhzg6/1/XluGrQQxMOATd0AtJyMIgDJKfAwA0rBtW); Phase 1 BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVE9oE00Uz5vdZCfvK2267ce331Jxm4LUyIbZTVfSXpL2JJ5aT73Ztdma+CcJ2SDVUy1FpWiDCEqqWEGrIlF6sFBFPIiE2FMF6UEQS22hiAcRURAU2U2qtffW32GYefObeb/3h4ctFAIggQLtMABJyMIIwDmAGwB3AcQ695Y4t1GQKwL1BQT5FAr0yWyDtPwP8nSlAMjT4vsACvTqQkB66UOBzoyC9K4eBTo/CtIbZ3P9NkhTAvJ0tQAo0PJD97lAZ0ogva1Hnn6/7PzzdNpZZxcCyNOxSw7z+TRIH+rRgzydmoXgnkAl1f7paO/iBPR/HhgHMpaaBN9Ns2S+7r4H/vOpO9dgVZtILcFYqqfud2xxeExaDBYxWERjusoMg0UY0zXGDI3puqFVCCwQbpnMe/FfpLIPeXqxDEE/CuhVO8KGjU01c6EMQQG9yKkRG5tRkL3I0XJfjaqFDVvcKe/AplAj5UXvOEcoOO+QMHv9280E8gehUAaRl0mXR0S56vLVWRCvgDhkZo8dzGTzis70vSrrVPVolzKYNNOHrYSSySlmImEllEMnlXzSUnKZvJlPZdKKbZm5waTSbluWYqWTZnrQOm6l82oia6vrJLVKCh+xM+ndsoptYivWBRGp7rgvrQA2hhqoTyT7PbIbu1bTWloB8cJmZRpTWeeWKGtDOSRRn+h/Bo6wR18l2U17R1jXom4h1k6IZ7YvUy0bq8j9qqIjpNwn+uVqczzoE3PbJqnaMcUvksStkQp8JPppzuOiOf4NfDKPhELwB/E7Js/IUPz/yaKDF7HWIReLMX2JSLwSC80Rz19BPr6+21Lsur9lfjrd9cCteHfNEB9wpmoR3INnKRbi6Nx/PRuGL4MoxGEf9EI/JCELwzBMfg4AY3QbKA==).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

