from django.db import models

from api.recursos_humanos.models import trabajador


# Tipos de servicios que brinda la empresa
# actualizado el servicio (se le agrego una lista de categoria, capacidad_de_matricula)

class servicio(models.Model):
    nombre_servicio = models.TextField()
    #   categoria = models.TextField()
    #lista_categorias = models.ManyToManyField('categoria_del_profesor_del_servicio')
    lista_trabajadores = models.ManyToManyField('trabajador')
    capacidad_de_matricula = models.IntegerField()


# area participante en el proyecto


class area_participante(models.Model):
    nombre = models.TextField()
    porcentaje = models.FloatField()
    lista_trabajador = models.ManyToManyField('trabajador')


# Jonathan
# tareas detalladas para la ficha tecnica
class tareas_detalladas(models.Model):
    nombre_completo = models.TextField()


# recursos necesarios para el trabajo para la ficha tecnica
class recursos_necesarios(models.Model):
    nombre_completo = models.TextField()
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    caracteristicas_especiales = models.TextField()
    justificacion = models.TextField()
    valor_unitario = models.FloatField()
    total = models.FloatField()


# productos necesarios para la ficha tecnica
class productos_necesarios(models.Model):
    nombre_completo = models.TextField()
    descripcion = models.TextField()


# encuentros por semana para la ficha tecnica
class encuetros_por_semana(models.Model):
    cantidad = models.IntegerField()
    semana = models.IntegerField()



# productos necesarios para la ficha tecnica
class cronograma_para_ficha_tecnica(models.Model):
    numero_de_la_tarea = models.IntegerField()
    nombre_completo_de_la_tarea = models.TextField()
    lista_encuetros_por_semana = models.ManyToManyField('encuetros_por_semana')


# resultados obtenidos para la ficha tecnica
class resultados_para_ficha_tecnica(models.Model):
    numero_de_la_tarea = models.IntegerField()
    # nombre_completo_de_la_tarea_que_da_cumplimiento_al_numero_de_tarea
    nombre_completo_de_la_tarea = models.TextField()
    descripcion_del_tipo_de_entregable = models.TextField()
    formato_del_entregable = models.TextField()
    fecha_escrita_de_entrega_de_entregable = models.TextField()


# resultados obtenidos con el trabajo para la ficha tecnica
class resultados_obtenidos_para_ficha_tecnica(models.Model):
    nombre_producto_obtenido = models.TextField()
    descripcion_producto_obtenido = models.TextField()
    tipo_de_registro = models.TextField()


# falta este en vue
# areas y trabajadores con el trabajo para la ficha tecnica
#class areas_y_trabajdores_para_la_ficha_tecnica(models.Model):
 #   id_area_participante = models.ForeignKey(area_participante, null=False, blank=False,
 #                                            on_delete=models.DO_NOTHING)
  #  id_trabajador = models.ForeignKey(trabajador, null=False, blank=False,
   #                                   on_delete=models.DO_NOTHING)


# falta este en vue
# horas_de_dedicacion al contrato
class tiempo_dedicado_en_horas_mensuales(models.Model):
    id_resultados_obtenidos_para_ficha_tecnica = models.ForeignKey(resultados_obtenidos_para_ficha_tecnica, null=False,
                                                                   blank=False,
                                                                   on_delete=models.DO_NOTHING)
    horas_dedicadas = models.IntegerField()


# registros_de_derechos y propiedad

class registros_de_derechos_y_propiedad(models.Model):
    id_resultados_obtenidos_para_ficha_tecnica = models.ForeignKey(resultados_obtenidos_para_ficha_tecnica, null=False,
                                                                   blank=False,
                                                                   on_delete=models.DO_NOTHING)
    porcentaje_de_la_cujae = models.FloatField()
    porcentaje_del_cliente = models.FloatField()
    tipo_de_registro = models.TextField()


# control de documentos del contrato

class control_de_documentos_del_contrato(models.Model):
    nombre_del_documento = models.TextField()
    fecha_de_entrega = models.DateField()
    responsable = models.TextField()


# consideraciones para elaborar la ficha tecnica

class consideraciones_para_la_ficha_tecnica(models.Model):
    descripcion = models.TextField()


# valor_del_contrato_por_los_servicios_comercializados

class valor_del_contrato_por_los_servicios_comercializados(models.Model):
    valor = models.FloatField()
    moneda = models.TextField()


# Ficha tecnica

# falta este en vue
class ficha_tecnica(models.Model):
    descripcion = models.TextField()
    fecha = models.DateField()
    cliente = models.TextField()
    # el objeto es el producto
    objeto = models.TextField()
    vigencia = models.TextField()
    objetivos_especificos = models.TextField()
    lista_tareas_detalladas = models.ManyToManyField('tareas_detalladas')
    informacion_a_entregar_por_el_cliente = models.TextField()
    lista_recurso_necesarios = models.ManyToManyField('recursos_necesarios')
    lista_de_productos_extras_para_el_contrato = models.ManyToManyField('productos_necesarios')
    # id_area_ejecutora_principal = models.ForeignKey(area_participante, null=False, blank=False,
    #                                                on_delete=models.DO_NOTHING)
    id_area_ejecutora_principal = models.TextField()
    lista_area_participante = models.ManyToManyField('area_participante')
    id_cronograma = models.ForeignKey(cronograma_para_ficha_tecnica, null=False, blank=False,
                                      on_delete=models.DO_NOTHING)
    lista_resultados_de_tareas = models.ManyToManyField('resultados_para_ficha_tecnica')
    lista_resultados_obtenidos_para_ficha_tecnica = models.ManyToManyField('resultados_obtenidos_para_ficha_tecnica')

    lista_tiempo_dedicado_en_horas_mensuales = models.ManyToManyField('tiempo_dedicado_en_horas_mensuales')
    coordinador_del_contrato_por_la_cujae = models.TextField()
    cargo_del_cliente = models.TextField()
    lista_pagos_al_cliente = models.ManyToManyField('pagos_al_cliente')
    id_valor_del_contrato_por_los_servicios_comercializados = models.ForeignKey(
        valor_del_contrato_por_los_servicios_comercializados, null=False, blank=False,
        on_delete=models.DO_NOTHING)
    lista_facturacion_pagos = models.ManyToManyField('facturacion_pagos')
    lista_registros_de_derechos_y_propiedad = models.ManyToManyField('registros_de_derechos_y_propiedad')
    lista_control_de_documentos_del_contrato = models.ManyToManyField('control_de_documentos_del_contrato')
    firmado_por_responsable_del_contrato_de_ceta = models.TextField()
    lista_consideraciones_para_la_ficha_tecnica = models.ManyToManyField('consideraciones_para_la_ficha_tecnica')
