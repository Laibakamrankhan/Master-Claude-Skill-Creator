# Master Skill Creator

## Overview

The Master Skill Creator is a Claude Code skill designed to help users create new Claude Code skills with proper structure, documentation, and best practices. This skill serves as a template and guide for generating high-quality, reusable skills that follow established patterns.

## Purpose

Creating Claude Code skills requires specific structure and documentation standards. The Master Skill Creator simplifies this process by providing:

- Proper directory structure setup
- Standardized skill file templates
- Documentation guidelines
- Best practices for skill development

## Features

- **Skill Structure Generation**: Creates the proper directory structure for new skills
- **Template Creation**: Generates standard files including SKILL.md, README.md, REFERENCE.md, and EXAMPLES.md
- **Documentation Standards**: Ensures proper documentation follows established guidelines
- **Best Practices Integration**: Incorporates security and usability best practices from the start

## Usage

To use the Master Skill Creator:

1. **Define Your Skill**:
   - Determine the skill's purpose and functionality
   - Choose an appropriate name (lowercase with hyphens)
   - Write a clear, specific description (under 1024 characters)

2. **Run the Skill Creator**:
   ```
   /master-skill-creator
   ```

3. **Follow the Prompts**:
   - Provide the skill name
   - Describe the skill's purpose
   - Specify required tools and permissions
   - Define input parameters if needed

## Skill Structure

The Master Skill Creator generates the following structure:

```
.claude/skills/[skill-name]/
├── SKILL.md          # Main skill definition and instructions
├── README.md         # Usage documentation
├── REFERENCE.md      # Detailed reference material
├── EXAMPLES.md       # Usage examples
└── scripts/          # Optional helper scripts
```

## Best Practices

### Skill Design
- **Specific Descriptions**: Make the skill's description specific enough that Claude knows exactly when to use it
- **Focused Scope**: Each skill should address one main capability
- **Tool Permissions**: Only allow necessary tools for security
- **Clear Instructions**: Provide step-by-step guidance that Claude can follow
- **Examples**: Include concrete examples to help Claude understand usage

### Security Considerations
- Limit tool permissions to only what's necessary
- Avoid overly broad file system access
- Validate inputs when possible
- Follow the principle of least privilege

### Documentation
- Include clear usage instructions
- Provide relevant examples
- Document any prerequisites
- Explain expected outputs

## Examples

### Creating a Git Helper Skill
```
Skill Name: git-helper
Description: Provides common Git operations and workflows
Tools: Bash, Read, Grep
```

### Creating a Testing Automation Skill
```
Skill Name: test-runner
Description: Automates running and interpreting test suites
Tools: Bash, Read, Write
```

## Troubleshooting

### Skill Not Recognized
- Verify the skill directory is in the correct location (`.claude/skills/`)
- Check that the SKILL.md file follows the proper YAML frontmatter format
- Ensure the skill name uses only lowercase letters and hyphens

### Tool Permissions Issues
- Review and minimize the tools specified in your skill definition
- Test the skill with minimal permissions first
- Add additional permissions only as needed

### Structure Problems
- Ensure all required files are present
- Verify file permissions allow reading
- Check that YAML frontmatter is properly formatted

## Contributing

When contributing to the Master Skill Creator or creating new skills:

1. Follow the established patterns and structure
2. Include comprehensive examples
3. Document any special requirements
4. Test the skill thoroughly before sharing
5. Update documentation as needed

## License

This skill follows the same licensing terms as Claude Code and is provided as part of the Claude Code skill framework.
