'use client';

import { Task } from '@/types/task';
import { Button } from '@/components/ui/button';
import { formatDate } from '@/lib/utils';

interface TaskItemProps {
  task: Task;
  onToggleComplete: (taskId: string) => Promise<void>;
  onEdit: (task: Task) => void;
  onDelete: (taskId: string) => Promise<void>;
}

export function TaskItem({
  task,
  onToggleComplete,
  onEdit,
  onDelete,
}: TaskItemProps) {
  const handleToggle = async () => {
    await onToggleComplete(task.id);
  };

  const handleDelete = async () => {
    if (confirm('Are you sure you want to delete this task?')) {
      await onDelete(task.id);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow p-4 flex items-start gap-4">
      <button
        onClick={handleToggle}
        className={`mt-1 h-5 w-5 rounded border-2 flex items-center justify-center transition-colors ${
          task.is_completed
            ? 'bg-primary-600 border-primary-600 text-white'
            : 'border-gray-300 hover:border-primary-400'
        }`}
        aria-label={task.is_completed ? 'Mark as incomplete' : 'Mark as complete'}
      >
        {task.is_completed && (
          <svg className="h-3 w-3" fill="currentColor" viewBox="0 0 12 12">
            <path d="M10.28 2.28L3.989 8.575 1.695 6.28A1 1 0 00.28 7.695l3 3a1 1 0 001.414 0l7-7A1 1 0 0010.28 2.28z" />
          </svg>
        )}
      </button>

      <div className="flex-1 min-w-0">
        <h3
          className={`font-medium ${
            task.is_completed ? 'line-through text-gray-400' : 'text-gray-900'
          }`}
        >
          {task.title}
        </h3>
        {task.description && (
          <p className="mt-1 text-sm text-gray-500 line-clamp-2">
            {task.description}
          </p>
        )}
        <p className="mt-2 text-xs text-gray-400">
          Created {formatDate(task.created_at)}
        </p>
      </div>

      <div className="flex gap-2">
        <Button variant="secondary" size="sm" onClick={() => onEdit(task)}>
          Edit
        </Button>
        <Button variant="secondary" size="sm" onClick={handleDelete}>
          Delete
        </Button>
      </div>
    </div>
  );
}
