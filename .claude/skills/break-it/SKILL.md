---
name: break-it
description: Design failure drills for a working step or component so the owner learns to debug it (wrong ports, missing volumes, failed migrations, CI errors, race conditions). Use after a step works, or when the owner says "break it" or wants debugging practice.
argument-hint: <phase step or component, e.g. "0.5 compose stack" or "worker">
---

# Break it: $ARGUMENTS

Goal: the owner deliberately causes realistic failures and fixes them, so real failures later are familiar.

## Steps

1. **Read the current state** of the component: the relevant files, the phase file in `docs/phases/`, and any drills already listed there. Confirm it currently works (ask the owner to run it, or run read-only checks like `docker compose ps`).

2. **Propose 3–5 drills**, ordered easy to hard. For each:
   - **Break:** the exact change or command to make (small and fully reversible).
   - **Predict:** ask the owner what they think will happen *before* they run it.
   - **Symptom:** what they will see (error text, status code, red check).
   - **Where to look:** the log, tool or file that reveals the cause.
   - **Hint ladder:** three hints from vague to specific. Reveal one at a time, only when asked.
   - **Fix and why:** hidden until they have fixed it or asked for the answer.

3. **Run drills one at a time.** Wait for the owner to try each drill. Do not apply the break yourself unless they ask.

4. **Restore and verify.** After each drill, make sure everything is back to working (`git status` clean, services healthy).

5. **Log it.** Propose a learning-log row per drill for `docs/LEARNING.md` ("What broke and how I fixed it").

## Rules

- Never break anything that is hard to undo: no deleting volumes with real work, no force-pushes, no history rewrites.
- Drills happen on a branch or with uncommitted changes that are reverted afterwards.
- Prefer failures that happen in real projects over contrived ones.
