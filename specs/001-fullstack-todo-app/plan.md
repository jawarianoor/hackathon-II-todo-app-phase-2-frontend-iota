# Implementation Plan: Phase II Full-Stack Todo Web Application

**Branch**: `001-fullstack-todo-app` | **Date**: 2025-12-25 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-fullstack-todo-app/spec.md`

## Summary

Transform the Phase I CLI Todo application into a multi-user, authenticated full-stack web application. The system uses a Next.js frontend with Better Auth for authentication, a FastAPI backend for RESTful API services, and Neon PostgreSQL for persistent storage. All task operations are user-scoped with JWT-based authentication ensuring complete data isolation between users.

## Technical Context

**Language/Version**: Python 3.11+ (backend), TypeScript 5.x (frontend)
**Primary Dependencies**: FastAPI, SQLModel, Better Auth, Next.js 16+
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest (backend), Jest/Vitest (frontend)
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge - last 2 versions)
**Project Type**: Web application (frontend + backend monorepo)
**Performance Goals**: Task list load < 2 seconds, 100 concurrent users
**Constraints**: < 200ms API response time, JWT-based stateless auth
**Scale/Scope**: 100 concurrent users, ~1000 tasks per user max

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| Technology Stack Compliance | PASS | Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL per Article V |
| Authentication Model | PASS | Better Auth + JWT per Article III |
| API Contract | PASS | REST endpoints match Article IV.1 definitions |
| Monorepo Structure | PASS | frontend/ + backend/ structure per Article VI |
| Data Isolation | PASS | User-scoped endpoints with ownership verification |
| Stateless Backend | PASS | JWT-based auth, no server sessions |
| Secure-by-Default | PASS | All endpoints require auth per Article VIII.4 |

**Gate Result**: PASS - All constitution requirements satisfied

## Project Structure

### Documentation (this feature)

```text
specs/001-fullstack-todo-app/
├── plan.md              # This file
├── spec.md              # Feature specification
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── openapi.yaml     # API contract
├── checklists/          # Validation checklists
│   └── requirements.md
└── tasks.md             # Phase 2 output (/sp.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment configuration
│   ├── database.py          # Database connection
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User SQLModel
│   │   └── task.py          # Task SQLModel
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py          # Pydantic schemas for user
│   │   └── task.py          # Pydantic schemas for task
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py          # Dependency injection
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── tasks.py     # Task CRUD endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Task business logic
│   └── auth/
│       ├── __init__.py
│       └── jwt.py           # JWT verification
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_tasks.py
│   └── test_auth.py
├── pyproject.toml
├── requirements.txt
└── CLAUDE.md

frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx       # Root layout
│   │   ├── page.tsx         # Landing/login page
│   │   ├── auth/
│   │   │   ├── login/
│   │   │   │   └── page.tsx
│   │   │   └── register/
│   │   │       └── page.tsx
│   │   └── dashboard/
│   │       ├── layout.tsx   # Protected layout
│   │       └── page.tsx     # Task list page
│   ├── components/
│   │   ├── ui/              # Reusable UI components
│   │   │   ├── button.tsx
│   │   │   ├── input.tsx
│   │   │   └── card.tsx
│   │   ├── auth/
│   │   │   ├── login-form.tsx
│   │   │   └── register-form.tsx
│   │   └── tasks/
│   │       ├── task-list.tsx
│   │       ├── task-item.tsx
│   │       ├── task-form.tsx
│   │       └── empty-state.tsx
│   ├── lib/
│   │   ├── api-client.ts    # Centralized API client
│   │   ├── auth.ts          # Better Auth configuration
│   │   └── utils.ts         # Utility functions
│   └── types/
│       ├── task.ts          # Task type definitions
│       └── user.ts          # User type definitions
├── tests/
│   └── components/
├── package.json
├── tsconfig.json
├── next.config.js
├── tailwind.config.js
└── CLAUDE.md
```

**Structure Decision**: Web application structure with separate frontend/ and backend/ directories per Constitution Article VI.1. This enables independent deployment and clear separation of concerns.

## Complexity Tracking

> No complexity violations - design follows constitution requirements.

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| Monorepo | frontend + backend | Required by constitution |
| Auth | Better Auth + JWT | Required by constitution |
| ORM | SQLModel | Required by constitution |
| Database | Neon PostgreSQL | Required by constitution |
