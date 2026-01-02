'use client';

import { useEffect, useState, useCallback } from 'react';
import { Task } from '@/types/task';
import { TaskList } from '@/components/tasks/task-list';
import { TaskForm } from '@/components/tasks/task-form';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { apiClient } from '@/lib/api-client';
import { authClient } from '@/lib/auth-client';

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [userId, setUserId] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchTasks = useCallback(async (uid: string) => {
    try {
      console.log('Fetching tasks for user:', uid);
      const data = await apiClient.getTasks(uid);
      console.log('Tasks fetched:', data);
      setTasks(data.tasks || []);
      setError(null);
    } catch (err) {
      console.error('Error fetching tasks:', err);
      setError(err instanceof Error ? err.message : 'Failed to fetch tasks');
    }
  }, []);

  useEffect(() => {
    const init = async () => {
      try {
        const session = await authClient.getSession();
        console.log('Dashboard session:', session);

        if (!session.data?.user) {
          console.log('No user in session');
          setIsLoading(false);
          return;
        }

        const user = session.data.user;
        console.log('User ID:', user.id);
        setUserId(user.id);

        await fetchTasks(user.id);
      } catch (err) {
        console.error('Error in init:', err);
        setError(err instanceof Error ? err.message : 'Failed to load session');
      } finally {
        setIsLoading(false);
      }
    };

    init();
  }, [fetchTasks]);

  const handleCreateTask = async (title: string, description: string) => {
    if (!userId) throw new Error('User not authenticated');
    setError(null);
    const newTask = await apiClient.createTask(userId, { title, description });
    setTasks((prev) => [newTask, ...prev]);
    setShowForm(false);
  };

  const handleUpdateTask = async (title: string, description: string) => {
    if (!userId || !editingTask) throw new Error('Cannot update task');
    setError(null);
    const updatedTask = await apiClient.updateTask(userId, editingTask.id, {
      title,
      description,
    });
    setTasks((prev) =>
      prev.map((t) => (t.id === updatedTask.id ? updatedTask : t))
    );
    setEditingTask(null);
  };

  const handleToggleComplete = async (taskId: string) => {
    if (!userId) return;
    setError(null);
    try {
      console.log('Toggling task:', taskId, 'for user:', userId);
      const updatedTask = await apiClient.toggleComplete(userId, taskId);
      console.log('Toggle result:', updatedTask);
      setTasks((prev) =>
        prev.map((t) => (t.id === updatedTask.id ? updatedTask : t))
      );
    } catch (err) {
      console.error('Error toggling task:', err);
      setError(err instanceof Error ? err.message : 'Failed to update task');
    }
  };

  const handleDelete = async (taskId: string) => {
    if (!userId) return;
    setError(null);
    try {
      console.log('Deleting task:', taskId, 'for user:', userId);
      await apiClient.deleteTask(userId, taskId);
      setTasks((prev) => prev.filter((t) => t.id !== taskId));
    } catch (err) {
      console.error('Error deleting task:', err);
      setError(err instanceof Error ? err.message : 'Failed to delete task');
    }
  };

  const handleEdit = (task: Task) => {
    setEditingTask(task);
    setShowForm(false);
  };

  const handleCancelForm = () => {
    setShowForm(false);
    setEditingTask(null);
  };

  if (isLoading) {
    return (
      <div className="flex justify-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600" />
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">My Tasks</h2>
          <p className="text-gray-600">Manage your tasks below</p>
        </div>
        {!showForm && !editingTask && (
          <Button onClick={() => setShowForm(true)}>Add Task</Button>
        )}
      </div>

      {error && (
        <div className="mb-6 rounded-md bg-red-50 p-4 text-sm text-red-600">
          {error}
        </div>
      )}

      {(showForm || editingTask) && (
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>{editingTask ? 'Edit Task' : 'New Task'}</CardTitle>
          </CardHeader>
          <CardContent>
            <TaskForm
              task={editingTask || undefined}
              onSubmit={editingTask ? handleUpdateTask : handleCreateTask}
              onCancel={handleCancelForm}
            />
          </CardContent>
        </Card>
      )}

      <TaskList
        tasks={tasks}
        onToggleComplete={handleToggleComplete}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />
    </div>
  );
}
