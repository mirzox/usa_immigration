import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Contact from '../views/Contact.vue'
import Checkforms from '../views/Checkforms.vue'
import AnotherServices from '../views/AnotherServices.vue'
import Familyservices from '../views/FamilyServices.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/contact',
    name: 'contact',
    component: Contact
  },
  {
    path: '/checkforms',
    name: 'checkforms',
    component: Checkforms
  },
  {
    path: '/anotherservices',
    name: 'anotherservices',
    component: AnotherServices
  },
  {
    path: '/familyservices',
    name: 'familyservices',
    component: Familyservices
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior: function (to) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
  },
})

router.afterEach((to, from) => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
})

export default router
