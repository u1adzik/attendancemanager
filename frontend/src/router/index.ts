import { createRouter, createWebHistory } from 'vue-router'
import ModeView from '../views/ModeView.vue'
import ManagerView from '../views/ManagerView.vue'
import EditorView from '../views/EditorView.vue'
import AttendanceView from '../views/AttendanceView.vue'
import StudentsView from '../views/StudentsView.vue'

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
    {
    path: '/attendance/:disciplineId/:groupId',
    name: 'AttendanceView',
    component: AttendanceView
  },
  {
    path: '/students/:id',
    name: 'StudentDetails',
    component: StudentsView // Используйте компонент, который будет отображать информацию о студенте
  },
  ]
})

export default router
