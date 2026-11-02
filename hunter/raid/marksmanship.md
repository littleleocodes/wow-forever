# Marksmanship Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Marksmanship

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Marksmanship — Raid](../research/raid/builds/marksmanship-ml-raid.md)** (7/39/5) — [open the talent tree](https://talentsforever.com/hunter/60/502-0053552501520051-5-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Lone Wolf), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the With a pet setup. The spec's best build for each other setup, in a full raid:

- Lone Wolf: [Marksmanship — Lone Wolf](../research/raid/builds/mm-lone-wolf-raid.md) (5/41/5, 764 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-0053452511513051-5-7)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Trueshot Aura**: turn it on before the pull; **Trueshot Aura**: turn it on before the pull.

**Then press the first one that is ready**, top to bottom:

1. **Aimed Shot**
2. **Arcane Shot**
3. **Rapid Fire**
4. **Serpent Sting**: keep it on the target
5. **Sniper Shot**

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 782 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 821 | [7/39/5](https://talentsforever.com/hunter/60/502-0053252501523051-5-7) |
| Phase 1 BiS | 812 | this build |

**The gear** (average item level: Pre-BiS 66.6; Phase 1 BiS 66.0; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Chain Helm](https://www.wowhead.com/forever/item=16465)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Shifting Cloak](https://www.wowhead.com/forever/item=18511) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Field Marshal's Chain Breastplate](https://www.wowhead.com/forever/item=16466)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Marshal's Chain Bracers](https://www.wowhead.com/forever/item=16461)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Chain Grips](https://www.wowhead.com/forever/item=16463)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marshal's Chain Girdle](https://www.wowhead.com/forever/item=16464) | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Marshal's Chain Legguards](https://www.wowhead.com/forever/item=16467)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outrider's Chain Leggings](https://www.wowhead.com/forever/item=22673)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Chain Boots](https://www.wowhead.com/forever/item=16462)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| Trinket | [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Enriched Seal](https://www.wowhead.com/forever/item=271903) |
| Main hand | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Thorium Poleaxe](https://www.wowhead.com/forever/item=250615) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Grand Marshal's Bullseye](https://www.wowhead.com/forever/item=18833)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElU1o+2QYwPO8SZO3j9rl/67b8g9+xCKjC6QmqZnbPLTbSTzI8ORFt7h2NsOtpe1hHsQMdpAxZCLCNpQJcziGgsfhwcFkMPGjm0MFP3DoBA8edpN5EMnblvkxby3/51CePk/yvL/83rwEb1NQQQMD0jANJahACPA2wC4Au5u3SNQaAf0jpFQV9ZdQoachaBd3oUS31wElevaZigptrIF2KqNCvwxB+zmBCv08BO2HKGmEoP2YQImehIAKPWvertAv2vWvdqI56ycqSvSDN6L844No5u87PdpvCRRQoa+9Dtp3valB9ThIX2zBCpDlYBPi2/57/vfjWzuwB8pq8O6b8GpwDsvBBOXskIcPSb9nu5Zte1nXcz3b8dys7TmWd0ykE0J/IgcUk0h1OcI7ghRFGSXLsWvY16rubkMqjgrGLDfj1dgSsGf9ygtT5UrdcG132HJsy35kzJgp+QvPFwtGuWr4hUKxYDz3olEvFY1que7Xg/KCUSv61ZmSka4Vi8b8vFX1g4LVblrNZmauVl4Y0h/APrOXxljskBAa0zmSnfFqbRwW1xU9hiJtlNla93Ey+BBL4T3fyogS/ebqSUZUCW+ZPVRm5AlBVzCGomM36aK2pJMxgb38Ly571HIf7SjXfZg0GRXbmjiHnXG4mV8GmKHf/38eoyvOkuzTm9x5HWUMcIo9g/1mkoqMzkWGGkcQmULi1FAz+6nM4nvQ2tj2M3g4YPZRmdE9aKJeN1Qz0fLOhww3tTeOgM11/UVonoerdWBv3WDOdTu62GPosIe5uX8YiqGIkOUb+3c/vOxwvsNwkgX/xcs6HcXjB1BdDjTxV3IMl8RdEgUe6fwK9OIt7FH/WAVNHhJ4XOZSf5J4lAnhbP725kYUn+QenOXxdc49J5pk5Mx9ItyRqOfbWVdj8P2urTPKf596Jz/eKuSn4RWADeB/hPOcKdL9gYl7r793NoxAHh6HSXgaSlCBRVgkfw0AVaSAcg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElU9oI2UUwOd9M5l5eWoy+zVtZwf/jEGW7MDEmamz7q6HZPckHmTRixfdHTdZM8U2IcmhgmAKPUgp/gOhLUqFGixFD4KHIohQKVT8k5aiglUsWsGDh96kHkTmS0L9U28JvkN4eW/mfb/5ffMxdBZBBwMsyMENqEANWgBvAawB8NtFi8Wti2B+RIi6bD5PGu62wDi8jRQ8fBlIwb3PddLwkzYYu2qcfJA2fkqRhl+0wPg+TjotMH5IkYL7rwNp+Or74nYNv+zXv2rHcxZ3dJJx9XFScEWM/K2dNn5NkUQaLr0Gxv5I9py+HeUOV2Ae2Fy0DMnV8N3wuysrbVgHbSF65w14KTqAuegqCnQowodsLHB9x3WDiSDwA9cLfNcNPCfYZsoOwx/Zx0gZQlMlBXe2IIukkuJ4boNGe9W1VcgmSaOE4+eDBp8F/lRYe/Z6tda0fNe/4Hiu4z5w2bpZCaefKZesat0KS6VyyXr6OatZKVv1ajNsRtVpq1EO6zcrVq5RLltTU049jEpOv+l0m/nJRnX6vHkPjdojmOCJTcYwYQokNx80+jg8aWpmgmTsVPkrw8fJ0308S3d8qxIp+M3xo5zpCp2x06hy9ohkapQg2XO7dHFbMdllib/wDy73kuM/OFCuuyhjc5T7mgSHm/eEmZ/HuWXe/V8e4yv2Mvyz09wFA2WM6Dp/ksbsDMocJ2NDnS2ITRHzGmTYY6jy5Dr0Nrb/DAGN26OoclyHLupJQ7dTPe9iyIWu9s4W8Mmhvwjd83C8CPzNU8z5/kAXe4g8fr8w9zdDCZIJJsTG/tWPKHuCb7N1jUf/xpvwBoonDqA+FxnyL2wbjpg/K0sicsV5GKEzlNZ/XwBDPS+JOCpk/2DJOJNat4pnl5fi+LRw7y0RXxf8A2YoVsHeYNL/Es1iPxtqnHtvaOtcEr+PvV280isUb8CLAEsg/kgHBVvGjfGrd5587ly4CEV4GK7BE1CBGszADPtzACfqgJI=).

## Other builds of this spec

- [Marksmanship with Beast Mastery support](../research/raid/builds/bm-mm-full-buffs-raid.md) (21/30/0, 720 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005050001-005155000150305--7)
- [Marksmanship (optimized, lone wolf)](../research/raid/builds/opt-mm-lonewolf-raid-raid-dps.md) (7/41/3, 713 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/50002-3053552011523051-3-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

