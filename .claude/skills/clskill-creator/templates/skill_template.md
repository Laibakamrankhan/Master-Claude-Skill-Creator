---
name: "{{ skill_name }}"
description: "{{ skill_description }}"
version: "1.0.0"
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