#!/usr/bin/env python3
"""
Demonstration of the Claude Skill Creator functionality
"""

import sys
import os
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from lib.skill_generator import ClaudeSkill, SkillGenerator
# from services.skill_service import SkillCreationService  # Commenting out for demo
from scripts.validate_skill import ClaudeSkillValidator
from scripts.package_skill import ClaudeSkillPackager


def demo_skill_creation():
    """Demonstrate the skill creation process"""
    print("=== Claude Skill Creator Demo ===\n")

    # Create a sample skill programmatically
    print("1. Creating a sample skill programmatically...")
    skill = ClaudeSkill(
        name="Weather Assistant",
        description="A skill that helps users get weather information and forecasts"
    )

    skill.instructions = """Act as a weather assistant. Provide current weather conditions and forecasts based on user location.
    When users ask about weather, ask for their location if not specified.
    Provide temperature, conditions, and any weather alerts.
    Give appropriate advice based on conditions (e.g., bring umbrella for rain)."""

    skill.examples = [
        {
            "user_input": "What's the weather like in New York today?",
            "assistant_response": "Currently in New York: 72°F, Partly Cloudy. No severe weather alerts. It's a pleasant day!"
        },
        {
            "user_input": "Will it rain tomorrow in Seattle?",
            "assistant_response": "Tomorrow's forecast for Seattle: 65°F, 80% chance of rain. Don't forget your umbrella!"
        }
    ]

    skill.best_practices = """- Always confirm location if not specified
- Provide temperature in user's local units (Fahrenheit/Celsius)
- Mention any weather alerts or warnings
- Give practical advice based on conditions
- Be aware of seasonal patterns"""

    print(f"   Created skill: {skill.name}")
    print(f"   Description: {skill.description}\n")

    # Generate the skill file
    print("2. Generating SKILL.md file...")
    generator = SkillGenerator()
    output_path = "./demo_weather_skill.md"  # Use explicit relative path
    saved_path = generator.save_skill(skill, output_path)
    print(f"   Skill saved to: {saved_path}\n")

    # Validate the generated skill
    print("3. Validating the generated skill...")
    validator = ClaudeSkillValidator()
    result = validator.validate_skill_file(saved_path)

    print(f"   Validation result: {'PASS' if result.is_valid else 'FAIL'}")
    print(f"   Compliance score: {result.compliance_score}%")
    if result.errors:
        print(f"   Errors: {len(result.errors)}")
    if result.warnings:
        print(f"   Warnings: {len(result.warnings)}")
    print()

    # Package the skill
    print("4. Packaging the skill for distribution...")
    packager = ClaudeSkillPackager()

    # Create a temporary directory structure for packaging
    demo_dir = Path("./demo_skill")
    demo_dir.mkdir(exist_ok=True)

    # Move the skill file to the demo directory
    skill_demo_path = demo_dir / "SKILL.md"
    Path(saved_path).rename(skill_demo_path)

    # Package the skill
    zip_path = "./demo_weather_skill.zip"
    packaged_path = packager.package_skill(str(demo_dir), zip_path)

    print(f"   Skill packaged to: {packaged_path}")

    # Cleanup
    if demo_dir.exists():
        import shutil
        shutil.rmtree(demo_dir)

    print("\n=== Demo completed successfully! ===")
    print("\nWhat we demonstrated:")
    print("- Creating a Claude Skill programmatically")
    print("- Generating a properly formatted SKILL.md file")
    print("- Validating the skill against Claude's requirements")
    print("- Packaging the skill for distribution")


if __name__ == "__main__":
    demo_skill_creation()