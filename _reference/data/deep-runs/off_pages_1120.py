"""Builds that leave the player pages and stay in research (2026-11-20, the play check's rule for alternatives, the audit session's
ruling: "a player page should not list a build that both fails the check and trails the pick"; an alternative that fails is put
through the exact filler pass, and leaves when a dead point has no legal home or it is an old build far behind its page's pick).
render_modes.page_list leaves out `player_page: false`; the research pages keep every build.

    python _reference/data/deep-runs/off_pages_1120.py [--write]
"""
import argparse
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(DATA)]
import paths  # noqa: E402
from filelock import locked  # noqa: E402
from fmt_json import dumps  # noqa: E402

OFF = {
    ("mage", "frost-winters-chill-raid"): "fails the play check (Presence of Mind never cast and worth nothing) and trails Frost's pick "
                                          "(frost-med-raid, 796.3) by 37% (504.6; full raid, 3,000 fights, seed 1)",
    ("mage", "arcane-blast-raid"): "fails the play check (Burning Soul and Improved Frostbolt worth nothing, neither a gate) and trails "
                                   "Arcane's pick (arcane-fire-raid, 825.9) by 16% (692.6; full raid, 3,000 fights, seed 1)",
    ("warlock", "destruction-fire-raid"): "fails the play check (Amplify Curse never cast and worth nothing, no gate) and trails "
                                          "Destruction's pick (destruction-succubus-raid, 881.5) by 17.5% (726.9)",
    ("paladin", "ret-raid-dps"): "fails the play check (Precision worth nothing at the hit cap, no gate) and trails Retribution's pick "
                                 "(767.8) by 17.7% (632.1)",
    ("paladin", "opt-ret-dps-raid-dps"): "fails the play check (Precision worth nothing at the hit cap, no gate) and trails Retribution's "
                                         "pick (767.8) by 17.7% (632.1)",
    ("rogue", "assassination-mutilate-raid"): "fails the play check (Remorseless Attacks worth nothing in a boss fight, no gate) and trails "
                                              "Assassination's pick (assassination-open-raid, 844.1) by 17.9% (692.8)",
    ("rogue", "subtlety-hemo-raid"): "fails the play check (Camouflage, Dirty Tricks, Improved Ambush, Master of Deception and Setup worth "
                                     "nothing in a raid) and trails Subtlety's pick (subtlety-ml-raid, 817.1) by 19% (661.5)",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    for cls in sorted({c for c, _ in OFF}):
        bp = paths.builds_json("forever", cls)
        with locked(bp.with_suffix(".lock")):
            data = json.load(open(bp, encoding="utf-8"))
            changed = 0
            for b in data["builds"]:
                why = OFF.get((cls, b["id"]))
                if not why or b.get("player_page") is False:
                    continue
                b["player_page"] = False
                b["player_page_why"] = f"2026-11-20: off the player pages, kept in research: {why}."
                changed += 1
                print(f"{cls} {b['id']}: off the player pages")
            if a.write and changed:
                bp.write_text(dumps(data) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
