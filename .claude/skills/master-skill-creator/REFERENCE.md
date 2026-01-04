# Master Skill Creator - Reference Guide

## Skill Creation Checklist

### Before Creating a Skill
- [ ] Identify the specific functionality needed
- [ ] Check if a similar skill already exists
- [ ] Determine the appropriate scope (personal vs project)
- [ ] Plan the skill's name and description

### Skill Structure Requirements
- [ ] Directory named with lowercase letters and hyphens only
- [ ] SKILL.md file with proper YAML frontmatter
- [ ] Valid name (max 64 characters, lowercase, numbers, hyphens)
- [ ] Description under 1024 characters
- [ ] Clear instructions and examples

### YAML Frontmatter Fields
- `name`: Unique identifier for the skill
- `description`: When and why to use this skill
- `allowed-tools`: List of tools Claude can use (optional)

## Advanced Skill Patterns

### Multi-step Skills
For skills that require multiple phases:
1. Create clear phase indicators in instructions
2. Provide checkpoints for validation
3. Include error handling instructions

### Template-based Skills
For skills that generate files:
1. Include template examples
2. Specify variable substitution patterns
3. Validate generated output

### Integration Skills
For skills that work with external tools:
1. Define prerequisites
2. Include authentication patterns
3. Handle common error states

## Common Mistakes to Avoid

### Poor Descriptions
- Vague: "Helps with coding"
- Better: "Generates unit tests for JavaScript functions using Jest framework"

### Overly Broad Permissions
- Instead of allowing all tools, specify only what's necessary
- Consider security implications of each tool

### Unclear Instructions
- Don't assume Claude knows internal details
- Provide step-by-step processes
- Include expected outcomes at each step

## Skill Naming Conventions

### Good Names
- `git-commit-helper`
- `javascript-test-generator`
- `api-documentation-checker`

### Avoid
- `skill123` (too generic)
- `my-skill` (too vague)
- `JavaScript-Test-Generator` (uppercase/casing issues)

## Skill Activation Triggers

To help Claude know when to use your skill, include trigger phrases in the description such as:
- "Use when..."
- "Activate for..."
- "Apply to..."