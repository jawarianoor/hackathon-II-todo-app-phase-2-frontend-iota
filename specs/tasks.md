# Task Breakdown

## Todo App – Phase I: In-Memory Python Console Application

**Document Version:** 1.0
**Date:** December 23, 2025
**Status:** Ready for Execution
**Plan Reference:** plan.md v1.0
**Specification Reference:** specify.md v1.0

---

## 1. Task Overview

This document breaks down the implementation plan into discrete, achievable tasks. Each task is atomic, testable, and has clear completion criteria.

**Total Tasks:** 25
**Estimated Complexity:** Low to Medium

---

## 2. Task Legend

| Symbol | Meaning |
|--------|---------|
| `[ ]` | Not Started |
| `[~]` | In Progress |
| `[x]` | Completed |
| `[!]` | Blocked |

**Priority Levels:**
- **P0:** Critical - Must complete, blocks other tasks
- **P1:** High - Important for functionality
- **P2:** Medium - Enhances quality
- **P3:** Low - Nice to have

---

## 3. Task List

### MILESTONE 1: Project Foundation
**Goal:** Establish project structure and configuration

---

#### TASK-001: Initialize UV Project
**Priority:** P0
**Status:** `[ ]`
**Dependency:** None
**Deliverable:** `pyproject.toml`

**Description:**
Initialize the project using UV package manager with proper configuration.

**Steps:**
1. Run `uv init` in project root
2. Configure `pyproject.toml` with:
   - Project name: `todo-app`
   - Version: `0.1.0`
   - Python requirement: `>=3.13`
   - No external dependencies

**Acceptance Criteria:**
- [ ] `pyproject.toml` exists in project root
- [ ] Python version constraint is `>=3.13`
- [ ] No external dependencies listed

---

#### TASK-002: Create Source Directory Structure
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-001
**Deliverable:** `src/todo/` directory

**Description:**
Create the required directory structure for the application package.

**Steps:**
1. Create `src/` directory
2. Create `src/todo/` directory

**Acceptance Criteria:**
- [ ] `src/` directory exists
- [ ] `src/todo/` directory exists

---

#### TASK-003: Create Package Initialization File
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-002
**Deliverable:** `src/todo/__init__.py`

**Description:**
Create the package initialization file to make `todo` a Python package.

**Steps:**
1. Create `__init__.py` in `src/todo/`
2. Add package version and docstring

**Acceptance Criteria:**
- [ ] `src/todo/__init__.py` exists
- [ ] Package is importable

---

### MILESTONE 2: Data Layer
**Goal:** Implement data models and storage

---

#### TASK-004: Implement Task Data Model
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-003
**Deliverable:** `src/todo/models.py`

**Description:**
Create the Task dataclass with all required attributes.

**Steps:**
1. Create `models.py` file
2. Import `dataclass` from `dataclasses`
3. Define `Task` class with:
   - `id: int`
   - `title: str`
   - `description: str`
   - `is_completed: bool = False`

**Acceptance Criteria:**
- [ ] Task dataclass is defined
- [ ] All four attributes present with correct types
- [ ] `is_completed` defaults to `False`
- [ ] Task can be instantiated

---

#### TASK-005: Implement TaskStorage Class Structure
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-004
**Deliverable:** `src/todo/storage.py` (partial)

**Description:**
Create the TaskStorage class with internal data structures.

**Steps:**
1. Create `storage.py` file
2. Import `Task` from models
3. Define `TaskStorage` class
4. Initialize `_tasks: dict[int, Task]` as empty dict
5. Initialize `_next_id: int` starting at 1

**Acceptance Criteria:**
- [ ] TaskStorage class exists
- [ ] Private `_tasks` dictionary initialized
- [ ] Private `_next_id` counter initialized to 1

---

#### TASK-006: Implement Storage Add Operation
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-005
**Deliverable:** `add()` method in storage.py

**Description:**
Implement the add method to store new tasks.

**Steps:**
1. Define `add(self, task: Task) -> Task` method
2. Assign `_next_id` to task
3. Store task in `_tasks` dictionary
4. Increment `_next_id`
5. Return the task with assigned ID

**Acceptance Criteria:**
- [ ] Tasks receive auto-incremented IDs
- [ ] Tasks are stored in `_tasks` dictionary
- [ ] Method returns the stored task

---

#### TASK-007: Implement Storage Get Operations
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-006
**Deliverable:** `get()` and `get_all()` methods

**Description:**
Implement methods to retrieve tasks from storage.

**Steps:**
1. Define `get(self, task_id: int) -> Task | None`
2. Define `get_all(self) -> list[Task]`

**Acceptance Criteria:**
- [ ] `get()` returns Task or None
- [ ] `get_all()` returns list of all tasks
- [ ] Empty storage returns empty list

---

