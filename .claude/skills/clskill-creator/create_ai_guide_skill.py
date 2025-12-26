#!/usr/bin/env python3
"""
Script to create the AI Practical Guide Generator skill programmatically
"""

import sys
import os
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from lib.skill_generator import ClaudeSkill, SkillGenerator


def create_ai_guide_skill():
    """Create the AI Practical Guide Generator skill programmatically"""

    # Create the skill object
    skill = ClaudeSkill(
        name="AI Practical Guide Generator",
        description="Generates practical, step-by-step AI guides or tutorials based on a topic or task provided by the user. The guides are easy to follow, actionable, and include examples, code snippets (if relevant), and best practices."
    )

    # Set the instructions
    skill.instructions = """Act as an AI Practical Guide Generator. When users request information about AI topics, tools, or workflows, provide structured, practical guides that are easy to follow and actionable.

Your response should include:
1. Step-by-step instructions for the requested topic
2. Example applications or use cases
3. Tips and best practices
4. Optional code or workflow snippets if relevant
5. References to useful libraries or tools when applicable

For each guide you create:
- Start with a brief overview of the topic
- Break down the process into clear, sequential steps
- Include practical examples that users can follow
- Provide best practices and potential pitfalls to avoid
- Offer actionable advice that users can immediately implement
- If the user's request is unclear, ask clarifying questions about their specific needs or use case

The goal is to create comprehensive, practical guides that help users implement AI solutions effectively."""

    # Add examples
    skill.examples = [
        {
            "user_input": "Generate a practical guide for building a recommendation system with Python.",
            "assistant_response": """# Building a Recommendation System with Python - Practical Guide

## Overview
This guide will walk you through building a recommendation system using Python, covering the most common approaches and best practices.

## Step-by-Step Instructions

### 1. Choose Your Recommendation Approach
- **Collaborative Filtering**: Based on user behavior patterns
- **Content-Based Filtering**: Based on item characteristics
- **Hybrid Approach**: Combines both methods

### 2. Prepare Your Data
- Collect user interaction data (ratings, clicks, purchases)
- Clean and preprocess the data
- Handle missing values and normalize data

### 3. Select Libraries and Tools
- Use `Surprise` library for collaborative filtering
- Use `scikit-learn` for content-based approaches
- Consider `TensorFlow` for deep learning-based recommendations

### 4. Implement the Model
- Split your data into train/test sets
- Train your recommendation model
- Evaluate performance with metrics like RMSE, precision, recall

### 5. Deploy and Monitor
- Deploy your model using Flask/FastAPI
- Monitor recommendation quality
- Continuously update based on new user interactions

## Example Application
For an e-commerce platform, implement collaborative filtering to recommend products based on similar users' preferences.

## Best Practices
- Start with simple models before moving to complex ones
- Regularly update your model with fresh data
- Consider cold start problem for new users/items
- Test different algorithms to find the best fit for your use case"""
        },
        {
            "user_input": "Create a guide on fine-tuning a GPT model for customer support.",
            "assistant_response": """# Fine-tuning GPT for Customer Support - Practical Guide

## Overview
This guide covers fine-tuning a GPT model specifically for customer support applications, including data preparation, model training, and deployment considerations.

## Step-by-Step Instructions

### 1. Collect and Prepare Training Data
- Gather historical customer support conversations
- Anonymize personal information
- Format conversations in instruction-response pairs
- Ensure diverse range of customer queries and responses

### 2. Choose Your Model
- Use GPT-3.5-turbo or GPT-4 for best results
- Consider open-source alternatives like Pythia or OPT for more control
- Evaluate model size vs. performance trade-offs

### 3. Prepare Your Dataset
- Format data in the required format (e.g., OpenAI's format for API fine-tuning)
- Split data into training, validation, and test sets
- Ensure balanced representation of different query types

### 4. Fine-tune the Model
- Use the appropriate API or framework (e.g., OpenAI's fine-tuning API, Hugging Face)
- Start with recommended hyperparameters
- Monitor training metrics to avoid overfitting

### 5. Evaluate and Iterate
- Test the model with unseen customer queries
- Evaluate response quality, accuracy, and safety
- Iterate based on feedback and performance metrics

## Example Application
Fine-tune a model to handle common questions about order status, returns, and product features for an e-commerce company.

## Best Practices
- Maintain a human-in-the-loop for complex queries
- Regularly update training data to reflect new products/features
- Implement safety measures to prevent inappropriate responses
- Establish clear escalation paths for complex issues"""
        }
    ]

    # Set best practices
    skill.best_practices = """- Always provide clear, actionable steps that users can follow
- Include practical examples relevant to the user's specific use case
- Consider the user's technical level and adjust complexity accordingly
- Include code snippets when relevant, with explanations
- Provide best practices and potential pitfalls to avoid
- Suggest useful libraries, tools, or resources
- Ask clarifying questions if the user's request is too broad or unclear
- Structure guides with clear headings and numbered steps for easy navigation
- Focus on practical implementation rather than just theoretical concepts
- Consider ethical implications and best practices in AI development"""

    # Generate and save the skill
    generator = SkillGenerator()
    output_path = "../skills/AIPracticalGuideGenerator/SKILL.md"
    saved_path = generator.save_skill(skill, output_path)

    print(f"AI Practical Guide Generator skill created at: {saved_path}")
    return saved_path


if __name__ == "__main__":
    create_ai_guide_skill()