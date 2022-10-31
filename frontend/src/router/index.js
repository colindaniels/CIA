import { createRouter, createWebHistory } from 'vue-router'



  const routes = [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/home-view.vue'),
      meta: {
        title: 'Home TITLE'
      }
    },
    {
        path: '/test',
        name: 'TEST',
        component: () => import('../views/test-view.vue'),
        meta: {
          title: 'TEST'
        }
      },
      {
        path: '/map',
        name: 'map',
        component: () => import('../views/map-view.vue'),
        meta: {
          title: 'map'
        }
      }
    
    
  ]

  const router = createRouter({
    history: createWebHistory(),
    routes,
  });



export default router;