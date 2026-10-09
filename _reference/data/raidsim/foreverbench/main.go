// foreverbench: run several talent builds through the ElliotWood/Forever (wowsims) simulator with one gear set,
// rotation and encounter, and print DPS per build as JSON lines (with the damage of every action).
//
//	foreverbench --config bench.json
//
// bench.json (paths relative to the simulator repository root):
//
//	{
//	  "class": "ClassMage", "race": "RaceTroll",
//	  "gear": "ui/specs/mage/dps/gear_sets/p1.bis.gear.json",
//	  "apl": "ui/specs/mage/dps/apls/frost.apl.json",
//	  "spec": {"mage": {"options": {"classOptions": {"defaultMageArmor": "MageArmorMageArmor"}}}},
//	  "consumables": {"flaskId": 13512, "foodId": 18254},
//	  "buffs": "full", "profession1": "Engineering", "profession2": "Tailoring",
//	  (buffs: "full" = every raid buff and debuff minus buffs_off / debuffs_off; "self" = only buffs_on / debuffs_on, the class's
//	   own buffs the simulator does not add by itself — the class code still adds its talent auras; "none" = nothing but those auras)
//	  "distanceFromTarget": 20, "inFrontOfTarget": false, "reactionTimeMs": 200,
//	  "iterations": 3000, "duration": 120, "seed": 1,
//	  "builds": [{"label": "opt-frost-raid-raid-dps", "talents": "0502050030003--055500033100030024"}]
//	}
//
// "link": true prints, per build, the simulator's share link instead of simulating: {"label", "link"} where link is the UI's
// URL hash (the IndividualSimSettings proto with the build's gear, talents, rotation, consumables, buffs and encounter, zlib-compressed
// and base64-encoded, as the UI's "copy link" writes it; "api_version" stamps the UI's proto version on it). Open it as
// <site>/<class>/<spec>/#<link> (2026-10-03: the gear-tier pages link every set to the live simulator).
//
// A build may carry its own rotation: "apl" (a path) or "apl_json" (the rotation inline); otherwise the config's "apl" applies.
//
// Output per build: {"label", "talents", "dps", "dps_stdev", "hps", "threat", "oom_seconds", "iterations", "seconds",
// "actions": [{"spellId"|"itemId"|"other", "tag", "damage", "casts", "hits", "pet": true?}, ...]} — damage summed over targets
// and averaged per iteration, player and pet actions.
//
// It is compiled inside the simulator repository (cmd/foreverbench/main.go) by _reference/data/raidsim/setup.py; the
// source of truth is _reference/data/raidsim/foreverbench/main.go in the wow-forever project.
package main

import (
	"bytes"
	"compress/zlib"
	"encoding/base64"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/wowsims/forever/sim"
	"github.com/wowsims/forever/sim/core"
	"github.com/wowsims/forever/sim/core/proto"
	"google.golang.org/protobuf/encoding/protojson"
	gproto "google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protoreflect"
)

type build struct {
	Label   string          `json:"label"`
	Talents string          `json:"talents"`
	APL     string          `json:"apl"`      // optional: this build's own rotation (a path, absolute or relative to --root) ...
	APLJSON json.RawMessage `json:"apl_json"` // ... or the rotation itself inline (raidsim/apl_opt.py scores many variants in one run)
	GearJSON json.RawMessage `json:"gear_json"` // optional: this build's own gear set inline (raidsim/gear_opt.py races gear sets)
	// optional: extra stats added to the character (proto Stat names: "StatSpellDamage", "StatAttackPower", ...), the simulator's
	// own bonus_stats; 2026-10-07: how much spell power a caster needs to match another spec's DPS
	BonusStats map[string]float64 `json:"bonus_stats"`
}

