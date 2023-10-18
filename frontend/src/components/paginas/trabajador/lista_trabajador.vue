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


  <div class="container-md-10" style="margin: 20px;">
<!--  <div class="containerPrueba">-->
    <h1>Lista de trabajadores</h1>
    <br>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessage">
      Trabajador eliminado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageUpdate">
      Trabajador modificado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageInsertar">
      Trabajador creado con éxito
    </div>

    <div class="form-group row" style="align-items: baseline;">
      <div class="col-md-4">
        <label for="filtroNombre">Filtrar por Nombre:</label>
        <input type="text" class="form-control" id="filtroNombre" v-model="filtroNombre" @input="aplicarFiltro">
      </div>

    </div>


    <br>

    <table class="table" style="font-family: 'Bahnschrift'">
      <thead>
      <tr>
        <th  style="font-weight: bold" >#</th>
        <th  style="font-weight: bold" >ID</th>
        <!--<th scope="col" style="font-weight: bold" align="center">Nombre</th>-->
        <th  style="font-weight: bold"  id="nombre">
          Nombre
          <span class="arrow" @click="ordenarPor('fields.nombre')">
            &#8593;&#8595;
          </span>
        </th>
        <th  style="font-weight: bold">Listado de plazos</th>

        <th  style="font-weight: bold" id="categoria">
          Categoría
          <span class="arrow" @click="ordenarPor('fields.id_categoria_del_profesor_del_servicio')">
            &#8593;&#8595;
          </span>
        </th>
      </tr>
      </thead>
      <tbody class="table-group-divider">
      <tr v-for="(item, index) in lista_trabajadores" :key="index">
        <th scope="row">{{ index + 1 }}</th>
        <td >{{ item.pk }}</td>
        <td >{{ item.fields.nombre }}</td>
         <td >
          <ul>
            <li v-for="id_plazo in item.fields.lista_plazo" >{{ obtenerNombrePlazo(id_plazo) }}</li>
          </ul>
        </td>
        <td >{{ obtener_nombre_categoria(item.fields.id_categoria_del_profesor_del_servicio) }}</td>



        <td>
          <div class="fila">
            <!--  <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>
              <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>-->
            <button class="btn btn-icon-text elemento" @click="abrirPopup(item)" type="submit">
              <img src="/iconos/Editar_40px.png" alt="Ícono de Modificar" width="40" height="40">
              <!--   Modificar-->
              </button>

              <div class="espacio"></div> <!-- Espacio entre elementos -->
            <button class="btn btn-icon-text elemento2" @click="eliminar_trabajadores(item.pk)" style="margin-left: 20px;border-color: red; background-color: red" type="submit">
              <img src="/iconos/Eliminar_40px.png" alt="Ícono de Eliminar" width="40" height="40">
              <!--   Eliminar-->
             </button>
           </div>
         </td>
       </tr>


       </tbody>
     </table>

     <button class="btn btn-icon-text elemento" @click="abrirPopupInsertar" type="submit" style="font-family: 'Bahnschrift'">
       <img src="/iconos/Nuevo_40px.png" alt="Ícono de Crear nuevo" width="40" height="40">
       Crear nuevo trabajador
     </button>

     <div class="popup modal fade show d-block" v-if="mostrarPopup_de_Insertar" style="font-family: 'Bahnschrift'">
       <div class="popup-contenidoTrabajador">
         <h2>Crear nuevo trabajador</h2>
         <br>

         <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
           Error, carácter no permitido
         </div>


         <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
           Error, faltan campos por llenar
         </div>

         <h5>ID del trabajador:</h5>

         <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.id_trabajador" required>
         <br>
         <h5>Nombre del trabajador:</h5>


         <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.nombre" required @input="validarNombre(popupItemNuevo)">
         <br>
         <h5>Categoría del trabajador:</h5>
         <select single class="form-control" id="validationCustom01" v-model="popupItemNuevo.id_categoria_del_profesor_del_servicio" required>
           <option v-for="categoria in lista_categoria_aux" :key="categoria.pk" :value="categoria.pk">{{ categoria.fields.nombre_categoria }}</option>
         </select>
         <br>
         <div>
           <h5>Lista de plazos:</h5>
           <select multiple class="form-control" id="validationCustom01" v-model="selectedPlazos" required>
             <option v-for="plazo in lista_plazos_aux" :key="plazo.id" :value="plazo.id">{{ plazo.nombre_plazo }}</option>
           </select>
         </div>


         <br>
         <div class="fila">
           <button class="btn btn-icon-text elemento3" @click="guardar_nuevo_trabajador" type="submit">
             <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar" width="44" height="44">
           <!--  Crear nuevo-->
           </button>
           <div class="espacio"></div>
           <button class="btn btn-icon-text elemento4" id="cerrarPopupInsertar" @click="cerrarPopupInsertar">
             <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar" width="40" height="40">
             <!--  Cancelar-->
            </button>
          </div>
        </div>
      </div>

      <!-- <div class="popup" v-if="popupItem">-->
    <div class="popup modal fade show d-block" v-if="mostrarPopup">
      <div class="popup-contenidoTrabajador">

        <h2>Modificar trabajador</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>
        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>
   <!--    <h5>ID del trabajador:</h5>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>

        <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.id_trabajador" required>-->
        <br>
        <h5>Nombre del trabajador:</h5>
        <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.fields.nombre" required @input="validarNombre(popupItem)">
        <br>
        <h5>Categoría del trabajador:</h5>
        <select single class="form-control" id="validationCustom01" v-model="popupItem.fields.id_categoria_del_profesor_del_servicio" required>
          <option v-for="categoria in lista_categoria_aux" :key="categoria.pk" :value="categoria.pk">{{ categoria.fields.nombre_categoria }}</option>
        </select>
        <br>
        <div>
          <h5>Lista de plazos:</h5>
          <select multiple class="form-control" id="validationCustom01" v-model="selectedPlazos" required>
            <option v-for="plazo in lista_plazos_aux" :key="plazo.id" :value="plazo.id">{{ plazo.nombre_plazo }}</option>
          </select>
        </div>

        <div class="fila">
          <button class="btn btn-icon-text elemento3" @click="guardarCambios" type="submit">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar" width="40" height="40">
            Modificar
          </button>
          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4" id="cerrarPopup" @click="cerrarPopup">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar" width="40" height="40">
            Cancelar
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
//import {it} from "vuetify/locale";

