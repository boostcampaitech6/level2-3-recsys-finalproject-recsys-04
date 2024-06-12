// /** @type {import('tailwindcss').Config} */
// export default {
//   content: [
//     "./index.html",
//     "./src/**/*.{vue,js,ts,jsx,tsx}",
//   ],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./index.html","./src/**/*.{vue,js,ts,jsx,tsx}",],// tailwind를 사용하는 모든 페이지와 컴포넌트
  darkMode: 'class', //,false
  theme: {
    extend:{},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};