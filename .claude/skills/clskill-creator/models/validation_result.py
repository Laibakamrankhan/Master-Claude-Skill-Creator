from typing import List, Optional


class ValidationResult:
    """Represents the result of validating a Claude Skill"""

    def __init__(self, is_valid: bool, errors: List[str], warnings: List[str], suggestions: Optional[List[str]] = None, compliance_score: float = 0.0):
        self.is_valid = is_valid
        self.errors = errors or []
        self.warnings = warnings or []
        self.suggestions = suggestions or []
        self.compliance_score = compliance_score

    def __repr__(self):
        return f"ValidationResult(is_valid={self.is_valid}, errors={self.errors}, warnings={self.warnings}, compliance_score={self.compliance_score})"

    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            "is_valid": self.is_valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "suggestions": self.suggestions,
            "compliance_score": self.compliance_score
        }

    def add_error(self, error: str):
        """Add an error to the validation result"""
        self.errors.append(error)
        self.is_valid = False

    def add_warning(self, warning: str):
        """Add a warning to the validation result"""
        self.warnings.append(warning)

    def add_suggestion(self, suggestion: str):
        """Add a suggestion to the validation result"""
        self.suggestions.append(suggestion)

    @property
    def error_count(self):
        """Get the number of errors"""
        return len(self.errors)

    @property
    def warning_count(self):
        """Get the number of warnings"""
        return len(self.warnings)

    @property
    def suggestion_count(self):
        """Get the number of suggestions"""
        return len(self.suggestions)