# CLAUDE.md - AI Assistant Guidelines

## Purpose

This document defines the rules and constraints for using Claude Code (AI assistant) in the development of the Todo App project.

## Phase II: Full-Stack Web Application

This project is now in **Phase II**, transitioning from a CLI application to a full-stack web application with:
- Next.js frontend with Better Auth
- FastAPI backend with JWT verification
- Neon PostgreSQL database

## Constitutional Authority

All AI-assisted development MUST comply with `constitution.md`. This document serves as supplementary guidance for AI interactions.

## Specification-Driven Development Rules

### Rule 1: Specifications are the Source of Truth
- All code generation MUST derive from approved specifications
- Changes to functionality require specification updates FIRST
- Never implement features not defined in specifications

### Rule 2: Reference Documents
Before generating code, consult these documents in order:
1. `constitution.md` - Supreme governing document
2. `specs/001-fullstack-todo-app/spec.md` - Feature specification
3. `specs/001-fullstack-todo-app/plan.md` - Implementation plan
4. `specs/001-fullstack-todo-app/tasks.md` - Task breakdown

### Rule 3: Compliance Verification
All generated code must:
- Trace back to a specification requirement
- Follow the defined architecture (Frontend → API → Service → Database)
- Use the mandated technology stack (Next.js, FastAPI, SQLModel, PostgreSQL)
- Support Python 3.11+ and TypeScript strict mode

## Project Structure

```
/
├── backend/                  # FastAPI application
│   ├── src/
│   │   ├── api/              # API routes
│   │   ├── models/           # SQLModel models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   └── auth/             # JWT verification
│   └── CLAUDE.md             # Backend-specific guidelines
├── frontend/                 # Next.js application
│   ├── src/
│   │   ├── app/              # App Router pages
│   │   ├── components/       # React components
│   │   ├── lib/              # Utilities
│   │   └── types/            # TypeScript types
│   └── CLAUDE.md             # Frontend-specific guidelines
└── specs/                    # Specifications
```

## Code Generation Principles

### DO:
- Generate clean, readable, self-documenting code
- Follow single responsibility principle
- Use type hints (Python) and strict TypeScript
- Implement proper error handling
- Follow the established project structure
- Verify user ownership on all task operations

### DO NOT:
- Add features not in specifications
- Use technologies outside the mandated stack
- Deviate from the layered architecture
- Generate random or non-deterministic behavior
- Skip input validation
- Allow cross-user data access

## Security Requirements

1. **Authentication Required**: All API endpoints require JWT authentication
2. **User Isolation**: Users can only access their own tasks
3. **Ownership Verification**: Verify task ownership on every operation
4. **Input Validation**: Validate all user input on both frontend and backend

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/{user_id}/tasks` | List user's tasks |
| POST | `/api/{user_id}/tasks` | Create task |
| GET | `/api/{user_id}/tasks/{id}` | Get task |
| PUT | `/api/{user_id}/tasks/{id}` | Update task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle complete |

## Sub-Project Guidelines

For backend-specific guidance, see: `backend/CLAUDE.md`
For frontend-specific guidance, see: `frontend/CLAUDE.md`

## Version Control

When committing AI-generated code:
- Reference the task ID in commit message
- Note specification compliance
- Mark completed tasks in tasks.md

---

*This document governs AI assistant usage for Phase II development.*
