from django.urls import path

from . import views
from .economia.views import contratos_view, pagos_al_cliente_view, facturacion_pagos_view
from .recursos_humanos.views import norma_view, plazo_view, trabajador_view, programa_de_cobro_view, \
    planificacion_de_gastos_personales_view, categoria_profesor_view
from .seguridad.views import rol_view, usuario_view
from .servicios.views import servicio_view, area_participante_view, tareas_detalladas_view, recursos_necesarios_view, \
    productos_necesarios_view, encuetros_por_semana_view, cronograma_para_ficha_tecnica_view, \
    resultados_obtenidos_para_ficha_tecnica_view, resultados_para_ficha_tecnica_view, \
    tiempo_dedicado_en_horas_mensuales_view, \
    registros_de_derechos_y_propiedad_view, control_de_documentos_del_contrato_view, \
    consideraciones_para_la_ficha_tecnica_view, valor_del_contrato_por_los_servicios_comercializados_view, \
    ficha_tecnica_view
from .views import empresa_view

urlpatterns = [
    # devuelve tod0
    # path('norms/', norms_view.as_view(), name='norms_list'),
    # devuelve tod0 o algun elemento en especifico
    path('normas/<int:id>', norma_view.as_view(), name='norms_process'),
    path('normas/put/<int:id>', norma_view.as_view(), name='norms_update'),
    path('normas/delete/<int:id>', norma_view.as_view(), name='delete_norms'),
    path('normas/post/', norma_view.as_view(), name='post_norms'),

    # roles

    path('roles/<int:id>', rol_view.as_view(), name='roles_process'),
    path('roles/put/<int:id>', rol_view.as_view(), name='roles_update'),
    path('roles/delete/<int:id>', rol_view.as_view(), name='delete_roles'),
    path('roles/post/', rol_view.as_view(), name='post_roles'),

    # plazos

    path('plazos/<int:id>', plazo_view.as_view(), name='plazos_process'),
    path('plazos/put/<int:id>', plazo_view.as_view(), name='plazos_update'),
    path('plazos/delete/<int:id>', plazo_view.as_view(), name='delete_plazos'),
    path('plazos/post/', plazo_view.as_view(), name='post_plazos'),

    # trabajadores
    path('trabajadores/<int:id>', trabajador_view.as_view(), name='trabajadores_process'),
    path('trabajadores/post/', trabajador_view.as_view(), name='post_trabajadores'),
    path('trabajadores/put/<int:id>', trabajador_view.as_view(), name='trabajadores_update'),
    # path('trabajadores/put/', trabajador_view.as_view(), name='trabajadores_update'),
    path('trabajadores/delete/<int:id>', trabajador_view.as_view(), name='delete_trabajadores'),

    # usuarios

    path('usuarios/<int:id>', usuario_view.as_view(), name='usuarios_process'),
    path('usuarios/post/', usuario_view.as_view(), name='post_usuarios'),
    path('usuarios/put/<int:id>', usuario_view.as_view(), name='usuarios_update'),
    path('usuarios/delete/<int:id>', usuario_view.as_view(), name='delete_usuarios'),

    # servicios

    path('servicios/<int:id>', servicio_view.as_view(), name='servicios_process'),
    path('servicios/post/', servicio_view.as_view(), name='post_servicios'),
    path('servicios/put/<int:id>', servicio_view.as_view(), name='servicios_update'),
    path('servicios/delete/<int:id>', servicio_view.as_view(), name='delete_servicios'),

    # programa de cobros

    path('programa_de_cobro/<int:id>', programa_de_cobro_view.as_view(), name='programa_de_cobro_process'),
    path('programa_de_cobro/post/', programa_de_cobro_view.as_view(), name='post_programa_de_cobro'),
    path('programa_de_cobro/put/<int:id>', programa_de_cobro_view.as_view(), name='programa_de_cobro_update'),
    path('programa_de_cobro/delete/<int:id>', programa_de_cobro_view.as_view(), name='delete_programa_de_cobro'),

    # planificacion_de_gastos_personales

    path('planificacion_de_gastos_personales/<int:id>', planificacion_de_gastos_personales_view.as_view(),
         name='planificacion_de_gastos_personales_process'),
    path('planificacion_de_gastos_personales/post/', planificacion_de_gastos_personales_view.as_view(),
         name='post_planificacion_de_gastos_personales'),
    path('planificacion_de_gastos_personales/put/<int:id>', planificacion_de_gastos_personales_view.as_view(),
         name='planificacion_de_gastos_personales_update'),
    path('planificacion_de_gastos_personales/delete/<int:id>', planificacion_de_gastos_personales_view.as_view(),
         name='delete_planificacion_de_gastos_personales'),

    # area_participante

    path('area_participante/<int:id>', area_participante_view.as_view(), name='area_participante_process'),
    path('area_participante/post/', area_participante_view.as_view(), name='post_area_participante'),
    path('area_participante/put/<int:id>', area_participante_view.as_view(), name='area_participante_update'),
    path('area_participante/delete/<int:id>', area_participante_view.as_view(), name='delete_area_participante'),

    # empresa

    path('empresas/<int:id>', empresa_view.as_view(), name='empresa_process'),
    path('empresas/post/', empresa_view.as_view(), name='post_empresa'),
    path('empresas/put/<int:id>', empresa_view.as_view(), name='empresa_update'),
    path('empresas/delete/<int:id>', empresa_view.as_view(), name='delete_empresa'),

    # contrato

    path('contratos/<int:id>', contratos_view.as_view(), name='contratos_process'),
    path('contratos/post/', contratos_view.as_view(), name='post_contratos'),
    path('contratos/put/<int:id>', contratos_view.as_view(), name='contratos_update'),
    path('contratos/delete/<int:id>', contratos_view.as_view(), name='delete_contratos'),

    # categoria_del_profesor_del_servicio (nuevo)

    path('categoria_profesores/<int:id>', categoria_profesor_view.as_view(), name='categoria_profesores_process'),
    path('categoria_profesores/post/', categoria_profesor_view.as_view(), name='post_categoria_profesores'),
    path('categoria_profesores/put/<int:id>', categoria_profesor_view.as_view(), name='categoria_profesores_update'),
    path('categoria_profesores/delete/<int:id>', categoria_profesor_view.as_view(), name='delete_categoria_profesores'),

    # Login
    path('login/', views.LoginView.as_view(), name='login'),

    # jonathan

    # pagos_al_cliente (nuevo)

    path('pagos_al_cliente/<int:id>', pagos_al_cliente_view.as_view(), name='pagos_al_cliente_process'),
    path('pagos_al_cliente/post/', pagos_al_cliente_view.as_view(), name='post_pagos_al_cliente'),
    path('pagos_al_cliente/put/<int:id>', pagos_al_cliente_view.as_view(), name='pagos_al_cliente_update'),
    path('pagos_al_cliente/delete/<int:id>', pagos_al_cliente_view.as_view(), name='delete_pagos_al_cliente'),

    # facturacion_pagos (nuevo)

    path('facturacion_pagos/<int:id>', facturacion_pagos_view.as_view(), name='facturacion_pagos_process'),
    path('facturacion_pagos/post/', facturacion_pagos_view.as_view(), name='post_facturacion_pagos'),
    path('facturacion_pagos/put/<int:id>', facturacion_pagos_view.as_view(), name='facturacion_pagos_update'),
    path('facturacion_pagos/delete/<int:id>', facturacion_pagos_view.as_view(), name='delete_facturacion_pagos'),

    # tareas_detalladas (nuevo)

    path('tareas_detalladas/<int:id>', tareas_detalladas_view.as_view(), name='tareas_detalladas_process'),
    path('tareas_detalladas/post/', tareas_detalladas_view.as_view(), name='post_tareas_detalladas'),
    path('tareas_detalladas/put/<int:id>', tareas_detalladas_view.as_view(), name='tareas_detalladas_update'),
    path('tareas_detalladas/delete/<int:id>', tareas_detalladas_view.as_view(), name='delete_tareas_detalladas'),

    # recursos_necesarios (nuevo)

    path('recursos_necesarios/<int:id>', recursos_necesarios_view.as_view(), name='recursos_necesarios_process'),
    path('recursos_necesarios/post/', recursos_necesarios_view.as_view(), name='post_recursos_necesarios'),
    path('recursos_necesarios/put/<int:id>', recursos_necesarios_view.as_view(), name='recursos_necesarios_update'),
    path('recursos_necesarios/delete/<int:id>', recursos_necesarios_view.as_view(), name='delete_recursos_necesarios'),

    # productos_necesarios (nuevo)

    path('productos_necesarios/<int:id>', productos_necesarios_view.as_view(), name='productos_necesarios_process'),
    path('productos_necesarios/post/', productos_necesarios_view.as_view(), name='post_productos_necesarios'),
    path('productos_necesarios/put/<int:id>', productos_necesarios_view.as_view(), name='productos_necesarios_update'),
    path('productos_necesarios/delete/<int:id>', productos_necesarios_view.as_view(), name='delete_productos_necesarios'),

    # encuetros_por_semana (nuevo)

    path('encuetros_por_semana/<int:id>', encuetros_por_semana_view.as_view(), name='encuetros_por_semana_process'),
    path('encuetros_por_semana/post/', encuetros_por_semana_view.as_view(), name='post_encuetros_por_semana'),
    path('encuetros_por_semana/put/<int:id>', encuetros_por_semana_view.as_view(), name='encuetros_por_semana_update'),
    path('encuetros_por_semana/delete/<int:id>', encuetros_por_semana_view.as_view(), name='delete_encuetros_por_semana'),

    # cronograma_para_ficha_tecnica (nuevo)

    path('cronograma_para_ficha_tecnica/<int:id>', cronograma_para_ficha_tecnica_view.as_view(), name='cronograma_para_ficha_tecnica_process'),
    path('cronograma_para_ficha_tecnica/post/', cronograma_para_ficha_tecnica_view.as_view(), name='post_cronograma_para_ficha_tecnica'),
    path('cronograma_para_ficha_tecnica/put/<int:id>', cronograma_para_ficha_tecnica_view.as_view(), name='cronograma_para_ficha_tecnica_update'),
    path('cronograma_para_ficha_tecnica/delete/<int:id>', cronograma_para_ficha_tecnica_view.as_view(), name='delete_cronograma_para_ficha_tecnica'),

    # resultados_para_ficha_tecnica (nuevo)

    path('resultados_para_ficha_tecnica/<int:id>', resultados_para_ficha_tecnica_view.as_view(), name='resultados_para_ficha_tecnica_process'),
    path('resultados_para_ficha_tecnica/post/', resultados_para_ficha_tecnica_view.as_view(), name='post_resultados_para_ficha_tecnica'),
    path('resultados_para_ficha_tecnica/put/<int:id>', resultados_para_ficha_tecnica_view.as_view(), name='resultados_para_ficha_tecnica_update'),
    path('resultados_para_ficha_tecnica/delete/<int:id>', resultados_para_ficha_tecnica_view.as_view(), name='delete_resultados_para_ficha_tecnica'),

    # resultados_obtenidos_para_ficha_tecnica (nuevo)

    path('resultados_obtenidos_para_ficha_tecnica/<int:id>', resultados_obtenidos_para_ficha_tecnica_view.as_view(), name='resultados_obtenidos_para_ficha_tecnica_process'),
    path('resultados_obtenidos_para_ficha_tecnica/post/', resultados_obtenidos_para_ficha_tecnica_view.as_view(), name='post_resultados_obtenidos_para_ficha_tecnica'),
    path('resultados_obtenidos_para_ficha_tecnica/put/<int:id>', resultados_obtenidos_para_ficha_tecnica_view.as_view(), name='resultados_obtenidos_para_ficha_tecnica_update'),
    path('resultados_obtenidos_para_ficha_tecnica/delete/<int:id>', resultados_obtenidos_para_ficha_tecnica_view.as_view(), name='delete_resultados_obtenidos_para_ficha_tecnica'),


    # tiempo_dedicado_en_horas_mensuales (nuevo)

    path('tiempo_dedicado_en_horas_mensuales/<int:id>', tiempo_dedicado_en_horas_mensuales_view.as_view(), name='tiempo_dedicado_en_horas_mensuales_process'),
    path('tiempo_dedicado_en_horas_mensuales/post/', tiempo_dedicado_en_horas_mensuales_view.as_view(), name='post_tiempo_dedicado_en_horas_mensuales'),
    path('tiempo_dedicado_en_horas_mensuales/put/<int:id>', tiempo_dedicado_en_horas_mensuales_view.as_view(), name='tiempo_dedicado_en_horas_mensuales_update'),
    path('tiempo_dedicado_en_horas_mensuales/delete/<int:id>', tiempo_dedicado_en_horas_mensuales_view.as_view(), name='delete_tiempo_dedicado_en_horas_mensuales'),

    # registros_de_derechos_y_propiedad (nuevo)

    path('registros_de_derechos_y_propiedad/<int:id>', registros_de_derechos_y_propiedad_view.as_view(), name='registros_de_derechos_y_propiedad_process'),
    path('registros_de_derechos_y_propiedad/post/', registros_de_derechos_y_propiedad_view.as_view(), name='post_registros_de_derechos_y_propiedad'),
    path('registros_de_derechos_y_propiedad/put/<int:id>', registros_de_derechos_y_propiedad_view.as_view(), name='registros_de_derechos_y_propiedad_update'),
    path('registros_de_derechos_y_propiedad/delete/<int:id>', registros_de_derechos_y_propiedad_view.as_view(), name='delete_registros_de_derechos_y_propiedad'),

    # control_de_documentos_del_contrato (nuevo)

    path('control_de_documentos_del_contrato/<int:id>', control_de_documentos_del_contrato_view.as_view(), name='control_de_documentos_del_contrato_process'),
    path('control_de_documentos_del_contrato/post/', control_de_documentos_del_contrato_view.as_view(), name='post_control_de_documentos_del_contrato'),
    path('control_de_documentos_del_contrato/put/<int:id>', control_de_documentos_del_contrato_view.as_view(), name='control_de_documentos_del_contrato_update'),
    path('control_de_documentos_del_contrato/delete/<int:id>', control_de_documentos_del_contrato_view.as_view(), name='delete_control_de_documentos_del_contrato'),

    # consideraciones_para_la_ficha_tecnica (nuevo)

    path('consideraciones_para_la_ficha_tecnica/<int:id>', consideraciones_para_la_ficha_tecnica_view.as_view(), name='consideraciones_para_la_ficha_tecnica_process'),
    path('consideraciones_para_la_ficha_tecnica/post/', consideraciones_para_la_ficha_tecnica_view.as_view(), name='post_consideraciones_para_la_ficha_tecnica'),
    path('consideraciones_para_la_ficha_tecnica/put/<int:id>', consideraciones_para_la_ficha_tecnica_view.as_view(), name='consideraciones_para_la_ficha_tecnica_update'),
    path('consideraciones_para_la_ficha_tecnica/delete/<int:id>', consideraciones_para_la_ficha_tecnica_view.as_view(), name='delete_consideraciones_para_la_ficha_tecnica'),

    # valor_del_contrato_por_los_servicios_comercializados (nuevo)

    path('valor_del_contrato_por_los_servicios_comercializados/<int:id>', valor_del_contrato_por_los_servicios_comercializados_view.as_view(), name='valor_del_contrato_por_los_servicios_comercializados_process'),
    path('valor_del_contrato_por_los_servicios_comercializados/post/', valor_del_contrato_por_los_servicios_comercializados_view.as_view(), name='post_valor_del_contrato_por_los_servicios_comercializados'),
    path('valor_del_contrato_por_los_servicios_comercializados/put/<int:id>', valor_del_contrato_por_los_servicios_comercializados_view.as_view(), name='valor_del_contrato_por_los_servicios_comercializados_update'),
    path('valor_del_contrato_por_los_servicios_comercializados/delete/<int:id>', valor_del_contrato_por_los_servicios_comercializados_view.as_view(), name='delete_valor_del_contrato_por_los_servicios_comercializados'),

    # ficha_tecnica (nuevo)

    path('ficha_tecnica/<int:id>', ficha_tecnica_view.as_view(), name='ficha_tecnica_process'),
    path('ficha_tecnica/post/', ficha_tecnica_view.as_view(), name='post_ficha_tecnica'),
    path('ficha_tecnica/put/<int:id>', ficha_tecnica_view.as_view(), name='ficha_tecnica_update'),
    path('ficha_tecnica/delete/<int:id>', ficha_tecnica_view.as_view(), name='delete_ficha_tecnica'),

]
