"""
build_crafting.py - PoE2 Crafting Reference Library Generator
Build: Lightning+Chaos Invoker Monk (dual 1H Mace + Quarterstaff), target: Dual Mjolnir lvl 65

Reads raw_mods.json and raw_base_items.json and generates crafting/ directory with 5 markdown files.
"""

import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# Force UTF-8 output on Windows to avoid cp1250 encode errors
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
RAW_MODS = BASE_DIR / "raw_mods.json"
RAW_BASE_ITEMS = BASE_DIR / "raw_base_items.json"
OUT_DIR = BASE_DIR / "crafting"

# ─── Build-relevant mod groups ────────────────────────────────────────────────
STAR_GROUPS_WEAPONS = {
    # Lightning / elemental damage
    "LightningDamage", "AddedLightningDamage", "ElementalDamageAttacks",
    "LightningDamageAttacks", "LightningDamagePercentAttacks",
    # Physical (scales via conversion)
    "IncreasedPhysicalDamage", "AddedPhysicalDamage", "PhysicalDamage",
    # Attack speed & crit
    "AttackSpeed", "CriticalStrikeChance", "CriticalStrikeMultiplier",
    "IncreasedCriticalStrikeChance", "IncreasedCriticalStrikeMultiplier",
    # Chaos
    "ChaosDamage", "AddedChaosDamage", "ChaosDamageAttacks",
    # Attributes
    "Strength", "Intelligence",
}

STAR_GROUPS_JEWELLERY = {
    "Strength", "Intelligence",
    "LightningResistance", "AllResistances",
    "Life", "MaximumLife",
    "LightningDamage", "AddedLightningDamage",
    "ElementalDamageAttacks",
}

STAR_GROUPS_ARMOUR = {
    "Life", "MaximumLife",
    "EnergyShield", "IncreasedEnergyShield",
    "AllResistances", "LightningResistance", "FireResistance", "ColdResistance",
    "Strength", "Intelligence",
    "MovementSpeed",
}

# ─── Helpers ──────────────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    """Strip wiki-link markup: [label|target] → target, or just label."""
    text = re.sub(r'\[([^\|]+)\|([^\]]+)\]', r'\2', text)
    text = re.sub(r'\[([^\]]+)\]', r'\1', text)
    return text


def spawns_on(mod: dict, tags: set) -> bool:
    """
    Return True if mod can spawn on any item with one of the given tags.
    Rules:
    - Any tag in spawn_weights with weight > 0 → eligible
    - If none of the target tags appear in spawn_weights but default > 0 → also eligible
    - If ALL target tags appear with weight 0 → not eligible
    """
    weights = {w["tag"]: w["weight"] for w in mod.get("spawn_weights", [])}
    # Check explicit tag matches first
    for tag in tags:
        if tag in weights:
            if weights[tag] > 0:
                return True
            # tag explicitly set to 0 → blocked
    # If none of our target tags appear at all, fall back to default
    if not any(t in weights for t in tags):
        return weights.get("default", 0) > 0
    return False


def is_craftable_affix(mod: dict) -> bool:
    """Only domain=item, generation_type prefix or suffix, not essence-only."""
    return (
        mod.get("domain") == "item"
        and mod.get("generation_type") in ("prefix", "suffix")
        and not mod.get("is_essence_only", False)
    )


def format_row(name, gen_type, text, req_level, group, starred):
    star = "★ " if starred else ""
    ptype = "P" if gen_type == "prefix" else "S"
    return f"| {star}{name} | {ptype} | {text} | {req_level} | {group} |"


def write_affix_table(f, mods_list, star_groups):
    f.write("| Mod Name | P/S | Stat Text | Req Lvl | Group |\n")
    f.write("|---|---|---|---|---|\n")
    for mod_id, mod in mods_list:
        groups = mod.get("groups", [])
        group_str = groups[0] if groups else "—"
        starred = bool(star_groups & set(groups))
        text = clean_text(mod.get("text", ""))
        name = mod.get("name", mod_id)
        req = mod.get("required_level", 0)
        f.write(format_row(name, mod["generation_type"], text, req, group_str, starred) + "\n")


