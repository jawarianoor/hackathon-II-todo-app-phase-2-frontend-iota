# Tasks: Phase II Full-Stack Todo Web Application

**Input**: Design documents from `/specs/001-fullstack-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/openapi.yaml, research.md, quickstart.md

**Tests**: Tests are NOT explicitly requested in the specification. Implementation tasks only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/`, `backend/tests/`
- **Frontend**: `frontend/src/`, `frontend/tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for both frontend and backend

- [X] T001 Create backend directory structure per plan.md at `backend/`
- [X] T002 Create frontend directory structure per plan.md at `frontend/`
- [X] T003 [P] Initialize Python project with pyproject.toml at `backend/pyproject.toml`
- [X] T004 [P] Create requirements.txt with FastAPI, SQLModel, python-jose, asyncpg, bcrypt at `backend/requirements.txt`
- [X] T005 [P] Initialize Next.js project with TypeScript at `frontend/package.json`
- [X] T006 [P] Configure TypeScript strict mode at `frontend/tsconfig.json`
- [X] T007 [P] Configure Tailwind CSS at `frontend/tailwind.config.js`
- [X] T008 [P] Create Next.js config at `frontend/next.config.js`
- [X] T009 [P] Create backend CLAUDE.md with FastAPI guidelines at `backend/CLAUDE.md`
- [X] T010 [P] Create frontend CLAUDE.md with Next.js guidelines at `frontend/CLAUDE.md`
- [X] T011 [P] Update root CLAUDE.md for Phase II monorepo at `CLAUDE.md`

**Checkpoint**: Project structure ready - both frontend and backend initialized

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

### Backend Foundation

- [X] T012 Create environment configuration module at `backend/src/config.py`
- [X] T013 Create database connection module with async SQLModel at `backend/src/database.py`
- [X] T014 [P] Create User SQLModel in `backend/src/models/user.py`
- [X] T015 [P] Create Task SQLModel in `backend/src/models/task.py`
- [X] T016 Create models __init__.py exporting all models at `backend/src/models/__init__.py`
- [X] T017 [P] Create user Pydantic schemas at `backend/src/schemas/user.py`
- [X] T018 [P] Create task Pydantic schemas at `backend/src/schemas/task.py`
- [X] T019 Create schemas __init__.py exporting all schemas at `backend/src/schemas/__init__.py`
- [X] T020 Create JWT verification module at `backend/src/auth/jwt.py`
- [X] T021 Create auth __init__.py at `backend/src/auth/__init__.py`
- [X] T022 Create API dependencies (get_current_user, get_db) at `backend/src/api/deps.py`
- [X] T023 Create FastAPI main app with CORS middleware at `backend/src/main.py`
- [X] T024 Create backend src __init__.py at `backend/src/__init__.py`

### Frontend Foundation

- [X] T025 [P] Create User TypeScript types at `frontend/src/types/user.ts`
- [X] T026 [P] Create Task TypeScript types at `frontend/src/types/task.ts`
- [X] T027 Create utility functions at `frontend/src/lib/utils.ts`
- [X] T028 Create centralized API client with JWT injection at `frontend/src/lib/api-client.ts`
- [X] T029 Configure Better Auth at `frontend/src/lib/auth.ts`
- [X] T030 [P] Create Button UI component at `frontend/src/components/ui/button.tsx`
- [X] T031 [P] Create Input UI component at `frontend/src/components/ui/input.tsx`
- [X] T032 [P] Create Card UI component at `frontend/src/components/ui/card.tsx`
- [X] T033 Create root layout with providers at `frontend/src/app/layout.tsx`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1)

**Goal**: Users can register, login, logout, and have protected routes

**Independent Test**: Register a new account, login with credentials, verify session, logout successfully

### Implementation for User Story 1

- [X] T034 [US1] Create registration form component at `frontend/src/components/auth/register-form.tsx`
- [X] T035 [US1] Create login form component at `frontend/src/components/auth/login-form.tsx`
- [X] T036 [US1] Create register page at `frontend/src/app/auth/register/page.tsx`
- [X] T037 [US1] Create login page at `frontend/src/app/auth/login/page.tsx`
- [X] T038 [US1] Create landing page with login/register links at `frontend/src/app/page.tsx`
- [X] T039 [US1] Create protected dashboard layout with auth check at `frontend/src/app/dashboard/layout.tsx`
- [X] T040 [US1] Add Better Auth API routes at `frontend/src/app/api/auth/[...all]/route.ts`
- [X] T041 [US1] Implement logout functionality in dashboard layout

**Checkpoint**: User Story 1 complete - users can register, login, and access protected routes

---

## Phase 4: User Story 2 - View Personal Task List (Priority: P2)

**Goal**: Authenticated users can see their task list on the dashboard

**Independent Test**: Login, navigate to dashboard, verify task list displays correctly (or empty state)

### Implementation for User Story 2

- [X] T042 [US2] Create TaskService with get_user_tasks method at `backend/src/services/task_service.py`
- [X] T043 [US2] Create services __init__.py at `backend/src/services/__init__.py`
- [X] T044 [US2] Create GET /api/{user_id}/tasks endpoint at `backend/src/api/routes/tasks.py`
- [X] T045 [US2] Create routes __init__.py and register router at `backend/src/api/routes/__init__.py`
- [X] T046 [US2] Register task routes in main app at `backend/src/main.py` (update)
- [X] T047 [US2] Create empty state component at `frontend/src/components/tasks/empty-state.tsx`
- [X] T048 [US2] Create task item component at `frontend/src/components/tasks/task-item.tsx`
- [X] T049 [US2] Create task list component at `frontend/src/components/tasks/task-list.tsx`
- [X] T050 [US2] Create dashboard page with task list at `frontend/src/app/dashboard/page.tsx`

**Checkpoint**: User Story 2 complete - users can view their task list

---

## Phase 5: User Story 3 - Add New Task (Priority: P3)

**Goal**: Authenticated users can create new tasks

**Independent Test**: Login, create a task with title and description, verify it appears in the list

### Implementation for User Story 3

- [X] T051 [US3] Add create_task method to TaskService at `backend/src/services/task_service.py` (update)
- [X] T052 [US3] Create POST /api/{user_id}/tasks endpoint at `backend/src/api/routes/tasks.py` (update)
- [X] T053 [US3] Create task form component with validation at `frontend/src/components/tasks/task-form.tsx`
- [X] T054 [US3] Add create task functionality to dashboard page at `frontend/src/app/dashboard/page.tsx` (update)
- [X] T055 [US3] Add API client method for createTask at `frontend/src/lib/api-client.ts` (update)

**Checkpoint**: User Story 3 complete - users can create new tasks

---

## Phase 6: User Story 4 - Update Existing Task (Priority: P4)

**Goal**: Authenticated users can edit their task title and description

**Independent Test**: Login, edit an existing task, verify changes persist

### Implementation for User Story 4

- [X] T056 [US4] Add update_task method to TaskService at `backend/src/services/task_service.py` (update)
- [X] T057 [US4] Add get_task method to TaskService at `backend/src/services/task_service.py` (update)
- [X] T058 [US4] Create GET /api/{user_id}/tasks/{id} endpoint at `backend/src/api/routes/tasks.py` (update)
- [X] T059 [US4] Create PUT /api/{user_id}/tasks/{id} endpoint at `backend/src/api/routes/tasks.py` (update)
- [X] T060 [US4] Add edit mode to task item component at `frontend/src/components/tasks/task-item.tsx` (update)
- [X] T061 [US4] Add API client methods for getTask and updateTask at `frontend/src/lib/api-client.ts` (update)

**Checkpoint**: User Story 4 complete - users can update their tasks

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Authenticated users can delete their tasks

**Independent Test**: Login, delete a task, verify it no longer appears in the list

### Implementation for User Story 5

- [X] T062 [US5] Add delete_task method to TaskService at `backend/src/services/task_service.py` (update)
- [X] T063 [US5] Create DELETE /api/{user_id}/tasks/{id} endpoint at `backend/src/api/routes/tasks.py` (update)
- [X] T064 [US5] Add delete button and confirmation to task item at `frontend/src/components/tasks/task-item.tsx` (update)
- [X] T065 [US5] Add API client method for deleteTask at `frontend/src/lib/api-client.ts` (update)

**Checkpoint**: User Story 5 complete - users can delete their tasks

---

## Phase 8: User Story 6 - Toggle Task Completion (Priority: P6)

**Goal**: Authenticated users can mark tasks as complete or incomplete

**Independent Test**: Login, toggle a task's completion status, verify visual change and persistence

### Implementation for User Story 6

- [X] T066 [US6] Add toggle_complete method to TaskService at `backend/src/services/task_service.py` (update)
- [X] T067 [US6] Create PATCH /api/{user_id}/tasks/{id}/complete endpoint at `backend/src/api/routes/tasks.py` (update)
- [X] T068 [US6] Add completion toggle checkbox to task item at `frontend/src/components/tasks/task-item.tsx` (update)
- [X] T069 [US6] Add visual styling for completed vs incomplete tasks at `frontend/src/components/tasks/task-item.tsx` (update)
- [X] T070 [US6] Add API client method for toggleComplete at `frontend/src/lib/api-client.ts` (update)

**Checkpoint**: User Story 6 complete - users can toggle task completion

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements affecting multiple user stories

- [X] T071 [P] Add loading states to all async operations in frontend components
- [X] T072 [P] Add error handling and user-friendly error messages throughout frontend
- [ ] T073 [P] Add success feedback (toast notifications) for CRUD operations
- [X] T074 [P] Ensure responsive design works on mobile devices
- [X] T075 [P] Add input validation error display in forms
- [X] T076 [P] Configure CORS properly for production in `backend/src/main.py`
- [X] T077 [P] Add health check endpoint at `backend/src/main.py`
- [X] T078 Update README.md with setup and run instructions at `README.md`
- [ ] T079 Validate application against quickstart.md scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational (BLOCKS ALL USER STORIES)
    ↓
┌───────────────────────────────────────────────────┐
│ Phase 3: US1 - Authentication (P1)                │
│     ↓                                             │
│ Phase 4: US2 - View Tasks (P2) ──────────────┐   │
│     ↓                                         │   │
│ Phase 5: US3 - Add Task (P3)                  │   │
│     ↓                                         │   │
│ Phase 6: US4 - Update Task (P4)               │   │
│     ↓                                         │   │
│ Phase 7: US5 - Delete Task (P5)               │   │
│     ↓                                         │   │
│ Phase 8: US6 - Toggle Complete (P6)           │   │
└───────────────────────────────────────────────┘   │
    ↓                                               │
Phase 9: Polish (after all stories complete) ◄──────┘
```

