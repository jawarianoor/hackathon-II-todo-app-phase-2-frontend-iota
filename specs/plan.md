# Implementation Plan

## Todo App – Phase I: In-Memory Python Console Application

**Plan Version:** 1.0
**Date:** December 23, 2025
**Status:** Ready for Implementation
**Specification Reference:** specify.md v1.0
**Constitutional Reference:** constitution.md v1.0

---

## 1. Plan Overview

### 1.1 Purpose
This document outlines the step-by-step implementation plan for Phase I of the Todo Application. It provides a structured approach for AI-assisted code generation following the approved specification.

### 1.2 Implementation Approach
- **Bottom-Up Development:** Build from data layer to presentation layer
- **Incremental Validation:** Test each layer before proceeding
- **Specification Compliance:** Every implementation step traces to specify.md

---

## 2. Pre-Implementation Checklist

Before beginning implementation, ensure:

- [x] Constitution.md is finalized and approved
- [x] Specification (specify.md) is complete and approved
- [ ] Development environment is configured (WSL 2, Python 3.13+, UV)
- [ ] Project directory structure is initialized

---

## 3. Implementation Phases

### Phase 1: Project Setup
**Priority:** Critical
**Dependencies:** None

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 1.1 | Initialize UV project | `pyproject.toml` | Section 9.3 |
| 1.2 | Create directory structure | `src/todo/` folder | Section 2.2 |
| 1.3 | Create package `__init__.py` | `src/todo/__init__.py` | Section 2.2 |
| 1.4 | Create supporting documents | `README.md`, `CLAUDE.md` | Constitution Art. V |

**Acceptance Criteria:**
- [ ] `uv` recognizes project structure
- [ ] `src/todo/` directory exists with `__init__.py`
- [ ] All required root files present

---

### Phase 2: Data Layer Implementation
**Priority:** Critical
**Dependencies:** Phase 1

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 2.1 | Implement Task dataclass | `src/todo/models.py` | Section 3 |
| 2.2 | Implement TaskStorage class | `src/todo/storage.py` | Section 4 |

#### 2.1 Task Model Implementation

**File:** `src/todo/models.py`

**Requirements:**
- Use `@dataclass` decorator
- Implement all attributes: `id`, `title`, `description`, `is_completed`
- Set `is_completed` default to `False`
- Use type hints for all attributes

**Acceptance Criteria:**
- [ ] Task can be instantiated with required fields
- [ ] Default values work correctly
- [ ] Type hints are present

#### 2.2 Storage Implementation

**File:** `src/todo/storage.py`

**Requirements:**
- Implement `TaskStorage` class
- Private `_tasks: dict[int, Task]` for storage
- Private `_next_id: int` starting at 1
- Implement all operations: `add`, `get`, `get_all`, `update`, `delete`, `clear`

**Acceptance Criteria:**
- [ ] Tasks can be added with auto-generated IDs
- [ ] Tasks can be retrieved by ID
- [ ] All tasks can be listed
- [ ] Tasks can be updated
- [ ] Tasks can be deleted
- [ ] Storage can be cleared

---

### Phase 3: Service Layer Implementation
**Priority:** Critical
**Dependencies:** Phase 2

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 3.1 | Implement TodoService class | `src/todo/service.py` | Section 5 |

**File:** `src/todo/service.py`

**Requirements:**
- Implement `TodoService` class
- Inject `TaskStorage` dependency
- Implement all service operations:
  - `add_task(title, description) -> Task`
  - `get_all_tasks() -> list[Task]`
  - `get_task(task_id) -> Task | None`
  - `update_task(task_id, title, description) -> Task | None`
  - `delete_task(task_id) -> bool`
  - `toggle_completion(task_id) -> Task | None`

**Acceptance Criteria:**
- [ ] All six service methods implemented
- [ ] Input validation in service layer
- [ ] Proper None/bool returns for error cases

---

### Phase 4: CLI Layer Implementation
**Priority:** Critical
**Dependencies:** Phase 3

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 4.1 | Implement TodoCLI class | `src/todo/cli.py` | Section 6 |
| 4.2 | Implement main menu | Menu display and routing | Section 6.1 |
| 4.3 | Implement Add Task flow | Option 1 handler | Section 6.2.1 |
| 4.4 | Implement View Tasks flow | Option 2 handler | Section 6.2.2 |
| 4.5 | Implement Update Task flow | Option 3 handler | Section 6.2.3 |
| 4.6 | Implement Delete Task flow | Option 4 handler | Section 6.2.4 |
| 4.7 | Implement Toggle flow | Option 5 handler | Section 6.2.5 |
| 4.8 | Implement Exit flow | Option 6 handler | Section 6.2.6 |
| 4.9 | Implement input validation | All input handlers | Section 6.3 |

**File:** `src/todo/cli.py`

**Requirements:**
- Implement `TodoCLI` class
- Inject `TodoService` dependency
- Main loop with menu display
- Individual handler methods for each menu option
- Input validation with error messages
- Consistent formatting per spec

**Acceptance Criteria:**
- [ ] Menu displays correctly
- [ ] All 6 menu options work
- [ ] Input validation prevents invalid data
- [ ] Error messages match specification
- [ ] Exit terminates cleanly

---

### Phase 5: Application Entry Point
**Priority:** Critical
**Dependencies:** Phase 4

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 5.1 | Implement `__main__.py` | `src/todo/__main__.py` | Section 8 |

