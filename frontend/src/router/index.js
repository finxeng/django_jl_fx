import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from "../components/Home";
import UploadFile from "../components/UploadFile";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UploadFile',
      component: UploadFile
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ]
})
