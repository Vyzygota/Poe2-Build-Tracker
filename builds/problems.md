# Znane problemy — tracker

Patrz [monk_invoker.md](monk_invoker.md) dla kontekstu buildu.

---

## Status

| # | Problem | Status | Fix |
|---|---|---|---|
| 1 | Power Charge generation | 🔴 AKTYWNE | Ailith's Chimes = lvl 65 drop-only, niedostępne teraz |
| 2 | Resistances | 🔄 ONGOING | Naturalne uzupełnianie w trakcie gry |
| 3 | Brutality I na QS Strike | 🟡 DO WYMIANY | → Lightning Attunement I |
| 4 | Spirit 30/30 (0 wolne) | 🟡 CZEKA | Wzrost Spirit pool przy levelup |

---

## #1 — Power Charge generation 🔴

**Ailith's Chimes** (T1 DEX lineage support) — mechanicznie idealny fix (combo expend → Power Charges), ale:
- `is_lineage: true` — drop-only, NIE craftowany z Uncut Support Gem
- Wymagany poziom: **65** (ten sam próg co Mjölnir)

⚠️ Poprzednia sesja błędnie oznaczyła jako "ROZWIĄZANE" — wymaga weryfikacji alternatyw.

**Plan długoterminowy:** Ailith's Chimes + Mjölnir = endgame package (lvl 65).

**Teraz (lvl 22):** szukamy alternatywy do generacji Power Charges. Do ustalenia.

---

## #2 — Resistances 🔴

**Stan:** Fire: -48% | Lightning: -42% | Cold: +18%  
**Cel:** 75% cap WSZYSTKICH przed Act 2

**Działania:**
1. Storm Rune (Lesser/Normal) w każdy dostępny gear slot
2. Wymiana itemów na te z Fire/Lightning Res
3. Ire of Aldur na rings — konwertuje Fire/Cold mody gear → Lightning

---

## #3 — Brutality I na QS Strike 🟡

**Problem:** Brutality support usuwa elemental damage z QS Strike.  
**Fix:** Wymień → Lightning Attunement I (ten sam T1, INT, dodaje Lightning dmg do ataków)

---

## #4 — Spirit 30/30 🟡

**Problem:** Herald of Thunder rezerwuje całe 30 Spirit. Żadna nowa aura nie wejdzie.  
**Fix:** Pasywki zwiększające Spirit pool (np. "Lead me through Grace..." Invoker node — dist 3, ale to asc punkt) lub gear z +Spirit.  
**Teraz:** Czekaj na naturalny wzrost Spirit przy levelup.
