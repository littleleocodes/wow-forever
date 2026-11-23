# ItemSparse (bind type, races, the other faction's item), client 1.60.1.70938 (2026-11-22)

From wago.tools' DB2 export (`https://wago.tools/db2/ItemSparse/csv?build=1.60.1.70938`, fetched earlier into
`~/.wow-forever-tools/wago/`, where the full table stays), for the gear lists (`raidsim/bind_types.py`, `raidsim/gear_lists.py`).
`ItemSparse-bind.csv` keeps seven columns for the simulator database's items only:

- `Bonding`: 0 none, 1 when picked up, 2 when equipped (the auction house can sell it), 3 when used, 4 quest item;
- `AllowableRace_0`: a race mask (-1 or 0: every race), which tells a one-faction item;
- `OppositeFactionItemID`: the other faction's version of the item;
- `RequiredHoliday`: an event item;
- `MinFactionID`, `MinReputation`: a reputation the item asks for (4 Friendly, 5 Honored, 6 Revered, 7 Exalted).

The export holds 19,325 rows, and only 3,632 of the simulator database's 7,389 items are among them (Hand of Justice, 11815, is not;
Lionheart Helm, 12640, is): the client ships part of the table and the server sends the rest. `bind_types.py` takes the client's value
where the row exists and Classic's `item_template` (CMaNGOS classic-db, `raw/2026-11-09-cmangos-classic-db-c33f90b8e/item_bonding.csv`)
otherwise. On the 2,119 items both hold they disagree on 3 (two items bind when picked up in the client and not at all in Classic,
one binds when equipped in the client and not at all in Classic).
