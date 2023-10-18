<template>
  <nav class="navbar navbar-dark bg-dark fixed-top" >
    <div class="container-fluid">
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


            <li class="nav-item dropdown" v-if="nombre_del_rol_para_navbar === 'Especialista de sistemas'">
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
<!--  <div class="containerPrueba">-->
    <h1>Lista de registros de derechos y propiedad</h1>
    <br>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessage">
      Registro eliminado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageUpdate">
      Registro modificado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageInsertar">
      Registro creado con éxito
    </div>

    <div class="form-group row" style="align-items: baseline;">
    <div class="col-md-4">
      <label for="filtroNombre">Filtrar por nombre de producto:</label>
      <input type="text" class="form-control" id="filtroNombre" v-model="filtroNombre" @input="aplicarFiltro">
    </div>
    </div>
    <br>

    <table class="table" style="font-family: 'Bahnschrift'">
      <thead>
      <tr>
        <th scope="col" style="font-weight: bold">#</th>
        <th scope="col" style="font-weight: bold"   colspan="2" id="nombre">
          Producto obtenido
          <span class="arrow" @click="ordenarPor('id_resultados_obtenidos_para_ficha_tecnica_id')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold"  >
          Porcentaje de la CUJAE
          <span class="arrow" @click="ordenarPor('porcentaje_de_la_cujae')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold"  >
          Porcentaje del cliente
          <span class="arrow" @click="ordenarPor('porcentaje_del_cliente')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold"  >
          Tipo de registro
          <span class="arrow" @click="ordenarPor('tipo_de_registro')">
    &#8593;&#8595;
  </span>
        </th>
      </tr>
      </thead>
      <tbody class="table-group-divider">
      <tr v-for="(item, index) in lista_registros_de_derechos_y_propiedad" :key="index">
        <th scope="row">{{ index + 1 }}</th>
        <td  colspan="2">{{ obtenerNombreResultados_obtenidos_para_ficha_tecnica(item.id_resultados_obtenidos_para_ficha_tecnica_id) }}</td>
        <td>{{ item.porcentaje_de_la_cujae }}</td>
        <td>{{ item.porcentaje_del_cliente }}</td>
        <td>{{ item.tipo_de_registro }}</td>


        <td>
          <div class="fila">
            <!--  <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>
              <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>-->
            <button class="btn btn-icon-text elemento" @click="abrirPopup(item)" type="submit">
              <img src="/iconos/Editar_40px.png" alt="Ícono de Modificar" width="40" height="40">

            </button>

            <div class="espacio"></div> <!-- Espacio entre elementos -->
            <button class="btn btn-icon-text elemento2" @click="eliminar(item.id)" style="margin-left: 20px; border-color: red; background-color: red" type="submit">
              <img src="/iconos/Eliminar_40px.png" alt="Ícono de Eliminar" width="40" height="40">

            </button>
          </div>
        </td>
      </tr>


      </tbody>
    </table>

    <button class="btn btn-icon-text elemento" @click="abrirPopupInsertar" type="submit">
      <img src="/iconos/Nuevo_40px.png" alt="Ícono de Crear nuevo" width="40" height="40">
      Crear nuevo registro
    </button>

    <div class="popup modal fade show d-block" v-if="mostrarPopup_de_Insertar" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoArea">
        <h2>Crear nuevo</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>


        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>

        <h5>Nombre del producto obtenido:</h5>

        <select single class="form-control" id="validationCustom01" v-model="popupItemNuevo.id_resultados_obtenidos_para_ficha_tecnica" required>
          <option v-for="resultado in lista_resultados_obtenidos_para_ficha_tecnica_aux" :key="resultado.id" :value="resultado.id">{{ resultado.nombre_producto_obtenido }}</option>
        </select>

        <br>
        <h5>Porcentaje de la CUJAE:</h5>
        <input type="number"  class="form-control" id="validationCustom01" v-model="popupItemNuevo.porcentaje_de_la_cujae" required min="1" max="100">
        <br>
        <h5>Porcentaje del cliente:</h5>
        <input type="number"  class="form-control" id="validationCustom01" v-model="popupItemNuevo.porcentaje_del_cliente" required min="1" max="100">

        <br>
        <h5>Tipo de registro:</h5>
        <input type="text"  class="form-control" id="validationCustom01" v-model="popupItemNuevo.tipo_de_registro" required>


        <br>
        <div class="fila">
          <button class="btn btn-icon-text elemento3" @click="guardar_nueva" type="submit">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar"  width="40" height="40">

          </button>
          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4" id="cerrarPopupInsertar" @click="cerrarPopupInsertar">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar"  width="40" height="40">

          </button>
        </div>
      </div>
    </div>

    <!-- <div class="popup" v-if="popupItem">-->
    <div class="popup modal fade show d-block" v-if="mostrarPopup" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoArea">

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>
        <h2>Modificar Área</h2>
        <br>

        <h5>Nombre del producto obtenido:</h5>

        <select single class="form-control" id="validationCustom01" v-model="popupItem.id_resultados_obtenidos_para_ficha_tecnica" required>
          <option v-for="resultado in lista_resultados_obtenidos_para_ficha_tecnica_aux" :key="resultado.id" :value="resultado.id">{{ resultado.nombre_producto_obtenido }}</option>
        </select>

        <br>
        <h5>Porcentaje de la CUJAE:</h5>
        <input type="number"  class="form-control" id="validationCustom01" v-model="popupItem.porcentaje_de_la_cujae" required min="1" max="100">
        <br>
        <h5>Porcentaje del cliente:</h5>
        <input type="number"  class="form-control" id="validationCustom01" v-model="popupItem.porcentaje_del_cliente" required min="1" max="100">

        <br>
        <h5>Tipo de registro:</h5>
        <input type="text"  class="form-control" id="validationCustom01" v-model="popupItem.tipo_de_registro" required>



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

    <div class="popup modal fade show d-block" v-if="mostrarPopupFiltro">
      <div class="popup-contenidoUsuario">
        <h2>Filtrar usuarios</h2>
        <br>
        <form @submit.prevent="aplicarFiltro">
          <!-- Campos de filtro -->
          <div class="form-group">
            <label for="filtroNombre">Nombre:</label>
            <input type="text" class="form-control" id="filtroNombre" v-model="filtro.nombre_usuario">
          </div>
          <br>
          <!-- Agrega otros campos de filtro aquí -->
          <button class="btn btn-primary elemento3" type="submit">Aplicar Filtro</button>
          <button class="btn btn-secondary elemento4" @click="cerrarPopupFiltro">Cancelar</button>
        </form>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import Inicio from "@/App.vue";
