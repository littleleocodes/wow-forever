# Elemental-Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental-Enhancement

*A melee shaman: Enhancement's Stormstrike and Flurry with Elemental's shock and Fire Nova talents.* (a hybrid: Elemental/Enhancement).

**[Elemental-Enhancement — Raid](../research/raid/builds/elemental-enhancement-ml-raid.md)** (17/29/5) — [open the talent tree](https://talentsforever.com/shaman/60/503303102-05303003100510224-05-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Stormstrike**
2. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova**
6. **Rockbiter Weapon**

**Rockbiter Weapon** is your filler: cast it whenever nothing above is ready.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 695 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 698 | [17/29/5](https://talentsforever.com/shaman/60/053303102-05303003100510224-05-7) |
| Phase 1 BiS | 712 | this build |

**The gear** (average item level: Pre-BiS 61.7; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Magister's Robes](https://www.wowhead.com/forever/item=16688) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Magister's Robes](https://www.wowhead.com/forever/item=16688) · *General Drakkisath, Blackrock Spire*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElV1IG1kUx3PuTGZuzorGq7Kzg7s7RnZxszthMjESfUn0adkn9cm3dTTjJvuRhExY3H3RFXEX2VX2xSVuqYV+UmLxoYItlkIpwfbJQvFBKRUbQUofSiktFFrKTJLWSl9jz8PlzLnnnvM7c/9wsZWCFyRQoAOGIQEZmAT4C+AUwAUAVufsEns3AnLJQwWvKP+OIr222iDtfYQ8nVkG5Gn+oRdF+v+mV7ojoEhXpkB6UI8ivT0F0j3bOXkOpCURebo/DyjS4mXnuEhXCiDdr0eevlyw6yxsepGnq87673W75s2zID2qRxfydGkVfF97N5IdT37q35qDoafDs0Cmk4sgnDYKxnbvRfD8nTx/AvaDc8ldmE721b2dLQZXyWdaOBTSQkFNV7VwSAtptq+Fg5qud6paeIPAJuH2SEnEFqSyYCMUwedBEd1qZyBsYVMlPF8En4hu5NSQhc0oym7kaHGgkhoMhC32ufwpNvkbKc/csxyhYJ9DolnVskcTyDsJ80VgvEx6XAzlcsu7fwL7D9iYkfn5+3Qmp+ia3qVq3aoe6VFGE0bqBzOupLOKEY+bcWXkNyWXMJVsOmfkkumUYplGdjShdFimqZiphJEaNX8xUzk1nrHUapJaTgr8aKVTX8kqtrM2rPMhUt1uXygBNvobqMDIdy7ZmT1YYS2UgC0cJQtqqt5VE7JvymTbggc5ujPIiJevko1UyPTwF86N7Ayyf94DpnXXBKwdZb9EBea5AfYfu/Jckh09dAb0YMThOfiVzRzfFbYelhf3Rl42SHGAeeSyai8NsOyxIZWlnH8msYlj00tLVSvrE7ZWnKHXJyTugGzAY6L/wbkca469AEHmkVDwvSIeO+SaHIt9spi37Va0bcyxrai+SyReifrXiOuDWC5W9WpqXy7XrE+3sw6eifVWArFh+8XJg/Ph2o36Obr2cd+hh0mDCMTgW+iHIUhABsZhnLweAHIub3Y=); Phase 1 BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzElV9IHFcUxvfcmZ25eyq6XpVOB9uOKy1221lmZ11ZfdnVp9In9cm3Orpjd/tnd9lZiu2LVqQt0rqUFosmxEBiEsIm+BDBBJOHEBaTJwPBByVEzAoS8hBCSCCQEGZ2NzGS1zXn4XLn3O/e8ztzP7jYSsELEijQAcOQgAxMAvwJcBLgHACrc1aJvRoBueShgleUf0WRXl1pkHY/QJ6W8oA8ffAfoEiPbXil2wKKdHkKpPv1KNJbUyDdtScnzoC0KCJP9/K2snjJ2S7S5QJI9+qRpy/m7HOuLdnjyoYXeTr9r628sQTSw3p0IU8XV8D3pXc92fH4h/7NWRh6MjwDZDq5AMIpo2Bs9Z4Hz1/Js8dhLzib3IHpZF/dm95icIV8EtZCIS0U1HRVC4e0kGbPtXBQ0/VOVQuvE9gg3C4pidiCVBaQp/8UwedBEd1qZyBsYVMlnS+CT0Q3cmrIwmYUZTdytDhQkQYDYYt9Kn+MTf5GyjP3DEco2PuQaFb12MMC8pYgXwTGy6THxVAul7zzB7D/gY0ZmR+/TWdyiq7pXarWreqRHmU0YaS+M+NKOqsY8bgZV0Z+UXIJU8mmc0YumU4plmlkRxNKh2WaiplKGKlR8yczlVPjGUutitSyKPC9lU59IavYztqwzodIdbt8oQTY6G+gAiPfuGSn92CFtVACNneYLKipeldNyL4qk20JHuTo9iAjXr5KNlIh08OfOTeyPcj+fgeY1l0TsHaU/RIVmOc62H/s8jNJdvzQGdCDEYdn/2f2+9FdYetBe3Gv7WWDFAeYRy679uIAyx4ZUtnK808lNnFkfmmpemVtwvaK0/TahMTtk3V4RPTfOJcTzbHnIMg8Egq+l8Rjp1yTY7GPFubtuBltG3NiM6rvEIlXov5V4novkYtVZzWNzy/UrE63Mw6ejvVWErFh+8WZB+fDtRP1c3T1w74DD5MGEYjB19APQ5CADIzDOHk1AGj9b0g=).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

