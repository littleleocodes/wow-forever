# Balance Druid — Leveling (solo)

[Druid](../README.md) > [Leveling (solo)](README.md) > Balance

> **Being checked:** The first point of Eclipse makes the pick slower at 30 (the play check: 33.3 seconds a kill at 29, 35.9 at 30), and the rotation is being checked for why. The build and numbers on this page may change when it is done.

**Leveling from level 1?** [The rotation level by level](balance-by-level.md): what to press as each spell and talent arrives. [Your keys and macros](keybinds.md).

**[Balance — Leveling](../research/leveling/builds/balance-open-leveling.md)** (36/0/15) — [open the talent tree](https://talentsforever.com/druid/60/5332200105501351--51531-12)

> 🔬 Derived build: found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling simulator; the winner picked by a race at levels 20-60). A model of the beta, to check at launch.

**Signature spells:** 97% of the damage at level 60 in the fight lab comes from the spec's core spells (Wrath, Starfire, Moonfire; this build never casts Insect Swarm) (the spec's rule: at least 70%; **Starfire**, **Moonfire** cast at level 60).

## How to play

**Before the fight:** **Mark of the Wild** and **Thorns** up; **Moonkin Form** once you have it (40).

**In the fight**, top to bottom:

1. **Moonfire** on a mob above a third of its health.
2. **Wrath** while the mob walks in and whenever nothing below applies: each one stores **Eclipse** charges.
3. **Starfire** while **Eclipse** has charges, or while the mob is rooted or stunned.
4. A nearly dead mob: finish it with **Wrath**.
5. Low on health: **Entangling Roots** on the mob, step out of melee. The tuned rules cast no heal in a fight.

**Between fights:** Eat when your health is below 40%, in **Moonkin Form** from 40 (stay in it). No heals between fights either: the tuned rules of 2026-11-21 eat instead, about 2% faster per kill. Drink when your mana is below a quarter (25%). Whenever you sit down to drink, also eat if your health is not full, and whenever you sit down to eat, also drink if your mana is not full: no extra time (the tuned rules do it). Stand up once the bar you sat down for is full.

## Why this rotation

Pull with an instant, then cast: **Moonfire** on the mob, **Wrath** while it runs in, then **Starfire** whenever **Eclipse** has shortened it or the mob cannot hit you, **Wrath** otherwise, and **Wrath** to finish. Eat between fights below 40% health: the tuned rules cast no heal, in a fight or between fights.

**Why it works**

- **Moonfire** first: it is instant, so it ticks while the mob is still running at you. The fight lab puts it only on a mob above about a third of its health: a mob below that dies before the burn pays off. This build skips Insect Swarm (a Balance tier 4 talent), so **Moonfire** is the only damage over time you cast; **Genesis** (levels 23-24 and 56) makes its burn 4% stronger, 6% from 56.
- **Wrath** is the default nuke and, until level 26, almost the only one: with **Improved Wrath** (levels 10-14) it is a 1.5-second cast for half the mana, and a short cast loses little to pushback once the mob is hitting you.
- **Eclipse** (levels 30-32) is the build's most valuable talent in the fight lab: each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts (0.17 s at 1 point, 0.33 at 2, 0.5 at 3; up to 4 charges, 15 seconds). So the fight lab weaves: **Wrath**, then **Starfire** while charges last, about two **Starfire** casts for each **Wrath**.
- **Starfire** is your hardest hit. It takes 3 seconds with **Improved Starfire** (2.5 on a full **Eclipse** charge), so it waits for a charge or a safe moment: when the mob is rooted or stunned (**Improved Starfire** stuns for 3 seconds 15% of the time). **Nature's Focus** (levels 42-46) lets your casts ignore pushback 70% of the time.
- **Moonglow** (levels 15, 17 and 19: damage spells cost 25% less), **Moonfury** (10% more Arcane and Nature damage at 5 points) and **Moonkin Form** (40) are the next most valuable talents in the fight lab.
- Keep **Thorns** and **Mark of the Wild** up between fights (no key).
- Low on health (below 35%): **Entangling Roots** holds the mob in place but it still hits you if you stand next to it, so step away. A direct hit can break the roots. The tuned rules of 2026-11-20 cast no **Regrowth** in a fight (against mobs of your level it never paid); cast one if a pull goes wrong.

**Caveats**

- **Moonkin Form** blocks healing spells: to cast **Regrowth** you must leave it, and going back costs 35% of your base mana. So stay in the form between fights and eat; leave it only for an emergency heal, which the tuned rules never cast, and go back in once you have half your health.
- Mana: **Moonglow** cuts your damage spells' cost by 25% and **Reflection** (levels 47-49) keeps up to half your regeneration going while you cast. The tuned fight lab drinks below a quarter of your mana (25%, the tuned rules of 2026-11-20) and eats below 40% of your health (the tuned rule of 2026-11-06), and does both together whenever it sits down for one: the other bar fills at no extra time (the tuned rules of 2026-11-17; 7% faster per kill in the fight lab). Druids cannot use a wand, so an empty bar means waiting.
- Before **Moonkin Form** (40) you could heal between fights with **Rejuvenation** and **Regrowth**, but eating while you drink measured faster: the re-tune of 2026-11-21 switched those heals off, 2.1-2.3% faster per kill over the levels.

**When to change it**

- When the mob is nearly dead, finish it with an instant **Moonfire** or a quick **Wrath** rather than a **Starfire** it will not live through: the fight lab does exactly that.

## Talents while leveling

One point per level from 10, in this order:

| Levels | Talent | Points |
|---|---|---|
| 10-14 | Improved Wrath (Balance) | 5 |
| 15 | Moonglow (Balance) | 1 |
| 16 | Improved Moonfire (Balance) | 1 |
| 17 | Moonglow (Balance) | 1 |
| 18 | Improved Moonfire (Balance) | 1 |
| 19 | Moonglow (Balance) | 1 |
| 20-21 | Nature's Majesty (Balance) | 2 |
| 22 | Nature's Splendor (Balance) | 1 |
| 23-24 | Genesis (Balance) | 2 |
| 25-29 | Improved Starfire (Balance) | 5 |
| 30-32 | Eclipse (Balance) | 3 |
| 33 | Nature's Grace (Balance) | 1 |
| 34 | Vengeance (Balance) | 1 |
| 35-38 | Moonfury (Balance) | 4 |
| 39 | Vengeance (Balance) | 1 |
| 40 | Moonkin Form (Balance) | 1 |
| 41 | Moonfury (Balance) | 1 |
| 42-46 | Nature's Focus (Restoration) | 5 |
| 47-49 | Reflection (Restoration) | 3 |
| 50-54 | Naturalist (Restoration) | 5 |
| 55 | Vengeance (Balance) | 1 |
| 56 | Genesis (Balance) | 1 |
| 57-58 | Vengeance (Balance) | 2 |
| 59 | Natural Shapeshifter (Restoration) | 1 |
| 60 | Heart of the Wild (Restoration) | 1 |

## The numbers

| Level | Seconds per kill (same-level mobs, eating and drinking included) |
|---|---|
| 20 | 29 |
| 30 | 34 |
| 40 | 37 |
| 50 | 30 |
| 60 | 28 |

## Other builds of this spec

- [Balance (optimized)](../research/leveling/builds/opt-balance-dps-leveling-st.md) (36/0/15, 32 s per kill, level-weighted) — [open the talent tree](https://talentsforever.com/druid/60/5332200105501351--5253-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-22 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938). Simulations, not in-game measurements. Between fights, your own health and mana regeneration keeps running while you eat and drink, as on Classic's servers; not yet checked against a Forever combat log. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows.*