def load_json(path: Path) -> dict:
    print(f"Loading {path.name}…")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# ─── Currency knowledge table ─────────────────────────────────────────────────
# Map internal ID fragment → (function_desc, when_to_use)
CURRENCY_KNOWLEDGE = {
    "CurrencyIdentification":       ("Identifies an unidentified item",
                                     "Use on any unidentified magic/rare/unique drop"),
    "CurrencyWeaponQuality":        ("Improves quality of a martial weapon (+1% per use, up to 20%)",
                                     "Use on weapons before crafting — quality increases implicit values"),
    "CurrencyMagicQuality":         ("Improves quality of a wand/staff/sceptre",
                                     "For caster weapons only; not relevant to Monk maces"),
    "CurrencyArmourQuality":        ("Improves quality of armour",
                                     "Use on armour before crafting to boost defence values"),
    "CurrencyFlaskQuality":         ("Improves quality of a flask",
                                     "Use on flasks to increase effect/duration"),
    "CurrencyGemQuality":           ("Improves quality of a gem",
                                     "Use on skill gems to boost quality effects"),
    "CurrencyUpgradeToMagic":       ("Upgrades a normal item to magic (1–2 mods)",
                                     "First step: turn a white base into a magic item"),
    "CurrencyUpgradeToMagic2":      ("Greater version — upgrades normal to magic (better odds on higher tiers)",
                                     "Prefer on higher-level bases"),
    "CurrencyUpgradeToMagic3":      ("Perfect version — upgrades normal to magic",
                                     "Best quality normal→magic upgrade"),
    "CurrencyRerollMagic":          ("Rerolls all mods on a magic item",
                                     "Spam on a magic base to fish for desired prefix+suffix combo"),
    "CurrencyAddModToMagic":        ("Adds a mod to a magic item (if only 1 mod)",
                                     "Add second mod to a one-affix magic item"),
    "CurrencyUpgradeMagicToRare":   ("Upgrades a magic item to rare (3–4 mods)",
                                     "Convert a perfect magic item to rare to gain more mods"),
    "CurrencyUpgradeToRare":        ("Upgrades a normal item directly to rare (4 random mods)",
                                     "Skip magic step — go straight to rare base"),
    "CurrencyRerollRare":           ("Rerolls all mods on a rare item (Chaos Orb)",
                                     "Core crafting currency — reroll rares to find desired affix combos"),
    "CurrencyRerollRare2":          ("Greater Chaos Orb — rerolls rare mods (higher tier weighting)",
                                     "Better than Chaos Orb on level 75+ items"),
    "CurrencyRerollRare3":          ("Perfect Chaos Orb — rerolls rare mods (highest tier weighting)",
                                     "Best reroll for endgame bases"),
    "CurrencyAddModToRare":         ("Adds one mod to a rare item with open affix slot (Exalted Orb)",
                                     "Add a specific-tier mod after locking good existing mods"),
    "CurrencyAddModToRare2":        ("Greater Exalted Orb — adds mod to rare (higher tier weighting)",
                                     "Prefer for endgame weapon crafting"),
    "CurrencyAddModToRare3":        ("Perfect Exalted Orb — adds mod with highest tier weighting",
                                     "Best for finalizing endgame rare weapons"),
    "CurrencyRemoveMod":            ("Removes one random mod from a rare item (Orb of Annulment)",
                                     "Remove a bad mod after exalting — risky but powerful"),
    "CurrencyConvertToNormal":      ("Removes all mods from a rare/magic item (Orb of Scouring)",
                                     "Reset a bad roll to white; start crafting over"),
    "CurrencyModValues":            ("Re-rolls numeric values of all mods on a magic/rare item (Divine Orb)",
                                     "Re-roll tier rolls — use when mod is correct but values are low"),
    "CurrencyRerollImplicit":       ("Re-rolls numeric values of implicit mods (Blessed Orb)",
                                     "Improve implicit on a well-rolled weapon"),
    "CurrencyRerollDefences":       ("Re-rolls defence values on armour (Sacred Orb)",
                                     "Optimize armour/ES/evasion values"),
    "CurrencyCorrupt":              ("Corrupts an item — random effect (Vaal Orb): add mod, reroll, add socket, or nothing",
                                     "Final step on a finished item to gamble for extra power; cannot be modified after"),
    "CurrencyImprintOrb":           ("Creates an Imprint of a magic item that can be restored (Eternal Orb)",
                                     "Backup magic item before risky crafting"),
    "CurrencyHinekorasLock":        ("Locks an item's mods so Divine Orb cannot reroll them",
                                     "Use before Divine Orb to protect already-maxed mod values"),
    "CurrencyFractureRare":         ("Fractures one mod on a rare item — that mod is permanently locked (Fracturing Orb)",
                                     "Lock a high-tier desired mod before rerolling others"),
    "CurrencyDuplicate":            ("Creates an exact copy of an item (Mirror of Kalandra)",
                                     "The rarest currency — copy a near-perfect endgame item"),
    "CurrencyUpgradeRandomly":      ("Randomly upgrades a normal item to magic, rare, or unique (Orb of Chance)",
                                     "Gamble for a unique on a specific base type"),
    "CurrencyPassiveRefund":        ("Refunds one passive skill point (Orb of Regret)",
                                     "Respec passive tree nodes"),
    "CurrencyRerollSocketColours":  ("Rerolls socket colours on an item (Chromatic Orb)",
                                     "Not relevant in PoE2 — socket system changed"),
    "CurrencyAddEquipmentSocket":   ("Adds a socket to an item (Artificer's Orb)",
                                     "Add rune sockets to weapons/armour"),
    "CurrencyEssenceLightning":     ("Forces a guaranteed lightning mod on an item",
                                     "★ Guaranteed lightning damage on weapon — use Essence of Electricity on mace"),
    "CurrencyGreaterEssenceLightning": ("Greater version — forces higher-tier lightning mod",
                                     "★ Better guaranteed lightning mod — use on high-level bases"),
    "CurrencyPerfectEssenceLightning": ("Perfect version — forces top-tier lightning mod",
                                     "★ Best guaranteed lightning mod for endgame mace"),
    "CurrencyEssencePhysical":      ("Forces a guaranteed physical damage mod",
                                     "★ Use on mace to guarantee phys damage (scales lightning via conversion)"),
    "CurrencyEssenceAttack":        ("Forces a guaranteed attack-related mod",
                                     "★ Use on weapon — attack speed or similar"),
    "CurrencyEssenceCritical":      ("Forces a guaranteed critical strike mod",
                                     "★ Use for guaranteed crit chance/multi on weapons"),
    "CurrencyEssenceAttribute":     ("Forces a guaranteed attribute (Str/Int/Dex) mod",
                                     "Use on rings/amulets when short on Str/Int requirements"),
    "CurrencyEssenceLife":          ("Forces a guaranteed maximum life mod",
                                     "Use on body armour or rings for life"),
    "CurrencyRitualSplinter":       ("100 splinters combine into a Ritual Vessel",
                                     "Collect to build Ritual Vessels for replaying ritual monster pools"),
    "CurrencyRitualStone":          ("Stores monsters from a completed Ritual Altar (Ritual Vessel)",
                                     "Use at a Ritual Altar to add stored monsters to a future map's ritual"),
    "CurrencyMapQuality":           ("Improves quality of a map (Cartographer's Chisel)",
                                     "Use on maps before running to increase item quantity"),
    "CurrencyAddSkillGemSocket3":   ("Adds a 3rd socket to a skill gem (Lesser Jeweller's Orb)",
                                     "Add sockets to skill gems to fit more support gems"),
    "CurrencyAddSkillGemSocket4":   ("Adds a 4th socket to a skill gem (Greater Jeweller's Orb)",
                                     "Further expand support gem slots"),
    "CurrencyAddSkillGemSocket5":   ("Adds a 5th socket to a skill gem (Perfect Jeweller's Orb)",
                                     "Maximum support gem capacity"),
}


