"""Markdown for the gear-tier sets with links (2026-10-03, user request: a way to see the actual pre-BiS and BiS items).

Reads raidsim/gear-links.json (written by raidsim/gear_links.py: every item and enchant with its Wowhead Forever link and source, and
share links that open each tier x setting character in the community simulator's live web UI). Used by render_modes.py (raid pages)
and raidsim/ml_builds.py --rank (_reference/dps-rankings.md). Without the file the callers fall back to plain item names.
"""
import functools
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LINKS = HERE / "raidsim" / "gear-links.json"
TIER_NAME = {"dungeon": "Quests and dungeons", "prebis": "Pre-BiS", "bis": "Raid BiS"}   # (2026-11-18: the third tier; "Phase 1 BiS" before)
TIERS = ("dungeon", "prebis", "bis")


@functools.lru_cache(maxsize=None)
def data():
    try:
        return json.load(open(LINKS, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def spec(cls, spec_name, role=None):
    """A spec's sets; `role` "tank" or "heal" for the support sets (2026-10-15: the druid's bear shares the Feral Combat page)."""
    return (data().get("specs") or {}).get(f"{cls}|{spec_name}" + (f"|{role}" if role else ""))


def sim_link(cls, spec_name, key):
    """The simulator share link of a tier x setting ("bis-raid", "prebis-dummy" ...), or None."""
    return ((spec(cls, spec_name) or {}).get("sim") or {}).get(key)


def cell(row):
    """One item: its Wowhead link, where it comes from, its enchant."""
    out = f"[{row['name']}]({row['url']})"
    if row.get("source"):
        out += f" · *{row['source']}*"
    e = row.get("enchant")
    if e:
        out += "<br>+ " + (f"[{e['name']}]({e['url']})" if e.get("url") else e["name"])
    return out


def table(cls, spec_name, role=None):
    """Markdown lines: a Slot | Quests and dungeons | Pre-BiS | Raid BiS table of the spec's sets, every item linked; [] without links."""
    s = spec(cls, spec_name, role)
    if not s or not s.get("gear"):
        return []
    tiers = [t for t in TIERS if t in s["gear"]]
    keyed = {}
    order = []
    for t in tiers:
        seen = {}
        for row in s["gear"][t]:
            n = seen.get(row["slot"], 0)
            seen[row["slot"]] = n + 1
            k = (row["slot"], n)
            if k not in keyed:
                keyed[k] = {}
                order.append(k)
            keyed[k][t] = row
    o = ["| Slot | " + " | ".join(TIER_NAME[t] for t in tiers) + " |", "|---" * (len(tiers) + 1) + "|"]
    for k in order:
        o.append(f"| {k[0]} | " + " | ".join(cell(keyed[k][t]) if t in keyed[k] else "-" for t in tiers) + " |")
    return o


ONYXIA = "Onyxia's Lair"


def raid_gear(s):
    """{tier: {raid: [item and enchant names]}} of a spec's sets, from gear_links.py's raid tags."""
    out = {}
    for t, rows in (s.get("gear") or {}).items():
        for row in rows or []:
            for name, raid in ((row.get("name"), row.get("raid")), ((row.get("enchant") or {}).get("name"), (row.get("enchant") or {}).get("raid"))):
                if raid:
                    out.setdefault(t, {}).setdefault(raid, []).append(name)
    return out


def raid_note(cls, spec_name, role=None):
    """One line under a gear table whose sets hold raid gear (2026-11-22, the user first-hand to the audit session: "Molten Core is not in
    Forever right now. No raid is. And the only raids coming are the 3 you mentioned": The Barrow Deeps, Hyjal Summit and Onyxia's Lair,
    2026-12-09). Each column's Molten Core and Onyxia's Lair items and enchants (a pre-raid caster set's Enchant Weapon - Spell Power is
    a Molten Core formula), from gear_links.py's raid tags; [] when the sets hold none."""
    found = raid_gear(spec(cls, spec_name, role) or {})
    if not found:
        return []
    cols = []
    for t in TIERS:
        for raid in ("Molten Core", ONYXIA):
            if (found.get(t) or {}).get(raid):
                cols.append(f"{TIER_NAME[t]}: {', '.join(dict.fromkeys(found[t][raid]))} ({raid})")
    mc = any("Molten Core" in v for v in found.values())
    head = ("Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and "
            "Onyxia's Lair." if mc else "No raid is open yet: Onyxia's Lair opens on 2026-12-09.")
    return [f"*{head} These sets still count raid gear ({'; '.join(cols)}). The gear lists are being made again.*", ""]


def any_mc(cls, spec_names):
    """True when a set of any of the specs holds Molten Core gear (the class raid index's note)."""
    return any("Molten Core" in v for n in spec_names for v in raid_gear(spec(cls, n) or {}).values())


def sim_line(cls, spec_name, raid_first=True, role=None):
    """'Open in the simulator' links for every tier, or ''."""
    s = spec(cls, spec_name, role)
    if not s or not s.get("sim"):
        return ""
    parts = []
    for t in TIERS:
        # the full raid only: the player pages show no training-dummy setting since 2026-10-04 (user decision: raid and leveling only)
        links = [f"[{lab}]({s['sim'][f'{t}-{st}']})" for st, lab in (("raid", "full raid"),) if s["sim"].get(f"{t}-{st}")]
        if links:
            parts.append(f"{(LIST_NAME if s.get('lists') else TIER_NAME)[t]}: " + " · ".join(links))
    return ("**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, "
            "rotation, consumables and buffs we simulate): " + "; ".join(parts) + ".") if parts else ""


# ------------------------------------------------------------------------------------------------ the three lists (2026-11-23)
# The user, 2026-11-22: "True BiS": "all obtainable items like PvP rewards, raids, dungeons, 0.5 quest chain, etc."; "True Pre-BiS":
# "everything that doesn't include raids"; "Easy Pre-BiS": "things just like dungeons and quests and doesn't include recipes and using the
# AH". The audit session's page spec of 2026-11-23: each list under its name with its definition; a set with one-faction items shown as
# the Alliance and Horde sets; each item's source in a player's words, PvP marked; the no-PvP set for the True lists; the hit against
# the caps, the set bonuses, the currency; each list's DPS on the same fights and the gap from Easy to True Pre-BiS; the footer.
LIST_ORDER = ("dungeon", "prebis", "bis")
LIST_NAME = {"dungeon": "Easy Pre-BiS", "prebis": "True Pre-BiS", "bis": "True BiS"}
LIST_DEF = {"dungeon": "dungeons and quests: no crafting recipes, no auction house, reputation up to Honored",
            "prebis": "everything in the game now that doesn't come from a raid: dungeons, quests, crafts, the auction house, reputation, "
                      "PvP rewards, the Tier 0.5 chain",
            "bis": "everything obtainable: True Pre-BiS plus the raids open now (none until The Barrow Deeps, Hyjal Summit and Onyxia's "
                   "Lair on 2026-12-09); the set differs from True Pre-BiS only where a raid item wins"}
KIND_WORDS = {"dungeon_drop_easy": "dungeon", "dungeon_drop": "dungeon", "world_drop": "world drop", "quest": "quest", "quest_ubrs": "quest",
              "quest_traded": "quest (its turn-in comes from the auction house)",
              "tier05": "Tier 0.5 chain", "craft": "crafted", "rep_to_honored": "reputation (Honored or below)",
              "rep_above_honored": "reputation (Revered or Exalted)", "battleground_easy": "battleground (Honored or below)",
              "battleground": "battleground (Revered or Exalted)", "pvp": "honor rank", "vendor": "vendor",
              "dungeon_currency": "Pix Xizzix, for Tarnished Undermine Reals", "auction": "auction house", "vetted": "no listed source",
              "onyxia": "Onyxia's Lair", "new_raid": "a raid of 2026-12-09"}
HIT_NAME = {"melee_main_hand": "melee (main hand)", "melee_off_hand": "melee (off hand)", "ranged": "ranged", "spell": "spells"}


def has_lists(cls, spec_name, role=None):
    """True when the spec's sets were made under the lists (gear-links.json carries them)."""
    return bool((spec(cls, spec_name, role) or {}).get("lists"))


def source_words(row):
    """Where an item comes from, in a player's words: the list kind first (dungeon, quest, crafted, reputation, battleground, honor rank,
    auction house ...), then the database's detail (the boss and dungeon, the quest, the profession, the vendor)."""
    kinds = [k for k in row.get("kinds") or [] if k in KIND_WORDS]
    kind = KIND_WORDS[kinds[0]] if kinds else ""
    if kinds and row.get("standing") and kinds[0] in ("rep_to_honored", "rep_above_honored", "battleground_easy", "battleground"):
        kind = ("reputation" if kinds[0].startswith("rep") else "battleground") + f" ({row['standing']})"   # the faction and standing
    detail = row.get("source") or ""
    if detail.startswith("sold by ") and detail[8:] in kind:   # "Pix Xizzix, for Tarnished Undermine Reals" says the vendor once
        detail = ""
    if detail.endswith(" reputation") and kind.startswith("reputation ("):
        detail = ""
    if detail.startswith("quest: ") and kind == "quest":
        return "quest: " + detail[7:]
    return ", ".join(x for x in (kind, detail) if x) or "-"


def list_rows(rows):
    """A list set's table: Slot | Item | From | Enchant; PvP items and profession-bound crafts marked."""
    o = ["| Slot | Item | From | Enchant |", "|---|---|---|---|"]
    for row in rows:
        m = row.get("marks") or {}
        tags = (" **PvP**" if m.get("pvp") else "") + (f" *(you need {m['profession']})*" if m.get("profession") else "") \
            + (" *(effect not simulated)*" if row.get("effect_not_simulated") else "")
        fa = row.get("faction_alt")
        if fa:   # a one-faction item in a set shown as one set: the other side's item (its twin when the stats are the same)
            tags += f" ({fa['faction']}; {fa['for']}: [{fa['name']}]({fa['url']}){', the same stats' if fa.get('twin') else ''})"
        e = row.get("enchant")
        ench = (f"[{e['name']}]({e['url']})" if e.get("url") else e["name"]) if e else "-"
        o.append(f"| {row['slot']} | [{row['name']}]({row['url']}){tags} | {source_words(row)} | {ench} |")
    return o


def list_facts(x):
    """The lines under a list's table: hit against the caps, the set bonuses on, the bonuses not simulated, the currency."""
    o = []
    hit = x.get("hit") or {}
    used = {u["hit"]: u for u in hit.get("used") or []}
    if used:
        parts = []
        mh, oh = used.get("melee_main_hand"), used.get("melee_off_hand")
        if mh and oh and mh["value"] == oh["value"]:
            parts.append(f"melee {mh['value']:g}% (both hands; useful up to {mh['cap']:g}% for a dual wielder's swings)")
        else:
            parts += [f"{HIT_NAME[k]} {used[k]['value']:g}% of {used[k]['cap']:g}%" for k in ("melee_main_hand", "melee_off_hand") if k in used]
        parts += [f"{HIT_NAME[k]} {used[k]['value']:g}% (cap {used[k]['cap']:g}%)" for k in ("ranged", "spell") if k in used]
        line = "Hit: " + "; ".join(parts)
        if hit.get("flags"):
            line += ". Past every cap this build uses: some of this hit is wasted"
        o.append(line + ".")
    if x.get("sets_on"):
        o.append("Set bonuses on: " + ", ".join(x["sets_on"]) + ".")
    for u in x.get("unsimulated") or []:
        for b in u.get("reached") or []:
            text = b["text"] if "$" not in (b.get("text") or "$") else "an effect the simulator does not play"
            o.append(f"Set bonus not simulated: {u['set']} ({b['pieces']} pieces): {text}")
    cc = x.get("currency_cost")
    if cc:
        tot = cc.get("total", cc) if isinstance(cc, dict) else cc
        o.append("Currency: " + (", ".join(f"{v} {k}" for k, v in tot.items()) if isinstance(tot, dict) else str(tot)) + ".")
    return [f"*{line}*" for line in o]


def lists_section(cls, spec_name, role=None, lacks=None):
    """Markdown lines of a spec's three lists (see the block comment above), or [] when its sets predate the lists. `lacks`: the line a
    tank's or healer's page carries about the rules its maker does not apply yet."""
    s = spec(cls, spec_name, role) or {}
    L = s.get("lists") or {}
    if not L:
        return []
    o = []
    d = {t: L[t]["dps"] for t in LIST_ORDER if t in L and L[t].get("dps")}
    if d:
        parts = []
        for t in LIST_ORDER:
            if t in d:
                gap = f" ({d[t] / d['dungeon'] - 1:+.1%} over Easy Pre-BiS)" if t != "dungeon" and "dungeon" in d else ""
                parts.append(f"{LIST_NAME[t]} {d[t]:.0f}{gap}")
        o += ["**This build in each list's set** (full raid, the same fights, two seeds): " + "; ".join(parts) + ".", ""]
    for t in LIST_ORDER:
        if t not in L:
            continue
        x = L[t]
        o += [f"#### {LIST_NAME[t]}", "", f"*{LIST_DEF[t]}.* Average item level {x.get('ilvl', '-')}.", ""]
        sides = [k for k in (f"{t}-alliance", f"{t}-horde") if k in L]
        if x.get("faction_alternatives") and sides:
            o += ["This list's best set holds items only one faction can use, so it is shown as the set each faction can wear.", ""]
            for k in sides:
                head = f"**{k.split('-')[1].capitalize()}**" + (f" ({L[k]['dps']:.0f})" if L[k].get("dps") else "")
                o += [head, ""] + list_rows(L[k]["rows"]) + [""] + list_facts(L[k]) + [""]
        else:
            o += list_rows(x["rows"]) + [""] + list_facts(x) + [""]
        nk = f"{t}-nopvp"
        if t != "dungeon" and nk in L and any((r.get("marks") or {}).get("pvp") for r in x["rows"]):
            o += [f"**{LIST_NAME[t]} without PvP rewards** (the set most players can wear now):", ""] + list_rows(L[nk]["rows"]) + [""]
            o += list_facts(L[nk]) + [""]
    foot = []
    if any((L[k].get("budget") or "default") == "first-pass" for k in L):
        foot.append("Sets chosen at the first-pass budgets (1,000 fights a candidate, 6,000 to confirm); close calls are being made again "
                    "at the full budgets.")
    if any(L[k].get("close_call") for k in L):
        foot.append("A set marked as a close call here led the next set by less than 0.2%: it is being made again.")
    ns = sorted({r["name"] for k in L for r in L[k]["rows"] if r.get("effect_not_simulated")})
    if ns:
        foot.append("Effects not simulated (the item counts for its stats only): " + ", ".join(ns) + ".")
    if lacks:
        foot.append(lacks)
    if foot:
        o += ["*" + " ".join(foot) + "*", ""]
    return o
