from fastapi import FastAPI, Depends, HTTPException, status
from contextlib import asynccontextmanager
from typing import List
from sqlmodel import Session
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Load environment variables FIRST before importing modules that need them
load_dotenv()

# Now import modules that depend on environment variables
from database.session import get_session, create_db_and_tables
from models.todo import TodoTask
from schemas.todo import (
    TodoTaskRead,
    TodoTaskCreate,
    TodoTaskUpdate,
    TodoTaskToggleComplete,
    ErrorResponse
)
from core.services.todo_service import (
    get_all_tasks_for_user,
    get_task_by_id_for_user,
    create_task,
    update_task,
    delete_task,
    toggle_task_completion
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler to initialize the database on startup
    """
    await create_db_and_tables()
    yield


# Create FastAPI app with lifespan event handler
app = FastAPI(
    title="Todo API",
    description="REST API for todo management with JWT-based authentication and user isolation",
    version="0.1.0",
    lifespan=lifespan
)

# Get allowed origins from environment variable, with a default for development
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.tasks import router as tasks_router
from api.auth import router as auth_router

# Include the authentication API router
app.include_router(auth_router, prefix="/api", tags=["auth"])

# Include the tasks API router with user_id in path pattern
# Router already has prefix="/{user_id}/tasks", so final pattern is /api/{user_id}/tasks
app.include_router(tasks_router, prefix="/api")


@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "message": "Todo API is running",
        "version": "0.1.0"
    }

@app.get("/")
def route_check():
    """
    Route check endpoint
    """
    return {
        "status": "healthy",
        "message": "Todo API is running",
        "version": "0.1.0"
    }


# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """
    Global HTTP exception handler
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """
    General exception handler for unexpected errors
    """
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """
    Handler for value errors (like validation errors from user input)
    """
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )