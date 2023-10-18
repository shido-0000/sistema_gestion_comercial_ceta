<template>
  <div>
  <!-- Verificar si el usuario está autenticado antes de mostrar el contenido -->
  <div v-if="usuarioAutenticado">
  <nav class="navbar navbar-dark bg-dark fixed-top" >
  <div class="container-fluid" style="font-family: 'Bahnschrift'">
    <a class="navbar-brand">Menú principal de CETA</a>

    <div class="d-flex justify-content-end align-items-center ">
      <!-- Esto empujará el formulario hacia la derecha -->
        <div class="mt-10"></div>
      <!-- Muestra el nombre del usuario-->
      <div class="text-white mr-3" style="margin-left: 900px">¡Hola, {{ nombre_usuario }}! </div>
      <!-- Botón de cierre de sesión -->
      <div>
      <button class="btn btn-sm" @click="cerrarSesion" type="submit" >
        <img src="/iconos/cerrar_sesion_48px.png" alt="Icono de Cerrar Sesión" width="42" height="42">
      </button>
    </div>

    </div>
    <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
      <div class="offcanvas-header">
        <img src="iconos/opciones2_40px.png" style="color: white">
        <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">Opciones</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
      </div>
      <div class="offcanvas-body">



        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="http://localhost:5173/inicio">
              <img src="iconos/inicio_40px.png">
              Inicio
            </a>
          </li>


          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="iconos/economia7_40px.png" style="color: white">
              Economía
            </a>
            <ul class="dropdown-menu dropdown-menu-dark">
              <li><a class="dropdown-item" href="/area_participante">
                <img src="iconos/area_participante_40px.png" style="color: white">
                Área participante
              </a>
              </li>

              <li><a class="dropdown-item" href="/contrato" v-if="nombre_del_rol === 'Gestor de proyecto' || nombre_del_rol === 'Director de CETA'">
                <img src="iconos/contratos_40px.png" style="color: white">
                Contratos
              </a>
              </li>
            </ul>
          </li>


          <li class="nav-item dropdown" v-if="nombre_del_rol === 'Especialista de sistemas' || nombre_del_rol === 'Director de CETA'">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="iconos/Security Lock_40px.png" style="color: white">
              Seguridad
            </a>
            <ul class="dropdown-menu dropdown-menu-dark" >
              <li><a class="dropdown-item" href="/rol" v-if="nombre_del_rol === 'Admin'">
              <img src="iconos/roles_40px.png" style="color: white">
              Roles
              </a>
              </li>

              <li><a class="dropdown-item" href="/usuario">
                <img src="iconos/usuarios_40px.png" style="color: white">
                Usuarios
              </a>
              </li>
            </ul>
          </li>

          <li class="nav-item dropdown" >
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="iconos/Recursos_humanos_40px.png" style="color: white">
              Recursos Humanos
            </a>
            <ul class="dropdown-menu dropdown-menu-dark">
              <li><a class="dropdown-item" href="/trabajador">
                <img src="iconos/trabajadores_40px.png" style="color: white">
                Trabajadores
              </a>
              </li>



              <li><a class="dropdown-item" href="/categorias_de_profesores_del_servicio">
                <img src="iconos/trabajadores_40px.png" style="color: white">
                Categorías de profesores de los servicios
              </a>
              </li>

              <li><a class="dropdown-item" href="/programa_de_cobro">
                <img src="iconos/programa_de_cobro_40px.png" style="color: white">
                Programas de cobro
              </a>
              </li>

              <li><a class="dropdown-item" href="/planificacion_de_gastos_personales">
                <img src="iconos/planificacio_gastos_personales_40px.png" style="color: white">
                Planificación de gastos personales
              </a>
              </li>

              <li><a class="dropdown-item" href="/plazos">
                <img src="iconos/plazos_40px.png" style="color: white">
                Plazos
              </a>
              </li>

              <li><a class="dropdown-item" href="/norma">
                <img src="iconos/normas40px.png" style="color: white">
                Normas
              </a>
              </li>
            </ul>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="iconos/servicios_40px.png">
              Servicios
            </a>
            <ul class="dropdown-menu dropdown-menu-dark">
              <li><a class="dropdown-item" href="/servicios">Ver servicios existentes</a></li>
            </ul>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <img src="iconos/servicios_40px.png">
              Datos para la ficha técnica
            </a>


            <ul class="dropdown-menu dropdown-menu-dark">
              <li><a class="dropdown-item" href="/tareas_detalladas">Tareas detalladas</a></li>
              <li><a class="dropdown-item" href="/recursos_necesarios">Recursos necesarios</a></li>
              <li><a class="dropdown-item" href="/productos_necesarios">Productos necesarios</a></li>
              <li><a class="dropdown-item" href="/encuetros_por_semana">Encuetros por semana</a></li>
              <li><a class="dropdown-item" href="/resultados_para_ficha_tecnica">Resultados para la ficha técnica</a></li>
              <li><a class="dropdown-item" href="/resultados_obtenidos_para_ficha_tecnica">Resultados obtenidos para la ficha técnica</a></li>
              <li><a class="dropdown-item" href="/control_de_documentos_del_contrato">Control de documentos del contrato</a></li>
              <li><a class="dropdown-item" href="/consideraciones_para_la_ficha_tecnica">Consideraciones para la ficha técnica</a></li>
              <li><a class="dropdown-item" href="/valor_del_contrato_por_los_servicios_comercializados">Valor de los contratos por los servicios comercializados</a></li>
              <li><a class="dropdown-item" href="/pagos_al_cliente">Pagos al cliente</a></li>
              <li><a class="dropdown-item" href="/facturacion_pagos">Facturación pagos</a></li>

              <li><a class="dropdown-item" href="/cronograma_para_ficha_tecnica">Cronograma para ficha técnica</a></li>
              <li><a class="dropdown-item" href="/areas_y_trabajdores_para_la_ficha_tecnica">Áreas y trabajadores para la ficha técnica</a></li>
              <li><a class="dropdown-item" href="/registros_de_derechos_y_propiedad">Registros de derechos y propiedad</a></li>

            </ul>
          </li>

        </ul>
        <!--<form class="d-flex mt-3" role="search">
          <input class="form-control me-2" type="search" placeholder="Buscar producto" aria-label="Buscar">
          <button class="btn btn-success" type="submit">Buscar</button>
        </form>-->
      </div>
    </div>
  </div>
