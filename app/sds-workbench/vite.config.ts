import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

function resolveBasePath(): string {
  const fromEnv = process.env.BASE_PATH?.trim();
  if (fromEnv) return fromEnv.endsWith('/') ? fromEnv : `${fromEnv}/`;

  const repoName = process.env.GITHUB_REPOSITORY?.split('/')[1];
  if (process.env.GITHUB_ACTIONS && repoName) return `/${repoName}/`;

  return '/';
}

export default defineConfig({
  base: resolveBasePath(),
  plugins: [react()],
  server: {
    port: 5173,
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'terser',
  },
  test: {
    environment: 'node',
    globals: true,
  },
});
