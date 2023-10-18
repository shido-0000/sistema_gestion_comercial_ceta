from django.db import models
from api.servicios.models import servicio, resultados_obtenidos_para_ficha_tecnica


# contrato del proyecto


class contrato(models.Model):
    version = models.CharField(max_length=5)
    CES = models.TextField()
    titulo = models.TextField()
    numero = models.TextField()
    grupo_ejecutor_del_contrato = models.TextField()
    cliente = models.TextField()
    gestor = models.TextField()
    producto = models.TextField()
    codigo = models.TextField()
    id_servicio = models.ForeignKey(servicio, null=False, blank=False, on_delete=models.DO_NOTHING)
    localizacion_del_cliente = models.TextField()
    coordinador_del_contrato = models.TextField()
    cantidad_de_participantes = models.IntegerField()
    fecha_de_inicio = models.DateField()
    terminacion = models.DateField()
    valor_del_contrato = models.FloatField()
    margen_comercial = models.FloatField()
    ingreso_bruto = models.FloatField()
    observaciones = models.TextField()
    gastos_de_operacion_desde_CETA = models.FloatField()
    ingreso_neto_planificado = models.FloatField()
    remuneracion = models.FloatField()
    norma_maxima = models.FloatField()
    norma_asignada = models.FloatField()
    propuesto_por = models.TextField()
    aprobado_por = models.TextField()
    lista_programa_de_cobro = models.ManyToManyField('programa_de_cobro')
    lista_area_participante = models.ManyToManyField('area_participante')


# Jonathan
# pagos al cliente por ejecucion de la compra, esto es para la ficha tecnica

class pagos_al_cliente(models.Model):
    fecha = models.DateField()
    valor = models.FloatField()
    detalles = models.TextField()


class facturacion_pagos(models.Model):
    fecha = models.DateField()
    valor = models.FloatField()
    id_resultados_obtenidos_para_ficha_tecnica = models.ForeignKey(resultados_obtenidos_para_ficha_tecnica, null=False,
                                                                   blank=False,
                                                                   on_delete=models.DO_NOTHING)
