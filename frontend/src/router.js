import { createRouter, createWebHistory } from 'vue-router';
import LessonsList from './components/LessonsList.vue';
import LessonDetail from './components/LessonDetail.vue';

const routes = [
  {
    path: '/',
    name: 'LessonsList',
    component: LessonsList,
  },
  {
    path: '/lesson/:id',
    name: 'LessonDetail',
    component: LessonDetail,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
