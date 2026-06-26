# Notatki, pytania, eksperymenty

## 2026-06-06 — Start projektu

### Kontekst sezonu
- Nowy sezon, pierwsze przejście kampanii
- Rynek (trade) zablokowany — pure self-found do czasu odblokowania
- Gemy tylko z: dropów z potworów, vendorów NPC, nagród za questy

### Preferencje gracza
- Lubi duelistów: mobilność, combo, szybkie bicie + element magii
- W PoE2 nie ma duelissy → Monk Invoker jako najbliższy odpowiednik
- Irytacja: quarterstaffs biją za wolno (auto-ataki) → rozwiązanie: Tempest Flurry

### Otwarte pytania
- [x] Jak aktywnie wykorzystać dual maces secondary? → **Set II = boss set.** Mace Strike + Uul-Netol's Embrace (Chaos + Armour Break). Switch na najtrudniejszych bossach.
- [x] Jaka jest dobra kolejność ascendancy nodów? → **"I am the Thunder" → "Sunder my Enemies" → "Scatter" → "Master"**
- [x] Czy inwestować w Chaos Resistance podczas leveling? → **TAK, dla survivalu.** Twoja chaos res = obrona przed wrogami. Chaos dmg który zadajesz = trafia przez WROGÓW chaos resistance (early game: 0%). Obie rzeczy, różne mechaniki.

### Do przetestowania
- [x] Tempest Flurry zamiast auto-ataków — tak, to main attack od lvl 12+
- [x] Herald of Thunder vs Herald of Ice → **Herald of Thunder** (synergia z lightning build). Rozważyć: Herald of Agony (chaos-based) gdy Chaos system będzie gotowy.
- [ ] Esh's Radiance na Thunderstorm — przetestować Chaos → Shock buildup
- [x] Power Charge generation — **rozwiązane: Ailith's Chimes (T1 DEX) na Tempest Flurry**
  - Combo expend → chance to gain Power Charges (kilka razy/sec przy TF)
  - Passive: The Power Within (dist 5) → +1 max PC, +20% crit dmg
  - SKIP: Resonance (dist 8) — brak frenzy gen na ścieżce, nieopłacalne

## 2026-06-08 — Sesja 7

### Kierunek budowy: Lightning + Chaos
- Tematycznie: DarthLuke Skywalker = Force Lightning + Dark Side Chaos
- Chaos secondary: nigdy immune, Esh's Radiance = chaos buduje Shock (oba elementy → jeden ailment)
- Graf graficznym (graphify): 10 communities, god node = Monk Invoker Ascendancy (12 edges)

### Biblioteka socketables (gotowa)
- 77 basic runes, 34 ancient runes, 17 warding runes, 89 named runes
- 78 abyss soul cores, 13 verisium alloys, 9 jewels, 31 talismans
- Pliki: skill_graph.json, support_gems.json (c:\GitHUB\Poe2\)
- Regeneracja: `python build_graph.py` + `python build_socketables.py`
