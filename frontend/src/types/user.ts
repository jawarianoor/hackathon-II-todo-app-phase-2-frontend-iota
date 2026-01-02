/**
 * User type definitions
 */

export interface User {
  id: string;
  email: string;
  createdAt: string;
}

export interface UserCreate {
  email: string;
  password: string;
}

export interface AuthSession {
  user: User;
  token: string;
}
