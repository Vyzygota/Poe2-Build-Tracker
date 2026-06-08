"""
build_bases.py - generates crafting/bases_*.md files with base items by slot, sorted by level req
"""
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("crafting", exist_ok=True)

with open("raw_base_items.json", encoding="utf-8") as f:
    data = json.load(f)

# Item classes to generate tables for
SLOTS = {
    "bases_weapons.md": {
        "title": "Bazy broni — po poziomie wymagania",
        "classes": ["One Hand Mace", "Warstaff", "Two Hand Mace", "Flail"],
    },
    "bases_helmets.md": {
        "title": "Hełmy — po poziomie wymagania",
        "classes": ["Helmet"],
    },
    "bases_body.md": {
        "title": "Pancerze — po poziomie wymagania",
        "classes": ["Body Armour"],
    },
    "bases_gloves.md": {
        "title": "Rękawice — po poziomie wymagania",
        "classes": ["Gloves"],
    },
    "bases_boots.md": {
        "title": "Buty — po poziomie wymagania",
        "classes": ["Boots"],
    },
    "bases_jewellery.md": {
        "title": "Biżuteria — po poziomie wymagania",
        "classes": ["Ring", "Amulet", "Belt"],
    },
}

# Defence type detection from tags
def defence_type(tags):
    t = set(tags or [])
    has_str = "str_armour" in t or "str_dex_armour" in t or "str_int_armour" in t or "str_dex_int_armour" in t
    has_dex = "dex_armour" in t or "str_dex_armour" in t or "dex_int_armour" in t or "str_dex_int_armour" in t
    has_int = "int_armour" in t or "str_int_armour" in t or "dex_int_armour" in t or "str_dex_int_armour" in t
    parts = []
    if has_str: parts.append("Armour")
    if has_dex: parts.append("Evasion")
    if has_int: parts.append("ES")
    if not parts:
        # try tag names directly
        for tag in t:
            if tag in ("str_armour",): return "Armour"
            if tag in ("dex_armour",): return "Evasion"
            if tag in ("int_armour",): return "ES"
    return "/".join(parts) if parts else "—"

def weapon_type(tags):
    t = set(tags or [])
    if "staff" in t or "warstaff" in t: return "Staff/Warstaff"
    if "mace" in t:
        if "onehand" in t: return "1H Mace"
        if "twohand" in t: return "2H Mace"
        return "Mace"
    if "flail" in t: return "Flail"
    return "Weapon"

def format_req(req):
    if not req: return "—"
    parts = []
    if req.get("strength", 0) > 0: parts.append(f"Str {req['strength']}")
    if req.get("dexterity", 0) > 0: parts.append(f"Dex {req['dexterity']}")
    if req.get("intelligence", 0) > 0: parts.append(f"Int {req['intelligence']}")
    return ", ".join(parts) if parts else "—"

def format_defence(props, tags):
    if not props: return "—"
    parts = []
    if props.get("armour"): parts.append(f"Ar:{props['armour']}")
    if props.get("evasion"): parts.append(f"Ev:{props['evasion']}")
    if props.get("energy_shield"): parts.append(f"ES:{props['energy_shield']}")
    return " ".join(parts) if parts else "—"

def format_weapon(props):
    if not props: return "—"
    dmg_min = props.get("physical_damage_min")
    dmg_max = props.get("physical_damage_max")
    aps = props.get("attack_time")
    if dmg_min and dmg_max:
        aps_val = round(1000 / aps, 2) if aps else "?"
        return f"{dmg_min}-{dmg_max} phys | {aps_val} APS"
    return "—"

for fname, cfg in SLOTS.items():
    items = []
    for k, v in data.items():
        if v.get("item_class") not in cfg["classes"]:
            continue
        if v.get("release_state") in ("unique_only", "unreleased", "drop_disabled"):
            continue
        name = v.get("name", "")
        if not name or name.startswith("[DNT") or name.startswith("[UNUSED"):
            continue
        req = v.get("requirements", {}) or {}
        lvl = req.get("level") or v.get("drop_level") or 0
        items.append({
            "name": name,
            "lvl": lvl,
            "item_class": v.get("item_class"),
            "req": req,
            "req_str": format_req(req),
            "tags": v.get("tags", []),
            "properties": v.get("properties", {}) or {},
            "implicits": v.get("implicits", []),
        })

    items.sort(key=lambda x: (x["lvl"], x["name"]))

    # Is this a weapon slot?
    is_weapon = any(c in ["One Hand Mace", "Two Hand Mace", "Warstaff", "Flail"] for c in cfg["classes"])
    is_jewellery = any(c in ["Ring", "Amulet", "Belt"] for c in cfg["classes"])

    lines = [f"# {cfg['title']}\n"]
    lines.append(f"Klasy: {', '.join(cfg['classes'])}\n")

    if is_weapon:
        lines.append("| Lvl | Nazwa | Typ | Dmg | APS | Req atrybuty |")
        lines.append("|---|---|---|---|---|---|")
        for it in items:
            typ = weapon_type(it["tags"])
            props = it["properties"]
            dmg_min = props.get("physical_damage_min", "?")
            dmg_max = props.get("physical_damage_max", "?")
            aps_ms = props.get("attack_time")
            aps = round(1000 / aps_ms, 2) if aps_ms else "?"
            lines.append(f"| {it['lvl']} | {it['name']} | {typ} | {dmg_min}–{dmg_max} | {aps} | {it['req_str']} |")
    elif is_jewellery:
        lines.append("| Lvl | Nazwa | Typ | Req atrybuty | Implicits |")
        lines.append("|---|---|---|---|---|")
        for it in items:
            imps = "; ".join(it["implicits"][:2]) if it["implicits"] else "—"
            lines.append(f"| {it['lvl']} | {it['name']} | {it['item_class']} | {it['req_str']} | {imps} |")
    else:
        lines.append("| Lvl | Nazwa | Typ obrony | Wartości | Req atrybuty |")
        lines.append("|---|---|---|---|---|")
        for it in items:
            def_type = defence_type(it["tags"])
            def_val = format_defence(it["properties"], it["tags"])
            lines.append(f"| {it['lvl']} | {it['name']} | {def_type} | {def_val} | {it['req_str']} |")

    lines.append("")

    with open(f"crafting/{fname}", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"{fname}: {len(items)} items")

print("Done.")
