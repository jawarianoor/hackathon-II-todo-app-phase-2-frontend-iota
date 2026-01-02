# Todo App Constitution

## Phase II: Full-Stack Web Application

**Version:** 2.0.0
**Effective Date:** 2025-12-25
**Status:** Active
**Phase:** II of N

---

## Preamble

This Constitution serves as the supreme governing document for Phase II of the project titled **"The Evolution of Todo: From CLI to Distributed Cloud-Native AI Systems."**

Phase II transitions the system from a single-user, in-memory CLI application into a **multi-user, authenticated, full-stack web application with persistent storage**. This document establishes the non-negotiable rules, constraints, architecture, security model, and development workflow that all contributors, specifications, and generated code MUST adhere to without exception.

Manual boilerplate coding is strictly prohibited. All code MUST be generated via **Claude Code** using **Spec-Kit Plus specifications**.

---

## Article I: Project Identity

### Section 1.1 – Project Title

**Todo App – Phase II: Full-Stack Web Application**

### Section 1.2 – Project Context

This project is part of a multi-phase journey titled "The Evolution of Todo: From CLI to Distributed Cloud-Native AI Systems." Students act as **Product Architects**, using **AI-first, spec-driven development** to evolve a simple console app into a modern, scalable system.

### Section 1.3 – Phase II Objective

Transform the Phase I console application into a **modern, multi-user full-stack web application** that:

- Uses a RESTful API backend
- Has a responsive frontend UI
- Persists data in a cloud-hosted database
- Enforces strict user authentication and data isolation
- Is structured as a **Spec-Kit–compatible monorepo**

---

## Article II: Core Functional Requirements

The application MUST implement all Phase I features in a web context. All functionality MUST be scoped **per authenticated user**.

### Section 2.1 – Add Task

- Create a new todo item with a title and description
- Assign a unique identifier to each task upon creation
- Associate the task with the authenticated user

### Section 2.2 – View Task List

- Display all tasks belonging to the authenticated user
- Each entry SHALL include: ID, title, description, and completion status
- Tasks from other users MUST NOT be visible

### Section 2.3 – Update Task

- Modify the title and/or description of an existing task
- Identify the target task by its unique ID
- Operation MUST verify task ownership before modification

### Section 2.4 – Delete Task

- Remove a task permanently from persistent storage
- Identify the target task by its unique ID
- Operation MUST verify task ownership before deletion

### Section 2.5 – Mark as Complete / Incomplete

- Toggle the completion status of a task
- Identify the target task by its unique ID
- Operation MUST verify task ownership before status change

---

## Article III: Authentication & Security Model

Authentication is mandatory and MUST be enforced on every API request.

### Section 3.1 – Authentication Provider

**Better Auth** SHALL be used for authentication on the Next.js frontend.

### Section 3.2 – Authentication Mechanism

**JWT (JSON Web Tokens)** SHALL be used for API authentication.

### Section 3.3 – Required Security Behavior

The following security behaviors are MANDATORY:

1. Users authenticate via Better Auth on the frontend
2. Better Auth issues a signed JWT upon successful authentication
3. JWT MUST be attached to every API request via header:
   ```
   Authorization: Bearer <token>
   ```
4. FastAPI backend MUST:
   - Verify JWT signature using the shared secret
   - Extract user identity from the token
   - Reject unauthenticated requests with HTTP 401
   - Enforce task ownership on every operation

### Section 3.4 – Shared Secret Configuration

Both frontend and backend MUST use the same secret for JWT signing/verification. The secret SHALL be provided via environment variable:

```
BETTER_AUTH_SECRET
```

### Section 3.5 – Data Isolation

- Users MUST only access their own tasks
- API endpoints MUST verify that the authenticated user owns the requested resource
- Cross-user data access is PROHIBITED

---

## Article IV: REST API Contract

The backend MUST expose RESTful endpoints under `/api`.

