"""Application entry point for the Todo application.

This module wires all components and starts the CLI.
"""

from todo.cli import TodoCLI
from todo.service import TodoService
from todo.storage import TaskStorage


def main() -> None:
    """Application entry point."""
    # Initialize components with dependency injection
    storage = TaskStorage()
    service = TodoService(storage)
    cli = TodoCLI(service)

    # Start the application
    cli.run()


if __name__ == "__main__":
    main()
