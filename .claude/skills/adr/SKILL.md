---
name: adr
description: Create an Architecture Decision Record in docs/adr/ for a significant decision (new service, library choice, data model change, hard-to-reverse trade-off). Use when the owner says "write an ADR" or a decision has just been agreed.
argument-hint: <decision title>
---

# ADR: $ARGUMENTS

1. List `docs/adr/` and take the next number after the highest existing one (four digits, e.g. `0004`).
2. Copy the structure of `docs/adr/0000-template.md`. File name: `NNNN-kebab-case-title.md`.
3. Fill in from the conversation:
   - **Context**: the problem and constraints (free tier, learning goals, scale).
   - **Options considered**: at least two real options with honest pros and cons.
   - **Decision**: one or two sentences.
   - **Consequences**: what gets easier, harder, and what to revisit.
4. Leave **What I learned** for the owner: ask them for one or two lines in their own words.
5. Status is `proposed` until the owner says it is accepted.
6. If it replaces an older ADR, set the old one's status to `superseded by ADR-NNNN` and link both ways.
7. If the decision changes the stack or conventions, update the matching section of `AGENTS.md` and mention it.

Keep the ADR under one page.
