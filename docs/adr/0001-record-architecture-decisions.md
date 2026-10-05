# ADR-0001: Record architecture decisions

- **Status:** accepted
- **Date:** 2026-10-05
- **Phase:** 0

## Context

This is a long, learning-focused project. Decisions made early (stack, storage, data model) will be questioned later, by me or by an AI agent working in the repo. Without a record, the reasons get lost and decisions get re-argued.

## Decision

Every significant decision gets a short Architecture Decision Record in `docs/adr/`, numbered in order, using [0000-template.md](0000-template.md). Create one with `/adr <title>`.

"Significant" means: it is hard to reverse, it affects more than one app, or it adds a new service or dependency category.

## Consequences

- Decisions are reviewable in pull requests like code.
- Superseded decisions stay in the history with a link to the replacement.
- Small overhead per decision; worth it for the learning value of writing down trade-offs.
