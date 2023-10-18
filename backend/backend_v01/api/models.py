from django.db import models


# Create your models here.

class empresa(models.Model):
    nombre_empresa = models.TextField()
    lista_de_contrato = models.ManyToManyField('contrato')
    lista_de_seguridad = models.ManyToManyField('usuario')