type config struct {
	Class              string          `json:"class"`
	Race               string          `json:"race"`
	Gear               string          `json:"gear"`
	APL                string          `json:"apl"`
	Spec               json.RawMessage `json:"spec"`
	Consumables        json.RawMessage `json:"consumables"`
	Buffs              string          `json:"buffs"`
	BuffsOff           []string        `json:"buffs_off"`   // raid/party/individual buff fields (proto names) cleared from the full set: the spec's own aura is a talent under test
	DebuffsOff         []string        `json:"debuffs_off"` // debuff fields cleared the same way (Winter's Chill for a frost mage, Improved Scorch for fire ...)
	// "self" buffs: the only raid/party/individual buff fields set (proto names -> true, a number or an enum value name): the
	// class's own buffs the simulator does not add itself (a druid's Mark of the Wild, a paladin's blessing on itself, a shaman's water totem)
	BuffsOn   map[string]json.RawMessage `json:"buffs_on"`
	DebuffsOn map[string]json.RawMessage `json:"debuffs_on"` // debuffs the class applies itself (a hunter's Hunter's Mark)
	Profession1        string          `json:"profession1"`
	Profession2        string          `json:"profession2"`
	DistanceFromTarget float64         `json:"distanceFromTarget"`
	InFrontOfTarget    bool            `json:"inFrontOfTarget"`
	ReactionTimeMs     int32           `json:"reactionTimeMs"`
	Iterations         int32           `json:"iterations"`
	Duration           float64         `json:"duration"`
	TargetLevel        int32           `json:"targetLevel"` // 0 = the sim's default raid boss (63); 60 = a training dummy
	NoExecute          bool            `json:"noExecute"`   // no execute phases (a dummy never dies)
	MobType            string          `json:"mobType"`     // the target's creature type (a proto MobType name without its prefix); "" = Elemental, see below
	NumTargets         int             `json:"numTargets"`  // targets in the encounter (2026-10-08, the fight-variety check); 0 or 1 = one
	Atiesh             bool            `json:"atiesh"`      // 2026-10-09: the full raid's four Atiesh auras (off by default: a Naxxramas item)
	Seed               int64           `json:"seed"`
	IsTank             bool            `json:"isTank"`
	// "statweights": true prints, per build, the simulator's stat weights (DPS per point of each stat, weapon DPS as pseudo-stats)
	// instead of a race row (2026-09-30: raidsim/gear_opt.py builds equal-tier gear sets from them)
	StatWeights        bool            `json:"statweights"`
	// "link": true prints each build's share link for the simulator's web UI instead of a race row (see the file header)
	Link       bool  `json:"link"`
	APIVersion int32 `json:"api_version"` // the UI's proto version (proto/common.proto current_version_number) stamped on links
	Builds             []build         `json:"builds"`
}

func init() {
	sim.RegisterAll()
}

func die(format string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, format+"\n", args...)
	os.Exit(1)
}

func readJSON(root, rel string) []byte {
	path := rel
	if !filepath.IsAbs(rel) {
		path = filepath.Join(root, rel)
	}
	data, err := os.ReadFile(path)
	if err != nil {
		die("cannot read %s: %v", rel, err)
	}
	return data
}

func actionRows(actions []*proto.ActionMetrics, iterations int32, pet bool) []map[string]interface{} {
	rows := []map[string]interface{}{}
	for _, am := range actions {
		if am == nil || am.Id == nil {
			continue
		}
		var dmg, thr float64
		var casts, hits int32
		for _, t := range am.Targets {
			dmg += t.Damage
			thr += t.Threat
			casts += t.Casts
			hits += t.Hits
		}
		if dmg <= 0 && thr <= 0 && casts <= 0 { // cast-only actions (cooldowns, buffs, totems) stay: the rotation pages count every cast
			continue
		}
		row := map[string]interface{}{"tag": am.Id.Tag, "damage": dmg / float64(iterations), "threat": thr / float64(iterations), "casts": float64(casts) / float64(iterations),
			"hits": float64(hits) / float64(iterations), "school": am.SpellSchool}
		switch id := am.Id.RawId.(type) {
		case *proto.ActionID_SpellId:
			row["spellId"] = id.SpellId
		case *proto.ActionID_ItemId:
			row["itemId"] = id.ItemId
		case *proto.ActionID_OtherId:
			row["other"] = id.OtherId.String()
		}
		if pet {
			row["pet"] = true
		}
		rows = append(rows, row)
	}
	return rows
}

// clearField resets one field of a buff message by its proto or JSON name; false when the message has no such field.
func clearField(m gproto.Message, name string) bool {
	r := m.ProtoReflect()
	fd := r.Descriptor().Fields().ByName(protoreflect.Name(name))
	if fd == nil {
		fd = r.Descriptor().Fields().ByJSONName(name)
	}
	if fd == nil {
		return false
	}
	r.Clear(fd)
	return true
}