def get_currency_function(item_id: str, item: dict) -> tuple:
    """Return (function_desc, when_to_use) for a currency item."""
    # Strip path prefix to get bare ID
    bare = item_id.split("/")[-1]
    # Check exact match
    if bare in CURRENCY_KNOWLEDGE:
        return CURRENCY_KNOWLEDGE[bare]
    # Check prefix match (e.g. CurrencyEssenceLightning covers all tiers)
    for key, val in CURRENCY_KNOWLEDGE.items():
        if bare.startswith(key) or key.startswith(bare):
            return val
    # Fall back to description in properties
    desc = ""
    directions = ""
    if item.get("properties"):
        desc = item["properties"].get("description") or ""
        directions = item["properties"].get("directions") or ""
    if desc or directions:
        return (desc.strip(), directions.strip())
    return ("—", "—")


# ─── Main generation ──────────────────────────────────────────────────────────

def generate_currency(base_items: dict, out_path: Path):
    """Generate crafting/currency.md."""
    print("  Generating currency.md…")
    # Collect all currency items
    currency_items = []
    for item_id, item in base_items.items():
        if "/Currency/" in item_id and item.get("item_class") in (
            "StackableCurrency", "Currency", None
        ):
            # Skip [DNT] items
            name = item.get("name", "")
            if name.startswith("[DNT]"):
                continue
            if not name:
                continue
            currency_items.append((item_id, item))

    # Group by category
    categories = {
        "Core Crafting Orbs": [],
        "Essences": [],
        "Quality Currency": [],
        "Ritual & League Mechanics": [],
        "Sockets": [],
        "Shards": [],
        "Other / Legacy": [],
    }

    def categorize(item_id, item):
        bare = item_id.split("/")[-1]
        name = item.get("name", "")
        if "Essence" in bare or "Essence" in name:
            return "Essences"
        if bare in ("CurrencyWeaponQuality", "CurrencyArmourQuality", "CurrencyMagicQuality",
                    "CurrencyFlaskQuality", "CurrencyGemQuality", "CurrencyMapQuality"):
            return "Quality Currency"
        if "Ritual" in bare or "Ritual" in name or "Petition" in name:
            return "Ritual & League Mechanics"
        if "Socket" in bare or "Jeweller" in bare or "Artificer" in bare:
            return "Sockets"
        if "Shard" in bare or "Shard" in name or "Splinter" in name:
            return "Shards"
        core = ["CurrencyIdentification", "CurrencyUpgradeToMagic", "CurrencyRerollMagic",
                "CurrencyAddModToMagic", "CurrencyUpgradeMagicToRare", "CurrencyUpgradeToRare",
                "CurrencyRerollRare", "CurrencyAddModToRare", "CurrencyRemoveMod",
                "CurrencyConvertToNormal", "CurrencyModValues", "CurrencyRerollImplicit",
                "CurrencyRerollDefences", "CurrencyCorrupt", "CurrencyImprintOrb",
                "CurrencyHinekorasLock", "CurrencyFractureRare", "CurrencyDuplicate",
                "CurrencyUpgradeRandomly", "CurrencyPassiveRefund"]
        for c in core:
            if bare.startswith(c):
                return "Core Crafting Orbs"
        return "Other / Legacy"

    for item_id, item in currency_items:
        cat = categorize(item_id, item)
        categories[cat].append((item_id, item))

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# PoE2 Currency Reference\n\n")
        f.write("Build focus: Lightning+Chaos Invoker Monk (dual 1H Mace + Quarterstaff → Dual Mjölnir)\n\n")
        f.write("> Items marked ★ are directly relevant to this build's crafting workflow.\n\n")

        total = 0
        for cat_name, items in categories.items():
            if not items:
                continue
            f.write(f"## {cat_name}\n\n")
            f.write("| Name | Internal ID | Function | When to Use |\n")
            f.write("|---|---|---|---|\n")
            for item_id, item in sorted(items, key=lambda x: x[1].get("name", "")):
                bare = item_id.split("/")[-1]
                name = item.get("name", bare)
                fn, when = get_currency_function(item_id, item)
                # Star highly relevant items
                star = ""
                if any(k in bare for k in [
                    "EssenceLightning", "EssencePhysical", "EssenceAttack", "EssenceCritical",
                    "RerollRare", "AddModToRare", "ModValues", "RemoveMod", "FractureRare",
                    "Corrupt", "HinekorasLock", "ImprintOrb",
                ]):
                    star = "★ "
                f.write(f"| {star}{name} | `{bare}` | {fn} | {when} |\n")
                total += 1
            f.write("\n")

    print(f"    -> {total} currency items written")
    return total


