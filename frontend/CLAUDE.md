# Frontend CLAUDE.md

This file provides context-specific instructions and guidelines for working on the frontend component of the todo application.

## Task Context

**Surface:** Frontend development focusing on Next.js, UI components, user interactions, and API integration.

## Technologies

- **Framework:** Next.js 16.1 with App Router
- **Styling:** Tailwind CSS with Shadcn UI components
- **Package Management:** npm/yarn for JavaScript dependencies
- **API Integration:** REST API calls to backend endpoints

## Key Directories

- `app/` - Next.js App Router pages and layouts
- `components/` - Reusable React components for UI elements
- `lib/` - Utility functions and API client utilities
- `providers/` - Context providers (e.g., authentication context)
- `tests/` - Frontend tests

## Development Guidelines

1. Follow Next.js best practices for App Router
2. Use Shadcn UI components for consistent UI elements
3. Implement responsive design with Tailwind CSS
4. Handle authentication state properly using context providers
5. Integrate with backend APIs using proper error handling
6. Maintain separation between presentation logic and business logic

## MCP Server Usage

- Use nextjs mcp server for Next.js-specific documentation and tooling
- Use context7 MCP server for React and JavaScript documentation
- Prioritize official documentation over internal knowledge

## Testing

- Write tests using Jest and React Testing Library
- Follow TDD principles (Red-Green-Refactor)
- Test component interactions and user flows
- Ensure accessibility considerations are met