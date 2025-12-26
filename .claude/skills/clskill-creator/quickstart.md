# Quickstart Guide: Claude Skill Creator

## Overview

The Claude Skill Creator is a meta-skill that helps you generate, validate, and package Claude Skills automatically and reliably. This guide will help you get started quickly.

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Install required dependencies:
  ```bash
  pip install pyyaml jinja2
  ```

## Step 1: Create a New Skill

To create a new Claude Skill interactively:

```bash
cd .claude/skills/clskill-creator
python -m cli.skill_creator
```

Follow the prompts to describe your skill:
1. Name your skill
2. Describe what it does
3. Provide detailed instructions
4. Add example interactions
5. Define best practices

## Step 2: Validate Your Skill

After creating your skill, validate it to ensure it meets Claude's requirements:

```bash
python scripts/validate_skill.py path/to/your/SKILL.md
```

Fix any errors or warnings shown by the validator.

## Step 3: Package for Distribution

To package your skill for distribution:

```bash
python scripts/package_skill.py path/to/skill/directory output.zip
```

## Example Workflow

Here's a complete example of creating a simple calculator skill:

1. **Start the creator:**
   ```bash
   python -m cli.skill_creator
   ```

2. **Provide skill information:**
   - Name: "Calculator Helper"
   - Description: "A skill that helps with basic calculations"
   - Instructions: "Help users perform basic arithmetic operations like addition, subtraction, multiplication, and division."
   - Example: "User: What's 15 + 27? | Claude: 15 + 27 = 42"

3. **Validate the skill:**
   ```bash
   python scripts/validate_skill.py Calculator_Helper_skill.md
   ```

4. **Package for distribution:**
   ```bash
   python scripts/package_skill.py . Calculator_Helper_skill.md packaged_calculator.zip
   ```

## Running Tests

To verify the Claude Skill Creator is working properly:

```bash
python test_skill_creation.py
```

## Next Steps

- Review the [reference documentation](reference.md) for advanced usage
- Look at the [examples](examples/) directory for sample skills
- Customize the [templates](templates/) for your specific needs
- Integrate the skill creation process into your workflow

## Troubleshooting

**If validation fails:**
- Check that your SKILL.md starts with YAML frontmatter (`---`)
- Ensure all required sections (Instructions, Examples, Best Practices) are present
- Verify your YAML syntax is correct

**If packaging fails:**
- Make sure the skill directory contains a SKILL.md file
- Check that file paths are correct

**For more help:**
- Review the [reference documentation](reference.md)
- Examine the [example skills](examples/)