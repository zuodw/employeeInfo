import Vue from 'vue'
import Router from 'vue-router'
import EmployeeInfoUpdate from '@/components/EmployeeInfoUpdate'
import SignUp from '@/components/SignUp'
import Index from '@/components/Index'
import axios from 'axios'

Vue.use(Router)
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://192.168.0.106:5000/'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      meta: {
        isLogin: false
      }
    },
    {
      path: '/employeeInfoUpdate',
      name: 'EmployeeInfoUpdate',
      component: EmployeeInfoUpdate,
      meta: {
        isLogin: true
      }
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUp,
      meta: {
        isLogin: false
      }
    }
  ]
})
