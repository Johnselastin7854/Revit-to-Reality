---
name: phase-checkpoint
description: Review progress on the current phase against its plan and definition of done, update docs/ROADMAP.md and the phase file, and write a learning summary. Use when the owner finishes a step or phase, or asks "where are we?" / "what's next?".
argument-hint: [phase number, defaults to the one in progress]
---

# Phase checkpoint $ARGUMENTS

1. **Find the phase.** Read `docs/ROADMAP.md`; use the argument, or the phase marked 🟡. Open its file in `docs/phases/`.

2. **Verify, don't assume.** For each unchecked step, check the evidence with read-only actions:
   - files exist (Glob/Read),
   - `docker compose -f infra/compose.yaml ps` shows healthy services,
   - `pnpm lint`, `pnpm typecheck`, `pnpm test`, `uv run pytest` pass (if they exist yet),
   - latest CI run status (`gh run list --limit 3`) if the repo is on GitHub.
   Report each step as done / partly done / not started, with the evidence.

3. **Check understanding.** For the definition-of-done "you can explain" items, ask the owner 2–3 of them. Mark them done only when the answer is right.

4. **Update docs** (show the diff before writing):
   - tick finished steps in the phase file and in `docs/ROADMAP.md`;
   - when every step is done, mark the phase ✅ and the next one 🟡, and create `docs/phases/phase-N-<name>.md` for the next phase from the Phase 0 file's structure (goal, definition of done, steps with Learn / Build / Practice, break-it drills, checkpoint);
   - make sure the learning log has entries for this phase; ask for any missing ones.

5. **Summarise** in under 10 lines: what was finished, what is left, the single next step, and which `/teach` topic to start with.