### User Story Dependencies

- **US1 (Auth)**: Required for all other stories - MUST complete first
- **US2 (View)**: Requires US1 - dashboard needs authentication
- **US3 (Add)**: Requires US2 - need task list to show new tasks
- **US4 (Update)**: Requires US3 - need tasks to update
- **US5 (Delete)**: Requires US3 - need tasks to delete
- **US6 (Toggle)**: Requires US3 - need tasks to toggle

### Parallel Opportunities

**Phase 1 - Setup**:
```
T003, T004 (backend init) || T005, T006, T007, T008 (frontend init)
T009 || T010 || T011 (CLAUDE.md files)
```

**Phase 2 - Foundational**:
```
T014 || T015 (models)
T017 || T018 (schemas)
T025 || T026 (types)
T030 || T031 || T032 (UI components)
```

**Phase 9 - Polish**:
```
T071 || T072 || T073 || T074 || T075 || T076 || T077 (all independent)
```

---

## Implementation Strategy

### MVP First (User Stories 1-3)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL)
3. Complete Phase 3: US1 - Authentication
4. Complete Phase 4: US2 - View Tasks
5. Complete Phase 5: US3 - Add Task
6. **STOP and VALIDATE**: Test registration, login, view, and add
7. Deploy/demo MVP if ready

### Full Feature Set

Continue after MVP:
8. Complete Phase 6: US4 - Update Task
9. Complete Phase 7: US5 - Delete Task
10. Complete Phase 8: US6 - Toggle Complete
11. Complete Phase 9: Polish
12. Final validation against quickstart.md

---

## Task Summary

| Phase | Description | Task Count |
|-------|-------------|------------|
| Phase 1 | Setup | 11 |
| Phase 2 | Foundational | 22 |
| Phase 3 | US1 - Auth | 8 |
| Phase 4 | US2 - View | 9 |
| Phase 5 | US3 - Add | 5 |
| Phase 6 | US4 - Update | 6 |
| Phase 7 | US5 - Delete | 4 |
| Phase 8 | US6 - Toggle | 5 |
| Phase 9 | Polish | 9 |
| **Total** | | **79** |

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story can be validated independently after completion
- Commit after each task or logical group
- MVP scope: Complete through Phase 5 (US1-US3)
- All file paths are relative to repository root
