# Research: Phase II Full-Stack Todo Web Application

**Feature**: 001-fullstack-todo-app
**Date**: 2025-12-25
**Status**: Complete

## Overview

This document captures research findings and technical decisions for implementing the Phase II full-stack todo application.

---

## 1. Better Auth Integration with Next.js

### Decision
Use Better Auth with email/password authentication, configured to issue JWTs for API authentication.

### Rationale
- Better Auth is specified in the constitution (Article III.1)
- Provides built-in session management for Next.js
- Can issue JWTs that FastAPI can verify independently
- Supports the stateless backend requirement

### Implementation Approach
1. Install `better-auth` package in frontend
2. Configure Better Auth with `BETTER_AUTH_SECRET` environment variable
3. Set up authentication routes at `/api/auth/*`
4. Create auth context provider for session management
5. Configure JWT token generation for API calls

### Alternatives Considered
- **NextAuth.js**: More complex, overkill for email/password only
- **Custom JWT**: More work, less secure without proper implementation

---

## 2. FastAPI JWT Verification

### Decision
Use `python-jose` library with HS256 algorithm for JWT verification.

### Rationale
- FastAPI has excellent support for dependency injection
- `python-jose` is lightweight and well-maintained
- HS256 symmetric encryption works with shared secret
- Stateless verification per constitution requirement

### Implementation Approach
1. Create `auth/jwt.py` module with verification function
2. Extract token from `Authorization: Bearer <token>` header
3. Verify signature using `BETTER_AUTH_SECRET`
4. Extract `user_id` from token payload
5. Use FastAPI dependency injection for route protection

### Token Structure (Expected from Better Auth)
```json
{
  "sub": "user_id",
  "email": "user@example.com",
  "iat": 1703500000,
  "exp": 1703586400
}
```

---

## 3. SQLModel with Neon PostgreSQL

### Decision
Use SQLModel for ORM with async support connecting to Neon PostgreSQL.

### Rationale
- SQLModel is specified in constitution (Article V.2)
- Combines Pydantic and SQLAlchemy
- Type-safe database models
- Async support for better performance

### Implementation Approach
1. Use `sqlmodel` with `asyncpg` driver
2. Connection string from `DATABASE_URL` environment variable
3. Create async session factory
4. Use dependency injection for database sessions
5. Implement repository pattern in services layer

### Connection Configuration
```python
DATABASE_URL = "postgresql+asyncpg://user:pass@host/db?sslmode=require"
```

---

## 4. API Design Patterns

### Decision
Follow REST conventions with user-scoped routes as defined in constitution.

### Rationale
- Constitution defines exact endpoint structure (Article IV.1)
- User ID in URL enables clear ownership semantics
- Stateless design supports horizontal scaling

### Endpoint Structure
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/{user_id}/tasks` | List all tasks |
| POST | `/api/{user_id}/tasks` | Create task |
| GET | `/api/{user_id}/tasks/{id}` | Get single task |
| PUT | `/api/{user_id}/tasks/{id}` | Update task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle completion |

### Security Middleware
- Verify JWT on every request
- Compare URL `user_id` with token `sub` claim
- Return 403 if mismatch

---

## 5. Frontend Architecture

### Decision
Use Next.js App Router with server components where possible, client components for interactivity.

### Rationale
- App Router is the modern Next.js standard
- Server components reduce client bundle size
- Better Auth integrates well with App Router
- Follows React best practices

### Component Strategy
- **Server Components**: Layout, initial page render
- **Client Components**: Forms, task interactions, auth state
- **API Client**: Centralized fetch wrapper with token injection

### State Management
- Use React Context for auth state
- Local state for form handling
- Server state via fetch (no Redux needed for this scope)

---

## 6. Environment Variables

### Decision
Use separate `.env` files for frontend and backend with shared secrets.

### Required Variables

**Backend (.env)**
```
DATABASE_URL=postgresql+asyncpg://...
BETTER_AUTH_SECRET=shared-secret-here
CORS_ORIGINS=http://localhost:3000
```

**Frontend (.env.local)**
```
NEXT_PUBLIC_API_URL=http://localhost:8000
BETTER_AUTH_SECRET=shared-secret-here
```

---

## 7. Error Handling Strategy

### Decision
Implement consistent error responses across frontend and backend.

### Backend Error Format
```json
{
  "detail": "Error message",
  "code": "ERROR_CODE",
  "status": 400
}
```

### HTTP Status Code Usage
- 200: Successful GET, PUT, PATCH, DELETE
- 201: Successful POST (created)
- 400: Validation error
- 401: Missing or invalid token
- 403: User ID mismatch (forbidden)
- 404: Resource not found
- 500: Server error

### Frontend Error Display
- Toast notifications for transient errors
- Inline form errors for validation
- Full-page error for critical failures

---

## 8. CORS Configuration

### Decision
Configure CORS on FastAPI to allow frontend origin only.

### Implementation
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Summary

All technical decisions align with constitution requirements. No NEEDS CLARIFICATION items remain. The implementation can proceed to data modeling and contract definition.
