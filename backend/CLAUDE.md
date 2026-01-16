# Backend CLAUDE.md

This file provides context-specific instructions and guidelines for working on the backend component of the todo application.

## Task Context

**Surface:** Backend development focusing on FastAPI, database interactions, authentication, and API endpoints.

## Technologies

- **Framework:** FastAPI with Python 3.13+
- **Database:** Neon Serverless PostgreSQL with SQLModel ORM
- **Authentication:** Better Auth with JWT token integration
- **Package Management:** UV for Python dependencies

## Key Directories

- `models/` - SQLModel database models
- `api/` - API routes for authentication and todo operations
- `core/` - Core business logic and services
- `database/` - Database configuration and session management
- `dependencies/` - FastAPI dependencies (e.g., authentication)
- `schemas/` - Pydantic schemas for request/response validation

## Development Guidelines

1. Follow clean architecture principles with domain logic separated from I/O concerns
2. Use dependency injection for all external concerns
3. Implement proper error handling with user-friendly messages
4. Apply JWT token validation for all protected API routes
5. Use SQLModel ORM for all database interactions to prevent SQL injection
6. Maintain separation between business logic (services) and API layer (routes)

## MCP Server Usage

- Use context7 MCP server for Python/FastAPI documentation
- Use appropriate MCP servers for database and authentication documentation
- Prioritize official documentation over internal knowledge

## Testing

- Write tests using pytest
- Follow TDD principles (Red-Green-Refactor)
- Ensure proper test coverage for business logic
- Test authentication and authorization flows thoroughly