# SpellReagents for the crafted gear, client 1.60.1.71037 (2026-11-23)

From wago.tools' DB2 exports (`https://wago.tools/db2/SpellReagents/csv?build=1.60.1.71037` and `SpellEffect` of the same build; the
full tables stay in `~/.wow-forever-tools/wago/`), for the gear lists (`raidsim/bind_types.py --extract-reagents`, read by
`raidsim/gear_lists.py`). `SpellReagents-crafts.csv` keeps every spell that makes an item of the simulator's database (a create-item
effect, 24, or the database's own recipe spell): `spell`, `creates` (the item), `reagents` (`item:count;...`). All 998 crafted items of
the database at the pin of 2026-11-22 have a row.

Why: Classic's dump does not know Forever's recipes. 97 of them take Malleable Essence of Nature (274030; its tooltip: "Acquired from
disenchanting items from Hyjal Summit or Barrow Deeps"): the 72 item-level-61 epics of the Hyjal vendor's patterns and 25 item-level-65
epics. By the user's accepted reading (raid-material crafts are raid items) they are True BiS items from 2026-12-09.
