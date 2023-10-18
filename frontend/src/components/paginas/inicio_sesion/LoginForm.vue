<template>
  <div class="fullscreen-bg">
    <div class="row justify-content-center align-items-center vh-100" style="font-family: 'Bahnschrift'">
      <div class="col-md-3"> <!-- Modifica el ancho del formulario -->
        <div class="card card-shadow"> <!-- Agregamos una clase para la sombra -->
          <div class="card-header bg-primary text-white">Inicio de Sesión</div> <!-- Cambiamos el color de fondo y texto -->
          <div class="card-body">
            <form>
              <div class="mb-2 d-flex align-items-center input-line">
                <label for="username" class="form-label" style="padding-right: 20px; padding-left: 10px;">
                  <img src="/iconos/usuario.png" alt="usuario" width="40" height="40">
                </label>
                <input type="text" class="form-control no-border" id="username" v-model="username" placeholder="Escribir usuario">
              </div>
              <div class="mb-1 d-flex align-items-center">
                <label for="password" class="form-label" style="padding-right: 10px; padding-left: 10px;">
                  <img src="/iconos/contrasena.png" alt="contraseña" width="50" height="50">
                </label>
                <input type="password" class="form-control" id="password" v-model="password" placeholder="Escribir contraseña">
              </div>

              <br>
              <div class="text-center"> <!-- Centra el botón horizontalmente -->
                <button type="button" class="btn btn-primary btn-rounded" style="border-radius: 50px" @click="login">Iniciar Sesión</button>
              </div>
            </form>
            <!-- Agrega un div para mostrar el mensaje de error -->
            <div v-if="showErrorMessage" class="alert alert-danger mt-3">{{ error }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import bcrypt from 'bcryptjs';
import {ref} from "vue";
const isLoggedIn = ref(false); // Inicialmente, el usuario no está autenticado


export default {
  data() {
    return {
      username: "",
      password: "",
      error: "", // Agrega una propiedad para almacenar el mensaje de error
      showErrorMessage: false,
    };
  },
  methods: {
    async login(event) {
      event.preventDefault();
      this.error = ""; // Reinicia el mensaje de error al intentar iniciar sesión nuevamente

      axios
          .post("http://127.0.0.1:8000/api/login/", {
            username: this.username,
            password: this.password
          })
          .then(response => {
            if (response.data.message === 'Inicio de sesión exitoso') {

              // Almacenar el nombre de usuario en localStorage
              localStorage.setItem('nombre_usuario', response.data.usuario.nombre_usuario);

              // Redirigir a la página de inicio
              isLoggedIn.value = true;
              this.$router.push({ name: 'Inicio' });
            } else {
              this.error = "Credenciales incorrectas"; // Establece el mensaje de error
            }
          })
          .catch(error => {
            console.error("Error al iniciar sesión", error);
            this.showErrorMessage = true;
            this.error = "Error, usuario o contraseña incorrectas"; // Establece el mensaje de error en caso de error de red u otro error
            setTimeout(() => {
              this.showErrorMessage = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          });
    }
  }
};
</script>

<style>
.fullscreen-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%; /* Aumenta la altura para alargar el fondo */
  overflow: hidden;
  background-image: url('/iconos/imagen.webp'); /* Cambia '/iconos/imagen.webp' a la ruta de tu imagen de fondo */
  background-size: cover;
  background-repeat: no-repeat;
}

/* Estilo para los bordes ovalados del botón y estirar el botón */
.btn-rounded {
  border-radius: 80px;
  width: 100%; /* Estira el botón hasta el borde del formulario */
}

/* Estilo para la sombra del formulario */
.card-shadow {
 /* box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3); /* Cambia el valor para ajustar la sombra según tus preferencias */
  box-shadow: 0px 0px 20px rgba(0, 0, 0, 1);
  background-color: #fff; /* Cambia el color de fondo del formulario */
}

/* Cambia el color del texto del botón si es necesario */
.btn-primary {
  background-color: #007bff; /* Cambia el color de fondo del botón */
  color: #fff; /* Cambia el color del texto del botón si es necesario */
}

/* Estilo para quitar los bordes de las cajas de entrada */
.no-border {
  border: none;
  outline: none;
  background: transparent;
  border-bottom: 1px solid #ccc; /* Línea inferior de las cajas de entrada */
  padding: 3px; /* Espaciado adicional para las cajas de entrada */
}

/* Estilo para las líneas de entrada */
.input-line {
  margin-bottom: 10px; /* Espacio entre las líneas */
}
</style>
