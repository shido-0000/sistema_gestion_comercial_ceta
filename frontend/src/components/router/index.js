import { createRouter, createWebHistory } from 'vue-router';
import inicio from "@/components/paginas/inicio/inicio.vue";
import inicio_sesion from "@/components/paginas/inicio_sesion/LoginForm.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Login",
      component: inicio_sesion,
    },
    {
      path: '/Inicio',
      name: 'Inicio',
      component: inicio,
      beforeEnter: (to, from, next) => {
        const nombreUsuario = localStorage.getItem('nombre_usuario');
        if (nombreUsuario) {
          // Si el usuario está autenticado, permite el acceso a la página de inicio
          next();
        } else {
          // Si el usuario no está autenticado, redirige a la página de inicio de sesión
          next('/');
        }
      },
    },
    {

      path: '/plazos',
      name: 'Lista de plazos',
      component: () => import("@/components/paginas/plazos/lista_plazos.vue"),

    },
    {
      path: '/norma',
      name: 'Lista de normas',
      component: () => import("@/components/paginas/norma/lista_norma.vue"),
    },
  /*  {
      path: '/plazos',
      name: 'Lista de plazos',
      component: () => import("@/components/paginas/plazos/lista_plazos.vue"),
    },*/
    {
      path: '/trabajador',
      name: 'Lista de trabajadores',
      component: () => import("@/components/paginas/trabajador/lista_trabajador.vue"),
    },
    {
      path: '/programa_de_cobro',
      name: 'Lista de programas de cobro',
      component: () => import("@/components/paginas/programa_de_cobro/lista_programa_de_cobro.vue"),
    },
    {
      path: '/rol',
      name: 'rol',
      component: () => import("@/components/paginas/rol/rol.vue"),
    },
    {
      path: '/usuario',
      name: 'usuario',
      component: () => import("@/components/paginas/usuario/usuario.vue"),
    },
    {
      path: '/planificacion_de_gastos_personales',
      name: 'planificacion_de_gastos_personales',
      component: () => import("@/components/paginas/planificacion_de_gastos_personales/planificacion_de_gastos_personales.vue"),
    },
    {
      path: '/servicios',
      name: 'servicios',
      component: () => import("@/components/paginas/servicio/servicio.vue"),
    },
    {
      path: '/area_participante',
      name: 'area_participante',
      component: () => import("@/components/paginas/area_participante/area_participante.vue"),
    },
    {
      path: '/contrato',
      name: 'contrato',
      component: () => import("@/components/paginas/contrato/contratos.vue"),
    },

      //nuevo
    {
      path: '/profesor',
      name: 'Lista de profesores',
      component: () => import("@/components/paginas/profesor/profesor.vue"),
    },
    {
      path: '/categorias_de_profesores_del_servicio',
      name: 'Lista de categorias de profesores del servicio',
      component: () => import("@/components/paginas/categoria_del_profesor_del_servicio/categoria_del_profesor_del_servicio.vue"),
    },

      // Jonathan

    {
      path: '/tareas_detalladas',
      name: 'Lista de tareas detalladas',
      component: () => import("@/components/paginas/ficha_tecnica/tareas_detalladas/tareas_detalladas.vue"),
    },

    {
      path: '/recursos_necesarios',
      name: 'Lista de recursos necesarios',
      component: () => import("@/components/paginas/ficha_tecnica/recursos_necesarios/recursos_necesarios.vue"),
    },

    {
      path: '/productos_necesarios',
      name: 'Lista de productos necesarios',
      component: () => import("@/components/paginas/ficha_tecnica/productos_necesarios/productos_necesarios.vue"),
    },

    {
      path: '/encuetros_por_semana',
      name: 'Lista de encuetros por semana',
      component: () => import("@/components/paginas/ficha_tecnica/encuetros_por_semana/encuetros_por_semana.vue"),
    },

    {
      path: '/resultados_para_ficha_tecnica',
      name: 'Lista de resultados para ficha tecnica',
      component: () => import("@/components/paginas/ficha_tecnica/resultados_para_ficha_tecnica/resultados_para_ficha_tecnica.vue"),
    },

    {
      path: '/resultados_obtenidos_para_ficha_tecnica',
      name: 'Lista de resultados obtenidos para ficha tecnica',
      component: () => import("@/components/paginas/ficha_tecnica/resultados_obtenidos_para_ficha_tecnica/resultados_obtenidos_para_ficha_tecnica.vue"),
    },

    {
      path: '/control_de_documentos_del_contrato',
      name: 'Lista de control de documentos del contrato',
      component: () => import("@/components/paginas/ficha_tecnica/control_de_documentos_del_contrato/control_de_documentos_del_contrato.vue"),
    },

    {
      path: '/consideraciones_para_la_ficha_tecnica',
      name: 'Lista de consideraciones para la ficha tecnica',
      component: () => import("@/components/paginas/ficha_tecnica/consideraciones_para_la_ficha_tecnica/consideraciones_para_la_ficha_tecnica.vue"),
    },

    {
      path: '/valor_del_contrato_por_los_servicios_comercializados',
      name: 'Lista de valor del contrato por los servicios comercializados',
      component: () => import("@/components/paginas/ficha_tecnica/valor_del_contrato_por_los_servicios_comercializados/valor_del_contrato_por_los_servicios_comercializados.vue"),
    },

    {
      path: '/pagos_al_cliente',
      name: 'Lista de pagos al cliente',
      component: () => import("@/components/paginas/pagos_al_cliente/pagos_al_cliente.vue"),
    },
    {
      path: '/facturacion_pagos',
      name: 'Lista de facturacion pagos',
      component: () => import("@/components/paginas/facturacion_pagos/facturacion_pagos.vue"),
    },
    {
      path: '/cronograma_para_ficha_tecnica',
      name: 'Lista de cronograma para ficha tecnica',
      component: () => import("@/components/paginas/ficha_tecnica/cronograma_para_ficha_tecnica/cronograma_para_ficha_tecnica.vue"),
    },
    {
      path: '/areas_y_trabajdores_para_la_ficha_tecnica',
      name: 'Lista de areas y trabajdores para la ficha tecnica',
      component: () => import("@/components/paginas/ficha_tecnica/areas_y_trabajdores_para_la_ficha_tecnica/areas_y_trabajdores_para_la_ficha_tecnica.vue"),
    },

    {
      path: '/registros_de_derechos_y_propiedad',
      name: 'Lista de registros de derechos y propiedad',
      component: () => import("@/components/paginas/ficha_tecnica/registros_de_derechos_y_propiedad/registros_de_derechos_y_propiedad.vue"),
    },
  ]
});

// Agregamos una guarda global para verificar el rol del usuario
router.beforeEach((to, from, next) => {
  const nombreUsuario = localStorage.getItem('nombre_usuario');
  const nombreRol = localStorage.getItem('nombre_del_rol'); // Supongamos que tienes una variable en localStorage para el rol

  if (to.path.startsWith('/Seguridad') && nombreRol !== 'jefa') {
    // Si el usuario no tiene el rol 'jefa' y está intentando acceder a una página bajo '/seguridad', redirígelo a la página de inicio
    next('/');
  } else {
    // De lo contrario, permite el acceso normalmente
    next();
  }
});
export default router;
