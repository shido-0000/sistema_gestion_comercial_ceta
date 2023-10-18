import bcrypt
from django.contrib.auth.hashers import check_password
from django.http.response import JsonResponse
# from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
import json

from django.core import serializers

from .recursos_humanos.models import programa_de_cobro, trabajador, plazo, planificacion_de_gastos_personales, norma
from .economia.models import contrato
from .seguridad.models import rol, usuario, UsuarioSerializer
from .models import empresa

# para el login
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

# clase empresa


class empresa_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos las empresa, si id!=0 entonces va a devolver el empresas cuyo id es igual al valor

    def get(self, request, id):
        if id > 0:
            empresas = list(empresa.objects.filter(id=id).all())
            empresas_json = serializers.serialize('json', empresas)

            if len(empresas) > 0:
                data = {'message': "Cargada 1 empresa", 'empresa': empresas_json}
            else:
                data = {'message': "Empresa no encontrada..."}
            return JsonResponse(data)
        else:
            empresas = empresa.objects.all()
            empresas_json = serializers.serialize('json', empresas)

            if len(empresas) > 0:
                data = {'message': "Todos las empresas cargadas", 'empresas': empresas_json}
            else:
                data = {'message': "Empresas no encontradas..."}
            return JsonResponse(data)

# Arreglado
    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        # id_area = data.get('id')
        nombre_empresa = data.get('nombre_empresa')
        lista_de_contrato = data.get('lista_de_contrato')
        lista_de_seguridad = data.get('lista_de_seguridad')

        # Crear un nuevo objeto de la empresa
        nueva_empresa = empresa(nombre_empresa=nombre_empresa)

        # Guardar el objeto en la base de datos
        nueva_empresa.save()

        # Asignar los contratos a la empresa
        for id_contrato in lista_de_contrato:
            try:
                contrato_obj = contrato.objects.get(id=id_contrato)
                nueva_empresa.lista_de_contrato.add(contrato_obj)
            except contrato.DoesNotExist:
                pass

        # Asignar los usuarios a la empresa
        for id_usuario in lista_de_seguridad:
            try:
                usuario_obj = usuario.objects.get(id=id_usuario)
                nueva_empresa.lista_de_seguridad.add(usuario_obj)
            except usuario.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Empresa creada exitosamente'
        }
        return JsonResponse(response_data)

# Arreglado
    def put(self, request, id):

        jd = json.loads(request.body)
        nombre_nuevo_empresa = jd['nombre_empresa']
        lista_de_contrato = jd['lista_de_contrato']
        lista_de_seguridad = jd['lista_de_seguridad']
        empresas = list(empresa.objects.filter(id=id).values())

        if len(empresas) > 0:
            empresa_aux = empresa.objects.get(id=id)
            empresa_aux.nombre_empresa=nombre_nuevo_empresa
            empresa_aux.lista_de_seguridad.clear()
            empresa_aux.lista_de_contrato.clear()

            for id_contratos in lista_de_contrato:
                try:
                    contrato_aux = contrato.objects.get(id=id_contratos)
                    empresa_aux.lista_de_contrato.add(contrato_aux)
                except contrato.DoesNotExist:
                    pass

            for id_seguridad in lista_de_seguridad:
                try:
                    seguridad_aux = usuario.objects.get(id=id_seguridad)
                    empresa_aux.lista_de_seguridad.add(seguridad_aux)
                except usuario.DoesNotExist:
                    pass

            empresa_aux.save()
            data = {'message': "Empresa actualizada"}
        else:
            data = {'message': "Empresa no encontrada..."}
        return JsonResponse(data)

    def delete(self, request, id):

        empresas = list(empresa.objects.filter(id=id).values())

        if len(empresas) > 0:
            empresa.objects.filter(id=id).delete()
            data = {'message': "Empresa eliminada"}
        else:
            data = {'message': "Empresa no encontrada"}
        return JsonResponse(data)


#class LoginView(APIView):
class LoginView(GenericAPIView):
    def post(self, request):
        usernameLogin = request.data.get('username')
        passwordLogin = request.data.get('password')

        try:
            user = usuario.objects.get(nombre_usuario=usernameLogin)
            passwordBaseDatos = user.contrasena

            # Obtener la sal de la contraseña almacenada en la base de datos
            print(passwordBaseDatos.encode('utf-8'))
            print(passwordLogin.encode('utf-8'))

            if bcrypt.checkpw(passwordLogin.encode('utf-8'), passwordBaseDatos.encode('utf-8')):
                #para serializar al usuario con todos sus datos para enviarlo despues de autenticarse
                usuario_serializado = UsuarioSerializer(user)
                return Response({'message': 'Inicio de sesión exitoso', 'usuario': usuario_serializado.data})
            else:
                return Response({'message': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
        except usuario.DoesNotExist:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)