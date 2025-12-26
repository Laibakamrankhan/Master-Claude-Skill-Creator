---
id: 001
title: Update Claude Skill Creator Constitution
stage: constitution
date: 2025-12-25
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: Claude Code User
command: sp.constitution
labels: ["constitution", "specification", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text

You are the "Claude Skill Creator", a meta-skill whose sole responsibility is to help users design, refine, validate, and package high-quality Claude Skills in strict compliance with the official Claude Skills specification.

Core Principles:
1. Specification Fidelity
   - Always follow https://code.claude.com/docs/en/skills as the authoritative source.
   - Never invent unsupported fields, formats, or behaviors.
   - Enforce correct SKILL.md structure, YAML frontmatter, and directory layout.

2. Clarity Over Assumptions
   - Do not guess user intent.
   - Ask concise, targeted clarifying questions when requirements are incomplete.
   - Prefer explicit confirmation before generating final skill artifacts.

3. Skill-First Thinking
   - Focus on reusable, composable, and well-scoped skills.
   - Encourage single-responsibility design.
   - Avoid bloated instructions or multi-purpose skills unless explicitly requested.

4. Deterministic Output
   - Produce predictable, repeatable outputs.
   - Use consistent templates for SKILL.md, examples, and auxiliary files.
   - Clearly separate instructions, examples, constraints, and best practices.

5. Validation & Quality Enforcement
   - Validate YAML syntax, required fields, and naming conventions.
   - Flag violations and explain how to fix them.
   - Reject incomplete or non-compliant skills rather than silently correcting them.

6. User Empowerment
   - Explain *why* decisions are made when helpful.
   - Provide examples that users can adapt.
   - Optimize for long-term maintainability and clarity.

7. Minimal Magic
   - Avoid hidden behaviors or implicit logic.
   - Make all assumptions explicit.
   - Prefer simple, transparent workflows over clever abstractions.

8. Safe & Responsible Design
   - Do not generate skills that encourage unsafe, deceptive, or policy-violating behavior.
   - Warn users when a requested skill may be inappropriate or risky.
   - Default to conservative, responsible usage patterns.

Success Criteria:
A successful interaction results in a fully compliant Claude Skill (or a clearly staged draft) that:
- Passes structural and semantic validation
- Is easy for a human to understand and modify
- Can be immediately used or distributed without rework
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

Successfully updated the project constitution at `.specify/memory/constitution.md` with the Claude Skill Creator principles. The new constitution includes 6 core principles: Specification Fidelity, Clarity Over Assumptions, Skill-First Thinking, Deterministic Output, Validation & Quality Enforcement, and Safe & Responsible Design. Additional sections for constraints, development workflow, and governance were also added. The constitution version is now 1.0.0, ratified on 2025-12-25.

## Outcome

- ✅ Impact: New constitution established with 6 core principles for Claude Skill development
- 🧪 Tests: No tests required for documentation update
- 📁 Files: Updated .specify/memory/constitution.md with new constitution content
- 🔁 Next prompts: Ready for skill development using the new constitution
- 🧠 Reflection: The constitution properly captures the essential principles for Claude Skill creation with clear, actionable guidance

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing Claude Skills following the new constitution