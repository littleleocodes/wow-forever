"""Generate `_reference/beta-checklist.md`: what the level-30-capped beta can verify, per class.

Sections per class:
1. Talents reachable at 30 (rows 1-5) whose higher ranks are extrapolated -> read the real rank tooltips.
2. Hand-entered effects for those talents whose note admits an estimate -> confirm the mechanic/number.
3. Reachable talents whose tooltip quotes level-60 client damage/heal/mana numbers -> confirm the level-scaled values in game.
4. The 10-30 stretch of the recommended leveling order (respec-plan.md) -> play it and time it.
5. Ability unlock levels the spec models assume (Classic learn levels) -> confirm in Forever.
6. Cross-spec baselines the planner cannot measure -> time-to-kill comparisons at 30.
7. Open questions from the leveling builds.

    python _reference/data/build_beta_checklist.py
"""
import pathlib
import sys
import json
import re
from pathlib import Path
import paths  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SCORER = ROOT / "_reference" / "data" / "scorer"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
CAP = 30                              # Blizzard's final beta cap; the beta opened at 20 (2026-09-17) and rises to 30 later
MAX_ROW = (CAP - 9 - 1) // 5          # tier index reachable with cap-9 points (0-based row): 20 points -> row 4
EST_WORDS = re.compile(r"\b(est\.|estimated|unknown|assum|guess|pending|demo)", re.I)
NUM_TOOLTIP = re.compile(r"\b\d{2,4}\s*(?:to\s*\d{2,4}\s*)?(?:damage|healing|Mana|mana|health)\b|\bheals?\b.*\bfor \d{2,4}", re.I)


def load_json(p):
    return json.load(open(p, encoding="utf-8"))


def class_section(cls):
    tree = load_json(ROOT / "_reference" / "data" / "forever-talents" / f"{cls}.json")
    manual = load_json(SCORER / "effects" / "forever" / f"{cls}.manual.json")
    specs = load_json(SCORER / "specs" / f"{cls}.json")["models"]
    out = [f"## {cls.capitalize()}", ""]

    # 1 + 3: reachable talents
    est_rows, num_rows = [], []
    for tr in tree["trees"]:
        for t in tr["talents"]:
            if t["row"] > MAX_ROW:
                continue
            if t.get("estimated"):
                est_rows.append((tr["name"], t["row"] + 1, t["name"], t["maxRank"], t["estimated"]))
            first = (t.get("ranks") or [""])[0] or ""
            if NUM_TOOLTIP.search(first):
                num_rows.append((tr["name"], t["row"] + 1, t["name"], first.replace("\n", " ")[:160]))
    out.append(f"### 1. Read the real rank tooltips ({len(est_rows)} reachable talents have extrapolated ranks)")
    out.append("")
    out.append("| Tree | Row | Talent | Ranks | Extrapolated ranks |")
    out.append("|---|---|---|---|---|")
    for tn, row, name, mx, est in sorted(est_rows):
        out.append(f"| {tn} | {row} | {name} | {mx} | {', '.join(str(r) for r in est)} |")
    out.append("")

    # 2: manual notes with estimates for reachable talents
    reach = {t["name"] for tr in tree["trees"] for t in tr["talents"] if t["row"] <= MAX_ROW}
    est_manual = [(n, e["note"]) for n, e in manual.items() if n in reach and isinstance(e, dict) and EST_WORDS.search(e.get("note", ""))]
    out.append(f"### 2. Confirm the hand-entered mechanics ({len(est_manual)} reachable talents carry an estimate)")
    out.append("")
    out.append("| Talent | What the model assumes |")
    out.append("|---|---|")
    for n, note in sorted(est_manual):
        out.append(f"| {n} | {note[:220]} |")
    out.append("")

    out.append(f"### 3. Confirm level-scaled spell numbers ({len(num_rows)} reachable talents quote level-60 client values)")
    out.append("")
    out.append("| Tree | Row | Talent | Beta tooltip (level 60, build 1.60.1.70009) |")
    out.append("|---|---|---|---|")
    for tn, row, name, txt in sorted(num_rows):
        out.append(f"| {tn} | {row} | {name} | {txt} |")
    out.append("")

    # 4: leveling order 10-30 from the respec plan
    plan = paths.respec_plan(cls)
    out.append("### 4. Play the recommended 10-30 order and time it")
    out.append("")
    if plan.exists():
        text = plan.read_text(encoding="utf-8")
        m = re.search(r"## Recommended schedule.*?\n- \*\*Levels (\d+)-(\d+): (.*?)\*\*.*?- order: (.*?)\n", text, re.S)
        if m:
            steps = [s.strip() for s in m.group(4).split(",")]
            early = [s for s in steps if int(re.match(r"(\d+)", s).group(1)) <= CAP]
            out.append(f"Plan: **{m.group(3)}** (from `{cls}/leveling/respec-plan.md`)")
            out.append("")
            out.append("- " + "; ".join(early))
            out.append("")
            out.append("Log per level bracket: kills per hour, deaths, drink/eat time; compare with the alternative plans on the same page.")
    out.append("")

    # 5: unlock levels assumed
    out.append("### 5. Confirm ability unlock levels the models assume (Classic learn levels)")
    out.append("")
    rows = set()
    for mname, m in specs.items():
        for s in m["sources"]:
            ml = s.get("min_level")
            if ml and ml <= CAP + 10:
                rows.add((ml, s["id"], mname))
    out.append(", ".join(f"{sid} {ml} ({mn})" for ml, sid, mn in sorted(rows)) or "-")
    out.append("")

    # 6: cross-spec baselines
    models = list(specs)
    if len(models) > 1:
        out.append("### 6. Time-to-kill of a talentless spec vs spec at 30 (the planner assumes equal)")
        out.append("")
        out.append("Models: " + ", ".join(models) + ". Same mob, same gear, ~10 kills each, note kill time and downtime; this sets `abs_dps_factor`.")
        out.append("")

    # 7: open questions from leveling builds
    builds = load_json(ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json")["builds"]
    qs = []
    for b in builds:
        if b.get("content") == "leveling":
            for q in b.get("open_questions", []):
                if q not in qs:
                    qs.append(q)
    if qs:
        out.append("### 7. Open questions from the leveling builds")
        out.append("")
        for q in qs:
            out.append(f"- {q}")
        out.append("")
    return "\n".join(out)


def main():
    parts = ["# Beta checklist (level cap 30)", "",
             "> Generated by `_reference/data/build_beta_checklist.py` from the Forever talent snapshot (beta client build 1.60.1.70009), the scorer's manual effect files, the spec models and the respec plans. The beta opened 2026-09-17 with a level-20 cap that Blizzard raises to 30 later in the test (2026-09-17 to 2026-10-21); until then only rows 1-3 and the first 11 points are testable. "
             f"Only what a level-{CAP} character can verify: talent rows 1-5, spells learned by {CAP}, the first {CAP - 9} talent points. "
             "Capstones, raid crit/hit baselines and level-60 rotations stay open until the cap lifts.", "",
             "Global checks: respec cost schedule in Forever (the planner assumes 1g then +5g, cap 50g); whether DoTs can crit (the Forever models assume yes); pet talent behaviour; whether Forever changed any ability learn level (section 5 of each class).", ""]
    for cls in CLASSES:
        parts.append(class_section(cls))
    path = ROOT / "_reference" / "beta-checklist.md"
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
