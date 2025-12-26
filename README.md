# Claude Skill Creator

A comprehensive toolkit for creating, validating, and packaging Claude Skills using the official [Claude Skills specification](https://code.claude.com/docs/en/skills).

## Overview

The Claude Skill Creator is a meta-skill designed to automate the generation, validation, and packaging of custom Claude Skills. It follows the official Claude Skills specification to ensure all generated skills are compliant and ready for use with Claude.

## Project Structure

```
Claude_Skill/
├── .claude/                    # Claude-specific configurations
│   ├── commands/              # Command definitions
│   └── skills/                # Skill implementations
│       ├── clskill-creator/   # The main Claude Skill Creator implementation
│       └── skills/            # Additional skills
├── .specify/                  # Spec-Driven Development artifacts
│   ├── memory/               # Project constitution
│   ├── scripts/              # Automation scripts
│   └── templates/            # Project templates
├── specs/                     # Feature specifications
│   └── 1-skill-creator/      # Main skill creator specifications
├── history/                   # Prompt history records
│   └── prompts/              # Historical prompts and responses
├── CLAUDE.md                 # Claude Code rules and guidelines
├── python_basics_practical_guide.md # Python guide reference
└── README.md                 # This file
```

## Features

### 1. Skill Creation
- Generate complete `SKILL.md` files with proper YAML frontmatter
- Include Instructions, Examples, and Best Practices sections
- Ask clarifying questions to refine requirements
- Follow official Claude Skills specification

### 2. Skill Validation
- Validate SKILL.md format against official specification
- Provide specific error messages and correction suggestions
- Ensure compliance with Claude's technical requirements

### 3. Skill Packaging
- Package skills into distributable ZIP files
- Create correct directory structure
- Include optional supporting files and assets

## Getting Started

### Prerequisites
- Claude Code environment
- Python 3.8 or higher
- Access to Claude Skills specification

### Installation
The project is designed to work with Claude Code. Simply clone the repository and follow the Claude Code setup instructions for your environment.

### Usage

The Claude Skill Creator can be used through the following workflow:

1. **Describe Your Skill**: Provide a description of the skill you want to create
2. **Refine Requirements**: Answer clarifying questions to specify functionality
3. **Generate Skill**: Receive a complete, validated SKILL.md file
4. **Package for Distribution**: Create a distributable ZIP file

## Core Components

### SKILL.md Template
Located in `.claude/skills/clskill-creator/SKILL.md`, this defines the Claude Skill Creator itself with:
- Name and description
- Instructions for skill creation
- Example usage scenarios
- Best practices and constraints

### Core Scripts
- `create_ai_guide_skill.py`: Main skill creation logic
- `test_skill_creation.py`: Validation and testing utilities
- `demo.py`: Example usage demonstration

### Specification Artifacts
- `specs/1-skill-creator/spec.md`: Detailed feature specification
- `specs/1-skill-creator/plan.md`: Architectural plan
- `specs/1-skill-creator/tasks.md`: Implementation tasks

## Development Workflow

This project follows Spec-Driven Development (SDD) principles:

1. **Specification**: Define requirements in `specs/` directory
2. **Planning**: Create architectural plans in `plan.md` files
3. **Tasking**: Break work into testable tasks in `tasks.md`
4. **Implementation**: Execute tasks with code quality standards
5. **History**: Maintain prompt history in `history/prompts/`

## Key Principles

- **Specification Fidelity**: Always follow official Claude Skills specification
- **Clarity Over Assumptions**: Ask clarifying questions when requirements are incomplete
- **Skill-First Thinking**: Focus on reusable, composable skills
- **Deterministic Output**: Produce predictable, repeatable outputs
- **Validation & Quality Enforcement**: Validate all generated artifacts
- **Safe & Responsible Design**: Ensure all skills are appropriate and secure

## Contributing

1. Create feature specifications in the `specs/` directory
2. Follow the SDD workflow (spec → plan → tasks → implementation)
3. Maintain prompt history records for all changes
4. Ensure all generated skills comply with official specification

## Architecture Decision Records (ADRs)

Significant architectural decisions are documented in `history/adr/` following the project's ADR guidelines.

## Prompt History Records

All user interactions and development decisions are captured as Prompt History Records in `history/prompts/` following the project's PHR guidelines.

## License

This project follows the principles and guidelines established in the project constitution at `.specify/memory/constitution.md`.

## Support

For issues or questions about the Claude Skill Creator:
- Review the specification documents in `specs/1-skill-creator/`
- Check the reference documentation in `.claude/skills/clskill-creator/reference.md`
- Consult the quickstart guide at `.claude/skills/clskill-creator/quickstart.md`
