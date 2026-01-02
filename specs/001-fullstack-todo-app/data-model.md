# Data Model: Phase II Full-Stack Todo Web Application

**Feature**: 001-fullstack-todo-app
**Date**: 2025-12-25
**Status**: Complete

## Overview

This document defines the data entities, their attributes, relationships, and validation rules for the Phase II todo application.

---

## Entity Relationship Diagram

```
┌─────────────────┐       ┌─────────────────┐
│      User       │       │      Task       │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │──────<│ id (PK)         │
│ email (unique)  │       │ user_id (FK)    │
│ password_hash   │       │ title           │
│ created_at      │       │ description     │
│ updated_at      │       │ is_completed    │
└─────────────────┘       │ created_at      │
                          │ updated_at      │
                          └─────────────────┘
```

**Relationship**: One User has many Tasks (1:N)

---

## Entity: User

Represents a registered user of the system.

### Attributes

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | UUID | Primary Key | Unique identifier |
| email | String(255) | Unique, Not Null | User's email address |
| password_hash | String(255) | Not Null | Bcrypt hashed password |
| created_at | DateTime | Not Null, Default: now() | Account creation timestamp |
| updated_at | DateTime | Not Null, Default: now() | Last update timestamp |

### Validation Rules

- **email**: Must be valid email format, max 255 characters
- **password** (pre-hash): Minimum 8 characters

### Indexes

- Primary: `id`
- Unique: `email`

### SQLModel Definition

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(max_length=255, unique=True, index=True)
    password_hash: str = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## Entity: Task

Represents a todo item belonging to a user.

### Attributes

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | UUID | Primary Key | Unique identifier |
| user_id | UUID | Foreign Key → User.id, Not Null | Owner reference |
| title | String(100) | Not Null | Task title |
| description | String(500) | Nullable | Task description |
| is_completed | Boolean | Not Null, Default: false | Completion status |
| created_at | DateTime | Not Null, Default: now() | Creation timestamp |
| updated_at | DateTime | Not Null, Default: now() | Last update timestamp |

### Validation Rules

- **title**: Required, 1-100 characters
- **description**: Optional, max 500 characters
- **is_completed**: Boolean, defaults to false

### Indexes

- Primary: `id`
- Index: `user_id` (for efficient user task queries)
- Composite: `(user_id, created_at)` (for sorted task lists)

### SQLModel Definition

```python
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="users.id", index=True)
    title: str = Field(max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    is_completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
```

---

## Database Schema (PostgreSQL DDL)

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);

-- Tasks table
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500),
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_user_created ON tasks(user_id, created_at DESC);

-- Updated_at trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply trigger to both tables
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_tasks_updated_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

---

## Pydantic Schemas (API Layer)

### Task Schemas

```python
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from typing import Optional

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    description: Optional[str]
    is_completed: bool
    created_at: datetime
    updated_at: datetime

class TaskList(BaseModel):
    tasks: list[TaskResponse]
    count: int
```

### User Schemas

```python
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: UUID
    email: str
    created_at: datetime
```

---

## State Transitions

### Task Completion State

```
                  toggle_complete()
    ┌─────────────────────────────────────┐
    │                                     │
    ▼                                     │
┌─────────┐    toggle_complete()    ┌─────────┐
│ Pending │ ──────────────────────> │Complete │
│  (F)    │ <────────────────────── │  (T)    │
└─────────┘                         └─────────┘
```

- **Pending** (`is_completed = false`): Default state for new tasks
- **Complete** (`is_completed = true`): Task marked as done
- **Transition**: Toggle between states via PATCH endpoint

---

## Data Integrity Rules

1. **Cascade Delete**: When a user is deleted, all their tasks are deleted
2. **Ownership**: Tasks always have a valid user_id reference
3. **Timestamps**: Both created_at and updated_at are automatically managed
4. **UUID Generation**: IDs are generated by the database for consistency

---

## Query Patterns

### Get User's Tasks (sorted by creation date, newest first)

```sql
SELECT * FROM tasks
WHERE user_id = :user_id
ORDER BY created_at DESC;
```

### Verify Task Ownership

```sql
SELECT EXISTS(
    SELECT 1 FROM tasks
    WHERE id = :task_id AND user_id = :user_id
);
```

### Count User's Tasks

```sql
SELECT COUNT(*) FROM tasks WHERE user_id = :user_id;
```
