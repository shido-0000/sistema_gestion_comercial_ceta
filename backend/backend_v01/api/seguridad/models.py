from django.db import models
from rest_framework import serializers


# rol de los trabajadores

class rol(models.Model):
    nombre_rol = models.TextField()


# usuario que entre al sistema, ya sea un trabajador o un invitado


class usuario(models.Model):
    nombre_completo = models.TextField(null=False)
    nombre_usuario = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=255)  # O ajusta la longitud según tus necesidades
    id_rol = models.ForeignKey(rol, null=False, blank=False, on_delete=models.DO_NOTHING)


# para enviar todos los datos del usuario luego de hacer el login
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'  # Incluye todos los campos del modelo usuario en la serialización
