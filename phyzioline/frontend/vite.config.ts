import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    // Output to Django's static files
    outDir: '../static/react_build',
    manifest: true,
    rollupOptions: {
      input: './src/main.tsx',
    },
  },
})