### Section 4.1 – Endpoint Definitions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/{user_id}/tasks` | Retrieve all tasks for user |
| POST | `/api/{user_id}/tasks` | Create a new task |
| GET | `/api/{user_id}/tasks/{id}` | Retrieve a specific task |
| PUT | `/api/{user_id}/tasks/{id}` | Update an existing task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete a task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle task completion status |

### Section 4.2 – API Rules

The following rules are NON-NEGOTIABLE:

1. JWT authentication is REQUIRED for ALL endpoints
2. The `user_id` in the URL MUST match the authenticated user's ID
3. Responses MUST only include the authenticated user's data
4. Errors MUST follow proper HTTP status codes:
   - 200: Success
   - 201: Created
   - 400: Bad Request
   - 401: Unauthorized
   - 403: Forbidden (user_id mismatch)
   - 404: Not Found
   - 500: Server Error

### Section 4.3 – Request/Response Format

- All request and response bodies MUST use JSON format
- Content-Type header MUST be `application/json`

---

## Article V: Technology Stack

The following technology choices are **NON-NEGOTIABLE**.

### Section 5.1 – Frontend

| Component | Technology | Version/Notes |
|-----------|------------|---------------|
| Framework | Next.js | 16+ with App Router |
| Language | TypeScript | Strict mode |
| Authentication | Better Auth | JWT-based |
| UI | Responsive Design | Mobile-first |
| API Client | Centralized | Single API client module |

### Section 5.2 – Backend

| Component | Technology | Version/Notes |
|-----------|------------|---------------|
| Framework | FastAPI | Latest stable |
| Language | Python | 3.11+ |
| ORM | SQLModel | For database operations |
| Architecture | RESTful | Stateless |
| Auth Verification | JWT | Stateless verification |

### Section 5.3 – Database

| Component | Technology | Notes |
|-----------|------------|-------|
| Provider | Neon | Serverless PostgreSQL |
| Persistence | Required | All data must be persistent |
| Schema | Spec-defined | Via specifications |

### Section 5.4 – Development Tools

| Tool | Purpose |
|------|---------|
| Claude Code | AI code generation |
| Spec-Kit Plus | Specification management |

---

## Article VI: Monorepo & Project Structure

The project MUST be organized as a **Spec-Kit–compatible monorepo**.

### Section 6.1 – Required Structure

```
/
├── .spec-kit/
│   └── config.yaml           # Spec-Kit configuration
├── specs/
│   ├── overview/             # High-level specifications
│   ├── features/             # Feature specifications
│   ├── api/                  # API contract specifications
│   ├── database/             # Database schema specifications
│   └── ui/                   # UI/UX specifications
├── frontend/                 # Next.js application
│   ├── src/
│   │   ├── app/              # App Router pages
│   │   ├── components/       # React components
│   │   ├── lib/              # Utilities and API client
│   │   └── types/            # TypeScript types
│   ├── CLAUDE.md             # Frontend-specific AI guidelines
│   └── package.json
├── backend/                  # FastAPI application
│   ├── src/
│   │   ├── api/              # API routes
│   │   ├── models/           # SQLModel models
│   │   ├── services/         # Business logic
│   │   └── auth/             # JWT verification
│   ├── CLAUDE.md             # Backend-specific AI guidelines
│   └── pyproject.toml
├── constitution.md           # This governing document
├── CLAUDE.md                 # Root-level AI guidelines
└── README.md                 # Setup and run instructions
```

### Section 6.2 – Specification References

Specifications are the **single source of truth** and MUST be referenced using:
```
@specs/<category>/<file>.md
```

### Section 6.3 – CLAUDE.md Requirements

The following CLAUDE.md files are MANDATORY:

| Location | Purpose |
|----------|---------|
| `/CLAUDE.md` | Root-level guidelines for entire project |
| `/frontend/CLAUDE.md` | Frontend-specific development guidelines |
| `/backend/CLAUDE.md` | Backend-specific development guidelines |

---

## Article VII: Development Workflow

All development MUST follow this sequence. Deviation is PROHIBITED.

### Section 7.1 – Workflow Steps

