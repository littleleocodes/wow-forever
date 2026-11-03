The official simulator's paladin presets as JSON, copied from wowsims/forever at bac92dbd5 (2026-11-02). Since #812 (2026-11-03) the
simulator keeps them as SIML (`ui/specs/paladin/**/*.siml`), which our tools do not read; the protection gear set is item for item the
same as the SIML one at d97252f2a (`foreverbench -siml2json`). The entries' tuned rotations are our own files one folder up; these are
the base rotations (dummy setting) and the tank's gear.
