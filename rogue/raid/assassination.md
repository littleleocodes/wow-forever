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
| Pre-BiS | 652 | this build |
| Phase 1 BiS | 710 | this build |

**The gear** (average item level: Pre-BiS 63.2; Phase 1 BiS 67.2; each item opens its Wowhead page, with where it drops and its enchant):

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
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Pants](https://www.wowhead.com/forever/item=16909) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21202) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE9IHGcUnzcz7n6+ruvwUXEcShk9lHXLtN/suNbV0l2F0tJelPbgrU7dtbvV7iy7K9UeijEJCZiQ4CHEkEOCCRiSgJggwWsSWWECakwOwRASc5DgYQkkJ0PCzPpniR5jyO/0m/f9ft9773vDQx8BCWRQIQAMaN3OF8+gBWLQCd2QgREAZZIQXhKV/9FLXl0F+flnKJAbQyiS+7aEHnI+KS950Etu36yW1/zoJYcnQH7sENuW5Cd+FMnYooReMj3umr3k1EZVKf7mDKBIli8DCuTkPyiSi6cBvWRlSZI3nAvuLLpEJMtLUkNQKqTkE6nA+gDbbItB59gydM+swDjwm21nYdK8ANfMKVhtLwB04G5vc3w9Y2GDGToLh/QwYyysGSxs6AZjjOmGxliowIvP+EseegyUI4DDyr8YpgZKQT/xUGEUOKUCBQQd/Q0+xBnwYkWAJ6+bsDpYRTyU/2VL0Iw/0O/32MJYG6whAsW5HWNJbrj+il1/RNkWUEnxl2dq5ejXSiOq9Ms91zeV65x7yNM0HQWaMjMDf1iZvBpioWZNZxrTW9XepJn+KxFXraxqxuOJuPrnsJpPJtSslTfzKSut5hJmtjepBnKJhGrmcmYul0q7J1rWTMW1bZ1W0n3zd85KNyo16HvkqUSBzFvU+VOcIuatfYvQmw68iNn+nSJm++lvShf+RH/c59l05dvyp9tS8P9xigdF5L+LuOMRysbrHJCpl0BRIS4vrv1KB99rkkW0UMtBNVlKu3IX6ODHHHAp7dsRkIV1vgBFPnRI4Fx8HnsBIvLINVwRKp0AN9IXqzs34WAhWt/n4mE0VORlUY0GCzz3SSEf22YHiq+uf/A8kXu2bft6pmPtW4FYDxwHmICUVTy68PuDaMSNcovRdkdp2xvRrhJZjQYFcqu244vdHVna+D+7Oz8JGRiCIfpuAMLePjA=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE9IHGcUnzcz7n6+ruvyUXEcShk9lHXLtN/suNbV0l2F0tJelPbgrU7dtbvV7iy7K9VeulWXBlSUeIkhh4QIMRAhSJDgNURW2IBJTA7BEBI9SPCw5JCTkDAz/lmixxjyO/3mfb/fe+/73vDQQ8AHEijgBwa04eiLZ9AGUeiGXkhDHkBeIIT3ifK/6CZTEyDtfIIi2ZkBFMnDkg9d5FJCuu9CN7lzq1ba9qKbjM+D9NQiq+MgPfOiSCY3fOgm047bTWb2apz4tYKVpjAHKJDpv1AkV2YB3SQ/B9KelWDWISJZKkBTwFdMSlNJ/+4Q2++IQvfkA+hd3oTzwO93XICrxmW4YSzCVmcRoAuPL7fKNzIW0pmusVBQCzHGQqrOQrqmM8aYpquMBYu8+IJfcNH/QZ4AHJX/xhDV0RfwEhcVxoCTq1BA0NDb5EFcBjdW+XnyugVrAzXERfmfDgSt+B399oQthPWBOiJQXD0yOnLd9lcd+8PyoYD6ZG9lpXaOfik3o0I/P5G+pVJn5SHPU3QMaNJID/1mpnNKkAVbVY2pTGtX+hNG6o94TDEzihGLxWPK76NKLhFXMmbOyCXNlJKNG5n+hOLPxuOKkc0a2WwyZZ+oGSMZUw91qqP76s+smWqW69DzxFWNAlkzqfWrWE2smac2obWceRMrg0dNrAzSX+Qe/IF+f8qzafLXlU93oOD/4WQXish/E7bHI1SM1zogi6+AokxsXt7+mQ6/c0kWVoNtZ3VJp+zmXaDDH3LATtk3eZCEXb4IZT74n8DZ+DT6EkTkkWu6LlRbAS4/EG24OG9hPdI4YONxJFjmJVGJBIo891EhFz1kZ4ovlt57nfC9Uqnk6bsZ7TwIRPvgHMA8JM1yYf3XR5GwHeU2Ip2WslTai/Q4ZCsSEMjt+q7Pjneks/J/tJd+AtIwAiP07QB8bTrq).

## Other builds of this spec

- [Assassination — Seal Fate daggers](../research/raid/builds/assassination-seal-fate-raid.md) (30/19/2, 702 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031232150005-305313000013-002-6)
- [Assassination — Seal Fate / Vigor](../research/raid/builds/assassination-mutilate-raid.md) (30/21/0, 690 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031252112005-305313000015--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

