// foreverbench: run several talent builds through the official WoW Forever simulator (github.com/wowsims/forever since 2026-10-18;
// the ElliotWood/Forever fork before) with one gear set,
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
	"runtime"
	"strings"
	"sync"
	"time"

	"github.com/wowsims/forever/assets/database"
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
	// "spells": true prints, per build, the spell and aura ids the character (and its pets) registers, instead of a race row
	// (2026-10-18, the port: the official simulator registers one rank per spell, so rotations naming another rank cast nothing;
	// raidsim/apl_remap.py rewrites them from this list)
	Spells bool `json:"spells"`
	// "validate": true prints, per build, the rotation's validation messages by priority-list and prepull index (the simulator's own
	// APL checks: an unknown spell or aura, a condition it cannot resolve and treats as always true), instead of a race row
	Validate bool `json:"validate"`
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

// fieldAliases: raid buff fields upstream renamed at the 2026-11-01 rank work (b6657d382: the group buffs became one input reading the
// single-target spell's top rank, whose amounts match the group spell's top rank), so specs.json and run.py run on both sides of the re-pin.
var fieldAliases = map[string]string{
	"gift_of_the_wild": "mark_of_the_wild", "mark_of_the_wild": "gift_of_the_wild",
	"prayer_of_fortitude": "power_word_fortitude", "power_word_fortitude": "prayer_of_fortitude",
	"arcane_brilliance": "arcane_intellect", "arcane_intellect": "arcane_brilliance",
	"prayer_of_shadow_protection": "shadow_protection", "shadow_protection": "prayer_of_shadow_protection",
}

