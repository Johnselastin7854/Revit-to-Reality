# Architecture

This is the target design. It is built up phase by phase; see [ROADMAP.md](ROADMAP.md). Decisions and their reasons live in [adr/](adr/).

## Principles

1. **Modular monolith first.** One API service and one worker. Split only when there is a measured reason.
2. **Adapters in, canonical model out.** Every input format (IFC, PDF, RVT) is converted into the same internal building model. Everything downstream works for every source.
3. **Heavy work never runs inside a request.** Uploads go straight to storage; conversion runs in a queue-driven worker; progress is pushed over WebSockets.
4. **Jobs are idempotent.** Running a job twice must produce the same result, so retries are always safe.
5. **The AI answers from data.** The assistant calls typed tools over the canonical model. If the data does not contain the answer, it says so.
6. **Free tier and local first.** Everything runs on a laptop with Docker; cloud services are free-tier equivalents with the same APIs.

## System overview

```
                 ┌──────────────── Frontend (Next.js + React Three Fiber) ─────────────────┐
                 │ Upload · 3D viewer · PDF plan viewer · Chat · Minimap · Mobile navigation │
                 └──────────────┬──────────────────────────────────┬────────────────────────┘
                                │ REST                             │ WebSocket
                 ┌──────────────▼──────────────┐       ┌───────────▼───────────┐
                 │ API (Fastify, TypeScript)   │◄─────►│ Realtime: job progress│
                 │  · auth, projects, models   │       │ alarms, positions     │
                 │  · AI assistant (tool loop) │       └───────────▲───────────┘
                 │  · MCP server               │                   │ MQTT
                 │  · spatial service (routing)│       ┌───────────┴───────────┐
                 └───┬───────────┬─────────────┘       │ Sensor/alarm simulator│
                     │           │                     └───────────────────────┘
       ┌─────────────▼───┐ ┌─────▼───────────────┐
       │ Postgres        │ │ Object storage      │
       │ + pgvector      │ │ MinIO / R2          │
       │ + pg-boss queue │ │ originals, GLB,     │
       └─────────▲───────┘ │ tiles, PDFs, plans  │
                 │         └─────────▲───────────┘
       ┌─────────┴───────────────────┴──────────── Python worker ────────────────────────┐
       │ IFC adapter (IfcOpenShell) · PDF adapter (PyMuPDF + Shapely) · RVT adapter (later)│
       │ → geometry (GLB / tiles) · elements · rooms · room graph · walkable mesh · plans  │
       └──────────────────────────────────────────────────────────────────────────────────┘
```

## Canonical building model

| Entity | Key fields |
|---|---|
| `project` | id, name, owner |
| `model` | id, project_id, source_type (`ifc` \| `pdf` \| `rvt`), name |
| `model_version` | id, model_id, original_file_key, status, created_at |
| `level` | id, version_id, name, elevation |
| `space` (room) | id, level_id, number, name, function, outline (polygon), area |
| `element` | guid, version_id, level_id, space_id, ifc_class, discipline, system, type_name, props (JSONB), bbox |
| `connection` | from_space, to_space, via (door \| stair \| lift), position |
| `asset_link` | element/space ↔ sensor id, document id |

Geometry lives in object storage, keyed by version. Metadata lives in Postgres and is queried on demand; the browser never holds every property of a large model.

## Key flows

**Upload:** browser gets a presigned URL → uploads straight to storage → `POST /models/:id/versions` → job queued → worker converts → progress over WebSocket → version `ready`.

**"What is this?":** viewer sends the selected GUID → assistant calls `describe_element(guid)` → API returns element, type, system, room, properties → the model explains in plain English.

**"Take me to …":** assistant calls `find_places(query, level)` → if ambiguous, asks → `route(from, to)` runs A* on the room graph and walkable mesh → viewer animates the camera or draws the route; turn instructions are derived from route angles plus landmarks.

**Alarm navigation:** simulator publishes MQTT alarms → API stores and pushes them → "take me to critical alarms on P1" → `get_alarms` → device → space → `route` → turn-by-turn directions.

## Scaling notes (for later phases)

- Split geometry by level and discipline; stream with LOD; use instancing for repeated elements.
- Index `elements` on `(version_id, discipline)`, `(version_id, level_id)` and GIN on `props`.
- Scale workers by queue depth; split huge IFCs by storey.
- Cache geometry on a CDN with content-hash URLs.
- Trace one upload end to end with a single trace id (OpenTelemetry).
