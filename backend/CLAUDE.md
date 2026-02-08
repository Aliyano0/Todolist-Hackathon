# Claude Code Rules for Backend

You are an expert AI assistant specializing in backend development for the todo-list hackathon project.

## Task Context

**Surface**: You operate on the backend implementation level, providing guidance for FastAPI, SQLModel, and PostgreSQL development tasks.

**Success is measured by**:
- All backend code follows Python 3.13+ standards
- FastAPI endpoints properly implement the specified API contracts
- SQLModel ORM is used correctly for database operations
- All endpoints return appropriate HTTP status codes and JSON responses
- Error handling follows the specification with descriptive JSON messages
- Code follows clean architecture principles
- Authentication IS implemented (multi-user implementation with JWT tokens and user isolation)

## Tech Stack

- **Backend Framework**: FastAPI (Python 3.13+)
- **ORM**: SQLModel for database operations
- **Database**: Neon Serverless PostgreSQL
- **Dependencies**: uvicorn, psycopg2-binary (for Neon Serverless PostgreSQL with SQLModel ORM), python-jose[cryptography]
- **Package Manager**: UV

## Project Structure

```
backend/
├── CLAUDE.md                    # This file
├── main.py                    # FastAPI app entry point
├── models/                    # SQLModel database models
│   └── todo.py                # Todo model definition
├── api/                       # API routes
│   └── tasks.py               # Task CRUD routes
├── core/                      # Core business logic (services, utils)
│   └── services/
│       └── todo_service.py    # Todo business logic
├── database/                  # Database configuration
│   └── session.py             # Database session management
├── schemas/                   # Pydantic schemas
│   └── todo.py                # Task request/response schemas
├── dependencies/              # FastAPI dependencies
├── tests/                     # Backend tests
├── .env.example              # Environment variables template
├── pyproject.toml            # Project dependencies
├── requirements.txt          # Python dependencies
└── todo_backend.db           # SQLite database file (if needed for dev)
```

## Development Guidelines

### 1. API Contract Adherence
- Follow the exact API contracts specified in the project documentation
- Return appropriate HTTP status codes (200, 201, 204, 400, 404, 500)
- Use proper JSON response formats
- Implement validation as specified

### 2. Database Operations
- Use SQLModel ORM exclusively for database operations
- Follow proper session management patterns
- Handle database connection errors gracefully
- Implement proper error handling for database operations

### 3. Validation and Error Handling
- Validate required fields (especially task title)
- Return descriptive error messages in JSON format
- Handle edge cases as specified in the requirements

### 4. Clean Architecture
- Separate concerns between models, services, schemas, and API routes
- Keep business logic in service layer
- Use proper dependency injection patterns

### 5. Multi-User Implementation with Authentication
- Authentication IS implemented (multi-user system with JWT tokens)
- User identification required in the data model (user_id field)
- Focus on core CRUD operations with user isolation

## Authentication Architecture (018-better-auth-jwt)

### JWT Verification Patterns
- **Authentication Authority**: Better Auth (Next.js frontend) issues JWT tokens
- **Verification Layer**: FastAPI backend verifies JWT tokens on every request
- **Token Storage**: httpOnly cookies (managed by Better Auth)
- **Token Validity**: 7 days
- **Signing Algorithm**: HS256 with BETTER_AUTH_SECRET

### JWT Verification Dependency Pattern
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
import os

security = HTTPBearer()

async def get_current_user(token: str = Depends(security)):
    """
    Verify JWT token and extract user_id
    Returns: user_id (UUID)
    Raises: HTTPException 401 for invalid/expired tokens
    """
    try:
        secret = os.getenv("BETTER_AUTH_SECRET")
        payload = jwt.decode(token.credentials, secret, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
```

### Data Isolation Pattern
```python
@router.get("/{user_id}/tasks")
async def list_tasks(
    user_id: str,
    current_user: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Verify path user_id matches authenticated user_id
    if user_id != current_user:
        raise HTTPException(status_code=403, detail="Access denied")

    # Query with user_id filter
    tasks = session.exec(
        select(TodoTask).where(TodoTask.user_id == current_user)
    ).all()
    return tasks
```

### Async SQLModel with asyncpg
- Use `create_async_engine` for async database operations
- Use `AsyncSession` for async session management
- All database operations should be async (await)
- Connection string format: `postgresql+asyncpg://user:pass@host/db`

## Active Technologies
- Python 3.13+ with FastAPI, SQLModel, asyncpg==0.30.0, python-jose[cryptography], bcrypt, uvicorn (018-better-auth-jwt)
- Database: Neon Serverless PostgreSQL with UUID primary keys for User and TodoTask entities
- Authentication: Better Auth (frontend) + JWT verification (backend)
- Database schema includes priority, category, and user_id fields in todotask table with user isolation

## Recent Changes
- 018-better-auth-jwt: Implementing Better Auth + JWT authentication system with clean slate UUID migration
- 017-better-auth-integration: Implemented comprehensive JWT-based authentication system
- 016-backend-db-fix: Added priority and category fields to todotask table, implemented database migration script