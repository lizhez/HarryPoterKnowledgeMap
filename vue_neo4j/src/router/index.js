import Vue from 'vue'
import VueRouter from 'vue-router'
import Book1 from "@/views/Book1"
import Home from "@/views/Home";
import Book2 from "@/views/Book2";
import Book3 from "@/views/Book3";
import Graph from "@/components/Graph";
import statistics from "@/components/statistics";



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/book1',
    name: 'book1',
    component:Book1
  },
  {
    path: '/book2',
    name: 'book2',
    component:Book2
  },
  {
    path: '/book3',
    name: 'book3',
    component:Book3
  },
  {
    path: '/graph',
    name: 'graph',
    component:Graph
  },
  {
    path: '/sta',
    name: 'sta',
    component:statistics
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
