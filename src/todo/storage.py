"""In-memory storage for the Todo application.

This module provides the TaskStorage class for managing tasks in memory.
"""

from todo.models import Task


class TaskStorage:
    """In-memory storage manager for tasks.

    Provides CRUD operations for Task objects stored in memory.
    """

    def __init__(self) -> None:
        """Initialize the storage with empty task dictionary."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """Add a new task to storage.

        Args:
            task: Task object to store (id will be assigned).

        Returns:
            Task with assigned ID.
        """
        task.id = self._next_id
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> Task | None:
        """Retrieve a task by ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            Task if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def get_all(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            List of all tasks (empty list if none).
        """
        return list(self._tasks.values())

    def update(self, task: Task) -> bool:
        """Update an existing task.

        Args:
            task: Task object with updated values.

        Returns:
            True if updated, False if task not found.
        """
        if task.id not in self._tasks:
            return False
        self._tasks[task.id] = task
        return True

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The unique identifier of the task to delete.

        Returns:
            True if deleted, False if task not found.
        """
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True

    def clear(self) -> None:
        """Remove all tasks and reset ID counter."""
        self._tasks.clear()
        self._next_id = 1
