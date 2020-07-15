import Vue from 'vue'
import Router from 'vue-router'
import EmployeeInfoUpdate from '@/components/EmployeeInfoUpdate'
import SignUp from '@/components/SignUp'
import Index from '@/components/Index'
import axios from 'axios'

Vue.use(Router)
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://192.168.0.102:5000/'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/employeeInfoUpdate',
      name: 'EmployeeInfoUpdate',
      component: EmployeeInfoUpdate
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp
    }
  ]
})
