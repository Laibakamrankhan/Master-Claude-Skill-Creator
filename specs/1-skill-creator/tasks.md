---
description: "Task list for implementing the Claude Skill Creator meta-skill"
---

# Tasks: Claude Skill Creator

**Input**: Design documents from `/specs/1-skill-creator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan at `.claude/skills/clskill-creator/`
- [ ] T002 Initialize Python 3.11 project with PyYAML, Jinja2 dependencies
- [ ] T003 [P] Configure linting and formatting tools for Python

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T004 Create base skill template at `.claude/skills/clskill-creator/templates/skill_template.md`
- [ ] T005 [P] Implement skill validation framework at `.claude/skills/clskill-creator/scripts/validate_skill.py`
- [ ] T006 [P] Setup skill packaging framework at `.claude/skills/clskill-creator/scripts/package_skill.py`
- [ ] T007 Create base models/entities that all stories depend on
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create a new Claude Skill (Priority: P1) 🎯 MVP

**Goal**: User can describe a skill purpose and receive a properly formatted SKILL.md file with all required sections filled out

**Independent Test**: User can describe a skill purpose (e.g., "Create a skill for converting units") and receive a properly formatted SKILL.md file with all required sections filled out

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Contract test for skill creation endpoint in tests/contract/test_skill_creation.py
- [ ] T011 [P] [US1] Integration test for user journey in tests/integration/test_skill_creation.py

### Implementation for User Story 1

- [ ] T012 [P] [US1] Create skill generator model in `.claude/skills/clskill-creator/lib/skill_generator.py`
- [ ] T013 [P] [US1] Create interactive CLI interface in `.claude/skills/clskill-creator/cli/skill_creator.py`
- [ ] T014 [US1] Implement clarifying questions flow in `.claude/skills/clskill-creator/services/question_flow.py`
- [ ] T015 [US1] Implement skill generation from user input in `.claude/skills/clskill-creator/services/skill_service.py`
- [ ] T016 [US1] Add validation and error handling for user inputs
- [ ] T017 [US1] Add logging for skill creation operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Validate Claude Skill Format (Priority: P2)

**Goal**: User can provide a SKILL.md file and receive feedback on any format or specification violations with specific guidance on how to fix them

**Independent Test**: User can provide a SKILL.md file and receive feedback on any format or specification violations with specific guidance on how to fix them

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for validation endpoint in tests/contract/test_skill_validation.py
- [ ] T019 [P] [US2] Integration test for validation user journey in tests/integration/test_skill_validation.py

### Implementation for User Story 2

- [ ] T020 [P] [US2] Create validation result model in `.claude/skills/clskill-creator/models/validation_result.py`
- [ ] T021 [US2] Implement YAML structure validation in `.claude/skills/clskill-creator/validators/yaml_validator.py`
- [ ] T022 [US2] Implement Claude Skills specification validation in `.claude/skills/clskill-creator/validators/specification_validator.py`
- [ ] T023 [US2] Add validation CLI interface in `.claude/skills/clskill-creator/cli/validation_cli.py`
- [ ] T024 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Package Claude Skill for Distribution (Priority: P3)

**Goal**: User can provide a skill directory and receive a properly structured ZIP file ready for distribution

**Independent Test**: User can provide a skill directory and receive a properly structured ZIP file ready for distribution

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US3] Contract test for packaging endpoint in tests/contract/test_skill_packaging.py
- [ ] T026 [P] [US3] Integration test for packaging user journey in tests/integration/test_skill_packaging.py

### Implementation for User Story 3

- [ ] T027 [P] [US3] Create distribution package model in `.claude/skills/clskill-creator/models/distribution_package.py`
- [ ] T028 [US3] Implement ZIP packaging functionality in `.claude/skills/clskill-creator/packaging/zip_packager.py`
- [ ] T029 [US3] Implement proper directory structure creation in `.claude/skills/clskill-creator/packaging/structure_manager.py`
- [ ] T030 [US3] Add packaging CLI interface in `.claude/skills/clskill-creator/cli/packaging_cli.py`

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T031 [P] Documentation updates in `.claude/skills/clskill-creator/reference.md`
- [ ] T032 Code cleanup and refactoring
- [ ] T033 Performance optimization across all stories
- [ ] T034 [P] Additional unit tests in tests/unit/
- [ ] T035 Security hardening
- [ ] T036 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence