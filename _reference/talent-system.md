# The talent system — Classic rules and what Forever changes

## Classic Era rules (the baseline the validator enforces)

- Talent points: 1 per level from level 10, so **51 at level 60**.
- Three trees per class, **7 tiers** each. Tier *n* unlocks once you have **5 × (n − 1)** points in that tree
  (tier 2 at 5, tier 3 at 10, … tier 7 at 30). Points in other trees never count.
- Some talents also require a specific other talent at max rank (drawn as an arrow in the calculator).
- Ranks: 1–5 points per talent. The tier-7 talent is always a 1-point "capstone" (31 points minimum).
- A "31/20/0" style split lists points per tree in in-game left-to-right order:

| Class | Tree 1 | Tree 2 | Tree 3 |
|---|---|---|---|
| Druid | Balance | Feral Combat | Restoration |
| Hunter | Beast Mastery | Marksmanship | Survival |
| Mage | Arcane | Fire | Frost |
| Paladin | Holy | Protection | Retribution |
| Priest | Discipline | Holy | Shadow |
| Rogue | Assassination | Combat | Subtlety |
| Shaman | Elemental | Enhancement | Restoration |
| Warlock | Affliction | Demonology | Destruction |
| Warrior | Arms | Fury | Protection |

- Respeccing costs gold (1g the first time, +5g per respec up to 50g in Classic). Leveling builds in this
  project are therefore chosen to end in a usable 60 build where possible.

## What Forever changes (beta client build 1.60.1.70291, 2026-10-08)

- **Same skeleton**: 3 trees, 7 tiers, 51 points, 5-per-tier gating (assumed — fan calculators and the demo
  behave this way; not yet confirmed by Blizzard).
- **A fourth 1-point talent per tree at the 16-point mark** (tier 4), in addition to the Classic 11/21/31
  gold-medal talents — e.g. Warrior Arms *Spearing Strike*, Fury *Raging Blows*, Protection *Vanguard*.
- **466 talents in build 70291: 140 new** (mostly later-expansion abilities: Mutilate, Lava Burst, Penance, Heating Up (Hot Streak
  until 70170), Lone Wolf, Soul Link-style hybrids) and **105 Classic talents removed** — notably the weapon specializations
  (Warrior, Rogue, Shaman), Tactical Mastery, Aimed Shot/Lethal Shots as talents, Improved Backstab,
  Blessing of Kings (now baseline), Consecration (now baseline), Omen of Clarity (now baseline).
- **244 talents changed** (reworded or retuned), **28 moved** to a different position and 54 the same as Classic (the `status` field of
  `_reference/data/forever-talents/<class>.json`; counts of 2026-10-15). The per-class `research/talents/forever/talent-trees.md`
  shows every talent with its Classic tooltip next to the Forever one; what each beta build changed: `forever-talents/README.md`.
- Tooltip numbers in the data are the **beta client's level-60 values with no gear** (the demo's level-38 numbers are gone).
- The beta client stores the trees in retail-style Trait tables (TraitTree/TraitNode/TraitEdge), one tree per class; the talent panel has **Primary** and **Secondary** tabs (not yet explained; likely dual spec). No talent has four ranks any more (ranks are 1, 2, 3 or 5).
- Respecs in the beta cost 1 silver if you have not changed talents recently (temporary, beta only); after a reset the next one is much dearer but drops back to 1 silver after an hour (dev notes 2026-09-24).

## How this affects "optimal talents"

1. Any Classic build whose points sit in removed talents has **orphaned points** — see each class's
   `research/talents/forever/baseline-audit.md` for the exact count.
2. Tier requirements shift when talents move; a Classic build can become illegal in Forever even if every
   talent still exists. The validator re-checks proposed Forever builds against the Forever trees.
3. New capstones and 16-point talents can change *which tree* a spec wants to go deep in
   (e.g. Hunter Marksmanship without a pet via Lone Wolf, Shaman Elemental with Lava Burst).
4. Baseline-ification (Kings, Consecration, Omen of Clarity) frees points that used to be mandatory.
