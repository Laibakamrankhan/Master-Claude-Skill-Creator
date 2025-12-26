# Claude Skill Creator - Reference Documentation

## Overview

The Claude Skill Creator is a meta-skill that helps you generate, validate, and package Claude Skills automatically and reliably. It follows the official Claude Skills specification and provides a complete workflow for skill development.

## Installation

1. Ensure you have Python 3.11+ installed
2. Install required dependencies:
   ```bash
   pip install pyyaml jinja2
   ```

## Usage

### Creating a New Skill

To create a new Claude Skill interactively:

```bash
python -m cli.skill_creator
```

Or specify an output path:
```bash
python -m cli.skill_creator path/to/my_skill.md
```

The tool will guide you through:
1. Describing your skill's purpose and capabilities
2. Answering clarifying questions to refine requirements
3. Adding detailed instructions and examples
4. Defining best practices

### Validating a Skill

To validate a SKILL.md file:

```bash
python scripts/validate_skill.py path/to/SKILL.md
```

This checks:
- YAML frontmatter structure (name, description, version)
- Required sections (Instructions, Examples, Best Practices)
- Content quality and compliance with Claude Skills specification
- Provides a compliance score and suggestions for improvement

### Packaging a Skill

To package a skill for distribution:

```bash
python scripts/package_skill.py path/to/skill/directory [output_path] [--no-supporting-files]
```

Options:
- `--no-supporting-files`: Exclude optional supporting files (scripts, assets, etc.)

## Directory Structure

```
.claude/skills/clskill-creator/
├── SKILL.md                 # Meta-skill definition
├── scripts/
│   ├── validate_skill.py    # Validation script
│   └── package_skill.py     # Packaging script
├── templates/
│   └── skill_template.md    # Template for generating new skills
├── lib/
│   └── skill_generator.py   # Core skill generation logic
├── cli/
│   └── skill_creator.py     # Interactive CLI interface
├── services/
│   ├── question_flow.py     # Clarifying questions logic
│   └── skill_service.py     # Skill creation orchestration
├── models/
│   └── validation_result.py # Validation result model
├── examples/                # Example skills
└── reference.md             # This documentation
```

## Template Variables

The skill template supports these variables:
- `{{ skill_name }}` - Name of the skill
- `{{ skill_description }}` - Description of the skill
- `{{ version }}` - Version number
- `{{ instructions }}` - Detailed instructions
- `{{ examples }}` - List of example interactions
- `{{ best_practices }}` - Best practices for the skill

## Validation Rules

The validator checks for:

### YAML Frontmatter
- Must contain `name`, `description`, and `version` fields
- Name should be descriptive and not too long
- Version should follow semantic versioning (X.Y.Z)

### Required Sections
- `Instructions` section with detailed guidance
- `Examples` section with user/assistant interactions
- `Best Practices` section with usage guidelines

### Content Quality
- Minimum length requirements for content
- Proper formatting and structure
- Compliance with Claude's safety guidelines

## Best Practices

### For Skill Creation
1. Be specific about the skill's purpose and scope
2. Consider your target audience and their technical level
3. Include practical examples that demonstrate real use cases
4. Think about edge cases and error handling
5. Follow Claude's safety and usage guidelines

### For Validation
1. Always validate your skill before distribution
2. Address all errors and warnings before finalizing
3. Aim for a high compliance score (90%+ recommended)
4. Test the skill with sample prompts

### For Distribution
1. Package with supporting files if they're needed
2. Use descriptive names and clear descriptions
3. Include comprehensive examples
4. Document any special requirements or limitations

## API and Integration

The Claude Skill Creator can be integrated programmatically:

```python
from lib.skill_generator import ClaudeSkill, SkillGenerator
from services.skill_service import SkillCreationService

# Create a skill programmatically
skill = ClaudeSkill(name="My Skill", description="A useful skill")
skill.instructions = "Detailed instructions here..."
skill.examples = [{"user_input": "Example query", "assistant_response": "Example response"}]
skill.best_practices = "Best practices here..."

# Generate the skill file
generator = SkillGenerator()
generator.save_skill(skill, "output_path.md")
```

## Troubleshooting

### Common Issues

**YAML Error**: Check that your frontmatter starts and ends with `---`
**Missing Sections**: Ensure all required sections (Instructions, Examples, Best Practices) are present
**Invalid Name**: Skill names should be descriptive and follow naming conventions

### Getting Help

If you encounter issues:
1. Validate your skill to see specific error messages
2. Check the examples directory for reference implementations
3. Review the Claude Skills specification for requirements