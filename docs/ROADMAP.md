# Roadmap

Status key: ✅ done · 🟡 in progress · ⬜ not started

Every phase runs the same loop: **learn → practise → build → break it → write it down.**
The learning topics for each phase are in [LEARNING.md](LEARNING.md). Update this file with `/phase-checkpoint`.

| # | Phase | Status | Outcome |
|---|---|---|---|
| −1 | Discovery & design | ✅ | Requirements, architecture, learning plan, concept film |
| 0 | Foundations | 🟡 | Monorepo, Docker dev stack, database, CI, "hello world" through every layer |
| 1 | Python warm-up | ⬜ | Read an IFC, list levels/rooms/elements, export JSON |
| 2 | IFC pipeline + viewer | ⬜ | Upload → queue → worker → GLB + elements → 3D viewer |
| 3 | Canonical model + discipline filters | ⬜ | One schema for all sources; MEP toggles, model tree, inspector |
| 4 | Spatial layer | ⬜ | Rooms, room graph, walkable mesh, "fly to room" |
| 5 | AI assistant + MCP | ⬜ | `describe_element`, `find_places`, `navigate_to`; MCP server |
| 6 | Walk + minimap + directions | ⬜ | First-person walk, minimap, turn-by-turn in 3D |
| 7 | PDF adapter | ⬜ | Plan viewer → wall/room extraction → walkable 3D |
| 8 | Digital twin + alarms | ⬜ | Simulated sensors over MQTT, heatmaps, "go to critical alarm" |
| 9 | Mobile indoor navigation | ⬜ | Phone web app, QR positioning, live directions |
| 10 | RAG on documents | ⬜ | Q&A over specs and manuals with citations and evals |
| 11 | Micro frontends + scale | ⬜ | Module Federation split, streaming large models, load tests |
| later | Native `.rvt` adapter | ⬜ | Via Autodesk APS when budget allows |

---

## Phase −1 · Discovery & design ✅

- [x] Read and reviewed the original architecture draft; listed its gaps (upload limits, `.rvt` reality, single-GLB scaling, metadata in one JSON column, polling)
- [x] Target system architecture: adapters → canonical model → services
- [x] Scaling review for large federated models
- [x] Feature set: MEP filters, AI assistant, walkthrough, minimap, PDF plans, indoor navigation, digital twin
- [x] How the AI understands elements (model data, not drawings) and how navigation is derived from IFC spaces
- [x] Indoor positioning options (QR codes first, free)
- [x] Learning curriculum per phase
- [x] Stack and free-tier decisions ([ADR-0002](adr/0002-tech-stack-and-free-tier.md))
- [x] Concept film with narration ([concept-film/](concept-film/))

## Phase 0 · Foundations 🟡

Full plan: [phases/phase-0-foundations.md](phases/phase-0-foundations.md)

- [x] 0.0 Project docs and Claude Code setup (README, AGENTS.md, CLAUDE.md, skills, agents)
- [x] 0.1 Tools installed and verified
- [ ] 0.2 Git + GitHub workflow
- [ ] 0.3 Monorepo skeleton (pnpm + Turborepo)
- [ ] 0.4 Code quality tooling (TS + Python)
- [ ] 0.5 Docker Compose dev stack (Postgres + pgvector, MinIO)
- [ ] 0.6 Database migrations + first schema
- [ ] 0.7 Hello-world slice: web → api → db + storage, worker heartbeat
- [ ] 0.8 CI on GitHub Actions
- [ ] 0.9 Break-it drills done and logged
- [ ] 0.10 Phase checkpoint + learning summary

## Phase 1 onwards

Each phase gets its own file in `docs/phases/` when it starts, using the Phase 0 file as the template.
