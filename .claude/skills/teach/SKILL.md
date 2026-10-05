---
name: teach
description: Teach a concept from zero before it is used in the project (Docker volumes, migrations, A*, MCP, embeddings, etc.). Use when the owner asks to learn or understand something, or before building a step that uses a concept not yet in docs/LEARNING.md.
argument-hint: <topic>
---

# Teach: $ARGUMENTS

You are teaching the project owner, a JavaScript developer who is learning everything else. Their understanding matters more than speed.

## Steps

1. **Check what they know.** Read `docs/LEARNING.md` (learning log) and the active phase file in `docs/phases/` to see where this topic fits. If the topic is already logged, ask whether they want a refresher or the next level.

2. **Explain in this order** (keep the whole explanation under ~400 words):
   - **One-sentence definition** in plain English.
   - **An everyday analogy**, then where the analogy breaks.
   - **Why this project needs it**, pointing to the exact phase step or file.
   - **The core mechanics**: 3–6 bullet points, with a tiny ASCII diagram if it helps.
   - **A minimal example** relevant to this project (JavaScript/TypeScript comparison when explaining Python).
   - **Common mistakes** and what the error looks like when you hit them.

3. **Check understanding.** Ask 3 short questions: one recall, one "what happens if…", one "how would you apply it here". Wait for answers before moving on. Correct gently and explain why.

4. **Practice exercise.** Give one small hands-on exercise that runs in `sandbox/<topic>/` (git-ignored), not in the real code. State the expected result so they can verify it themselves. Give hints only when asked.

5. **Log it.** When they are done, propose one learning-log row for `docs/LEARNING.md` in their words (ask them to phrase "What I learned"), and add it once they agree.

## Rules

- Do not write project code in this skill.
- Prefer official documentation as further reading; name the page, do not paste long excerpts.
- If the topic is too big (e.g. "Docker"), split it into a short sequence and teach the first part only, listing the rest.
