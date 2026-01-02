# Quickstart Guide: Phase II Full-Stack Todo Web Application

**Feature**: 001-fullstack-todo-app
**Date**: 2025-12-25

## Prerequisites

- Python 3.11+
- Node.js 18+
- npm or pnpm
- Neon PostgreSQL account (or local PostgreSQL)
- Git

## Environment Setup

### 1. Clone and Navigate

```bash
cd Todo_App
git checkout 001-fullstack-todo-app
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Unix/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Backend Environment Variables

Create `backend/.env`:

```env
DATABASE_URL=postgresql+asyncpg://username:password@host/database?sslmode=require
BETTER_AUTH_SECRET=your-secure-secret-minimum-32-chars
CORS_ORIGINS=http://localhost:3000
```

### 4. Database Migration

```bash
# From backend directory
python -m src.database  # Creates tables
```

### 5. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install
# or
pnpm install
```

### 6. Frontend Environment Variables

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
BETTER_AUTH_SECRET=your-secure-secret-minimum-32-chars
BETTER_AUTH_URL=http://localhost:3000
```

**Important**: `BETTER_AUTH_SECRET` must match between frontend and backend!

## Running the Application

### Start Backend (Terminal 1)

```bash
cd backend
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/Mac

uvicorn src.main:app --reload --port 8000
```

Backend runs at: http://localhost:8000
API docs at: http://localhost:8000/docs

### Start Frontend (Terminal 2)

```bash
cd frontend
npm run dev
# or
pnpm dev
```

Frontend runs at: http://localhost:3000

## Verification Steps

### 1. Backend Health Check

```bash
curl http://localhost:8000/health
# Expected: {"status": "healthy"}
```

### 2. API Documentation

Open http://localhost:8000/docs in browser to see Swagger UI.

### 3. Frontend Access

Open http://localhost:3000 in browser:
1. You should see the login/register page
2. Register a new account
3. After login, you should be redirected to the dashboard
4. Try creating a task

## Common Issues

### Database Connection Failed

- Verify `DATABASE_URL` is correct
- Check Neon dashboard for connection string
- Ensure `?sslmode=require` is included

### CORS Errors

- Verify `CORS_ORIGINS` in backend `.env` matches frontend URL
- Restart backend after changing `.env`

### JWT Verification Failed

- Ensure `BETTER_AUTH_SECRET` is identical in both `.env` files
- Secret must be at least 32 characters

### Port Already in Use

```bash
# Find and kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Find and kill process on port 3000 (Windows)
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

## Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm test
# or
pnpm test
```

## API Quick Reference

All endpoints require `Authorization: Bearer <token>` header.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/{user_id}/tasks` | List all tasks |
| POST | `/api/{user_id}/tasks` | Create task |
| GET | `/api/{user_id}/tasks/{id}` | Get task |
| PUT | `/api/{user_id}/tasks/{id}` | Update task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle complete |

### Example: Create Task

```bash
curl -X POST http://localhost:8000/api/{user_id}/tasks \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task", "description": "Optional description"}'
```

## Project Structure

```
Todo_App/
├── backend/
│   ├── src/
│   │   ├── main.py          # FastAPI app
│   │   ├── config.py        # Settings
│   │   ├── database.py      # DB connection
│   │   ├── models/          # SQLModel models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── api/             # API routes
│   │   ├── services/        # Business logic
│   │   └── auth/            # JWT verification
│   ├── tests/
│   ├── pyproject.toml
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js pages
│   │   ├── components/      # React components
│   │   ├── lib/             # Utilities
│   │   └── types/           # TypeScript types
│   ├── package.json
│   └── .env.local
├── specs/
│   └── 001-fullstack-todo-app/
└── constitution.md
```

## Next Steps

After verifying the setup works:

1. Run `/sp.tasks` to generate implementation tasks
2. Run `/sp.implement` to execute tasks
3. Commit changes with meaningful messages
4. Push to remote repository
