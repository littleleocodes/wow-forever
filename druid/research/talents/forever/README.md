# Druid — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Omen of Clarity (Balance T3) | **Removed — baseline**, and now also procs from spells | The Feral Balance dip (14 points) loses its main reason |
| Natural Weapons (Balance T2) | **Removed** | Feral loses +10% physical damage; Naturalist (Resto T2, +5% all damage) is the nearest replacement |
| Nature's Grasp / Improved Nature's Grasp | **Removed** — presumably baseline | Tier-1 Balance filler gone; Genesis / Improved Wrath remain |
| Improved Thorns | **Removed** | |
| Improved Healing Touch (Resto T2) | **Removed** → *Naturalist* (5: -0.1s/rank HT and +1%/rank damage) | Same cast-time job, and a Feral damage talent |
| Improved Mark of the Wild, Improved Enrage | **Removed** | 5 healer points freed |
| Heart of the Wild | Feral T6 → **tier 1** (Intellect, bear Stamina, cat Strength) | Feral's best talent is now the first one |
| Improved Shred, Blood Frenzy, Feline Swiftness, Feral Aggression, Faerie Fire (Feral) | **Removed** → Shredding Attacks, Feral Swiftness, Predatory Instincts; Faerie Fire (Feral) baseline | Cat build rebuilt |
| Insect Swarm | Resto T3 → **Balance T4**, no longer the Gift of Nature prerequisite | |
| Swiftmend | Capstone → **16-point talent**; no longer consumes the HoT (reveal) | Every healer takes it |
| Nature's Swiftness | Requires **Naturalist 5** | |
| Improved Regrowth | Requires **Improved Rejuvenation 3** | |
| Nature's Grace | Instant -0.5s → +10% cast speed for 3s | Weaker; the Classic Regrowth build loses its engine |
| Sharpened Claws | 3 ranks → 2 ranks (3%/rank) | Cheaper |
| Moonfury | 2%/rank in the beta client (the demo transcription read 1%) | Same as Classic |

## What's new and matters

- **Nature's Majesty** (crit with spells *and* melee) and **Nature's Reach** (hit with all spells and attacks) in Balance tier 2 — every spec wants them.
- **Genesis** (periodic damage/healing), **Nature's Splendor**, **Eclipse**, **Overgrowth** (Balance); Balance of Nature was cut in beta build 69893.
- **Primal Bite** (bear-only 16-pt; named Mangle until build 70009, its debuff is gone), **Shredding Attacks**, **Predatory Instincts**, **King of the Jungle**, **Natural Reaction**, **Rend and Tear**, **Berserk** (Feral).
- **Naturalist**, **Gift of the Earthmother**, **Living Spirit**, **Wild Growth** (Restoration).
- Furor reworked: cat keeps 20%/rank of its Energy on shift (100% at 5/5) plus 2/rank Energy per second out of form; powershifting loses nothing at 5/5.

## Decisions made in the proposed builds

1. **Resto 11/0/40**: deep Restoration for Wild Growth + Swiftmend with the four good Balance healer talents.
2. **Regrowth/Nature's Grace 21/0/30** kept as the comparison build; expected to lose.
3. **Feral cat and bear 9/32/10**: Balance dip = Genesis/Majesty/Reach; Restoration dip = Furor + Naturalist.
4. **Moonkin 46/0/5**: deep Balance with Eclipse (Balance of Nature's 5 points went to Improved Entangling Roots / Overgrowth after the cut; the optimizer prefers 36/2/13).
5. **PvP Resto 14/0/37**.

## To verify at launch

- Furor's cat energy retention and Wolfshead Helm interaction.
- Cats get no Mangle: the beta spellbook has Primal Bite (bear) ranks at 25/40/50/60 only; Berserk's 3-target strike is the bear's.
- Swiftmend not consuming HoTs; Wild Growth numbers and target cap.
- Eclipse charge mechanics (Moonfury is 2%/rank, confirmed).
