# Technical Specification

## Todo App – Phase I: In-Memory Python Console Application

**Specification Version:** 1.0
**Date:** December 23, 2025
**Status:** Approved
**Constitutional Reference:** constitution.md v1.0

---

## 1. Overview

### 1.1 Purpose
This specification defines the technical requirements for implementing the Phase I Todo Application as mandated by the Constitution. It serves as the authoritative source for AI-assisted code generation.

### 1.2 Scope
This specification covers:
- Data models and structures
- Core feature implementations
- User interface (CLI) design
- Module architecture
- Input/output specifications

### 1.3 Constitutional Compliance
This specification adheres to:
- Article II: Core Functional Requirements
- Article III: Development Constraints
- Article IV: Architectural & Design Principles
- Article V: Project Structure

---

## 2. System Architecture

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────┐
│                   CLI Layer                      │
│              (User Interface Module)             │
├─────────────────────────────────────────────────┤
│                 Service Layer                    │
│             (Business Logic Module)              │
├─────────────────────────────────────────────────┤
│                  Data Layer                      │
│            (In-Memory Storage Module)            │
└─────────────────────────────────────────────────┘
```

### 2.2 Module Structure

```
src/
└── todo/
    ├── __init__.py          # Package initialization
    ├── __main__.py          # Application entry point
    ├── models.py            # Data models (Task)
    ├── storage.py           # In-memory storage management
    ├── service.py           # Business logic operations
    └── cli.py               # Command-line interface
```

---

## 3. Data Models

### 3.1 Task Model

| Attribute | Type | Description | Constraints |
|-----------|------|-------------|-------------|
| `id` | `int` | Unique task identifier | Auto-incremented, positive integer |
| `title` | `str` | Task title | Required, non-empty, max 100 characters |
| `description` | `str` | Task description | Required, max 500 characters |
| `is_completed` | `bool` | Completion status | Default: `False` |

### 3.2 Task Model Definition

```python
@dataclass
class Task:
    id: int
    title: str
    description: str
    is_completed: bool = False
```

---

## 4. Storage Specification

### 4.1 In-Memory Store

| Component | Type | Purpose |
|-----------|------|---------|
| `_tasks` | `dict[int, Task]` | Primary task storage (id → Task mapping) |
| `_next_id` | `int` | ID counter for new tasks |

### 4.2 Storage Operations

| Operation | Input | Output | Description |
|-----------|-------|--------|-------------|
| `add(task)` | `Task` | `Task` | Store task, return with assigned ID |
| `get(id)` | `int` | `Task \| None` | Retrieve task by ID |
| `get_all()` | None | `list[Task]` | Retrieve all tasks |
| `update(task)` | `Task` | `bool` | Update existing task |
| `delete(id)` | `int` | `bool` | Remove task by ID |
| `clear()` | None | None | Remove all tasks (for testing) |

---

## 5. Service Layer Specification

### 5.1 Service Operations

#### 5.1.1 Add Task
- **Function:** `add_task(title: str, description: str) -> Task`
- **Behavior:**
  1. Validate title is non-empty
  2. Validate description is provided
  3. Create Task instance with `is_completed=False`
  4. Store in memory with auto-generated ID
  5. Return created Task

#### 5.1.2 View All Tasks
- **Function:** `get_all_tasks() -> list[Task]`
- **Behavior:**
  1. Retrieve all tasks from storage
  2. Return list (empty list if no tasks)

#### 5.1.3 Get Task by ID
- **Function:** `get_task(task_id: int) -> Task | None`
- **Behavior:**
  1. Validate task_id is positive integer
  2. Retrieve task from storage
  3. Return Task or None if not found

#### 5.1.4 Update Task
- **Function:** `update_task(task_id: int, title: str | None, description: str | None) -> Task | None`
- **Behavior:**
  1. Retrieve existing task by ID
  2. If not found, return None
  3. Update title if provided and non-empty
  4. Update description if provided
  5. Persist changes
  6. Return updated Task

#### 5.1.5 Delete Task
- **Function:** `delete_task(task_id: int) -> bool`
- **Behavior:**
  1. Attempt to remove task by ID
  2. Return True if deleted, False if not found

#### 5.1.6 Toggle Completion
- **Function:** `toggle_completion(task_id: int) -> Task | None`
- **Behavior:**
  1. Retrieve task by ID
  2. If not found, return None
  3. Invert `is_completed` status
  4. Persist change
  5. Return updated Task

---

## 6. CLI Specification

### 6.1 Main Menu

```
=====================================
       TODO APP - Phase I
=====================================

1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

### 6.2 Command Flows

