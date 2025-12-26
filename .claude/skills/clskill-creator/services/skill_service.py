import sys
import os
from pathlib import Path
from typing import Dict, Any, List

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lib.skill_generator import ClaudeSkill, SkillGenerator
from services.question_flow import QuestionFlowService
import re


class SkillCreationService:
    """Service to orchestrate the skill creation process"""

    def __init__(self):
        self.generator = SkillGenerator()
        self.question_service = QuestionFlowService()

    def create_skill_interactive(self, initial_description: str = None) -> ClaudeSkill:
        """Create a skill with interactive question flow"""
        if not initial_description:
            initial_description = input("Describe the skill you want to create: ").strip()

        # Ask clarifying questions
        responses = self.question_service.ask_questions()

        # Refine the skill data based on responses
        refined_data = self.question_service.refine_skill_data(initial_description, responses)

        # Create the ClaudeSkill object
        skill = ClaudeSkill(
            name=refined_data['name'],
            description=refined_data['description']
        )

        # Set up instructions based on functionality and constraints
        instructions_parts = [
            f"Act as a {refined_data['name']} assistant.",
            refined_data.get('functionality', ''),
            f"Target users: {refined_data.get('target_users', 'General users')}.",
        ]

        if refined_data.get('constraints'):
            instructions_parts.append(f"Important constraints: {refined_data['constraints']}")

        skill.instructions = "\n\n".join([part for part in instructions_parts if part])

        # Add examples if provided
        example_text = refined_data.get('example', '')
        if example_text:
            # Try to parse the example into user/assistant format
            skill.examples = self._parse_examples(example_text)
        else:
            skill.examples = [{
                "user_input": "How can I use this skill?",
                "assistant_response": "This skill helps you accomplish the task based on your requirements."
            }]

        # Add best practices
        best_practices_parts = [
            "Always follow Claude's safety guidelines",
            f"Focus on the core functionality: {refined_data.get('functionality', 'general purpose')}",
        ]

        if refined_data.get('constraints'):
            best_practices_parts.append(f"Respect the constraints: {refined_data['constraints']}")

        skill.best_practices = "\n\n".join(best_practices_parts)

        return skill

    def _parse_examples(self, example_text: str) -> List[Dict[str, str]]:
        """Parse example text into user/assistant format"""
        examples = []

        # Look for patterns like "User: ... Claude: ..." or "Q: ... A: ..."
        # Split by double newlines to separate different examples
        example_blocks = example_text.split('\n\n')

        for block in example_blocks:
            block = block.strip()
            if not block:
                continue

            # Try to identify user and assistant parts
            user_match = re.search(r'(?:User|Q|Question):\s*(.*?)(?:\n|$)', block, re.IGNORECASE)
            assistant_match = re.search(r'(?:Claude|A|Answer|Assistant):\s*(.*?)(?:\n|$)', block, re.IGNORECASE)

            user_input = user_match.group(1).strip() if user_match else ""
            assistant_response = assistant_match.group(1).strip() if assistant_match else ""

            # If regex didn't work, try simple split
            if not user_input or not assistant_response:
                lines = block.split('\n')
                if len(lines) >= 2:
                    user_input = lines[0].strip()
                    assistant_response = lines[1].strip()

            if user_input and assistant_response:
                examples.append({
                    "user_input": user_input,
                    "assistant_response": assistant_response
                })

        # If no examples could be parsed, use the whole text as a single example
        if not examples:
            examples.append({
                "user_input": "Example query",
                "assistant_response": example_text
            })

        return examples

    def create_skill_from_data(self, skill_data: Dict[str, Any]) -> ClaudeSkill:
        """Create a skill from provided data"""
        skill = ClaudeSkill(
            name=skill_data.get('name', 'Default Skill'),
            description=skill_data.get('description', 'A useful skill'),
            version=skill_data.get('version', '1.0.0')
        )

        skill.instructions = skill_data.get('instructions', 'Default instructions for this skill.')
        skill.examples = skill_data.get('examples', [])
        skill.best_practices = skill_data.get('best_practices', 'Follow best practices for this skill.')

        return skill