//import {it} from "vuetify/locale";

export default {
  components: {Inicio},
  data() {
    return {
      lista_registros_de_derechos_y_propiedad: [], // Array para almacenar los datos de la API
      showSuccessMessage: false,
      showSuccessMessageUpdate: false,
      popupItem: null,
      popupItemNuevo: null,
      showErrorMessage: false,
      showSuccessMessageInsertar:false,
      mostrarPopup: false, // Variable para controlar la visibilidad del pop-up
      mostrarPopup_de_Insertar: false, // Variable para controlar la visibilidad del pop-up

      lista_encuetros_por_semana_aux: [], //variable utilizada para guardar todos los trabajadores y recorrerlos
      selectedEncuetros_por_semana: [], // Esta propiedad rastreará los IDs de los encuentros seleccionados

      showErrorMessage_de_caracter_no_permitido: false,



      ////para ordenar
      columnaOrden: "", // Columna utilizada para el orden
      ordenAsc: true, // Dirección del orden

      /////para filtrar
      lista_registros_de_derechos_y_propiedad_original: [], // Lista original de usuarios
      filtroNombre: null, // Nueva propiedad para el filtro por rol
      quitarFiltros: false, // Estado del checkbox "Quitar Filtros"



      //datos del usuario autenticado
      nombre_para_navbar_usuario: "", // Inicializa el nombre de usuario
      usuario_para_navbar_autenticado:"",
      lista_para_navbar_usuario: [],
      lista_para_navbar_rol: [],
      nombre_del_rol_para_navbar: "",


      lista_resultados_obtenidos_para_ficha_tecnica_aux:[],
    };

  },

  // estos metodos se ejecutan automaticamente cuando la pagina este cargada
  mounted() {
    this.obtenerRegistros_de_derechos_y_propiedad();
    this.obtenerResultados_obtenidos_para_ficha_tecnica();


    // Recupera el nombre de usuario de localStorage
    this.nombre_para_navbar_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRolParaElNavBar();
  },

  methods: {
    obtenerRegistros_de_derechos_y_propiedad() {
      axios.get('http://127.0.0.1:8000/api/registros_de_derechos_y_propiedad/0')
          .then(response => {


             this.lista_registros_de_derechos_y_propiedad = response.data["registros_de_derechos_y_propiedad"];
             this.lista_registros_de_derechos_y_propiedad_original = response.data["registros_de_derechos_y_propiedad"];

          })
          .catch(error => {
            console.error(error);
          });
    },
    eliminar(id){
      //const url = 'http://127.0.0.1:8000/api/tipo_de_moneda/delete/${id}';
      const url = `http://127.0.0.1:8000/api/registros_de_derechos_y_propiedad/delete/${id}`;
      console.log(id)
      axios.delete(url)
          .then(response => {
            this.obtenerRegistros_de_derechos_y_propiedad();

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

    if (this.popupItem.id_resultados_obtenidos_para_ficha_tecnica === 0 ||
        this.popupItem.porcentaje_de_la_cujae === 0 ||
        this.popupItem.porcentaje_del_cliente === 0 ||
        this.popupItem.tipo_de_registro === ''

    ) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }


      const url = `http://127.0.0.1:8000/api/registros_de_derechos_y_propiedad/put/${this.popupItem.id}`;
      const payload = {
       // id_trabajador: this.popupItem.id_trabajador,
        id_resultados_obtenidos_para_ficha_tecnica: this.popupItem.id_resultados_obtenidos_para_ficha_tecnica,
        porcentaje_de_la_cujae: this.popupItem.porcentaje_de_la_cujae,
        porcentaje_del_cliente: this.popupItem.porcentaje_del_cliente,
        tipo_de_registro: this.popupItem.tipo_de_registro,
        // Otros campos a modificar si es necesario
      };

      axios.put(url, payload)
          .then(response => {
            this.obtenerRegistros_de_derechos_y_propiedad(); // Actualizar la tabla si es necesario
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


    guardar_nueva() {
      if (this.popupItemNuevo.id_resultados_obtenidos_para_ficha_tecnica === 0 ||
          this.popupItemNuevo.porcentaje_de_la_cujae === 0 ||
          this.popupItemNuevo.porcentaje_del_cliente === 0 ||
          this.popupItemNuevo.tipo_de_registro === ''

      ) {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }


      const url = 'http://127.0.0.1:8000/api/registros_de_derechos_y_propiedad/post/';
      const payload = {

        id_resultados_obtenidos_para_ficha_tecnica: this.popupItemNuevo.id_resultados_obtenidos_para_ficha_tecnica,
        porcentaje_de_la_cujae: this.popupItemNuevo.porcentaje_de_la_cujae,
        porcentaje_del_cliente: this.popupItemNuevo.porcentaje_del_cliente,
        tipo_de_registro: this.popupItemNuevo.tipo_de_registro,
      };

      axios.post(url, payload)
          .then(response => {
            // Lógica después de crear el area
            this.popupItemNuevo.nombre_completo_de_la_tarea = ''; // Limpiar el campo de texto
            this.popupItemNuevo.numero_de_la_tarea = 0; // Limpiar el campo de texto
            this.popupItemNuevo.lista_encuetros_por_semana = null; // Limpiar el campo de texto
            this.showSuccessMessageInsertar = true; // Mostrar mensaje de éxito
            this.showErrorMessage = false; // Ocultar mensaje de error

            this.obtenerRegistros_de_derechos_y_propiedad(); // Actualizar la tabla si es necesario
            this.cerrarPopupInsertar(); // Cerrar el popup después de insertar

            setTimeout(() => {
              this.showSuccessMessageInsertar = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },



    obtenerResultados_obtenidos_para_ficha_tecnica() {
      axios.get('http://127.0.0.1:8000/api/resultados_obtenidos_para_ficha_tecnica/0')
          .then(response => {
            this.lista_resultados_obtenidos_para_ficha_tecnica_aux = response.data["resultados_obtenidos_para_ficha_tecnica"];

           console.log(this.lista_resultados_obtenidos_para_ficha_tecnica_aux)
            })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreResultados_obtenidos_para_ficha_tecnica(id){

        if (this.lista_resultados_obtenidos_para_ficha_tecnica_aux.length > 0) {
          const resultadoId = parseInt(id); // Asegurarse de que id_rol sea un número
          const resultado = this.lista_resultados_obtenidos_para_ficha_tecnica_aux.find(p => p.id === id);

          if (resultado) {
            return resultado.nombre_producto_obtenido;
          }
        }
        return 'Resultado no encontrado';
      },


///////////// funcione para validar
    //////////validar nombre

    validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-ZÁáÉéÍíÓóÚúÜü\s]*$/;

      if (!regex.test(item.fields.nombre)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.fields.nombre = item.fields.nombre.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
    },

    /////// funcion ordenar

    // Método para cambiar la columna de orden y la dirección
   /* ordenarPor(columna) {
      console.log(columna)
      if (this.columnaOrden === columna) {
        this.ordenAsc = !this.ordenAsc; // Cambiar la dirección si se hace clic en la misma columna
      } else {
        this.columnaOrden = columna; // Cambiar la columna de orden
        this.ordenAsc = true; // Restablecer la dirección a ascendente
      }

      // Lógica de ordenamiento aquí
      this.lista_area_participante.sort((a, b) => {
        const factor = this.ordenAsc ? 1 : -1;
        const valorA = a[columna];
        const valorB = b[columna];
       return valorA.localeCompare(valorB) * factor;

      });
    },*/

    ordenarPor(columna) {
      if (this.columnaOrden === columna) {
        this.ordenAsc = !this.ordenAsc; // Cambiar la dirección si se hace clic en la misma columna
      } else {
        this.columnaOrden = columna; // Cambiar la columna de orden
        this.ordenAsc = true; // Restablecer la dirección a ascendente
      }

      // Lógica de ordenamiento aquí
      this.lista_registros_de_derechos_y_propiedad.sort((a, b) => {
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


    aplicarFiltro() {
      if (this.quitarFiltros) {
        // Si el checkbox está marcado, restaura la lista original
       // this.lista_area_participante = [...this.lista_area_participante_original];
      } else {
        // Aplica el filtro por nombre
          const filteredList = this.lista_registros_de_derechos_y_propiedad_original.filter(registro => {
          const registro_Match = (!this.filtroNombre || this.obtenerNombreResultados_obtenidos_para_ficha_tecnica(registro.id_resultados_obtenidos_para_ficha_tecnica_id) === this.filtroNombre);
          return registro_Match;
        });

        this.lista_registros_de_derechos_y_propiedad = filteredList;
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

.popup-contenidoArea {
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