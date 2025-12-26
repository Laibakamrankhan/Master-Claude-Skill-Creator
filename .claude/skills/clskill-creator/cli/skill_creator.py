import json
import os
from typing import Dict, Any, List
import sys
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lib.skill_generator import ClaudeSkill, SkillGenerator


class InteractiveSkillCreator:
    """Interactive CLI interface for creating Claude Skills"""

    def __init__(self):
        self.generator = SkillGenerator()

    def get_skill_info(self) -> ClaudeSkill:
        """Interactive prompts to gather skill information from user"""
        print("=== Claude Skill Creator ===\n")
        print("Let's create a new Claude Skill!\n")

        # Get basic skill information
        name = self._get_input("What should your skill be named? ")
        description = self._get_input("Describe what your skill does in one or two sentences: ")

        print(f"\nGreat! You're creating: {name} - {description}\n")

        # Gather detailed information
        instructions = self._get_detailed_instructions()
        examples = self._get_examples()
        best_practices = self._get_best_practices()

        # Create and populate the skill object
        skill = ClaudeSkill(name=name, description=description)
        skill.instructions = instructions
        skill.examples = examples
        skill.best_practices = best_practices

        return skill

    def _get_input(self, prompt: str) -> str:
        """Get input from user with basic validation"""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Please provide a non-empty response.")

    def _get_detailed_instructions(self) -> str:
        """Get detailed instructions for the skill"""
        print("\nNow let's define the instructions for your skill.")
        print("These should be detailed steps or guidelines for how Claude should behave when using this skill.\n")

        instructions = []
        while True:
            instruction = input("Add an instruction (or press Enter to finish): ").strip()
            if not instruction:
                break
            instructions.append(instruction)

        if not instructions:
            print("No instructions provided. Using a default placeholder.")
            return "Please provide detailed instructions for this skill."

        return "\n".join(instructions)

    def _get_examples(self) -> List[Dict[str, str]]:
        """Get example user-assistant interactions"""
        print("\nLet's add some examples of how users might interact with your skill.")
        print("Each example should show a user query and Claude's expected response.\n")

        examples = []
        example_num = 1

        while True:
            print(f"Example {example_num}:")
            user_input = input("User query (or press Enter to finish): ").strip()
            if not user_input:
                break

            assistant_response = input("Claude's response: ").strip()
            if not assistant_response:
                print("Please provide a response for Claude.")
                continue

            examples.append({
                "user_input": user_input,
                "assistant_response": assistant_response
            })

            example_num += 1
            print()  # Empty line for readability

        if not examples:
            print("No examples provided. Adding a default example.")
            return [{
                "user_input": "Sample user query",
                "assistant_response": "Sample Claude response"
            }]

        return examples

    def _get_best_practices(self) -> str:
        """Get best practices for using the skill"""
        print("\nFinally, let's define some best practices for using your skill.")
        print("These might include usage tips, limitations, or guidelines.\n")

        practices = []
        while True:
            practice = input("Add a best practice (or press Enter to finish): ").strip()
            if not practice:
                break
            practices.append(practice)

        if not practices:
            print("No best practices provided. Using a default placeholder.")
            return "Use this skill appropriately and follow Claude's usage guidelines."

        return "\n".join(practices)

    def run(self, output_path: str = None) -> str:
        """Run the interactive skill creation process"""
        try:
            skill = self.get_skill_info()

            # Determine output path
            if not output_path:
                skill_filename = f"{skill.name.lower().replace(' ', '_')}_skill.md"
                output_path = os.path.join(os.getcwd(), skill_filename)

            # Generate and save the skill
            saved_path = self.generator.save_skill(skill, output_path)

            print(f"\n✅ Success! Your skill has been created at: {saved_path}")
            print("\nYou can now validate and package your skill for distribution.")

            return saved_path

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            return None
        except Exception as e:
            print(f"\n❌ Error creating skill: {str(e)}")
            return None


def main():
    """Main entry point for the CLI"""
    import sys

    output_path = None
    if len(sys.argv) > 1:
        output_path = sys.argv[1]

    creator = InteractiveSkillCreator()
    creator.run(output_path)


if __name__ == "__main__":
    main()