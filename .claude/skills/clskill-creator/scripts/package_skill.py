#!/usr/bin/env python3
"""
Packager for Claude Skills - creates distributable ZIP files with proper structure
"""

import sys
import os
import zipfile
from pathlib import Path
from typing import List, Optional
import shutil


class ClaudeSkillPackager:
    """Packages Claude Skills for distribution"""

    def __init__(self):
        # Required files for a valid Claude Skill package
        self.required_files = [
            'SKILL.md'
        ]

        # Optional directories that might be included
        self.optional_directories = [
            'scripts',
            'assets',
            'examples'
        ]

    def package_skill(self, skill_directory: str, output_path: str = None, include_supporting_files: bool = True) -> str:
        """
        Package a Claude Skill directory into a distributable ZIP file

        Args:
            skill_directory: Path to the skill directory to package
            output_path: Path for the output ZIP file (optional, auto-generated if not provided)
            include_supporting_files: Whether to include supporting files (scripts, assets, etc.)

        Returns:
            Path to the created ZIP file
        """
        skill_path = Path(skill_directory)

        if not skill_path.exists():
            raise FileNotFoundError(f"Skill directory does not exist: {skill_directory}")

        if not skill_path.is_dir():
            raise ValueError(f"Path is not a directory: {skill_directory}")

        # Validate required files exist
        required_file_paths = [skill_path / req_file for req_file in self.required_files]
        missing_files = [str(p) for p in required_file_paths if not p.exists()]

        if missing_files:
            raise FileNotFoundError(f"Missing required files in skill directory: {', '.join(missing_files)}")

        # Generate output path if not provided
        if not output_path:
            skill_name = self._extract_skill_name(skill_path)
            output_path = f"{skill_name.replace(' ', '_')}_package.zip"

        # Create the ZIP file
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            self._add_directory_to_zip(zipf, skill_path, include_supporting_files)

        return output_path

    def _extract_skill_name(self, skill_path: Path) -> str:
        """Extract skill name from SKILL.md file"""
        skill_file = skill_path / "SKILL.md"

        if skill_file.exists():
            try:
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Look for name in YAML frontmatter
                import re
                match = re.search(r'name:\s*[\'"]?([^\'"\n]+)[\'"]?', content.split('---')[1] if '---' in content else content)
                if match:
                    return match.group(1).strip()

                # Fallback: use directory name
                return skill_path.name
            except Exception:
                # Fallback: use directory name
                return skill_path.name
        else:
            # Fallback: use directory name
            return skill_path.name

    def _add_directory_to_zip(self, zipf: zipfile.ZipFile, directory: Path, include_supporting_files: bool):
        """Add directory contents to ZIP file"""
        for root, dirs, files in os.walk(directory):
            # If not including supporting files, filter out optional directories
            if not include_supporting_files:
                dirs[:] = [d for d in dirs if d not in self.optional_directories]

            for file in files:
                file_path = Path(root) / file
                # Calculate the relative path from the skill directory
                relative_path = file_path.relative_to(directory)

                # Skip if it's inside an optional directory and we're not including supporting files
                if not include_supporting_files:
                    if any(str(relative_path).startswith(opt_dir + '/') or str(relative_path) == opt_dir
                           for opt_dir in self.optional_directories):
                        continue

                zipf.write(file_path, relative_path)

    def validate_package_structure(self, skill_directory: str) -> dict:
        """
        Validate the structure of a skill directory before packaging

        Returns:
            Dictionary with validation results
        """
        skill_path = Path(skill_directory)
        result = {
            'valid': True,
            'missing_required_files': [],
            'found_files': [],
            'found_directories': [],
            'warnings': []
        }

        if not skill_path.exists() or not skill_path.is_dir():
            result['valid'] = False
            result['errors'] = [f"Directory does not exist: {skill_directory}"]
            return result

        # Check for required files
        for req_file in self.required_files:
            req_path = skill_path / req_file
            if not req_path.exists():
                result['missing_required_files'].append(req_file)
                result['valid'] = False

        # Collect all files and directories
        for item in skill_path.iterdir():
            if item.is_file():
                result['found_files'].append(item.name)
            elif item.is_dir():
                result['found_directories'].append(item.name)

        # Check for common issues
        if 'SKILL.md' in result['found_files']:
            # Check if SKILL.md has proper structure
            skill_file = skill_path / 'SKILL.md'
            try:
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for YAML frontmatter
                if not content.startswith('---'):
                    result['warnings'].append("SKILL.md should start with YAML frontmatter (---)")

                # Check for required sections
                required_sections = ['Instructions', 'Examples', 'Best Practices']
                for section in required_sections:
                    if f'## {section}' not in content and f'# {section}' not in content:
                        result['warnings'].append(f"SKILL.md is missing required section: {section}")

            except Exception as e:
                result['warnings'].append(f"Could not read SKILL.md: {str(e)}")

        return result


def main():
    """Command line interface for the packager"""
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <skill_directory> [output_path] [--no-supporting-files]")
        print("  skill_directory: Path to the skill directory to package")
        print("  output_path: Path for the output ZIP file (optional)")
        print("  --no-supporting-files: Exclude optional supporting files (scripts, assets, etc.)")
        sys.exit(1)

    skill_directory = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
    include_supporting_files = not ('--no-supporting-files' in sys.argv or '--no-supporting' in sys.argv)

    # If output path is an option, set it to None and use default
    if output_path and output_path.startswith('--'):
        output_path = None

    packager = ClaudeSkillPackager()

    try:
        # Validate structure first
        validation = packager.validate_package_structure(skill_directory)

        if not validation['valid']:
            print("ERROR: Invalid skill structure:")
            if 'missing_required_files' in validation:
                for missing in validation['missing_required_files']:
                    print(f"  - Missing required file: {missing}")
            if 'errors' in validation:
                for error in validation['errors']:
                    print(f"  - {error}")
            sys.exit(1)

        # Show warnings if any
        if validation['warnings']:
            print("Warning:  Warnings found:")
            for warning in validation['warnings']:
                print(f"  - {warning}")
            print()

        # Package the skill
        print(f"Packing skill from: {skill_directory}")
        print(f"Include supporting files: {include_supporting_files}")

        zip_path = packager.package_skill(skill_directory, output_path, include_supporting_files)

        print(f"SUCCESS: Skill successfully packaged to: {zip_path}")

        # Show package info
        zip_size = Path(zip_path).stat().st_size
        print(f"INFO: Package size: {zip_size} bytes ({zip_size / 1024:.2f} KB)")

    except Exception as e:
        print(f"FAILED: Error packaging skill: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()