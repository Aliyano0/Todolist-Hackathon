# Claude Code Rules for Frontend Development

You are an expert AI assistant specializing in frontend development for the Todo application.

## Task Context

**Surface**: Frontend development for Next.js Todo application
**Success Metric**: Features match spec, pass tests, follow architecture

## Core Guarantees

### 1. Frontend Development Standards:
- Use Next.js 16.1+ with App Router
- Implement responsive UI with Tailwind CSS
- Follow accessibility standards (WCAG 2.1 AA)
- Use TypeScript for type safety
- Implement proper error handling

### 2. Component Architecture:
- Organize components by feature (todo, theme, navigation)
- Use Shadcn/UI components where appropriate
- Follow Next.js best practices for Client vs Server components
- Implement proper state management with React hooks

### 3. API Integration:
- Integrate with backend API using REST endpoints
- Implement optimistic updates for better UX
- Handle loading and error states properly
- Follow the API contracts defined in specs/011-frontend-rebuild/contracts/

### 4. Theming & UI:
- Implement light/dark theme support
- Use ThemeProvider for context-based theming
- Ensure responsive design across mobile/tablet/desktop
- Add subtle animations for improved UX

## Better Auth Integration (018-better-auth-jwt)

### Authentication Configuration Pattern
```typescript
// lib/auth.ts
import { betterAuth } from "better-auth";
import { nextCookies } from "better-auth/next-js";

export const auth = betterAuth({
  secret: process.env.BETTER_AUTH_SECRET!,
  baseURL: process.env.BETTER_AUTH_URL!,
  database: {
    // Better Auth connects to backend API
    provider: "custom",
  },
  plugins: [nextCookies()],
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: false, // Phase 3 feature
  },
});
```

### AuthProvider Pattern
```typescript
// providers/AuthProvider.tsx
"use client";
import { SessionProvider } from "better-auth/react";

export function AuthProvider({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}
```

### Protected Routes Pattern
```typescript
// app/middleware.ts
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  const token = request.cookies.get("better-auth.session_token");

  if (!token && request.nextUrl.pathname.startsWith("/dashboard")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/dashboard/:path*"],
};
```

### useAuth Hook Pattern
```typescript
// hooks/useAuth.ts
"use client";
import { useSession, signIn, signOut } from "better-auth/react";

export function useAuth() {
  const { data: session, isPending } = useSession();

  return {
    user: session?.user,
    isAuthenticated: !!session,
    isLoading: isPending,
    signIn,
    signOut,
  };
}
```

### API Client with Credentials Pattern
```typescript
// lib/api.ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function apiRequest<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    credentials: "include", // Send cookies with request
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
  });

  if (response.status === 401) {
    // Redirect to login on unauthorized
    window.location.href = "/login";
    throw new Error("Unauthorized");
  }

  if (response.status === 403) {
    throw new Error("Access denied");
  }

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Request failed");
  }

  return response.json();
}
```

### Password Validation Pattern
```typescript
// lib/validation.ts
export function validatePassword(password: string): {
  isValid: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (password.length < 8) {
    errors.push("Password must be at least 8 characters");
  }
  if (!/[A-Z]/.test(password)) {
    errors.push("Password must contain at least one uppercase letter");
  }
  if (!/[a-z]/.test(password)) {
    errors.push("Password must contain at least one lowercase letter");
  }
  if (!/[0-9]/.test(password)) {
    errors.push("Password must contain at least one number");
  }
  if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    errors.push("Password must contain at least one special character");
  }

  return {
    isValid: errors.length === 0,
    errors,
  };
}
```

## Active Technologies
- Next.js 16.1 with App Router
- React 19.2.3
- TypeScript 5.x
- Tailwind CSS with Shadcn/UI
- Radix UI primitives
- Better Auth for authentication
- REST API integration with credentials support
- Priority and category fields support in frontend types (016-backend-db-fix)

## Recent Changes
- 018-better-auth-jwt: Implementing Better Auth integration with JWT tokens, protected routes, and password validation
- 016-backend-db-fix: Priority and category fields support in frontend types