#### TASK-008: Implement Storage Update Operation
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-007
**Deliverable:** `update()` method

**Description:**
Implement method to update existing tasks.

**Steps:**
1. Define `update(self, task: Task) -> bool`
2. Check if task ID exists
3. Replace task in storage
4. Return True if updated, False if not found

**Acceptance Criteria:**
- [ ] Existing tasks can be updated
- [ ] Returns True on success
- [ ] Returns False if task not found

---

#### TASK-009: Implement Storage Delete Operation
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-008
**Deliverable:** `delete()` method

**Description:**
Implement method to remove tasks from storage.

**Steps:**
1. Define `delete(self, task_id: int) -> bool`
2. Check if task ID exists
3. Remove from storage
4. Return True if deleted, False if not found

**Acceptance Criteria:**
- [ ] Tasks can be deleted by ID
- [ ] Returns True on success
- [ ] Returns False if task not found

---

#### TASK-010: Implement Storage Clear Operation
**Priority:** P2
**Status:** `[ ]`
**Dependency:** TASK-009
**Deliverable:** `clear()` method

**Description:**
Implement method to clear all tasks (for testing purposes).

**Steps:**
1. Define `clear(self) -> None`
2. Reset `_tasks` to empty dict
3. Reset `_next_id` to 1

**Acceptance Criteria:**
- [ ] All tasks removed
- [ ] ID counter reset

---

### MILESTONE 3: Service Layer
**Goal:** Implement business logic operations

---

#### TASK-011: Implement TodoService Class Structure
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-010
**Deliverable:** `src/todo/service.py` (partial)

**Description:**
Create the TodoService class with storage dependency.

**Steps:**
1. Create `service.py` file
2. Import `Task` and `TaskStorage`
3. Define `TodoService` class
4. Accept `TaskStorage` in constructor
5. Store as instance variable

**Acceptance Criteria:**
- [ ] TodoService class exists
- [ ] Storage dependency injected via constructor

---

#### TASK-012: Implement Add Task Service
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-011
**Deliverable:** `add_task()` method

**Description:**
Implement service method to add new tasks.

**Steps:**
1. Define `add_task(self, title: str, description: str) -> Task`
2. Validate title is non-empty
3. Create Task instance (id=0 placeholder)
4. Call storage.add()
5. Return created task

**Acceptance Criteria:**
- [ ] Tasks created with title and description
- [ ] Empty title raises error or is handled
- [ ] Returns created Task with ID

---

#### TASK-013: Implement Get Tasks Services
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-012
**Deliverable:** `get_all_tasks()` and `get_task()` methods

**Description:**
Implement service methods to retrieve tasks.

**Steps:**
1. Define `get_all_tasks(self) -> list[Task]`
2. Define `get_task(self, task_id: int) -> Task | None`
3. Delegate to storage layer

**Acceptance Criteria:**
- [ ] All tasks retrievable
- [ ] Single task retrievable by ID
- [ ] None returned for non-existent ID

---

#### TASK-014: Implement Update Task Service
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-013
**Deliverable:** `update_task()` method

**Description:**
Implement service method to update tasks.

**Steps:**
1. Define `update_task(self, task_id: int, title: str | None, description: str | None) -> Task | None`
2. Retrieve existing task
3. Update fields if provided
4. Call storage.update()
5. Return updated task or None

**Acceptance Criteria:**
- [ ] Task title updateable
- [ ] Task description updateable
- [ ] Partial updates supported
- [ ] None returned if task not found

---

#### TASK-015: Implement Delete Task Service
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-014
**Deliverable:** `delete_task()` method

**Description:**
Implement service method to delete tasks.

**Steps:**
1. Define `delete_task(self, task_id: int) -> bool`
2. Delegate to storage.delete()
3. Return result

**Acceptance Criteria:**
- [ ] Tasks deletable by ID
- [ ] Returns True on success
- [ ] Returns False if not found

---

#### TASK-016: Implement Toggle Completion Service
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-015
**Deliverable:** `toggle_completion()` method

**Description:**
Implement service method to toggle task completion status.

**Steps:**
1. Define `toggle_completion(self, task_id: int) -> Task | None`
2. Retrieve task by ID
3. Invert `is_completed` value
4. Update in storage
5. Return updated task or None

**Acceptance Criteria:**
- [ ] Completion status toggles correctly
- [ ] Returns updated Task
- [ ] Returns None if not found

---

### MILESTONE 4: CLI Layer
**Goal:** Implement user interface

---

#### TASK-017: Implement TodoCLI Class Structure
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-016
**Deliverable:** `src/todo/cli.py` (partial)

**Description:**
Create the TodoCLI class with service dependency and main loop.

**Steps:**
1. Create `cli.py` file
2. Import `TodoService`
3. Define `TodoCLI` class
4. Accept `TodoService` in constructor
5. Implement `run()` method with main loop

