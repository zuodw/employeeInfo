import Vue from 'vue'
import Router from 'vue-router'
import EmployeeInfoUpdate from '@/components/EmployeeInfoUpdate'
import SignUp from '@/components/SignUp'
import SignIn from '@/components/SignIn'
import Index from '@/components/Index'
import MyPage from '@/components/MyPage'
import axios from 'axios'

Vue.use(Router)
Vue.prototype.$axios = axios

axios.defaults.baseURL = 'http://192.168.0.102:5000/'

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
      path: '/signup',
      name: 'SignUp',
      component: SignUp,
      meta: {
        isLogin: false
      }
    },
    {
      path: '/signin',
      name: 'SignIn',
      component: SignIn,
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
      path: '/mypage',
      name: 'MyPage',
      component: MyPage,
      meta: {
        isLogin: true
      }
    }
  ]
})
