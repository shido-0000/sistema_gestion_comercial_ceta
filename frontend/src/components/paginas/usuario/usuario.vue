<template>
  <nav class="navbar navbar-dark bg-dark fixed-top" >
    <div class="container-fluid" style="font-family: 'Bahnschrift'">
      <a class="navbar-brand">Menú principal de CETA</a>

      <div class="d-flex justify-content-end align-items-center ">
        <!-- Esto empujará el formulario hacia la derecha -->

        <div class="mt-10"></div>

        <!-- Muestra el nombre del usuario-->
        <div class="text-white mr-3">¡Hola, {{ nombre_para_navbar_usuario }}!</div>
        <!-- Muestra el nombre del usuario recibido de los parámetros de la ruta
        <div v-if="userName" class="text-white mr-3">¡Hola, {{ userName }}!</div>-->

        <!-- Botón de cierre de sesión -->
        <div>
          <button class="btn btn-sm" @click="cerrarSesion" type="submit">
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


            <li class="nav-item dropdown" >
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

                <li><a class="dropdown-item" href="/contrato" v-if="nombre_del_rol_para_navbar === 'Gestor de proyecto' || nombre_del_rol_para_navbar === 'Director de CETA'">
                  <img src="iconos/contratos_40px.png" style="color: white">
                  Contratos
                </a>
                </li>
              </ul>
            </li>


            <li class="nav-item dropdown" v-if="nombre_del_rol_para_navbar === 'Especialista de sistemas' || nombre_del_rol_para_navbar === 'Director de CETA'">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <img src="iconos/Security Lock_40px.png" style="color: white">
                Seguridad
              </a>
              <ul class="dropdown-menu dropdown-menu-dark">
                <li><a class="dropdown-item" href="/rol" v-if="nombre_del_rol_para_navbar === 'Admin'">
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

          </ul>
          <!--<form class="d-flex mt-3" role="search">
            <input class="form-control me-2" type="search" placeholder="Buscar producto" aria-label="Buscar">
            <button class="btn btn-success" type="submit">Buscar</button>
          </form>-->
        </div>
      </div>
    </div>
  </nav>
  <br><br><br>


  <div class="container-md-10" style="margin: 20px;font-family: 'Bahnschrift'">
  <!--<div class="containerPrueba">-->
    <h1>Lista de usuarios</h1>
    <br>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessage">
      Usuario eliminado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageUpdate">
      Usuario modificado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageInsertar">
      Usuario creado con éxito
    </div>

    <br>


    <div class="form-group row" style="align-items: baseline;">
      <div class="col-md-4">
        <label for="filtroNombre">Filtrar por nombre de usuario:</label>
        <input type="text" class="form-control" id="filtroNombre" v-model="filtroNombre" @input="aplicarFiltro">
      </div>
      <div class="col-md-4">
        <label for="filtroRol">Filtrar por Rol:</label>
        <select class="form-control" id="filtroRol" v-model="filtroRol" @change="aplicarFiltro">
          <option value="">Todos</option> <!-- Opción para mostrar todos los roles -->
          <option v-for="rol in lista_rol_aux" :key="rol.id" :value="rol.id">{{ rol.nombre_rol }}</option>
        </select></div>
    </div>

    <table class="table" style="font-family: 'Bahnschrift'">
      <thead>
      <tr>
        <th scope="col" style="font-weight: bold">#</th>
       <!-- <th scope="col" style="font-weight: bold" align="center">Nombre</th>-->
        <th scope="col" style="font-weight: bold" >
          Nombre completo
          <span class="arrow" @click="ordenarPor('nombre_completo')">
              &#8593;&#8595;
            </span>
        </th>
        <th scope="col" style="font-weight: bold" >
          Nombre de usuario
          <span class="arrow" @click="ordenarPor('nombre_usuario')">
              &#8593;&#8595;
            </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center">Rol</th>
      </tr>
      </thead>
      <tbody class="table-group-divider">
      <tr v-for="(item, index) in lista_usuario" :key="index">
        <th scope="row">{{ index + 1 }}</th>
        <td >{{ item.nombre_completo }}</td>
        <td >{{ item.nombre_usuario }}</td>

        <td >{{ obtenerNombreDeRol(item.id_rol_id) }}</td>

        <td>
          <div class="fila">
            <button class="btn btn-icon-text elemento" @click="abrirPopup(item)" type="submit" v-if="nombre_del_rol_para_navbar === 'Especialista de sistemas'">
              <img src="/iconos/Editar_40px.png" alt="Ícono de Modificar usuario"  width="40" height="40">

            </button>

            <div class="espacio"></div> <!-- Espacio entre elementos -->
            <button class="btn btn-icon-text elemento2" @click="eliminar_usuario(item.id)" style="margin-left: 20px;border-color: red; background-color: red" type="submit" v-if="nombre_del_rol_para_navbar === 'Especialista de sistemas'">
              <img src="/iconos/Eliminar_40px.png" alt="Ícono de Eliminar usuario"  width="40" height="40">

            </button>
          </div>
        </td>
      </tr>


      </tbody>
    </table>

    <button class="btn btn-icon-text elemento" @click="abrirPopupInsertar" type="submit" v-if="nombre_del_rol_para_navbar === 'Especialista de sistemas'">
      <img src="/iconos/Nuevo_40px.png" alt="Ícono de Crear nuevo usuario" width="40" height="40">
      Crear nuevo usuario
    </button>

    <!-- Botón para exportar a PDF
    <button class="btn btn-primary elemento" @click="exportarAPDF" type="button">
      Exportar a PDF
    </button>-->

    <div class="popup modal fade show d-block" v-if="mostrarPopup_de_Insertar" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoUsuario">
        <h2>Crear nuevo usuario</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>


        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>

        <div class="alert alert-info" role="alert" v-if="showErrorMessage_de_usuario_existente">
          Ya existe un usuario con ese nombre
        </div>

        <h5>Nombre completo:</h5>
        <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.nombre_completo" required @input="validarNombre(popupItemNuevo)">
        <br>

        <h5>Nombre del usuario:</h5>
        <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.nombre_usuario" required @input="validarNombre(popupItemNuevo)">
        <br>

        <h5>Contraseña:</h5>


        <input type="password" class="form-control" id="validationCustom01" v-model="popupItemNuevo.contrasena" required>
        <br>

        <div>
          <h5>Rol:</h5>
          <select single class="form-control" id="validationCustom01" v-model="popupItemNuevo.selectedRol" required>
           <option v-for="rol in lista_rol_aux" :key="rol.id" :value="rol.id">{{ rol.nombre_rol }}</option>
          </select>
        </div>


        <br>
        <div class="fila">
          <button class="btn btn-icon-text elemento3"   @click="guardar_nuevo_usuario" type="submit">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar" width="40" height="40">
             </button>

          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4"  id="cerrarPopupInsertar" @click="cerrarPopupInsertar">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar" width="40" height="40">

          </button>
        </div>
      </div>
    </div>


    <div class="popup modal fade show d-block" v-if="mostrarPopup" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoUsuario">

        <h2>Modificar usuario</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>
        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>
        <h5>Nombre completo:</h5>
        <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.nombre_completo" required @input="validarNombre(popupItemNuevo)">

        <br>
        <h5>Nombre del usuario:</h5>
        <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.nombre_usuario" required @input="validarNombre(popupItem)">
        <br>
        <div>
          <h5>Lista de roles:</h5>
          <select single class="form-control" id="validationCustom01" v-model="this.popupItem.selectedRol" required>
            <option v-for="rol in lista_rol_aux" :key="rol.id" :value="rol.id">{{ rol.nombre_rol }}</option>
          </select>
        </div>

        <div class="fila">
          <button class="btn btn-icon-text elemento3" @click="guardarCambios" type="submit">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar" width="40" height="40">

          </button>
          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4" id="cerrarPopup" @click="cerrarPopup">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar" width="40" height="40">

          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
