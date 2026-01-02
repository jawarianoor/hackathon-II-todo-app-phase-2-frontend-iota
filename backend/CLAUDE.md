# Backend CLAUDE.md - FastAPI Guidelines

## Purpose

This document provides AI assistant guidelines specific to the FastAPI backend of the Phase II Todo App.

## Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **ORM**: SQLModel
- **Database**: Neon PostgreSQL (async with asyncpg)
- **Authentication**: JWT verification (tokens from Better Auth)

## Architecture

```
backend/src/
├── main.py           # FastAPI app entry, CORS, routes
├── config.py         # Environment configuration
├── database.py       # Async database connection
├── models/           # SQLModel database models
├── schemas/          # Pydantic request/response schemas
├── api/
│   ├── deps.py       # Dependency injection (auth, db)
│   └── routes/       # API route handlers
├── services/         # Business logic layer
└── auth/             # JWT verification
```

## Code Patterns

### Route Handler Pattern
```python
@router.get("/{user_id}/tasks")
async def list_tasks(
    user_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> TaskList:
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return await task_service.get_user_tasks(db, user_id)
```

### Service Layer Pattern
```python
async def get_user_tasks(db: AsyncSession, user_id: UUID) -> list[Task]:
    statement = select(Task).where(Task.user_id == user_id)
    result = await db.execute(statement)
    return result.scalars().all()
```

## Rules

1. Always verify user_id in URL matches authenticated user
2. Use dependency injection for database sessions
3. Return proper HTTP status codes (401, 403, 404)
4. Validate input with Pydantic schemas
5. Keep business logic in services, not routes
6. Use async/await for all database operations

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `BETTER_AUTH_SECRET`: Shared JWT secret
- `CORS_ORIGINS`: Allowed frontend origins
