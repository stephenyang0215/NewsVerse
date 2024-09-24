import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
export const constantRoutes = [
  {
    path: '/',
    redirect: '/plate',
    component: () => import('@/views/Home/index.vue'),
    meta: { scrollTop: 0 },
    children: [
      {
        path: '/login',
        component: () => import('@/views/login/index'),
        meta: { scrollTop: 0 }
      },
      {
        path: '/plate',
        component: () => import('@/components/Plate/index.vue'),
        meta: { scrollTop: 0 }
      },
      {
        path: '/list',
        component: () => import('@/components/List/index.vue'),
        meta: { scrollTop: 0 }
      },
      {
        path: '/add',
        component: () => import('@/components/Add/index.vue'),
        meta: { scrollTop: 0 }
      },
      {
        path: '/comment',
        component: () => import('@/components/Comment/index.vue'),
        meta: { scrollTop: 0 }
      }
    ]
  }
]

const createRouter = () =>
  new VueRouter({
    routes: constantRoutes
  })

const router = createRouter()

export default router
