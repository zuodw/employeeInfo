import Vue from 'vue'
import Router from 'vue-router'
import EmployeeInfoAdd from '@/components/EmployeeInfoAdd'
import Login from '@/components/Login'
import axios from 'axios'

Vue.use(Router)
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://192.168.0.106/'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'EmployeeInfoAdd',
      component: EmployeeInfoAdd
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