def generate_affixes(mods: dict, out_path: Path, tags: set, title: str,
                     focus_note: str, star_groups: set):
    """Generate an affixes markdown file for the given item tags."""
    print(f"  Generating {out_path.name}…")

    eligible = []
    for mod_id, mod in mods.items():
        if not is_craftable_affix(mod):
            continue
        if spawns_on(mod, tags):
            eligible.append((mod_id, mod))

    # Sort by group then required_level
    eligible.sort(key=lambda x: (
        x[1].get("groups", [""])[0],
        x[1].get("required_level", 0),
        x[1].get("name", "")
    ))

    # Split into prefixes and suffixes
    prefixes = [(m_id, m) for m_id, m in eligible if m["generation_type"] == "prefix"]
    suffixes = [(m_id, m) for m_id, m in eligible if m["generation_type"] == "suffix"]

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"Applicable item tags: `{'`, `'.join(sorted(tags))}`\n\n")
        f.write(f"**Build focus:** {focus_note}\n\n")
        f.write("> ★ = high priority for Lightning+Chaos Invoker Monk build\n\n")

        f.write(f"## Prefixes ({len(prefixes)} total)\n\n")
        write_affix_table(f, prefixes, star_groups)
        f.write("\n")

        f.write(f"## Suffixes ({len(suffixes)} total)\n\n")
        write_affix_table(f, suffixes, star_groups)
        f.write("\n")

    count = len(eligible)
    print(f"    -> {count} mods ({len(prefixes)} prefixes, {len(suffixes)} suffixes)")
    return count


