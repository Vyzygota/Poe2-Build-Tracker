# Claude Code — PoE2 Build Tracker

@AGENTS.md
<!-- NOTE: graphify follows @-includes and indexes AGENTS.md content under both files.
     This creates duplicate god-nodes (e.g. "Global Agent Rules (Minimal Core)" × 2) in the graph.
     This is intentional — AGENTS.md is the universal source of truth for all agents;
     CLAUDE.md is a thin Claude Code overlay that includes it via @. The duplication is
     a faithful representation of the include relationship, not structural drift. -->

## Claude Code Extensions

### Skill Invocation
- Project skills live in `.agents/skills/` and are invoked via the `Skill` tool.
- When the user types `/<skill-name>`, invoke `Skill` tool with the exact name before generating any response.
- Always read `SKILL.md` before executing a complex workflow — skills contain the authoritative steps.

### Audit Pipeline (Claude Code execution path)
- `/self-audit` → `/graphify` (if stale) → feature work. In that order, every session.
- The `Skill` tool is the execution path for all pipeline steps — memory or preferences cannot substitute.
- `graphify` installs a `PreToolUse` hook. After it runs, all `Grep`/`Glob` calls auto-consult the graph.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- ALWAYS read graphify-out/GRAPH_REPORT.md before reading any source files, running grep/glob searches, or answering codebase questions. The graph is your primary map of the codebase.
- IF graphify-out/wiki/index.md EXISTS, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
