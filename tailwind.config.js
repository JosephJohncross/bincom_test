/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './food_stores/static/js/*.js',
    './templates/*.html', 
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