def generate_rituals(out_path: Path, base_items: dict):
    """Generate crafting/rituals.md — static knowledge + data from raw_base_items."""
    print("  Generating rituals.md…")

    # Pull actual item data
    ritual_items = {}
    for item_id, item in base_items.items():
        if "Ritual" in item_id or "Ritual" in item.get("name", ""):
            name = item.get("name", "")
            if name and not name.startswith("[DNT]"):
                desc = ""
                directions = ""
                if item.get("properties"):
                    desc = item["properties"].get("description") or ""
                    directions = item["properties"].get("directions") or ""
                ritual_items[name] = {
                    "id": item_id,
                    "desc": desc.strip(),
                    "directions": directions.strip(),
                    "item_class": item.get("item_class", ""),
                    "drop_level": item.get("drop_level", 0),
                }

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Rituals in Path of Exile 2\n\n")
        f.write("> Static knowledge doc — covers ritual mechanics and why they matter for crafting.\n\n")
        f.write("## What Are Rituals?\n\n")
        f.write(
            "Rituals are an endgame league mechanic found in Maps. "
            "When you enter a map, you may encounter **Ritual Altars** — glowing circles containing "
            "monsters. You activate an altar, kill all monsters within the ritual circle, and earn "
            "**Tribute** (a currency-like resource). After completing multiple altars in a map, a "
            "**Ritual Vendor** appears where you spend your accumulated Tribute on specific items "
            "from a curated loot pool.\n\n"
        )
        f.write("## How Tribute Works\n\n")
        f.write(
            "1. **Activate** a Ritual Altar (click it).\n"
            "2. **Kill all monsters** inside the glowing ritual circle — they may revive as empowered "
            "versions.\n"
            "3. Each altar completed adds to your **Tribute counter** and populates the ritual item pool.\n"
            "4. After the final altar in the map, a **Ritual Vendor** spawns.\n"
            "5. Browse the vendor's loot pool and **spend Tribute** to purchase items.\n"
            "6. Items you cannot afford (insufficient Tribute) can be **deferred** — this makes them "
            "cost more Tribute but re-adds them to a future ritual's pool with bonus Tribute added.\n"
            "7. **Deferring strategically** lets you farm Tribute across multiple maps to afford "
            "expensive high-tier items.\n\n"
        )
        f.write("## Why Rituals Matter for Crafting\n\n")
        f.write(
            "- **Guaranteed item pool**: Unlike random drops, ritual pools contain specific items you "
            "can browse and target.\n"
            "- **Targeted base acquisition**: If you see a high-level Mace base or a specific unique "
            "in the pool, you can defer it and return once you have enough Tribute.\n"
            "- **Currency drops**: Ritual pools can contain Exalted Orbs, Divine Orbs, and Essences "
            "— valuable for weapon crafting.\n"
            "- **Unique items**: Ritual pools can contain uniques including endgame-tier weapons. "
            "For this build, Mjölnir (unique Mace) could theoretically appear in ritual pools.\n"
            "- **No RNG on purchase**: Once in the pool, the item is guaranteed — only cost varies.\n\n"
        )
        f.write("## Ritual Items (from game data)\n\n")
        f.write("| Item | Class | Drop Lvl | Description | Usage |\n")
        f.write("|---|---|---|---|---|\n")

        # Key ritual items to highlight
        key_items = [
            "Ritual Splinter", "Ritual Vessel", "Blood-filled Vessel",
            "Head of the King", "Petition Splinter", "Ritual Tablet",
            "An Audience with the King", "Tribute to the Goddess",
        ]
        for name in key_items:
            if name in ritual_items:
                d = ritual_items[name]
                f.write(f"| **{name}** | {d['item_class']} | {d['drop_level']} | "
                        f"{d['desc'] or d['directions']} | {d['directions'] if d['desc'] else '—'} |\n")

        f.write("\n")
        f.write("## Ritual Tablet (TowerAugment)\n\n")
        f.write(
            "The **Ritual Tablet** is a Tower Augmentation item (`domain: tablet`, "
            "drop level 65). It is placed into a Tower on the Atlas to add Ritual Altars "
            "to all maps in the tower's influence radius. Using a Ritual Tablet effectively "
            "forces ritual encounters to appear, giving you a reliable way to farm Tribute "
            "and access the ritual vendor in every map within range.\n\n"
            "Key details:\n"
            "- Implicit mod: `TowerAddRitualToMapsImplicit` — adds ritual to maps\n"
            "- Drop level: 65 — only found in high-tier maps\n"
            "- Can have additional mods (magic/rare) that enhance ritual rewards or Tribute gain\n"
            "- Ritual Tablets with mods like 'Ritual monsters have X% more life' increase Tribute "
            "earned per altar completed\n\n"
        )
        f.write("## Crafting Workflow with Rituals\n\n")
        f.write(
            "For the Lightning+Chaos Invoker Monk targeting Dual Mjölnir:\n\n"
            "1. Place a **Ritual Tablet** in a nearby Tower to guarantee ritual spawns.\n"
            "2. Complete all ritual altars in each map to maximize Tribute per run.\n"
            "3. Browse the ritual vendor for:\n"
            "   - High-level 1H Mace bases (for crafting toward Mjölnir)\n"
            "   - Exalted Orbs / Greater Exalted Orbs (for adding mods)\n"
            "   - Essences of Electricity / Abrasion (guaranteed lightning/phys mods)\n"
            "   - Unique maces if Mjölnir appears in the pool\n"
            "4. **Defer expensive items** you cannot yet afford — they accumulate bonus Tribute.\n"
            "5. Use **Blood-filled Vessels** to replay high-value ritual monster pools in "
            "future maps, potentially re-stocking the vendor with similar items.\n\n"
        )

    print(f"    -> {len(ritual_items)} ritual items referenced")
    return len(ritual_items)


