# Monk — Invoker Ascendancy
**Archetype:** Lightning + Chaos | dual weapon sets | DarthLuke Skywalker  
**Tematycznie:** Force Lightning (primary) + Dark Side Chaos (backup — never immune)  
**Status:** Leveling | Act 1 | Level 19

---

## Jak działa ten build (core loop)

```
Set I (QS — clear):
  Tempest Flurry [x3 ciosy] → generuje combo → Crescendo (4. cios = AoE lightning)
  Thunderstorm   [drop + idź] → pasywny AoE, buduje Shock przez Esh's Radiance (Chaos → Shock!)
  Spark          → projectile lightning cleanup

Set II (Dual Mace — boss):
  Mace Strike → Uul-Netol's Embrace (Chaos + Armour Break) per hit
  Thunderstorm  → współdzielony, ciągnie oba sety
```

**Dlaczego Chaos jako secondary:**
- Lightning immunity u niektórych bossów = 0 damage. Chaos NIE MA immunities w PoE2.
- Esh's Radiance: Chaos damage buduje Shock — oba elementy wzmacniają TEN SAM ailment.
- Fenumus' Rune of Agony ×2 = +26% auto-Chaos na każdym hicie bez dodatkowego skilla.

---

## Dlaczego Invoker?

1. **"I am the Thunder..."** — +% dmg jako Lightning, porażenie tworzy naładowany grunt
2. **"Sunder my Enemies..."** — Crits ignorują elemental resistancje wrogów *(ogromne dla lightning+chaos)*
3. **"...and Scatter Them to the Winds"** — Elemental Expression: melee crit = automatyczny czar
4. **"Master of the Elements"** — bonus elemental dmg

---

## Aktywne skille (lvl 19, PoB potwierdzone)

