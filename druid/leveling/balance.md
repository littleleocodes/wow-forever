# Balance Druid — Leveling (solo)

[Druid](../README.md) > [Leveling (solo)](README.md) > Balance

**[Balance — Leveling](../research/leveling/builds/balance-open-leveling.md)** (38/0/13) — [open the talent tree](https://talentsforever.com/druid/60/5432200115501351--505003-6)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

## How to play

**Before the fight:** **Moonkin Form** once you have it.

**In the fight**, top to bottom:

1. **Moonfire** on a mob above a third of its health, **Insect Swarm** above 40%.
2. **Wrath** while the mob walks in and whenever nothing below applies: each one stores **Eclipse** charges.
3. **Starfire** while **Eclipse** has charges, or while the mob is rooted or stunned.
4. A nearly dead mob: finish it with **Moonfire** or **Wrath**.
5. Low on health: **Entangling Roots** on the mob, step out of melee, then **Regrowth** (it drops **Moonkin Form**; go back in while the mob still has half its health).

**Between fights:** Stay in **Moonkin Form** and eat when your health is below 80%. Drink when your mana is below 45%.

## Why this rotation

Pull with instants, then cast: **Moonfire** and **Insect Swarm** on the mob, **Wrath** while it runs in, then **Starfire** whenever **Eclipse** has shortened it or the mob cannot hit you, **Wrath** otherwise. Finish with an instant, and heal from range when you must.

**Why it works**

- **Moonfire** and **Insect Swarm** first: both are instant, so they tick while the mob is still running at you, and **Genesis** adds up to 5% to their ticks. The fight lab puts **Moonfire** only on a mob above 35% health and **Insect Swarm** above 40%: a mob below that dies before they pay off.
- **Wrath** is the default nuke: with **Improved Wrath** it is a 1.5-second cast for half the mana, and a short cast loses little to pushback once the mob is hitting you. Each **Wrath** also stores 2 **Eclipse** charges for the **Starfire** casts after it. Before **Eclipse** at 30 the fight lab casts almost nothing else, about 10 Wraths a kill at 20.
- **Starfire** hits about three times as hard at 60 but takes 3 seconds even with **Improved Starfire**, so it waits for a faster or a safe moment: when **Eclipse** has charges (each charge shortens one **Starfire**), or when the mob is rooted or stunned (**Improved Starfire** stuns for 3 seconds 15% of the time). From 41, **Nature's Focus** also lets you ignore some of the pushback.
- Low on health: **Entangling Roots** holds the mob in place but it still hits you if you stand next to it, so step away, then cast **Regrowth** from range. A direct hit can break the roots.

**Caveats**

- **Eclipse** at the 1 point this build takes saves 0.17 seconds a charge (0.5 at 3 points), so the weave is a small gain: the fight lab measured the full 0.5 seconds it used to give every rank as 2-3% faster per kill than the real 1-point value.
- **Moonkin Form** (40) blocks healing spells: to cast **Regrowth** you must leave it, and going back costs 35% of your base mana. So stay in the form between fights and eat; leave it only for an emergency heal, and go back in while the mob still has half its health (the fight lab plays it that way).
- Mana: **Moonglow** cuts your damage spells' cost by 25% and **Reflection** keeps half your regeneration going while you cast. The tuned fight lab drinks below 45% mana and eats below 80% health: topping up early measured 1.7% faster per kill, with fewer deaths at 40-50.

**When to change it**

- When the mob is nearly dead, finish it with an instant **Moonfire** or a quick **Wrath** rather than a **Starfire** it will not live through: the fight lab does exactly that.

*This guide was written for the rotation of 2026-10-09; the list above was re-tuned since, so follow the list where the two differ.*

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Improved Wrath (Balance) | 5 |
| 15-17 | Moonglow (Balance) | 3 |
| 18 | Improved Moonfire (Balance) | 1 |
| 19-20 | Nature's Majesty (Balance) | 2 |
| 21 | Nature's Splendor (Balance) | 1 |
| 22 | Improved Moonfire (Balance) | 1 |
| 23-24 | Genesis (Balance) | 2 |
| 25 | Insect Swarm (Balance) | 1 |
| 26-29 | Improved Starfire (Balance) | 4 |
| 30-32 | Eclipse (Balance) | 3 |
| 33 | Nature's Grace (Balance) | 1 |
| 34 | Improved Starfire (Balance) | 1 |
| 35-39 | Moonfury (Balance) | 5 |
| 40 | Moonkin Form (Balance) | 1 |
| 41-45 | Vengeance (Balance) | 5 |
| 46-50 | Nature's Focus (Restoration) | 5 |
| 51-55 | Naturalist (Restoration) | 5 |
| 56-58 | Reflection (Restoration) | 3 |
| 59-60 | Genesis (Balance) | 2 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 44 |
| 30 | 52 |
| 40 | 52 |
| 50 | 45 |
| 60 | 42 |

## Other builds of this spec

- [Balance (optimized)](../research/leveling/builds/opt-balance-dps-leveling-st.md) (36/2/13, 53 s per kill (level-weighted)) — [open the talent tree](https://talentsforever.com/druid/60/5032203105501351-02-505003-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

