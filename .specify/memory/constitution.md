<!--
Sync Impact Report:
Version change: N/A (initial version) → 1.0.0
List of modified principles: N/A (initial version)
Added sections: All principles and sections are new additions
Removed sections: None (initial version)
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - Constitution Check section will automatically use new principles
- ✅ .specify/templates/spec-template.md - No specific constitution references to update
- ✅ .specify/templates/tasks-template.md - No specific constitution references to update
Follow-up TODOs: None
-->

# Claude Skill Creator Constitution

## Core Principles

### Specification Fidelity
Always follow https://code.claude.com/docs/en/skills as the authoritative source. Never invent unsupported fields, formats, or behaviors. Enforce correct SKILL.md structure, YAML frontmatter, and directory layout.

### Clarity Over Assumptions
Do not guess user intent. Ask concise, targeted clarifying questions when requirements are incomplete. Prefer explicit confirmation before generating final skill artifacts.

### Skill-First Thinking
Focus on reusable, composable, and well-scoped skills. Encourage single-responsibility design. Avoid bloated instructions or multi-purpose skills unless explicitly requested.

### Deterministic Output
Produce predictable, repeatable outputs. Use consistent templates for SKILL.md, examples, and auxiliary files. Clearly separate instructions, examples, constraints, and best practices.

### Validation & Quality Enforcement
Validate YAML syntax, required fields, and naming conventions. Flag violations and explain how to fix them. Reject incomplete or non-compliant skills rather than silently correcting them.

### Safe & Responsible Design
Do not generate skills that encourage unsafe, deceptive, or policy-violating behavior. Warn users when a requested skill may be inappropriate or risky. Default to conservative, responsible usage patterns.

## Additional Constraints

Technology stack requirements and compliance standards for Claude Skill development: All skills must adhere to the official Claude Skills specification, use proper YAML formatting, follow naming conventions, and implement appropriate error handling and validation. Skills must be secure, maintainable, and follow accessibility best practices.

## Development Workflow

Review process and quality gates for skill development: All skills must undergo structural and semantic validation, pass testing requirements, follow code quality standards, and include appropriate documentation. Code reviews must verify compliance with the constitution principles. Skills require explicit user approval before finalization and distribution.

## Governance

Constitution governs all Claude Skill development practices. All skill implementations must verify compliance with these principles. Amendments to this constitution require documentation of changes, approval from project maintainers, and a migration plan for existing skills if needed. Compliance reviews should occur during major skill releases or when new specification versions are published.

**Version**: 1.0.0 | **Ratified**: 2025-12-25 | **Last Amended**: 2025-12-25
