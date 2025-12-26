#!/usr/bin/env python3
"""
Validator for Claude Skills - checks YAML structure and compliance with Claude Skills specification
"""

import yaml
import re
from pathlib import Path
from typing import Dict, Any, List
import sys

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from models.validation_result import ValidationResult


class ClaudeSkillValidator:
    """Validates Claude Skills against the official specification"""

    def __init__(self):
        # Required fields in the YAML frontmatter
        self.required_frontmatter_fields = {
            'name': str,
            'description': str,
            'version': str
        }

        # Required sections in the markdown body
        self.required_sections = [
            'Instructions',
            'Examples',
            'Best Practices'
        ]

    def validate_skill_file(self, skill_path: str) -> ValidationResult:
        """Validate a Claude Skill file at the given path"""
        path = Path(skill_path)

        if not path.exists():
            return ValidationResult(
                is_valid=False,
                errors=[f"File does not exist: {skill_path}"],
                warnings=[],
                suggestions=[]
            )

        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                errors=[f"Could not read file: {str(e)}"],
                warnings=[],
                suggestions=[]
            )

        return self.validate_skill_content(content)

    def validate_skill_content(self, content: str) -> ValidationResult:
        """Validate Claude Skill content"""
        result = ValidationResult(is_valid=True, errors=[], warnings=[], suggestions=[])

        # Split content to separate YAML frontmatter from markdown content
        frontmatter, markdown_content = self._extract_frontmatter(content)

        if frontmatter is None:
            result.add_error("No YAML frontmatter found. Claude Skills must have YAML frontmatter with name, description, and version.")
            return result

        # Validate frontmatter
        self._validate_frontmatter(frontmatter, result)

        # Validate markdown structure
        self._validate_markdown_structure(markdown_content, result)

        # Calculate compliance score
        result.compliance_score = self._calculate_compliance_score(result)

        return result

    def _extract_frontmatter(self, content: str) -> tuple:
        """Extract YAML frontmatter from content"""
        lines = content.split('\n')

        # Check if content starts with frontmatter delimiter
        if len(lines) > 0 and lines[0].strip() == '---':
            # Find the end of frontmatter
            frontmatter_end = -1
            for i in range(1, len(lines)):
                if lines[i].strip() == '---':
                    frontmatter_end = i
                    break

            if frontmatter_end > 1:
                frontmatter_str = '\n'.join(lines[1:frontmatter_end])
                markdown_content = '\n'.join(lines[frontmatter_end + 1:])

                try:
                    frontmatter = yaml.safe_load(frontmatter_str)
                    return frontmatter, markdown_content
                except yaml.YAMLError as e:
                    return None, content

        return None, content

    def _validate_frontmatter(self, frontmatter: Dict[str, Any], result: ValidationResult):
        """Validate the YAML frontmatter"""
        if not isinstance(frontmatter, dict):
            result.add_error("YAML frontmatter must be a dictionary")
            return

        # Check required fields
        for field, expected_type in self.required_frontmatter_fields.items():
            if field not in frontmatter:
                result.add_error(f"Missing required field in frontmatter: '{field}'")
            else:
                value = frontmatter[field]
                if not isinstance(value, expected_type):
                    result.add_error(f"Field '{field}' should be of type {expected_type.__name__}, got {type(value).__name__}")

                # Additional validation for specific fields
                if field == 'name':
                    self._validate_name(value, result)
                elif field == 'description':
                    self._validate_description(value, result)
                elif field == 'version':
                    self._validate_version(value, result)

    def _validate_name(self, name: str, result: ValidationResult):
        """Validate the skill name"""
        if not name or len(name.strip()) == 0:
            result.add_error("Skill name cannot be empty")
        elif len(name) > 100:
            result.add_warning("Skill name seems very long, consider making it more concise")
        elif not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9 _-]*[a-zA-Z0-9]$', name.strip()):
            result.add_warning("Skill name should contain only letters, numbers, spaces, hyphens, and underscores")

    def _validate_description(self, description: str, result: ValidationResult):
        """Validate the skill description"""
        if not description or len(description.strip()) == 0:
            result.add_error("Skill description cannot be empty")
        elif len(description) > 500:
            result.add_warning("Skill description is very long, consider making it more concise")
        elif len(description) < 10:
            result.add_warning("Skill description is very short, consider adding more detail")

    def _validate_version(self, version: str, result: ValidationResult):
        """Validate the version string"""
        if not version or len(version.strip()) == 0:
            result.add_error("Version cannot be empty")
        else:
            # Basic semantic versioning check
            if not re.match(r'^\d+\.\d+\.\d+', version.strip()):
                result.add_warning(f"Version '{version}' does not follow semantic versioning (X.Y.Z) format")

    def _validate_markdown_structure(self, content: str, result: ValidationResult):
        """Validate the markdown structure and required sections"""
        lines = content.split('\n')

        # Find all headers in the document
        headers = []
        for i, line in enumerate(lines):
            if line.strip().startswith('#'):
                # This is a markdown header
                header_match = re.match(r'^#+\s+(.+)$', line.strip())
                if header_match:
                    headers.append(header_match.group(1).strip())

        # Check for required sections
        missing_sections = []
        for required_section in self.required_sections:
            if required_section not in headers:
                missing_sections.append(required_section)

        if missing_sections:
            result.add_error(f"Missing required sections: {', '.join(missing_sections)}")
            result.add_suggestion("Add the following sections to your skill: " + ", ".join(missing_sections))

        # Additional markdown checks
        if len(content.strip()) == 0:
            result.add_error("Skill content is empty")
        elif len(content) < 100:
            result.add_warning("Skill content is very short, consider adding more detail")

        # Check for proper Examples section format
        if 'Examples' in headers:
            self._validate_examples_section(lines, result)

    def _validate_examples_section(self, lines: List[str], result: ValidationResult):
        """Validate the Examples section format"""
        examples_start_idx = -1
        examples_end_idx = len(lines)

        # Find the Examples section
        for i, line in enumerate(lines):
            if line.strip().startswith('#') and 'Examples' in line:
                examples_start_idx = i
                # Find the next header to determine where examples section ends
                for j in range(i + 1, len(lines)):
                    if lines[j].strip().startswith('#') and lines[j].strip().startswith('##'):
                        examples_end_idx = j
                        break
                break

        if examples_start_idx == -1:
            return  # Examples section not found, this is already reported

        # Look for example patterns within the examples section
        example_found = False
        for i in range(examples_start_idx, examples_end_idx):
            line = lines[i]
            if 'User:' in line or 'Claude:' in line or 'Assistant:' in line:
                example_found = True
                break

        if not example_found:
            result.add_warning("Examples section should contain actual user/Claude interaction examples")
            result.add_suggestion("Add example interactions in the format: 'User: [query]' and 'Claude: [response]'")

    def _calculate_compliance_score(self, result: ValidationResult) -> float:
        """Calculate a compliance score based on validation results"""
        total_possible_points = 100

        # Deduct points for errors
        error_penalty = len(result.errors) * 10  # 10 points per error
        warning_penalty = len(result.warnings) * 2  # 2 points per warning

        score = total_possible_points - error_penalty - warning_penalty
        return max(0, min(100, score))  # Clamp between 0 and 100


def main():
    """Command line interface for the validator"""
    if len(sys.argv) != 2:
        print("Usage: python validate_skill.py <path_to_skill.md>")
        sys.exit(1)

    skill_path = sys.argv[1]
    validator = ClaudeSkillValidator()
    result = validator.validate_skill_file(skill_path)

    # Print validation results
    print(f"\nValidation Results for: {skill_path}")
    print("="*50)

    if result.is_valid:
        print(f"PASS - Compliance Score: {result.compliance_score}%")
    else:
        print(f"FAIL - Compliance Score: {result.compliance_score}%")

    if result.errors:
        print(f"\nErrors ({len(result.errors)}):")
        for i, error in enumerate(result.errors, 1):
            print(f"  {i}. {error}")

    if result.warnings:
        print(f"\nWarnings ({len(result.warnings)}):")
        for i, warning in enumerate(result.warnings, 1):
            print(f"  {i}. {warning}")

    if result.suggestions:
        print(f"\nSuggestions ({len(result.suggestions)}):")
        for i, suggestion in enumerate(result.suggestions, 1):
            print(f"  {i}. {suggestion}")

    # Exit with appropriate code
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()