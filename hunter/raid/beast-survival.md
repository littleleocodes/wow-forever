# Beast-Survival Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Survival

*Dual-wield melee with no pet out: Summon Hawk and Lone Wolf from the other trees (16/11/24), about 9% more damage than Melee Survival in a full raid (802 against 737 DPS, 2026-11-19; the hybrid check, kept by open_builds.raid_kept).* (a hybrid: Beast Mastery/Survival).

**[Beast-Survival — Raid](../research/raid/builds/beast-survival-open-raid.md)** (16/11/24) — [open the talent tree](https://talentsforever.com/hunter/60/55000005001-005005001-5302002300500121-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Setup, before the pull:** **Dismiss Pet**: **Lone Wolf** only works while you have no pet out.

**Before the pull:** **Hunter's Mark**.

**Keep up all fight:** **Aspect of the Beast**.

**Then press the first one that is ready**, top to bottom:

1. **Explosive Trap** when you have at least 60% mana, until the last 20 seconds of the fight
2. **Raptor Strike**; no global cooldown, so press it alongside the others
3. **Mongoose Bite** after you dodge
4. **Strider Kick**
5. **Summon Hawk**
6. **Immolation Trap**
7. **Wing Clip**

**Wing Clip** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Rapid Fire**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Survival plays the melee Survival list with **Summon Hawk** added: no pet, so **Lone Wolf**'s 20% stays on, and up to two hawks attack the boss beside you.

**Why it works**

- **Raptor Strike** first whenever it is ready: it replaces your next main-hand swing and costs no global cooldown. Then **Mongoose Bite** when it lights up and **Strider Kick** on its 8-second cooldown.
- **Summon Hawk** next, about 27 times in a 3-minute fight: a dive bomb plus 5% of your ranged attack power, then a hawk that attacks for 18 seconds. Two can be out at once and a new one replaces the one closest to leaving; **Unleashed Fury** makes them hit 15% harder. The simulator measured about 15% more damage in a full raid once the hawk joined the melee rotation, and it counts hawks as guardians, not pets, so **Lone Wolf** stays on while they fly.
- **Hunter's Mark** before the pull is for **Expose Prey**: each hit on a marked target has a 10% chance to light up **Mongoose Bite** for 10 seconds, and in a raid you rarely dodge, the bite's only other trigger. Recast the mark when its 2 minutes run out.
- The fire-trap cooldown goes under the boss every 18 seconds (two points in **Survivalist's Discipline**), 30% stronger with **Clever Traps**: **Explosive Trap** while you have 60% mana or more and 20 seconds left (the melee list's 2026-11-10 change), else **Immolation Trap**. With no **Resourcefulness** here, expect more **Immolation Trap** than the Survival build. **Wing Clip** fills the global cooldowns left over, for its small hit and another chance at **Mongoose Bite**.

**Caveats**

- Mana: this build has no **Resourcefulness**, and each hawk costs 190 mana. In a full raid the simulator needs one mana potion a fight; with only your own buffs it ran out of mana and fell about a quarter behind the Survival builds on the training dummy. Without Blessing of Wisdom or Mana Spring, play Survival.
- The build rests on the simulator's reading that a hawk is not a pet: if the game counts hawks as pets, **Lone Wolf** turns off while they are out. Check it at launch.
- No pet: **Dismiss Pet** before the pull. Track the boss's creature type: **Improved Tracking** adds 5% only against the tracked type.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98) and **Aspect of the Beast** rank 4 +110 melee attack power (rank 3 +90). Cast the highest rank you have.

**When to change it**

- Adds around you: **Explosive Trap** even below 60% mana; it shares the fire-trap cooldown with **Immolation Trap**.
- Pulled off the boss by a mechanic: **Summon Hawk** reaches 35 yards, so keep the hawks coming, and make **Strider Kick** your last hit before you run (30% movement speed for 3 seconds).
- Short on mana: let **Wing Clip** go first; its own hit is your least damage per point of mana.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 16 | Deadly Aspects 5, Endurance Training 5, Unleashed Fury 5, Summon Hawk 1 |
| Marksmanship | 11 | Lethal Attacks 5, Careful Aim 5, Lone Wolf 1 |
| Survival | 24 | Improved Tracking 5, Deflection 3, Savage Strikes 2, Clever Traps 2, Surefooted 3, Predator's Edge 5, Expose Prey 1, Survivalist's Discipline 2, Strider Kick 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 802 |

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

