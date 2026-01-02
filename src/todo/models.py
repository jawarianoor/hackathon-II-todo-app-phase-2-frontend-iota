"""Data models for the Todo application.

This module contains the Task dataclass representing a todo item.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique task identifier (auto-incremented).
        title: Task title (required, max 100 characters).
        description: Task description (max 500 characters).
        is_completed: Completion status (default: False).
    """

    id: int
    title: str
    description: str
    is_completed: bool = False
