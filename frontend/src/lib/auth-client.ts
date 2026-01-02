/**
 * Better Auth client for frontend authentication
 */

import { createAuthClient } from 'better-auth/react';

// Create auth client - baseURL is empty since auth API is on same origin
export const authClient = createAuthClient({
  baseURL: typeof window !== 'undefined' ? window.location.origin : '',
});

export const { signIn, signUp, signOut, useSession } = authClient;
