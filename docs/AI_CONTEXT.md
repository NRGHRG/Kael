# AI Context

Welcome to Project Kael.

This repository is the shared source of truth for every human and AI
contributor. Conversation history can provide useful background, but it must
not override the repository's current code and documentation.

## Required reading

Before proposing or making changes, read:

1. `KAEL_FOUNDATION.md` for Kael's identity, mission, and principles.
2. `PROJECT_STATE.md` for the current sprint and verified project status.
3. `AI_GUIDELINES.md` for collaboration and engineering rules.
4. The code affected by the task.

If these sources disagree, stop and surface the conflict to Memo before making
an architectural decision.

## Project identity

Kael is not a chatbot. Kael is an intelligent desktop companion designed to
help, learn, automate tasks, and evolve alongside its user.

Kael must remain honest, transparent, permission-aware, privacy-respecting,
modular, and understandable.

## Team

- **Memo** — Founder, Product Owner, Tech Lead, and final decision-maker.
- **KaelGPT** — Software architecture, AI design, and code review.
- **Kael Codex** — Implementation, refactoring, testing, and repository work.
- **Git** — Permanent shared project history.

These roles describe responsibilities, not authority over Memo or over the
repository's documented principles.

## Working agreement

1. Work on one clearly scoped objective at a time.
2. Inspect the current repository before suggesting changes.
3. Explain important decisions and trade-offs in plain language.
4. Verify changes before presenting them as complete.
5. Keep `PROJECT_STATE.md` accurate when a sprint or milestone changes.
6. Finish each sprint with a review of architecture, quality, tests, and debt.
7. Do not begin the next sprint until Memo approves the current one.

## Current handoff

Sprint 1, the configuration system, is complete and published. Sprint 2, the
console logger, is complete and published with automated tests for its log
levels. Sprint 3 is focused on BootManager, the startup orchestrator that will
eventually coordinate modules like Pulse, Archive, Echo, Mind, Memory, Voice,
and Vision. Read `PROJECT_STATE.md` before acting because it is the
authoritative status document.
