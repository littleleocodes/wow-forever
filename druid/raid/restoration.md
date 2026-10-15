# Restoration Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Restoration

**[Restoration — Raid healing](../research/raid/builds/restoration-ml-heal.md)** (11/5/35) — [open the talent tree](https://talentsforever.com/druid/60/05122001-05-232033505310305-6)

> 🔬 Derived build: found by this project's deep search over every legal build of the spec in the healer lab (this project's healing model; healers are not in the community simulator), then raced against the spec's builds; it beat the hand-made build (Restoration — Raid Healer), which stays below as the alternative. A model of the beta, to check at launch.

## How to heal

Keep **Rejuvenation** on the tank and heal it with **Healing Touch** at the rank that covers the health it is missing. **Regrowth** is for raid members who drop under half health, **Swiftmend** is your emergency button, **Tranquility** your group heal, and mana is what runs out first.

**Why it works**

- **Healing Touch** is about half your healing in the healer lab (55%). Start it on the tank when it is missing at least about half of what your top rank heals and the next boss hit is on its way: a 3.5-second cast (3.3 with this build's 2 points in **Naturalist**), and a rank sized to the missing health saves mana over the top rank (840 mana, 10% less with **Tranquil Spirit**).
- **Rejuvenation** is about a third of your healing. Keep it on the tank whenever it is missing more than 5% of its health, always at the top rank: it is instant and costs 360 mana, **Improved Rejuvenation**, **Gift of Nature** and **Genesis** add to it, and **Nature's Splendor** stretches it by 3 seconds.
- **Regrowth** is the fast heal: a 2-second cast with a direct heal and a heal over time (6 seconds longer with **Nature's Splendor**), and **Improved Regrowth** adds 50% to its critical chance. The lab gives a raid member under half health a **Rejuvenation** first and a **Regrowth** if they still need it, and casts **Regrowth** on the tank when it is missing about a full one.
- **Swiftmend** heals at once for the full amount of your **Rejuvenation** or **Regrowth** on the target, every 15 seconds: the lab presses it when anyone falls under 35% health, then **Regrowth** if it is on cooldown. It only works on a target with your heal over time, one more reason to keep **Rejuvenation** on the tank.
- This build has no **Wild Growth** and no **Nature's Swiftness**: when three or more raid members are under half health, the lab channels **Tranquility** (5-minute cooldown), about 5% of your healing.
- **Reflection** (half your mana regeneration keeps going while you cast) is the talent the lab values most by far, and **Living Spirit** (+15% Spirit) and **Tranquil Spirit** are mana talents too: this build is shaped by mana, not cast time.

**Caveats**

- Mana runs out before cast time does: in the lab's five-minute fight this build spends about 32 seconds out of mana. The lab drinks a mana potion as soon as you are 20% down, from the start of the fight, and casts **Innervate** on itself under 40% mana.
- Leave raid members above half health to their own regeneration and the other healers: the lab heals them only under 50%, the mana going to the tank.
- Forever gives low ranks less of your healing power (Blizzard's beta notes; the exact rule is not published). The lab assumes TBC's rule: **Healing Touch** ranks 9 to 11 keep their full bonus, rank 8 about 92% and rank 7 about 82%, so downrank only that far.
- The beta's **Swiftmend** tooltip no longer says it uses up the heal over time, as Classic's did, and the lab leaves it ticking. If it does use it up at launch, save **Swiftmend** for emergencies and keep a **Rejuvenation** ready to put back.

**When to change it**

- A whole party hurt at once and standing together: **Tranquility** (a 10-second channel on your party within 20 yards).
- A tank or healer dies: **Rebirth** (30-minute cooldown) brings them back during the fight.
- Curses and poisons: **Remove Curse** and **Abolish Poison** are yours to cast. The lab does not model them, so dispel when the debuff would cost more health than your next heal restores.
- If your raid's damage comes in bursts on whole parties, the hand-made build under Other builds takes **Wild Growth** and **Nature's Swiftness**; in the lab's steady damage this build heals slightly more (capacity 0.60 against 0.59).

## The numbers

Healing capacity 0.60 (the raid damage it heals through in this project's healer lab), 350 healing per second. Healers are not in the community simulator.

## Other builds of this spec

- [Restoration — Raid Healer](../research/raid/builds/resto-raid-healer.md) (11/5/35) — [open the talent tree](https://talentsforever.com/druid/60/05302001-05-5050035153113021-6)
- [Restoration — Regrowth / Nature's Grace, with a Balance dip](../research/raid/builds/resto-regrowth-natures-grace.md) (21/0/30) — [open the talent tree](https://talentsforever.com/druid/60/1532223110001--505003510311105-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

