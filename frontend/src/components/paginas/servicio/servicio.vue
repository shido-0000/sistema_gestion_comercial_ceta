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


  <div class="container-md-10" style="margin: 20px;font-family: 'Bahnschrift'">
  <!--<div class="containerPrueba">-->
    <h1>Lista de servicios</h1>
    <br>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessage">
      Servicio eliminado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageUpdate">
      Servicio modificado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageInsertar">
      Servicio creado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageNoEliminar">
      El servicio está siendo utilizado en un contrato, no se puede eliminar
    </div>

    <br>

    <table class="table" style="font-family: 'Bahnschrift'">
      <thead>
      <tr>
        <th scope="col" style="font-weight: bold">#</th>
       <!--<th scope="col" style="font-weight: bold" align="center">Nombre del servicio</th>-->
        <th scope="col" style="font-weight: bold" >
          Nombre del servicio
          <span class="arrow" @click="ordenarPor('fields.nombre_servicio')">
              &#8593;&#8595;
            </span>
        </th>

        <th scope="col" style="font-weight: bold" >
          Capacidad de matrícula
          <span class="arrow" @click="ordenarPor('fields.capacidad_de_matricula')">
              &#8593;&#8595;
            </span>
        </th>

        <th scope="col" style="font-weight: bold" >Listado de trabajadores</th>

      </tr>
      </thead>
      <tbody class="table-group-divider">
      <tr v-for="(item, index) in lista_servicio" :key="index">
        <th scope="row">{{ index + 1 }}</th>
        <td >{{ item.fields.nombre_servicio }}</td>
        <td >{{ item.fields.capacidad_de_matricula }}</td>
      <!--  <td >
          <ul>
            <li v-for="id_categoria in item.fields.lista_categorias" >{{ obtenerNombreCategoria(id_categoria) }}</li>
          </ul>
        </td>-->
        <td >
          <ul>
            <li v-for="id_trabajador in item.fields.lista_trabajadores" >{{ obtenerNombreTrabajador(id_trabajador) }}</li>
          </ul>
        </td>

        <td>
          <div class="fila">
            <button class="btn btn-icon-text elemento" @click="abrirPopup(item)" type="submit">
              <img src="/iconos/Editar_40px.png" alt="Ícono de Modificar" width="40" height="40">

            </button>
            <div class="espacio"></div>
            <button class="btn btn-icon-text elemento2" @click="eliminar_servicio(item.pk)" style="margin-left: 20px;border-color: red; background-color: red" type="submit">
              <img src="/iconos/Eliminar_40px.png" alt="Ícono de Eliminar" width="40" height="40">

            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table>

    <button class="btn btn-icon-text elemento" @click="abrirPopupInsertar" type="submit">
      <img src="/iconos/Nuevo_40px.png" alt="Ícono de Crear nuevo" width="40" height="40">
      Crear nuevo servicio
    </button>

    <div class="popup modal fade show d-block" v-if="mostrarPopup_de_Insertar" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoServicio" style="top: 33%">
        <h2>Crear nuevo</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Campo vacío
        </div>


        <!-- Grupo 1 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Nombre del servicio:</h5>
            <input type="text" class="form-control" name="insertar_nombre" id="insertar_nombre" v-model="popupItemNuevo.nombre_servicio" required @input="validarNombre(popupItemNuevo)">
          </div>
          <div class="col-md-4">
            <h5>Capacidad de matrícula:</h5>
            <input type="number" class="form-control" name="insertar_capacidad_matricula" id="insertar_capacidad_matricula" v-model="popupItemNuevo.capacidad_de_matricula" required min="1">
          </div>

          <div class="col-md-4">
            <h5>Total de costo a pagar:</h5>
            <input type="text" readonly class="form-control" name="importeAPagar" id="importeAPagar" v-model="importeAPagar" required></div>
        </div>

        <br>

        <!-- Grupo 2 de campos -->
        <!--<div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Lista de categorías:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedCategorias" required>
              <option v-for="categorias in lista_categorias_aux" :key="categorias.pk" :value="categorias.pk">{{ categorias.fields.nombre_categoria }}</option>
            </select>
          </div>-->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Lista de trabajadores:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedTrabajadores" required>
              <option v-for="trabajadores in lista_trabajadores_aux" :key="trabajadores.pk" :value="trabajadores.pk">{{ trabajadores.fields.nombre }}</option>
            </select>
          </div>
          <div class="col-md-4">
            <h5>Calcular costo:</h5>
            <button class="btn btn-icon-text elemento4" id="calcular_importe_a_pagar" @click="calcular_importe_a_pagar">
              <img src="/iconos/Calcular_50px.png" alt="Ícono de Calcular" width="40" height="40">
              Calcular
            </button>
          </div>
        </div>

        <br>

        <div class="fila">
          <button class="btn btn-icon-text elemento3" @click="guardar_nuevo_servicio" type="submit" :disabled="deshabilitar_boton_confirmar">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar" width="40" height="40">

          </button>
          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4" id="cerrarPopupInsertar" @click="cerrarPopupInsertar">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar" width="40" height="40">

          </button>
        </div>
      </div>
    </div>

    <div class="popup modal fade show d-block" v-if="mostrarPopup" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoServicio" style="top: 33%">
        <h2>Modificar datos</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Campo vacío
        </div>

        <!-- Grupo 1 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Nombre del servicio:</h5>
            <input type="text" class="form-control" name="insertar_nombre" id="insertar_nombre" v-model="popupItem.nombre_servicio" required @input="validarNombre(popupItemNuevo)">
          </div>
          <div class="col-md-4">
            <h5>Capacidad de matrícula:</h5>
            <input type="number" class="form-control" name="insertar_capacidad_matricula" id="insertar_capacidad_matricula" v-model="popupItem.capacidad_de_matricula" required min="1">
          </div>

          <div class="col-md-4">
            <h5>Total de costo a pagar:</h5>
            <input type="text" readonly class="form-control" name="importeAPagar" id="importeAPagar" v-model="importeAPagar" required></div>
        </div>

        <br>

        <!-- Grupo 2 de campos -->
        <!--<div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Lista de categorías:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedCategorias" required>
              <option v-for="categorias in lista_categorias_aux" :key="categorias.pk" :value="categorias.pk">{{ categorias.fields.nombre_categoria }}</option>
            </select>
          </div>-->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Lista de trabajadores:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedTrabajadores" required>
              <option v-for="trabajadores in lista_trabajadores_aux" :key="trabajadores.pk" :value="trabajadores.pk">{{ trabajadores.fields.nombre }}</option>
            </select>
          </div>
          <div class="col-md-4">
            <h5>Calcular costo:</h5>
            <button class="btn btn-icon-text elemento4" id="calcular_importe_a_pagar" @click="calcular_importe_a_pagar">
              <img src="/iconos/Calcular_50px.png" alt="Ícono de Calcular" width="40" height="40">
              Calcular
            </button>
          </div>
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

