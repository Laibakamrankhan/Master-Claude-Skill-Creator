# Master Skill Creator - Examples

## Example 1: Creating a Python Testing Skill

**User Request**: "Create a skill that helps generate Python unit tests"

**Using Master Skill Creator**:
1. Create directory: `.claude/skills/python-test-generator`
2. Generate SKILL.md with Python testing instructions
3. Include examples for pytest and unittest
4. Specify tools: Bash, Read, Write, Grep

**Generated SKILL.md**:
```yaml
---
name: python-test-generator
description: Generates Python unit tests for functions and classes. Use when asked to create test files or add tests to existing code.
allowed-tools: Read, Write, Grep
---
# Python Test Generator

## Instructions
1. Analyze the target Python file
2. Identify functions and classes to test
3. Generate appropriate test cases using pytest
4. Follow AAA pattern (Arrange, Act, Assert)

## Examples
- Generate tests for a calculator module
- Create parameterized tests for edge cases
- Mock external dependencies in tests
```

## Example 2: Creating a Documentation Skill

**User Request**: "Create a skill that helps with API documentation"

**Using Master Skill Creator**:
1. Create directory: `.claude/skills/api-documentation-helper`
2. Include OpenAPI/Swagger guidelines
3. Add examples for different API documentation formats
4. Specify tools: Read, Write, Grep, Bash

## Example 3: Creating a Build System Skill

**User Request**: "Create a skill for managing npm packages"

**Using Master Skill Creator**:
1. Create directory: `.claude/skills/npm-package-manager`
2. Include common npm commands and workflows
3. Add dependency analysis instructions
4. Specify tools: Bash, Read, Grep

## Example 4: Creating a Security Check Skill

**User Request**: "Create a skill that audits code for security vulnerabilities"

**Using Master Skill Creator**:
1. Create directory: `.claude/skills/security-auditor`
2. Include common vulnerability patterns to look for
3. Add instructions for different languages/frameworks
4. Specify tools: Grep, Read, Bash

## Example 5: Creating a Code Review Skill

**User Request**: "Create a skill that performs code reviews"

**Using Master Skill Creator**:
1. Create directory: `.claude/skills/code-reviewer`
2. Include review criteria and checklists
3. Add examples of good review comments
4. Specify tools: Read, Grep, Bash