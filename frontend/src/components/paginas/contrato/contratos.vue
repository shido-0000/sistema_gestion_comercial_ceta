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
            <img src="/iconos/cerrar_sesion_48px.png" alt="Icono de Cerrar Sesión">
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
<!--  <div class="containerPrueba">-->

    <div class="alert alert-danger" role="alert" v-if="menssage_no_se_puede_eliminar_o_modificar_contrato">
      Error, no puede eliminar o modificar este contrato porque usted no es su creador
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessage">
      Contrato eliminado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageUpdate">
      Contrato modificado con éxito
    </div>

    <div class="alert alert-success" role="alert" v-if="showSuccessMessageInsertar">
      Contrato creado con éxito
    </div>


    <h1>Lista de contratos</h1>
    <br>

    <table class="table">
      <thead>
      <tr>
        <th scope="col" style="font-weight: bold">#</th>
        <th scope="col" style="font-weight: bold" align="center"  id="Version">
          Versión
          <span class="arrow" @click="ordenarPor('fields.version')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="CES">
          CES
          <span class="arrow" @click="ordenarPor('fields.CES')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Titulo">
          Título
          <span class="arrow" @click="ordenarPor('fields.titulo')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Numero">
          Número
          <span class="arrow" @click="ordenarPor('fields.numero')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Grupo_ejecutor_del_contrato">
          Grupo ejecutor del contrato
          <span class="arrow" @click="ordenarPor('fields.grupo_ejecutor_del_contrato')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Cliente">
          Cliente
          <span class="arrow" @click="ordenarPor('fields.cliente')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Gestor">
          Gestor
          <span class="arrow" @click="ordenarPor('fields.gestor')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Producto">
          Producto
          <span class="arrow" @click="ordenarPor('fields.producto')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Codigo">
          Código
          <span class="arrow" @click="ordenarPor('fields.codigo')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Servicio">
          Servicio
          <span class="arrow" @click="ordenarPor('fields.servicio')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Localizacion_del_cliente">
          Localización del cliente
          <span class="arrow" @click="ordenarPor('fields.localizacion_del_cliente')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Coordinador_del_contrato">
          Coordinador del contrato
          <span class="arrow" @click="ordenarPor('fields.coordinador_del_contrato')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Cantidad_de_participantes">
          Cantidad de participantes
          <span class="arrow" @click="ordenarPor('fields.cantidad_de_participantes')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Fecha_de_inicio">
          Fecha de inicio
          <span class="arrow" @click="ordenarPor('fields.fecha_de_inicio')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Fecha_de_terminacion">
          Fecha de terminación
          <span class="arrow" @click="ordenarPor('fields.terminacion')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Valor_del_contrato">
          Valor del contrato
          <span class="arrow" @click="ordenarPor('fields.valor_del_contrato')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Margen_comercial">
          Margen comercial
          <span class="arrow" @click="ordenarPor('fields.margen_comercial')">
    &#8593;&#8595;
  </span>
        </th>
        <th scope="col" style="font-weight: bold" align="center"  id="Ingreso_bruto">
          Ingreso bruto
          <span class="arrow" @click="ordenarPor('fields.ingreso_bruto')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Observaciones">
          Observaciones
          <span class="arrow" @click="ordenarPor('fields.observaciones')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center" id="Gastos_de_operación_desde_CETA">
          Gastos de operación desde CETA
          <span class="arrow" @click="ordenarPor('fields.gastos_de_operacion_desde_CETA')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Ingreso_neto_planificado">
          Ingreso neto planificado
          <span class="arrow" @click="ordenarPor('fields.ingreso_neto_planificado')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Remuneracion">
          Remuneración
          <span class="arrow" @click="ordenarPor('fields.remuneracion')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center" id="Norma_maxima">
          Norma máxima
          <span class="arrow" @click="ordenarPor('fields.norma_maxima')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center" id="Norma_asignada">
          Norma asignada
          <span class="arrow" @click="ordenarPor('fields.norma_asignada')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Propuesto_por">
          Propuesto por
          <span class="arrow" @click="ordenarPor('fields.propuesto_por')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center"  id="Aprobado_por">
          Aprobado por
          <span class="arrow" @click="ordenarPor('fields.aprobado_por')">
    &#8593;&#8595;
  </span>
        </th>

        <th scope="col" style="font-weight: bold" align="center">Listado de programa de cobro</th>
        <th scope="col" style="font-weight: bold" align="center">Listado de áreas participantes</th>
       <!-- <th scope="col" style="font-weight: bold; width: 40px">#</th>
        <th scope="col" style="font-weight: bold; width: 120px">Versión</th>
        <th scope="col" style="font-weight: bold; width: 120px">CES</th>
        <th scope="col" style="font-weight: bold; width: 120px">Título</th>
        <th scope="col" style="font-weight: bold; width: 120px">Número</th>
        <th scope="col" style="font-weight: bold; width: 210px">Grupo ejecutor del contrato</th>
        <th scope="col" style="font-weight: bold; width: 180px">Cliente</th>
        <th scope="col" style="font-weight: bold; width: 180px">Gestor</th>
        <th scope="col" style="font-weight: bold; width: 180px">Producto</th>
        <th scope="col" style="font-weight: bold; width: 120px">Código</th>
        <th scope="col" style="font-weight: bold; width: 120px">Servicio</th>
        <th scope="col" style="font-weight: bold; width: 180px">Localización del cliente</th>
        <th scope="col" style="font-weight: bold; width: 180px">Coordinador del contrato</th>
        <th scope="col" style="font-weight: bold; width: 120px">Cantidad de participantes</th>
        <th scope="col" style="font-weight: bold; width: 250px">Fecha de inicio</th>
        <th scope="col" style="font-weight: bold; width: 180px">Fecha de terminación</th>
        <th scope="col" style="font-weight: bold; width: 120px">Valor del contrato</th>
        <th scope="col" style="font-weight: bold; width: 120px">Margen comercial</th>
        <th scope="col" style="font-weight: bold; width: 120px">Ingreso bruto</th>
        <th scope="col" style="font-weight: bold; width: 180px">Observaciones</th>
        <th scope="col" style="font-weight: bold; width: 180px">Gastos de operación desde CETA</th>
        <th scope="col" style="font-weight: bold; width: 120px">Ingreso neto planificado</th>
        <th scope="col" style="font-weight: bold; width: 120px">Remuneración</th>
        <th scope="col" style="font-weight: bold; width: 120px">Norma máxima</th>
        <th scope="col" style="font-weight: bold; width: 120px">Norma asignada</th>
        <th scope="col" style="font-weight: bold; width: 180px">Propuesto por</th>
        <th scope="col" style="font-weight: bold; width: 180px">Aprobado por</th>
        <th scope="col" style="font-weight: bold; width: 180px">Listado de programa de cobro</th>
        <th scope="col" style="font-weight: bold; width: 180px">Listado de áreas participantes</th>
      --></tr>
      </thead>
      <tbody class="table-group-divider">
      <tr v-for="(item, index) in lista_contratos" :key="index">
        <th scope="row">{{ index + 1 }}</th>
        <td align="center" style="width: 40px">{{ item.fields.version }}</td>
        <td align="center" style="width: 120px">{{ item.fields.CES }}</td>
        <td align="center" style="width: 120px">{{ item.fields.titulo }}</td>
        <td align="center" style="width: 120px">{{ item.fields.numero }}</td>
        <td align="center" style="width: 210px">{{ item.fields.grupo_ejecutor_del_contrato }}</td>
        <td align="center" style="width: 180px">{{ item.fields.cliente }}</td>
        <td align="center" style="width: 180px">{{ item.fields.gestor }}</td>
        <td align="center" style="width: 180px">{{ item.fields.producto }}</td>
        <td align="center" style="width: 120px">{{ item.fields.codigo }}</td>
        <td align="center" style="width: 120px">{{obtenerNombreServicio(item.fields.id_servicio)  }}</td>
        <td align="center" style="width: 180px">{{ item.fields.localizacion_del_cliente }}</td>
        <td align="center" style="width: 180px">{{ item.fields.coordinador_del_contrato }}</td>
        <td align="center" style="width: 120px">{{ item.fields.cantidad_de_participantes }}</td>
        <td align="center" style="width: 250px">{{ item.fields.fecha_de_inicio }}</td>
        <td align="center" style="width: 180px">{{ item.fields.terminacion }}</td>
        <td align="center" style="width: 120px">{{ item.fields.valor_del_contrato }}</td>
        <td align="center" style="width: 120px">{{ item.fields.margen_comercial }}</td>
        <td align="center" style="width: 120px">{{ item.fields.ingreso_bruto }}</td>
        <td align="center" style="width: 180px">{{ item.fields.observaciones }}</td>
        <td align="center" style="width: 180px">{{ item.fields.gastos_de_operacion_desde_CETA }}</td>
        <td align="center" style="width: 120px">{{ item.fields.ingreso_neto_planificado }}</td>
        <td align="center" style="width: 120px">{{ item.fields.remuneracion }}</td>
        <td align="center" style="width: 120px">{{ item.fields.norma_maxima }}</td>
        <td align="center" style="width: 180px">{{ item.fields.norma_asignada }}</td>
        <td align="center" style="width: 180px">{{ item.fields.propuesto_por }}</td>
        <td align="center" style="width: 180px">{{ item.fields.aprobado_por }}</td>
        <td align="center" style="width: 180px">
          <ul>
            <li v-for="id_programa_cobro in item.fields.lista_programa_de_cobro" >{{ obtenerNombreProgramaCobro(id_programa_cobro) }}</li>
          </ul>
        </td>
        <td align="center" style="width: 180px">
          <ul>
            <li v-for="id_area_participante in item.fields.lista_area_participante" >{{ obtenerNombreAreaParticipante(id_area_participante) }}</li>
          </ul>
        </td>



        <td>
          <div class="fila">
            <!--  <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>
              <button class="btn btn-primary elemento" @click="abrirPopup(item)" type="submit">Modificar</button>-->
            <button class="btn btn-icon-text elemento" @click="abrirPopup(item)" type="submit" v-if="item.fields.propuesto_por === nombreCompletoUsuario">
              <img src="/iconos/Editar_40px.png" alt="Ícono de Modificar">

            </button>

            <div class="espacio"></div> <!-- Espacio entre elementos -->
            <button class="btn btn-icon-text elemento2" @click="eliminar_contratos(item.pk)" style="border-color: red; background-color: red" type="submit" v-if="item.fields.propuesto_por === nombreCompletoUsuario && nombre_del_rol_para_navbar === 'Gestor de proyecto'">
              <img src="/iconos/Eliminar_40px.png" alt="Ícono de Eliminar">

            </button>
          </div>
        </td>
      </tr>

      </tbody>
    </table>

    <button class="btn btn-icon-text elemento" @click="abrirPopupInsertar" type="submit" v-if="nombre_del_rol_para_navbar === 'Gestor de proyecto'" style="font-family: 'Bahnschrift'">
      <img src="/iconos/Nuevo_40px.png" alt="Ícono de Crear nuevo">
      Crear nuevo contrato
    </button>


    <!--popup para crear un nuevo contrato-->
        <div class="popup modal fade show d-block" v-if="mostrarPopup_de_Insertar" style="font-family: 'Bahnschrift'">
          <div class="popup-contenidoContrato">
            <h2>Crear nuevo contrato</h2>
            <br>

            <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
              Error, carácter no permitido
            </div>

            <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
              Error, faltan campos por llenar
            </div>

            <br>

            <!-- Grupo 1 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Versión:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.version" required>
              </div>
              <div class="col-md-4">
                <h5>CES:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.CES" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Título:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.titulo" required @input="validarNombre(popupItemNuevo)">
              </div>
            </div>

            <!-- Grupo 2 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Número:</h5>
                <input type="number" class="form-control" v-model="popupItemNuevo.numero" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Grupo ejecutor del contrato:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.grupo_ejecutor_del_contrato" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Cliente:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.cliente" required @input="validarNombre(popupItemNuevo)">
              </div>
            </div>

            <!-- Grupo 3 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Gestor:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.gestor" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Producto:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.producto" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Código:</h5>
                <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.codigo" required >
              </div>
            </div>

            <!-- Grupo 4 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Localización del cliente:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.localizacion_del_cliente" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Coordinador del contrato:</h5>
                <input type="text" class="form-control" v-model="popupItemNuevo.coordinador_del_contrato" required @input="validarNombre(popupItemNuevo)">
              </div>
              <div class="col-md-4">
                <h5>Cantidad de participantes:</h5>
                <input type="number" class="form-control" v-model="popupItemNuevo.cantidad_de_participantes" required min="1">
              </div>
            </div>

            <!-- Grupo 5 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Fecha de inicio:</h5>
                <input type="date" class="form-control" id="validationCustom01" v-model="popupItemNuevo.fecha_de_inicio" required >
              </div>
              <div class="col-md-4">
                <h5>Fecha de terminación:</h5>
                <input type="date" class="form-control" id="validationCustom01" v-model="popupItemNuevo.terminacion" required >
              </div>
              <div class="col-md-4">
                <h5>Valor del contrato:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.valor_del_contrato" required min="1">
              </div>
            </div>

            <!-- Grupo 6 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Margen comercial:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.margen_comercial" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Ingreso bruto:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.ingreso_bruto" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Observaciones:</h5>
                <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.observaciones" required>
              </div>
            </div>

            <!-- Grupo 7 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Gastos de operación desde CETA:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.gastos_de_operacion_desde_CETA" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Ingreso neto planificado:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.ingreso_neto_planificado" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Remuneración:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.remuneracion" required min="1">
              </div>
            </div>

            <!-- Grupo 8 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Norma máxima:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.norma_maxima" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Norma asignada:</h5>
                <input type="number" class="form-control" id="validationCustom01" v-model="popupItemNuevo.norma_asignada" required min="1">
              </div>
              <div class="col-md-4">
                <h5>Servicio:</h5>
                <select single class="form-control" id="validationCustom01" v-model="selectedServicio" required>
                  <option v-for="servicio in lista_servicios" :key="servicio.pk" :value="servicio.pk">{{ obtenerNombreServicio(servicio.pk) }}</option>
                </select>
              </div>

            </div>

            <!-- Grupo 9 de campos -->
            <div class="form-group row" style="align-items: baseline;">

              <div class="col-md-4">
                <h5>Listado de programas de cobro:</h5>
                <select multiple class="form-control" id="validationCustom01" v-model="selectedProgramaCobro" required>s
                  <option v-for="programa in lista_programa_cobros" :key="programa.id" :value="programa.id">{{ programa.nombre_programa }}</option>
                </select>
              </div>
              <div class="col-md-4">
                <h5>Listado de áreas participantes:</h5>
                <select multiple class="form-control" id="validationCustom01" v-model="selectedAreaParticipante" required>
                  <option v-for="area_participante in lista_area_participante" :key="area_participante.pk" :value="area_participante.pk">{{ area_participante.fields.nombre }}</option>
                </select>
              </div>

            </div>

            <!-- Grupo 10 de campos -->
            <div class="form-group row" style="align-items: baseline;">
              <div class="col-md-4">
                <h5>Propuesto por:</h5>
               <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.propuesto_por" readonly  required @input="validarNombre(popupItemNuevo)">

              </div>
              <div class="col-md-4">
                <h5>Aprobado por:</h5>
                <input type="text" class="form-control" id="validationCustom01" v-model="popupItemNuevo.aprobado_por" required @input="validarNombre(popupItemNuevo)">
              </div>

            </div>

            <!-- Continúa con los grupos de campos restantes -->

            <br>

            <div class="fila">
              <button class="btn btn-icon-text elemento3" @click="guardar_nuevo_contrato" type="submit">
                <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar">

              </button>
              <div class="espacio"></div>
              <button class="btn btn-icon-text elemento4" id="cerrarPopupInsertar" @click="cerrarPopupInsertar">
                <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar">

              </button>
            </div>
          </div>
        </div>


    <!-- <div class="popup" v-if="popupItem">-->
    <div class="popup modal fade show d-block" v-if="mostrarPopup" style="font-family: 'Bahnschrift'">
      <div class="popup-contenidoContrato">

        <h2>Modificar contrato</h2>
        <br>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage_de_caracter_no_permitido">
          Error, carácter no permitido
        </div>

        <div class="alert alert-danger" role="alert" v-if="showErrorMessage">
          Error, faltan campos por llenar
        </div>

        <!-- Grupo 1 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Versión:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.version" required>
          </div>
          <div class="col-md-4">
            <h5>CES:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.CES" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Título:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.titulo" required @input="validarNombre(popupItem)">
          </div>
        </div>

        <!-- Grupo 2 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Número:</h5>
            <input type="number" class="form-control" v-model="popupItem.fields.numero" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Grupo ejecutor del contrato:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.grupo_ejecutor_del_contrato" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Cliente:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.cliente" required @input="validarNombre(popupItem)">
          </div>
        </div>

        <!-- Grupo 3 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Gestor:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.gestor" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Producto:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.producto" required @input="validarNombre(popupItem)">
          </div>

          <div class="col-md-4">
            <h5>Código:</h5>
            <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.fields.codigo" required >
          </div>
        </div>

        <!-- Grupo 4 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Localización del cliente:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.localizacion_del_cliente" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Coordinador del contrato:</h5>
            <input type="text" class="form-control" v-model="popupItem.fields.coordinador_del_contrato" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Cantidad de participantes:</h5>
            <input type="number" class="form-control" v-model="popupItem.fields.cantidad_de_participantes" required min="1">
          </div>
        </div>

        <!-- Grupo 5 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Fecha de inicio:</h5>
            <input type="date" class="form-control" id="validationCustom01" v-model="popupItem.fields.fecha_de_inicio" required >
          </div>
          <div class="col-md-4">
            <h5>Fecha de terminación:</h5>
            <input type="date" class="form-control" id="validationCustom01" v-model="popupItem.fields.terminacion" required >
          </div>
          <div class="col-md-4">
            <h5>Valor del contrato:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.valor_del_contrato" required min="1">
          </div>
        </div>

        <!-- Grupo 6 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Margen comercial:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.margen_comercial" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Ingreso bruto:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.ingreso_bruto" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Observaciones:</h5>
            <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.fields.observaciones" required>
          </div>
        </div>

        <!-- Grupo 7 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Gastos de operación desde CETA:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.gastos_de_operacion_desde_CETA" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Ingreso neto planificado:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.ingreso_neto_planificado" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Remuneración:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.remuneracion" required min="1">
          </div>
        </div>

        <!-- Grupo 8 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Norma máxima:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.norma_maxima" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Norma asignada:</h5>
            <input type="number" class="form-control" id="validationCustom01" v-model="popupItem.fields.norma_asignada" required min="1">
          </div>
          <div class="col-md-4">
            <h5>Propuesto por:</h5>
            <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.fields.propuesto_por" required @input="validarNombre(popupItem)">
          </div>
          <div class="col-md-4">
            <h5>Aprobado por:</h5>
            <input type="text" class="form-control" id="validationCustom01" v-model="popupItem.fields.aprobado_por" required @input="validarNombre(popupItem)">
          </div>
        </div>

        <!-- Grupo 9 de campos -->
        <div class="form-group row" style="align-items: baseline;">

          <div class="col-md-4">
            <h5>Listado de programas de cobro:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedProgramaCobro" required>
              <option v-for="programa in lista_programa_cobros" :key="programa.id" :value="programa.id">{{ programa.nombre_programa }}</option>
            </select>
          </div>
          <div class="col-md-4">
            <h5>Listado de áreas participantes:</h5>
            <select multiple class="form-control" id="validationCustom01" v-model="selectedAreaParticipante" required>
              <option v-for="area_participante in lista_area_participante" :key="area_participante.pk" :value="area_participante.pk">{{ area_participante.fields.nombre }}</option>
            </select>
          </div>
        </div>

        <!-- Grupo 10 de campos -->
        <div class="form-group row" style="align-items: baseline;">
          <div class="col-md-4">
            <h5>Servicios:</h5>
            <select single class="form-control" id="validationCustom01" v-model="selectedServicio" required>
              <option v-for="servicio in lista_servicios" :key="servicio.pk" :value="servicio.pk">{{ obtenerNombreServicio(servicio.pk) }}</option>
            </select>
          </div>

        </div>

        <div class="fila">
          <button class="btn btn-icon-text elemento3" @click="guardarCambios" type="submit">
            <img src="/iconos/Confirmar_30px.png" alt="Ícono de Confirmar">

          </button>
          <div class="espacio"></div>
          <button class="btn btn-icon-text elemento4" id="cerrarPopup" @click="cerrarPopup">
            <img src="/iconos/Cancelar_30px.png" alt="Ícono de Cancelar">

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
      lista_contratos: [], // Array para almacenar los datos de la API
      showSuccessMessage: false,
      showSuccessMessageUpdate: false,
      popupItem: null,
      popupItemNuevo: null,
      showErrorMessage: false,
      showSuccessMessageInsertar:false,
      mostrarPopup: false, // Variable para controlar la visibilidad del pop-up
      mostrarPopup_de_Insertar: false, // Variable para controlar la visibilidad del pop-up


      contrato_dado: null,

      showErrorMessage_de_caracter_no_permitido: false,

      lista_servicios: [],
      lista_programa_cobros: [],
      lista_area_participante: [],

      selectedProgramaCobro: [],
      selectedAreaParticipante: [],
      selectedServicio: null,

      //datos del usuario autenticado
      nombre_para_navbar_usuario: "", // Inicializa el nombre de usuario
      usuario_para_navbar_autenticado:"",
      lista_para_navbar_usuario: [],
      lista_para_navbar_rol: [],
      nombre_del_rol_para_navbar: "",


      menssage_no_se_puede_eliminar_o_modificar_contrato:false,
      usuario_autenticado_con_todos_sus_datos: null,


      nombreCompletoUsuario:'',
    };

  },

  // estos metodos se ejecutan automaticamente cuando la pagina este cargada
  mounted() {
    this.obtenerContratos();
    this.obtenerListaServicio();
    this.obtenerListaProgramaCobro();
    this.obtenerListaAreaParticipante();

    // Recupera el nombre de usuario de localStorage
    this.nombre_para_navbar_usuario = localStorage.getItem('nombre_usuario');
    this.obtenerNombreDeRolParaElNavBar();

    // Cuando se monta el componente, obtén el nombre completo del usuario
    this.obtenerNombreCompletoDeUsuarioParaComprobarSICreoElContrato();
  },

  methods: {
    obtenerContratos() {
      axios.get('http://127.0.0.1:8000/api/contratos/0')
          .then(response => {

            this.lista_contratos = JSON.parse(response.data["contratos"]);
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerContratoPorID(id) {
      axios.get(`http://127.0.0.1:8000/api/contratos/${id}`)
          .then(response => {

            this.contrato_dado = JSON.parse(response.data["contrato"]);
            //console.log(this.contrato_dado)
        //    console.log(response)
          })
          .catch(error => {
            console.error(error);
          });
    },

    eliminar_contratos(id){
    // this.obtenerContratoPorID(id);

      axios.get(`http://127.0.0.1:8000/api/contratos/${id}`)
          .then(response => {

            this.contrato_dado = JSON.parse(response.data["contrato"]);
            //console.log(this.contrato_dado)
            //    console.log(response)

            if (this.contrato_dado.fields.propuesto_por != this.usuario_autenticado_con_todos_sus_datos.nombre_completo) {
              // Mostrar un mensaje de advertencia o tomar la acción apropiada
              // Por ejemplo, puedes mostrar un mensaje de error o simplemente no permitir la eliminación
              this.menssage_no_se_puede_eliminar_o_modificar_contrato = true;
              // Mostrar un mensaje de error
              setTimeout(() => {
                this.menssage_no_se_puede_eliminar_o_modificar_contrato = false; // Ocultar mensaje de error después de unos segundos
              }, 3000);

              return; // Salir de la función sin eliminar el contrato
            }
          })
          .catch(error => {
            console.error(error);
          });



      //const url = 'http://127.0.0.1:8000/api/tipo_de_moneda/delete/${id}';
      const url = `http://127.0.0.1:8000/api/contratos/delete/${id}`;
      axios.delete(url)
          .then(response => {
            this.obtenerContratos();

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

    if (this.popupItem.fields.version === '' || this.popupItem.fields.CES === '' || this.popupItem.fields.titulo === '' || this.popupItem.fields.numero === ''
        || this.popupItem.fields.grupo_ejecutor_del_contrato === '' || this.popupItem.fields.cliente === '' || this.popupItem.fields.gestor === '' || this.popupItem.fields.producto === ''
        || this.popupItem.fields.codigo === '' || this.selectedServicio === null || this.popupItem.fields.localizacion_del_cliente === '' || this.popupItem.fields.coordinador_del_contrato === ''
        || this.popupItem.fields.cantidad_de_participantes === 0 || this.popupItem.fields.fecha_de_inicio === null || this.popupItem.fields.terminacion === null || this.popupItem.fields.valor_del_contrato === 0
        || this.popupItem.fields.margen_comercial === 0|| this.popupItem.fields.ingreso_bruto === 0 || this.popupItem.fields.observaciones === '' || this.popupItem.fields.gastos_de_operacion_desde_CETA === 0
        || this.popupItem.fields.ingreso_neto_planificado === 0 || this.popupItem.fields.remuneracion === 0 || this.popupItem.fields.norma_maxima === 0 || this.popupItem.fields.norma_asignada === 0
        || this.popupItem.fields.propuesto_por === '' || this.popupItem.fields.aprobado_por === '' || this.selectedProgramaCobro.length === 0 || this.selectedAreaParticipante.length === 0 || this.popupItem.fields.codigo === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }

    console.log(this.selectedServicio)


      const url = `http://127.0.0.1:8000/api/contratos/put/${this.popupItem.pk}`;


      const payload = {

        version: this.popupItem.fields.version,
        CES: this.popupItem.fields.CES,
        titulo: this.popupItem.fields.titulo,
        numero: this.popupItem.fields.numero,
        grupo_ejecutor_del_contrato: this.popupItem.fields.grupo_ejecutor_del_contrato,
        cliente : this.popupItem.fields.cliente,
        gestor: this.popupItem.fields.gestor,
        producto: this.popupItem.fields.producto,
        codigo: this.popupItem.fields.codigo,
        id_servicio: this.selectedServicio,
        localizacion_del_cliente: this.popupItem.fields.localizacion_del_cliente,
        coordinador_del_contrato: this.popupItem.fields.coordinador_del_contrato,
        cantidad_de_participantes: this.popupItem.fields.cantidad_de_participantes,
        fecha_de_inicio: this.popupItem.fields.fecha_de_inicio,
        terminacion: this.popupItem.fields.terminacion,
        valor_del_contrato: this.popupItem.fields.valor_del_contrato,
        margen_comercial: this.popupItem.fields.margen_comercial,
        ingreso_bruto: this.popupItem.fields.ingreso_bruto,
        observaciones: this.popupItem.fields.observaciones,
        gastos_de_operacion_desde_CETA: this.popupItem.fields.gastos_de_operacion_desde_CETA,
        ingreso_neto_planificado: this.popupItem.fields.ingreso_neto_planificado,
        remuneracion: this.popupItem.fields.remuneracion,
        norma_maxima: this.popupItem.fields.norma_maxima,
        norma_asignada: this.popupItem.fields.norma_asignada,
        propuesto_por: this.popupItem.fields.propuesto_por,
        aprobado_por: this.popupItem.fields.aprobado_por,
        lista_programa_de_cobro: this.selectedProgramaCobro,
        lista_area_participante: this.selectedAreaParticipante,


        // Otros campos a modificar si es necesario
      };

      axios.put(url, payload)
          .then(response => {

            this.popupItem.version = '';
            this.popupItem.CES = '';
            this.popupItem.titulo = '';
            this.popupItem.numero = '';
            this.popupItem.grupo_ejecutor_del_contrato = '';
            this.popupItem.cliente = '';
            this.popupItem.gestor = '';
            this.popupItem.producto = '';
            this.popupItem.codigo = '';
            this.selectedServicio = null;
            this.popupItem.localizacion_del_cliente = '';
            this.popupItem.coordinador_del_contrato = '';
            this.popupItem.cantidad_de_participantes = '';
            this.popupItem.fecha_de_inicio = null;
            this.popupItem.terminacion = null;
            this.popupItem.valor_del_contrato = 0;
            this.popupItem.margen_comercial = 0;
            this.popupItem.ingreso_bruto = 0;
            this.popupItem.observaciones = '';
            this.popupItem.gastos_de_operacion_desde_CETA = 0;
            this.popupItem.ingreso_neto_planificado = 0;
            this.popupItem.remuneracion = 0;
            this.popupItem.norma_maxima = 0;
            this.popupItem.norma_asignada = 0;
            this.popupItem.propuesto_por = '';
            this.popupItem.aprobado_por = '';
            this.selectedProgramaCobro = null;
            this.selectedAreaParticipante = null;


            this.obtenerContratos(); // Actualizar la tabla si es necesario
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


    guardar_nuevo_contrato() {
      if (this.popupItemNuevo.version === '' || this.popupItemNuevo.CES === '' || this.popupItemNuevo.titulo === '' || this.popupItemNuevo.numero === ''
          || this.popupItemNuevo.grupo_ejecutor_del_contrato === '' || this.popupItemNuevo.cliente === '' || this.popupItemNuevo.gestor === '' || this.popupItemNuevo.producto === ''
          || this.popupItemNuevo.codigo === '' || this.selectedServicio === null || this.popupItemNuevo.localizacion_del_cliente === '' || this.popupItemNuevo.coordinador_del_contrato === ''
          || this.popupItemNuevo.cantidad_de_participantes === 0 || this.popupItemNuevo.fecha_de_inicio === null || this.popupItemNuevo.terminacion === null || this.popupItemNuevo.valor_del_contrato === 0
          || this.popupItemNuevo.margen_comercial === 0|| this.popupItemNuevo.ingreso_bruto === 0 || this.popupItemNuevo.observaciones === '' || this.popupItemNuevo.gastos_de_operacion_desde_CETA === 0
          || this.popupItemNuevo.ingreso_neto_planificado === 0 || this.popupItemNuevo.remuneracion === 0 || this.popupItemNuevo.norma_maxima === 0 || this.popupItemNuevo.norma_asignada === 0
          || this.popupItemNuevo.propuesto_por === ''  || this.selectedProgramaCobro.length === 0 || this.selectedAreaParticipante.length === 0 || this.popupItemNuevo.codigo === '') {
        // Mostrar mensaje de error si el campo está vacío
        this.showErrorMessage = true;
        setTimeout(() => {
          this.showErrorMessage = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
        return;
      }


      console.log(this.selectedServicio)
     /* axios.get(`http://127.0.0.1:8000/api/servicios/${this.selectedServicio}`)
          .then(response => {
            console.log(response)
            this.selectedServicio = response.data.servicio; // Asigna el objeto servicio
          })
          .catch(error => {
            console.error(error);
          });*/
     console.log(this.selectedServicio)
      this.selectedServicio = parseInt(this.selectedServicio);


      const url = 'http://127.0.0.1:8000/api/contratos/post/';
      const payload = {

        version: this.popupItemNuevo.version,
        CES: this.popupItemNuevo.CES,
        titulo: this.popupItemNuevo.titulo,
        numero: this.popupItemNuevo.numero,
        grupo_ejecutor_del_contrato: this.popupItemNuevo.grupo_ejecutor_del_contrato,
        cliente : this.popupItemNuevo.cliente,
        gestor: this.popupItemNuevo.gestor,
        producto: this.popupItemNuevo.producto,
        codigo: this.popupItemNuevo.codigo,
        id_servicio: this.selectedServicio,
        localizacion_del_cliente: this.popupItemNuevo.localizacion_del_cliente,
        coordinador_del_contrato: this.popupItemNuevo.coordinador_del_contrato,
        cantidad_de_participantes: this.popupItemNuevo.cantidad_de_participantes,
        fecha_de_inicio: this.popupItemNuevo.fecha_de_inicio,
        terminacion: this.popupItemNuevo.terminacion,
        valor_del_contrato: this.popupItemNuevo.valor_del_contrato,
        margen_comercial: this.popupItemNuevo.margen_comercial,
        ingreso_bruto: this.popupItemNuevo.ingreso_bruto,
        observaciones: this.popupItemNuevo.observaciones,
        gastos_de_operacion_desde_CETA: this.popupItemNuevo.gastos_de_operacion_desde_CETA,
        ingreso_neto_planificado: this.popupItemNuevo.ingreso_neto_planificado,
        remuneracion: this.popupItemNuevo.remuneracion,
        norma_maxima: this.popupItemNuevo.norma_maxima,
        norma_asignada: this.popupItemNuevo.norma_asignada,
        propuesto_por: this.popupItemNuevo.propuesto_por,
        aprobado_por: this.popupItemNuevo.aprobado_por,
        lista_programa_de_cobro: this.selectedProgramaCobro,
        lista_area_participante: this.selectedAreaParticipante,


        // Otros campos a insertar si es necesario

      };

      axios.post(url, payload)
          .then(response => {
            // Lógica después de crear el contrato

            this.popupItemNuevo.version = '';
            this.popupItemNuevo.CES = '';
            this.popupItemNuevo.titulo = '';
            this.popupItemNuevo.numero = '';
            this.popupItemNuevo.grupo_ejecutor_del_contrato = '';
            this.popupItemNuevo.cliente = '';
            this.popupItemNuevo.gestor = '';
            this.popupItemNuevo.producto = '';
            this.popupItemNuevo.codigo = '';
            this.selectedServicio = null;
            this.popupItemNuevo.localizacion_del_cliente = '';
            this.popupItemNuevo.coordinador_del_contrato = '';
            this.popupItemNuevo.cantidad_de_participantes = '';
            this.popupItemNuevo.fecha_de_inicio = null;
            this.popupItemNuevo.terminacion = null;
            this.popupItemNuevo.valor_del_contrato = 0;
            this.popupItemNuevo.margen_comercial = 0;
            this.popupItemNuevo.ingreso_bruto = 0;
            this.popupItemNuevo.observaciones = '';
            this.popupItemNuevo.gastos_de_operacion_desde_CETA = 0;
            this.popupItemNuevo.ingreso_neto_planificado = 0;
            this.popupItemNuevo.remuneracion = 0;
            this.popupItemNuevo.norma_maxima = 0;
            this.popupItemNuevo.norma_asignada = 0;
            this.popupItemNuevo.propuesto_por = '';
            this.popupItemNuevo.aprobado_por = '';
            this.selectedProgramaCobro = null;
            this.selectedAreaParticipante = null;




            this.showSuccessMessageInsertar = true; // Mostrar mensaje de éxito
            this.showErrorMessage = false; // Ocultar mensaje de error

            this.obtenerContratos(); // Actualizar la tabla si es necesario
            this.cerrarPopupInsertar(); // Cerrar el popup después de insertar

            setTimeout(() => {
              this.showSuccessMessageInsertar = false; // Ocultar mensaje de éxito después de unos segundos
            }, 3000);
          })
          .catch(error => {
            console.error(error);
          });
    },

    //cargamos la lista de servicios desde la llamada a la API


    obtenerListaServicio(){
      axios.get('http://127.0.0.1:8000/api/servicios/0')
          .then(response => {
            // this.tipos_productos = response.data["Tipos de productos"]; // Actualizar los datos en la tabla
            //  console.log(response);
           // this.lista_servicios = response.data["servicio"];
            this.lista_servicios = JSON.parse(response.data["servicio"]);


          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreServicio(id_servicio) {

      //console.log("id_plazo: "+id_plazo)
      if (this.lista_servicios.length > 0) {
        const servicioId = parseInt(id_servicio); // Asegurarse de que id_plazo sea un número
        const servicio = this.lista_servicios.find(p => p.pk === servicioId);

        if (servicio) {
          return servicio.fields.nombre_servicio;
        }
      }
      return 'Servicio no encontrado';
    },

//cargamos la lista de programas de cobro desde la llamada a la API
    obtenerListaProgramaCobro(){
      axios.get('http://127.0.0.1:8000/api/programa_de_cobro/0')
          .then(response => {
            // this.tipos_productos = response.data["Tipos de productos"]; // Actualizar los datos en la tabla
            //  console.log(response);
            this.lista_programa_cobros = response.data["programa_de_cobro"];
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreProgramaCobro(id_programa_cobro) {

      //console.log("id_plazo: "+id_plazo)
      if (this.lista_programa_cobros.length > 0) {
        const programaId = parseInt(id_programa_cobro); // Asegurarse de que id_plazo sea un número
        const programa_cobro = this.lista_programa_cobros.find(p => p.id === programaId);

        if (programa_cobro) {
          return programa_cobro.nombre_programa;
        }
      }
      return 'Servicio no encontrado';
    },

    //cargamos la lista de areas participantes desde la llamada a la API
    obtenerListaAreaParticipante(){
      axios.get('http://127.0.0.1:8000/api/area_participante/0')
          .then(response => {
            // this.tipos_productos = response.data["Tipos de productos"]; // Actualizar los datos en la tabla
            //  console.log(response);
            this.lista_area_participante = JSON.parse(response.data["áreas"]);
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreAreaParticipante(id_area) {

      if (this.lista_area_participante.length > 0) {
        const areaId = parseInt(id_area); // Asegurarse de que id_plazo sea un número
        const area_participante = this.lista_area_participante.find(p => p.pk === areaId);

        if (area_participante) {
          return area_participante.fields.nombre;
        }
      }
      return 'Área participante no encontrada';
    },





///////////// funcione para validar
    //////////validar nombre

  /*  validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-Z\s]*$/;

      if (!regex.test(item.nombre)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.nombre = item.nombre.replace(/[^a-zA-Z\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
    },*/

    validarNombre(item) {
      // Expresión regular que permite letras (mayúsculas y minúsculas) y espacios en blanco
      const regex = /^[a-zA-ZÁáÉéÍíÓóÚúÜü\s]*$/;

      if (!regex.test(item.propuesto_por)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.propuesto_por = item.propuesto_por.replace(/[^a-zA-ZÁáÉéÍíÓóÚúÜü\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
      }
      else if (!regex.test(item.aprobado_por)) {
        // Si el valor no coincide con la expresión regular, eliminar caracteres no válidos
        item.aprobado_por = item.aprobado_por.replace(/[^a-zA-Z\s]/g, '');

        // Mostrar un mensaje de error
        this.showErrorMessage_de_caracter_no_permitido = true;
        setTimeout(() => {
          this.showErrorMessage_de_caracter_no_permitido = false; // Ocultar mensaje de error después de unos segundos
        }, 3000);
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
      this.lista_contratos.sort((a, b) => {
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

                  if (this.lista_para_navbar_rol.length > 0) {
                    const id_rol_del_usuario_autenticado = this.usuario_para_navbar_autenticado.id_rol_id;
                    const rolId = parseInt(id_rol_del_usuario_autenticado);
                    const rol = this.lista_para_navbar_rol.find(p => p.id === rolId);
                    if (rol) {
                      // Almacena el nombre del rol en una propiedad de datos
                      this.nombre_del_rol_para_navbar = rol.nombre_rol;
                      localStorage.setItem('nombre_rol', this.nombre_del_rol_para_navbar);

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

    obtenerNombreCompletoDeUsuarioQueCreaElContrato() {
      //cargamos la lista de usuarios desde la llamada a la API
     axios.get('http://127.0.0.1:8000/api/usuarios/0')
          .then(response => {

            this.lista_para_navbar_usuario = response.data["usuarios"];
            this.usuario_autenticado_con_todos_sus_datos = this.lista_para_navbar_usuario.find(p => p.nombre_usuario === this.nombre_para_navbar_usuario);
            this.popupItemNuevo.propuesto_por = this.usuario_autenticado_con_todos_sus_datos.nombre_completo;
          })
          .catch(error => {
            console.error(error);
          });
    },

    obtenerNombreCompletoDeUsuarioParaComprobarSICreoElContrato() {
      //cargamos la lista de usuarios desde la llamada a la API
      axios.get('http://127.0.0.1:8000/api/usuarios/0')
          .then(response => {

            this.lista_para_navbar_usuario = response.data["usuarios"];
            let usuario = this.lista_para_navbar_usuario.find(p => p.nombre_usuario === this.nombre_para_navbar_usuario);
            let nombre_completo = usuario.nombre_completo

            // Configura la variable de datos con el nombre completo del usuario
            this.nombreCompletoUsuario = nombre_completo;
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
      this.obtenerNombreCompletoDeUsuarioQueCreaElContrato();
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

.popup-contenidoContrato {
  background-color: #fff;
  width: 1000px; /* Aumenta el ancho a tu preferencia */
  margin: 100px auto;
  padding: 20px;
  text-align: center;
  border-radius: 10px;
  position: absolute;
  top: 70%;
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