// setField sets one field of a buff or debuff message from a JSON value: true/false, a number, or an enum value name.
func setField(m gproto.Message, name string, raw json.RawMessage) bool {
	r := m.ProtoReflect()
	fd := r.Descriptor().Fields().ByName(protoreflect.Name(name))
	if fd == nil {
		fd = r.Descriptor().Fields().ByJSONName(name)
	}
	if fd == nil {
		return false
	}
	var num float64
	isNum := json.Unmarshal(raw, &num) == nil
	switch fd.Kind() {
	case protoreflect.BoolKind:
		var b bool
		if err := json.Unmarshal(raw, &b); err != nil {
			die("buff %s: %v", name, err)
		}
		r.Set(fd, protoreflect.ValueOfBool(b))
	case protoreflect.EnumKind:
		if isNum {
			r.Set(fd, protoreflect.ValueOfEnum(protoreflect.EnumNumber(int32(num))))
		} else {
			var v string
			if err := json.Unmarshal(raw, &v); err != nil {
				die("buff %s: %v", name, err)
			}
			ev := fd.Enum().Values().ByName(protoreflect.Name(v))
			if ev == nil {
				die("buff %s: no enum value %q", name, v)
			}
			r.Set(fd, protoreflect.ValueOfEnum(ev.Number()))
		}
	case protoreflect.Int32Kind:
		if !isNum {
			die("buff %s: not a number", name)
		}
		r.Set(fd, protoreflect.ValueOfInt32(int32(num)))
	case protoreflect.DoubleKind:
		if !isNum {
			die("buff %s: not a number", name)
		}
		r.Set(fd, protoreflect.ValueOfFloat64(num))
	default:
		die("buff %s: unsupported field kind %s", name, fd.Kind())
	}
	return true
}

