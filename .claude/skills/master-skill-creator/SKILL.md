---
name: master-skill-creator
description: Creates new Claude Code skills with proper structure and documentation. Use when asked to create new skills or when you need to implement a new capability as a skill.
allowed-tools: Write, Read, Bash
---

# Master Skill Creator

## Purpose
This skill helps create new Claude Code skills with proper structure, documentation, and best practices.

## Instructions

### Step 1: Define the Skill
1. Determine the skill's purpose and functionality
2. Choose an appropriate name (lowercase, hyphens only)
3. Write a clear, specific description (under 1024 characters)

### Step 2: Create the Skill Structure
1. Create the skill directory: `mkdir -p .claude/skills/[skill-name]`
2. Create the main SKILL.md file with proper YAML frontmatter
3. Add any supporting files as needed

### Step 3: Generate Content
1. Write clear, step-by-step instructions for the skill
2. Include relevant examples
3. Specify any required tools
4. Add best practices and troubleshooting tips

## Detailed Steps

### 1. Create Skill Directory
```
mkdir -p .claude/skills/[your-skill-name]
```

### 2. Create Main SKILL.md File
```yaml
---
name: [your-skill-name]
description: [Brief description of what this skill does and when to use it]
# Optional: specify allowed tools
# allowed-tools: Read, Write, Bash
---
# [Your Skill Title]

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this skill.

## Best Practices
Include any important considerations or tips.
```

### 3. Add Supporting Files (if needed)
- `REFERENCE.md` - Detailed documentation
- `EXAMPLES.md` - Usage examples
- `scripts/` directory - Helper scripts
- `templates/` directory - Template files

## Examples

### Example: Creating a Git Helper Skill
When asked to create a git helper skill:
1. Create directory: `.claude/skills/git-helper`
2. Generate SKILL.md with git-specific instructions
3. Include common git workflows and commands
4. Specify tools like Bash, Read, Grep

### Example: Creating a Testing Skill
When asked to create a testing automation skill:
1. Create directory: `.claude/skills/test-runner`
2. Include instructions for different test frameworks
3. Add examples for running tests and interpreting results
4. Specify tools like Bash, Grep, Read

## Best Practices

1. **Specific Descriptions**: Make the skill's description specific enough that Claude knows exactly when to use it
2. **Focused Scope**: Each skill should address one main capability
3. **Tool Permissions**: Only allow necessary tools for security
4. **Clear Instructions**: Provide step-by-step guidance that Claude can follow
5. **Examples**: Include concrete examples to help Claude understand usage

## Troubleshooting

- If Claude doesn't use the skill: Check description specificity and file location
- If skill has errors: Verify file paths and dependencies
- For conflicts: Make descriptions more specific with distinct trigger terms