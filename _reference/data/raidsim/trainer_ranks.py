"""Trainer ranks only in the raid rotations (2026-11-19, the independent audit's H18; user: "Go with the audits recommendations").

The official simulator knows the class books' ranks (sim/core/spelldata/book_ranks.go: Grimoire of Shadow Bolt X, Tome of Frostbolt XI,
Guide: Serpent Sting IX, Tablet of Flame Shock VI, Handbook of Backstab IX ...), and 45 of our rotation files cast them. In Classic most
of these books drop in Ruins of Ahn'Qiraj; Forever's raids open on 2026-12-09 with Molten Core and Onyxia.

ASSUMPTION (the audit session's reading, approved with its recommendations; not the user's own words): Forever has no class books yet,
so every rotation casts the trainer's top rank: the same rule as the gear (what the game has now). The pages say so.

One mapping, book id -> trainer id (`trainer-ranks.json`): the trainer's highest rank below the book's, by rank number in our spellbooks
(their rank lists are not always in rank order: Shadow Bolt lists rank 10 before rank 9). The simulator registers both ranks of every
spell a rotation casts (Shadow Bolt 11661 and 25307, Serpent Sting 13555 and 25295, Starfire and Flame Shock all ranks). Every
reference is swapped, casts and conditions alike (dotRemainingTime, spellCastTime, auraIsActive ...): a rotation that casts the trainer
rank while its conditions still name the book rank reads an absent spell (forever_absent.go) and stops casting it.

    python _reference/data/raidsim/trainer_ranks.py              # list the rotation files that name a book rank
    python _reference/data/raidsim/trainer_ranks.py --apply      # swap them to the trainer rank, in place (format kept)
    python _reference/data/raidsim/trainer_ranks.py --reverse    # undo when Forever adds the books: each trainer top rank back to the book's
    python _reference/data/raidsim/trainer_ranks.py --map        # rewrite trainer-ranks.json from book_ranks.go and forever-spells/

Rotation files: everything under raidsim/apls/ (but `prev-*` folders, kept copies of older rotations) and every rotation a specs.json
entry names inside this repository (the entries' bases under presets/). The insertion pool of the rotation search leaves book ranks out
(apl_opt.new_spell_pool), and apl_validate.py lists any book rank left in an entry's rotation.
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
MAP = HERE / "trainer-ranks.json"
SPELLS = DATA / "forever-spells"
ASSUMPTION = ("Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like; "
              "Ruins of Ahn'Qiraj in Classic) are assumed not to be in Forever yet.")


def book_ids(sim_repo):
    """{book rank id: what teaches it} from the simulator's hand-kept list."""
    src = (pathlib.Path(sim_repo) / "sim" / "core" / "spelldata" / "book_ranks.go").read_text(encoding="utf-8")
    return {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"(\d+): true, // (.*)", src)}


def make_map(sim_repo):
    book = book_ids(sim_repo)
    ranks = {}
    for f in sorted(SPELLS.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for tab in d["tabs"]:
            for sp in tab["spells"]:
                ids = [(int(re.sub(r"\D", "", r.get("rank") or "0") or 0), r["id"]) for r in sp["ranks"] if r.get("id")]
                for n, sid in ids:
                    ranks[sid] = (f.stem, sp["name"], n, ids)
    out = {}
    for b, why in sorted(book.items()):
        if b not in ranks:
            continue   # a buff aura of a book rank (the totem tablets' buffs): no rotation casts it
        cls, name, n, ids = ranks[b]
        if b == 31018:   # "Book of Ferocious Bite V, which teaches rank 6"
            n = 6
        lower = sorted((m, sid) for m, sid in ids if m < n and sid not in book)
        if not lower:
            continue
        out[str(b)] = {"trainer": lower[-1][1], "class": cls, "spell": name, "book_rank": n, "trainer_rank": lower[-1][0], "book": why}
    return out


def load_map():
    return {int(k): v for k, v in json.loads(MAP.read_text(encoding="utf-8"))["map"].items()}


def rotation_files():
    files = {p for p in (HERE / "apls").rglob("*.json") if not any(part.startswith("prev-") for part in p.parts)}
    specs = json.loads((HERE / "specs.json").read_text(encoding="utf-8"))   # the Forever entries, by class
    for cls, entries in specs.items():
        if cls.startswith("_") or not isinstance(entries, dict):
            continue
        for e in entries.values():
            if not isinstance(e, dict):
                continue
            for key in ("apl", "apl_opt", "apl_opt_raid"):
                p = ROOT / e[key] if e.get(key) else None
                if p and p.is_file():
                    files.add(p)
    return sorted(files)


SPELL = re.compile(r'("spellId"\s*:\s*)(\d+)(\s*,\s*"rank"\s*:\s*\d+)?')


def swap_text(text, mp):
    """The text with every spellId of `mp` swapped ({old id: (new id, new rank)}), a "rank" right after it set to the new rank."""
    def sub(m):
        old = int(m.group(2))
        if old not in mp:
            return m.group(0)
        new, rank = mp[old]
        tail = re.sub(r"\d+$", str(rank), m.group(3)) if m.group(3) else ""
        return f"{m.group(1)}{new}{tail}"
    return SPELL.sub(sub, text)


def named(text, ids):
    return sorted({int(x) for x in re.findall(r'"spellId"\s*:\s*(\d+)', text)} & set(ids))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--reverse", action="store_true")
    ap.add_argument("--map", action="store_true")
    a = ap.parse_args()
    if a.map or not MAP.exists():
        sys.path.insert(0, str(HERE))
        import setup as SIM_SETUP
        mp = make_map(SIM_SETUP.checkout())
        MAP.write_text(json.dumps({"assumption": ASSUMPTION, "source": "sim/core/spelldata/book_ranks.go of the pinned simulator and "
                                   "our spellbooks' rank numbers (trainer_ranks.py --map)", "map": mp}, indent=1) + "\n", encoding="utf-8")
        print(f"{len(mp)} book ranks -> {MAP.relative_to(ROOT)}")
    mp = load_map()
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in mp.items()}
    rev = {v["trainer"]: (b, v["book_rank"]) for b, v in mp.items()}
    use = rev if a.reverse else fwd
    n = 0
    for p in rotation_files():
        text = p.read_text(encoding="utf-8")
        hit = named(text, use)
        if not hit:
            continue
        n += 1
        rel = p.relative_to(ROOT).as_posix()
        names = ", ".join(str(i) for i in hit)
        if a.apply or a.reverse:
            p.write_text(swap_text(text, use), encoding="utf-8", newline="")
            print(f"{'swapped' if a.apply else 'reversed'} {rel}: {names}")
        else:
            print(f"{rel}: {', '.join(mp[i]['spell'] + f' ({i})' for i in hit)}")
    print(f"{n} rotation files {'changed' if (a.apply or a.reverse) else 'name a book rank'}")


if __name__ == "__main__":
    main()
