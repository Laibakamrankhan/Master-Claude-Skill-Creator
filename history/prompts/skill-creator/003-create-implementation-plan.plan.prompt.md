---
id: 003
title: Create Implementation Plan
stage: plan
date: 2025-12-25
surface: agent
model: Claude Sonnet 4.5
feature: skill-creator
branch: 1-skill-creator
user: Claude Code User
command: sp.plan
labels: ["planning", "architecture", "implementation"]
links:
  spec: specs/1-skill-creator/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-skill-creator/plan.md
 - specs/1-skill-creator/research.md
 - specs/1-skill-creator/data-model.md
 - specs/1-skill-creator/quickstart.md
 - specs/1-skill-creator/contracts/skill-creation-api.yaml
tests:
 - none
---

## Prompt

```text
Objective: Create a "Master Claude Skill Creator" meta-skill that can generate, validate, and package Claude Skills automatically and reliably.

Plan Steps:

1. Requirement Analysis
   - Gather user goals for the skill they want to create.
   - Ask clarifying questions to refine purpose, scope, and outputs.
   - Determine optional supporting files or features (scripts/, assets/, reference.md).

2. Skill Generation
   - Produce a SKILL.md with proper YAML frontmatter: name, description, version.
   - Populate Instructions, Examples, and Best Practices sections.
   - Use templates for consistency.

3. Validation
   - Check SKILL.md structure, YAML syntax, and field requirements.
   - Validate directory structure and auxiliary files if any.
   - Provide error messages and guidance for corrections.

4. Packaging
   - Organize files into a distributable structure:
     `.claude/skills/<skill-name>/`
       - SKILL.md
       - scripts/ (optional)
       - assets/ (optional)
       - reference.md (optional)
   - Optionally generate a ZIP archive for distribution.

5. Testing & Examples
   - Include example user prompts and expected outputs.
   - Include test scripts to verify YAML and structure.

6. Documentation & Instructions
   - Provide clear instructions on how to use the meta-skill.
   - Document validation process and templates.
   - Include notes about customization, extensions, and safe practices.

Success Criteria:
- Skill fully compliant with Claude Skills spec.
- User can generate, refine, validate, and package a skill with minimal manual edits.
- Clear guidance provided for iterative improvement.
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

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

Successfully created the implementation plan for the Claude Skill Creator meta-skill. The plan includes:
- Technical context with language (Python 3.11), dependencies (PyYAML, Jinja2), and platform considerations
- Constitution check ensuring compliance with all principles from the project constitution
- Project structure following Claude's expected format with meta-skill directory
- Research document resolving all technical decisions and alternatives considered
- Data model defining entities (Claude Skill, Validation Result, Distribution Package, Skill Template)
- Quickstart guide for users to get started with the skill creator
- API contract specification for the skill creation, validation, and packaging functionality
- Post-design constitution check confirming all principles are implemented

## Outcome

- ✅ Impact: Comprehensive implementation plan created with all required artifacts for Claude Skill Creator
- 🧪 Tests: No automated tests for planning phase, but all design artifacts validated against constitution
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/skill-creation-api.yaml
- 🔁 Next prompts: Ready to proceed with /sp.tasks to generate implementation tasks
- 🧠 Reflection: Plan addresses all requirements from user input with proper architecture and validation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task generation with /sp.tasks