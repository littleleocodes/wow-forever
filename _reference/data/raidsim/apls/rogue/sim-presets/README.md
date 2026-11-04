The official simulator's rogue default rotation, copied from wowsims/forever at 6ee3c30f3 (2026-11-04, the rogue port #840/#849:
Shank after the energy pooling checks, the Ghostly Strike buff where Cutthroat was read, no Venom finisher or Thousand Cuts lines).
Our rotations of the entries were tuned before the rework and name spells and talents the 70755 rogue no longer has (the Venom finisher
1259812/1259799, Cutthroat 1310721, Thousand Cuts), so those lines never fire; against this default in a full raid on 6ee3c30f3 our
Combat swords builds lost 10.6-10.9% (rogue_apl_race, 2026-11-04 00:45). Entries whose builds this rotation beats take it as their base
(`apl`) and their tuned rotations are searched again from it (raid_rogue_1103.sh).