1. **Write or update specifications** – Define requirements in `/specs`
2. **Generate a plan from the spec** – Use `/sp.plan` command
3. **Break the plan into tasks** – Use `/sp.tasks` command
4. **Implement exclusively via Claude Code** – Use `/sp.implement` command
5. **Iterate by modifying specs, not manual code** – Specs drive all changes

### Section 7.2 – Claude Code Requirements

Before generating any code, Claude Code MUST read:

1. `constitution.md` – This governing document
2. Relevant spec files from `/specs`
3. Applicable `CLAUDE.md` instructions

### Section 7.3 – Prohibited Actions

The following actions are EXPLICITLY PROHIBITED:

1. Manual boilerplate coding
2. Code generation without specification basis
3. Deviating from the defined architecture
4. Skipping workflow steps
5. Direct database manipulation outside of migrations

---

## Article VIII: Design & Engineering Principles

### Section 8.1 – Clean Architecture

The system MUST implement clean architecture principles:
- Clear separation between layers
- Dependencies point inward (UI → Services → Data)
- Business logic independent of frameworks

### Section 8.2 – Separation of Concerns

- Frontend handles UI and user interaction only
- Backend handles business logic and data access
- Database handles data persistence only
- No business logic in frontend components

### Section 8.3 – Stateless Backend Design

- Backend MUST be stateless
- No server-side sessions
- All state conveyed via JWT tokens
- Horizontal scalability by design

### Section 8.4 – Secure-by-Default

- All endpoints require authentication by default
- Input validation on all API endpoints
- SQL injection prevention via ORM
- XSS prevention in frontend
- CORS properly configured

### Section 8.5 – Maintainability & Clarity

- Code must be self-documenting
- Favor readability over cleverness
- Consistent naming conventions
- Proper error handling and logging

### Section 8.6 – Deterministic & Testable

- No randomness in application behavior (except for ID generation)
- All operations must produce predictable results
- Code must be testable in isolation

---

## Article IX: Phase II Deliverables

Phase II SHALL be considered complete upon delivery of:

### Section 9.1 – Functional Deliverables

1. Fully working authenticated web application
2. All five core features implemented:
   - Add Task
   - View Task List
   - Update Task
   - Delete Task
   - Mark Task as Complete / Incomplete
3. Persistent task storage in Neon PostgreSQL
4. JWT-secured REST API
5. Responsive frontend UI

### Section 9.2 – Repository Deliverables

A GitHub repository containing:

| Deliverable | Description |
|-------------|-------------|
| `constitution.md` | This governing document |
| `/specs` | Complete specification history |
| `/frontend` | Next.js application code |
| `/backend` | FastAPI application code |
| `/CLAUDE.md` files | AI guidelines (root, frontend, backend) |
| `README.md` | Setup and run instructions |

---

## Article X: Governance

### Section 10.1 – Constitutional Authority

This Constitution holds supreme authority over all project decisions within Phase II. No specification, code, or process may contradict its provisions.

### Section 10.2 – Amendment Process

Amendments to this Constitution require:

1. Formal written proposal with rationale
2. Impact assessment on existing code
3. Version increment following semantic versioning:
   - MAJOR: Backward incompatible changes
   - MINOR: New sections or materially expanded guidance
   - PATCH: Clarifications, wording, typo fixes
4. Date update in document header

### Section 10.3 – Interpretation

In cases of ambiguity, interpretation SHALL favor:

1. Security over convenience
2. Specification compliance over expedience
3. Simplicity over complexity
4. User data isolation over feature richness

### Section 10.4 – Compliance Review

All code reviews MUST verify:

1. Specification traceability
2. Authentication enforcement
3. User data isolation
4. Architecture adherence
5. Technology stack compliance

---

## Signatures

**Ratified:** 2025-12-25
**Authority:** Product Architect
**Phase:** II of N

---

*This Constitution governs Phase II. It supersedes the Phase I constitution for all Phase II development. Subsequent phases shall establish their own constitutional documents, building upon the foundations established herein.*
