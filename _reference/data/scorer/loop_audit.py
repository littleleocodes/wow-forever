"""Loop audit: which community-taken talents does the model not understand?

For every Classic reference build (the community-standard builds the model is calibrated against) this lists
each talent the community takes with the model's value for it (score lost when the talent is removed from the
full build, per point). Talents below the threshold are flagged: the community takes them for a reason the model
does not encode - usually a role in the spec's loop (control, an enabler, safety) rather than damage. The same
check runs on the Forever hand drafts against the Forever optimizer builds.

    python _reference/data/scorer/loop_audit.py [class ...] [--threshold 0.004]

Writes `_reference/data/scorer/loops/audit.md`. The answers (why each flagged talent is taken, with sources) go
into `loops/<class>.json`, and their numbers into the manual effect files.
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

from compare_effects import build_alloc, load_builds  # noqa: E402
from effects import CLASSES  # noqa: E402
from optimize import Optimizer  # noqa: E402

sys.path.insert(0, str(HERE.parent))
from render_optimizer_sections import ROWS  # noqa: E402  (use-case -> spec, profile, Forever hand draft)

# Home spec model / profile for each Classic reference build: the pair whose model describes how that build plays.
HOME = {
    ("hunter", "bm-mm-raid"): ("mm-raid", "raid-dps"),
    ("hunter", "leveling-beast-mastery"): ("bm-leveling", "leveling-st"),
    ("hunter", "bm-solo-farm"): ("bm-leveling", "solo-60"),
    ("mage", "frost-winters-chill-raid"): ("frost-raid", "raid-dps"),
    ("mage", "frost-arcane-power-raid"): ("frost-raid", "raid-dps-extwc"),
    ("mage", "fire-raid"): ("fire-raid", "raid-dps"),
    ("mage", "leveling-frost"): ("frost-leveling", "leveling-st"),
    ("mage", "aoe-grinding-frost"): ("frost-aoe", "leveling-aoe"),
    ("warrior", "fury-dw-raid"): ("fury-dw-raid", "raid-dps"),
    ("warrior", "fury-2h-raid"): ("arms-2h-raid", "raid-dps"),
    ("warrior", "prot-raid-tank"): ("prot-tank", "raid-tank"),
    ("warrior", "leveling-arms"): ("arms-2h-raid", "leveling-st"),
    ("rogue", "combat-swords-raid"): ("combat-swords-raid", "raid-dps"),
    ("rogue", "combat-daggers-raid"): ("combat-daggers-raid", "raid-dps"),
    ("rogue", "leveling-combat-swords"): ("combat-swords-raid", "leveling-st"),
    ("priest", "holy-raid-healer"): ("holy-heal", "raid-heal"),
    ("priest", "disc-power-infusion-healer"): ("holy-heal", "raid-heal"),
    ("priest", "leveling-shadow"): ("shadow-dps", "leveling-st"),
    ("paladin", "holy-raid-healer"): ("holy-heal", "raid-heal"),
    ("paladin", "ret-raid-dps"): ("ret-dps", "raid-dps"),
    ("paladin", "prot-tank"): ("prot-tank", "raid-tank"),
    ("paladin", "leveling-retribution"): ("ret-dps", "leveling-st"),
    ("shaman", "resto-raid-healer"): ("resto-heal", "raid-heal"),
    ("shaman", "elemental-raid-dps"): ("elemental-dps", "raid-dps"),
    ("shaman", "enhancement-raid-support"): ("enhancement-dps", "raid-dps"),
    ("shaman", "leveling-enhancement"): ("enhancement-dps", "leveling-st"),
    ("warlock", "ds-ruin-raid"): ("sb-raid", "raid-dps"),
    ("warlock", "sm-ruin-raid"): ("sb-raid", "raid-dps"),
    ("warlock", "leveling-affliction-demo"): ("affliction-leveling", "leveling-st"),
    ("druid", "resto-swiftmend-healer"): ("resto-heal", "raid-heal"),
    ("druid", "resto-regrowth-natures-grace"): ("resto-heal", "raid-heal"),
    ("druid", "feral-cat-dps"): ("feral-cat-dps", "raid-dps"),
    ("druid", "feral-bear-tank"): ("feral-bear-tank", "raid-tank"),
    ("druid", "balance-moonkin-raid"): ("balance-dps", "raid-dps"),
    ("druid", "leveling-feral"): ("feral-cat-dps", "leveling-st"),
}


def removal_values(opt, alloc, level=60):
    """{talent: (rank, loss per point)} - score lost when the talent is dropped from `alloc` (dependants stripped)."""
    base = opt.score(alloc, level)
    out = {}
    for name, rank in alloc.items():
        trial = {n: r for n, r in alloc.items() if n != name}
        # strip anything that becomes illegal without it (prereqs / tier gating)
        changed = True
        while changed:
            changed = False
            if opt.tree.legal(trial):
                break
            for n in list(trial):
                t2 = {k: v for k, v in trial.items() if k != n}
                if opt.tree.legal(t2):
                    trial = t2; changed = True; break
            else:
                break
        loss = base - opt.score(trial, level)
        out[name] = (rank, loss / rank)
    return out


def audit_class(cls, threshold):
    rows = []
    cb = load_builds(ROOT / cls / "research" / "talents" / "classic-baseline" / "builds.json")
    fb = load_builds(ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json")
    opts = {}

    def optimizer(game, spec, prof):
        key = (game, spec, prof)
        if key not in opts:
            opts[key] = Optimizer(game, cls, spec, prof)
        return opts[key]

    for (c, cid), (spec, prof) in HOME.items():
        if c != cls or cid not in cb:
            continue
        opt = optimizer("classic-era", spec, prof)
        vals = removal_values(opt, build_alloc(cb[cid]))
        for name, (rank, v) in vals.items():
            rows.append(("classic", cid, spec, prof, name, rank, v, opt.effects[name]["source"], opt.tree.info[name][0]))
    # Forever: hand-draft talents the optimizer build for the same use-case dropped
    seen_drafts = set()
    for label, spec, prof, draft in ROWS.get(cls, []):
        fid = f"opt-{spec}-{prof}"
        if fid not in fb or draft not in fb or draft in seen_drafts:
            continue
        seen_drafts.add(draft)   # a draft is judged against the first (home) use-case that cites it
        opt = optimizer("forever", spec, prof)
        fa = build_alloc(fb[fid])
        for name, (rank, v) in removal_values(opt, build_alloc(fb[draft])).items():
            if fa.get(name, 0) == 0:
                rows.append(("forever-draft", draft, spec, prof, name, rank, v, opt.effects[name]["source"], opt.tree.info[name][0]))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--threshold", type=float, default=0.004, help="flag talents worth less than this per point (score units)")
    a = ap.parse_args()
    classes = [c for c in CLASSES if not a.classes or c in a.classes]
    out = ["# Loop audit: community-taken talents the model under-values", "",
           "> Generated by `_reference/data/scorer/loop_audit.py`. Value = score lost per point when the talent is removed from the full build "
           "(leveling: fraction of time per kill; raid: DPS/HPS/threat score). Talents under the threshold are flagged: the community takes them for a reason the model does not encode. "
           "Resolve each flag in `loops/<class>.json` (role, rationale, source) and the manual effect files.", ""]
    total_flags = 0
    total_open = 0
    for cls in classes:
        rows = audit_class(cls, a.threshold)
        flagged = [r for r in rows if r[6] < a.threshold]
        total_flags += len(flagged)
        loops_path = HERE / "loops" / f"{cls}.json"
        loops = json.load(open(loops_path, encoding="utf-8")) if loops_path.exists() else {}

        def documented(spec, name):
            entry = loops.get(spec, {}).get("talents", {}).get(name)
            if entry:
                return entry["role"], entry["why"]
            for sp, body in loops.items():
                if isinstance(body, dict) and name in body.get("talents", {}):
                    return body["talents"][name]["role"] + f" (from {sp})", body["talents"][name]["why"]
            return "", ""
        open_flags = [r for r in flagged if not documented(r[2], r[4])[0]]
        total_open += len(open_flags)
        out.append(f"## {cls.capitalize()} - {len(flagged)} flagged of {len(rows)} taken talents, {len(open_flags)} without a documented reason")
        out.append("")
        out.append("| Game | Build | Spec / profile | Talent | Tree | Ranks | Value/pt | Encoding | Documented role (loops/) | Why |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        for game, bid, spec, prof, name, rank, v, src, tree in sorted(flagged, key=lambda r: (r[0], r[1], r[6])):
            role, why = documented(spec, name)
            out.append(f"| {game} | `{bid}` | {spec} / {prof} | **{name}** | {tree} | {rank} | {v * 100:+.2f}% | {src} | {role or 'OPEN'} | {why[:140]} |")
        out.append("")
        print(f"{cls:8s} flagged {len(flagged)}/{len(rows)}  open {len(open_flags)}")
    (HERE / "loops").mkdir(exist_ok=True)
    (HERE / "loops" / "audit.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"total flagged: {total_flags} -> {(HERE / 'loops' / 'audit.md').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
