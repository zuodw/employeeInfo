import Vue from 'vue'
import Router from 'vue-router'
import EmployeeInfoAdd from '@/components/EmployeeInfoAdd'
import axios from 'axios'

Vue.use(Router)
axios.defaults.baseURL = 'http://192.168.0.106/'
Vue.prototype.$axios = axios

export default new Router({
  routes: [
    {
      path: '/',
      name: 'EmployeeInfoAdd',
      component: EmployeeInfoAdd
    }
  ]
})
