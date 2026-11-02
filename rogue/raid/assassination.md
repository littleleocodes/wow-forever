# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**[Assassination — Raid](../research/raid/builds/assassination-ml-raid.md)** (30/21/0) — [open the talent tree](https://talentsforever.com/rogue/60/0053031033150105-305313000015--7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Assassination — Seal Fate daggers). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 3 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Cold Blood** right before your finisher
3. **Eviscerate** (rank 8) when you have 5 combo points and 75+ energy and either Expose Armor is not active or Expose Armor has under 16 seconds left
4. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
5. **Mutilate**

**Mutilate** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Vanish**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

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

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 631 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 716 | this build |
| Phase 1 BiS | 719 | [30/21/0](https://talentsforever.com/rogue/60/0053031034140105-303333000015--7) (ties this build) |

**The gear** (average item level: Pre-BiS 66.5; Phase 1 BiS 66.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Grand Marshal's Dirk](https://www.wowhead.com/forever/item=18838)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Dirk](https://www.wowhead.com/forever/item=18838)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Razor](https://www.wowhead.com/forever/item=18840)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Razor](https://www.wowhead.com/forever/item=18840)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk1sG1UQ9rxd289j11k9pXS7/G0sVLkGl7e7XpM0qNlGKlQtFaE94BtZaqd2G9mR14iWkxOQQCpCAkTU5IRoKlAFUhVBFeXABSkNUg9NgIIQ0NByqFAPFUI9hR+9ddy6ia9O57D7duabmW/ezEiLj1BQQAUdkjAMRRiDOsA7AB8DfAbAYr6VCGsvaD/FKVFkbRwwTC/VQf0jijI9ewZQpt9dVjBMvzkH6lJIHL7sUm/EMUzfnAL1V3FYqIN6LY4yPX1FIBcb7mF6aWJN/8M5EeefSfH86oqCMr3wkUg0+SGot0SEM42DTJeXlMQuZbGUvDnKV/uHrr4Hub+HPwCy2j8N9Kz7ufvL3skj54G8W7oAK/vm4NYnMEj9QsCBefIo57bFLYNblmFzg9tpi9uWYXHOuWEvEvk6+THGxoGV3LHRVypjNd3kZjZt8LSZ2a0fLbrlY4W8Xqnqbj5fyOuvntJrxYJerdTcWqlS1r2CWz1a1JNeoaC7nud6XqnsW9JVt5RPN3HpBm7Xca9S3ql1YzQRwbAZRIlO57TGi13bVA5VLLFjOKg5qKTiVGbkjYAWQhmJYeNTLIWRZTmEMp3564X1ANPG6CzQhlEF7NEe9yESkyYgIKpBsO6DCJ2y2s/eBu0twFPa62gzy/cJtfgYGE/EEGchjMEkoXcy2JXaQkOMHFgDZHEPe3aDm43bUlupxHD+rmOTg/AP3vPv05oApmjx1ky7A+xJbSfq7LEN4TOtOBGH/l5ml6X1rTLS3OxUq34j+D1hSwTPg/YptLmAHtboANzHO7osUwwlZXr7xkHcz55rU9pDqW4qMzoPoq47mUZ/sx5qCbW9zfRwB3tiQySrOSMH1mYk6+Eh7SB2JbZg9DoVNICO14ewO8VoiIWPi3ync00awjl0b8CesduEO5J4CV9khzCCYQyOuKNeAR22p/XT0J5GJRHH2CxEUKJfv8yIEsSHU9upzGLzLToxBigZWU/kpzM5NtFm87jRqXZuxdjPIcFmocKIIvskFiptSRiZjpO4eOIuiYsn2GFtCJ9n+9qMirjdlk3Y0LM+f1ullm1t3i5qVGDEGLLauhp5X9rs7VSNYZ/B+zn22ma2t1Hsf3VQpZtkEW4Tc1wK+NLt/AkyEgwk/iURoQjUR5zt01NCvh3oGfHl6oC5QlRZH0jNkcADkZrTPHVUdnzRsTx9/vPwjLN3TeEMi7+cKfA/AisDKYnObRts+Rni0AsO7IchyEERxuAknCT/DwDDOOH+); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVk1sG1UQ9rxd289j11k9pXT7+NtYqHINLm93bZM0qHEjFaqWitAe8I0stVO7jezIa0TLyQlIIBWBABGRnBCkAlUgVRFUUQ5ckNIg9dAEKAgBDW0PFeqhQqin8KO3jls38dXpHHbfznwz882bGWnxIQoa6GBAHIahCGNQB3gL4GOAzwFYxLMSae0F/nOUEk3l44BBeqEO+vUwqvT6u4Aq/f6ihkH67RnQlwLy8FWXfi2KQfr6FOi/ycNCHfQrUVTp6UsSudhwD9ILE2v6H8/IOP9MyufXlzRU6bkPZaLJD0C/KSN81DiodHlJi+3SFkvxG6NitX/o8juQ+3v4fSCr/dNAP3W+cH7dO3nkLJC3S+dgZd8c3PwEBqlXCGRhnjwsRNoWtinslJkSpkgnbWHbti2EEGZ6kahXyU8RNg6s5IyNvlQZqxmWsDJJUySt1G7jaNEpHyvkjUrVcPL5Qt54+ZRRKxaMaqXm1EqVsuEWnOrRohF3CwXDcV3HdUtlz5KsOqV8solLNnC7jruV8k7ejeFYCIOWHxU6neONF7uyqRyqWGLHcJBnUUtEqcrIaz4eQBWJmcYnWAJDy2oAVTrz13PrAVYaw7NAG0YdsIc/6kEUpkyAT1aDYN8DkTpttZ+9CfwNwFP8VUwz2/MJtPiYGI1FEGchiP44obdT2JXYQgOMHFgDZHAPe3qDWxq3JbZSheH8HccmB+nvv+vfx5sApvFoa6bdPvY434kGe2RD+FQrTsahf5TZRWV9q8yksDrVqt8J/kDYEsGzwD+DNhfQwxodgHt4h5dVioG4Sm9dO4j72TNtSnsg0U1VRudB1nU71ehvxkUe09vbLBd3sMc2RLKbM3JgbUYyLh7iB7ErtgXDV6mkAXS8PoTdCUYDLHhc5juda9KQzoG7A/ZUuk24I7EX8Hl2CEMYRP+IM+oWMMv2tH6a/EnUYlGMzEIIFfrNi4xofnwwsZ2qLDLfopNjgIqZcWV+OpNjE202T5idaudWjPwSkGwWKoxoqkdiodKWhJnqOInzJ+6QOH+CHeZD+Czb12ZU5O22bMKGnvV526q0bGvzdpFTiZFjyGrrahR9Sau3UzUGPQbv5dgrm9neRrH/1UFXbpBFuEWsccXnSXf2T1CRoC/2LwlJha8+kt0+PSXlu4GeEU8uD1grRFeNgcQc8d0XqWWbp47Kji87lqfPex6eye5dU2SH5V/OFHgfvpWBhELntg22/AwJ6IUs7IchyEERxuAknCT/DwC2xeI2).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

