# Revit to Reality

> Upload a building model (IFC, Revit or a PDF floor plan) and explore it in the browser: filter MEP disciplines, ask an AI assistant about any element, walk through it with a game-style minimap, get turn-by-turn directions to rooms and alarms, and run it as a live digital twin.

**Status:** 🟡 Phase 0 · Foundations — see [docs/ROADMAP.md](docs/ROADMAP.md)
**Type:** learn-and-build project · free tiers only
**Concept film:** open [docs/concept-film/revit-to-reality-film.html](docs/concept-film/revit-to-reality-film.html) in a browser (86 s, with narration)

---

## What it will do

| Area | Capability |
|---|---|
| **Ingest** | Upload `.ifc` (Revit export), `.pdf` floor plans, later native `.rvt` via an adapter. Background workers convert everything into one canonical building model. |
| **View** | Streamed 3D viewer that stays smooth on large models. Exploded view, X-ray, section cuts, measure, element inspector. |
| **Disciplines** | Toggle Architecture, Structure, HVAC, Plumbing, Electrical and Fire Protection. Isolate a system, colour by system. |
| **AI assistant** | "What is this?", "Show unfinished sprinkler lines on Level 12", "Take me to the ground floor AHU room". The assistant calls typed tools (also exposed as an **MCP server**) and answers from model data, not guesses. |
| **Walk + minimap** | First-person walkthrough with collision, a GTA-style rotating minimap, full floor map, room labels and a route line. |
| **Indoor navigation** | Google-Maps-style turn-by-turn directions inside the building, in 3D and on a phone (QR-code positioning). |
| **PDF plans** | Plan viewer with scale calibration, then automatic wall and room extraction, then a simple walkable 3D model. |
| **Digital twin** | Simulated sensors and alarms over MQTT, heatmaps by room, "take me to the critical alarm on P1". |
| **Documents (RAG)** | Ask questions about specs and manuals, with citations. |

## Why this project exists

It is a vehicle for learning, one real feature at a time:

- **System design** — queues, idempotency, caching, scaling a heavy conversion pipeline
- **Architecture** — modular monolith first, adapters, a canonical data model, ADRs
- **RAG** — chunking, embeddings, hybrid search, evals
- **MCP** — exposing the platform's tools to any AI client
- **Micro frontends** — splitting the UI once the monolith works
- **DevOps basics** — Docker, CI/CD, environments, observability

Every phase follows the same loop: **learn → practise → build → break it on purpose → write down what you learned.** Details in [docs/LEARNING.md](docs/LEARNING.md).

## Architecture (target)

```
 .ifc ─► IFC adapter ─┐
 .pdf ─► PDF adapter ─┼─► Canonical building model ─► Viewer · Chat · Navigation · Twin
 .rvt ─► RVT adapter ─┘   (levels, rooms, elements,
        (Python worker)    geometry, room graph)

 Frontend (Next.js + React Three Fiber)
      │ REST                       │ WebSocket
 API + AI assistant + MCP (TS) ◄──► Realtime (jobs, alarms, positions)
      │
 Postgres + pgvector · S3-compatible storage (MinIO local / Cloudflare R2) · pg-boss queue
```

Full design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Decisions: [docs/adr/](docs/adr/).

## Tech stack (free tier)

| Layer | Choice |
|---|---|
| Frontend | Next.js (App Router), TypeScript, React Three Fiber, Drei, Zustand, Tailwind |
| API, AI assistant, MCP server | Node.js + TypeScript (Fastify), MCP TypeScript SDK |
| Conversion worker | Python 3.12, IfcOpenShell, Shapely, PyMuPDF, Pydantic |
| Database | PostgreSQL 16 + pgvector |
| Queue | pg-boss (runs inside Postgres) |
| File storage | MinIO locally, Cloudflare R2 in the cloud (S3-compatible API) |
| AI models | Ollama (local, free) or Google Gemini API free tier |
| Real-time / IoT | WebSockets, Mosquitto (MQTT) |
| Tooling | pnpm workspaces, Turborepo, ESLint, Prettier, Vitest, uv, ruff, pytest |
| DevOps | Docker Compose, GitHub Actions, Sentry free plan |

## Repository layout

What exists today is marked ✅. Everything else is created during Phase 0.

```
revit-to-reality/
├── README.md                ✅
├── AGENTS.md                ✅ instructions for AI coding agents
├── CLAUDE.md                ✅ Claude Code entry point (imports AGENTS.md)
├── .claude/
│   ├── settings.json        ✅ shared permissions
│   ├── skills/              ✅ /teach /break-it /adr /phase-checkpoint /debug-stack
│   └── agents/              ✅ tutor, architect, code-reviewer, devops-helper, ifc-specialist
├── docs/                    ✅ roadmap, architecture, learning, phases, ADRs, concept film
├── apps/
│   ├── web/                 Next.js frontend
│   ├── api/                 Fastify API (+ AI assistant, MCP server later)
│   └── worker/              Python conversion worker
├── packages/
│   ├── shared-types/        TypeScript types shared by web and api
│   └── config/              shared tsconfig / eslint config
├── db/migrations/           SQL migrations (dbmate)
├── infra/compose.yaml       local dev stack (Postgres, MinIO, worker)
├── samples/                 public sample IFC / PDF files only
└── .github/                 CI workflow, PR template ✅
```

## Getting started

Phase 0 is in progress, so there is nothing to run yet. Follow [docs/phases/phase-0-foundations.md](docs/phases/phase-0-foundations.md) step by step. When it's done, this section will read:

```bash
pnpm install
docker compose -f infra/compose.yaml up -d
pnpm dev
```

## Working with Claude Code

The project is set up for Claude Code. The same files work in the desktop app and in the terminal (`claude`), because both read them from the repository:

| File | Purpose |
|---|---|
| `CLAUDE.md` | Loaded automatically at the start of every session; imports `AGENTS.md` |
| `AGENTS.md` | Project rules, stack, conventions, learning-first workflow (also readable by other AI tools) |
| `.claude/skills/*` | Slash commands: `/teach`, `/break-it`, `/adr`, `/phase-checkpoint`, `/debug-stack` |
| `.claude/agents/*` | Specialist subagents: tutor, architect, code-reviewer, devops-helper, ifc-specialist |
| `.claude/settings.json` | Shared permissions (safe read-only commands allowed, secrets blocked) |

Personal settings go in `.claude/settings.local.json`, which git ignores.

## Data and confidentiality

Only use **public sample models** (for example the buildingSMART sample files) in this repository. Never commit real project models, client drawings or credentials.

## License

To be decided.
