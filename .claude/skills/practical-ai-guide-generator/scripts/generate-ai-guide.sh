#!/bin/bash
# Script to help generate new practical AI guides
# Usage: ./generate-ai-guide.sh <topic-name> <output-file>

if [ $# -ne 2 ]; then
    echo "Usage: $0 <topic-name> <output-file>"
    echo "Example: $0 'neural-networks' 'neural-networks-guide.md'"
    exit 1
fi

TOPIC_NAME=$1
OUTPUT_FILE=$2

# Create the basic structure for an AI guide
cat > "$OUTPUT_FILE" << EOF
# ${TOPIC_NAME^} - Practical Guide

## Introduction
An introduction to ${TOPIC_NAME} and its significance in AI.

## Prerequisites
What you need to know before starting this guide.

## Basic Concepts
Fundamental concepts related to ${TOPIC_NAME}.

## Practical Examples
Hands-on examples with code and explanations.

## Advanced Topics
More complex aspects of ${TOPIC_NAME}.

## Real-World Applications
How ${TOPIC_NAME} is used in practice.

## Exercises
Practice problems to reinforce learning.

## Summary
Key takeaways from this guide.

## Next Steps
Where to go next to continue learning about ${TOPIC_NAME}.
EOF

echo "AI guide for '$TOPIC_NAME' created successfully at $OUTPUT_FILE"
echo ""
echo "Next steps:"
echo "1. Customize the content for your specific topic"
echo "2. Add detailed explanations and examples"
echo "3. Include code snippets and visual aids"
echo "4. Add exercises and solutions"
echo "5. Review and refine the content"