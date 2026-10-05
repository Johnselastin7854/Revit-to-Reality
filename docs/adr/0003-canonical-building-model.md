# ADR-0003: Source adapters and a canonical building model

- **Status:** accepted
- **Date:** 2026-10-05
- **Phase:** 0 (implemented from Phase 3)

## Context

The app must accept IFC files now, PDF floor plans later, and native Revit files eventually. The viewer, AI assistant, navigation and digital twin should not care which format a building came from.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| Treat IFC as the internal format; convert PDFs to IFC | One format | Writing valid IFC from rough PDF data is hard and lossy |
| Separate pipelines per format | Simple at first | Every feature has to be built three times |
| **Adapters → canonical model** | Features are built once; new formats only need an adapter | We must design and maintain our own schema |

## Decision

Each input format has an **adapter** in the Python worker that produces the same **canonical building model**: levels, spaces (rooms), elements, connections (doors, stairs, lifts), geometry files and a room graph. See [ARCHITECTURE.md](../ARCHITECTURE.md#canonical-building-model).

Adapters declare what they could fill in (e.g. a PDF has no MEP systems and no real heights), and features degrade gracefully when data is missing.

## Consequences

- Viewer, chat, navigation and twin are written once against the canonical model.
- The schema needs versioning as it grows.
- PDF-sourced buildings show fewer features; the UI must make that clear.
