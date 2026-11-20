# Upstream warlock rotations

The official wowsims/forever simulator's own warlock rotations at 2e6e77d84 (`ui/specs/warlock/dps/builds/*.build.json`, each build file's `player.rotation`), copied on 2026-11-19 for the independent audit's D1/D2 (our warlock entries had raced upstream's talents under rotations from the deleted ElliotWood fork). Book ranks swapped to trainer ranks (`trainer_ranks.py`). They compete as rotations in the warlock entries (`deep-runs/warlock_raid_1119.sh`); an entry that adopts one takes it as its base (`apl`) and tunes from there.
