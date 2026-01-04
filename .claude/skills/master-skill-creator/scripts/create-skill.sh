#!/bin/bash
# Script to help create new Claude Code skills
# Usage: ./create-skill.sh <skill-name> <skill-description>

if [ $# -ne 2 ]; then
    echo "Usage: $0 <skill-name> <skill-description>"
    echo "Example: $0 'git-helper' 'Helps with common git operations'"
    exit 1
fi

SKILL_NAME=$1
SKILL_DESCRIPTION=$2

# Validate skill name format
if [[ ! $SKILL_NAME =~ ^[a-z0-9-]+$ ]]; then
    echo "Error: Skill name must contain only lowercase letters, numbers, and hyphens"
    exit 1
fi

# Create skill directory
SKILL_DIR=".claude/skills/$SKILL_NAME"
mkdir -p "$SKILL_DIR"

# Create SKILL.md file
cat > "$SKILL_DIR/SKILL.md" << EOF
---
name: $SKILL_NAME
description: $SKILL_DESCRIPTION
---
# $(echo $SKILL_NAME | sed 's/^-/\U&/g' | sed 's/-/ /g')

## Instructions
Provide clear, step-by-step guidance for Claude.

## Examples
Show concrete examples of using this skill.

## Best Practices
Include any important considerations or tips.
EOF

echo "Skill '$SKILL_NAME' created successfully at $SKILL_DIR"
echo "Files created:"
echo "- $SKILL_DIR/SKILL.md"
echo ""
echo "Next steps:"
echo "1. Review and customize the generated SKILL.md file"
echo "2. Add any supporting files as needed"
echo "3. Test the skill with Claude"