**File:** `src/todo/__main__.py`

**Requirements:**
- Import and instantiate all components
- Wire dependencies (Storage → Service → CLI)
- Implement `main()` function
- Add `if __name__ == "__main__"` guard

**Acceptance Criteria:**
- [ ] `python -m todo` launches application
- [ ] All components properly initialized
- [ ] Application runs without import errors

---

### Phase 6: Documentation
**Priority:** High
**Dependencies:** Phase 5

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 6.1 | Write README.md | `README.md` | Constitution Art. V |
| 6.2 | Write CLAUDE.md | `CLAUDE.md` | Constitution Art. V |

#### 6.1 README.md Content

- Project title and description
- Phase I overview
- Prerequisites (Python 3.13+, UV)
- Installation instructions
- Usage instructions
- Project structure
- Feature list

#### 6.2 CLAUDE.md Content

- AI assistant usage guidelines
- Specification-driven development rules
- Code generation principles
- Prohibited actions
- Required practices

**Acceptance Criteria:**
- [ ] README provides complete setup instructions
- [ ] CLAUDE.md defines AI usage rules

---

### Phase 7: Validation & Testing
**Priority:** High
**Dependencies:** Phase 6

| Step | Task | Deliverable | Spec Reference |
|------|------|-------------|----------------|
| 7.1 | Manual feature testing | Test results | Section 12 |
| 7.2 | Validate acceptance criteria | Checklist completion | Section 12 |

**Test Scenarios:**

1. **Add Task Test**
   - Add task with valid title and description
   - Verify ID assignment
   - Verify task appears in list

2. **View Tasks Test**
   - View empty list (empty state message)
   - View list with multiple tasks
   - Verify all fields displayed

3. **Update Task Test**
   - Update existing task title
   - Update existing task description
   - Update both fields
   - Attempt update on non-existent ID

4. **Delete Task Test**
   - Delete existing task
   - Verify removal from list
   - Attempt delete on non-existent ID

5. **Toggle Completion Test**
   - Toggle incomplete to complete
   - Toggle complete to incomplete
   - Attempt toggle on non-existent ID

6. **Input Validation Test**
   - Invalid menu choices
   - Non-numeric task IDs
   - Empty title
   - Oversized inputs

**Acceptance Criteria:**
- [ ] All 5 core features pass testing
- [ ] All validation scenarios handled
- [ ] No unhandled exceptions

---

## 4. Implementation Order Summary

```
┌─────────────────────────────────────────────────────────────┐
│  Phase 1: Project Setup                                      │
│  └─► pyproject.toml, directory structure, __init__.py        │
├─────────────────────────────────────────────────────────────┤
│  Phase 2: Data Layer                                         │
│  └─► models.py (Task) → storage.py (TaskStorage)             │
├─────────────────────────────────────────────────────────────┤
│  Phase 3: Service Layer                                      │
│  └─► service.py (TodoService)                                │
├─────────────────────────────────────────────────────────────┤
│  Phase 4: CLI Layer                                          │
│  └─► cli.py (TodoCLI) with all menu handlers                 │
├─────────────────────────────────────────────────────────────┤
│  Phase 5: Entry Point                                        │
│  └─► __main__.py (wiring and main function)                  │
├─────────────────────────────────────────────────────────────┤
│  Phase 6: Documentation                                      │
│  └─► README.md, CLAUDE.md                                    │
├─────────────────────────────────────────────────────────────┤
│  Phase 7: Validation                                         │
│  └─► Manual testing, acceptance criteria verification        │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. File Creation Order

| Order | File | Purpose |
|-------|------|---------|
| 1 | `pyproject.toml` | Project configuration |
| 2 | `src/todo/__init__.py` | Package initialization |
| 3 | `src/todo/models.py` | Task data model |
| 4 | `src/todo/storage.py` | In-memory storage |
| 5 | `src/todo/service.py` | Business logic |
| 6 | `src/todo/cli.py` | User interface |
| 7 | `src/todo/__main__.py` | Entry point |
| 8 | `README.md` | User documentation |
| 9 | `CLAUDE.md` | AI guidelines |

---

## 6. Risk Mitigation

| Risk | Mitigation Strategy |
|------|---------------------|
| Import errors between modules | Follow strict implementation order |
| Circular dependencies | Use dependency injection pattern |
| Input validation gaps | Test all edge cases per Section 6.3 |
| Specification deviation | Cross-reference spec during review |

---

## 7. Completion Checklist

### Core Features
- [ ] Add Task functionality complete
- [ ] View Task List functionality complete
- [ ] Update Task functionality complete
- [ ] Delete Task functionality complete
- [ ] Toggle Completion functionality complete

### Project Structure
- [ ] `src/todo/` package exists
- [ ] All 6 module files created
- [ ] `pyproject.toml` configured
- [ ] `README.md` complete
- [ ] `CLAUDE.md` complete

### Quality Assurance
- [ ] All acceptance criteria met (Section 12 of specify.md)
- [ ] No external dependencies
- [ ] Clean code principles followed
- [ ] Input validation comprehensive
- [ ] Error handling consistent

---

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Product Architect | Initial plan |

---

## 9. Approval

**Plan Status:** APPROVED FOR EXECUTION

**Specification Compliance:** VERIFIED

**Constitutional Compliance:** VERIFIED

**Date:** December 23, 2025

---

*This implementation plan derives authority from specify.md and constitution.md. All implementation must follow this plan sequentially.*
