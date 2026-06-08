# Workflow — PoE2 Build Tracker (DarthLuke)

## 2026-06-08 — Sprint: Fix resists + Ailith's Chimes

- **Goal:** DarthLuke Monk lvl 19 → przetrwać Act 2. Dwa zadania blokujące postęp.
- **Stack:** PoE2 patch 0.5 "Runes of Aldur", Invoker Monk, dual weapon set
- **Blockers:**
  - 🟡 Ailith's Chimes (T1 DEX support) — do craftowania z Uncut Support Gem T1
- **Ongoing (nie blokery):**
  - 🔄 Resistances — uzupełniają się naturalnie z gear/levelup, nie blokują postępu

## 2026-06-08 — Decision: Lightning + Chaos jako dual-element system

- **Decision:** Chaos jako secondary element obok Lightning (primary).
- **Rationale:** Chaos nigdy nie ma immunity w PoE2 → pokrywa lightning-immune bossów. Shock jako wspólny ailment (Esh's Radiance sprawia że chaos builduje Shock tak samo jak lightning).
- **Blockers:** brak

## 2026-06-08 — Decision: Audit Pipeline order w AGENTS.md

- **Decision:** Dodano Sekcję 5 (Audit Pipeline) z restrykcyjną kolejnością 10 kroków. CLAUDE.md przerobiony na thin `@AGENTS.md` overlay.
- **Rationale:** Sesja działająca bez zdefiniowanego pipelinu nie może być audytowana we właściwej kolejności — restart był wymagany.
- **Commit:** `5dcf36d`
- **Blockers:** brak

## Roadmapa endgame

| Etap | Wymagania | Cel |
|---|---|---|
| Teraz (lvl 19) | Fix resists → Ailith's Chimes → The Power Within | Przeżyć Act 2 |
| lvl 26 | 2× Seeing Stars (mace) | +150 flat lightning total |
| lvl 65 | 214 Str + 200 Int | 2× Mjölnir — Dual Lightning Spell on Hit |
