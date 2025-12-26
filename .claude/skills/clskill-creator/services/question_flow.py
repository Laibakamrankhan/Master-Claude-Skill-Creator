import sys
import os
from pathlib import Path
from typing import Dict, Any, List, Callable

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.validation_result import ValidationResult


class QuestionFlowService:
    """Handles the flow of clarifying questions for skill creation"""

    def __init__(self):
        self.questions = {
            'purpose': {
                'prompt': "What is the primary purpose of your skill?",
                'validation': self._validate_purpose,
                'help_text': "Be specific about what the skill should accomplish."
            },
            'target_users': {
                'prompt': "Who are the target users for this skill?",
                'validation': self._validate_target_users,
                'help_text': "Consider the technical level and needs of your users."
            },
            'functionality': {
                'prompt': "What specific functions should the skill perform?",
                'validation': self._validate_functionality,
                'help_text': "List the main tasks or operations the skill should handle."
            },
            'examples': {
                'prompt': "Provide an example interaction (user query and Claude response):",
                'validation': self._validate_example,
                'help_text': "Give a specific example of how someone would use this skill."
            },
            'constraints': {
                'prompt': "Are there any constraints or limitations to consider?",
                'validation': self._validate_constraints,
                'help_text': "Consider technical, security, or usage limitations."
            }
        }

    def _validate_purpose(self, value: str) -> ValidationResult:
        """Validate the skill purpose"""
        if not value or len(value.strip()) < 5:
            return ValidationResult(
                is_valid=False,
                errors=["Purpose must be at least 5 characters long"],
                warnings=[]
            )

        if len(value) > 200:
            return ValidationResult(
                is_valid=True,
                errors=[],
                warnings=["Purpose seems quite long, consider making it more concise"]
            )

        return ValidationResult(is_valid=True, errors=[], warnings=[])

    def _validate_target_users(self, value: str) -> ValidationResult:
        """Validate the target users description"""
        if not value or len(value.strip()) < 3:
            return ValidationResult(
                is_valid=False,
                errors=["Please describe the target users"],
                warnings=[]
            )

        return ValidationResult(is_valid=True, errors=[], warnings=[])

    def _validate_functionality(self, value: str) -> ValidationResult:
        """Validate the functionality description"""
        if not value or len(value.strip()) < 10:
            return ValidationResult(
                is_valid=False,
                errors=["Functionality description should be more detailed"],
                warnings=[]
            )

        return ValidationResult(is_valid=True, errors=[], warnings=[])

    def _validate_example(self, value: str) -> ValidationResult:
        """Validate the example interaction"""
        if not value or len(value.strip()) < 10:
            return ValidationResult(
                is_valid=False,
                errors=["Example should be more detailed"],
                warnings=[]
            )

        return ValidationResult(is_valid=True, errors=[], warnings=[])

    def _validate_constraints(self, value: str) -> ValidationResult:
        """Validate the constraints description"""
        return ValidationResult(is_valid=True, errors=[], warnings=[])

    def ask_questions(self) -> Dict[str, str]:
        """Ask all clarifying questions and collect responses"""
        responses = {}

        print("\nLet me ask you some clarifying questions to better understand your skill requirements:\n")

        for key, config in self.questions.items():
            while True:
                print(f"{config['prompt']}")
                print(f"Help: {config['help_text']}")

                response = input("> ").strip()

                # Validate the response
                validation_result = config['validation'](response)

                if not validation_result.is_valid:
                    print(f"❌ Error: {'; '.join(validation_result.errors)}")
                    continue

                if validation_result.warnings:
                    print(f"⚠️  Warning: {'; '.join(validation_result.warnings)}")

                responses[key] = response
                break  # Valid response, move to next question

                print()  # Add spacing between questions

        return responses

    def refine_skill_data(self, initial_description: str, responses: Dict[str, str]) -> Dict[str, Any]:
        """Refine the skill data based on responses"""
        # Combine initial description with clarifying responses
        refined_data = {
            'initial_description': initial_description,
            'purpose': responses.get('purpose', ''),
            'target_users': responses.get('target_users', ''),
            'functionality': responses.get('functionality', ''),
            'example': responses.get('examples', ''),
            'constraints': responses.get('constraints', ''),
        }

        # Generate a more specific skill name based on purpose
        purpose_words = responses.get('purpose', '').split()[:3]
        skill_name = ' '.join(purpose_words).title().replace(' ', '') or 'MySkill'
        refined_data['name'] = skill_name

        # Generate description by combining purpose and functionality
        description_parts = [responses.get('purpose', ''), responses.get('functionality', '')]
        description = '. '.join([part for part in description_parts if part]) or initial_description
        refined_data['description'] = description

        return refined_data