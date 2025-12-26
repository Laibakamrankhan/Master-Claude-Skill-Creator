import os
import yaml
from jinja2 import Template
from typing import Dict, Any, List, Optional


class ClaudeSkill:
    """Represents a Claude Skill with all required components"""

    def __init__(self, name: str, description: str, version: str = "1.0.0"):
        self.name = name
        self.description = description
        self.version = version
        self.instructions = ""
        self.examples = []
        self.best_practices = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert the skill to a dictionary for YAML serialization"""
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version
        }


class SkillGenerator:
    """Generates Claude Skills based on user input"""

    def __init__(self, template_path: str = ".claude/skills/clskill-creator/templates/skill_template.md"):
        self.template_path = template_path
        self.template_content = self._load_template()

    def _load_template(self) -> str:
        """Load the skill template from file"""
        try:
            with open(self.template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            # Fallback to default template
            return """---
name: "{{ skill_name }}"
description: "{{ skill_description }}"
version: "{{ version }}"
---

# {{ skill_name }}

## Instructions

{{ instructions }}

## Examples

{% for example in examples %}
### Example {{ loop.index }}
**User:** {{ example.user_input }}
**Claude:** {{ example.assistant_response }}
{% endfor %}

## Best Practices

{{ best_practices }}
"""

    def generate_skill(self, skill_data: ClaudeSkill) -> str:
        """Generate a complete SKILL.md file from the provided data"""
        template = Template(self.template_content)

        # Prepare the context for template rendering
        context = {
            "skill_name": skill_data.name,
            "skill_description": skill_data.description,
            "version": skill_data.version,
            "instructions": skill_data.instructions,
            "examples": skill_data.examples,
            "best_practices": skill_data.best_practices
        }

        return template.render(**context)

    def save_skill(self, skill_data: ClaudeSkill, output_path: str) -> str:
        """Generate and save the skill to the specified path"""
        skill_content = self.generate_skill(skill_data)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(skill_content)

        return output_path