export default {
  data() {
    return {
      lista_servicio: [], // Array para almacenar los datos de la API
      lista_contratos: [], // Array para almacenar los datos de la API

      lista_categorias_aux: [], // Array para almacenar los datos de la API

      lista_trabajadores_aux: [], // Array para almacenar los datos de la API


      showSuccessMessage: false,
      showSuccessMessageUpdate: false,
      showSuccessMessageNoEliminar: false,
      popupItem: null,
      showErrorMessage: false,
      showSuccessMessageInsertar:false,
      mostrarPopup: false, // Variable para controlar la visibilidad del pop-up
      mostrarPopup_de_Insertar: false, // Variable para controlar la visibilidad del pop-up

      //selectedCategorias: [],
      selectedTrabajadores:[],
      showErrorMessage_de_caracter_no_permitido: false,

      popupItemNuevo: {
        nombre_servicio: '',
      },

      ////para ordenar
      columnaOrden: "", // Columna utilizada para el orden
      ordenAsc: true, // Dirección del orden


      //datos del usuario autenticado
      nombre_para_navbar_usuario: "", // Inicializa el nombre de usuario
      usuario_para_navbar_autenticado:"",
      lista_para_navbar_usuario: [],
      lista_para_navbar_rol: [],
      nombre_del_rol_para_navbar: "",

// Variable para almacenar el resultado del importe
      importeAPagar: 0,

      deshabilitar_boton_confirmar: true,
    };

  },

  //esto es para actualizar la propiedad deshabilitar_boton_confirmar
  watch: {
    importeAPagar(importe_total) {
      this.deshabilitar_boton_confirmar = importe_total === 0;
    },
  },


  mounted() {
    this.obtener_servicio();
    this.obtener_contratos();
    this.obtenerListaCategorias();
    this.obtenerListaTrabajadores();

    // Recupera el nombre de usuario de localStorage
    this.nombre_para_navbar_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRolParaElNavBar();
  },

  methods: {
    obtener_servicio() {
      axios.get('http://127.0.0.1:8000/api/servicios/0')
          .then(response => {
            // Actualizar los datos en la tabla
            console.log(response)
          //  this.lista_servicio = response.data["servicio"];
           this.lista_servicio = JSON.parse(response.data["servicio"]);

          })
          .catch(error => {
            console.error(error);
          });
    },
    obtener_contratos(){
      axios.get('http://127.0.0.1:8000/api/contratos/0')
          .then(response => {
            // Actualizar los datos en la tabla
            console.log(response)
            this.lista_contratos = JSON.parse(response.data["contratos"]);

          })
          .catch(error => {
            console.error(error);
          });
    },
    obtenerContratoConEseServicio(servicioId) {
      this.showSuccessMessageNoEliminar = false;

      if (this.lista_contratos.length > 0) {
        //console.log(this.lista_trabajador_aux.length)
        const contrato = this.lista_contratos.find(p => p.fields.id_servicio === servicioId);
        //console.log(trabajador.fields.nombre)
        if (contrato) {
          this.showSuccessMessageNoEliminar = true;
        } else
          this.showSuccessMessageNoEliminar = false;
      }
      return this.showSuccessMessageNoEliminar;
    },
    eliminar_servicio(id){
      const url = `http://127.0.0.1:8000/api/servicios/delete/${id}`;
      if(this.obtenerContratoConEseServicio(id) == true){
      setTimeout(() => {
        this.showSuccessMessageNoEliminar = false; // Ocultar mensaje de éxito después de unos segundos
      }, 3000);
      } else {
      axios.delete(url)
          .then(response => {
            this.obtener_servicio();

            // mostrar mensaje flotante
            // Mostrar mensaje de éxito
            this.showSuccessMessage = true; // Mostrar mensaje de éxito
            setTimeout(() => {
              this.showSuccessMessage = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });}
    },

    guardarCambios() {

      if (this.popupItem.nombre_servicio === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      if (this.popupItem.capacidad_de_matricula === 0) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      if (this.selectedTrabajadores.length === 0) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      const url = `http://127.0.0.1:8000/api/servicios/put/${this.popupItem.pk}`;
      const payload = {
        nombre_servicio: this.popupItem.nombre_servicio,
        capacidad_de_matricula: this.popupItem.capacidad_de_matricula,
        lista_trabajadores: this.selectedTrabajadores, // Usar los IDs de las categorias seleccionados
        // Otros campos a modificar si es necesario
      };

      axios.put(url, payload)
          .then(response => {
            this.obtener_servicio(); // Actualizar la tabla si es necesario
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


    guardar_nuevo_servicio() {

      if (!this.popupItemNuevo) {
        // Si popupItemNuevo es undefined, muestra un mensaje de error o maneja la situación de manera apropiada
        return;
      }

      if (
          !this.popupItemNuevo.nombre_servicio ||
          this.popupItemNuevo.nombre_servicio.trim() === ''
      ) {
        // Mostrar un mensaje de error al usuario indicando que los campos son obligatorios
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      if (this.popupItemNuevo.capacidad_de_matricula === 0) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }
      if (this.selectedTrabajadores.length === 0) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

      const url = 'http://127.0.0.1:8000/api/servicios/post/';
      const payload = {
        nombre_servicio: this.popupItemNuevo.nombre_servicio,
        capacidad_de_matricula: this.popupItemNuevo.capacidad_de_matricula,
        lista_trabajadores: this.selectedTrabajadores, // Usar los IDs de las categorias seleccionados

      };

      axios.post(url, payload)
          .then(response => {
            // Lógica después de crear el tipo de norma
            this.popupItemNuevo.nombre_servicio = ''; // Limpiar el campo de texto
            this.popupItemNuevo.capacidad_de_matricula = 0 // Limpiar el campo de texto
            this.showSuccessMessageInsertar = true; // Mostrar mensaje de éxito
            this.showErrorMessage = false; // Ocultar mensaje de error

            this.obtener_servicio(); // Actualizar la tabla si es necesario
            this.cerrarPopupInsertar(); // Cerrar el popup después de insertar

            setTimeout(() => {
              this.showSuccessMessageInsertar = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },

  /*  obtenerNombreCategoria(id_categoria) {

      //console.log("id_plazo: "+id_plazo)
      if (this.lista_categorias_aux.length > 0) {
        const categoriaId = parseInt(id_categoria); // Asegurarse de que id_plazo sea un número
        const categoria = this.lista_categorias_aux.find(p => p.pk === categoriaId);

        if (categoria) {
          return categoria.fields.nombre_categoria;
        }
      }
      return 'Categoría no encontrada';
    },*/

    obtenerNombreTrabajador(id_trabajador) {

      //console.log("id_plazo: "+id_plazo)
      if (this.lista_trabajadores_aux.length > 0) {
        const trabajadorId = parseInt(id_trabajador); // Asegurarse de que id_plazo sea un número
        const trabajador = this.lista_trabajadores_aux.find(p => p.pk === id_trabajador);

        if (trabajador) {
          return trabajador.fields.nombre;
        }
      }
      return 'Trabajador no encontrado';
    },


    //cargamos la lista de categorias de profesores para los servicios desde la llamada a la API
    obtenerListaCategorias(){
      axios.get('http://127.0.0.1:8000/api/categoria_profesores/0')
          .then(response => {
            this.lista_categorias_aux = JSON.parse(response.data["categoria_profesor"]);
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerListaTrabajadores() {
      axios.get('http://127.0.0.1:8000/api/trabajadores/0')
          .then(response => {


            this.lista_trabajadores_aux = JSON.parse(response.data["trabajadores"]);
            //  this.lista_trabajadores = response.data["trabajadores"];

            //  this.lista_trabajador_original = JSON.parse(response.data["trabajadores"]);
            //  this.lista_trabajadores = [...this.lista_trabajador_original]; // Copia la lista original a la lista filtrada
          })
          .catch(error => {
            console.error(error);
          });
    },


    /// funcion para calcular el costo total a pagar

    /*calcular_importe_a_pagar(){
      let suma = 0;

      for (let i = 0; i < this.selectedCategorias.length; i++) {
        // console.log(this.lista[i]);

        const categoria = this.lista_categorias_aux.find(p => p.pk === this.selectedCategorias[i]);
        let costo_por_hora = categoria.fields.tarifa_por_hora * categoria.fields.total_de_horas;

        suma+=costo_por_hora;

        // Puedes realizar operaciones con cada elemento aquí
      }

      // Actualizar la variable importeAPagar con el resultado
      this.importeAPagar = suma;
    },*/

    calcular_importe_a_pagar(){
      let suma = 0;

      for (let i = 0; i < this.selectedTrabajadores.length; i++) {
        // console.log(this.lista[i]);

        const trabajador = this.lista_trabajadores_aux.find(p => p.pk === this.selectedTrabajadores[i]);
        let id_categoria = trabajador.fields.id_categoria_del_profesor_del_servicio;


        const categoria = this.lista_categorias_aux.find(p => p.pk === id_categoria);

        let costo_por_hora = categoria.fields.tarifa_por_hora * categoria.fields.total_de_horas;

        suma+=costo_por_hora;

        // Puedes realizar operaciones con cada elemento aquí
      }

      // Actualizar la variable importeAPagar con el resultado
      this.importeAPagar = suma;
    },

    ///////////// funcione para validar
    //////////validar nombre

    validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-ZÁáÉéÍíÓóÚúÜü\s]*$/;

      if (!regex.test(item.nombre_servicio)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.nombre_servicio = item.nombre_servicio.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
    },

    // Método para cambiar la columna de orden y la dirección

    ordenarPor(columna) {
      if (this.columnaOrden === columna) {
        this.ordenAsc = !this.ordenAsc; // Cambiar la dirección si se hace clic en la misma columna
      } else {
        this.columnaOrden = columna; // Cambiar la columna de orden
        this.ordenAsc = true; // Restablecer la dirección a ascendente
      }

      // Lógica de ordenamiento aquí
      this.lista_servicio.sort((a, b) => {
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

     // this.popupItemNuevo.nombre_rol = '';
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
  top: 0%;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.popup-contenidoServicio {
  background-color: #fff;
  width: 600px;
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