// setField sets one field of a buff or debuff message from a JSON value: true/false, a number, or an enum value name.
// A rank select (int32 since b6657d382: 0 off, 1 the trainer's top rank, 2+ book ranks) takes true as 1 and false as 0, and a bool
// field takes a number as on (non-zero) or off, so a config written for either side of that change reads the same.
func setField(m gproto.Message, name string, raw json.RawMessage) bool {
	r := m.ProtoReflect()
	fd := r.Descriptor().Fields().ByName(protoreflect.Name(name))
	if fd == nil {
		fd = r.Descriptor().Fields().ByJSONName(name)
	}
	if fd == nil {
		if alt, ok := fieldAliases[name]; ok {
			fd = r.Descriptor().Fields().ByName(protoreflect.Name(alt))
		}
	}
	if fd == nil {
		return false
	}
	var num float64
	isNum := json.Unmarshal(raw, &num) == nil
	var flag bool
	isBool := json.Unmarshal(raw, &flag) == nil
	switch fd.Kind() {
	case protoreflect.BoolKind:
		if isNum {
			r.Set(fd, protoreflect.ValueOfBool(num != 0))
			break
		}
		if !isBool {
			die("buff %s: not true/false", name)
		}
		r.Set(fd, protoreflect.ValueOfBool(flag))
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
		if !isNum && isBool {
			num = 0
			if flag {
				num = 1
			}
		} else if !isNum {
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
	gearMissing := officialGear(equipment)
	// Consumables (2026-10-18, the port to wowsims/forever): the official simulator's ConsumesSpec names item ids only (flask, food,
	// elixirs as a list, the stone or oil and the poison/firestone/spellstone of each hand apart, potions by class for the APL's
	// potion placeholders). specs.json keeps the fork's fields, translated here (legacyConsumables); the fork's imbue ids that were
	// enchant or spell ids map onto the items (legacyImbueItems). Forever's stacking of a stone or oil with a poison or stone imbue is
	// native there: "extraMhImbueId" / "extraOhImbueId" become the other half of the hand.
	consumables, potPlaceholder := legacyConsumables(cfg.Consumables)
	rotation := &proto.APLRotation{}
	if cfg.APL != "" {
		if err := unmarshal.Unmarshal(legacyAPL(readJSON(*root, cfg.APL), potPlaceholder), rotation); err != nil {
			die("bad apl %s: %v", cfg.APL, err)
		}
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
	if len(cfg.Spec) > 0 {
		cfg.Spec = legacySpec(cfg.Spec)
	}
	// Builds in parallel (2026-10-24 audit): with several builds the sims run side by side, one build per thread (core.RunRaidSim), instead
	// of one build at a time split over every thread and waiting for the slowest split (12 one-fight splits of a build took 12-83 ms under
	// load, one fight 3 ms). The iterations and their seeds are the same (a split starts at RandomSeed + the iterations before it), so
	// the results match up to the order of the floating-point sums. Lines are printed in the config's order. WOW_FOREVER_BENCH_SPLIT=1
	// keeps the old way.
	var jobs []simJob
	parallel := len(cfg.Builds) > 1 && os.Getenv("WOW_FOREVER_BENCH_SPLIT") != "1"
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
		missing := gearMissing
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
			missing = officialGear(own)
		}
		if len(b.APLJSON) > 0 || b.APL != "" {
			own := &proto.APLRotation{}
			src := []byte(b.APLJSON)
			if len(src) == 0 {
				src = readJSON(*root, b.APL)
			}
			if err := unmarshal.Unmarshal(legacyAPL(src, potPlaceholder), own); err != nil {
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
			if cfg.IsTank { // 2026-10-18 (audit 2 row 63): a tank gets the simulator's tank set, without Blessing of Salvation's -30% threat
				indiv = gproto.Clone(core.FullTankIndividualBuffs).(*proto.IndividualBuffs)
			}
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
		if cfg.Validate {
			res := core.ComputeStats(&proto.ComputeStatsRequest{Raid: raid, Encounter: encounter})
			out := map[string]interface{}{"label": b.Label}
			if res.ErrorResult != "" {
				out["error"] = res.ErrorResult
			} else if rs := res.RaidStats.Parties[0].Players[0].RotationStats; rs != nil {
				collect := func(list []*proto.APLActionStats) map[string][]string {
					m := map[string][]string{}
					for i, a := range list {
						for _, v := range a.Validations {
							m[fmt.Sprint(i)] = append(m[fmt.Sprint(i)], v.LogLevel.String()+": "+v.Validation)
						}
					}
					return m
				}
				out["priority"] = collect(rs.PriorityList)
				out["prepull"] = collect(rs.PrepullActions)
			}
			line, _ := json.Marshal(out)
			fmt.Println(string(line))
			continue
		}
		if cfg.Spells {
			env, _, _ := core.NewEnvironment(raid, encounter, false, false)
			ch := env.Raid.Parties[0].Players[0].GetCharacter()
			list := func(u *core.Unit) (spells []int32, auras []map[string]interface{}) {
				for _, s := range u.Spellbook {
					if id := s.ActionID.SpellID; id != 0 {
						spells = append(spells, id)
					}
				}
				for _, a := range u.GetAuras() {
					auras = append(auras, map[string]interface{}{"label": a.Label, "spellId": a.ActionID.SpellID, "itemId": a.ActionID.ItemID})
				}
				return
			}
			sp, au := list(&ch.Unit)
			out := map[string]interface{}{"label": b.Label, "spells": sp, "auras": au}
			var pets []map[string]interface{}
			for _, pet := range ch.Pets {
				ps, pa := list(&pet.Unit)
				pets = append(pets, map[string]interface{}{"name": pet.Label, "spells": ps, "auras": pa})
			}
			out["pets"] = pets
			var targetAuras []map[string]interface{}
			for _, tu := range env.Encounter.AllTargetUnits {
				_, ta := list(tu)
				targetAuras = append(targetAuras, ta...)
			}
			out["target_auras"] = targetAuras
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
				// damage builds: the offensive stats only (Strength .. Expertise, Spirit, Intellect); tanks: everything. Expertise was left out
				// until 2026-10-16, so gear picked by these weights scored it at zero (Adaptive Combat Assistant, +20 Expertise)
				if cfg.IsTank || i <= int(proto.Stat_StatExpertiseRating) {
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
		job := simJob{label: b.Label, talents: b.Talents, request: request, missing: missing, iterations: cfg.Iterations}
		if parallel {
			jobs = append(jobs, job)
			continue
		}
		fmt.Println(job.run(false))
	}
	if len(jobs) > 0 {
		lines := make([]string, len(jobs))
		next := make(chan int)
		var wg sync.WaitGroup
		for w := 0; w < min(runtime.NumCPU(), len(jobs)); w++ {
			wg.Add(1)
			go func() {
				defer wg.Done()
				for i := range next {
					lines[i] = jobs[i].run(true)
				}
			}()
		}
		for i := range jobs {
			next <- i
		}
		close(next)
		wg.Wait()
		for _, ln := range lines {
			fmt.Println(ln)
		}
	}
}

type simJob struct {
	label, talents string
	request        *proto.RaidSimRequest
	missing        []string
	iterations     int32
}

// run simulates the build and returns its output line: on one thread (single) or split over every thread.
func (j simJob) run(single bool) string {
	t0 := time.Now()
	var result *proto.RaidSimResult
	if single {
		result = core.RunRaidSim(gproto.Clone(j.request).(*proto.RaidSimRequest))
	} else {
		result = core.RunRaidSimConcurrent(j.request)
	}
	if result.Error != nil {
		return fmt.Sprintf("{\"label\": %q, \"error\": %q}", j.label, result.Error.Message)
	}
	pm := result.RaidMetrics.Parties[0].Players[0]
	actions := actionRows(pm.Actions, j.iterations, false)
	for _, pet := range pm.Pets {
		actions = append(actions, actionRows(pet.Actions, j.iterations, true)...)
	}
	out := map[string]interface{}{
		"label": j.label, "talents": j.talents,
		"dps": pm.Dps.Avg, "dps_stdev": pm.Dps.Stdev, "hps": pm.Hps.Avg, "threat": pm.Threat.Avg,
		"dtps": pm.Dtps.Avg, "dtps_stdev": pm.Dtps.Stdev, "tmi": pm.Tmi.Avg, "tto": pm.Tto.Avg,
		"oom_seconds": pm.SecondsOomAvg, "iterations": j.iterations, "seconds": time.Since(t0).Seconds(),
		"actions": actions,
	}
	if len(j.missing) > 0 {
		out["missing_gear"] = j.missing
	}
	line, _ := json.Marshal(out)
	return string(line)
}

func containsID(ids []int32, id int32) bool {
	for _, x := range ids {
		if x == id {
			return true
		}
	}
	return false
}

// legacyImbueItems: the ElliotWood/Forever fork's imbue ids (enchant or spell ids) -> the official simulator's item ids.
var legacyImbueItems = map[int32]int32{
	25122: 20749, // Brilliant Wizard Oil
	25123: 20748, // Brilliant Mana Oil (the fork's "Mana Oil")
	25121: 20750, // Wizard Oil
	28898: 23123, // Blessed Wizard Oil
	22756: 18262, // Elemental Sharpening Stone
	28891: 23122, // Consecrated Sharpening Stone
	16138: 12404, // Dense Sharpening Stone
	16622: 12643, // Dense Weightstone
	26891: 8928,  // Instant Poison (the fork's top rank) -> Instant Poison VI
	27186: 20844, // Deadly Poison (the fork's top rank) -> Deadly Poison V
}

// legacyItems: the fork's boolean consumables -> item ids.
var legacyItems = map[string]int32{
	"goblinSapper": 10646, // Goblin Sapper Charge
}

// legacyConsumables translates a config's consumables (the fork's ConsumesSpec fields as JSON) into the official ConsumesSpec, and
// returns the APL potion placeholder the configured potion fills ("" when no potion): the fork's rotations cast "OtherActionPotion",
// which the official simulator split by potion class.
func legacyConsumables(raw json.RawMessage) (*proto.ConsumesSpec, string) {
	out := &proto.ConsumesSpec{}
	if len(raw) == 0 {
		return out, ""
	}
	var m map[string]json.RawMessage
	if err := json.Unmarshal(raw, &m); err != nil {
		die("bad consumables: %v", err)
	}
	num := func(k string) int32 {
		v, ok := m[k]
		if !ok {
			return 0
		}
		var f float64
		if json.Unmarshal(v, &f) != nil {
			var b bool
			if json.Unmarshal(v, &b) == nil && b {
				if id, ok := legacyItems[k]; ok {
					return id
				}
			}
			return 0
		}
		return int32(f)
	}
	known := func(id int32, what string) bool {
		if id == 0 {
			return false
		}
		if core.GetConsumableByID(id).Id == 0 {
			fmt.Fprintf(os.Stderr, "consumables: %s %d is not in the simulator's catalogue: left out\n", what, id)
			return false
		}
		return true
	}
	// one-per-kind fields that keep their meaning
	if id := num("flaskId"); known(id, "flaskId") {
		out.FlaskId = id
	}
	if id := num("foodId"); known(id, "foodId") {
		out.FoodId = id
	}
	if id := num("explosiveId"); known(id, "explosiveId") {
		out.ExplosiveId = id
	}
	if id := num("conjuredId"); known(id, "conjuredId") {
		out.ConjuredId = id
		out.ConjuredItems = append(out.ConjuredItems, id)
	}
	// elixirs and the other stacking buffs: elixirs go to elixir_ids, the rest to extra_ids (the simulator keeps one per exclusive group)
	for _, k := range []string{"battleElixirId", "guardianElixirId", "schoolElixirId", "spellPowerElixirId", "defenseElixirId",
		"strengthBuffId", "attackPowerBuffId", "zanzaId", "alcoholId", "goblinSapper", "dragonbreathChili"} {
		id := num(k)
		if k == "dragonbreathChili" { // the official catalogue has no Dragonbreath Chili (2026-10-18): dropped with a note
			if _, ok := m[k]; ok {
				fmt.Fprintln(os.Stderr, "consumables: dragonbreathChili is not in the simulator's catalogue: left out")
			}
			continue
		}
		if !known(id, k) {
			continue
		}
		if core.GetConsumableByID(id).Type == proto.ConsumableType_ConsumableTypeElixir {
			out.ElixirIds = append(out.ElixirIds, id)
		} else {
			out.ExtraIds = append(out.ExtraIds, id)
		}
	}
	// weapons: each hand carries one stone or oil (type Imbue) and one poison/firestone/spellstone (type WeaponImbue)
	hand := func(keys []string, stone, imbue *int32) {
		for _, k := range keys {
			id := num(k)
			if mapped, ok := legacyImbueItems[id]; ok {
				id = mapped
			}
			if !known(id, k) {
				continue
			}
			switch core.GetConsumableByID(id).Type {
			case proto.ConsumableType_ConsumableTypeWeaponImbue:
				*imbue = id
			default:
				*stone = id
			}
		}
	}
	hand([]string{"mhImbueId", "extraMhImbueId"}, &out.MhImbueId, &out.MhWeaponImbueId)
	hand([]string{"ohImbueId", "extraOhImbueId"}, &out.OhImbueId, &out.OhWeaponImbueId)
	// the potion fills the placeholder of its class: offensive first (Mighty Rage Potion is resource and offensive), then resource
	placeholder := ""
	if id := num("potId"); known(id, "potId") {
		classes := map[int32]bool{}
		for _, c := range consumablePotionClasses(id) {
			classes[int32(c)] = true
		}
		switch {
		case classes[int32(proto.PotionClass_PotionClassOffensive)]:
			out.OffensivePotId, placeholder = id, "OtherActionOffensivePotion"
		case classes[int32(proto.PotionClass_PotionClassResource)]:
			out.ResourcePotId, placeholder = id, "OtherActionResourcePotion"
		default:
			out.DefensivePotId, placeholder = id, "OtherActionDefensivePotion"
		}
		out.Potions = append(out.Potions, id)
	}
	for k := range m {
		switch k {
		case "flaskId", "foodId", "explosiveId", "conjuredId", "battleElixirId", "guardianElixirId", "schoolElixirId", "spellPowerElixirId",
			"defenseElixirId", "strengthBuffId", "attackPowerBuffId", "zanzaId", "alcoholId", "goblinSapper", "dragonbreathChili",
			"mhImbueId", "extraMhImbueId", "ohImbueId", "extraOhImbueId", "potId":
		default:
			fmt.Fprintf(os.Stderr, "consumables: unknown field %q left out\n", k)
		}
	}
	return out, placeholder
}

// legacySpec translates the fork's spec options the official protos lack (2026-10-22, sim-port.md open item 8). The spec fragment
// is read with DiscardUnknown, so a fork-only field was dropped without a word: the warlock's "sacrificeSummon" (Demonic Sacrifice
// before the pull, no demon out) and "pactSacrifice" (with Demonic Pact, the demon sacrificed while `summon` is out) are the
// official WarlockOptions.sacrificed_demon. Until then every Demonic Sacrifice entry ran without the sacrifice and with the Imp out
// (warlock sb-raid smoke build: 542.7 dummy DPS, 591.0 with the sacrifice). With "pactSacrifice", a build that has Demonic Sacrifice
// but not Demonic Pact now sacrifices that demon and has none out (the official resolveSacrifice), where the fork kept `summon`
// out without the buff. Any other field the official protos do not know is reported on stderr.
func legacySpec(raw json.RawMessage) json.RawMessage {
	var m map[string]interface{}
	if json.Unmarshal(raw, &m) != nil {
		return raw
	}
	if wl, ok := m["warlock"].(map[string]interface{}); ok {
		if opts, ok := wl["options"].(map[string]interface{}); ok {
			if co, ok := opts["classOptions"].(map[string]interface{}); ok {
				if sac, ok := co["sacrificeSummon"].(bool); ok {
					delete(co, "sacrificeSummon")
					if sac {
						if summon, ok := co["summon"]; ok {
							co["sacrificedDemon"] = summon
						}
						co["summon"] = "NoSummon"
					}
				}
				if pact, ok := co["pactSacrifice"]; ok {
					delete(co, "pactSacrifice")
					co["sacrificedDemon"] = pact
				}
			}
		}
	}
	out, err := json.Marshal(m)
	if err != nil {
		return raw
	}
	if err := protojson.Unmarshal(out, &proto.Player{}); err != nil {
		fmt.Fprintf(os.Stderr, "spec: the simulator ignores part of the spec fragment: %v\n", err)
	}
	return out
}

// legacyAPL rewrites the fork's generic potion action into the official placeholder of the configured potion's class.
func legacyAPL(src []byte, placeholder string) []byte {
	if placeholder == "" {
		placeholder = "OtherActionOffensivePotion" // no potion configured: the placeholder casts nothing
	}
	return bytes.ReplaceAll(src, []byte(`"OtherActionPotion"`), []byte(`"`+placeholder+`"`))
}

var uiConsumables map[int32]*proto.Consumable

// consumablePotionClasses: the potion classes the official database gives a consumable (core.Consumable does not carry them).
func consumablePotionClasses(id int32) []proto.PotionClass {
	if uiConsumables == nil {
		uiConsumables = map[int32]*proto.Consumable{}
		for _, c := range database.Load().Consumables {
			uiConsumables[c.Id] = c
		}
	}
	if c, ok := uiConsumables[id]; ok {
		return c.GetPotionClasses()
	}
	return nil
}

// officialGear removes from a gear set the items and enchants the official simulator's database does not have, and returns them
// ("item:<id>", "enchant:<id>"). 2026-10-18, the port to wowsims/forever: its database comes from Forever's game files, and 159 items
// of our gear sets (built on the ElliotWood/Forever fork's database: Blackhand's Breadth, Band of Accuria, the Molten Core tier sets ...)
// are not in them (Wowhead's Forever database does not list them either); the simulator panics on an unknown item. A run that lost
// gear reports it in "missing_gear": its numbers are not comparable until the set is re-made from the official database.
func officialGear(eq *proto.EquipmentSpec) []string {
	var missing []string
	for i, it := range eq.Items {
		if it == nil || it.Id == 0 {
			continue
		}
		if core.GetItemByID(it.Id) == nil {
			missing = append(missing, fmt.Sprintf("item:%d", it.Id))
			eq.Items[i] = &proto.ItemSpec{}
			continue
		}
		if it.Enchant != 0 && core.GetEnchantByEffectID(it.Enchant) == nil {
			missing = append(missing, fmt.Sprintf("enchant:%d", it.Enchant))
			it.Enchant = 0
		}
	}
	return missing
}
