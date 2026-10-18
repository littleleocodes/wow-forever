# Port to wowsims/forever (in progress, paused 2026-10-18)

User decision 2026-10-18 (audit 2 row 1): the raid pipeline moves from the deleted ElliotWood/Forever fork to the official
github.com/wowsims/forever. The port was stopped mid-work by the user the same evening; this note records the state.

- Changed, not built or tested: `raidsim/foreverbench/main.go` (port in progress, incl. a spell-listing mode), the raid APLs' spell ids
  (`raidsim/apl_remap.py`, `raidsim/apl-remap.json`), preset paths in `raidsim/specs.json` (the old fork's presets copied to
  `raidsim/presets/elliotwood-b7083fa/`).
- Not changed yet: `raidsim/setup.py` and `cloud_setup.py` still name the deleted fork and pin b7083fa (a fresh clone fails); the edits
  and patches are not ported; no smoke test has run.
- Next: finish the bench port, port or retire each edit and patch (the list in `patches/README.md`; plus audit 2 rows 13, 19, 57, 69 and
  plan item 16), switch setup.py to the official repository and its commit, smoke-test a handful of entries against the last committed
  numbers, then write this file's results.
