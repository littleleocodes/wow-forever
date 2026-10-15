# Restoration Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Restoration

**[Restoration — Raid healing](../research/raid/builds/restoration-ml-heal.md)** (11/5/35) — [open the talent tree](https://talentsforever.com/druid/60/05122001-05-232033505310305-6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (resto-raid-healer), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

Keep **Rejuvenation** on the tank and heal it with **Healing Touch** at the rank that covers the health it is missing. **Regrowth** is for raid members who drop under half health, **Swiftmend** and **Nature's Swiftness** are your emergency buttons, and mana is what runs out first.

**Why it works**

- **Healing Touch** is about two thirds of your healing in the healer lab. Start it on the tank when it is missing at least half of what your top rank heals and the next boss hit is on its way: **Naturalist** cuts the cast to 3 seconds, and a rank sized to the missing health saves mana over the top rank (840 mana, 10% less with **Tranquil Spirit**).
- **Rejuvenation** stays on the tank whenever it is missing more than a tenth of its health, always at the top rank: it is instant and costs 360 mana, **Improved Rejuvenation**, **Gift of Nature** and **Genesis** add to it, and **Nature's Splendor** stretches it to 15 seconds. **Gift of the Earthmother** cuts its global cooldown to 1 second.
- **Regrowth** is the fast heal: a 2-second cast with a big direct heal and a heal over 21 seconds (27 with **Nature's Splendor**). The lab gives a raid member under half health a **Rejuvenation** first and a **Regrowth** if they still need it, and casts **Regrowth** on the tank when it is missing about a full one; **Improved Regrowth** raises its critical chance.
- **Swiftmend** heals at once for the full amount of your **Rejuvenation** or **Regrowth** on the target, every 15 seconds: your instant answer when a raid member falls under 55% health. It only works on a target with your heal over time, one more reason to keep **Rejuvenation** on the tank.
- **Nature's Swiftness** makes your next **Healing Touch** instant: use it as soon as the tank falls under 55%. With a 3-minute cooldown, holding it for a worse moment wastes it.
- **Wild Growth** heals the target's whole party, up to five people, for 679 over 7 seconds (1,050 mana, 6-second cooldown): cast it when three or more people in one party are under half health. The lab's test fight rarely had that, so it measured no value there; in fights with heavy raid damage it is the heal that covers it.

**Caveats**

- Mana runs out before cast time does: in the lab's five-minute fight the build spends about 30 seconds out of mana, and **Reflection** (half your mana regeneration keeps going while you cast) is worth more than any other talent there. Drink a mana potion once you are 20% down after the first 45 seconds, and **Innervate** yourself under 40% mana: the lab measured early potions as 1 to 2% more healing capacity.
- Leave raid members above half health to their own regeneration and the other healers: the lab measured healing them only under 50%, instead of 70%, as 2% more healing capacity, the mana going to the tank.
- Forever gives low ranks less of your healing power (Blizzard's beta notes; the exact rule is not published). The lab assumes TBC's rule: **Healing Touch** ranks 9 to 11 keep their full bonus, rank 8 about 92% and rank 7 about 82%, so downrank only that far.
- The beta's **Swiftmend** tooltip no longer says it uses up the heal over time, as Classic's did, and the lab now leaves it ticking (worth about 3% healing capacity there). If it does use it up at launch, save **Swiftmend** for emergencies and keep a **Rejuvenation** ready to put back.

**When to change it**

- The tank under 55%: **Nature's Swiftness** and **Healing Touch** if it is ready, else **Swiftmend** if your heal over time is on the tank, else **Regrowth**. The lab measured reacting at 55% rather than 35% as 1 to 2.5% more healing capacity.
- A whole party hurt at once: **Wild Growth** on one of them; if the damage keeps coming and they stand together, **Tranquility** (5-minute cooldown, a 10-second channel on your party within 20 yards).
- A tank or healer dies: **Rebirth** (30-minute cooldown) brings them back during the fight.
- Curses and poisons: **Remove Curse** and **Abolish Poison** are yours to cast. The lab does not model them, so dispel when the debuff would cost more health than your next heal restores.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

Healing capacity 0.60 (the raid damage it heals through in this project's healer lab), 350 healing per second. Healers are not in the community simulator.

## Other builds of this spec

- [Restoration — Raid Healer](../research/raid/builds/resto-raid-healer.md) (11/5/35) — [open the talent tree](https://talentsforever.com/druid/60/05302001-05-5050035153113021-6)
- [Restoration — Regrowth / Nature's Grace, with a Balance dip](../research/raid/builds/resto-regrowth-natures-grace.md) (21/0/30) — [open the talent tree](https://talentsforever.com/druid/60/1532223110001--505003510311105-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

