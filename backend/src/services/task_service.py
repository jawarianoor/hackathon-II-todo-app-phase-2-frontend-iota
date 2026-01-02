"""Task service for business logic operations."""

from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.task import Task
from src.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Service class for task operations."""

    def __init__(self, session: AsyncSession):
        """Initialize with database session."""
        self.session = session

    async def get_tasks(self, user_id: str) -> list[Task]:
        """Get all tasks for a user."""
        statement = select(Task).where(Task.user_id == user_id).order_by(Task.created_at.desc())
        result = await self.session.exec(statement)
        return list(result.all())

    async def get_task(self, task_id: str, user_id: str) -> Task | None:
        """Get a specific task by ID for a user."""
        try:
            task_uuid = UUID(task_id)
        except ValueError:
            return None
        statement = select(Task).where(Task.id == task_uuid, Task.user_id == user_id)
        result = await self.session.exec(statement)
        return result.first()

    async def create_task(self, user_id: str, task_data: TaskCreate) -> Task:
        """Create a new task for a user."""
        task = Task(
            user_id=user_id,
            title=task_data.title,
            description=task_data.description,
        )
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def update_task(
        self, task_id: str, user_id: str, task_data: TaskUpdate
    ) -> Task | None:
        """Update an existing task."""
        task = await self.get_task(task_id, user_id)
        if not task:
            return None

        update_data = task_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)

        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete_task(self, task_id: str, user_id: str) -> bool:
        """Delete a task."""
        task = await self.get_task(task_id, user_id)
        if not task:
            return False

        await self.session.delete(task)
        await self.session.commit()
        return True

    async def toggle_complete(self, task_id: str, user_id: str) -> Task | None:
        """Toggle the completion status of a task."""
        task = await self.get_task(task_id, user_id)
        if not task:
            return None

        task.is_completed = not task.is_completed
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task
