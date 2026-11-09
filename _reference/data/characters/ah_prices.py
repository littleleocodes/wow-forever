"""Auction house prices from the user's ForeverTape add-on (2026-11-09, user: "in that folder I have an auction house add-on that is
updated hourly for all the prices of stuff ... that could help with the professions and auction house upgrades and any profession plans").

READ ONLY. ForeverTape (the user's add-on project, F:\\wow-addons, its own Claude session) writes, inside the game's add-on folder:
- AHCopy.lua: the whole auction house, hourly, from Blizzard's API (a scheduled task at :25): ForeverTape_AHCopy = { t = <epoch>,
  house = 110, rows = [[itemID,quantity,buyoutTotalCopper,,,,variant ...]], ... }; lots at one unit price are merged, so the unit price
  is buyoutTotal / quantity; variant "" for plain items, "b<bonus ids>" for gear versions; the user's own auctions are left out.
- Insights.lua: what items really sell for, from sales: ForeverTape_Insights.items[itemID] = "typical,source,soldPerDay,confidence,...".
Never read the add-on project's data/bnet_client.toml (the user's API secret), the WTF Config.wtf or RXPGuides (the add-on session's
request, 2026-11-09). Prices in copper.
"""
import pathlib
import re
import time

ROW = re.compile(r"^(\d+),(\d+),(\d+),[^,]*,[^,]*,[^,]*,(.*)$")
INS = re.compile(r"\[(\d+)\]\s*=\s*\"(\d+),([a-z]?),")


class Prices:
    def __init__(self, ahcopy, insights=None):
        self.t, self.rows, self.typical = None, {}, {}
        p = pathlib.Path(ahcopy)
        if p.exists():
            s = p.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"\bt\s*=\s*(\d+)", s)
            self.t = int(m.group(1)) if m else None
            block = re.search(r"rows\s*=\s*\[\[(.*?)\]\]", s, re.S)
            for line in (block.group(1) if block else "").splitlines():
                r = ROW.match(line.strip())
                if not r:
                    continue
                item, qty, total, variant = int(r.group(1)), int(r.group(2)), int(r.group(3)), r.group(4).strip()
                if qty and total:
                    self.rows.setdefault((item, variant), []).append((total / qty, qty))
        q = pathlib.Path(insights) if insights else None
        if q and q.exists():
            for m in INS.finditer(q.read_text(encoding="utf-8", errors="replace")):
                self.typical[int(m.group(1))] = (int(m.group(2)), m.group(3))

    def age_hours(self):
        return None if self.t is None else (time.time() - self.t) / 3600

    def cheapest(self, item, variant=""):
        """The "real cheapest" unit price in copper (ForeverTape's rule: the lowest price with at least 3% of the units at or below it,
        so a few odd cheap units do not count), and the units listed; None when nothing is listed."""
        lots = sorted(self.rows.get((item, variant), []))
        if not lots:
            return None
        units = sum(q for _, q in lots)
        need, seen = max(1, units * 0.03), 0
        for price, q in lots:
            seen += q
            if seen >= need:
                return price, units
        return lots[-1][0], units

    def buy(self, item, variant=""):
        """What buying one costs now: the real cheapest listing, else the typical sale price (Insights); None when unknown."""
        c = self.cheapest(item, variant)
        if c:
            return c[0]
        t = self.typical.get(item)
        return t[0] if t else None

    def listed(self, item, variant=""):
        return (item, variant) in self.rows


def money(copper):
    if copper is None:
        return "no price"
    copper = int(round(copper))
    g, s, c = copper // 10000, copper // 100 % 100, copper % 100
    return " ".join(x for x in (f"{g}g" if g else "", f"{s}s" if s else "", f"{c}c" if c or not (g or s) else "") if x)
