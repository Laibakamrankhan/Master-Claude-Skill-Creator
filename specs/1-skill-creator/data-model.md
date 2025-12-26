# Data Model: Claude Skill Creator

## Entities

### Claude Skill
**Description**: The primary entity representing a Claude Skill in the system
**Fields**:
- `name` (string): The unique name of the skill
- `description` (string): Brief description of the skill's purpose
- `version` (string): Version number following semantic versioning
- `instructions` (string): Detailed instructions for the skill
- `examples` (array of objects): Example interactions for the skill
- `best_practices` (string): Best practices for using the skill
- `yaml_frontmatter` (object): YAML metadata at the top of SKILL.md
- `file_path` (string): Path to the skill file on the filesystem

**Validation Rules**:
- `name` must be unique within the system
- `name` must follow Claude's naming conventions (alphanumeric + hyphens)
- `description` must be 1-2 sentences
- `instructions` must be non-empty
- `examples` must contain at least one example

### Validation Result
**Description**: Represents the result of validating a Claude Skill
**Fields**:
- `is_valid` (boolean): Whether the skill passes validation
- `errors` (array of strings): List of validation errors
- `warnings` (array of strings): List of validation warnings
- `compliance_score` (number): Percentage of specification compliance
- `suggestions` (array of strings): Suggestions for improvement

**Validation Rules**:
- `compliance_score` must be between 0 and 100
- `errors` and `warnings` must be arrays (can be empty)

### Distribution Package
**Description**: Represents a packaged Claude Skill ready for distribution
**Fields**:
- `skill_name` (string): Name of the skill being packaged
- `files` (array of objects): List of files included in the package
- `output_path` (string): Path where the package will be created
- `package_type` (string): Type of package (currently "zip")
- `size` (number): Size of the package in bytes (computed)

**Validation Rules**:
- `package_type` must be one of the supported types
- `files` must contain at least the SKILL.md file
- `output_path` must be a valid filesystem path

### Skill Template
**Description**: Template used for generating new Claude Skills
**Fields**:
- `name` (string): Name of the template
- `description` (string): Description of what the template is for
- `content` (string): Template content with placeholders
- `variables` (array of strings): List of placeholders in the template
- `category` (string): Category of the template (e.g., "utility", "integration")

**Validation Rules**:
- `variables` must match the placeholders in `content`
- `name` must be unique within the system

## Relationships

### Claude Skill -> Validation Result
- One-to-many: A Claude Skill can have multiple validation results over time
- Dependency: Validation Result references the skill it validates

### Claude Skill -> Distribution Package
- One-to-one: A Claude Skill can be packaged into one distribution package
- Dependency: Distribution Package contains the skill's files

### Skill Template -> Claude Skill
- One-to-many: A Skill Template can be used to generate many Claude Skills
- Dependency: Claude Skill generation uses a template as its base