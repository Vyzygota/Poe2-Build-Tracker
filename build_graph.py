"""
PoE2 Skill-Support Dependency Graph
Filtruje skille: lightning, 1H mace, quarterstaff
Buduje graf zależności skill → compatible supports
"""
import json
from pathlib import Path

DATA = Path(__file__).parent / "raw_skill_gems.json"

FOCUS_TAGS = {"lightning", "1h_mace", "one_hand_mace", "quarterstaff", "attack", "spell"}
FOCUS_CRAFTING = {"quarterstaff", "1h mace", "one hand mace", "mace", "elemental", "melee"}

def normalize(s):
    return s.lower().replace(" ", "_").replace("-", "_")

def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))

    active_skills = {}
    support_gems = {}

    for k, v in data.items():
        name = v.get("base_item", {}).get("display_name", "") or ""
        tags = [normalize(t) for t in (v.get("tags") or [])]
        crafting_types = [normalize(c) for c in (v.get("crafting_types") or [])]
        gem_type = v.get("gem_type", "")
        color = v.get("color", "")
        is_lineage = v.get("is_lineage", False)
        support_text = (v.get("support_text") or "").replace("[", "").replace("]", "").replace("|", " ")
        recommended = v.get("recommended_supports") or []

        # Tier
        tier = 1
        kl = k.lower()
        if kl.endswith("two"): tier = 2
        elif kl.endswith("three"): tier = 3

        if gem_type == "active":
            tags_set = set(tags)
            ct_set = set(crafting_types)

            # Filter: lightning OR mace OR quarterstaff related
            is_lightning = "lightning" in tags_set
            is_mace = any(x in ct_set for x in ("mace", "1h_mace", "one_hand_mace", "one_handed_mace"))
            is_qs = "quarterstaff" in ct_set
            is_attack = "attack" in tags_set
            is_spell = "spell" in tags_set

            if is_lightning or is_mace or is_qs:
                active_skills[k] = {
                    "name": name,
                    "tags": tags,
                    "crafting_types": crafting_types,
                    "is_lightning": is_lightning,
                    "is_mace": is_mace,
                    "is_quarterstaff": is_qs,
                    "is_attack": is_attack,
                    "is_spell": is_spell,
                    "recommended_supports": recommended,
                }

        elif gem_type == "support":
            # Attr from color
            attr = {"r": "str", "g": "dex", "b": "int"}.get(color, "generic")
            support_gems[k] = {
                "name": name,
                "attr": attr,
                "tier": tier,
                "is_lineage": is_lineage,
                "tags": tags,
                "text": support_text,
            }

    # Build dependency map: active skill → list of recommended support names
    skill_to_supports = {}
    for sk, sv in active_skills.items():
        sup_names = []
        for sup_key in sv["recommended_supports"]:
            if sup_key in support_gems:
                sup_names.append(support_gems[sup_key]["name"])
        skill_to_supports[sv["name"]] = sup_names

    # Build reverse map: support → skills that recommend it
    support_to_skills = {}
    for skill_name, sups in skill_to_supports.items():
        for sup in sups:
            support_to_skills.setdefault(sup, []).append(skill_name)

    # Categorize active skills
    lightning_spells = [v for v in active_skills.values() if v["is_lightning"] and v["is_spell"]]
    lightning_attacks = [v for v in active_skills.values() if v["is_lightning"] and v["is_attack"]]
    mace_skills = [v for v in active_skills.values() if v["is_mace"]]
    qs_skills = [v for v in active_skills.values() if v["is_quarterstaff"]]

    # Output
    output = {
        "summary": {
            "total_active_filtered": len(active_skills),
            "lightning_spells": len(lightning_spells),
            "lightning_attacks": len(lightning_attacks),
            "mace_skills": len(mace_skills),
            "quarterstaff_skills": len(qs_skills),
            "total_supports": len(support_gems),
        },
        "lightning_spells": [
            {"name": v["name"], "tags": v["tags"], "recommended_supports": skill_to_supports.get(v["name"], [])}
            for v in sorted(lightning_spells, key=lambda x: x["name"])
        ],
        "lightning_attacks": [
            {"name": v["name"], "tags": v["tags"], "recommended_supports": skill_to_supports.get(v["name"], [])}
            for v in sorted(lightning_attacks, key=lambda x: x["name"])
        ],
        "mace_skills": [
            {"name": v["name"], "tags": v["tags"], "crafting_types": v["crafting_types"], "recommended_supports": skill_to_supports.get(v["name"], [])}
            for v in sorted(mace_skills, key=lambda x: x["name"])
        ],
        "quarterstaff_skills": [
            {"name": v["name"], "tags": v["tags"], "recommended_supports": skill_to_supports.get(v["name"], [])}
            for v in sorted(qs_skills, key=lambda x: x["name"])
        ],
        "support_popularity": sorted(
            [{"support": k, "used_by_count": len(v), "skills": v} for k, v in support_to_skills.items()],
            key=lambda x: -x["used_by_count"]
        )[:40],
    }

    out_path = Path(__file__).parent / "skill_graph.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Graph saved: {out_path}")
    print(json.dumps(output["summary"], indent=2))

    # Print quick view
    print("\n=== QUARTERSTAFF SKILLS ===")
    for s in output["quarterstaff_skills"]:
        print(f"  {s['name']}: {s['recommended_supports'][:5]}")

    print("\n=== MACE SKILLS ===")
    for s in output["mace_skills"]:
        print(f"  {s['name']}: {s['recommended_supports'][:5]}")

    print("\n=== LIGHTNING SPELLS ===")
    for s in output["lightning_spells"]:
        print(f"  {s['name']}: {s['recommended_supports'][:5]}")

    print("\n=== TOP SUPPORTS (cross-skill popularity) ===")
    for s in output["support_popularity"][:15]:
        print(f"  [{s['used_by_count']}x] {s['support']}")

if __name__ == "__main__":
    main()
