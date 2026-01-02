'use client';

import { RegisterForm } from '@/components/auth/register-form';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { useRouter } from 'next/navigation';
import { authClient } from '@/lib/auth-client';

export default function RegisterPage() {
  const router = useRouter();

  const handleRegister = async (email: string, password: string, name?: string) => {
    try {
      const result = await authClient.signUp.email({
        email,
        password,
        name: name ?? email.split('@')[0],
      } as { email: string; password: string; name: string });

      console.log('SignUp result:', result);

      if (result.error) {
        console.error('SignUp error:', result.error);
        throw new Error(result.error.message || result.error.code || JSON.stringify(result.error) || 'Registration failed');
      }

      // Redirect to dashboard on success
      router.push('/dashboard');
    } catch (err) {
      console.error('Registration catch error:', err);
      throw err;
    }
  };

  const handleSwitchToLogin = () => {
    router.push('/auth/login');
  };

  return (
    <div className="flex min-h-screen items-center justify-center px-4">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-center text-2xl">Create Account</CardTitle>
        </CardHeader>
        <CardContent>
          <RegisterForm
            onSubmit={handleRegister}
            onSwitchToLogin={handleSwitchToLogin}
          />
        </CardContent>
      </Card>
    </div>
  );
}
