"""Tasks API routes."""

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

logger = logging.getLogger(__name__)

from src.api.deps import get_db
from src.services.task_service import TaskService
from src.schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskList

# Note: Authentication is handled by Better Auth on the frontend
# The user_id in the URL is verified by the frontend session
# Better Auth uses string IDs, not UUIDs
router = APIRouter(prefix="/api/{user_id}/tasks", tags=["tasks"])


@router.get("", response_model=TaskList)
async def get_tasks(
    user_id: str,
    db: AsyncSession = Depends(get_db),
) -> TaskList:
    """Get all tasks for a user."""
    logger.info(f"GET /tasks called for user: {user_id}")
    try:
        service = TaskService(db)
        tasks = await service.get_tasks(user_id)
        logger.info(f"Found {len(tasks)} tasks for user {user_id}")
        return TaskList(
            tasks=[TaskResponse.model_validate(task) for task in tasks],
            total=len(tasks),
        )
    except Exception as e:
        logger.error(f"Error getting tasks: {e}")
        raise


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    user_id: str,
    task_data: TaskCreate,
    db: AsyncSession = Depends(get_db),
) -> TaskResponse:
    """Create a new task."""
    service = TaskService(db)
    task = await service.create_task(user_id, task_data)
    return TaskResponse.model_validate(task)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    user_id: str,
    task_id: str,
    db: AsyncSession = Depends(get_db),
) -> TaskResponse:
    """Get a specific task."""
    service = TaskService(db)
    task = await service.get_task(task_id, user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return TaskResponse.model_validate(task)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    user_id: str,
    task_id: str,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db),
) -> TaskResponse:
    """Update a task."""
    service = TaskService(db)
    task = await service.update_task(task_id, user_id, task_data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return TaskResponse.model_validate(task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    user_id: str,
    task_id: str,
    db: AsyncSession = Depends(get_db),
) -> None:
    """Delete a task."""
    logger.info(f"DELETE /tasks/{task_id} called for user: {user_id}")
    try:
        service = TaskService(db)
        deleted = await service.delete_task(task_id, user_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )
        logger.info(f"Task {task_id} deleted successfully")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting task: {e}")
        raise


@router.patch("/{task_id}/complete", response_model=TaskResponse)
async def toggle_task_complete(
    user_id: str,
    task_id: str,
    db: AsyncSession = Depends(get_db),
) -> TaskResponse:
    """Toggle task completion status."""
    logger.info(f"PATCH /tasks/{task_id}/complete called for user: {user_id}")
    try:
        service = TaskService(db)
        task = await service.toggle_complete(task_id, user_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found",
            )
        logger.info(f"Task {task_id} toggled to is_completed={task.is_completed}")
        return TaskResponse.model_validate(task)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error toggling task: {e}")
        raise
