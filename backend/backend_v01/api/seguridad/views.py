from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
import json

#para cifrar las contraseñas
import bcrypt


from api.seguridad.models import rol, usuario

# Create your views here.


# clase rol


class rol_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            roles = list(rol.objects.filter(id=id).values())

            if len(roles) > 0:
                data = {'message': "Cargado 1 rol", 'roles': roles}
            else:
                data = {'message': "Rol no encontrado..."}
            return JsonResponse(data)
        else:
            roles = list(rol.objects.values())
            if len(roles) > 0:
                data = {'message': "Todos los roles cargado", 'roles': roles}
            else:
                data = {'message': "Roles no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_rol = jd['nombre_rol']

        if nombre_rol == "":
            data = {'message': "Error, faltan campos por llenar"}
        else:
            rol.objects.create(nombre_rol=jd['nombre_rol'])
            data = {'message': "Rol creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        roles = list(rol.objects.filter(id=id).values())

        if len(roles) > 0:
            rol_aux = rol.objects.get(id=id)
            rol_aux.nombre_rol = jd['nombre_rol']

            rol_aux.save()
            data = {'message': "Rol actualizado"}
        else:
            data = {'message': "Rol no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        roles = list(rol.objects.filter(id=id).values())

        if len(roles) > 0:
            rol.objects.filter(id=id).delete()
            data = {'message': "Rol eliminado"}
        else:
            data = {'message': "Rol no encontrado..."}
        return JsonResponse(data)


# clase usuario


class usuario_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los usuarios, si id!=0 entonces va a devolver el usuario cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            usuarios = list(usuario.objects.filter(id=id).values())

            if len(usuarios) > 0:
                data = {'message': "Cargado 1 usuario", 'usuario': usuarios}
            else:
                data = {'message': "Usuario no encontrado..."}
            return JsonResponse(data)
        else:
            usuarios = list(usuario.objects.values())

            if len(usuarios) > 0:
                data = {'message': "Todos los usuarios cargados", 'usuarios': usuarios}
            else:
                data = {'message': "Usuarios no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        nombre_completo = jd['nombre_completo']
        nombre_usuario = jd['nombre_usuario']
        contrasena = jd['contrasena']
        id_rol = jd['id_rol']

        if nombre_usuario == "" or contrasena == "" or id_rol is None:
            data = {'message': "Error, faltan campos por llenar"}
        else:
            try:
                rol_obj = rol.objects.get(id=id_rol)  # Obtener una instancia válida del modelo rol
                # Cifrar la contraseña antes de guardarla

                usuario.objects.create(nombre_completo=nombre_completo, nombre_usuario=nombre_usuario, contrasena=contrasena, id_rol=rol_obj)
                data = {'message': "Usuario creado"}
            except rol.DoesNotExist:
                data = {'message': "El rol especificado no existe"}

        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        usuarios = list(usuario.objects.filter(id=id).values())

        if len(usuarios) > 0:
            usuario_aux = usuario.objects.get(id=id)
            usuario_aux.nombre_completo = jd['nombre_completo']
            usuario_aux.nombre_usuario = jd['nombre_usuario']
            usuario_aux.contrasena = jd['contrasena']

            # Obtener la instancia del rol basada en el ID
            id_rol = jd['id_rol']
            rol_instancia = rol.objects.get(id=id_rol)

            # Asignar la instancia del rol
            usuario_aux.id_rol = rol_instancia

            usuario_aux.save()
            data = {'message': "Usuario actualizado"}
        else:
            data = {'message': "Usuario no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        usuarios = list(usuario.objects.filter(id=id).values())

        if len(usuarios) > 0:
            usuario.objects.filter(id=id).delete()
            data = {'message': "Usuario eliminado"}
        else:
            data = {'message': "Usuario no encontrado..."}
        return JsonResponse(data)