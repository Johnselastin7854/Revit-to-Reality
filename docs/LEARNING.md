# Learning

This project is a learning vehicle. Nothing gets built until the concept behind it is understood.

## The loop for every step

1. **Learn** — run `/teach <topic>` (or ask the `tutor` agent). Concepts only.
2. **Practise** — a small throwaway exercise in `sandbox/` (git-ignored), never in the real code.
3. **Build** — implement the step in the repo, in small commits.
4. **Break it** — run `/break-it <step>`; cause failures on purpose and fix them.
5. **Write it down** — add a row to the learning log below.

## Topics per phase

| Phase | Learn before building |
|---|---|
| −1 → 0 core | Terminal, Git, HTTP and APIs, TypeScript, React, SQL basics |
| 0 Foundations | Docker (images, containers, volumes, networks, compose, healthchecks, multi-stage builds), monorepos (pnpm, Turborepo), linting/formatting/testing, migrations, CI with GitHub Actions |
| 1 Python warm-up | Syntax, venv and uv, modules, pathlib and JSON, exceptions and logging, dataclasses and type hints, Pydantic, async basics, psycopg, boto3, pytest |
| 2 IFC pipeline | Presigned uploads, object storage, queues, idempotency, WebSockets, IFC structure (project → site → building → storey → elements), GUIDs, property sets, IfcOpenShell, glTF/GLB, Z-up vs Y-up, units, React Three Fiber |
| 3 Canonical model | MEP basics (HVAC, plumbing, electrical, fire), IFC distribution classes and systems, JSONB and GIN indexes, `EXPLAIN ANALYZE`, Zustand selectors, draw calls |
| 4 Spatial layer | Graphs, BFS/Dijkstra/A*, navmeshes, Shapely polygons, bounding boxes, coordinate transforms |
| 5 AI + MCP | Tokens and context windows, tool calling, streaming, prompt injection, MCP (tools, resources, prompts, stdio vs HTTP), typed tools vs text-to-SQL |
| 6 Walk + minimap | Game loop and delta time, pointer lock, collision (capsule vs BVH), physics basics, SVG/Canvas transforms, route → turn instructions |
| 7 PDF adapter | PDF internals (vector vs raster), PyMuPDF drawings and text, line clustering, polygonisation, scale calibration, human-in-the-loop correction |
| 8 Digital twin | IoT basics, MQTT (topics, QoS, retained messages), event-driven design, time-series data, reconnects and backpressure |
| 9 Mobile navigation | Indoor positioning options, QR anchors, device motion and compass, dead reckoning and drift, mobile web UX |
| 10 RAG | Chunking, embeddings, pgvector and HNSW, hybrid search, reranking, citations, eval sets and recall@k |
| 11 MFE + scale | Module Federation, shared singletons, contracts, independent deploys, CDN caching, load testing (k6), OpenTelemetry |

## Debugging habits

| Layer | Look here first |
|---|---|
| Browser | DevTools: Console, Network, Performance; React DevTools |
| API | Server logs, status codes, request/response payloads |
| Docker | `docker compose ps`, `docker compose logs <service>`, `docker compose exec <service> sh` |
| Database | `EXPLAIN ANALYZE`, migration status, constraints |
| Worker | `jobs` table status and error, worker logs, run one job locally |
| 3D | `r3f-perf`, axes and bounding-box helpers |
| AI | Log every tool call with arguments and result; the eval set |

Rule: **reproduce → isolate the layer → read the real error → change one thing at a time.**

## Learning log

| Date | Phase.step | Topic | What I learned (in my own words) | What broke and how I fixed it |
|---|---|---|---|---|
| 2026-10-05 | −1 | Architecture | Adapters feed one canonical model, so IFC, PDF and RVT share the viewer, chat and navigation | — |
| 2026-10-12 | 0.1 | uv | Installed globally with winget, like pnpm; each project's dependencies live in its own `.venv`, like `node_modules` (`pyproject.toml` ≈ `package.json`, `uv.lock` ≈ `pnpm-lock.yaml`) | — |
| 2026-10-12 | 0.1 | Python | `uv python install 3.12` gave 3.12.15 alongside two existing 3.13 installs; the project pins 3.12 with `.python-version`, so uv picks the right one regardless of PATH | — |
| 2026-10-14 | 0.1 | WSL 2 + Docker | Windows Home has no Hyper-V, so Docker Desktop runs its Linux engine inside WSL 2; `docker version` shows a Windows **Client** talking to a Linux **Server**. Docker brings its own internal distro and doesn't need Ubuntu | Ubuntu's first launch failed with `Wsl/Service/E_UNEXPECTED` right after `wsl --install`; WSL features only activate after a restart, and Ubuntu was optional anyway, so I installed Docker Desktop directly |
| 2026-10-14 | 0.1 | Image vs container | `docker run hello-world`: the daemon pulled an **image** (a read-only template) from Docker Hub, created a **container** (a running instance of it), and streamed its output back to the CLI | — |
| 2026-10-14 | 0.1 | Node LTS | Upgraded Node 22 → 24.20 LTS; even-numbered Node versions become LTS, and 22 is now maintenance-only | — |
