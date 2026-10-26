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
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Beaststalker's Gloves](https://www.wowhead.com/forever/item=16676) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) |
| Legs | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElE9INGUcx+f3zOzMs79sd3xcdRz6My0h68BsM2NjaoddPUWHkLp0KZ3ctR1Jd9ndg0GQlocQibqEimGwLonUISiQoIshbCSoWQb9ITGDDh28he/h5WVmd/F9X3xvLu/3MPzm9515nu/zeWYe7KEggwIaJGACclCAeYDPALYAWFtgEd8aBPUkTKnMq++gRL/7JqqcP4ICrawACvR4X0aJfl8F5Uj0i6+jyt8RlOj7q6D86Reb74HyVwQFur8OKNGPvwL/dYlWmv1fqv44nxzKKNDamYw8rbyCEv2/GlX+iyCHEv3pSFZ+74j3yjUvcb4BS0AWvTUIV9wv3D9GNqqwDdKy9/k6fOidwqI32na1qjR8S7oc0zZM0+m3HdsxLcfuNx3LcGpEOCT0jPwsYQypKqJAD/cgTlFEwbDMEnY2ulsViIdRwpBhJ50SWwD2ult4azxfKGu2aQ8YlmmYzw5rkzl39s1sRssXNTeTyWa0N97WyrmsVsyX3bKXn9VKWbc4mdMSpWxWm5kxiq6XMZqmUTeT06X8bJ/6JHbqHTTEQruE0JAaRDKTTqkZh4VVSQ0hTw/y7KPWx0ni0yyOj/4mIgr018uXGJEFbNejVGTkRU6VMIS8ZdbT+bagkmGOvXtfLnPIsJ+70VyPY0xnlG9iCnKYSSsg808309QnHsTRf+I4xn68jp1zoxk9HGevYZceozyj0z6hgz3wSSGxSqjoXVRk4W1obGxzDQ52651UZHQb6lGvDFmPNLgHgwzUsR/sAZtu+YdQ/x8uV4B9eg05277RyZ5Hiz0TkLuHUAh5hP5gY+/mE7StIN/u/JjC/0tqcEHsBZ4LlEgvQQe2Y1S+tQyK2McFukjFb5OwX3HzU+metVVfP6Semgp0krJPiSJoKX2HcA9F5XSzaql6v2zZPEPB9eXN9EijkZ6ADwBWIbjhTlM6T3e6Rx+7OrFNGIQ0vABj8CrkoABzMEfuDABm7165); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElE1oK1UUx+fcmczcHGsyvU3b6eDHGKSkAxNnpk5t6yJpV+JCim7caDs2qZlim5BkUUGw1S6kFL9AMKVSIQZL0YWgUAQ3lUKKhVaqFfzAUiu4cNHdo2/xeMwkoe89+nYN778IJ+c/c+7//u7MYB8FGRTQIAFTkIMCLAJ8DrAJwDoCi/jWMKjHYUplXn0LJfrDd1Hl7CEU6NkHgAI92pdRoj/WQPlZ9Itvo8o/EZTouxVQ/vKLvX1Z+TuCAt1fB5ToR9+Af7tEq+9Ao/9rzZ+z8wkgT6svoUDrp/7IG7Wo8n8EOZRo5WNQ/uiK98t1L3G2AStAlr01CFfdr9w/xzZqsAXSqvflOrzvncCyN95xuas0fE96HNM2TNMZHHRsx7Qc2zYdy3DqRDgk9JT8ImEMqSqiQA93IU5RRMGwzBJ2N7ubVYiHUcKQYSedElsC9qpbeGMyXyhrtmkPGZZpmE+PatM5d/71bEbLFzU3k8lmtNfe1Mq5rFbMl92yl5/XSlm3OJ3TEqVsVpubM4qulzFaptEwk7Ol/PyA+jh26100xEI7hNCQGkQyk06pFYeFVUkNIU8P8uzD9sdJ4pMsjg//LiIK9LeLFxiRBezUo1Rk5HlOlTCEvGU20vm2oJJRjr19Ty5zxLCfudZcj2JMZ5RvYQpymEkrIPNvL9PUx+7H0b/iKMZ+uoqdc60ZPZxkr2CPHqM8o7M+oYNd8EkhsUqo6D1UZOEtaB5saw8O9urdVGR0CxpRLw1ZjzS5B0OGGtgPdoHNtv1BaLwPF58C++wKcrZ9rYs9ixZ7KiB3F6EQ8giDwcHeySdoW0G+ncUJhf+P1OGc2Es8FyiRXoEu7MSofHMVFHGAC3Seit8iYb/iFmfSfWsVX3upJ2YCHafsE6IIWkrfJtwDUTndqtqq/q/bts5I8PviF+mxZiM9Be8BVCD4w52kdJ5u944/cvnFNmEY0vAcTMDLkIMCLMACuT0A/2Jeyg==).

## Other builds of this spec

- [Marksmanship with Beast Mastery support](../research/raid/builds/bm-mm-full-buffs-raid.md) (21/30/0, 715 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005050001-005155000150305--7)
- [Marksmanship (optimized, lone wolf)](../research/raid/builds/opt-mm-lonewolf-raid-raid-dps.md) (7/41/3, 706 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/500002-3053552011523051-3-7)
- [Marksmanship — Raid](../research/raid/builds/marksmanship-ml-raid.md) (11/40/0, 684 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5501-305355041150305--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

