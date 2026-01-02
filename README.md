# The Evolution of Todo - Phase 1

A simple in-memory todo console application built with clean architecture principles.

## Features

- Add tasks with title and optional description
- List all tasks with completion status indicators
- View individual task details
- Mark tasks as complete/incomplete
- Update task title and/or description
- Delete tasks
- **Interactive Mode** - Menu-driven session for easy task management

## Requirements

- Python 3.13+
- UV package manager

## Installation

```bash
# Install the package in development mode
uv pip install -e .
```

## Usage

### Quick Start (Single Command)

```bash
# Add a new task
todolist add "Buy groceries" -d "Milk, eggs, bread"

# List all tasks
todolist list
```


### Interactive Mode

Enter an interactive menu-driven session to manage tasks without typing full commands:

```bash
# Enter interactive mode
todolist interactive
```

**Menu Options:**
```
Menu:
  1. Add Task
  2. List Tasks
  3. Get Task Details
  4. Update Task
  5. Mark Complete/Incomplete
  6. Delete Task
  7. Exit
```

**Example Session:**
```
$ todolist interactive
==================================================
         Todo List - Interactive Mode
==================================================

Menu:
  1. Add Task
  2. List Tasks
  3. Get Task Details
  4. Update Task
  5. Mark Complete/Incomplete
  6. Delete Task
  7. Exit

Enter your choice (1-7): 1
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
Added task 1: "Buy groceries"

Menu:
  1. Add Task
  ...
```

### All Commands

```bash
# Show compact output
todolist list --simple

# View task details
todolist get 1

# Mark task as complete
todolist mark 1 --complete

# Mark task as incomplete
todolist mark 1 --incomplete

# Update task title
todolist update 1 --title "New title"

# Update task description
todolist update 1 -d "New description"

# Delete a task
todolist delete 1

# Enter interactive mode
todolist interactive

# Show help
todolist --help

# Show version
todolist --version
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing

# Run specific test file
uv run pytest tests/unit/use_cases/test_add_todo.py -v
```

## Project Structure

```
todolist-phase-1/
├── src/
│   └── core/
│       ├── entities/
│       │   └── todo.py           # Todo domain entity
│       ├── exceptions/
│       │   └── todo_errors.py    # Domain exceptions
│       ├── ports/
│       │   └── repository.py     # Repository port (interface)
│       └── use_cases/
│           ├── add_todo.py       # Add todo use case
│           ├── list_todos.py     # List todos use case
│           ├── get_todo.py       # Get todo use case
│           ├── update_todo.py    # Update todo use case
│           ├── delete_todo.py    # Delete todo use case
│           └── mark_complete.py  # Mark complete use case
├── adapters/
│   ├── cli/
│   │   └── __main__.py           # CLI entry point
│   └── repository/
│       └── memory_repository.py  # In-memory repository implementation
├── tests/
│   ├── unit/
│   │   ├── entities/
│   │   ├── ports/
│   │   └── use_cases/
│   └── integration/
│       └── test_cli_flow.py      # Full workflow integration tests
├── specs/
│   └── 001-todo-console-app/
│       ├── spec.md               # Feature specification
│       ├── plan.md               # Architecture plan
│       └── tasks.md              # Task breakdown
├── pyproject.toml
└── README.md
```

## Architecture

This project follows Clean Architecture with:

- **Entities**: Domain objects with validation logic
- **Use Cases**: Business logic encapsulated in single-responsibility classes
- **Ports**: Abstract interfaces for external dependencies
- **Adapters**: Concrete implementations (CLI, repository)

This separation enables easy testing and future evolution (e.g., adding persistence).

## Phase Roadmap

- **Phase 1**: In-memory console app (current)
- **Phase 2**: Add file-based persistence
- **Phase 3**: REST API
- **Phase 4**: Web UI
- **Phase 5**: Database persistence
