from django.contrib import admin
from .recursos_humanos.models import trabajador, programa_de_cobro, norma, plazo, planificacion_de_gastos_personales, \
    categoria_del_profesor_del_servicio
from .economia.models import contrato, pagos_al_cliente, facturacion_pagos
from .seguridad.models import usuario, rol
from .servicios.models import servicio, tareas_detalladas, recursos_necesarios, productos_necesarios, \
    encuetros_por_semana, cronograma_para_ficha_tecnica, resultados_para_ficha_tecnica, \
    resultados_obtenidos_para_ficha_tecnica,tiempo_dedicado_en_horas_mensuales, registros_de_derechos_y_propiedad, control_de_documentos_del_contrato, \
    consideraciones_para_la_ficha_tecnica, ficha_tecnica, area_participante, \
    valor_del_contrato_por_los_servicios_comercializados
from .models import empresa

# Register your models here.

admin.site.register(norma)
admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(plazo)
admin.site.register(trabajador)
admin.site.register(planificacion_de_gastos_personales)
admin.site.register(area_participante)
admin.site.register(servicio)
admin.site.register(programa_de_cobro)
admin.site.register(contrato)
admin.site.register(empresa)

# (nuevo)
admin.site.register(categoria_del_profesor_del_servicio)

# jonathan
admin.site.register(pagos_al_cliente)
admin.site.register(valor_del_contrato_por_los_servicios_comercializados)
admin.site.register(facturacion_pagos)
admin.site.register(tareas_detalladas)
admin.site.register(recursos_necesarios)
admin.site.register(productos_necesarios)
admin.site.register(encuetros_por_semana)
admin.site.register(cronograma_para_ficha_tecnica)
admin.site.register(resultados_para_ficha_tecnica)
admin.site.register(resultados_obtenidos_para_ficha_tecnica)

admin.site.register(tiempo_dedicado_en_horas_mensuales)
admin.site.register(registros_de_derechos_y_propiedad)
admin.site.register(control_de_documentos_del_contrato)
admin.site.register(consideraciones_para_la_ficha_tecnica)
admin.site.register(ficha_tecnica)
