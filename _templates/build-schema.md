# Build JSON schema

Used by `<class>/talents/classic-baseline/builds.json` and `<class>/talents/forever/proposed-builds.json`.
Validated by `_reference/data/validate_builds.py`, rendered by `render_builds.py`.

```jsonc
{
  "class": "Warrior",                 // display name
  "game": "classic-era" | "forever",  // which tree dataset to validate against
  "notes": "One paragraph shown on the index page.",
  "builds": [
    {
      "id": "fury-dw-raid",           // file name of the generated page; kebab-case, unique in the file
      "name": "Fury — Dual Wield (raid DPS)",
      "role": "dps" | "healer" | "tank",
      "content": "raid" | "dungeon" | "pvp" | "leveling" | "solo",
      "tier": "primary" | "alternative" | "situational" | "draft",   // "draft" for unverified Forever builds
      "based_on": "fury-dw-raid",     // Forever builds only: id of the Classic baseline it derives from
      "summary": "What the build is for and what it revolves around.",
      "allocation": {                 // every tree must be listed, in in-game order; [] for none
        "Arms": [["Improved Heroic Strike", 3], ["Tactical Mastery", 5]],
        "Fury": [["Cruelty", 5]],
        "Protection": []
      },
      "order": [                      // leveling builds only; simulated level by level by the validator
        {"levels": "10-12", "tree": "Arms", "talent": "Improved Rend", "points": 3}
      ],
      "core": [                       // priority order; the talents that define the build
        {"talent": "Bloodthirst", "why": "…"}
      ],
      "flex": [                       // points that can move without changing the build's identity
        {"points": 5, "default": "Improved Battle Shout", "alternatives": ["Booming Voice"], "why": "…"}
      ],
      "notes": ["Rotation hints, caveats."],
      "open_questions": ["Forever builds: what to verify at launch."],
      "sources": ["https://…"],
      "max_level": 60                 // optional; total points must equal max_level - 9 (default 60 → 51)
    }
  ]
}
```

Rules:

- Talent names must match the dataset exactly (`_reference/data/classic-era-talents.json` or
  `_reference/data/forever-talents/<class>.json`). The validator reports unknown names.
- Tier gating (5 points per tier) and prerequisites are enforced; the validator prints what is missing.
- Keep the file compact with `python _reference/data/fmt_json.py <file>`.
