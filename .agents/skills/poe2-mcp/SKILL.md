---
name: poe2-mcp
description: Use the two PoE2 MCP servers (poe2-build and poe2-optimizer) to analyze builds, passive tree, gems, item mods, and crafting for a Monk Invoker or any PoE2 character. Use when: analyzing a specific build from PoB code, searching for passive tree upgrades, inspecting gem synergies, checking item mods, or getting crafting advice.
---

# poe2-mcp

> Adapted for project: Monk Invoker — c:\Micro_Projrcts\Poe2
> Servers: `poe2-build` (deepwa7er) + `poe2-optimizer` (HivemindOverlord)

## Two Servers, Two Roles

| Server | Role | Best for |
|--------|------|----------|
| `poe2-build` | PoB-centric analysis | Load a specific build, analyze stats/passives/items, crafting, vendor regex |
| `poe2-optimizer` | Game-data layer (40 tools) | Passive tree data, gem inspection, item mods DB, mechanic lookup |

**Rule:** `poe2-optimizer` is the data layer — it returns facts. You synthesize recommendations yourself.

---

## poe2-build — Tool Reference

All tools below operate on the **currently loaded build** (load first with `load_build` or `load_my_character`).

### Load a build
```
load_build(pob_code="...")          # from PoB: File → Share → Copy code
load_my_character(name="CharName")  # loads from poe.ninja (profile must be public)
list_my_characters()                # list all your characters
```

### Analyze the loaded build
```
get_stats()             # life, mana, DPS, resistances, etc.
get_passives()          # allocated passive nodes + stat descriptions
get_items()             # equipped items and their mods
get_skills()            # skill socket groups and gem links
get_point_budget()      # passive/ascendancy point usage summary
analyze_defenses()      # uncapped resistances, health pool sanity check
```

### Passive tree exploration (Monk filter!)
```
search_tree("lightning", classes=["Monk"])       # keyword search — Monk region only
search_tree("attack speed", classes=["Monk"])
get_reachable_nodes(max_distance=5, classes=["Monk"])   # unallocated nodes within N steps
get_node(node_id=...)                            # inspect single node + neighbors
path_to_node(target_node_id=...)                 # shortest path + point cost
search_passives("mana")                          # search only ALLOCATED nodes
```

Valid class names for filter: `Druid`, `Huntress`, `Mercenary`, `Monk`, `Sorceress`, `Warrior`

### Crafting
```
list_mods_for_base("Two-Handed Staff", keyword="attack speed")
craft_advisor(target="lightning damage", slot="Gloves")
generate_vendor_regex(slot="Boots")              # vendor search regex, 50-char budget
```

### Meta / community builds
```
get_meta_overview()                              # ascendancy popularity from poe.ninja
list_top_builds(limit=20)
load_community_build(account="...", name="...")
```

---

## poe2-optimizer — Tool Reference

**Data sources:** extracted `.datc64` files, Patch 0.5. Game-text is authoritative. Do NOT fetch from wikis or poedb.

### Passive tree (9,605 nodes: 82 keystones, 2,151 notables)
```
inspect_passive_node(node_id=...)
inspect_keystone(name="Acrobatics")     # alias: name= also works
list_all_keystones()
list_all_notables()
check_tree_freshness()                  # verify local data is current with poe.ninja patch
```

### Gems (872 gems, Patch 0.5)
```
inspect_spell_gem(spell_name="Tempest Flurry")   # aliases: name=, gem_name=
inspect_support_gem(support_gem_name="...")
list_all_spells()                                # 83 active spells (PoB2 classification)
list_all_supports()
validate_support_combination(support_gems=["Rapid Attacks", "Brutality"])
```

### Item mods (16,788 mods)
```
inspect_mod(mod_id="...")
search_mods_by_stat(stat_keyword="attack speed")
get_mod_tiers(mod_id="AttackSpeed")
get_available_mods(base_item="...", item_level=...)
list_all_base_items()
inspect_base_item(base_item_name="...")
validate_item_mods(item_mods=[...])
```

### Ascendancies (37 classes, including Patch 0.5)
```
get_ascendancy_info(ascendancy_name="Invoker")
get_ascendancy_info(ascendancy_name="Monk")   # lists all Monk ascendancies
```

### Mechanics
```
explain_mechanic(mechanic_name="ignite")                         # Tier 2: hand-authored
explain_mechanic(mechanic_name="support_ignite_proliferation_radius")  # Tier 1: game-text
explain_mechanic()                                                # overview of query shapes
get_formula(formula_name="...")
```

### Character analysis (poe.ninja)
```
analyze_character(account="Name#1234", character="CharName", league="Standard")
analyze_passive_tree(node_ids=[...])     # feed node_ids from analyze_character result
```

### Diagnostics
```
health_check()
check_tree_freshness()
clear_cache()
```

---

## Known Limitations (Patch 0.5, 2026-06)

| Issue | Impact | Workaround |
|-------|--------|-----------|
| poe.ninja SPA migration (#61) | `compare_to_top_players` dead, fresh chars return 404 | Use PoB import instead |
| `search_trade_items` unimplemented | GGG OAuth blocked AI tooling | N/A |
| `inspect_spell_gem` missing: baseMultiplier, qualityStats, description | Incomplete gem data | Check in-game tooltip for exact numbers |

---

## Workflow: Monk Invoker Build Analysis

### Wariant A — masz PoB kod
```
1. load_build(pob_code="...")
2. get_stats()                     → sprawdź DPS, life, res
3. analyze_defenses()              → uncapped res / life pool
4. get_skills()                    → weryfikacja gem linków
5. search_tree("attack speed", classes=["Monk"])  → następne pasywki
6. get_reachable_nodes(max_distance=4, classes=["Monk"])
```

### Wariant B — analiza bez PoB (dane z poe.ninja)
```
1. list_my_characters()
2. load_my_character("NazwaPostaci")
3. get_passives() → analyze_passive_tree(node_ids=[...])
```

### Wariant C — szukasz konkretnego gemu
```
1. inspect_spell_gem(spell_name="Tempest Flurry")
2. list_all_supports()             → które supporty istnieją
3. validate_support_combination(support_gems=["Rapid Attacks", "Perpetual Charge"])
```

### Wariant D — crafting upgrade
```
1. get_items()                     → aktualny ekwipunek
2. analyze_defenses()              → gdzie są luki
3. craft_advisor(target="...", slot="...")
4. generate_vendor_regex(slot="...")
```

---

## Parameter Gotchas

- `inspect_keystone` accepts `name=` (alias) — inne toole wymagają canonical parameter name
- `inspect_spell_gem` accepts `name=`, `gem_name=` (aliasy)
- `validate_support_combination` accepts `support_gems` (array) lub aliasy `support_gem_names`, `names`
- Dla wszystkich innych: użyj dokładnej nazwy z inputSchema (sprawdź gdy wątpliwości)
- `poe2-optimizer` to warstwa danych — sam syntetyzuj rekomendacje na podstawie zwróconych faktów
