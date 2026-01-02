<!--
Sync Impact Report
==================
Version change: NEW (initial ratification)
Added sections: All sections are new
Removed sections: N/A (initial constitution)
Templates requiring updates: None (constitution template already aligns)
-->

# The Evolution of Todo - Phase I: In-Memory Python Console Todo App Constitution

## Core Principles

### I. Product Architect Mindset

Every contributor operates as a Product Architect, not a code implementer. This means:
- All decisions must be justified by explicit product value or future evolution benefit
- Technical choices must consider Phase II and beyond implications
- Architecture diagrams and decision rationale must be documented
- Questions are welcomed; assumptions must be surfaced and challenged

**Rationale**: "The Evolution of Todo" is an intentional multi-phase evolution project. Every
Phase I decision shapes the migration path forward. Treating contributors as architects
ensures decisions are reversible, traceable, and evolution-aware.

### II. Clean Architecture Mandatory

The application MUST follow clean architecture principles:
- Domain logic is isolated from I/O and presentation concerns
- Core entities and use cases reside in `src/core/` with zero external dependencies
- Ports (interfaces) define all external interactions; adapters implement them
- Dependencies point inward; no layer may import from an outer layer

**Rationale**: Phase I is an in-memory prototype, but Phase II will add persistence,
Phase III will add a web API, and Phase IV will add a GUI. Clean architecture ensures
each evolution is a port/adapter replacement, not a rewrite.

### III. Simplicity First (Non-Negotiable)

Complexity must be justified before being introduced. For every feature or abstraction:
- Ask: "What specific problem does this solve today?"
- If no immediate problem: do not introduce
- Prefer the simplest implementation that satisfies current requirements
- Defer decisions to the last responsible moment

**Rationale**: This is an evolution project. Over-engineering Phase I creates debt for
Phase II. The YAGNI principle ("You Aren't Gonna Need It") applies aggressively.

### IV. Six Core Features Only

Phase I MUST implement exactly these six features with no additions:
1. **Add**: Create a new todo item with title and optional description
2. **View**: List all todos; show individual todo details
3. **Update**: Modify title or description of an existing todo
4. **Delete**: Remove a todo item permanently
5. **Mark Complete**: Toggle completion status on a todo
6. **Interactive Mode**: Menu-driven session for persistent task management

**Rationale**: Constraining scope ensures a focused, complete Phase I. Feature creep
in early phases compounds through the evolution timeline. Interactive mode is a
UI/UX enhancement that improves usability without adding domain features.

### V. Zero Persistence Mandate

Phase I MUST NOT include any persistence layer:
- No file I/O for todo storage
- No database (SQL, NoSQL, embedded, or otherwise)
- No network storage
- All data lives in memory for the session only

**Rationale**: Persistence is Phase II's core concern. Introducing it early creates
legacy code that must be migrated. The in-memory constraint forces clean architecture
by eliminating "just save to disk" shortcuts.

### VI. Standard Library Only

Phase I MUST use only Python standard library:
- No third-party packages for any purpose
- No external CLI libraries (e.g., Click, Typer, argparse-based frameworks)
- No framework dependencies (e.g., Flask, FastAPI, Django)
- Build CLI interface using `argparse` at most, or manual argument parsing

**Rationale**: Standard library ensures portability, zero-dependency installation,
and demonstrates mastery of fundamentals. External CLI libraries hide architecture
behind "magic" that complicates future evolution.

### VII. Test-Driven Development (Non-Negotiable)

Phase I MUST use TDD for all implementation:
- Write failing test first for every feature
- Test must fail for a clear, specific reason
- Implement minimal code to pass the test
- Refactor while tests remain green
- Red-Green-Refactor cycle strictly enforced

**Rationale**: TDD ensures design discipline, regression safety, and evolution
readiness. Tests from Phase I will validate Phase II migrations.

## Goals

### Primary Goal
Deliver a working, tested, clean-architecture in-memory Python console todo application
that implements all six core features and serves as a solid foundation for future
evolution phases.

### Secondary Goals
- Establish clean architecture patterns that survive Phase II-IV evolution
- Create comprehensive test coverage that enables confident refactoring
- Document architectural decisions for traceability
- Demonstrate Spec-Kit Plus specification-driven development workflow

### Non-Goals
- Any form of data persistence (deferred to Phase II)
- Web API or HTTP server (deferred to Phase III)
- Graphical user interface (deferred to Phase IV)
- User authentication or authorization
- Data import/export functionality
- Categories, tags, or advanced metadata
- Undo/redo functionality
- Search or filtering capabilities

## Success Criteria

