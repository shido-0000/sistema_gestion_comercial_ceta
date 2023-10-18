from django.db import models


# categoria_del_profesor_del_servicio (nuevo)
class categoria_del_profesor_del_servicio(models.Model):
    nombre_categoria = models.TextField()
    tarifa_por_hora = models.FloatField()
    total_de_horas = models.FloatField()


# datos del trabajador


class trabajador(models.Model):
    id_trabajador = models.CharField(max_length=11, primary_key=True)
    nombre = models.TextField()
    lista_plazo = models.ManyToManyField('plazo')
    id_categoria_del_profesor_del_servicio = models.ForeignKey(categoria_del_profesor_del_servicio, null=False,
                                                               blank=False,
                                                               on_delete=models.DO_NOTHING)


# programa de cobro dentro del contrato


class programa_de_cobro(models.Model):
    nombre_programa = models.TextField()
    fecha = models.DateField()
    plan_MN = models.FloatField()
    plan_USD = models.FloatField()
    remuneracion = models.FloatField()


# planificacion de gastos personales de la empresa


class planificacion_de_gastos_personales(models.Model):
    ejecucion_fuera_de_provincia = models.BooleanField()
    lista_trabajador = models.ManyToManyField('trabajador')


# plazos de pago que tiene un trabajador
class plazo(models.Model):
    nombre_plazo = models.TextField()
    remuneracion = models.FloatField()
    cumplimiento_de_normas = models.BooleanField()
    total_asignado = models.FloatField()
    porcentaje = models.FloatField()


# normas para los gastos personales en los proyectos.


class norma(models.Model):
    nombre = models.TextField()
    cantidad = models.FloatField()
    tipo = models.TextField()
