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

## Overnight audit (2026-09-29, second pass, all classes)

**Data**: talentsforever.com's data.json (2026-09-26) matches our talent data exactly (client build 70009; check_beta_build.py: no newer
build). The site also carries the account-wide **Legacy** perks (16 points at launch; Talented gives talent points from level 5, Thrill of
Adventure heals 5% on a kill, Field Medicine shortens the bandage debuff, Gourmand doubles food buffs): none changes raid damage, several
change leveling; the guides assume none (they are earned).

**Rotation search**: `apl_opt.py`'s insertion pool now holds every combat spell of the class spellbook (not only new Forever spells),
each also guarded by "only while its dot is not ticking" (spells "over N sec") and "only while its aura is not on the target / on you"
(spells lasting "for N sec/min": a plain Curse of the Elements took a warlock to 0 DPS), plus an insertion spot after everything (the traps
won there). `--insert-only` sweeps just those insertions; every raid entry was swept (results: the rotation-search records, pass
"2026-09-29").

**Simulator patch**: Aspect of the Beast and the melee half of Deadly Aspects (`raidsim/patches/`): melee hunter +12.3% dummy, +12.9% raid.

**Warrior stance**: the warrior rotations never leave Berserker Stance, so Overpower and Rend (Battle Stance) were never cast. A Battle
Stance Arms rotation (Overpower, Rend when not ticking, Slam) lifts the simulator's Arms 39/12/0 preset from 167 to 198 dummy DPS and 377
to 454 raid; our Berserker builds stay ahead on the dummy (Arms 216, Fury 257). New entry `arms-battle-raid` (rotation-only) with its own
talent search.

**Fight lab (leveling)**, spells no leveling rotation used, checked one by one:

| Class | Spell | Result |
|---|---|---|
| Hunter (melee) | Immolation Trap | Added: the parser read no damage from the trap text (fixed in the hunter module), trap talents now count; cast while the mob is above 70% health: -4.6% to -6.3% time per kill at 40-60. |
| Warlock | Curse of the Elements | Added and measured: +1.7% to +3.3% time per kill at 50-60 (the mob dies before the curse repays its GCD and mana), so the tuned rules keep it off. A Curse sits beside a Bane in Forever; the raid rotations already cast it. |
| Rogue | Ambush | Not added: the leveling rogue plays swords (Ambush needs a dagger) and opens with Cheap Shot / Garrote. |
| Warrior | Slam | Not added: the module's measured reason stands (a 1.5 s cast on an 18 s cooldown in Forever). |
| Others | wards, blessings on others, crowd control, curses of weakness, totems of utility | No damage while leveling. |
