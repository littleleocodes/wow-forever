# PvP builds: work plan

Hand-kept. Started 2026-11-14 (user: "I think we start working on the PvP builds like when we originally started this project. Do
full research and come up with a game plan", then "make it happen, do full research on WoW Forever PvP builds and build whatever is
necessary").
- Research: `_reference/pvp-research.md`.
- The duel lab: `_reference/data/duellab/README.md`.

## Where PvP stood (2026-11-14)

- **Builds:** 34 PvP builds, research pages only (`<class>/research/pvp/`) since the user's 2026-10-04 decision ("raid and
  leveling only"). Ten are hand drafts from 2026-09; 24 are derived by `derive_pvp.py` (the stats model's `pvp` profile plus
  talentsforever pick rates).
- **The model guesses; nothing measures.**
  - The PvP profile's weights (burst 0.4, survival 0.5, mana 0.05, utility 1.5) were tuned so its optimizer lands near Classic's
    community PvP builds: 67% overlap on average, 31% for the Seal Fate rogue (`_reference/pvp-check.md`, last run 2026-10-15,
    before three talent updates).
  - About half of each class's talents have explicit PvP values. Some name talents that no longer exist; new ones (Bloom, Genesis,
    Boot Knife, Death Mark, Bane of Havoc, Bloodthrill) have none.

## The plan

1. **Research** (done 2026-11-14). `pvp-research.md`, and the community's builds as exact allocations in
   `_reference/data/pvp-community-builds.json`.
2. **The duel lab** (in progress), the measurement PvP lacked: level-60 one-against-one duels on the fight lab's class modules. Each
   spec plays its own tuned rotation, under a PvP layer per class (`pvp_<class>.py`), with Forever's PvP rules (`dtables.py`).
   - Done: the engine, the mage and warrior layers, the field and the matchup matrix (`pvp_field.py`).
   - In progress: the other seven classes' layers.
   - Then: validation. Logs per matchup; the matrix against what the community reports (warlocks strong, as in the level-30 Forever
     Open; mages favoured over warriors in the open); mirror matchups near 50%.
3. **Measure the builds.**
   - The field is the community's most-tagged PvP build per class.
   - A build's score is its mean win rate over the nine classes, with the mean health margin as the tie-break.
   - Talent values by removal against the field (`pvp_values.py`).
   - Races of our 34 builds, the community's builds and the stats model's.
4. **Search for the best PvP build per spec** (`pvp_search.py`):
   - Local search over legal builds from our builds and the community's: 1, 2, 3 and 5-point moves and prerequisite chains, common
     random numbers, kept on a second seed, 30+ points in the spec's tree.
   - Where the field cannot tell talents apart (unmodelled effects), the stats model's PvP value, then the community's pick rate.
   - A winner replaces a build only at the replacement bar (0.5%, measured on the field score).
5. **The stats model's PvP profile, calibrated on the duel lab** (as the fight-lab calibration fits leveling), and the PvP values
   brought up to the current trees. It stays the fast screen.
6. **Pages:**
   - PvP player pages again (`<class>/pvp/`, a PvP column in "Pick your spec").
   - Per spec: the build, its talentsforever link, how to play it (opener, control chains, cooldowns, the trinket), the matchups
     from the matrix, PvP keybinds and macros in the user's scheme.
   - The research pages and the matchup matrix.
   - **User decision:** the 2026-10-04 decision removed the PvP player pages, and the user's new request brings PvP back. To
     confirm when the pages are ready.
7. **Battlegrounds** (after duels):
   - Warsong Gulch flag carrier: survival against two or three attackers with a healer.
   - Healer under focus.
   - Burst against a clump (Darkspear Islands, Arathi Basin nodes).
   - Group scenarios on the same engine.

## Assumptions to revisit

- Open field, no line of sight: kiting classes are favoured. Pillars would move casters against melee.
- No consumables and no racials. Engineering items and Will of the Forsaken matter in real duels.
- Dungeon-blue gear for both sides. A PvP rank set from the simulator's item database is the next gear step.
- Pets cannot be attacked or controlled.
- Warrior stances are not modelled (every ability is usable).
- The AI plays well but not perfectly. A matchup's number is the model's AI against the model's AI.

## Log

- 2026-11-14:
  - Research done.
  - The duel engine, the mage and warrior layers and the field tools built.
  - The other classes' layers started, four in parallel.
  - First results: Frost mage over Arms warrior 89-92% (open field); the mage mirror 49%.
- 2026-11-14, later:
  - All nine classes have PvP layers. Shaman, warlock, hunter, priest, paladin, rogue and druid were written by agents; the mage
    and warrior drafts are being rewritten to the same standard.
  - Engine additions from the agents' findings:
    - pets that area spells and cleaves hit and control;
    - the defender's dodge, parry and block hooks;
    - Grounding through an engine hook; per-class trinkets that fire only when they free completely;
    - school lockouts on every spell; off-GCD spells (the fight lab ignores spell_gcd.json's off_gcd list);
    - no attacks on stealth; layer-declared immunities and stealth-keeping spells;
    - one DR count per step and spell; Wound Poison as a flat 165 off each heal per stack.
  - Baseline matrix (community builds, 200 duels a matchup), before the mage and warrior rewrite: strongly polarized, many
    matchups near 0% or 100%. Shadow priest and Ret/Prot paladin beat most classes; warlock and druid lose to healers.
    - Reading: each AI plays the same way every duel, so small edges become certainties, and AI quality differs between layers.
    - Next: a validation pass over the most extreme matchups (logs: AI defect or class strength), before any build is judged on
      the field.
- Fight-lab issues found on the way (they affect the leveling and raid pages; for the user to decide):
  - off-GCD spells cost a 1.5 s GCD;
  - the 2026-11-12 Stormstrike and Maelstrom Weapon hotfix is server-side and not in forever-spells;
  - Blackout procs from dot ticks (the client's proc mask has no periodic bit);
  - Hammer of Justice's stun is counted twice;
  - Voice of Truth (a trainer spell since 70753) is dropped;
  - Predator's Edge: the fight lab multiplies only the off-hand weapon's own damage by 1.5. Its aura (A_MOD_OFFHAND_DAMAGE_PCT)
    is a damage modifier on the whole off-hand hit, attack power included, as the raid simulator applies it. The melee Survival
    hunter's off hand is undervalued about 20%. Found 2026-11-14 comparing a guildmate's swords to a two-hander: the staff led by
    1.1% under the lab's rule and tied (±0.2%) under the whole-hit rule.
