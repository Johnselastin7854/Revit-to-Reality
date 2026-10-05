# AGENTS.md

Instructions for AI coding agents (Claude Code, and any other tool that reads AGENTS.md) working in this repository.

## Project

**Revit to Reality**: upload a building model (IFC, PDF floor plan, later Revit) and explore it in the browser: 3D viewer, MEP discipline filters, AI assistant, walkthrough with minimap, indoor navigation, digital twin. See [README.md](README.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/ROADMAP.md](docs/ROADMAP.md).

## This is a learning project — read this first

The owner is building this to learn system design, architecture, RAG, MCP, micro frontends and DevOps. They know JavaScript well and are learning Python, Docker and the rest. **Their understanding matters more than speed.**

1. **Teach before you build.** When a task touches a concept the owner has not logged in `docs/LEARNING.md`, explain it briefly first (what it is, why we need it here, one small example) and check they are ready before writing project code.
2. **Small steps.** One concept per change. No large, multi-file generations without agreeing on the plan first.
3. **Explain commands before running them**, especially Docker, Git and database commands. Say what each flag does.
4. **Leave the owner's exercises to the owner.** If a step in `docs/phases/` is marked as practice, guide with hints instead of writing the solution, unless they ask for it.
5. **Show your reasoning on trade-offs.** When there are options, give a recommendation and why. Record significant decisions as an ADR (`/adr`).
6. **After each step:** suggest a `/break-it` drill and a one-line entry for the learning log.

## Hard constraints

- **Free tier only.** Do not introduce paid services or dependencies that require payment. If something has a free tier with limits, say so.
- **No real project data.** Only public sample models in `samples/`. Never commit company models, client drawings or credentials.
- **No secrets in git.** Use `.env` (ignored) and keep `.env.example` documented. Never read or print the contents of `.env` files.
- **Ask before adding a dependency.** Say what it does, why it is needed, and whether a smaller option exists.
- **Do not push, merge, or change GitHub settings** unless the owner asks in this session.

## Stack

| Area | Choice |
|---|---|
| Web | Next.js (App Router), TypeScript, React Three Fiber, Drei, Zustand, Tailwind |
| API | Fastify + TypeScript; AI assistant and MCP server live here (later phases) |
| Worker | Python 3.12, uv, IfcOpenShell, Shapely, PyMuPDF, Pydantic, psycopg, boto3 |
| Data | PostgreSQL 16 + pgvector; pg-boss queue; dbmate SQL migrations |
| Storage | MinIO locally, Cloudflare R2 in the cloud (S3 API) |
| AI | Ollama locally or Gemini free tier, behind a provider interface |
| Tooling | pnpm workspaces, Turborepo, ESLint, Prettier, Vitest, ruff, pytest |
| DevOps | Docker Compose, GitHub Actions |

Decisions and reasons: [docs/adr/](docs/adr/).

## Repository layout

```
apps/web            Next.js frontend
apps/api            Fastify API
apps/worker         Python conversion worker (uv project)
packages/shared-types   TS types shared by web and api
packages/config     shared tsconfig and eslint config
db/migrations       dbmate SQL migrations
infra/compose.yaml  local dev stack
samples/            public sample files only
sandbox/            throwaway practice exercises (git-ignored)
docs/               roadmap, architecture, learning, phases, ADRs
```

Parts of this layout are created during Phase 0; check what exists before assuming.

## Commands

Fill these in as Phase 0 creates them. Until then, they do not exist.

| Task | Command |
|---|---|
| Install | `pnpm install` · `cd apps/worker && uv sync` |
| Dev stack | `docker compose -f infra/compose.yaml up -d` |
| Dev servers | `pnpm dev` |
| Lint / typecheck / test (TS) | `pnpm lint` · `pnpm typecheck` · `pnpm test` |
| Lint / test (Python) | `cd apps/worker && uv run ruff check . && uv run pytest` |
| Migrations | `dbmate up` · `dbmate rollback` |
| Logs | `docker compose -f infra/compose.yaml logs -f <service>` |

## Conventions

- TypeScript `strict`; no `any` without a comment explaining why.
- Python: type hints everywhere, Pydantic models at boundaries, `logging` not `print`.
- Names: `camelCase` in TS, `snake_case` in Python and SQL, `kebab-case` for files and folders in TS apps.
- Commits: Conventional Commits (`feat(api): …`, `fix(worker): …`, `docs: …`, `chore: …`).
- Branches: `phase-N/short-name`, `fix/short-name`.
- Every PR fills in the template, including "What I learned".
- Jobs must be idempotent; heavy work never runs inside an HTTP request.
- Shell: the owner is on Windows 11 with PowerShell and Git Bash. Use `docker compose` (v2), not `docker-compose`.

## Domain glossary

| Term | Meaning |
|---|---|
| BIM | Building Information Modelling: 3D model plus data about every element |
| IFC | Open BIM file format (buildingSMART). Revit can export it |
| GUID / GlobalId | Unique id of an IFC element; links 3D meshes to data |
| Storey / level | `IfcBuildingStorey` |
| Space / room | `IfcSpace`, with name, number and outline |
| Pset | Property set attached to an element (e.g. `Pset_WallCommon`) |
| MEP | Mechanical (HVAC), Electrical, Plumbing, plus Fire Protection |
| Discipline | ARCH, STR, HVAC, PLB, ELEC, FIRE |
| Canonical model | Our internal schema that every adapter produces ([ADR-0003](docs/adr/0003-canonical-building-model.md)) |
| Digital twin | 3D model linked to live sensor and alarm data |

## Definition of done (any task)

- It runs, and the relevant lint, typecheck and tests pass.
- Docs updated if behaviour or commands changed (`AGENTS.md` commands table, phase file checkboxes).
- The owner can explain what changed and why.
