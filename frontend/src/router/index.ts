import { createRouter, createWebHistory } from 'vue-router'
import ModeView from '../views/ModeView.vue'
import ManagerView from '../views/ManagerView.vue'
import EditorView from '../views/EditorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ModeView
    },
    {
      path: '/manager',
      name: 'manager',
      component: ManagerView
    },
    {
      path: '/editor',
      name: 'editor',
      component: EditorView
    },
  ]
})

export default router
