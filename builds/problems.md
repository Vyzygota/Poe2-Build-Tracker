# Znane problemy — tracker

Patrz [monk_invoker.md](monk_invoker.md) dla kontekstu buildu.

---

## Status

| # | Problem | Status | Fix |
|---|---|---|---|
| 1 | Power Charge generation = 0 | ✅ ROZWIĄZANE | Ailith's Chimes na TF |
| 2 | Resistances krytycznie niskie | 🔴 AKTYWNE | Storm Rune + wymiana gear |
| 3 | Brutality I na QS Strike | 🟡 DO WYMIANY | → Lightning Attunement I |
| 4 | Spirit 30/30 (0 wolne) | 🟡 CZEKA | Wzrost Spirit pool przy levelup |

---

## #1 — Power Charge generation ✅

**Fix:** Ailith's Chimes (T1 DEX support) na Tempest Flurry

Tempest Flurry expends Combo przy każdym cyklu → Ailith's Chimes generuje Power Charges na każdym combo expend. Kilka razy na sekundę przy normalnym ataku.

```
Tempest Flurry → Crescendo + Ailith's Chimes  (teraz, 2 sloty)
              → Crescendo + Rapid Attacks + Ailith's Chimes  (gdy 3. slot)
```

Passive bonus: **The Power Within** (dist 5) → +1 max PC, +20% crit dmg.

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
