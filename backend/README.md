# Todo Backend API (Single-User Implementation)

This is a FastAPI backend service for the single-user Todo web application. The backend provides RESTful API endpoints for creating, reading, updating, and deleting todo tasks without authentication. Data is persisted using SQLModel ORM with Neon Serverless PostgreSQL database.

## Features

- Basic Todo CRUD operations (Create, Read, Update, Delete)
- Toggle completion status
- Single-user implementation (no authentication required)
- RESTful API endpoints for todo management
- Standardized error responses
- Connection pooling for database efficiency
- Response wrapping with `data` property for frontend compatibility
- String IDs and camelCase field names for frontend compatibility

## Endpoints

- `GET /api/todos` - Retrieve all todos
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo
- `PATCH /api/todos/{id}/complete` - Toggle completion status

## Setup

1. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit the .env file to include your database URL
   DATABASE_URL=postgresql://username:password@host:port/database_name
   ```

3. Run the application:
   ```bash
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   # or if using python directly
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Testing

Run the tests using pytest:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=backend

# Run specific test file
pytest tests/test_todo_crud.py -v
```

## Architecture

This project follows clean architecture principles:

- `models/` - SQLModel database models
- `api/` - API routes for todo operations (tasks.py only)
- `core/` - Core business logic and services
- `database/` - Database configuration and session management
- `schemas/` - Pydantic schemas for request/response validation
- `tests/` - Backend tests
- `utils/` - Utility functions for data transformation