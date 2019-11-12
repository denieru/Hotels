import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import list_ini from '@/components/inih/list_ini'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Inicio',
      name: 'list_ini',
      component: list_ini
    }

  ], 
  mode:'history'
})
