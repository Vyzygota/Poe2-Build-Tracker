"""
PoE2 Socketables Builder
Zbiera: Runy (Lesser/Normal/Greater/Perfect), Ancient Runes, Warding Runes,
        Named Runes, Abyss SoulCores, Verisium Alloys, Jewels, Talismans
Dołącza do skill_graph.json
"""
import json
from pathlib import Path

BASE = Path("c:/Micro_Projrcts/Poe2")

def clean(text):
    return text.replace('[','').replace(']','').replace('|',' ').strip()

def load_display_names():
    """Build id -> display_name map from raw_base_items.json for SoulCore items."""
    data = json.loads((BASE / "raw_base_items.json").read_text(encoding="utf-8"))
    names = {}
    for k, v in data.items():
        if v.get('item_class') == 'SoulCore':
            item_id = k.split('/')[-1]
            names[item_id] = v.get('name', '')
    return names

def rune_category(item_id, display_name):
    """Classify rune into sub-category based on ID pattern."""
    dn = display_name.lower()
    if item_id.startswith('RuneOfTheAncients'):
        return 'ancient_rune'
    if item_id.startswith('RuneWardSpecial') or 'warding rune' in dn:
        return 'warding_rune'
    if item_id.startswith('RuneOlroths') or item_id.startswith('RuneSpecial') or 'legacy' in dn:
        return 'named_rune'
    # Basic runes: Lesser/Greater/Perfect/Normal variants of stat runes
    return 'basic_rune'

def build_runes_and_souls():
    """Process augments.json: split into runes (RuneXxx) and Abyss soul cores."""
    data = json.loads((BASE / "raw_augments.json").read_text(encoding="utf-8"))
    display_names = load_display_names()

    runes = []
    soul_cores = []

    for k, v in data.items():
        item_id = k.split('/')[-1]
        cats = v.get('categories', {}) if isinstance(v, dict) else {}
        effects = {}
        for slot, info in cats.items():
            texts = [clean(s) for s in info.get('stat_text', []) if s.strip()]
            if texts:
                effects[slot] = texts

        all_text = ' '.join(str(e) for e in effects.values()).lower()
        tags = []
        for tag in ['lightning','fire','cold','chaos','physical','life','mana',
                    'evasion','armour','energy shield','speed','ward',
                    'shock','freeze','electrocute','elemental','strength',
                    'dexterity','intelligence','accuracy']:
            if tag in all_text:
                tags.append(tag)

        display_name = display_names.get(item_id, '')

        if item_id.startswith('Rune'):
            cat = rune_category(item_id, display_name)
            # Detect tier from display name
            dn_lower = display_name.lower()
            if dn_lower.startswith('lesser '):
                tier = 1
            elif dn_lower.startswith('greater '):
                tier = 3
            elif dn_lower.startswith('perfect '):
                tier = 4
            elif cat == 'basic_rune':
                tier = 2
            else:
                tier = 0  # named/ancient/warding have no tier

            runes.append({
                'id': item_id,
                'name': display_name,
                'category': cat,
                'tier': tier,
                'effects': effects,
                'tags': tags,
            })
        else:
            soul_cores.append({
                'id': item_id,
                'name': display_names.get(item_id, ''),
                'type': 'abyss_soul_core',
                'effects': effects,
                'tags': tags,
            })

    return runes, soul_cores

def build_alloys():
    data = json.loads((BASE / "raw_base_items.json").read_text(encoding="utf-8"))
    alloys = []
    verisium_tiers = {
        'verisium_common': 1,
        'verisium_uncommon': 2,
        'verisium_rare': 3,
        'verisium_mythic': 4
    }
    for k, v in data.items():
        item_tags = v.get('tags', [])
        tier_tag = next((t for t in item_tags if t in verisium_tiers), None)
        if tier_tag:
            alloys.append({
                'id': k.split('/')[-1],
                'name': v.get('name', ''),
                'type': 'verisium_alloy',
                'tier': verisium_tiers[tier_tag],
                'tier_name': tier_tag,
                'tags': item_tags
            })
    return sorted(alloys, key=lambda x: (x['tier'], x['name']))