### Functional Criteria
- All six features (add, view, update, delete, mark complete, interactive mode) work correctly
- CLI interface is usable and provides helpful feedback
- Error handling provides clear, actionable messages

### Architectural Criteria
- Core domain has zero imports from outer layers (CLI, infrastructure)
- All dependencies point inward toward the domain
- New features can be added without modifying domain code
- Tests can run without CLI interface

### Quality Criteria
- 100% unit test coverage for core domain entities and use cases
- Tests execute in under 5 seconds
- No linting errors or warnings (flake8/pyflakes compliance)
- Type hints used throughout (PEP 484)

### Evolution Criteria
- Domain code contains no references to "Phase I" or in-memory constraints
- Persistence layer can be added without modifying domain code
- CLI can be replaced without modifying domain code

## Project Structure

```
todolist-phase-1/
├── src/
│   └── core/
│       ├── entities/
│       │   └── todo.py           # Todo entity, value objects
│       ├── ports/
│       │   ├── repository.py     # Repository port (in-memory impl in Phase I)
│       │   └── cli.py            # CLI port
│       ├── use_cases/
│       │   ├── add_todo.py
│       │   ├── list_todos.py
│       │   ├── get_todo.py
│       │   ├── update_todo.py
│       │   ├── delete_todo.py
│       │   └── mark_complete.py
│       └── exceptions/
│           └── todo_errors.py    # Domain exceptions
├── adapters/
│   ├── cli/
│   │   └── argparse_adapter.py   # argparse implementation
│   └── repository/
│       └── memory_repository.py  # In-memory implementation
├── tests/
│   ├── unit/
│   │   ├── entities/
│   │   ├── use_cases/
│   │   └── ports/
│   └── integration/
│       └── test_full_flow.py
├── specs/
│   └── phase-1/
│       ├── spec.md               # Feature specification
│       ├── plan.md               # Implementation plan
│       └── tasks.md              # Task breakdown
├── history/
│   ├── prompts/                  # PHR records
│   └── adr/                      # Architecture decision records
├── README.md
└── requirements.txt              # Empty or Python version only
```

## Constraints

### Technical Constraints
- Use UV to initiliaze the project and use UV venv.
- Python 3.13+ required
- Standard library only (no pip dependencies)
- In-memory data storage only
- CLI interface (no GUI or web)

### Process Constraints
- All features must follow TDD (Red-Green-Refactor)
- All architectural decisions must be documented as ADRs
- All changes must be traceable to a user story in spec.md
- Spec-Kit Plus workflow must be followed for all work

### Quality Constraints
- No TODO comments left in production code
- Maximum cyclomatic complexity: 10 per function
- Maximum function length: 50 lines
- All public APIs must have docstrings
- Type hints required for all function signatures

## Additional Constraints

### Forbidden Patterns
- Direct print statements in domain code (use ports)
- Hardcoded strings in domain (use constants or value objects)
- Mutable global state
- Implicit type conversions
- Exception swallowing without logging
- Magic numbers or magic strings

### Required Patterns
- Explicit is better than implicit (PEP 20)
- Composition over inheritance
- Single responsibility per class/function
- Dependency injection for all external concerns
- Result objects or exceptions for error handling (not return codes)

## Development Workflow

### Required Workflow Steps
1. **Spec**: Create feature specification in `specs/phase-1/spec.md`
2. **Plan**: Create implementation plan in `specs/phase-1/plan.md`
3. **Tasks**: Generate task breakdown in `specs/phase-1/tasks.md`
4. **Red**: Write failing test for next task
5. **Green**: Implement minimal code to pass test
6. **Refactor**: Improve code while tests stay green
7. **Document**: Update ADR if architectural decisions were made
8. **Repeat**: Continue until all tasks complete

### Code Review Standards
- All PRs must have passing tests before review
- Review must verify constitution compliance
- Review must verify clean architecture boundaries
- Review must verify TDD workflow was followed

## Governance

### Constitution Supremacy
This constitution supersedes all other development practices, conventions, and
guidelines within the project. When conflicts arise, constitution provisions take
precedence.

### Amendment Process
Constitutional amendments require:
1. Documentation of proposed change with rationale
2. Impact analysis on existing phases
3. Review by at least one other contributor
4. Update to constitution version following semantic versioning

### Versioning Policy
- **MAJOR**: Backward-incompatible changes to principles or removal of constraints
- **MINOR**: Addition of new principles, goals, or significant clarification
- **PATCH**: Typo fixes, wording clarifications, non-semantic refinements

### Compliance Verification
All PRs and commits must verify constitution compliance. Violations must be
documented in an ADR with explicit justification for why the constraint was
intentionally violated.

**Version**: 1.1.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