def highlight_top_mods(mods: dict, tags: set, star_groups: set, top_n=10):
    """Return top N starred mods for a given tag set, sorted by req_level desc."""
    results = []
    for mod_id, mod in mods.items():
        if not is_craftable_affix(mod):
            continue
        if not spawns_on(mod, tags):
            continue
        groups = set(mod.get("groups", []))
        if groups & star_groups:
            results.append((mod_id, mod))
    results.sort(key=lambda x: x[1].get("required_level", 0), reverse=True)
    return results[:top_n]


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("PoE2 Crafting Reference Generator")
    print("=" * 60)

    # Load data
    mods = load_json(RAW_MODS)
    base_items = load_json(RAW_BASE_ITEMS)

    # Create output directory
    OUT_DIR.mkdir(exist_ok=True)
    print(f"\nOutput directory: {OUT_DIR}\n")

    stats = {}

    # 1. Currency
    stats["currency"] = generate_currency(base_items, OUT_DIR / "currency.md")

    # 2. Weapon affixes (mace + quarterstaff)
    stats["weapons"] = generate_affixes(
        mods,
        OUT_DIR / "affixes_weapons.md",
        tags={"mace", "quarterstaff"},
        title="Weapon Affixes — 1H Mace & Quarterstaff",
        focus_note="Lightning damage, physical damage (conversion), attack speed, crit, Str/Int, chaos damage",
        star_groups=STAR_GROUPS_WEAPONS,
    )

    # 3. Jewellery affixes
    stats["jewellery"] = generate_affixes(
        mods,
        OUT_DIR / "affixes_jewellery.md",
        tags={"ring", "amulet", "belt"},
        title="Jewellery Affixes — Ring, Amulet, Belt",
        focus_note="Str/Int attributes, resistances, life, added lightning damage",
        star_groups=STAR_GROUPS_JEWELLERY,
    )

    # 4. Armour affixes
    stats["armour"] = generate_affixes(
        mods,
        OUT_DIR / "affixes_armour.md",
        tags={"helmet", "body_armour", "gloves", "boots", "str_armour", "str_int_armour"},
        title="Armour Affixes — Helmet, Body, Gloves, Boots",
        focus_note="Life/ES, resistances, Str/Int, movement speed (boots)",
        star_groups=STAR_GROUPS_ARMOUR,
    )

    # 5. Rituals
    stats["rituals"] = generate_rituals(OUT_DIR / "rituals.md", base_items)

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  currency.md       : {stats['currency']} items")
    print(f"  affixes_weapons.md: {stats['weapons']} mods")
    print(f"  affixes_jewellery.md: {stats['jewellery']} mods")
    print(f"  affixes_armour.md : {stats['armour']} mods")
    print(f"  rituals.md        : generated (static doc)")

    # ── Interesting findings ──────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("INTERESTING FINDINGS")
    print("=" * 60)

    print("\nTop weapon mods for Lightning+Chaos Monk (by req level):")
    top_weapon = highlight_top_mods(mods, {"mace", "quarterstaff"}, STAR_GROUPS_WEAPONS, top_n=15)
    for mod_id, mod in top_weapon:
        groups = mod.get("groups", ["?"])
        text = clean_text(mod.get("text", ""))
        req = mod.get("required_level", 0)
        print(f"  [{req:3d}] {mod.get('name', mod_id):30s}  {groups[0]:35s}  {text}")

    print("\nTop ring/amulet mods for Str+Int stacking:")
    top_jewellery = highlight_top_mods(mods, {"ring", "amulet"}, {"Strength", "Intelligence"}, top_n=10)
    for mod_id, mod in top_jewellery:
        groups = mod.get("groups", ["?"])
        text = clean_text(mod.get("text", ""))
        req = mod.get("required_level", 0)
        print(f"  [{req:3d}] {mod.get('name', mod_id):30s}  {groups[0]:25s}  {text}")

    print("\nAll output files:")
    for fname in sorted(OUT_DIR.glob("*.md")):
        size_kb = fname.stat().st_size / 1024
        print(f"  {fname.name:30s} {size_kb:7.1f} KB")

    print("\nDone!")


if __name__ == "__main__":
    main()