//import crypto from 'crypto'; // Importa la biblioteca crypto
import bcrypt from 'bcryptjs'; // Importa la biblioteca bcryptjs
//import jsPDF from 'jspdf';
//import 'jspdf-autotable';
//import {it} from "vuetify/locale";

export default {
  data() {
    return {
      lista_usuario: [], // Array para almacenar los datos de la API
      showSuccessMessage: false,
      showSuccessMessageUpdate: false,
      popupItem: null,
      popupItemNuevo: null,
      showErrorMessage: false,
      showSuccessMessageInsertar:false,
      mostrarPopup: false, // Variable para controlar la visibilidad del pop-up
      mostrarPopup_de_Insertar: false, // Variable para controlar la visibilidad del pop-up
      lista_rol_aux: [], //variable utilizada para guardar todos los roles y recorrerlos
      selectedRol: null, // Esta propiedad rastreará los IDs de los roles seleccionados

      showErrorMessage_de_caracter_no_permitido: false,
      showErrorMessage_de_usuario_existente: false,

      ////para ordenar
      columnaOrden: "", // Columna utilizada para el orden
      ordenAsc: true, // Dirección del orden


      /////para filtrar
      lista_usuario_original: [], // Lista original de usuarios
      filtroNombre: "", // Valor del filtro por nombre
      filtroRol: null, // Nueva propiedad para el filtro por rol
      quitarFiltros: false, // Estado del checkbox "Quitar Filtros"


      //datos del usuario autenticado
      nombre_para_navbar_usuario: "", // Inicializa el nombre de usuario
      usuario_para_navbar_autenticado:"",
      lista_para_navbar_usuario: [],
      lista_para_navbar_rol: [],
      nombre_del_rol_para_navbar: "",
    };

  },

  // estos metodos se ejecutan automaticamente cuando la pagina este cargada
  mounted() {
    this.obtenerUsuarios();
    this.obtenerListaRoles();

    // Recupera el nombre de usuario de localStorage
    this.nombre_para_navbar_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRolParaElNavBar();
  },

  methods: {
    obtenerUsuarios() {
      axios.get('http://127.0.0.1:8000/api/usuarios/0')
          .then(response => {

           // this.lista_usuario = response.data["usuarios"];
            this.lista_usuario_original = response.data["usuarios"];
            this.lista_usuario = [...this.lista_usuario_original]; // Copia la lista original a la lista filtrada

            //  console.log(response)
          })
          .catch(error => {
            console.error(error);
          });
    },
    eliminar_usuario(id) {
      const url = `http://127.0.0.1:8000/api/usuarios/delete/${id}`;
      axios.delete(url)
          .then(response => {
            this.obtenerUsuarios();

            // mostrar mensaje flotante
            // Mostrar mensaje de éxito
            this.showSuccessMessage = true; // Mostrar mensaje de éxito
            setTimeout(() => {
              this.showSuccessMessage = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },

    guardarCambios() {

      if (!this.popupItem) {
        // Si popupItem es undefined, muestra un mensaje de error o maneja la situación de manera apropiada
        return;
      }
      if (
          !this.popupItem.nombre_completo || this.popupItem.nombre_completo.trim()===''||
          !this.popupItem.nombre_usuario ||
          this.popupItem.nombre_usuario.trim() === '' ||
          !this.popupItem.contrasena ||
          this.popupItem.contrasena.trim() === '' ||
          !this.popupItem.selectedRol ||
          this.popupItem.selectedRol === null
      ) {
        // Mostrar un mensaje de error al usuario indicando que los campos son obligatorios
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      const url = `http://127.0.0.1:8000/api/usuarios/put/${this.popupItem.id}`;
      const payload = {
        nombre_completo: this.popupItem.nombre_completo,
        nombre_usuario: this.popupItem.nombre_usuario,
        contrasena: this.popupItem.contrasena,
        id_rol: this.popupItem.selectedRol
        // Otros campos a modificar si es necesario
      };

      axios.put(url, payload)
          .then(response => {
            this.obtenerUsuarios(); // Actualizar la tabla si es necesario
            this.cerrarPopup(); // Cerrar el popup después de guardar los cambios
            this.showErrorMessage = false; // Ocultar mensaje de error

            this.showSuccessMessageUpdate = true; // Mostrar mensaje de éxito
            setTimeout(() => {
              this.showSuccessMessageUpdate = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },


    async guardar_nuevo_usuario() {

      if (!this.popupItemNuevo) {
        // Si popupItemNuevo es undefined, muestra un mensaje de error o maneja la situación de manera apropiada
        return;
      }
      if (!this.popupItemNuevo.nombre_completo || this.popupItemNuevo.nombre_completo.trim()===''||
          !this.popupItemNuevo.nombre_usuario ||
          this.popupItemNuevo.nombre_usuario.trim() === '' ||
          !this.popupItemNuevo.contrasena ||
          this.popupItemNuevo.contrasena.trim() === '' ||
          !this.popupItemNuevo.selectedRol ||
          this.popupItemNuevo.selectedRol === null
      ) {
        // Mostrar un mensaje de error al usuario indicando que los campos son obligatorios
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      if (this.existe_ese_usuario(this.popupItemNuevo.nombre_usuario) === true) {
        // Mostrar un mensaje de error
        this.showErrorMessage_de_usuario_existente = true;
        setTimeout(() => {
          this.showErrorMessage_de_usuario_existente = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      } else {

        const url = 'http://127.0.0.1:8000/api/usuarios/post/';

        // Cifra la contraseña con bcrypt
        const saltRounds = 10; // Número de rondas de sal
        const contrasenaCifrada = await bcrypt.hash(this.popupItemNuevo.contrasena, saltRounds);

        const payload = {
          nombre_completo: this.popupItemNuevo.nombre_completo,
          nombre_usuario: this.popupItemNuevo.nombre_usuario,
          contrasena: contrasenaCifrada,
          id_rol: this.popupItemNuevo.selectedRol, // Enviar solo el ID del rol
        };


        axios.post(url, payload)
            .then(response => {
              this.popupItemNuevo.nombre_completo='';
              this.popupItemNuevo.nombre_usuario = ''; // Limpiar el campo de texto
              this.popupItemNuevo.contrasena = ''; // Limpiar el campo de texto
              this.popupItemNuevo.selectedRol = null; // Limpiar el campo de texto
              this.showSuccessMessageInsertar = true; // Mostrar mensaje de éxito
              this.showErrorMessage = false; // Ocultar mensaje de error

              this.obtenerUsuarios(); // Actualizar la tabla si es necesario
              this.cerrarPopupInsertar(); // Cerrar el popup después de insertar

              setTimeout(() => {
                this.showSuccessMessageInsertar = false; // Ocultar mensaje de éxito después de unos segundos
              }, 3000);
            })
            .catch(error => {
              console.error(error);
            });
      }
    },

    //cargamos la lista de roles desde la llamada a la API
    obtenerListaRoles() {
      axios.get('http://127.0.0.1:8000/api/roles/0')
          .then(response => {
            //  console.log(response);
            this.lista_rol_aux = response.data["roles"];
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreDeRol(id_rol) {

      if (this.lista_rol_aux.length > 0) {
        const rolId = parseInt(id_rol); // Asegurarse de que id_rol sea un número
        const roles = this.lista_rol_aux.find(p => p.id === rolId);

        if (roles) {
          return roles.nombre_rol;
        }
      }
      return 'Rol no encontrado';
    },


    ///////////////// funcion filtrar

    /*filtrarUsuarios() {
      // Filtrar la lista de usuarios en función de los valores de filtro
      this.lista_usuario = this.lista_usuario_original.filter((usuario) => {
        const nombreMatch =
            usuario.nombre_usuario.toLowerCase().includes(this.filtro.nombre_usuario.toLowerCase()) ||
            this.filtro.nombre_usuario.trim() === "";

        const rolMatch =
            usuario.id_rol_id === this.filtro.id_rol || this.filtro.id_rol === "";

        return nombreMatch && rolMatch;
      });
    },*/


///////////// funcione para validar
    //////////validar nombre

    validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-ZÁáÉéÍíÓóÚúÜü\s]*$/;

      if (!regex.test(item.nombre_completo)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.nombre_completo = item.nombre_completo.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }

      if (!regex.test(item.nombre_usuario)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.nombre_usuario = item.nombre_usuario.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
    },


    ///////////////validar si es usuario existe

    existe_ese_usuario(nombre) {
      const usuario = this.lista_usuario.find(p => p.nombre_usuario === nombre);

      if (usuario != null) {
        this.showErrorMessage_de_usuario_existente = true;
      } else {
        this.showErrorMessage_de_usuario_existente = false;
      }
      return this.showErrorMessage_de_usuario_existente;
    },

    /////// funcion ordenar

    // Método para cambiar la columna de orden y la dirección
    ordenarPor(columna) {
      if (this.columnaOrden === columna) {
        this.ordenAsc = !this.ordenAsc; // Cambiar la dirección si se hace clic en la misma columna
      } else {
        this.columnaOrden = columna; // Cambiar la columna de orden
        this.ordenAsc = true; // Restablecer la dirección a ascendente
      }

      // Lógica de ordenamiento aquí
      this.lista_usuario.sort((a, b) => {
        const factor = this.ordenAsc ? 1 : -1;
        const valorA = a[columna];
        const valorB = b[columna];
        return valorA.localeCompare(valorB) * factor;
      });
    },

    //////////////////////// filtrar



    aplicarFiltro() {
      if (this.quitarFiltros) {
        // Si el checkbox está marcado, restaura la lista original
        this.lista_usuario = [...this.lista_usuario_original];
      } else {
        // Aplica el filtro por nombre
        const filteredList = this.lista_usuario_original.filter(usuario => {
          const nombreMatch = (!this.filtroNombre || usuario.nombre_usuario.includes(this.filtroNombre));
          const rolMatch = (!this.filtroRol || usuario.id_rol_id === this.filtroRol);
          return nombreMatch && rolMatch;
        });

        this.lista_usuario = filteredList;
      }
    },


    limpiarFiltros() {
      if (this.quitarFiltros) {
        // Si el checkbox está marcado, restaura la tabla original
        this.lista_usuario = [...this.lista_usuario_original];
        this.filtroNombre = ""; // Limpia el filtro por nombre
      }
    },

    //// para cerrar sesion
    cerrarSesion() {
      // Aquí puedes agregar la lógica para cerrar la sesión del usuario.
      // Elimina el nombre de usuario almacenado en localStorage
      localStorage.removeItem('nombre_usuario');
      // Por ejemplo, redirigir al usuario a la página de inicio de sesión:
      this.$router.push('/'); // Cambia la ruta según tus necesidades
    },

    // obtener nombre del rol del usuario que accedio al sitio para usar en e navBar
    obtenerNombreDeRolParaElNavBar() {
      //cargamos la lista de usuarios desde la llamada a la API
      axios.get('http://127.0.0.1:8000/api/usuarios/0')
          .then(response => {

            this.lista_para_navbar_usuario = response.data["usuarios"];
            this.usuario_para_navbar_autenticado = this.lista_para_navbar_usuario.find(p => p.nombre_usuario === this.nombre_para_navbar_usuario);
            // console.log(this.usuario_autenticado)

            //cargamos la lista de roles desde la llamada a la API
            axios.get('http://127.0.0.1:8000/api/roles/0')
                .then(response => {
                  // console.log(response);
                  this.lista_para_navbar_rol= response.data["roles"];
                  console.log(this.lista_para_navbar_rol.length);

                  console.log(this.usuario_para_navbar_autenticado)
                  if (this.lista_para_navbar_rol.length > 0) {
                    const id_rol_del_usuario_autenticado = this.usuario_para_navbar_autenticado.id_rol_id;
                    const rolId = parseInt(id_rol_del_usuario_autenticado);
                    const rol = this.lista_para_navbar_rol.find(p => p.id === rolId);
                    if (rol) {
                      // Almacena el nombre del rol en una propiedad de datos
                      this.nombre_del_rol_para_navbar = rol.nombre_rol;
                      localStorage.setItem('nombre_rol', this.nombre_del_rol_para_navbar);
                      console.log(this.nombre_del_rol_para_navbar );
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


    /////////////////// exportar

   /* exportarAPDF() {
      const doc = new jsPDF();
      const tableData = this.lista_usuario.map((item, index) => {
        return [
          index + 1,
          item.nombre_usuario,
          item.contrasena,
          this.obtenerNombreDeRol(item.id_rol_id),
        ];
      });
      const tableColumns = ['#', 'Nombre', 'Contraseña', 'Rol'];

      doc.autoTable({
        head: [tableColumns],
        body: tableData,
        theme: 'striped',
      });

      doc.save('usuarios.pdf');
    },
*/


    abrirPopup(item) {
      this.popupItem = JSON.parse(JSON.stringify(item));
      this.mostrarPopup = true;
    },

    abrirPopupInsertar(item) {
      this.popupItemNuevo = JSON.parse(JSON.stringify(item));
      this.mostrarPopup_de_Insertar = true;
    },

    cerrarPopup() {
      this.popupItem = null;
      this.mostrarPopup = false;
    },

    cerrarPopupInsertar() {
      this.popupItemNuevo = null;
      this.mostrarPopup_de_Insertar = false;
    },
  }
};
</script>


<style>
.fila {
  display: inline-flex;
  align-items: center;
}

.elemento {
  margin-right: 1px;
}

.elemento2 {
  margin-left: 1px;
}

.elemento3 {
  margin-left: -10px;
  margin-top: auto;
}

.elemento4 {
  margin-left: 30px;

}

.espacio {
  flex-grow: 1;
}

.popup {
  display: none;
  position: fixed;
  top: 0%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.popup-contenidoUsuario {
  background-color: #fff;
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  text-align: center;
  border-radius: 10px; /* Borde redondeado */

  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#cerrarPopup {
  margin-top: 10px;
}


.botones {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.containerPrueba{
  display: inline-block;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  top: 5%;
  left: 50%;
  right: 50%;
}

/* Agrega esta clase personalizada para el cuadro de texto de filtrar nombre */
.custom-filter-input {
  max-width: 200px; /* Ajusta el ancho máximo según tus preferencias */
}

/*para la funcion ordenar*/
.arrow {
  font-size: 24px; /* Aumenta el tamaño a 16px (puedes ajustarlo según tus preferencias) */
  color: #007bff;
  cursor: pointer;
}

.arrow:hover {
  color: #0056b3; /* Cambia el color al pasar el mouse por encima */
}


/* Establece el fondo de los botones a transparente y elimina el borde */

/*Hemos establecido la clase btn-icon-text en ambos botones para aplicar los estilos.
Usamos background-color: transparent !important; para hacer el fondo del botón transparente.
Usamos border: none !important; para eliminar el borde del botón.
Establecemos padding: 0; para eliminar el relleno del botón y acercar el contenido (ícono y texto) al borde.
Usamos vertical-align: middle; y margin-right: 8px; en el ícono para alinear verticalmente el contenido y agregar un espacio entre el ícono y el texto.*/

.btn-icon-text {
  background-color: transparent !important;
  border: none !important;
  padding: 0; /* Elimina el relleno para que el contenido esté más cerca del borde */
}

/* Alinea el contenido (ícono y texto) verticalmente */
.btn-icon-text img {
  vertical-align: middle;
  margin-right: 2px; /* Espacio entre el ícono y el texto */
}
</style>