export default {
  data() {
    return {
      lista_trabajadores: [], // Array para almacenar los datos de la API
      showSuccessMessage: false,
      showSuccessMessageUpdate: false,
      popupItem: null,
      popupItemNuevo: null,
      showErrorMessage: false,
      showSuccessMessageInsertar:false,
      mostrarPopup: false, // Variable para controlar la visibilidad del pop-up
      mostrarPopup_de_Insertar: false, // Variable para controlar la visibilidad del pop-up

      lista_plazos_aux: [], //variable utilizada para guardar todos los plazos y recorrerlos
      selectedPlazos: [], // Esta propiedad rastreará los IDs de los plazos seleccionados

      showErrorMessage_de_caracter_no_permitido: false,

      /////para filtrar
      lista_trabajador_original: [], // Lista original de usuarios
      filtroNombre: "", // Valor del filtro por nombre
       quitarFiltros: false, // Estado del checkbox "Quitar Filtros"


      //datos del usuario autenticado
      nombre_para_navbar_usuario: "", // Inicializa el nombre de usuario
      usuario_para_navbar_autenticado:"",
      lista_para_navbar_usuario: [],
      lista_para_navbar_rol: [],
      nombre_del_rol_para_navbar: "",

      lista_categoria_aux:[],
    };

  },

  // estos metodos se ejecutan automaticamente cuando la pagina este cargada
  mounted() {
    this.obtenerTrabajadores();
    this.obtenerListaPlazos();
    this.obtenerCategoria_del_profesor_del_servicio();

    // Recupera el nombre de usuario de localStorage
    this.nombre_para_navbar_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRolParaElNavBar();
  },

  methods: {
    obtenerTrabajadores() {
      axios.get('http://127.0.0.1:8000/api/trabajadores/0')
          .then(response => {

            console.log(response)
           this.lista_trabajadores = JSON.parse(response.data["trabajadores"]);
            this.lista_trabajador_original = JSON.parse(response.data["trabajadores"]);
          //  this.lista_trabajadores = response.data["trabajadores"];

            //  this.lista_trabajador_original = JSON.parse(response.data["trabajadores"]);
          //  this.lista_trabajadores = [...this.lista_trabajador_original]; // Copia la lista original a la lista filtrada
       })
          .catch(error => {
            console.error(error);
          });
    },
    eliminar_trabajadores(id){
      //const url = 'http://127.0.0.1:8000/api/tipo_de_moneda/delete/${id}';
      const url = `http://127.0.0.1:8000/api/trabajadores/delete/${id}`;
      axios.delete(url)
          .then(response => {
            this.obtenerTrabajadores();

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

    if (this.popupItem.nombre === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      else if (this.selectedPlazos.length === 0) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      const url = `http://127.0.0.1:8000/api/trabajadores/put/${this.popupItem.pk}`;
      const payload = {
       // id_trabajador: this.popupItem.id_trabajador,
        nombre: this.popupItem.fields.nombre,
        id_categoria_del_profesor_del_servicio: this.popupItem.fields.id_categoria_del_profesor_del_servicio,
        lista_plazo: this.selectedPlazos
        // Otros campos a modificar si es necesario
      };

      axios.put(url, payload)
          .then(response => {
            this.obtenerTrabajadores(); // Actualizar la tabla si es necesario
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


    guardar_nuevo_trabajador() {
      if (this.popupItemNuevo.id_trabajador === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      else if (this.popupItemNuevo.nombre === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      else if (this.selectedPlazos.length === 0) {
        // Mostrar mensaje de error si no se selecciona ningún plazo
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      const url = 'http://127.0.0.1:8000/api/trabajadores/post/';
      const payload = {

        id_trabajador: this.popupItemNuevo.id_trabajador,
        nombre: this.popupItemNuevo.nombre,
        id_categoria_del_profesor_del_servicio: this.popupItemNuevo.id_categoria_del_profesor_del_servicio,
        lista_plazo: this.selectedPlazos, // Usar los IDs de los plazos seleccionados

      };

      axios.post(url, payload)
          .then(response => {
            // Lógica después de crear el tipo de norma
            this.popupItemNuevo.nombre = ''; // Limpiar el campo de texto
            this.popupItemNuevo.cantidad = 0; // Limpiar el campo de texto
            this.popupItemNuevo.tipo = ''; // Limpiar el campo de texto
            this.showSuccessMessageInsertar = true; // Mostrar mensaje de éxito
            this.showErrorMessage = false; // Ocultar mensaje de error

            this.obtenerTrabajadores(); // Actualizar la tabla si es necesario
            this.cerrarPopupInsertar(); // Cerrar el popup después de insertar

            setTimeout(() => {
              this.showSuccessMessageInsertar = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },

    //cargamos la lista de plazos desde la llamada a la API
    obtenerListaPlazos(){
      axios.get('http://127.0.0.1:8000/api/plazos/0')
          .then(response => {
            // this.tipos_productos = response.data["Tipos de productos"]; // Actualizar los datos en la tabla
            //  console.log(response);
            this.lista_plazos_aux = response.data["plazos"];
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombrePlazo(id_plazo) {

      //console.log("id_plazo: "+id_plazo)
      if (this.lista_plazos_aux.length > 0) {
        const plazoId = parseInt(id_plazo); // Asegurarse de que id_plazo sea un número
        const plazo = this.lista_plazos_aux.find(p => p.id === plazoId);

        if (plazo) {
          return plazo.nombre_plazo;
        }
      }
      return 'Plazo no encontrado';
    },

    obtenerCategoria_del_profesor_del_servicio() {
      axios.get('http://127.0.0.1:8000/api/categoria_profesores/0')
          .then(response => {

            console.log(response)
            this.lista_categoria_aux = JSON.parse(response.data["categoria_profesor"]);
            //   this.lista_categoria_del_profesor_del_servicio_original = response.data["categoria_profesor"];

          //  this.lista_categoria_del_profesor_del_servicio = [...this.lista_categoria_del_profesor_del_servicio_original]; // Copia la lista original a la lista filtrada

          })
          .catch(error => {
            console.error(error);
          });
    },

    obtener_nombre_categoria(id){
console.log(id)
      if (this.lista_categoria_aux.length > 0) {
        const categoria = this.lista_categoria_aux.find(p => p.pk === id);
        console.log(categoria)
        if (categoria) {
          return categoria.fields.nombre_categoria;
        }
      }
      return 'Categoría no encontrada';

    },

///////////// funcione para validar
    //////////validar nombre

    validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-ZÁáÉéÍíÓóÚúÜü\s]*$/;

      if (!regex.test(item.nombre)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.nombre = item.nombre.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
    },

    aplicarFiltro() {
      if (this.quitarFiltros) {
        // Si el checkbox está marcado, restaura la lista original
        this.lista_trabajadores = [...this.lista_trabajador_original];
      } else {
        // Aplica el filtro por nombre
        const filteredList = this.lista_trabajador_original.filter(trabajador => {
          const nombreMatch = (!this.filtroNombre || trabajador.fields.nombre.includes(this.filtroNombre));
           return nombreMatch;
        });

        this.lista_trabajadores = filteredList;
      }
    },


    limpiarFiltros() {
      if (this.quitarFiltros) {
        // Si el checkbox está marcado, restaura la tabla original
        this.lista_trabajadores = [...this.lista_trabajador_original];
        this.filtroNombre = ""; // Limpia el filtro por nombre
      }
    },

    ordenarPor(columna) {
      if (this.columnaOrden === columna) {
        this.ordenAsc = !this.ordenAsc; // Cambiar la dirección si se hace clic en la misma columna
      } else {
        this.columnaOrden = columna; // Cambiar la columna de orden
        this.ordenAsc = true; // Restablecer la dirección a ascendente
      }

      // Lógica de ordenamiento aquí
      this.lista_trabajadores.sort((a, b) => {
        const factor = this.ordenAsc ? 1 : -1;
        const keys = columna.split('.');
        let valorA = a;
        let valorB = b;
        for (const key of keys) {
          valorA = valorA[key];
          valorB = valorB[key];
        }
        if (typeof valorA === 'string' && typeof valorB === 'string') {
          return valorA.localeCompare(valorB) * factor;
        } else {
          return (valorA - valorB) * factor;
        }
      });
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
      this.mostrarPopup_de_Insertar=false;
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
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.popup-contenidoTrabajador {
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