**Acceptance Criteria:**
- [ ] TodoCLI class exists
- [ ] Service dependency injected
- [ ] Main loop implemented

---

#### TASK-018: Implement Main Menu Display
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-017
**Deliverable:** Menu display method

**Description:**
Implement the main menu display as per specification.

**Steps:**
1. Define `_display_menu(self)` method
2. Print header with app title
3. Print numbered menu options (1-6)
4. Print input prompt

**Acceptance Criteria:**
- [ ] Menu matches specification format
- [ ] All 6 options displayed
- [ ] Clear visual formatting

---

#### TASK-019: Implement Add Task Handler
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-018
**Deliverable:** Add task CLI handler

**Description:**
Implement CLI handler for adding new tasks.

**Steps:**
1. Define `_handle_add_task(self)` method
2. Prompt for title
3. Validate title (non-empty, max 100 chars)
4. Prompt for description
5. Validate description (max 500 chars)
6. Call service.add_task()
7. Display success message with ID

**Acceptance Criteria:**
- [ ] Title and description collected
- [ ] Input validation applied
- [ ] Success message displayed

---

#### TASK-020: Implement View Tasks Handler
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-019
**Deliverable:** View tasks CLI handler

**Description:**
Implement CLI handler for viewing all tasks.

**Steps:**
1. Define `_handle_view_tasks(self)` method
2. Call service.get_all_tasks()
3. If empty, display "No tasks found" message
4. If tasks exist, display formatted list
5. Show total count

**Acceptance Criteria:**
- [ ] Empty state handled
- [ ] Tasks display with ID, status, title, description
- [ ] Completion status shown correctly

---

#### TASK-021: Implement Update Task Handler
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-020
**Deliverable:** Update task CLI handler

**Description:**
Implement CLI handler for updating tasks.

**Steps:**
1. Define `_handle_update_task(self)` method
2. Prompt for task ID
3. Validate ID is positive integer
4. Retrieve and display current task
5. If not found, show error
6. Prompt for new title (Enter to skip)
7. Prompt for new description (Enter to skip)
8. Call service.update_task()
9. Display success message

**Acceptance Criteria:**
- [ ] Task ID validated
- [ ] Current values shown
- [ ] Partial updates supported
- [ ] Error shown if not found

---

#### TASK-022: Implement Delete Task Handler
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-021
**Deliverable:** Delete task CLI handler

**Description:**
Implement CLI handler for deleting tasks.

**Steps:**
1. Define `_handle_delete_task(self)` method
2. Prompt for task ID
3. Validate ID
4. Call service.delete_task()
5. Display success or error message

**Acceptance Criteria:**
- [ ] Task ID validated
- [ ] Success message on deletion
- [ ] Error message if not found

---

#### TASK-023: Implement Toggle Completion Handler
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-022
**Deliverable:** Toggle completion CLI handler

**Description:**
Implement CLI handler for toggling task completion.

**Steps:**
1. Define `_handle_toggle_completion(self)` method
2. Prompt for task ID
3. Validate ID
4. Call service.toggle_completion()
5. Display appropriate message based on new status

**Acceptance Criteria:**
- [ ] Task ID validated
- [ ] Correct message for complete/incomplete
- [ ] Error message if not found

---

### MILESTONE 5: Application Entry Point
**Goal:** Wire components and create executable entry

---

#### TASK-024: Implement Application Entry Point
**Priority:** P0
**Status:** `[ ]`
**Dependency:** TASK-023
**Deliverable:** `src/todo/__main__.py`

**Description:**
Create the main entry point that wires all components.

**Steps:**
1. Create `__main__.py` file
2. Import TaskStorage, TodoService, TodoCLI
3. Define `main()` function
4. Instantiate components with dependency injection:
   - storage = TaskStorage()
   - service = TodoService(storage)
   - cli = TodoCLI(service)
5. Call cli.run()
6. Add `if __name__ == "__main__"` guard

**Acceptance Criteria:**
- [ ] All components imported
- [ ] Dependencies properly wired
- [ ] `python -m todo` works

---

### MILESTONE 6: Documentation
**Goal:** Create required documentation files

---

#### TASK-025: Create README and CLAUDE Documentation
**Priority:** P1
**Status:** `[ ]`
**Dependency:** TASK-024
**Deliverable:** `README.md`, `CLAUDE.md`

**Description:**
Create the required documentation files.

**Steps:**
1. Create `README.md` with:
   - Project title and description
   - Prerequisites
   - Installation instructions
   - Usage instructions
   - Project structure
   - Feature list
2. Create `CLAUDE.md` with:
   - AI usage guidelines
   - Specification-driven rules
   - Prohibited actions

**Acceptance Criteria:**
- [ ] README provides complete setup guide
- [ ] CLAUDE.md defines AI constraints

---

