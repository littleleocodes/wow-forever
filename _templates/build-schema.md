# Build JSON schema

Used by `<class>/research/talents/classic-baseline/builds.json` and `<class>/research/talents/forever/proposed-builds.json`.
Validated by `_reference/data/validate_builds.py`, rendered by `render_builds.py` (build pages under
`<class>/research/<leveling|raid|pvp>/builds/`) and `render_modes.py` (player pages). Fields checked against the files on 2026-10-15.

```jsonc
{
  "class": "Warrior",                 // display name
  "game": "classic-era" | "forever",  // which tree dataset to validate against
  "notes": "One paragraph shown on the index page.",
  "builds": [
    {
      "id": "fury-dw-raid",           // file name of the generated page; kebab-case, unique in the file (see "Ids" below)
      "name": "Fury — Dual Wield (raid DPS)",
      "role": "dps" | "healer" | "tank",
      "content": "raid" | "dungeon" | "pvp" | "leveling" | "solo",   // decides the research folder: leveling/solo -> research/leveling/,
                                                                    // raid/dungeon -> research/raid/, pvp -> research/pvp/
      "tier": "primary" | "alternative" | "situational" | "draft",   // "draft" for every Forever build (unverified in game)
      "spec": "Fury",                 // optional: the player page it belongs to, a tree name or "Hybrid A/B" (spec_modes.py);
                                      // without it: tank/healer tree by role, else the tree with 30+ points, else a hybrid
      "based_on": "fury-dw-raid",     // Forever hand drafts: id of the Classic baseline it derives from
      "summary": "What the build is for and what it revolves around.",
      "allocation": {                 // every tree must be listed, in in-game order; [] for none
        "Arms": [["Improved Heroic Strike", 3], ["Tactical Mastery", 5]],
        "Fury": [["Cruelty", 5]],
        "Protection": []
      },
      "order": [                      // leveling builds; simulated level by level by the validator
        {"levels": "10-12", "tree": "Arms", "talent": "Improved Rend", "points": 3}
      ],
      "order_label": "own tree first",   // optional: which raced order the leveling search picked ("stats model", "own tree first",
                                         // "own tree last"; fightlab/fl_levels.py, raid_path_leveling.py)
      "core": [                       // priority order; the talents that define the build
        {"talent": "Bloodthirst", "why": "…"}
      ],
      "flex": [                       // points that can move without changing the build's identity
        {"points": 5, "default": "Improved Battle Shout", "alternatives": ["Booming Voice"], "why": "…"}
      ],
      "notes": ["Rotation hints, caveats."],
      "open_questions": ["Forever builds: what to verify at launch."],   // collected by build_launch_checklist.py
      "sources": ["https://…"],

      // Written by the scripts, not by hand (Forever only):
      "generated": "2026-10-15",      // date a script wrote the build; alone (no "derived") = a slot filler from spec_builds.py (⚗)
      "derived": "leveling" | "raid" | "pvp",   // a search's winner (🔬): derive_*.py, open_builds.py, raidsim/ml_builds.py,
                                                // heallab/deep_heal.py, raidsim/deep_tank.py, raid_path_leveling.py
      "replaces": "mm-hawk-raid",     // the hand draft this derived build beat by the bar (0.5% since 2026-10-07); the draft stays
                                      // as the alternative
      "raid_path": "holy-raid-healer",   // healer and tank leveling builds: the raid build they level into (raid_path_leveling.py)
      "preset": "Feral Cat 9/35/7",   // a derived build taken from one of the community simulator's preset talent builds
      "max_level": 60                 // optional, unused at present; total points must equal max_level - 9 (default 60 -> 51)
    }
  ]
}
```

Ids:

- Hand drafts: `<spec>-<variant>-<content>` (`fury-dw-raid`, `pvp-frost`, `leveling-arms`).
- Stats-model exports: `opt-<spec model>-<profile>` (`opt-fury-dw-raid-raid-dps`); search winners: `<spec slug>-ml-raid`,
  `-ml-parse`, `-ml-heal`, `-ml-tank`, `-open-raid`, `-open-leveling`.

Rules:

- Talent names must match the dataset exactly (`_reference/data/classic-era-talents.json` or
  `_reference/data/forever-talents/<class>.json`). The validator reports unknown names.
- Tier gating (5 points per tier) and prerequisites are enforced; the validator prints what is missing.
- Keep the file compact with `python _reference/data/fmt_json.py <file>`.
- After an edit: `python _reference/data/validate_builds.py && python _reference/data/render_builds.py` (must print `all builds valid`),
  then `python _reference/data/rebuild.py --steps regen` for the player pages.
