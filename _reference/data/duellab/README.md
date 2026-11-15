# Duel lab

Level-60 one-against-one PvP duels between talent builds (2026-11-14, user: "do full research on WoW Forever PvP builds and build
whatever is necessary"). No community simulator plays PvP, so this is the project's own model, built on the fight lab
(`../fightlab/`). Results are a model of stated assumptions, never measurements of the game. The facts it rests on, with sources:
`_reference/pvp-research.md`; the work plan: `_reference/pvp-plan.md`.

## How it works

- `duel.py`: the engine.
  - `Side`: one combatant, holding:
    - its fight-lab class module (`FR.make_module(cls, talents, 60, spec)`: spells at their level-60 ranks, talent numbers and
      mechanics);
    - its `Player` (`mod.make_player(60)`, gear tier `dtables.GEAR_TIER`);
    - its PvP state: control timers, diminishing returns, lockouts, immunities, stealth, debuffs, dots.
  - `SideFight`: a fight-lab `Fight` per side whose target is the other player seen through `Body`, a mob-shaped view. Every class
    module hook (on_hit, on_chill, crit bonuses, procs, pets) runs unchanged; damage, healing, the attack table and control are
    overridden for player targets.
  - `Duel`: one distance on a line, a 0.05 s step, both sides' regeneration, dots and heals over time, movement, auto attacks,
    casts and decisions; `run()` returns "A", "B" or "draw".
- `dtables.py`: every constant, each with its reason: diminishing-returns categories, the PvP cap, what breaks control, each class's
  trinket, reaction time, start distance, gear tier.
- `pvp_base.py`: `PvPAI`, the decision layer every class extends. Its fallback `rotation()` is the spec's own tuned leveling
  rotation (the fight lab's `mod.decide(fight)`) with the opponent as the mob. The PvP layer adds only what PvP needs: openers,
  control, interrupts, defensive cooldowns, kiting and the trinket. Each spec plays its own rotation (user rule, 2026-10-08).
- `pvp_<class>.py`: one class's layer. `duel_run.py` maps classes to them (`AI`).
- `duel_run.py`: runs duels, matchups and logs. A side is `<class>:<build id>` from
  `<class>/research/talents/forever/proposed-builds.json`. Its fight-lab rotation comes from the build's lead tree
  (`derive_leveling.LEVEL`).
- `pvp_field.py`: the field (the community's most-tagged build per class), the matchup matrix (`--matrix --write` writes
  `_reference/pvp-matchups.md`) and a build's score against the field (`--score`).
- `duel_profile.py`: the validation tool. Per side of a matchup it gives damage, healing and casts per duel, where the time goes
  (idle with the global cooldown free, split by state) and the waste read from the logs: control into an immunity, damage into an
  immunity, and a side's own control broken by its own damage. Run it on the matrix's most lopsided matchups after any layer change,
  then read a log of the worst (`duel_run.py --log 1`).

## Writing a class layer (`pvp_<class>.py`)

Subclass `PvPAI` and override what the class needs.

Settings:
- `keep_range`: 0 for melee, which closes in; else the distance held.
- `auto_attack`: whether the class swings in melee.
- `charges`: spell names that close the gap like Charge, usable from 8 to 25 yards.
- `ranges`: spell name to reach, where the data's range is wrong.

Hooks:
- `effects_for(me)`: `{spell name: handler(d, me, foe, spell)}` for every PvP effect the fight lab does not parse. Fear, Polymorph,
  Blind, Sap, Seduction, Psychic Scream, Kidney Shot's combo-point stun, Ice Block, Divine Shield, Blessing of Protection, Evasion,
  Sprint, Vanish and traps are all effects. A handler replaces the spell's whole resolution, so it must apply damage itself if the
  spell deals any (`me.fight.deal(spell, amount)`, or `FE.Fight.resolve_spell(me.fight, spell)` for the normal damage roll).
- `prefight(d, me, foe)`: stealth (`me.stealthed = True`), a shield or a pet before the duel.
- `intent(d, me, foe)` returns "close", "kite" or "hold"; `close_to(d, me)` is where closing stops.
- `while_controlled(d, me, foe)`: the trinket (the base handles the class's trinket rules), or Blink and the like.
- `off_gcd(d, me, foe)`: interrupts and cooldowns that cost no global cooldown.
- `decide(d, me, foe)`: the next action. End with `return self.rotation(d, me, foe)`.
- `damage_taken(d, me, src, spell, amount)`: change incoming damage (Mana Shield, a Voidwalker's sacrifice).
- `while_inactive(d, me, foe)`: inside a self-imposed pause (`me.inactive_until`, as in Ice Block). Return None and set
  `me.inactive_until = d.t` to leave it.

Primitives on a `Side`:
- **Control:**
  - `apply_cc(kind, seconds, dr_category, name, frozen=False, breaks=None, physical=False)`. `kind` is one of "stun", "root",
    "fear", "incap", "silence" or "disarm". It applies immunity, the PvP cap and diminishing returns, and returns the seconds
    applied.
  - Damage breaks an incap named in `dtables.BREAKS_ON_DAMAGE`.
  - Set `physical=True` for weapon abilities, which Blessing of Protection stops.
- **Immunities and timers:** `immune_until` (everything), `immune_phys_until` (Blessing of Protection), `fear_immune_until`,
  `inactive_until`.
- **Defensive buffs:** `dodge_buffs[name] = (chance, until)` for Evasion or Deterrence; `speed_bonus[name] = (fraction, until)` for
  Sprint, Dash or Ghost Wolf; `slow` and `slow_until` for slows on that side.
- **Shields, dispels and heals:**
  - `p.absorb` and `p.absorb_until`: an absorb shield.
  - `dispel_cc(...)`: a cleanse on yourself; `purge_shields()`: an offensive dispel on the target.
  - `cc_regen = (until, share per second)`: a polymorphed target's regeneration.
- **Casting state:** `interrupt(lock_seconds, by)` locks the school being cast; `break_cast(why)`; `use_trinket()`;
  `trinket_frees()`.
- **Queries:** `stealthed`, `behind(t)`, `controlled(t)`, `silenced(t)`, `school_locked(school, t)`, `is_casting()`,
  `cast_spell()`, `hp_frac()`, `mana_frac()`.
- **Actions:**
  - `can(name, ignore_gcd=False)`: known, ready, affordable, in range, not locked, not disarmed, the target visible.
  - `cast(name)`: what the engine does when you return the name.
- **Debuffs:** `debuffs[name] = {"until", "stacks"}`, as with Mortal Strike's and Wound Poison's healing reduction
  (`dtables.HEAL_REDUCTION`, applied automatically on damage).
- **Duel (`d`):**
  - `d.t`, `d.dist`, `d.set_dist(v)` (for a blink or a charge), `d.combat` (False until the first hostile hit).
  - `d.damage(src, dst, spell, amount, crit)` routes damage through immunities, absorbs and control breaks.
  - The opponent's module and state are on `foe` (`foe.mod`, `foe.p`, `foe.cls`).

Rules:
- Only `pvp_<class>.py` is yours.
  - Do not edit `duel.py`, `pvp_base.py`, `dtables.py`, `duel_run.py` or the fight lab.
  - If the engine lacks something, work around it in your file (override a hook, keep state on the AI instance), and list the engine
    change you would want in your report.
- The damage play is the rotation's. Add PvP decisions on top; do not rewrite the class's damage priority.
- The module docstring says what is modelled, what is not, and every assumption, with sources where they exist.
- No consumables and no racials (dtables). A warlock's Healthstone is the one class-made exception, if you add it.
- A talent that changes a PvP tool must only work when the build has it: check `me.mod.rank("Talent Name")` or `me.mod.tv(...)`.
  Examples are Improved Kick's silence, Improved Gouge, Improved Psychic Scream, Improved Hammer of Justice, Entrapment, Clever
  Traps, Improved Fear and Nature's Swiftness.

Testing:

    python _reference/data/duellab/duel_run.py <class>:<build> mage:pvp-frost --n 200 --log 2
    python _reference/data/duellab/duel_run.py <class>:<build> warrior:arms-pvp --n 200

Read the logs:
- Does every effect fire?
- Are control effects diminished and broken as they should be?
- Is the trinket used sensibly?
- Is nothing cast out of range or while controlled?
- Do duels end (no draws from a stuck AI)?
