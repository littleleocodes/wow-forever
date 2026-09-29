# Community simulator gaps audit (2026-09-29)

Hand-written (user question: "are there other small patches we're missing, like the melee hunter's aspects?"). Simulator: the
ElliotWood/Forever fork at 40be98e. Three checks, all nine classes:

1. **Talents the simulator never reads** (its Go code never references the talent field): Booming Voice (shout radius), the rogue
   utility talents (Endurance, Improved Sprint, Improved Kick, Camouflage, Master of Deception, Setup, Dirty Tricks, ...) and a few
   paladin utility talents. None changes single-target damage: zero is right.
2. **Talents stubbed "To be implemented"** in the simulator's comments: mage Wand Specialization, Improved Channeling, Arcane Geometry,
   Arcane Shielding, Improved Counterspell, Flame Throwing, Impact, Improved Fire Ward, Frost Warding, Permafrost, Frostbite, Arctic
   Reach, Ice Block, Ice Barrier; shaman Earthbound, Earth's Grasp, Guardian Totems, Improved Ghost Wolf, Water Shield; druid Improved
   Entangling Roots, Overgrowth; priest healing and utility talents. By their beta tooltips all are range, crowd control, wand,
   pushback, healing or defence: nothing a boss-damage race can see. Hunter pet abilities new in Forever (Savage Rend, Dismember,
   Pinch, Tendon Rip, Swipe, Mine!, Dust Cloud, Enchanted Flare) are unimplemented; only Dust Cloud (-505 armor, tallstrider) could
   move a pet build's damage.
3. **Implemented abilities no rotation casts** (ours or the simulator's; the rotation search only offered new Forever spells and
   cooldowns), each inserted at every position of the dummy rotation, best position confirmed on an independent seed:

| Class | Ability | Result |
|---|---|---|
| Hunter | Arcane Shot | **+4.8% dummy / +16.8% raid** (bm-mm builds), **+1.8% / +16.5%** (Lone Wolf); 0 in the Summon Hawk builds (shared timer). Added to the mm-raid and mm-lonewolf-raid rotations. |
| Hunter | Immolation / Explosive Trap (melee) | +7.7% dummy / +3.8% raid; added to melee-dps (see HANDOFF). |
| Warrior | Overpower, Rend | Never castable: the rotations stay in Berserker Stance (both need Battle Stance). A stance-dancing Arms rotation is the open "Arms APL" item. |
| Warrior | Slam | Loses 0.5-5%: correctly skipped. |
| Druid | Rake | 0 (Shred is the better use of energy). |
| Priest | Starshards | Never castable: a Night Elf racial and our priests are Trolls (a race question, not a patch). |
| Warlock | Soul Fire | Loses at every position (6 s cast). |

**Patch candidates** (simulator code, `raidsim/patches/`): Aspect of the Beast (+110 melee attack power) and the melee half of Deadly
Aspects (10% per melee swing, +30% melee speed for 12 s): the simulator models only Aspect of the Hawk and the ranged half, so the melee
hunter has no aspect and Deadly Aspects measures zero. Warlock Bane of Doom is not implemented at all. Hunter Dust Cloud (above).

**Root cause to fix**: `raidsim/apl_opt.py`'s insertion pool (`new_spell_pool`) holds only spells the spellbook marks new; old abilities
that no rotation casts (Arcane Shot, traps) were never tried. Extending the pool to every implemented damaging ability the entry's
rotations do not cast would have found both.
