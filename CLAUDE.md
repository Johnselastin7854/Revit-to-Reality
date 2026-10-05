# CLAUDE.md

Claude Code loads this file at the start of every session (desktop app and terminal alike). The shared rules live in AGENTS.md:

@AGENTS.md

## Claude Code specifics

### Current phase

Check [docs/ROADMAP.md](docs/ROADMAP.md) for the phase in progress and its open steps before starting work. The detailed plan for the active phase is in `docs/phases/`.

### Skills (slash commands in `.claude/skills/`)

| Command | Use it when |
|---|---|
| `/teach <topic>` | Before building anything with a new concept |
| `/break-it <step or component>` | After a step works, to practise debugging |
| `/adr <title>` | A significant decision has been made |
| `/phase-checkpoint` | Finishing a step or a phase; updates roadmap and learning log |
| `/debug-stack <symptom>` | Something is broken and the cause is unclear |

### Subagents (`.claude/agents/`)

| Agent | Delegate to it for |
|---|---|
| `tutor` | Concept explanations and quizzes; never edits files |
| `architect` | Design options, trade-offs, ADR drafts, architecture docs |
| `code-reviewer` | Reviewing a diff before commit, with explanations a learner can follow |
| `devops-helper` | Docker, Compose, CI and environment problems |
| `ifc-specialist` | IFC, IfcOpenShell, BIM data and MEP questions |

### Working style

- Prefer the dedicated file tools over shell commands for reading and editing.
- On Windows, give commands for PowerShell unless a script is clearly Bash.
- Keep responses short; put long explanations in `docs/` only when the owner wants to keep them.
