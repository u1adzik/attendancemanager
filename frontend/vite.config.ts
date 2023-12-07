import { fileURLToPath, URL } from 'node:url'
import { createProxyMiddleware } from 'http-proxy-middleware';
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: '127.0.0.1',
    port: 8080,
    middleware: [
      createProxyMiddleware('/api', {
        target: 'http://127.0.0.1:5000', // Адрес и порт вашего сервера Flask
        changeOrigin: true,
        pathRewrite: {
          '^/api': '',
        },
      }),
    ],
  },
  plugins: [
    vue(),
    vueJsx(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
