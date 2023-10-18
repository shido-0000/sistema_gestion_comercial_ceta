

import { createApp } from 'vue'
import App from './App.vue'
import router from './components/router'

/*import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'*/
import 'bootstrap/dist/css/bootstrap.css'



// Vuetify
/*import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
})

createApp(App).use(vuetify).mount('#app')*/

const app = createApp(App)
app.use(router)
app.mount('#app')
