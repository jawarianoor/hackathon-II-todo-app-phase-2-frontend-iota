"""Business logic layer for the Todo application.

This module provides the TodoService class containing all business operations.
"""

from todo.models import Task
from todo.storage import TaskStorage


class TodoService:
    """Service layer for todo operations.

    Provides business logic for task management operations.
    """

    def __init__(self, storage: TaskStorage) -> None:
        """Initialize the service with storage dependency.

        Args:
            storage: TaskStorage instance for data persistence.
        """
        self._storage = storage

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task.

        Args:
            title: Task title (required, non-empty).
            description: Task description.

        Returns:
            Created Task with assigned ID.

        Raises:
            ValueError: If title is empty.
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty.")

        task = Task(id=0, title=title.strip(), description=description.strip())
        return self._storage.add(task)

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            List of all tasks (empty list if none).
        """
        return self._storage.get_all()

    def get_task(self, task_id: int) -> Task | None:
        """Retrieve a task by ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            Task if found, None otherwise.
        """
        if task_id <= 0:
            return None
        return self._storage.get(task_id)

    def update_task(
        self, task_id: int, title: str | None = None, description: str | None = None
    ) -> Task | None:
        """Update an existing task.

        Args:
            task_id: The unique identifier of the task to update.
            title: New title (None to keep current).
            description: New description (None to keep current).

        Returns:
            Updated Task if found, None otherwise.
        """
        task = self._storage.get(task_id)
        if task is None:
            return None

        if title is not None and title.strip():
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()

        self._storage.update(task)
        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The unique identifier of the task to delete.

        Returns:
            True if deleted, False if not found.
        """
        return self._storage.delete(task_id)

    def toggle_completion(self, task_id: int) -> Task | None:
        """Toggle task completion status.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            Updated Task if found, None otherwise.
        """
        task = self._storage.get(task_id)
        if task is None:
            return None

        task.is_completed = not task.is_completed
        self._storage.update(task)
        return task
