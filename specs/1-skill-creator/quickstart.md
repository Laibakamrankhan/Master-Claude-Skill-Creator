# Quickstart: Claude Skill Creator

## Overview
The Claude Skill Creator is a meta-skill that helps you generate, validate, and package Claude Skills automatically and reliably.

## Prerequisites
- Python 3.11 or higher
- pip package manager
- Access to the Claude Skills specification documentation

## Installation
1. Clone or download the Claude Skill Creator repository
2. Install dependencies: `pip install pyyaml jinja2`
3. Verify installation: `python -c "import yaml, jinja2; print('Dependencies OK')"`

## Basic Usage

### Creating a New Skill
1. Run the skill creator: `python scripts/create_skill.py`
2. Provide a description of your desired skill when prompted
3. Answer clarifying questions to refine the skill requirements
4. Review the generated SKILL.md file

### Validating a Skill
1. Run the validator: `python scripts/validate_skill.py path/to/SKILL.md`
2. Review the validation results and compliance score
3. Make necessary corrections based on feedback

### Packaging a Skill
1. Run the packager: `python scripts/package_skill.py path/to/skill/directory`
2. The tool will create a ZIP file ready for distribution

## Example Workflow
1. Create a new skill for unit conversion:
   - Describe: "A skill that converts between different units of measurement"
   - Answer questions about supported units and conversion types
   - Review generated SKILL.md with instructions and examples

2. Validate your skill:
   - Run validation to ensure compliance with Claude specifications
   - Address any errors or warnings

3. Package for distribution:
   - Create a distributable ZIP file with proper structure

## Next Steps
- Review the complete SKILL.md specification
- Explore example skills in the examples/ directory
- Customize templates for your specific use cases