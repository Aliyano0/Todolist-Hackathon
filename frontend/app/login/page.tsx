'use client';

import LoginForm from '@/components/auth/LoginForm';
import { useAuth } from '@/providers/AuthProvider';

export default function LoginPage() {
  const { loading } = useAuth();

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-50">
      <LoginForm />
    </div>
  );
}