#### 6.2.1 Add Task Flow
```
--- Add New Task ---
Enter title: [user input]
Enter description: [user input]

✓ Task added successfully! (ID: X)
```

#### 6.2.2 View Tasks Flow
```
--- All Tasks ---

ID: 1 | Status: [ ] Incomplete
Title: Sample Task
Description: This is a sample description

ID: 2 | Status: [✓] Complete
Title: Another Task
Description: Another description

---
Total: 2 task(s)
```

**Empty State:**
```
--- All Tasks ---

No tasks found. Add a task to get started!
```

#### 6.2.3 Update Task Flow
```
--- Update Task ---
Enter task ID to update: [user input]

Current Task:
Title: Old Title
Description: Old Description

Enter new title (press Enter to keep current): [user input]
Enter new description (press Enter to keep current): [user input]

✓ Task updated successfully!
```

**Error State:**
```
✗ Task with ID X not found.
```

#### 6.2.4 Delete Task Flow
```
--- Delete Task ---
Enter task ID to delete: [user input]

✓ Task deleted successfully!
```

**Error State:**
```
✗ Task with ID X not found.
```

#### 6.2.5 Toggle Completion Flow
```
--- Toggle Task Completion ---
Enter task ID: [user input]

✓ Task marked as complete!
```
or
```
✓ Task marked as incomplete!
```

**Error State:**
```
✗ Task with ID X not found.
```

#### 6.2.6 Exit Flow
```
Goodbye! Thank you for using Todo App.
```

### 6.3 Input Validation

| Input | Validation Rule | Error Message |
|-------|-----------------|---------------|
| Menu choice | Must be 1-6 | "Invalid choice. Please enter 1-6." |
| Task ID | Must be positive integer | "Invalid ID. Please enter a valid number." |
| Title | Non-empty, max 100 chars | "Title cannot be empty." / "Title too long (max 100 characters)." |
| Description | Max 500 chars | "Description too long (max 500 characters)." |

---

## 7. Error Handling

### 7.1 Error Categories

| Category | Handling Strategy |
|----------|-------------------|
| Invalid Input | Display error message, re-prompt |
| Task Not Found | Display "not found" message, return to menu |
| Unexpected Error | Display generic error, continue operation |

### 7.2 Error Messages

All error messages SHALL:
- Begin with "✗" symbol
- Be clear and actionable
- Not expose internal implementation details

---

## 8. Application Entry Point

### 8.1 Main Execution

```python
# __main__.py
def main():
    """Application entry point."""
    cli = TodoCLI()
    cli.run()

if __name__ == "__main__":
    main()
```

### 8.2 Invocation Methods

```bash
# Method 1: Module execution
python -m todo

# Method 2: Direct script (if configured)
python src/todo/__main__.py
```

---

## 9. Dependencies

### 9.1 External Dependencies
None. Phase I uses only Python standard library.

### 9.2 Python Version
Python 3.13+ (as mandated by Constitution Article III)

### 9.3 pyproject.toml Specification

```toml
[project]
name = "todo-app"
version = "0.1.0"
description = "Phase I: In-Memory Python Console Todo Application"
requires-python = ">=3.13"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/todo"]
```

---

## 10. Testing Considerations

### 10.1 Testable Components
- Storage operations (CRUD)
- Service layer functions
- Input validation logic

### 10.2 Test Strategy
Unit tests SHALL verify:
- Task creation with valid data
- Task retrieval by ID
- Task update operations
- Task deletion operations
- Completion toggle functionality
- Empty state handling
- Invalid input handling

---

## 11. Future Phase Considerations

This specification is designed to facilitate evolution to subsequent phases:
- **Phase II:** File-based persistence (storage layer abstraction)
- **Phase III:** Database integration (storage interface)
- **Phase IV+:** API layer, cloud deployment (service layer extension)

The layered architecture ensures minimal refactoring for future enhancements.

---

## 12. Acceptance Criteria

Phase I implementation SHALL be accepted when:

1. [ ] All five core features function correctly
2. [ ] Menu navigation works without errors
3. [ ] Input validation prevents invalid data
4. [ ] Error messages display appropriately
5. [ ] Application runs via `python -m todo`
6. [ ] Code follows clean code principles
7. [ ] Project structure matches Article V mandate
8. [ ] No external dependencies used

---

## 13. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-23 | Product Architect | Initial specification |

---

## 14. Approval

**Specification Status:** APPROVED FOR IMPLEMENTATION

**Constitutional Compliance:** VERIFIED

**Date:** December 23, 2025

---

*This specification derives authority from constitution.md and serves as the binding reference for AI-assisted code generation.*
