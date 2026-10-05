# Phase 0 · Foundations

**Goal:** a working skeleton where every layer talks to the next one, running locally in Docker, checked by CI. No product features yet.

**Definition of done**
- `docker compose -f infra/compose.yaml up -d` starts Postgres and MinIO, and both report healthy
- `pnpm dev` starts web and api; `http://localhost:3000` shows a status page with green checks for **API**, **database**, **storage** and **worker**
- The worker (Python, in Docker) writes a heartbeat row to the database every 10 seconds
- A pull request on GitHub runs CI (lint, typecheck, tests for TS and Python) and it passes
- ADRs 0001–0003 exist; the learning log has an entry for each step
- You can explain, without notes: image vs container, volume vs bind mount, why `localhost` fails between containers, what a migration is, what CI runs and why

**How to work through it:** for each step, run `/teach <topic>` for anything new, do the practice exercise in a throwaway folder, then build the step in the repo, then run `/break-it <step>`. Finish with `/phase-checkpoint`.

---

## 0.0 Project docs and Claude Code setup ✅

README, AGENTS.md, CLAUDE.md, `.claude/skills`, `.claude/agents`, roadmap, architecture, ADRs, concept film.

## 0.1 Tools

**Install**
- Git, GitHub account, GitHub CLI (`gh`)
- Node.js LTS (24.x or newer LTS) and pnpm (`npm install -g pnpm`)
- Python 3.12 and uv (`pip install uv`, or the official installer)
- Docker Desktop with the WSL 2 backend
- VS Code with: ESLint, Prettier, Python, Ruff, Docker, EditorConfig
- Claude Code (desktop and/or terminal)

**Verify**
```bash
git --version && gh --version && node -v && pnpm -v && python --version && uv --version && docker version && docker compose version
```

**Learn:** what WSL 2 is and why Docker Desktop uses it; PATH and environment variables.

## 0.2 Git and GitHub workflow

**Learn:** commits, branches, merge vs rebase, pull requests, `.gitignore`, `.gitattributes` (line endings on Windows), Conventional Commits.

**Build**
- Repository on GitHub, `main` protected (no direct pushes once CI exists)
- Branch naming: `phase-0/compose-stack`, `fix/worker-heartbeat`
- Commit style: `feat(api): add /health endpoint`, `docs: add ADR-0003`
- PR template already in `.github/pull_request_template.md`

**Practice:** in a throwaway repo, create a merge conflict on purpose and resolve it.

## 0.3 Monorepo skeleton

**Learn:** what a monorepo is; pnpm workspaces; Turborepo task pipeline and caching; how TypeScript project references and shared packages work.

**Build**
```
apps/web            Next.js (App Router, TypeScript, Tailwind)
apps/api            Fastify + TypeScript, GET /health
apps/worker         Python 3.12 project managed by uv
packages/shared-types
packages/config     tsconfig.base.json, eslint config
pnpm-workspace.yaml, turbo.json, package.json (root scripts: dev, build, lint, typecheck, test)
```

**Practice:** create two tiny packages where one imports a function from the other.

## 0.4 Code quality tooling

**Learn:** linting vs formatting vs type checking; why tests run in CI.

**Build**
- TypeScript `strict: true`, ESLint, Prettier, Vitest (one sample test in api)
- Python: ruff (lint + format), pytest (one sample test), Pydantic installed
- `.editorconfig` already present

## 0.5 Docker Compose dev stack

**Learn:** image vs container vs registry; Dockerfile instructions; layers and build cache; volumes vs bind mounts; container networking and service names; environment variables; healthchecks; `depends_on`; multi-stage builds.

**Build** `infra/compose.yaml`
- `db`: `pgvector/pgvector:pg16`, named volume, healthcheck with `pg_isready`
- `storage`: MinIO (S3-compatible, same API as Cloudflare R2), console on port 9001, bucket `models` created on start
- `worker`: built from `apps/worker/Dockerfile`, depends on `db` being healthy
- `.env.example` with every variable documented; real `.env` ignored by git

**Practice:** containerise a 10-line Express app plus Postgres; delete the container and prove the data survived in the volume.

## 0.6 Database migrations and first schema

**Learn:** what a migration is and why we never edit the database by hand; up vs down; UUID keys; foreign keys; indexes; transactions.

**Build** with dbmate (plain SQL files, works for both TS and Python)
- `projects`, `models`, `model_versions`, `jobs`, `elements` (skeleton columns only)
- `worker_heartbeats` (used in 0.7)
- `CREATE EXTENSION vector;` to confirm pgvector works

**Practice:** write a migration, roll it back, change it, apply again.

## 0.7 Hello-world slice

**Learn:** HTTP status codes, JSON APIs, CORS, how the browser calls an API, connection pools.

**Build**
- api `GET /health` → checks database (`SELECT 1`) and storage (list bucket) → `{ api, db, storage, worker }`
- worker → every 10 s inserts into `worker_heartbeats`; api reports the worker as healthy if the last beat is under 30 s old
- web `/` → status page with four checks, refreshing every 5 s

## 0.8 CI

**Learn:** what CI is; GitHub Actions workflow, jobs, steps, caching, service containers, secrets.

**Build** `.github/workflows/ci.yml`
- Job `node`: pnpm install (cached) → lint → typecheck → test
- Job `python`: uv sync → ruff check → pytest
- Job `docker`: build the worker image
- Turn on branch protection: CI must pass before merging to `main`

## 0.9 Break-it drills

Run `/break-it phase-0`, or do these:
1. Point the api at `localhost` for the database while it runs inside Docker. Read the error, explain why, fix it.
2. Change the exposed Postgres port in compose only. Find what broke and where.
3. `docker compose down -v` — watch the data disappear; explain what `-v` removed.
4. Stop the worker. Watch the status page turn red after 30 s.
5. Push a type error. Read the failing CI log and fix it.
6. Break a migration (syntax error). See how dbmate reports it and recover.

Log each drill in [../LEARNING.md](../LEARNING.md).

## 0.10 Checkpoint

Run `/phase-checkpoint`. It checks the definition of done, updates the roadmap, and writes the phase summary.
