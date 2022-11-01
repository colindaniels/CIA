import { createRouter, createWebHistory } from 'vue-router'



  const routes = [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/home-view.vue'),
      meta: {
        title: 'Home'
      }
    },
    {
        path: '/slides',
        name: 'slides',
        component: () => import('../views/slides-view.vue'),
        meta: {
          title: 'Slides'
        }
      },
      {
        path: '/map',
        name: 'map',
        component: () => import('../views/map-view.vue'),
        meta: {
          title: 'Crime Map'
        }
      }
    
    
  ]

  const router = createRouter({
    history: createWebHistory(),
    routes,
  });



export default router;