def build_jewels():
    data = json.loads((BASE / "raw_base_items.json").read_text(encoding="utf-8"))
    jewels = []
    for k, v in data.items():
        if v.get('item_class') == 'Jewel':
            jewels.append({
                'id': k.split('/')[-1],
                'name': v.get('name', ''),
                'type': 'jewel',
                'tags': v.get('tags', [])
            })
    return jewels

def build_talismans():
    data = json.loads((BASE / "raw_base_items.json").read_text(encoding="utf-8"))
    talismans = []
    for k, v in data.items():
        if v.get('item_class') == 'Talisman':
            talismans.append({
                'id': k.split('/')[-1],
                'name': v.get('name', ''),
                'type': 'talisman',
                'tags': v.get('tags', [])
            })
    return sorted(talismans, key=lambda x: x['name'])

def main():
    print("Building socketables...")
    runes, soul_cores = build_runes_and_souls()
    alloys = build_alloys()
    jewels = build_jewels()
    talismans = build_talismans()

    # Sub-categories of runes
    basic_runes = [r for r in runes if r['category'] == 'basic_rune']
    ancient_runes = [r for r in runes if r['category'] == 'ancient_rune']
    warding_runes = [r for r in runes if r['category'] == 'warding_rune']
    named_runes = [r for r in runes if r['category'] == 'named_rune']

    skill_graph = json.loads((BASE / "skill_graph.json").read_text(encoding="utf-8"))

    skill_graph['socketables'] = {
        'summary': {
            'basic_runes': len(basic_runes),
            'ancient_runes': len(ancient_runes),
            'warding_runes': len(warding_runes),
            'named_runes': len(named_runes),
            'abyss_soul_cores': len(soul_cores),
            'verisium_alloys': len(alloys),
            'jewels': len(jewels),
            'talismans': len(talismans),
        },
        'basic_runes': sorted(basic_runes, key=lambda x: (x['tier'], x['name'])),
        'ancient_runes': sorted(ancient_runes, key=lambda x: x['name']),
        'warding_runes': sorted(warding_runes, key=lambda x: x['name']),
        'named_runes': sorted(named_runes, key=lambda x: x['name']),
        'abyss_soul_cores': soul_cores,
        'verisium_alloys': alloys,
        'jewels': jewels,
        'talismans': talismans,
    }

    # Lightning-relevant quick reference
    def is_lightning(item):
        return ('lightning' in item.get('tags', []) or
                'shock' in item.get('tags', []) or
                'electrocute' in item.get('tags', []) or
                'storm' in item.get('name', '').lower())

    skill_graph['lightning_socketables'] = {
        'basic_runes': [r for r in basic_runes if is_lightning(r)],
        'named_runes': [r for r in named_runes if is_lightning(r)],
        'ancient_runes': [r for r in ancient_runes if is_lightning(r)],
        'soul_cores': [s for s in soul_cores if is_lightning(s)],
        'alloys': [a for a in alloys if any(x in str(a).lower() for x in ['lightning','storm','prismatic'])],
    }

    out = BASE / "skill_graph.json"
    out.write_text(json.dumps(skill_graph, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n=== SOCKETABLES SUMMARY ===")
    for k, v in skill_graph['socketables']['summary'].items():
        print(" ", k + ":", v)

    print("\n=== BASIC RUNES (Lightning / Storm) ===")
    for r in skill_graph['lightning_socketables']['basic_runes']:
        fx = list(r['effects'].values())[0] if r['effects'] else []
        tier_label = ['','Lesser','Normal','Greater','Perfect'][r['tier']] if r['tier'] else '?'
        print(" ", tier_label, r['name'], "->", str(fx)[:70])

    print("\n=== NAMED RUNES (Lightning) ===")
    for r in skill_graph['lightning_socketables']['named_runes']:
        fx = list(r['effects'].values())[0] if r['effects'] else []
        print(" ", r['name'], "->", str(fx)[:80])

    print("\n=== VERISIUM ALLOYS ===")
    for a in alloys:
        print(" ", "[T" + str(a['tier']) + "]", a['name'])

if __name__ == "__main__":
    main()