| Skill | Set | Supporty | Uwagi |
|---|---|---|---|
| Tempest Flurry lvl 5 | I (QS) | Crescendo + Rapid Attacks I | Main attack, combo builder |
| Falling Thunder lvl 5 | I (QS) | Rapid Attacks I + Perpetual Charge | QS-only — porzucić przy wejściu na Seeing Stars |
| Thunderstorm lvl 5 | oba | Spell Echo + **Esh's Radiance** | Chaos → Shock buildup! |
| Spark lvl 4 | oba | brak (Pierce I = #1 priorytet) | |
| Mace Strike lvl 6 | II (mace) | Rapid Attacks I + **Uul-Netol's Embrace** | Chaos + Armour Break |
| Armour Breaker lvl 4 | II (mace) | Armour Demolisher I + Armour Explosion | Utility opancerzeni |
| Herald of Thunder lvl 4 | oba | Magnified Area I + Lightning Attunement | Rezerwuje całe Spirit 30/30 |
| Quarterstaff Strike lvl 6 | I (QS) | Rapid Attacks I + Brutality I | **Brutality usuwa elemental! Zamienić.** |

> **[!] Thunderstorm support do zmiany:** Prolonged Duration → Esh's Radiance gdy zdobędziesz.

---

## Roadmapa broni

```
lvl 19 now  →  QS (Tempest Flurry) + 2× dowolne 1H mace
lvl 26      →  QS + 2× Seeing Stars (+66-90 flat lightning each, energy gen ×2)
lvl 65      →  QS + 2× Mjölnir Torment Club (214 Str + 200 Int)
               "Level 15 Lightning Spell on Hit" × 2 = każdy atak odpala 2 lightning spelle
```

**Seeing Stars** (lvl 26 one-hand mace): priorytet farm/trade przy wejściu do Act 2–3.

---

## Passive Tree — priorytety

### Teraz (lvl 19, Act 1)
- **Resistances FIX:** Fire -48%, Lightning -42% — krytyczne przed Act 2
- **Staunching** (dist 6 od startu, +10 Str) → buduje Str do Mjölnira
- **Tenfold Attacks** (dist 7, +10 Str) → j.w.

### Act 2–3
- Power Charge generation/retention nodes ← **PRIORYTET** (patrz sekcja poniżej)
- Attack Speed (Tempest Flurry skaluje mocno)
- Lightning Damage

### Endgame
- Critical Strike Chance (base crit Monk + Invoker "Sunder" = crits ignorują res)
- Elemental Penetration
- Evasion / Energy Shield hybrid

---

## ⚠️ Znane problemy — do naprawienia

### 1. Power Charge generation = 0 [KRYTYCZNE]
- power_charges_max: 3, ale generacja = 0
- **Tymczasowe rozwiązanie:** Perpetual Charge na Falling Thunder (trzyma ładunki)
- **Docelowo:** pasywka "Power Charge on Critical Strike" lub Invoker "I am the Thunder..." (generuje przy Shock)
- Bez ładunków Invoker ascendancy nie pracuje na pełnych obrotach

### 2. Resistances za niskie [KRYTYCZNE przed Act 2]
- Fire: -48% | Lightning: -42% | Cold: +18%
- Fix: Lesser/Storm Rune w każdy slot gear który możesz; wymiana itemów z resists

### 3. Brutality I na QS Strike [DO WYMIANY]
- Brutality usuwa elemental damage — sprzeczne z lightning buildem
- Wymienić na: Rapid Attacks II lub Lightning Attunement I

### 4. Spirit: 30/30 (0 wolne)
- Herald of Thunder zajmuje wszystko
- Przy levelu nie wchodzi nic nowego dopóki nie wzrośnie Spirit pool

---

## Ascendancy — kolejność nodów (potwierdzona)

1. **"I am the Thunder..."** ← pierwszy punkt Lab (Normal Lab, po Act 3)
2. **"Sunder my Enemies..."** ← Cruel Lab
3. **"...and Scatter Them to the Winds"** ← Merciless Lab
4. **"Master of the Elements"** ← Endgame Lab

---

## Gem rekomendacje (z bazy repoe-fork)

| Skill | Top supports gry |
|---|---|
| Thunderstorm | Lightning Penetration, Shock Conduction, **Esh's Radiance** |
| Tempest Flurry | Shock, Lightning Attunement, Momentum, Crescendo |
| Spark | **Pierce I** (nr 1!), Zenith I, Electrocute |
| Mace Strike | **Uul-Netol's Embrace**, Close Combat II, Culling Strike II |

---

## Plan runiczny (endgame)

| Slot | Runa | Efekt |
|---|---|---|
| Mace ×2 | Legacy of Brain Rattler | Każde trafienie → Electrocution buildup |
| Mace ×2 | Legacy of Mjölner | +3 Level all Lightning Skills |
| Helm / Chest | Fenumus' Rune of Agony ×2 | +26% auto-Chaos total |
| Gloves / Boots | Storm Rune lub Greater Storm Rune | +14–18% Lightning Resistance |
| Rings | Ire of Aldur | Konwertuje Fire+Cold mody → Lightning |
| Amulet | Saqawal's Rune of the Sky | +5% dmg jako wszystkie elementy |

---

## Statystyki (lvl 19)
- Life: 361 · ES: 158 · Evasion: 296
- Fire: **-48%** · Lightning: **-42%** · Cold: +18%
- Str: 31 · Dex: 42 · Int: 35
- Spirit: 30/30 (full — Herald rezerwuje wszystko)

---

## Sesja — log zmian

| Data | Co się zmieniło |
|------|----------------|
| 2026-06-06 | Stworzenie pliku. Monk lvl 9, staff + dual maces |
| 2026-06-06 | Mechanika: Falling Thunder = Power Charge finisher, Tempest Flurry T5 |
| 2026-06-08 | Upgrade do lvl 19. Dual weapon sets potwierdzone. Lightning+Chaos kierunek ustalony |
| 2026-06-08 | Chaos system: Esh's Radiance + Uul-Netol + Fenumus ×2. Plan runiczny endgame. |
| 2026-06-08 | Biblioteka socketables: 77 basic runes, 89 named runes, 78 soul cores, 13 alloys |
