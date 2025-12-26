---
name: Claude Skill Creator
description: A meta-skill that helps users generate, validate, and package Claude Skills automatically and reliably
version: 1.0.0
---

# Claude Skill Creator

## Instructions

This meta-skill helps you create new Claude Skills by guiding you through the process of defining your skill's purpose, capabilities, and behavior. Follow these steps:

1. Describe the purpose and capabilities of the skill you want to create
2. Answer clarifying questions to refine the requirements
3. Review and customize the generated skill content
4. Validate the skill structure and compliance
5. Package the skill for distribution

The tool will generate a complete SKILL.md file with proper YAML frontmatter, detailed instructions, examples, and best practices.

## Examples

### Example 1
**User:** I want to create a skill for unit conversion
**Claude:**
1. What types of units would you like to convert? (e.g., length, weight, temperature, currency)
2. What's the primary use case for this skill?
3. Do you want to include specific conversion examples?

Based on your answers, I'll generate a complete unit conversion skill with examples.

### Example 2
**User:** Help me create a calendar assistant skill
**Claude:**
1. What calendar services should the skill integrate with? (Google, Outlook, etc.)
2. What operations should the skill support? (schedule, reschedule, check availability)
3. What information should users provide when making requests?

I'll create a calendar assistant skill with appropriate examples and best practices.

### Example 3
**User:** I need a skill to help with code review
**Claude:**
1. What programming languages should the skill focus on?
2. What aspects of code review should it address? (style, best practices, security, performance)
3. Should it provide specific examples of good vs bad code patterns?

I'll generate a code review skill with relevant instructions and examples.

## Best Practices

- Be specific about the skill's purpose and scope to get better results
- Consider edge cases and error handling when describing requirements
- Include specific examples of how users might interact with the skill
- Think about the target audience and their technical level
- Validate the generated skill to ensure it meets Claude's requirements
- Test the skill with sample prompts before finalizing