</nav>

    <div class="fullscreen-bg1"></div>

    <div style="z-index: 999">
      <h1>
        Bienvenido a CETA.SA
      </h1>
    </div>

  </div>

    
  <div v-else align="center">
    <p>Debe iniciar sesión para acceder a esta página.</p>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import bcrypt from 'bcryptjs';



export default {

  data() {
    return {
      nombre_usuario: "", // Inicializa el nombre de usuario
      usuario_autenticado:"",
      lista_usuario: [],
      lista_rol: [],
      nombre_del_rol: "",

    };
  },
  created() {
    // Recupera el nombre de usuario de localStorage
    this.nombre_usuario = localStorage.getItem('nombre_usuario');

    // Verifica si el nombre de usuario no está presente y redirige al inicio de sesión
    if (!this.nombre_usuario) {
      this.$router.push('/');
    }
  },

  mounted() {
    // Recupera el nombre de usuario de localStorage
    this.nombre_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRol();

    // Verifica si el nombre de usuario no está presente y redirige al inicio de sesión
    if (!this.nombre_usuario) {
      this.$router.push('/');
    }
  },

  computed: {
    usuarioAutenticado() {
      // Verificar si el usuario está autenticado (por ejemplo, si el nombre de usuario está en localStorage)
      return !!localStorage.getItem('nombre_usuario');
    },
  },

  methods: {
    cerrarSesion() {
      // Aquí puedes agregar la lógica para cerrar la sesión del usuario.
      // Elimina el nombre de usuario almacenado en localStorage
      localStorage.removeItem('nombre_usuario');
      // Por ejemplo, redirigir al usuario a la página de inicio de sesión:
      this.$router.push('/'); // Cambia la ruta según tus necesidades
    },

    obtenerNombreDeRol() {
      //cargamos la lista de usuarios desde la llamada a la API
      axios.get('http://127.0.0.1:8000/api/usuarios/0')
          .then(response => {

             this.lista_usuario = response.data["usuarios"];
             this.usuario_autenticado = this.lista_usuario.find(p => p.nombre_usuario === this.nombre_usuario);
            // console.log(this.usuario_autenticado)

            //cargamos la lista de roles desde la llamada a la API
            axios.get('http://127.0.0.1:8000/api/roles/0')
                .then(response => {
                  // console.log(response);
                  this.lista_rol= response.data["roles"];
                  console.log(this.lista_rol.length);

                  console.log(this.usuario_autenticado)
                  if (this.lista_rol.length > 0) {
                    const id_rol_del_usuario_autenticado = this.usuario_autenticado.id_rol_id;
                    const rolId = parseInt(id_rol_del_usuario_autenticado);
                    const rol = this.lista_rol.find(p => p.id === rolId);
                    if (rol) {
                      // Almacena el nombre del rol en una propiedad de datos
                      this.nombre_del_rol = rol.nombre_rol;
                      localStorage.setItem('nombre_rol', this.nombre_del_rol);
                      console.log(this.nombre_del_rol );
                    }
                  }

                })
                .catch(error => {
                  console.error(error);
                });
          })
          .catch(error => {
            console.error(error);
          });
    },
    // Otros métodos...
  },
};
</script>


<style>
.fullscreen-bg1 {
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

</style>



