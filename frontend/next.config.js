/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
  serverExternalPackages: ['pg', '@neondatabase/serverless', 'better-auth', 'drizzle-orm'],
}

module.exports = nextConfig
