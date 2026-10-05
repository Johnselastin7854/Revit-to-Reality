---
name: debug-stack
description: Systematically debug a problem anywhere in the stack (browser, API, Docker, database, worker, CI) while teaching the method. Use when something is broken, an error appears, a service is unhealthy, or the owner says "it doesn't work".
argument-hint: <symptom, e.g. "status page shows database red">
---

# Debug: $ARGUMENTS

Teach the method while fixing the problem. Narrate each step briefly so the owner can do it alone next time.

## Method

1. **Reproduce.** Get the exact symptom: error text, status code, which command, which URL. Ask the owner to paste it if needed.

2. **Isolate the layer.** Walk the request path and find the first place it goes wrong:
   `browser → web (Next.js) → api (Fastify) → db / storage → worker`

   | Layer | First checks (read-only) |
   |---|---|
   | Browser | DevTools Console and Network: status code, response body, CORS errors |
   | Web / API | terminal output of `pnpm dev`; hit the endpoint directly (`curl http://localhost:<port>/health`) |
   | Docker | `docker compose -f infra/compose.yaml ps` (health), `logs <service>`, `exec <service> sh` |
   | Database | can the service reach it by **service name**, not `localhost`? migrations applied? |
   | Storage | bucket exists? credentials from `.env.example` names set? endpoint URL inside vs outside Docker |
   | Worker | `jobs` / `worker_heartbeats` rows, worker logs, run the job function locally |
   | CI | `gh run view --log-failed`; does it pass locally with the same command? |

3. **Read the real error.** Quote the key line. Explain what it means in plain English.

4. **Form one hypothesis** and test it with **one** change. If wrong, undo it before trying the next.

5. **Fix, then verify** the original symptom is gone and nothing else broke.

6. **Prevent and log.** Suggest a guard (healthcheck, clearer error, test) if cheap, and propose a learning-log row for `docs/LEARNING.md`.

## Rules

- Never print secrets or `.env` contents; refer to variable names only.
- Ask before destructive commands (`down -v`, dropping tables, deleting files).
