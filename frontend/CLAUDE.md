# Frontend CLAUDE.md - Next.js Guidelines

## Purpose

This document provides AI assistant guidelines specific to the Next.js frontend of the Phase II Todo App.

## Technology Stack

- **Framework**: Next.js 16+ (App Router)
- **Language**: TypeScript (strict mode)
- **Authentication**: Better Auth
- **Styling**: Tailwind CSS
- **State**: React Context + local state

## Architecture

```
frontend/src/
├── app/                    # Next.js App Router
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Landing page
│   ├── auth/               # Auth pages (login, register)
│   ├── dashboard/          # Protected pages
│   └── api/auth/           # Better Auth routes
├── components/
│   ├── ui/                 # Reusable UI components
│   ├── auth/               # Auth forms
│   └── tasks/              # Task components
├── lib/
│   ├── api-client.ts       # Centralized API client
│   ├── auth.ts             # Better Auth config
│   └── utils.ts            # Utility functions
└── types/                  # TypeScript type definitions
```

## Code Patterns

### Server Component (default)
```tsx
export default async function DashboardPage() {
  // Server-side data fetching
  return <TaskList />
}
```

### Client Component
```tsx
'use client'

export function TaskForm({ onSubmit }: Props) {
  const [title, setTitle] = useState('')
  // Interactive logic
}
```

### API Client Usage
```tsx
import { apiClient } from '@/lib/api-client'

const tasks = await apiClient.getTasks(userId)
```

## Rules

1. Use Server Components by default, Client Components only when needed
2. All API calls go through centralized api-client.ts
3. Protected routes must check auth in layout.tsx
4. Use TypeScript strict mode - no `any` types
5. Handle loading and error states in UI
6. Mobile-first responsive design with Tailwind

## Environment Variables

- `NEXT_PUBLIC_API_URL`: Backend API URL
- `BETTER_AUTH_SECRET`: Shared JWT secret
- `BETTER_AUTH_URL`: Better Auth URL (usually same as app)