## 4. Task Dependencies Graph

```
TASK-001 (UV Init)
    │
    ▼
TASK-002 (Dir Structure)
    │
    ▼
TASK-003 (__init__.py)
    │
    ▼
TASK-004 (Task Model)
    │
    ▼
TASK-005 (Storage Class)
    │
    ├──► TASK-006 (Add)
    │        │
    │        ▼
    │    TASK-007 (Get/GetAll)
    │        │
    │        ▼
    │    TASK-008 (Update)
    │        │
    │        ▼
    │    TASK-009 (Delete)
    │        │
    │        ▼
    │    TASK-010 (Clear)
    │
    ▼
TASK-011 (Service Class)
    │
    ├──► TASK-012 (Add Task)
    │        │
    │        ▼
    │    TASK-013 (Get Tasks)
    │        │
    │        ▼
    │    TASK-014 (Update Task)
    │        │
    │        ▼
    │    TASK-015 (Delete Task)
    │        │
    │        ▼
    │    TASK-016 (Toggle)
    │
    ▼
TASK-017 (CLI Class)
    │
    ├──► TASK-018 (Menu)
    │        │
    │        ▼
    │    TASK-019 (Add Handler)
    │        │
    │        ▼
    │    TASK-020 (View Handler)
    │        │
    │        ▼
    │    TASK-021 (Update Handler)
    │        │
    │        ▼
    │    TASK-022 (Delete Handler)
    │        │
    │        ▼
    │    TASK-023 (Toggle Handler)
    │
    ▼
TASK-024 (__main__.py)
    │
    ▼
TASK-025 (Documentation)
```

---

## 5. Milestone Summary

| Milestone | Tasks | Priority | Description |
|-----------|-------|----------|-------------|
| 1 | TASK-001 to TASK-003 | P0 | Project foundation |
| 2 | TASK-004 to TASK-010 | P0 | Data layer (models, storage) |
| 3 | TASK-011 to TASK-016 | P0 | Service layer (business logic) |
| 4 | TASK-017 to TASK-023 | P0 | CLI layer (user interface) |
| 5 | TASK-024 | P0 | Application entry point |
| 6 | TASK-025 | P1 | Documentation |

---

## 6. Quick Reference

### Critical Path Tasks (P0)
All tasks from TASK-001 to TASK-024 are critical path items.

### Files to Create
| Task | File |
|------|------|
| TASK-001 | `pyproject.toml` |
| TASK-003 | `src/todo/__init__.py` |
| TASK-004 | `src/todo/models.py` |
| TASK-005-010 | `src/todo/storage.py` |
| TASK-011-016 | `src/todo/service.py` |
| TASK-017-023 | `src/todo/cli.py` |
| TASK-024 | `src/todo/__main__.py` |
| TASK-025 | `README.md`, `CLAUDE.md` |

---

## 7. Execution Checklist

### Milestone 1: Project Foundation
- [ ] TASK-001: Initialize UV Project
- [ ] TASK-002: Create Source Directory Structure
- [ ] TASK-003: Create Package Initialization File

### Milestone 2: Data Layer
- [ ] TASK-004: Implement Task Data Model
- [ ] TASK-005: Implement TaskStorage Class Structure
- [ ] TASK-006: Implement Storage Add Operation
- [ ] TASK-007: Implement Storage Get Operations
- [ ] TASK-008: Implement Storage Update Operation
- [ ] TASK-009: Implement Storage Delete Operation
- [ ] TASK-010: Implement Storage Clear Operation

### Milestone 3: Service Layer
- [ ] TASK-011: Implement TodoService Class Structure
- [ ] TASK-012: Implement Add Task Service
- [ ] TASK-013: Implement Get Tasks Services
- [ ] TASK-014: Implement Update Task Service
- [ ] TASK-015: Implement Delete Task Service
- [ ] TASK-016: Implement Toggle Completion Service

### Milestone 4: CLI Layer
- [ ] TASK-017: Implement TodoCLI Class Structure
- [ ] TASK-018: Implement Main Menu Display
- [ ] TASK-019: Implement Add Task Handler
- [ ] TASK-020: Implement View Tasks Handler
- [ ] TASK-021: Implement Update Task Handler
- [ ] TASK-022: Implement Delete Task Handler
- [ ] TASK-023: Implement Toggle Completion Handler

### Milestone 5: Application Entry Point
- [ ] TASK-024: Implement Application Entry Point

### Milestone 6: Documentation
- [ ] TASK-025: Create README and CLAUDE Documentation

---

## 8. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Product Architect | Initial task breakdown |

---

## 9. Approval

**Task Breakdown Status:** APPROVED FOR EXECUTION

**Plan Compliance:** VERIFIED

**Date:** December 23, 2025

---

*Execute tasks in order. Mark each task complete before proceeding to the next. Report blockers immediately.*