func main() {
	cfgPath := flag.String("config", "bench.json", "bench config (see the file header)")
	root := flag.String("root", ".", "simulator repository root that gear/apl paths are relative to")
	flag.Parse()
	raw, err := os.ReadFile(*cfgPath)
	if err != nil {
		die("cannot read config: %v", err)
	}
	var cfg config
	if err := json.Unmarshal(raw, &cfg); err != nil {
		die("bad config: %v", err)
	}
	unmarshal := protojson.UnmarshalOptions{DiscardUnknown: true}
	equipment := &proto.EquipmentSpec{}
	if cfg.Gear != "" {
		if err := unmarshal.Unmarshal(readJSON(*root, cfg.Gear), equipment); err != nil {
			die("bad gear set %s: %v", cfg.Gear, err)
		}
	}
	rotation := &proto.APLRotation{}
	if cfg.APL != "" {
		if err := unmarshal.Unmarshal(readJSON(*root, cfg.APL), rotation); err != nil {
			die("bad apl %s: %v", cfg.APL, err)
		}
	}
	consumables := &proto.ConsumesSpec{}
	// 2026-10-09: Forever lets temporary enchants stack with poisons, shaman imbues and the warlock's Firestone/Spellstone imbues; the
	// simulator has one consumable enchant per hand, so "extraMhImbueId" / "extraOhImbueId" in the consumables go to the patched core
	// through WOW_FOREVER_EXTRA_IMBUES (patches/forever/sim/core/forever_rules_patch.go foreverExtraImbues) and are removed here.
	if len(cfg.Consumables) > 0 {
		var raw map[string]json.RawMessage
		if json.Unmarshal(cfg.Consumables, &raw) == nil {
			var extra []string
			for _, kv := range [][2]string{{"extraMhImbueId", "mh"}, {"extraOhImbueId", "oh"}} {
				if v, ok := raw[kv[0]]; ok {
					extra = append(extra, kv[1]+":"+strings.TrimSpace(string(v)))
					delete(raw, kv[0])
				}
			}
			if len(extra) > 0 {
				os.Setenv("WOW_FOREVER_EXTRA_IMBUES", strings.Join(extra, ","))
				cfg.Consumables, _ = json.Marshal(raw)
			}
		}
	}
	if len(cfg.Consumables) > 0 {
		if err := unmarshal.Unmarshal(cfg.Consumables, consumables); err != nil {
			die("bad consumables: %v", err)
		}
	}
	// The simulator registers the chosen potion and conjured item (potId, conjuredId) only when they are also in the lists the
	// UI sends with every run (all eligible potions and conjured items: sim/core/consumes.go registerPotionCD and
	// registerConjuredCD). A config names one of each, so it goes into its list here; before 2026-09-28 no run of this bench
	// used a potion, a Demonic Rune or Thistle Tea.
	if consumables.PotId != 0 && !containsID(consumables.Potions, consumables.PotId) {
		consumables.Potions = append(consumables.Potions, consumables.PotId)
	}
	if consumables.ConjuredId != 0 && !containsID(consumables.ConjuredItems, consumables.ConjuredId) {
		consumables.ConjuredItems = append(consumables.ConjuredItems, consumables.ConjuredId)
	}
	classID, ok := proto.Class_value[cfg.Class]
	if !ok {
		die("unknown class %q", cfg.Class)
	}
	raceID, ok := proto.Race_value[cfg.Race]
	if !ok {
		die("unknown race %q", cfg.Race)
	}
	prof := func(name string, fallback proto.Profession) proto.Profession {
		if name == "" {
			return fallback
		}
		v, ok := proto.Profession_value[name]
		if !ok {
			die("unknown profession %q", name)
		}
		return proto.Profession(v)
	}
	if cfg.Iterations == 0 {
		cfg.Iterations = 2000
	}
	if cfg.Duration == 0 {
		cfg.Duration = 120
	}
	reaction := cfg.ReactionTimeMs
	if reaction == 0 {
		reaction = 200
	}
	for _, b := range cfg.Builds {
		player := &proto.Player{}
		if len(cfg.Spec) > 0 {
			if err := unmarshal.Unmarshal(cfg.Spec, player); err != nil {
				die("bad spec fragment: %v", err)
			}
		}
		player.Class = proto.Class(classID)
		player.Race = proto.Race(raceID)
		player.Equipment = equipment
		player.Consumables = consumables
		player.TalentsString = b.Talents
		player.Profession1 = prof(cfg.Profession1, proto.Profession_Engineering)
		player.Profession2 = prof(cfg.Profession2, proto.Profession_ProfessionUnknown)
		player.Rotation = rotation
		if len(b.BonusStats) > 0 {
			st := make([]float64, len(proto.Stat_name))
			for k, v := range b.BonusStats {
				idx, ok := proto.Stat_value[k]
				if !ok {
					die("unknown stat %q in bonus_stats (proto Stat names, e.g. StatSpellDamage)", k)
				}
				st[idx] = v
			}
			player.BonusStats = &proto.UnitStats{Stats: st}
		}
		if len(b.GearJSON) > 0 {
			own := &proto.EquipmentSpec{}
			if err := unmarshal.Unmarshal(b.GearJSON, own); err != nil {
				fmt.Printf("{\"label\": %q, \"error\": %q}\n", b.Label, "bad gear: "+err.Error())
				continue
			}
			player.Equipment = own
		}
		if len(b.APLJSON) > 0 || b.APL != "" {
			own := &proto.APLRotation{}
			src := []byte(b.APLJSON)
			if len(src) == 0 {
				src = readJSON(*root, b.APL)
			}
			if err := unmarshal.Unmarshal(src, own); err != nil {
				fmt.Printf("{\"label\": %q, \"error\": %q}\n", b.Label, "bad apl: "+err.Error())
				continue
			}
			player.Rotation = own
		}
		player.ReactionTimeMs = reaction
		player.ChannelClipDelayMs = 50
		player.DistanceFromTarget = cfg.DistanceFromTarget
		player.InFrontOfTarget = cfg.InFrontOfTarget
		var raid *proto.Raid
		if cfg.Buffs == "none" {
			player.Buffs = &proto.IndividualBuffs{}
			raid = core.SinglePlayerRaidProto(player, &proto.PartyBuffs{}, &proto.RaidBuffs{}, &proto.Debuffs{})
		} else if cfg.Buffs == "self" { // a training dummy: only the buffs the class brings itself
			party, raidBuffs, indiv, debuffs := &proto.PartyBuffs{}, &proto.RaidBuffs{}, &proto.IndividualBuffs{}, &proto.Debuffs{}
			for n, v := range cfg.BuffsOn {
				if !setField(raidBuffs, n, v) && !setField(party, n, v) && !setField(indiv, n, v) {
					die("buffs_on: no raid, party or individual buff field %q", n)
				}
			}
			for n, v := range cfg.DebuffsOn {
				if !setField(debuffs, n, v) {
					die("debuffs_on: no debuff field %q", n)
				}
			}
			player.Buffs = indiv
			raid = core.SinglePlayerRaidProto(player, party, raidBuffs, debuffs)
		} else {
			party, raidBuffs, indiv := gproto.Clone(core.FullPartyBuffs).(*proto.PartyBuffs), gproto.Clone(core.FullRaidBuffs).(*proto.RaidBuffs), gproto.Clone(core.FullIndividualBuffs).(*proto.IndividualBuffs)
			// 2026-10-09: the fork's full party (core.FullPartyBuffs) carries all four Atiesh auras (+33 spell damage, +2% spell
			// crit, +62 healing, +11 mp5 for the party). Atiesh is Naxxramas's legendary, in no announced Forever phase, so the
			// full raid leaves it out unless the config says "atiesh": true (comparisons with older runs).
			if !cfg.Atiesh {
				party.AtieshDruid, party.AtieshMage, party.AtieshPriest, party.AtieshWarlock = 0, 0, 0, 0
			}
			for _, n := range cfg.BuffsOff {
				if !clearField(raidBuffs, n) && !clearField(party, n) && !clearField(indiv, n) {
					die("buffs_off: no raid, party or individual buff field %q", n)
				}
			}
			debuffs := gproto.Clone(core.FullDebuffs).(*proto.Debuffs)
			for _, n := range cfg.DebuffsOff {
				if !clearField(debuffs, n) {
					die("debuffs_off: no debuff field %q", n)
				}
			}
			player.Buffs = indiv
			raid = core.SinglePlayerRaidProto(player, party, raidBuffs, debuffs)
		}
		if cfg.IsTank {
			raid.Tanks = append(raid.Tanks, &proto.UnitReference{Type: proto.UnitReference_Player, Index: 0})
		}
		encounter := core.MakeSingleTargetEncounter(0)
		encounter.Duration = cfg.Duration
		// The target's creature type (2026-10-06): the sim's default target has none (the UI's preset is Mechanical), so every effect
		// keyed on it read 0 in our runs, above all a hunter's Improved Tracking (+5% against every raid creature type but Mechanical).
		// Elemental by default (Ragnaros, Garr, Baron Geddon): tracked by hunters, but neither Humanoid/Giant (Murder: hand-valued in
		// specs.json), Undead/Demon (Exorcism, Holy Wrath, the Scourge items) nor Giant/Dragonkin (Spearing Strike), which stay off as
		// before. "mobType" in the config overrides ("Unknown" reproduces runs from before this date).
		tgt := gproto.Clone(encounter.Targets[0]).(*proto.Target)
		mobType := cfg.MobType
		if mobType == "" {
			mobType = "Elemental"
		}
		if v, ok := proto.MobType_value["MobType"+mobType]; ok {
			tgt.MobType = proto.MobType(v)
		} else {
			die("mobType: no creature type %q (Elemental, Beast, Humanoid, Undead, Demon, Dragonkin, Giant, Mechanical, Unknown ...)", mobType)
		}
		if cfg.TargetLevel > 0 {
			tgt.Level = cfg.TargetLevel
		}
		encounter.Targets = []*proto.Target{tgt}
		for i := 1; i < cfg.NumTargets; i++ { // several identical targets (cleave and area fights)
			encounter.Targets = append(encounter.Targets, gproto.Clone(tgt).(*proto.Target))
		}
		if cfg.NoExecute { // every execute_proportion_* field to zero (the two sims have different sets of them)
			er := encounter.ProtoReflect()
			fds := er.Descriptor().Fields()
			for i := 0; i < fds.Len(); i++ {
				if strings.HasPrefix(string(fds.Get(i).Name()), "execute_proportion") {
					er.Clear(fds.Get(i))
				}
			}
		}
		if cfg.Link {
			settings := &proto.IndividualSimSettings{
				Settings:  &proto.SimSettings{Iterations: cfg.Iterations},
				RaidBuffs: raid.Buffs, PartyBuffs: raid.Parties[0].Buffs, Debuffs: raid.Debuffs,
				Player: raid.Parties[0].Players[0], Encounter: encounter, Tanks: raid.Tanks,
			}
			if cfg.APIVersion > 0 { // by name: the classic simulator's settings have no api_version field
				if fd := settings.ProtoReflect().Descriptor().Fields().ByName("api_version"); fd != nil {
					settings.ProtoReflect().Set(fd, protoreflect.ValueOfInt32(cfg.APIVersion))
				}
			}
			out := map[string]interface{}{"label": b.Label}
			if bin, err := gproto.Marshal(settings); err != nil {
				out["error"] = err.Error()
			} else {
				var buf bytes.Buffer
				zw := zlib.NewWriter(&buf) // the zlib wrapper: the UI reads links with pako.inflate
				zw.Write(bin)
				zw.Close()
				out["link"] = base64.StdEncoding.EncodeToString(buf.Bytes())
			}
			line, _ := json.Marshal(out)
			fmt.Println(string(line))
			continue
		}
		if cfg.StatWeights {
			pl := raid.Parties[0].Players[0]
			swr := &proto.StatWeightsRequest{
				Player: pl, RaidBuffs: raid.Buffs, PartyBuffs: raid.Parties[0].Buffs, Debuffs: raid.Debuffs, Encounter: encounter,
				SimOptions:   &proto.SimOptions{Iterations: cfg.Iterations, RandomSeed: cfg.Seed},
				EpReferenceStat: proto.Stat_StatAttackPower, Tanks: raid.Tanks,
			}
			for i := 0; i < int(proto.Stat_StatPhysicalDamage); i++ {
				// damage builds: the offensive stats only (Strength .. Armor Penetration, Spirit, Intellect); tanks: everything
				if cfg.IsTank || i <= int(proto.Stat_StatArmorPenetration) {
					if !cfg.IsTank && (i == int(proto.Stat_StatStamina) || i == int(proto.Stat_StatHealingPower)) {
						continue
					}
					swr.StatsToWeigh = append(swr.StatsToWeigh, proto.Stat(i))
				}
			}
			swr.PseudoStatsToWeigh = []proto.PseudoStat{proto.PseudoStat_PseudoStatMainHandDps, proto.PseudoStat_PseudoStatOffHandDps, proto.PseudoStat_PseudoStatRangedDps}
			t0 := time.Now()
			res := core.StatWeights(swr)
			if res.Error != nil {
				fmt.Printf("{\"label\": %q, \"error\": %q}\n", b.Label, res.Error.Message)
				continue
			}
			pick := res.Dps
			if cfg.IsTank {
				pick = res.Tps
			}
			w := map[string]float64{}
			for i, v := range pick.Weights.Stats {
				w[proto.Stat(i).String()] = v
			}
			for i, v := range pick.Weights.PseudoStats {
				w[proto.PseudoStat(i).String()] = v
			}
			out := map[string]interface{}{"label": b.Label, "weights": w, "seconds": time.Since(t0).Seconds()}
			if cfg.IsTank { // tanks: threat per point, and damage taken per point (lower is better)
				d := map[string]float64{}
				for i, v := range res.Dtps.Weights.Stats {
					d[proto.Stat(i).String()] = v
				}
				out["dtps_weights"] = d
			}
			line, _ := json.Marshal(out)
			fmt.Println(string(line))
			continue
		}
		request := &proto.RaidSimRequest{
			Raid:       raid,
			Encounter:  encounter,
			SimOptions: &proto.SimOptions{Iterations: cfg.Iterations, RandomSeed: cfg.Seed},
		}
		t0 := time.Now()
		result := core.RunRaidSimConcurrent(request)
		if result.Error != nil {
			fmt.Printf("{\"label\": %q, \"error\": %q}\n", b.Label, result.Error.Message)
			continue
		}
		pm := result.RaidMetrics.Parties[0].Players[0]
		actions := actionRows(pm.Actions, cfg.Iterations, false)
		for _, pet := range pm.Pets {
			actions = append(actions, actionRows(pet.Actions, cfg.Iterations, true)...)
		}
		out := map[string]interface{}{
			"label": b.Label, "talents": b.Talents,
			"dps": pm.Dps.Avg, "dps_stdev": pm.Dps.Stdev, "hps": pm.Hps.Avg, "threat": pm.Threat.Avg,
			"dtps": pm.Dtps.Avg, "dtps_stdev": pm.Dtps.Stdev, "tmi": pm.Tmi.Avg, "tto": pm.Tto.Avg,
			"oom_seconds": pm.SecondsOomAvg, "iterations": cfg.Iterations, "seconds": time.Since(t0).Seconds(),
			"actions": actions,
		}
		line, _ := json.Marshal(out)
		fmt.Println(string(line))
	}
}

func containsID(ids []int32, id int32) bool {
	for _, x := range ids {
		if x == id {
			return true
		}
	}
	return false
}
