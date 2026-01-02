/**
 * Centralized API client for tasks
 * Authentication is handled by Better Auth on the frontend
 */

import type { Task, TaskCreate, TaskList, TaskUpdate } from '@/types/task';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Log API URL for debugging (only in browser)
if (typeof window !== 'undefined') {
  console.log('API_URL:', API_URL);
}

interface ApiError {
  detail: string;
  code?: string;
  status: number;
}

class ApiClient {
  private async request<T>(
    endpoint: string,
    options: RequestInit = {},
    retries = 2
  ): Promise<T> {
    const url = `${API_URL}${endpoint}`;
    const method = options.method || 'GET';
    console.log('API Request:', method, url);

    // Only add Content-Type for requests with body
   const headers = new Headers(options.headers);

if (options.body) {
  headers.set('Content-Type', 'application/json');
}

    try {
      const response = await fetch(url, {
        ...options,
        headers,
        mode: 'cors',
      });

      console.log('API Response:', response.status, response.statusText);
      return await this.handleResponse<T>(response);
    } catch (error) {
      console.error('Fetch error:', error);
      if (retries > 0) {
        console.log(`Retrying... (${retries} attempts left)`);
        // Wait 1 second before retry (helps with cold starts)
        await new Promise(resolve => setTimeout(resolve, 1000));
        return this.request<T>(endpoint, options, retries - 1);
      }
      throw error;
    }
  }

  private async handleResponse<T>(response: Response): Promise<T> {

    if (!response.ok) {
      const error: ApiError = await response.json().catch(() => ({
        detail: 'An unexpected error occurred',
        status: response.status,
      }));
      // Ensure detail is a string
      const message = typeof error.detail === 'string'
        ? error.detail
        : JSON.stringify(error.detail) || 'Request failed';
      throw new Error(message);
    }

    // Handle 204 No Content responses
    if (response.status === 204) {
      return {} as T;
    }

    return response.json();
  }

  // Kept for backwards compatibility but no longer needed
  setToken(_token: string | null): void {
    // No-op: auth is handled by Better Auth sessions
  }

  // Task endpoints
  async getTasks(userId: string): Promise<TaskList> {
    return this.request<TaskList>(`/api/${userId}/tasks`);
  }

  async getTask(userId: string, taskId: string): Promise<Task> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}`);
  }

  async createTask(userId: string, data: TaskCreate): Promise<Task> {
    return this.request<Task>(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async updateTask(userId: string, taskId: string, data: TaskUpdate): Promise<Task> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  async deleteTask(userId: string, taskId: string): Promise<void> {
    await this.request<void>(`/api/${userId}/tasks/${taskId}`, {
      method: 'DELETE',
    });
  }

  async toggleComplete(userId: string, taskId: string): Promise<Task> {
    return this.request<Task>(`/api/${userId}/tasks/${taskId}/complete`, {
      method: 'PATCH',
    });
  }
}

export const apiClient = new ApiClient();
