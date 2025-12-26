#!/usr/bin/env python3
"""
Test script for Claude Skill Creator functionality
"""

import os
import tempfile
from pathlib import Path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from lib.skill_generator import ClaudeSkill, SkillGenerator
from scripts.validate_skill import ClaudeSkillValidator
from scripts.package_skill import ClaudeSkillPackager


def test_skill_generation():
    """Test the skill generation functionality"""
    print("Testing skill generation...")

    # Create a sample skill
    skill = ClaudeSkill(name="Test Skill", description="A test skill for validation")
    skill.instructions = "These are test instructions for the skill."
    skill.examples = [
        {
            "user_input": "Test user query",
            "assistant_response": "Test assistant response"
        }
    ]
    skill.best_practices = "These are test best practices."

    # Generate the skill content
    generator = SkillGenerator()
    content = generator.generate_skill(skill)

    # Verify the content contains expected elements
    assert "Test Skill" in content
    assert "A test skill for validation" in content
    assert "Test user query" in content
    assert "Test assistant response" in content

    print("PASS: Skill generation test passed")


def test_skill_validation():
    """Test the skill validation functionality"""
    print("Testing skill validation...")

    # Create a valid skill content
    valid_skill_content = """---
name: Test Skill
description: A test skill for validation
version: 1.0.0
---

# Test Skill

## Instructions

These are test instructions for the skill.

## Examples

### Example 1
**User:** Test user query
**Claude:** Test assistant response

## Best Practices

These are test best practices.
"""

    # Validate the content
    validator = ClaudeSkillValidator()
    result = validator.validate_skill_content(valid_skill_content)

    # Check that validation passes
    assert result.is_valid, f"Validation failed: {result.errors}"
    assert result.compliance_score >= 90, f"Compliance score too low: {result.compliance_score}"

    print("PASS: Skill validation test passed")


def test_skill_packaging():
    """Test the skill packaging functionality"""
    print("Testing skill packaging...")

    # Create a temporary directory with a skill
    with tempfile.TemporaryDirectory() as temp_dir:
        skill_dir = Path(temp_dir) / "test_skill"
        skill_dir.mkdir()

        # Create a SKILL.md file
        skill_content = """---
name: Test Skill
description: A test skill for packaging
version: 1.0.0
---

# Test Skill

## Instructions

These are test instructions.

## Examples

### Example 1
**User:** Test query
**Claude:** Test response

## Best Practices

Test best practices.
"""

        skill_file = skill_dir / "SKILL.md"
        skill_file.write_text(skill_content)

        # Create the packaging output in the same temp directory
        output_path = os.path.join(temp_dir, "test_package.zip")

        # Package the skill
        packager = ClaudeSkillPackager()
        zip_path = packager.package_skill(str(skill_dir), output_path)

        # Verify the zip file was created
        assert os.path.exists(zip_path), "ZIP file was not created"

        print("PASS: Skill packaging test passed")


def test_invalid_skill_validation():
    """Test validation of invalid skills"""
    print("Testing invalid skill validation...")

    # Create an invalid skill (missing required sections)
    invalid_skill_content = """---
name: Test Skill
description: A test skill for validation
version: 1.0.0
---

# Test Skill

## Instructions

These are test instructions for the skill.
"""

    # Validate the content
    validator = ClaudeSkillValidator()
    result = validator.validate_skill_content(invalid_skill_content)

    # Check that validation fails as expected
    assert not result.is_valid, "Validation should have failed for missing sections"
    assert any("Examples" in error or "Best Practices" in error for error in result.errors), \
        f"Expected errors about missing sections, got: {result.errors}"

    print("PASS: Invalid skill validation test passed")


def main():
    """Run all tests"""
    print("Running Claude Skill Creator tests...\n")

    try:
        test_skill_generation()
        test_skill_validation()
        test_skill_packaging()
        test_invalid_skill_validation()

        print("\nSUCCESS: All tests passed!")
        return True
    except Exception as e:
        print(f"\nFAILED: Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)