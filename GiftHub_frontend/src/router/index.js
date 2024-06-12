import { createWebHistory, createRouter } from "vue-router";
import Main from "@/views/MainView.vue";
import Gender from "@/views/GenderView.vue";
import Age from "@/views/AgeView.vue";
import Color from "@/views/ColorView.vue";
import Price from "@/views/PriceView.vue";
import Inference from "@/views/InferenceView.vue";
import Situation from "@/views/SituationView.vue";
import Test from "@/views/test.vue";
import Design from "@/views/DesignTest.vue";
const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/gender",
    name: "Gender",
    component: Gender,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/age",
    name: "Age",
    component: Age,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/color",
    name: "Color",
    component: Color,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/color",
    name: "Color",
    component: Color,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/price",
    name: "Price",
    component: Price,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/situation",
    name: "Situation",
    component: Situation,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/inference",
    name: "Inference",
    component: Inference,
    meta: {
      title: 'GiftHub'
    }
  },
  {
    path: "/test",
    name: "Test",
    component: Test,
  },
  {
    path: "/design",
    name: "DesignTest",
    component: Design,
  },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Test';
  next();
});

export default router;