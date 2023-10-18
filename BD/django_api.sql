-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-10-2023 a las 07:47:13
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `django_api`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_area_participante`
--

CREATE TABLE `api_area_participante` (
  `id` bigint(20) NOT NULL,
  `nombre` longtext NOT NULL,
  `porcentaje` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_area_participante`
--

INSERT INTO `api_area_participante` (`id`, `nombre`, `porcentaje`) VALUES
(1, 'area1', 22),
(2, 'area', 25);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_area_participante_lista_trabajador`
--

CREATE TABLE `api_area_participante_lista_trabajador` (
  `id` bigint(20) NOT NULL,
  `area_participante_id` bigint(20) NOT NULL,
  `trabajador_id` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_categoria_del_profesor_del_servicio`
--

CREATE TABLE `api_categoria_del_profesor_del_servicio` (
  `id` bigint(20) NOT NULL,
  `nombre_categoria` longtext NOT NULL,
  `tarifa_por_hora` double NOT NULL,
  `total_de_horas` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_categoria_del_profesor_del_servicio`
--

INSERT INTO `api_categoria_del_profesor_del_servicio` (`id`, `nombre_categoria`, `tarifa_por_hora`, `total_de_horas`) VALUES
(1, 'wwww', 4, 4),
(3, 'z', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_consideraciones_para_la_ficha_tecnica`
--

CREATE TABLE `api_consideraciones_para_la_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_consideraciones_para_la_ficha_tecnica`
--

INSERT INTO `api_consideraciones_para_la_ficha_tecnica` (`id`, `descripcion`) VALUES
(2, 'asd'),
(3, 'ddd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_contrato`
--

CREATE TABLE `api_contrato` (
  `id` bigint(20) NOT NULL,
  `version` varchar(5) NOT NULL,
  `CES` longtext NOT NULL,
  `titulo` longtext NOT NULL,
  `numero` longtext NOT NULL,
  `grupo_ejecutor_del_contrato` longtext NOT NULL,
  `cliente` longtext NOT NULL,
  `gestor` longtext NOT NULL,
  `producto` longtext NOT NULL,
  `codigo` longtext NOT NULL,
  `localizacion_del_cliente` longtext NOT NULL,
  `coordinador_del_contrato` longtext NOT NULL,
  `cantidad_de_participantes` int(11) NOT NULL,
  `fecha_de_inicio` date NOT NULL,
  `terminacion` date NOT NULL,
  `valor_del_contrato` double NOT NULL,
  `margen_comercial` double NOT NULL,
  `ingreso_bruto` double NOT NULL,
  `observaciones` longtext NOT NULL,
  `gastos_de_operacion_desde_CETA` double NOT NULL,
  `ingreso_neto_planificado` double NOT NULL,
  `remuneracion` double NOT NULL,
  `norma_maxima` double NOT NULL,
  `norma_asignada` double NOT NULL,
  `propuesto_por` longtext NOT NULL,
  `aprobado_por` longtext NOT NULL,
  `id_servicio_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_contrato_lista_area_participante`
--

CREATE TABLE `api_contrato_lista_area_participante` (
  `id` bigint(20) NOT NULL,
  `contrato_id` bigint(20) NOT NULL,
  `area_participante_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_contrato_lista_programa_de_cobro`
--

CREATE TABLE `api_contrato_lista_programa_de_cobro` (
  `id` bigint(20) NOT NULL,
  `contrato_id` bigint(20) NOT NULL,
  `programa_de_cobro_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_control_de_documentos_del_contrato`
--

CREATE TABLE `api_control_de_documentos_del_contrato` (
  `id` bigint(20) NOT NULL,
  `nombre_del_documento` longtext NOT NULL,
  `fecha_de_entrega` date NOT NULL,
  `responsable` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_control_de_documentos_del_contrato`
--

INSERT INTO `api_control_de_documentos_del_contrato` (`id`, `nombre_del_documento`, `fecha_de_entrega`, `responsable`) VALUES
(2, 'Nombre ', '2023-10-18', 'Responsable'),
(3, 'documento', '2023-10-21', 'a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_cronograma_para_ficha_tecnica`
--

CREATE TABLE `api_cronograma_para_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `numero_de_la_tarea` int(11) NOT NULL,
  `nombre_completo_de_la_tarea` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_cronograma_para_ficha_tecnica`
--

INSERT INTO `api_cronograma_para_ficha_tecnica` (`id`, `numero_de_la_tarea`, `nombre_completo_de_la_tarea`) VALUES
(1, 5, 'venta'),
(3, 5, 'venta'),
(4, 7, 'asd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
--

CREATE TABLE `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana` (
  `id` bigint(20) NOT NULL,
  `cronograma_para_ficha_tecnica_id` bigint(20) NOT NULL,
  `encuetros_por_semana_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
--

INSERT INTO `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana` (`id`, `cronograma_para_ficha_tecnica_id`, `encuetros_por_semana_id`) VALUES
(1, 1, 2),
(3, 3, 3),
(8, 4, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_empresa`
--

CREATE TABLE `api_empresa` (
  `id` bigint(20) NOT NULL,
  `nombre_empresa` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_empresa_lista_de_contrato`
--

CREATE TABLE `api_empresa_lista_de_contrato` (
  `id` bigint(20) NOT NULL,
  `empresa_id` bigint(20) NOT NULL,
  `contrato_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_empresa_lista_de_seguridad`
--

CREATE TABLE `api_empresa_lista_de_seguridad` (
  `id` bigint(20) NOT NULL,
  `empresa_id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_encuetros_por_semana`
--

CREATE TABLE `api_encuetros_por_semana` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `semana` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_encuetros_por_semana`
--

INSERT INTO `api_encuetros_por_semana` (`id`, `cantidad`, `semana`) VALUES
(2, 2, 3),
(3, 6, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_facturacion_pagos`
--

CREATE TABLE `api_facturacion_pagos` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `valor` double NOT NULL,
  `id_resultados_obtenidos_para_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_facturacion_pagos`
--

INSERT INTO `api_facturacion_pagos` (`id`, `fecha`, `valor`, `id_resultados_obtenidos_para_ficha_tecnica_id`) VALUES
(1, '2023-10-29', 5, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica`
--

CREATE TABLE `api_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha` date NOT NULL,
  `cliente` longtext NOT NULL,
  `objeto` longtext NOT NULL,
  `vigencia` longtext NOT NULL,
  `objetivos_especificos` longtext NOT NULL,
  `informacion_a_entregar_por_el_cliente` longtext NOT NULL,
  `id_area_ejecutora_principal` longtext NOT NULL,
  `coordinador_del_contrato_por_la_cujae` longtext NOT NULL,
  `cargo_del_cliente` longtext NOT NULL,
  `firmado_por_responsable_del_contrato_de_ceta` longtext NOT NULL,
  `id_cronograma_id` bigint(20) NOT NULL,
  `id_valor_del_contrato_por_los_servicios_comercializados_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_area_participante`
--

CREATE TABLE `api_ficha_tecnica_lista_area_participante` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `area_participante_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
--

CREATE TABLE `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `consideraciones_para_la_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
--

CREATE TABLE `api_ficha_tecnica_lista_control_de_documentos_del_contrato` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `control_de_documentos_del_contrato_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
--

CREATE TABLE `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `productos_necesarios_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_facturacion_pagos`
--

CREATE TABLE `api_ficha_tecnica_lista_facturacion_pagos` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `facturacion_pagos_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_pagos_al_cliente`
--

CREATE TABLE `api_ficha_tecnica_lista_pagos_al_cliente` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `pagos_al_cliente_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_recurso_necesarios`
--

CREATE TABLE `api_ficha_tecnica_lista_recurso_necesarios` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `recursos_necesarios_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
--

CREATE TABLE `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `registros_de_derechos_y_propiedad_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_resultados_de_tareas`
--

CREATE TABLE `api_ficha_tecnica_lista_resultados_de_tareas` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `resultados_para_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
--

CREATE TABLE `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `resultados_obtenidos_para_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_tareas_detalladas`
--

CREATE TABLE `api_ficha_tecnica_lista_tareas_detalladas` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `tareas_detalladas_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
--

CREATE TABLE `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales` (
  `id` bigint(20) NOT NULL,
  `ficha_tecnica_id` bigint(20) NOT NULL,
  `tiempo_dedicado_en_horas_mensuales_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_norma`
--

CREATE TABLE `api_norma` (
  `id` bigint(20) NOT NULL,
  `nombre` longtext NOT NULL,
  `cantidad` double NOT NULL,
  `tipo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_norma`
--

INSERT INTO `api_norma` (`id`, `nombre`, `cantidad`, `tipo`) VALUES
(1, 'norma b', 5, 'cc'),
(2, 'norma A', 6, 'xx');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_pagos_al_cliente`
--

CREATE TABLE `api_pagos_al_cliente` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `valor` double NOT NULL,
  `detalles` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_pagos_al_cliente`
--

INSERT INTO `api_pagos_al_cliente` (`id`, `fecha`, `valor`, `detalles`) VALUES
(1, '2023-10-15', 12, 'asd'),
(2, '2023-10-11', 123, 'asd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_planificacion_de_gastos_personales`
--

CREATE TABLE `api_planificacion_de_gastos_personales` (
  `id` bigint(20) NOT NULL,
  `ejecucion_fuera_de_provincia` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_planificacion_de_gastos_personales`
--

INSERT INTO `api_planificacion_de_gastos_personales` (`id`, `ejecucion_fuera_de_provincia`) VALUES
(2, 1),
(3, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_planificacion_de_gastos_personales_lista_trabajador`
--

CREATE TABLE `api_planificacion_de_gastos_personales_lista_trabajador` (
  `id` bigint(20) NOT NULL,
  `planificacion_de_gastos_personales_id` bigint(20) NOT NULL,
  `trabajador_id` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_planificacion_de_gastos_personales_lista_trabajador`
--

INSERT INTO `api_planificacion_de_gastos_personales_lista_trabajador` (`id`, `planificacion_de_gastos_personales_id`, `trabajador_id`) VALUES
(3, 2, '22'),
(5, 3, '22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_plazo`
--

CREATE TABLE `api_plazo` (
  `id` bigint(20) NOT NULL,
  `nombre_plazo` longtext NOT NULL,
  `remuneracion` double NOT NULL,
  `cumplimiento_de_normas` tinyint(1) NOT NULL,
  `total_asignado` double NOT NULL,
  `porcentaje` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_plazo`
--

INSERT INTO `api_plazo` (`id`, `nombre_plazo`, `remuneracion`, `cumplimiento_de_normas`, `total_asignado`, `porcentaje`) VALUES
(1, 'plazo A', 2, 1, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_productos_necesarios`
--

CREATE TABLE `api_productos_necesarios` (
  `id` bigint(20) NOT NULL,
  `nombre_completo` longtext NOT NULL,
  `descripcion` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_productos_necesarios`
--

INSERT INTO `api_productos_necesarios` (`id`, `nombre_completo`, `descripcion`) VALUES
(2, 'b', 'b'),
(3, 'a', 'a');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_programa_de_cobro`
--

CREATE TABLE `api_programa_de_cobro` (
  `id` bigint(20) NOT NULL,
  `nombre_programa` longtext NOT NULL,
  `fecha` date NOT NULL,
  `plan_MN` double NOT NULL,
  `plan_USD` double NOT NULL,
  `remuneracion` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_programa_de_cobro`
--

INSERT INTO `api_programa_de_cobro` (`id`, `nombre_programa`, `fecha`, `plan_MN`, `plan_USD`, `remuneracion`) VALUES
(1, 'asd', '2023-10-12', 12, 12, 12);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_recursos_necesarios`
--

CREATE TABLE `api_recursos_necesarios` (
  `id` bigint(20) NOT NULL,
  `nombre_completo` longtext NOT NULL,
  `descripcion` longtext NOT NULL,
  `cantidad` int(11) NOT NULL,
  `caracteristicas_especiales` longtext NOT NULL,
  `justificacion` longtext NOT NULL,
  `valor_unitario` double NOT NULL,
  `total` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_recursos_necesarios`
--

INSERT INTO `api_recursos_necesarios` (`id`, `nombre_completo`, `descripcion`, `cantidad`, `caracteristicas_especiales`, `justificacion`, `valor_unitario`, `total`) VALUES
(2, 'recurso A', 'Descripción', 14, 'Características especiales', 'Justificación', 12, 168),
(3, 'recurso c', 'pepe1', 20, 'a', 'j', 3, 60);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_registros_de_derechos_y_propiedad`
--

CREATE TABLE `api_registros_de_derechos_y_propiedad` (
  `id` bigint(20) NOT NULL,
  `porcentaje_de_la_cujae` double NOT NULL,
  `porcentaje_del_cliente` double NOT NULL,
  `tipo_de_registro` longtext NOT NULL,
  `id_resultados_obtenidos_para_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_registros_de_derechos_y_propiedad`
--

INSERT INTO `api_registros_de_derechos_y_propiedad` (`id`, `porcentaje_de_la_cujae`, `porcentaje_del_cliente`, `tipo_de_registro`, `id_resultados_obtenidos_para_ficha_tecnica_id`) VALUES
(1, 22, 33, 'asd', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_resultados_obtenidos_para_ficha_tecnica`
--

CREATE TABLE `api_resultados_obtenidos_para_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `nombre_producto_obtenido` longtext NOT NULL,
  `descripcion_producto_obtenido` longtext NOT NULL,
  `tipo_de_registro` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_resultados_obtenidos_para_ficha_tecnica`
--

INSERT INTO `api_resultados_obtenidos_para_ficha_tecnica` (`id`, `nombre_producto_obtenido`, `descripcion_producto_obtenido`, `tipo_de_registro`) VALUES
(2, 'producto1 ', 'Descripción del tipo de entregable:', 'Tipo de registro:'),
(3, 'Nombre del producto:', 'tipo de entregable:', 'registro:');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_resultados_para_ficha_tecnica`
--

CREATE TABLE `api_resultados_para_ficha_tecnica` (
  `id` bigint(20) NOT NULL,
  `numero_de_la_tarea` int(11) NOT NULL,
  `nombre_completo_de_la_tarea` longtext NOT NULL,
  `descripcion_del_tipo_de_entregable` longtext NOT NULL,
  `formato_del_entregable` longtext NOT NULL,
  `fecha_escrita_de_entrega_de_entregable` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_resultados_para_ficha_tecnica`
--

INSERT INTO `api_resultados_para_ficha_tecnica` (`id`, `numero_de_la_tarea`, `nombre_completo_de_la_tarea`, `descripcion_del_tipo_de_entregable`, `formato_del_entregable`, `fecha_escrita_de_entrega_de_entregable`) VALUES
(2, 5, 'bailar', 'digital', 'pdf', 'pasado mañana'),
(3, 5, 'Actividad ', 'Descripción ', 'Formato ', 'Momento '),
(4, 7, 'cumplir ', 'tipo ', 'entregable', 'entrega');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_rol`
--

CREATE TABLE `api_rol` (
  `id` bigint(20) NOT NULL,
  `nombre_rol` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_rol`
--

INSERT INTO `api_rol` (`id`, `nombre_rol`) VALUES
(1, 'Gestor de proyecto'),
(2, 'Admin'),
(3, 'Director de CETA'),
(4, 'Especialista de sistemas'),
(5, 'Especialista económico'),
(6, 'Especialista principal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_servicio`
--

CREATE TABLE `api_servicio` (
  `id` bigint(20) NOT NULL,
  `nombre_servicio` longtext NOT NULL,
  `capacidad_de_matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_servicio`
--

INSERT INTO `api_servicio` (`id`, `nombre_servicio`, `capacidad_de_matricula`) VALUES
(4, 'venta', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_servicio_lista_trabajadores`
--

CREATE TABLE `api_servicio_lista_trabajadores` (
  `id` bigint(20) NOT NULL,
  `servicio_id` bigint(20) NOT NULL,
  `trabajador_id` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_servicio_lista_trabajadores`
--

INSERT INTO `api_servicio_lista_trabajadores` (`id`, `servicio_id`, `trabajador_id`) VALUES
(4, 4, '22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_tareas_detalladas`
--

CREATE TABLE `api_tareas_detalladas` (
  `id` bigint(20) NOT NULL,
  `nombre_completo` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_tareas_detalladas`
--

INSERT INTO `api_tareas_detalladas` (`id`, `nombre_completo`) VALUES
(5, 'venta'),
(7, 'asd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_tiempo_dedicado_en_horas_mensuales`
--

CREATE TABLE `api_tiempo_dedicado_en_horas_mensuales` (
  `id` bigint(20) NOT NULL,
  `horas_dedicadas` int(11) NOT NULL,
  `id_resultados_obtenidos_para_ficha_tecnica_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_trabajador`
--

CREATE TABLE `api_trabajador` (
  `id_trabajador` varchar(11) NOT NULL,
  `nombre` longtext NOT NULL,
  `id_categoria_del_profesor_del_servicio_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_trabajador`
--

INSERT INTO `api_trabajador` (`id_trabajador`, `nombre`, `id_categoria_del_profesor_del_servicio_id`) VALUES
('123', 'asd', 3),
('22', 'shido', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_trabajador_lista_plazo`
--

CREATE TABLE `api_trabajador_lista_plazo` (
  `id` bigint(20) NOT NULL,
  `trabajador_id` varchar(11) NOT NULL,
  `plazo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_trabajador_lista_plazo`
--

INSERT INTO `api_trabajador_lista_plazo` (`id`, `trabajador_id`, `plazo_id`) VALUES
(5, '123', 1),
(1, '22', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_usuario`
--

CREATE TABLE `api_usuario` (
  `id` bigint(20) NOT NULL,
  `nombre_completo` longtext NOT NULL,
  `nombre_usuario` varchar(20) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `id_rol_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_usuario`
--

INSERT INTO `api_usuario` (`id`, `nombre_completo`, `nombre_usuario`, `contrasena`, `id_rol_id`) VALUES
(1, 'Jonathan Perez Dominguez', 'j', '$2a$10$ZXU3aCAJMR12/zrsKtza2Ovuv3h1/CTJTgyHGjNsQgAuGdjMYnFtG', 4),
(2, 'juan perez', 'juan', '$2a$10$0rX95wnbupCeROFc/AM26OsbBWfTK5dEAYWcwRG4ld3jhcnHt3I/q', 1),
(3, 'miguel de leon', 'm', '$2a$10$m.t/Fju8cXIXH3vj09YJGesZ0omSzqxhRQB/ugHDZGJRNiBKiy4tS', 1),
(4, 'Juan Lui', 'director', '$2a$10$tXdJu7tj6SedptFFrGVZautGeup4idPR1Qxp6U9F0fkCBL6EuZyDe', 3),
(5, 'admin', 'admin', '$2a$10$J7RZQ6L0iQ1ccBzJZ0LqIOhjRlDygzqCkODoYOdlDgiJR0VoR/HrK', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_valor_del_contrato_por_los_servicios_comercializados`
--

CREATE TABLE `api_valor_del_contrato_por_los_servicios_comercializados` (
  `id` bigint(20) NOT NULL,
  `valor` double NOT NULL,
  `moneda` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `api_valor_del_contrato_por_los_servicios_comercializados`
--

INSERT INTO `api_valor_del_contrato_por_los_servicios_comercializados` (`id`, `valor`, `moneda`) VALUES
(2, 12, 'MN'),
(3, 22, 'USD');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add area_participante', 7, 'add_area_participante'),
(26, 'Can change area_participante', 7, 'change_area_participante'),
(27, 'Can delete area_participante', 7, 'delete_area_participante'),
(28, 'Can view area_participante', 7, 'view_area_participante'),
(29, 'Can add areas_y_trabajdores_para_la_ficha_tecnica', 8, 'add_areas_y_trabajdores_para_la_ficha_tecnica'),
(30, 'Can change areas_y_trabajdores_para_la_ficha_tecnica', 8, 'change_areas_y_trabajdores_para_la_ficha_tecnica'),
(31, 'Can delete areas_y_trabajdores_para_la_ficha_tecnica', 8, 'delete_areas_y_trabajdores_para_la_ficha_tecnica'),
(32, 'Can view areas_y_trabajdores_para_la_ficha_tecnica', 8, 'view_areas_y_trabajdores_para_la_ficha_tecnica'),
(33, 'Can add categoria_del_profesor_del_servicio', 9, 'add_categoria_del_profesor_del_servicio'),
(34, 'Can change categoria_del_profesor_del_servicio', 9, 'change_categoria_del_profesor_del_servicio'),
(35, 'Can delete categoria_del_profesor_del_servicio', 9, 'delete_categoria_del_profesor_del_servicio'),
(36, 'Can view categoria_del_profesor_del_servicio', 9, 'view_categoria_del_profesor_del_servicio'),
(37, 'Can add consideraciones_para_la_ficha_tecnica', 10, 'add_consideraciones_para_la_ficha_tecnica'),
(38, 'Can change consideraciones_para_la_ficha_tecnica', 10, 'change_consideraciones_para_la_ficha_tecnica'),
(39, 'Can delete consideraciones_para_la_ficha_tecnica', 10, 'delete_consideraciones_para_la_ficha_tecnica'),
(40, 'Can view consideraciones_para_la_ficha_tecnica', 10, 'view_consideraciones_para_la_ficha_tecnica'),
(41, 'Can add contrato', 11, 'add_contrato'),
(42, 'Can change contrato', 11, 'change_contrato'),
(43, 'Can delete contrato', 11, 'delete_contrato'),
(44, 'Can view contrato', 11, 'view_contrato'),
(45, 'Can add control_de_documentos_del_contrato', 12, 'add_control_de_documentos_del_contrato'),
(46, 'Can change control_de_documentos_del_contrato', 12, 'change_control_de_documentos_del_contrato'),
(47, 'Can delete control_de_documentos_del_contrato', 12, 'delete_control_de_documentos_del_contrato'),
(48, 'Can view control_de_documentos_del_contrato', 12, 'view_control_de_documentos_del_contrato'),
(49, 'Can add cronograma_para_ficha_tecnica', 13, 'add_cronograma_para_ficha_tecnica'),
(50, 'Can change cronograma_para_ficha_tecnica', 13, 'change_cronograma_para_ficha_tecnica'),
(51, 'Can delete cronograma_para_ficha_tecnica', 13, 'delete_cronograma_para_ficha_tecnica'),
(52, 'Can view cronograma_para_ficha_tecnica', 13, 'view_cronograma_para_ficha_tecnica'),
(53, 'Can add encuetros_por_semana', 14, 'add_encuetros_por_semana'),
(54, 'Can change encuetros_por_semana', 14, 'change_encuetros_por_semana'),
(55, 'Can delete encuetros_por_semana', 14, 'delete_encuetros_por_semana'),
(56, 'Can view encuetros_por_semana', 14, 'view_encuetros_por_semana'),
(57, 'Can add facturacion_pagos', 15, 'add_facturacion_pagos'),
(58, 'Can change facturacion_pagos', 15, 'change_facturacion_pagos'),
(59, 'Can delete facturacion_pagos', 15, 'delete_facturacion_pagos'),
(60, 'Can view facturacion_pagos', 15, 'view_facturacion_pagos'),
(61, 'Can add norma', 16, 'add_norma'),
(62, 'Can change norma', 16, 'change_norma'),
(63, 'Can delete norma', 16, 'delete_norma'),
(64, 'Can view norma', 16, 'view_norma'),
(65, 'Can add pagos_al_cliente', 17, 'add_pagos_al_cliente'),
(66, 'Can change pagos_al_cliente', 17, 'change_pagos_al_cliente'),
(67, 'Can delete pagos_al_cliente', 17, 'delete_pagos_al_cliente'),
(68, 'Can view pagos_al_cliente', 17, 'view_pagos_al_cliente'),
(69, 'Can add plazo', 18, 'add_plazo'),
(70, 'Can change plazo', 18, 'change_plazo'),
(71, 'Can delete plazo', 18, 'delete_plazo'),
(72, 'Can view plazo', 18, 'view_plazo'),
(73, 'Can add productos_necesarios', 19, 'add_productos_necesarios'),
(74, 'Can change productos_necesarios', 19, 'change_productos_necesarios'),
(75, 'Can delete productos_necesarios', 19, 'delete_productos_necesarios'),
(76, 'Can view productos_necesarios', 19, 'view_productos_necesarios'),
(77, 'Can add programa_de_cobro', 20, 'add_programa_de_cobro'),
(78, 'Can change programa_de_cobro', 20, 'change_programa_de_cobro'),
(79, 'Can delete programa_de_cobro', 20, 'delete_programa_de_cobro'),
(80, 'Can view programa_de_cobro', 20, 'view_programa_de_cobro'),
(81, 'Can add recursos_necesarios', 21, 'add_recursos_necesarios'),
(82, 'Can change recursos_necesarios', 21, 'change_recursos_necesarios'),
(83, 'Can delete recursos_necesarios', 21, 'delete_recursos_necesarios'),
(84, 'Can view recursos_necesarios', 21, 'view_recursos_necesarios'),
(85, 'Can add resultados_obtenidos_para_ficha_tecnica', 22, 'add_resultados_obtenidos_para_ficha_tecnica'),
(86, 'Can change resultados_obtenidos_para_ficha_tecnica', 22, 'change_resultados_obtenidos_para_ficha_tecnica'),
(87, 'Can delete resultados_obtenidos_para_ficha_tecnica', 22, 'delete_resultados_obtenidos_para_ficha_tecnica'),
(88, 'Can view resultados_obtenidos_para_ficha_tecnica', 22, 'view_resultados_obtenidos_para_ficha_tecnica'),
(89, 'Can add resultados_para_ficha_tecnica', 23, 'add_resultados_para_ficha_tecnica'),
(90, 'Can change resultados_para_ficha_tecnica', 23, 'change_resultados_para_ficha_tecnica'),
(91, 'Can delete resultados_para_ficha_tecnica', 23, 'delete_resultados_para_ficha_tecnica'),
(92, 'Can view resultados_para_ficha_tecnica', 23, 'view_resultados_para_ficha_tecnica'),
(93, 'Can add rol', 24, 'add_rol'),
(94, 'Can change rol', 24, 'change_rol'),
(95, 'Can delete rol', 24, 'delete_rol'),
(96, 'Can view rol', 24, 'view_rol'),
(97, 'Can add tareas_detalladas', 25, 'add_tareas_detalladas'),
(98, 'Can change tareas_detalladas', 25, 'change_tareas_detalladas'),
(99, 'Can delete tareas_detalladas', 25, 'delete_tareas_detalladas'),
(100, 'Can view tareas_detalladas', 25, 'view_tareas_detalladas'),
(101, 'Can add valor_del_contrato_por_los_servicios_comercializados', 26, 'add_valor_del_contrato_por_los_servicios_comercializados'),
(102, 'Can change valor_del_contrato_por_los_servicios_comercializados', 26, 'change_valor_del_contrato_por_los_servicios_comercializados'),
(103, 'Can delete valor_del_contrato_por_los_servicios_comercializados', 26, 'delete_valor_del_contrato_por_los_servicios_comercializados'),
(104, 'Can view valor_del_contrato_por_los_servicios_comercializados', 26, 'view_valor_del_contrato_por_los_servicios_comercializados'),
(105, 'Can add usuario', 27, 'add_usuario'),
(106, 'Can change usuario', 27, 'change_usuario'),
(107, 'Can delete usuario', 27, 'delete_usuario'),
(108, 'Can view usuario', 27, 'view_usuario'),
(109, 'Can add trabajador', 28, 'add_trabajador'),
(110, 'Can change trabajador', 28, 'change_trabajador'),
(111, 'Can delete trabajador', 28, 'delete_trabajador'),
(112, 'Can view trabajador', 28, 'view_trabajador'),
(113, 'Can add tiempo_dedicado_en_horas_mensuales', 29, 'add_tiempo_dedicado_en_horas_mensuales'),
(114, 'Can change tiempo_dedicado_en_horas_mensuales', 29, 'change_tiempo_dedicado_en_horas_mensuales'),
(115, 'Can delete tiempo_dedicado_en_horas_mensuales', 29, 'delete_tiempo_dedicado_en_horas_mensuales'),
(116, 'Can view tiempo_dedicado_en_horas_mensuales', 29, 'view_tiempo_dedicado_en_horas_mensuales'),
(117, 'Can add servicio', 30, 'add_servicio'),
(118, 'Can change servicio', 30, 'change_servicio'),
(119, 'Can delete servicio', 30, 'delete_servicio'),
(120, 'Can view servicio', 30, 'view_servicio'),
(121, 'Can add registros_de_derechos_y_propiedad', 31, 'add_registros_de_derechos_y_propiedad'),
(122, 'Can change registros_de_derechos_y_propiedad', 31, 'change_registros_de_derechos_y_propiedad'),
(123, 'Can delete registros_de_derechos_y_propiedad', 31, 'delete_registros_de_derechos_y_propiedad'),
(124, 'Can view registros_de_derechos_y_propiedad', 31, 'view_registros_de_derechos_y_propiedad'),
(125, 'Can add planificacion_de_gastos_personales', 32, 'add_planificacion_de_gastos_personales'),
(126, 'Can change planificacion_de_gastos_personales', 32, 'change_planificacion_de_gastos_personales'),
(127, 'Can delete planificacion_de_gastos_personales', 32, 'delete_planificacion_de_gastos_personales'),
(128, 'Can view planificacion_de_gastos_personales', 32, 'view_planificacion_de_gastos_personales'),
(129, 'Can add ficha_tecnica', 33, 'add_ficha_tecnica'),
(130, 'Can change ficha_tecnica', 33, 'change_ficha_tecnica'),
(131, 'Can delete ficha_tecnica', 33, 'delete_ficha_tecnica'),
(132, 'Can view ficha_tecnica', 33, 'view_ficha_tecnica'),
(133, 'Can add empresa', 34, 'add_empresa'),
(134, 'Can change empresa', 34, 'change_empresa'),
(135, 'Can delete empresa', 34, 'delete_empresa'),
(136, 'Can view empresa', 34, 'view_empresa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'api', 'areas_y_trabajdores_para_la_ficha_tecnica'),
(7, 'api', 'area_participante'),
(9, 'api', 'categoria_del_profesor_del_servicio'),
(10, 'api', 'consideraciones_para_la_ficha_tecnica'),
(11, 'api', 'contrato'),
(12, 'api', 'control_de_documentos_del_contrato'),
(13, 'api', 'cronograma_para_ficha_tecnica'),
(34, 'api', 'empresa'),
(14, 'api', 'encuetros_por_semana'),
(15, 'api', 'facturacion_pagos'),
(33, 'api', 'ficha_tecnica'),
(16, 'api', 'norma'),
(17, 'api', 'pagos_al_cliente'),
(32, 'api', 'planificacion_de_gastos_personales'),
(18, 'api', 'plazo'),
(19, 'api', 'productos_necesarios'),
(20, 'api', 'programa_de_cobro'),
(21, 'api', 'recursos_necesarios'),
(31, 'api', 'registros_de_derechos_y_propiedad'),
(22, 'api', 'resultados_obtenidos_para_ficha_tecnica'),
(23, 'api', 'resultados_para_ficha_tecnica'),
(24, 'api', 'rol'),
(30, 'api', 'servicio'),
(25, 'api', 'tareas_detalladas'),
(29, 'api', 'tiempo_dedicado_en_horas_mensuales'),
(28, 'api', 'trabajador'),
(27, 'api', 'usuario'),
(26, 'api', 'valor_del_contrato_por_los_servicios_comercializados'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-15 06:35:15.092215'),
(2, 'auth', '0001_initial', '2023-10-15 06:35:23.161100'),
(3, 'admin', '0001_initial', '2023-10-15 06:35:24.712378'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-15 06:35:24.759465'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-15 06:35:24.792011'),
(6, 'api', '0001_initial', '2023-10-15 06:36:28.630690'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-10-15 06:36:30.019088'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-10-15 06:36:30.899514'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-10-15 06:36:31.211922'),
(10, 'auth', '0004_alter_user_username_opts', '2023-10-15 06:36:31.358530'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-10-15 06:36:32.332256'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-10-15 06:36:32.384040'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-10-15 06:36:32.425846'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-10-15 06:36:32.512299'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-10-15 06:36:32.665521'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-10-15 06:36:32.803912'),
(17, 'auth', '0011_update_proxy_permissions', '2023-10-15 06:36:32.865279'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-10-15 06:36:32.955286'),
(19, 'sessions', '0001_initial', '2023-10-15 06:36:33.493599'),
(20, 'api', '0002_remove_servicio_lista_categorias_and_more', '2023-10-17 09:24:04.747560'),
(21, 'api', '0003_remove_ficha_tecnica_lista_areas_y_trabajdores_para_la_ficha_tecnica_and_more', '2023-10-17 12:46:16.792853');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `api_area_participante`
--
ALTER TABLE `api_area_participante`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_area_participante_lista_trabajador`
--
ALTER TABLE `api_area_participante_lista_trabajador`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_area_participante_li_area_participante_id_tra_b1dfb451_uniq` (`area_participante_id`,`trabajador_id`),
  ADD KEY `api_area_participant_trabajador_id_482be9e6_fk_api_traba` (`trabajador_id`);

--
-- Indices de la tabla `api_categoria_del_profesor_del_servicio`
--
ALTER TABLE `api_categoria_del_profesor_del_servicio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_consideraciones_para_la_ficha_tecnica`
--
ALTER TABLE `api_consideraciones_para_la_ficha_tecnica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_contrato`
--
ALTER TABLE `api_contrato`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_contrato_id_servicio_id_90bd9984_fk_api_servicio_id` (`id_servicio_id`);

--
-- Indices de la tabla `api_contrato_lista_area_participante`
--
ALTER TABLE `api_contrato_lista_area_participante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_contrato_lista_area__contrato_id_area_partici_52ab1ff8_uniq` (`contrato_id`,`area_participante_id`),
  ADD KEY `api_contrato_lista_a_area_participante_id_ef3d0bca_fk_api_area_` (`area_participante_id`);

--
-- Indices de la tabla `api_contrato_lista_programa_de_cobro`
--
ALTER TABLE `api_contrato_lista_programa_de_cobro`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_contrato_lista_progr_contrato_id_programa_de__ff826736_uniq` (`contrato_id`,`programa_de_cobro_id`),
  ADD KEY `api_contrato_lista_p_programa_de_cobro_id_86d3b62f_fk_api_progr` (`programa_de_cobro_id`);

--
-- Indices de la tabla `api_control_de_documentos_del_contrato`
--
ALTER TABLE `api_control_de_documentos_del_contrato`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_cronograma_para_ficha_tecnica`
--
ALTER TABLE `api_cronograma_para_ficha_tecnica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
--
ALTER TABLE `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_cronograma_para_fich_cronograma_para_ficha_te_ca9e2e1b_uniq` (`cronograma_para_ficha_tecnica_id`,`encuetros_por_semana_id`),
  ADD KEY `api_cronograma_para__encuetros_por_semana_e0c808aa_fk_api_encue` (`encuetros_por_semana_id`);

--
-- Indices de la tabla `api_empresa`
--
ALTER TABLE `api_empresa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_empresa_lista_de_contrato`
--
ALTER TABLE `api_empresa_lista_de_contrato`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_empresa_lista_de_con_empresa_id_contrato_id_1a52cf8c_uniq` (`empresa_id`,`contrato_id`),
  ADD KEY `api_empresa_lista_de_contrato_id_5fa9053a_fk_api_contr` (`contrato_id`);

--
-- Indices de la tabla `api_empresa_lista_de_seguridad`
--
ALTER TABLE `api_empresa_lista_de_seguridad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_empresa_lista_de_seg_empresa_id_usuario_id_cd406456_uniq` (`empresa_id`,`usuario_id`),
  ADD KEY `api_empresa_lista_de_usuario_id_8a0bf36f_fk_api_usuar` (`usuario_id`);

--
-- Indices de la tabla `api_encuetros_por_semana`
--
ALTER TABLE `api_encuetros_por_semana`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_facturacion_pagos`
--
ALTER TABLE `api_facturacion_pagos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_facturacion_pago_id_resultados_obteni_87aa6e08_fk_api_resul` (`id_resultados_obtenidos_para_ficha_tecnica_id`);

--
-- Indices de la tabla `api_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_ficha_tecnica_id_cronograma_id_daf93acd_fk_api_crono` (`id_cronograma_id`),
  ADD KEY `api_ficha_tecnica_id_valor_del_contrat_ee21d425_fk_api_valor` (`id_valor_del_contrato_por_los_servicios_comercializados_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_area_participante`
--
ALTER TABLE `api_ficha_tecnica_lista_area_participante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_area_pa_44f5743e_uniq` (`ficha_tecnica_id`,`area_participante_id`),
  ADD KEY `api_ficha_tecnica_li_area_participante_id_ec15996d_fk_api_area_` (`area_participante_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_conside_2d4ee23d_uniq` (`ficha_tecnica_id`,`consideraciones_para_la_ficha_tecnica_id`),
  ADD KEY `api_ficha_tecnica_li_consideraciones_para_9b3a2a78_fk_api_consi` (`consideraciones_para_la_ficha_tecnica_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_control_73b9f3f1_uniq` (`ficha_tecnica_id`,`control_de_documentos_del_contrato_id`),
  ADD KEY `api_ficha_tecnica_li_control_de_documento_a61bb6f6_fk_api_contr` (`control_de_documentos_del_contrato_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_product_4fd46eca_uniq` (`ficha_tecnica_id`,`productos_necesarios_id`),
  ADD KEY `api_ficha_tecnica_li_productos_necesarios_5318cb87_fk_api_produ` (`productos_necesarios_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_facturacion_pagos`
--
ALTER TABLE `api_ficha_tecnica_lista_facturacion_pagos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_factura_ab0f9c78_uniq` (`ficha_tecnica_id`,`facturacion_pagos_id`),
  ADD KEY `api_ficha_tecnica_li_facturacion_pagos_id_45d1ad9b_fk_api_factu` (`facturacion_pagos_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_pagos_al_cliente`
--
ALTER TABLE `api_ficha_tecnica_lista_pagos_al_cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_pagos_a_54dfce88_uniq` (`ficha_tecnica_id`,`pagos_al_cliente_id`),
  ADD KEY `api_ficha_tecnica_li_pagos_al_cliente_id_002810cf_fk_api_pagos` (`pagos_al_cliente_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_recurso_necesarios`
--
ALTER TABLE `api_ficha_tecnica_lista_recurso_necesarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_recurso_bb47d0a2_uniq` (`ficha_tecnica_id`,`recursos_necesarios_id`),
  ADD KEY `api_ficha_tecnica_li_recursos_necesarios__1c286236_fk_api_recur` (`recursos_necesarios_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_registr_dc1122ea_uniq` (`ficha_tecnica_id`,`registros_de_derechos_y_propiedad_id`),
  ADD KEY `api_ficha_tecnica_li_registros_de_derecho_d50a8df8_fk_api_regis` (`registros_de_derechos_y_propiedad_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_resultados_de_tareas`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_de_tareas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_resulta_a378db9b_uniq` (`ficha_tecnica_id`,`resultados_para_ficha_tecnica_id`),
  ADD KEY `api_ficha_tecnica_li_resultados_para_fich_d5671756_fk_api_resul` (`resultados_para_ficha_tecnica_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_resulta_66cf0580_uniq` (`ficha_tecnica_id`,`resultados_obtenidos_para_ficha_tecnica_id`),
  ADD KEY `api_ficha_tecnica_li_resultados_obtenidos_bcae768c_fk_api_resul` (`resultados_obtenidos_para_ficha_tecnica_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_tareas_detalladas`
--
ALTER TABLE `api_ficha_tecnica_lista_tareas_detalladas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_tareas__66751501_uniq` (`ficha_tecnica_id`,`tareas_detalladas_id`),
  ADD KEY `api_ficha_tecnica_li_tareas_detalladas_id_79e6da55_fk_api_tarea` (`tareas_detalladas_id`);

--
-- Indices de la tabla `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_ficha_tecnica_lista__ficha_tecnica_id_tiempo__ba2a74c4_uniq` (`ficha_tecnica_id`,`tiempo_dedicado_en_horas_mensuales_id`),
  ADD KEY `api_ficha_tecnica_li_tiempo_dedicado_en_h_93155eb5_fk_api_tiemp` (`tiempo_dedicado_en_horas_mensuales_id`);

--
-- Indices de la tabla `api_norma`
--
ALTER TABLE `api_norma`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_pagos_al_cliente`
--
ALTER TABLE `api_pagos_al_cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_planificacion_de_gastos_personales`
--
ALTER TABLE `api_planificacion_de_gastos_personales`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_planificacion_de_gastos_personales_lista_trabajador`
--
ALTER TABLE `api_planificacion_de_gastos_personales_lista_trabajador`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_planificacion_de_gas_planificacion_de_gastos__07c4a8d6_uniq` (`planificacion_de_gastos_personales_id`,`trabajador_id`),
  ADD KEY `api_planificacion_de_trabajador_id_62ffa8b4_fk_api_traba` (`trabajador_id`);

--
-- Indices de la tabla `api_plazo`
--
ALTER TABLE `api_plazo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_productos_necesarios`
--
ALTER TABLE `api_productos_necesarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_programa_de_cobro`
--
ALTER TABLE `api_programa_de_cobro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_recursos_necesarios`
--
ALTER TABLE `api_recursos_necesarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_registros_de_derechos_y_propiedad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_registros_de_der_id_resultados_obteni_44d9adaf_fk_api_resul` (`id_resultados_obtenidos_para_ficha_tecnica_id`);

--
-- Indices de la tabla `api_resultados_obtenidos_para_ficha_tecnica`
--
ALTER TABLE `api_resultados_obtenidos_para_ficha_tecnica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_resultados_para_ficha_tecnica`
--
ALTER TABLE `api_resultados_para_ficha_tecnica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_rol`
--
ALTER TABLE `api_rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_servicio`
--
ALTER TABLE `api_servicio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_servicio_lista_trabajadores`
--
ALTER TABLE `api_servicio_lista_trabajadores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_servicio_lista_traba_servicio_id_trabajador_i_bd311297_uniq` (`servicio_id`,`trabajador_id`),
  ADD KEY `api_servicio_lista_t_trabajador_id_f0e5a4a8_fk_api_traba` (`trabajador_id`);

--
-- Indices de la tabla `api_tareas_detalladas`
--
ALTER TABLE `api_tareas_detalladas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_tiempo_dedicado_en_horas_mensuales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_tiempo_dedicado__id_resultados_obteni_d62ebb06_fk_api_resul` (`id_resultados_obtenidos_para_ficha_tecnica_id`);

--
-- Indices de la tabla `api_trabajador`
--
ALTER TABLE `api_trabajador`
  ADD PRIMARY KEY (`id_trabajador`),
  ADD KEY `api_trabajador_id_categoria_del_pro_dd75f703_fk_api_categ` (`id_categoria_del_profesor_del_servicio_id`);

--
-- Indices de la tabla `api_trabajador_lista_plazo`
--
ALTER TABLE `api_trabajador_lista_plazo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_trabajador_lista_plazo_trabajador_id_plazo_id_140510ba_uniq` (`trabajador_id`,`plazo_id`),
  ADD KEY `api_trabajador_lista_plazo_plazo_id_96296412_fk_api_plazo_id` (`plazo_id`);

--
-- Indices de la tabla `api_usuario`
--
ALTER TABLE `api_usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_usuario_id_rol_id_835ffde6_fk_api_rol_id` (`id_rol_id`);

--
-- Indices de la tabla `api_valor_del_contrato_por_los_servicios_comercializados`
--
ALTER TABLE `api_valor_del_contrato_por_los_servicios_comercializados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `api_area_participante`
--
ALTER TABLE `api_area_participante`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `api_area_participante_lista_trabajador`
--
ALTER TABLE `api_area_participante_lista_trabajador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_categoria_del_profesor_del_servicio`
--
ALTER TABLE `api_categoria_del_profesor_del_servicio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_consideraciones_para_la_ficha_tecnica`
--
ALTER TABLE `api_consideraciones_para_la_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_contrato`
--
ALTER TABLE `api_contrato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_contrato_lista_area_participante`
--
ALTER TABLE `api_contrato_lista_area_participante`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_contrato_lista_programa_de_cobro`
--
ALTER TABLE `api_contrato_lista_programa_de_cobro`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_control_de_documentos_del_contrato`
--
ALTER TABLE `api_control_de_documentos_del_contrato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_cronograma_para_ficha_tecnica`
--
ALTER TABLE `api_cronograma_para_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
--
ALTER TABLE `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `api_empresa`
--
ALTER TABLE `api_empresa`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_empresa_lista_de_contrato`
--
ALTER TABLE `api_empresa_lista_de_contrato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_empresa_lista_de_seguridad`
--
ALTER TABLE `api_empresa_lista_de_seguridad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_encuetros_por_semana`
--
ALTER TABLE `api_encuetros_por_semana`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_facturacion_pagos`
--
ALTER TABLE `api_facturacion_pagos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_area_participante`
--
ALTER TABLE `api_ficha_tecnica_lista_area_participante`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_facturacion_pagos`
--
ALTER TABLE `api_ficha_tecnica_lista_facturacion_pagos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_pagos_al_cliente`
--
ALTER TABLE `api_ficha_tecnica_lista_pagos_al_cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_recurso_necesarios`
--
ALTER TABLE `api_ficha_tecnica_lista_recurso_necesarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_resultados_de_tareas`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_de_tareas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_tareas_detalladas`
--
ALTER TABLE `api_ficha_tecnica_lista_tareas_detalladas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_norma`
--
ALTER TABLE `api_norma`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `api_pagos_al_cliente`
--
ALTER TABLE `api_pagos_al_cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `api_planificacion_de_gastos_personales`
--
ALTER TABLE `api_planificacion_de_gastos_personales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_planificacion_de_gastos_personales_lista_trabajador`
--
ALTER TABLE `api_planificacion_de_gastos_personales_lista_trabajador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `api_plazo`
--
ALTER TABLE `api_plazo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `api_productos_necesarios`
--
ALTER TABLE `api_productos_necesarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_programa_de_cobro`
--
ALTER TABLE `api_programa_de_cobro`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_recursos_necesarios`
--
ALTER TABLE `api_recursos_necesarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_registros_de_derechos_y_propiedad`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `api_resultados_obtenidos_para_ficha_tecnica`
--
ALTER TABLE `api_resultados_obtenidos_para_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_resultados_para_ficha_tecnica`
--
ALTER TABLE `api_resultados_para_ficha_tecnica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_rol`
--
ALTER TABLE `api_rol`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `api_servicio`
--
ALTER TABLE `api_servicio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `api_servicio_lista_trabajadores`
--
ALTER TABLE `api_servicio_lista_trabajadores`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_tareas_detalladas`
--
ALTER TABLE `api_tareas_detalladas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `api_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_tiempo_dedicado_en_horas_mensuales`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_trabajador_lista_plazo`
--
ALTER TABLE `api_trabajador_lista_plazo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `api_usuario`
--
ALTER TABLE `api_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `api_valor_del_contrato_por_los_servicios_comercializados`
--
ALTER TABLE `api_valor_del_contrato_por_los_servicios_comercializados`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `api_area_participante_lista_trabajador`
--
ALTER TABLE `api_area_participante_lista_trabajador`
  ADD CONSTRAINT `api_area_participant_area_participante_id_b7901ef1_fk_api_area_` FOREIGN KEY (`area_participante_id`) REFERENCES `api_area_participante` (`id`),
  ADD CONSTRAINT `api_area_participant_trabajador_id_482be9e6_fk_api_traba` FOREIGN KEY (`trabajador_id`) REFERENCES `api_trabajador` (`id_trabajador`);

--
-- Filtros para la tabla `api_contrato`
--
ALTER TABLE `api_contrato`
  ADD CONSTRAINT `api_contrato_id_servicio_id_90bd9984_fk_api_servicio_id` FOREIGN KEY (`id_servicio_id`) REFERENCES `api_servicio` (`id`);

--
-- Filtros para la tabla `api_contrato_lista_area_participante`
--
ALTER TABLE `api_contrato_lista_area_participante`
  ADD CONSTRAINT `api_contrato_lista_a_area_participante_id_ef3d0bca_fk_api_area_` FOREIGN KEY (`area_participante_id`) REFERENCES `api_area_participante` (`id`),
  ADD CONSTRAINT `api_contrato_lista_a_contrato_id_9287a315_fk_api_contr` FOREIGN KEY (`contrato_id`) REFERENCES `api_contrato` (`id`);

--
-- Filtros para la tabla `api_contrato_lista_programa_de_cobro`
--
ALTER TABLE `api_contrato_lista_programa_de_cobro`
  ADD CONSTRAINT `api_contrato_lista_p_contrato_id_0f18a0f1_fk_api_contr` FOREIGN KEY (`contrato_id`) REFERENCES `api_contrato` (`id`),
  ADD CONSTRAINT `api_contrato_lista_p_programa_de_cobro_id_86d3b62f_fk_api_progr` FOREIGN KEY (`programa_de_cobro_id`) REFERENCES `api_programa_de_cobro` (`id`);

--
-- Filtros para la tabla `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
--
ALTER TABLE `api_cronograma_para_ficha_tecnica_lista_encuetros_por_semana`
  ADD CONSTRAINT `api_cronograma_para__cronograma_para_fich_a6fec4f1_fk_api_crono` FOREIGN KEY (`cronograma_para_ficha_tecnica_id`) REFERENCES `api_cronograma_para_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_cronograma_para__encuetros_por_semana_e0c808aa_fk_api_encue` FOREIGN KEY (`encuetros_por_semana_id`) REFERENCES `api_encuetros_por_semana` (`id`);

--
-- Filtros para la tabla `api_empresa_lista_de_contrato`
--
ALTER TABLE `api_empresa_lista_de_contrato`
  ADD CONSTRAINT `api_empresa_lista_de_contrato_id_5fa9053a_fk_api_contr` FOREIGN KEY (`contrato_id`) REFERENCES `api_contrato` (`id`),
  ADD CONSTRAINT `api_empresa_lista_de_empresa_id_cbfa1164_fk_api_empre` FOREIGN KEY (`empresa_id`) REFERENCES `api_empresa` (`id`);

--
-- Filtros para la tabla `api_empresa_lista_de_seguridad`
--
ALTER TABLE `api_empresa_lista_de_seguridad`
  ADD CONSTRAINT `api_empresa_lista_de_empresa_id_0186da57_fk_api_empre` FOREIGN KEY (`empresa_id`) REFERENCES `api_empresa` (`id`),
  ADD CONSTRAINT `api_empresa_lista_de_usuario_id_8a0bf36f_fk_api_usuar` FOREIGN KEY (`usuario_id`) REFERENCES `api_usuario` (`id`);

--
-- Filtros para la tabla `api_facturacion_pagos`
--
ALTER TABLE `api_facturacion_pagos`
  ADD CONSTRAINT `api_facturacion_pago_id_resultados_obteni_87aa6e08_fk_api_resul` FOREIGN KEY (`id_resultados_obtenidos_para_ficha_tecnica_id`) REFERENCES `api_resultados_obtenidos_para_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica`
  ADD CONSTRAINT `api_ficha_tecnica_id_cronograma_id_daf93acd_fk_api_crono` FOREIGN KEY (`id_cronograma_id`) REFERENCES `api_cronograma_para_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_id_valor_del_contrat_ee21d425_fk_api_valor` FOREIGN KEY (`id_valor_del_contrato_por_los_servicios_comercializados_id`) REFERENCES `api_valor_del_contrato_por_los_servicios_comercializados` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_area_participante`
--
ALTER TABLE `api_ficha_tecnica_lista_area_participante`
  ADD CONSTRAINT `api_ficha_tecnica_li_area_participante_id_ec15996d_fk_api_area_` FOREIGN KEY (`area_participante_id`) REFERENCES `api_area_participante` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_fc0af249_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_consideraciones_para_la_ficha_tecnica`
  ADD CONSTRAINT `api_ficha_tecnica_li_consideraciones_para_9b3a2a78_fk_api_consi` FOREIGN KEY (`consideraciones_para_la_ficha_tecnica_id`) REFERENCES `api_consideraciones_para_la_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_77382236_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_control_de_documentos_del_contrato`
  ADD CONSTRAINT `api_ficha_tecnica_li_control_de_documento_a61bb6f6_fk_api_contr` FOREIGN KEY (`control_de_documentos_del_contrato_id`) REFERENCES `api_control_de_documentos_del_contrato` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_41b59acd_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
--
ALTER TABLE `api_ficha_tecnica_lista_de_productos_extras_para_el_contrato`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_ef2b76f1_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_productos_necesarios_5318cb87_fk_api_produ` FOREIGN KEY (`productos_necesarios_id`) REFERENCES `api_productos_necesarios` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_facturacion_pagos`
--
ALTER TABLE `api_ficha_tecnica_lista_facturacion_pagos`
  ADD CONSTRAINT `api_ficha_tecnica_li_facturacion_pagos_id_45d1ad9b_fk_api_factu` FOREIGN KEY (`facturacion_pagos_id`) REFERENCES `api_facturacion_pagos` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_0eb94e3b_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_pagos_al_cliente`
--
ALTER TABLE `api_ficha_tecnica_lista_pagos_al_cliente`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_c4443a5d_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_pagos_al_cliente_id_002810cf_fk_api_pagos` FOREIGN KEY (`pagos_al_cliente_id`) REFERENCES `api_pagos_al_cliente` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_recurso_necesarios`
--
ALTER TABLE `api_ficha_tecnica_lista_recurso_necesarios`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_a75a1528_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_recursos_necesarios__1c286236_fk_api_recur` FOREIGN KEY (`recursos_necesarios_id`) REFERENCES `api_recursos_necesarios` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_ficha_tecnica_lista_registros_de_derechos_y_propiedad`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_33c53643_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_registros_de_derecho_d50a8df8_fk_api_regis` FOREIGN KEY (`registros_de_derechos_y_propiedad_id`) REFERENCES `api_registros_de_derechos_y_propiedad` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_resultados_de_tareas`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_de_tareas`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_5947aabd_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_resultados_para_fich_d5671756_fk_api_resul` FOREIGN KEY (`resultados_para_ficha_tecnica_id`) REFERENCES `api_resultados_para_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
--
ALTER TABLE `api_ficha_tecnica_lista_resultados_obtenidos_para_ficha_tecnica`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_6476653f_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_resultados_obtenidos_bcae768c_fk_api_resul` FOREIGN KEY (`resultados_obtenidos_para_ficha_tecnica_id`) REFERENCES `api_resultados_obtenidos_para_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_tareas_detalladas`
--
ALTER TABLE `api_ficha_tecnica_lista_tareas_detalladas`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_c49e7376_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_tareas_detalladas_id_79e6da55_fk_api_tarea` FOREIGN KEY (`tareas_detalladas_id`) REFERENCES `api_tareas_detalladas` (`id`);

--
-- Filtros para la tabla `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_ficha_tecnica_lista_tiempo_dedicado_en_horas_mensuales`
  ADD CONSTRAINT `api_ficha_tecnica_li_ficha_tecnica_id_c3eeb9a2_fk_api_ficha` FOREIGN KEY (`ficha_tecnica_id`) REFERENCES `api_ficha_tecnica` (`id`),
  ADD CONSTRAINT `api_ficha_tecnica_li_tiempo_dedicado_en_h_93155eb5_fk_api_tiemp` FOREIGN KEY (`tiempo_dedicado_en_horas_mensuales_id`) REFERENCES `api_tiempo_dedicado_en_horas_mensuales` (`id`);

--
-- Filtros para la tabla `api_planificacion_de_gastos_personales_lista_trabajador`
--
ALTER TABLE `api_planificacion_de_gastos_personales_lista_trabajador`
  ADD CONSTRAINT `api_planificacion_de_planificacion_de_gas_5713e983_fk_api_plani` FOREIGN KEY (`planificacion_de_gastos_personales_id`) REFERENCES `api_planificacion_de_gastos_personales` (`id`),
  ADD CONSTRAINT `api_planificacion_de_trabajador_id_62ffa8b4_fk_api_traba` FOREIGN KEY (`trabajador_id`) REFERENCES `api_trabajador` (`id_trabajador`);

--
-- Filtros para la tabla `api_registros_de_derechos_y_propiedad`
--
ALTER TABLE `api_registros_de_derechos_y_propiedad`
  ADD CONSTRAINT `api_registros_de_der_id_resultados_obteni_44d9adaf_fk_api_resul` FOREIGN KEY (`id_resultados_obtenidos_para_ficha_tecnica_id`) REFERENCES `api_resultados_obtenidos_para_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_servicio_lista_trabajadores`
--
ALTER TABLE `api_servicio_lista_trabajadores`
  ADD CONSTRAINT `api_servicio_lista_t_servicio_id_bccb1a3f_fk_api_servi` FOREIGN KEY (`servicio_id`) REFERENCES `api_servicio` (`id`),
  ADD CONSTRAINT `api_servicio_lista_t_trabajador_id_f0e5a4a8_fk_api_traba` FOREIGN KEY (`trabajador_id`) REFERENCES `api_trabajador` (`id_trabajador`);

--
-- Filtros para la tabla `api_tiempo_dedicado_en_horas_mensuales`
--
ALTER TABLE `api_tiempo_dedicado_en_horas_mensuales`
  ADD CONSTRAINT `api_tiempo_dedicado__id_resultados_obteni_d62ebb06_fk_api_resul` FOREIGN KEY (`id_resultados_obtenidos_para_ficha_tecnica_id`) REFERENCES `api_resultados_obtenidos_para_ficha_tecnica` (`id`);

--
-- Filtros para la tabla `api_trabajador`
--
ALTER TABLE `api_trabajador`
  ADD CONSTRAINT `api_trabajador_id_categoria_del_pro_dd75f703_fk_api_categ` FOREIGN KEY (`id_categoria_del_profesor_del_servicio_id`) REFERENCES `api_categoria_del_profesor_del_servicio` (`id`);

--
-- Filtros para la tabla `api_trabajador_lista_plazo`
--
ALTER TABLE `api_trabajador_lista_plazo`
  ADD CONSTRAINT `api_trabajador_lista_plazo_plazo_id_96296412_fk_api_plazo_id` FOREIGN KEY (`plazo_id`) REFERENCES `api_plazo` (`id`),
  ADD CONSTRAINT `api_trabajador_lista_trabajador_id_f91c37f3_fk_api_traba` FOREIGN KEY (`trabajador_id`) REFERENCES `api_trabajador` (`id_trabajador`);

--
-- Filtros para la tabla `api_usuario`
--
ALTER TABLE `api_usuario`
  ADD CONSTRAINT `api_usuario_id_rol_id_835ffde6_fk_api_rol_id` FOREIGN KEY (`id_rol_id`) REFERENCES `api_rol` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
