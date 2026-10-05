# ADR-0002: Tech stack and free-tier constraint

- **Status:** accepted
- **Date:** 2026-10-05
- **Phase:** 0

## Context

- The owner knows JavaScript and is willing to learn Python.
- The project is experimental: every service must be free (local or free tier).
- The best free libraries for BIM and geometry (IfcOpenShell, Shapely, PyMuPDF) are Python.
- Learning goals include system design, RAG, MCP, micro frontends and DevOps basics.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| TypeScript only (web-ifc for IFC) | One language | Weaker IFC tooling; no Shapely/PyMuPDF equivalents of the same quality |
| Python backend + TS frontend | Strong BIM tooling everywhere | Owner's strongest language unused on the backend |
| **TypeScript everywhere + Python worker only** | Plays to existing skills; Python only where it is clearly better | Two toolchains in one repo |

## Decision

- **TypeScript:** web (Next.js + React Three Fiber), API (Fastify), AI assistant, MCP server, realtime.
- **Python 3.12:** the conversion worker only (IFC, PDF, geometry).
- **Data:** PostgreSQL 16 + pgvector; pg-boss for the queue (no extra service).
- **Storage:** MinIO locally, Cloudflare R2 in the cloud; both speak the S3 API, so code does not change.
- **AI:** Ollama locally, or the Google Gemini API free tier. The assistant code talks to a small provider interface so models can be swapped.
- **Tooling:** pnpm workspaces, Turborepo, ESLint, Prettier, Vitest, uv, ruff, pytest, dbmate migrations.
- **DevOps:** Docker Compose locally, GitHub Actions for CI.

## Consequences

- The worker runs on the owner's machine during development; free cloud hosting for it is decided later (most free options need a card for verification).
- Supabase Auth is deferred to the phase that needs users; Phase 0 uses plain Postgres to learn Docker and SQL directly.
- Free-tier limits change; check the provider's current limits when each service is introduced.
- Native `.rvt` reading is not free; the RVT adapter waits until a budget exists (Revit users export IFC in the meantime).
