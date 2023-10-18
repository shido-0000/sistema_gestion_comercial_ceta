from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
import json

from django.core import serializers

# Create your views here.


# clase norma
from api.recursos_humanos.models import norma, plazo, programa_de_cobro, trabajador, planificacion_de_gastos_personales, \
    categoria_del_profesor_del_servicio


class norma_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todas las normas, si id!=0 entonces va a devolver la norma cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            norm = list(norma.objects.filter(id=id).values())

            if len(norm) > 0:
                data = {'message': "Cargada 1 norma", 'norma': norm}
            else:
                data = {'message': "Norma no encontrada..."}
            return JsonResponse(data)
        else:
            norm = list(norma.objects.values())
            if len(norm) > 0:
                data = {'message': "Todas las normas cargadas", 'norma': norm}
            else:
                data = {'message': "Normas no encontradas..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_norma = jd['nombre']

        if nombre_norma == "":
            data = {'message': "Error, hay datos en blanco"}
        else:
            norma.objects.create(nombre=jd['nombre'], cantidad=jd['cantidad'], tipo=jd['tipo'])
            data = {'message': "Norma creada"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        normas = list(norma.objects.filter(id=id).values())

        if len(normas) > 0:
            norma_aux = norma.objects.get(id=id)
            norma_aux.nombre = jd['nombre']
            norma_aux.cantidad = jd['cantidad']
            norma_aux.tipo = jd['tipo']

            if jd['nombre'] == '':
                data = {'message': "Error, hay datos en blanco"}
            else:
                norma_aux.save()
                data = {'message': "norma actualizada"}
        else:
            data = {'message': "Norma no encontrada..."}

        return JsonResponse(data)

    def delete(self, request, id):

        normas = list(norma.objects.filter(id=id).values())

        if len(normas) > 0:
            norma.objects.filter(id=id).delete()
            data = {'message': "Norma eliminada"}
        else:
            data = {'message': "Norma no encontrada..."}
        return JsonResponse(data)


# clase plazo


class plazo_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los plazos, si id!=0 entonces va a devolver el plazo cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            plazos = list(plazo.objects.filter(id=id).values())

            if len(plazos) > 0:
                data = {'message': "Cargado 1 plazo", 'plazos': plazos}
            else:
                data = {'message': "Plazo no encontrado..."}
            return JsonResponse(data)
        else:
            plazos = list(plazo.objects.values())

            if len(plazos) > 0:
                data = {'message': "Todos los plazos cargados", 'plazos': plazos}
            else:
                data = {'message': "Plazos no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        plazo.objects.create(nombre_plazo=jd['nombre_plazo'], remuneracion=jd['remuneracion'],
                             cumplimiento_de_normas=jd['cumplimiento_de_normas'], total_asignado=jd['total_asignado'],
                             porcentaje=jd['porcentaje'])
        data = {'message': "Plazo creado"}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        plazos = list(plazo.objects.filter(id=id).values())

        if len(plazos) > 0:
            plazo_aux = plazo.objects.get(id=id)
            plazo_aux.nombre_plazo = jd['nombre_plazo']
            plazo_aux.remuneracion = jd['remuneracion']
            plazo_aux.cumplimiento_de_normas = jd['cumplimiento_de_normas']
            plazo_aux.total_asignado = jd['total_asignado']
            plazo_aux.porcentaje = jd['porcentaje']

            plazo_aux.save()
            data = {'message': "Plazo actualizado"}
        else:
            data = {'message': "Plazo no encontrado..."}

        return JsonResponse(data)

    def delete(self, request, id):

        plazos = list(plazo.objects.filter(id=id).values())
        if len(plazos) > 0:
            plazo.objects.filter(id=id).delete()
            data = {'message': "Plazo eliminado"}
        else:
            data = {'message': "Plazo no encontrado..."}
        return JsonResponse(data)


# clase programa de cobro


class programa_de_cobro_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los servicios, si id!=0 entonces va a devolver el servicio cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            programa = list(programa_de_cobro.objects.filter(id=id).values())

            if len(programa) > 0:
                data = {'message': "Cargado 1 programa", 'programa_de_cobro': programa}
            else:
                data = {'message': "Programa no encontrado..."}
            return JsonResponse(data)
        else:
            programa = list(programa_de_cobro.objects.values())

            if len(programa) > 0:
                data = {'message': "Todos los programas cargados", 'programa_de_cobro': programa}
            else:
                data = {'message': "Programas no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        programa_de_cobro.objects.create(nombre_programa=jd['nombre_programa'], fecha=jd['fecha'],
                                         plan_MN=jd['plan_MN'], plan_USD=jd['plan_USD'],
                                         remuneracion=jd['remuneracion'])
        data = {'message': "Programa creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        programa = list(programa_de_cobro.objects.filter(id=id).values())

        if len(programa) > 0:
            programa_aux = programa_de_cobro.objects.get(id=id)
            programa_aux.nombre_programa = jd['nombre_programa']
            programa_aux.fecha = jd['fecha']
            programa_aux.plan_MN = jd['plan_MN']
            programa_aux.plan_USD = jd['plan_USD']
            programa_aux.remuneracion = jd['remuneracion']

            programa_aux.save()
            data = {'message': "Programa actualizado"}
        else:
            data = {'message': "Programa no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        programa = list(programa_de_cobro.objects.filter(id=id).values())

        if len(programa) > 0:
            programa_de_cobro.objects.filter(id=id).delete()
            data = {'message': "Programa eliminado"}
        else:
            data = {'message': "Programa no encontrado..."}
        return JsonResponse(data)

    # clase trabajador


class trabajador_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los trabajadores, si id!=0 entonces va a devolver el trabajador cuyo id es igual
    # al valor
    def get(self, request, id=0):

        if id > 0:
            trabajadores = list(trabajador.objects.filter(id_trabajador=id).all())
            trabajadores_json = serializers.serialize('json', trabajadores)

            if len(trabajadores) > 0:
                data = {'message': "Cargado 1 trabajador", 'trabajador': trabajadores_json}
            else:
                data = {'message': "Trabajador no encontrado..."}
            return JsonResponse(data)
        else:
            trabajadores = trabajador.objects.all()
            trabajadores_json = serializers.serialize('json', trabajadores)

            if len(trabajadores) > 0:
                data = {'message': "Todos los trabajadores cargados", 'trabajadores': trabajadores_json}
            else:
                data = {'message': "Trabajadores no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        id_trabajador = data.get('id_trabajador')
        nombre = data.get('nombre')
        lista_plazo = data.get('lista_plazo')
        id_categoria_del_profesor_del_servicio = data.get('id_categoria_del_profesor_del_servicio')

        nuevo_trabajador = None  # Define nuevo_trabajador con un valor predeterminado

        try:
            categoria_obj = categoria_del_profesor_del_servicio.objects.get(
                id=id_categoria_del_profesor_del_servicio)  # Obtener una instancia válida del modelo categoria

            nuevo_trabajador = trabajador.objects.create(id_trabajador=id_trabajador, nombre=nombre,
                                                         id_categoria_del_profesor_del_servicio=categoria_obj)

        except categoria_del_profesor_del_servicio.DoesNotExist:
            data = {'message': "La categoría especificada no existe"}

            # Guardar el objeto en la base de datos
            nuevo_trabajador.save()

        # Asignar los plazos a la lista de plazos del trabajador
        for id_plazo in lista_plazo:
            try:
                plazo_obj = plazo.objects.get(id=id_plazo)
                nuevo_trabajador.lista_plazo.add(plazo_obj)
            except plazo.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Trabajador creado exitosamente'
        }
        return JsonResponse(response_data)

    ## hay que revisarlo no modifica ni id ni nombre (Arreglado)
    def put(self, request, id):
        jd = json.loads(request.body)
        nuevo_nombre = jd['nombre']
        nueva_lista_de_plazos = jd['lista_plazo']
        id_categoria_del_profesor_del_servicio = jd['id_categoria_del_profesor_del_servicio']
        traba = list(trabajador.objects.filter(id_trabajador=id).values())

        if len(traba) > 0:
            trabajador_aux = trabajador.objects.get(id_trabajador=id)
            trabajador_aux.nombre = nuevo_nombre

            categoria_del_profesor_del_servicio_instancia = categoria_del_profesor_del_servicio.objects.get(
                id=id_categoria_del_profesor_del_servicio)
            trabajador_aux.id_categoria_del_profesor_del_servicio = categoria_del_profesor_del_servicio_instancia
            trabajador_aux.lista_plazo.clear()

            for id_plazos in nueva_lista_de_plazos:
                try:
                    plazo_auxiliar = plazo.objects.get(id=id_plazos)
                    trabajador_aux.lista_plazo.add(plazo_auxiliar)
                except plazo.DoesNotExist:
                    pass

            trabajador_aux.save()
            data = {'message': "Trabajador actualizado con exito"}
        else:
            data = {'message': "Trabajador no encontrado"}
        return JsonResponse(data)

    def delete(self, request, id):
        # obtener el trabajador por su id

        try:
            trabajador_obj = trabajador.objects.get(id_trabajador=id)
        except trabajador.DoesNotExist:
            # si el trabajador no existe, devolver error 404

            data = {'error': 'Trabajador no encontrado'}
            return JsonResponse(data, status=404)

        # eliminar el trabajador si lo encuentra
        trabajador_obj.delete()

        data = {'message': 'Trabajador eliminado'}
        return JsonResponse(data)


# clase planificacion de gastos personales


class planificacion_de_gastos_personales_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los planificacion_de_gastos_personales, si id!=0 entonces va a devolver el planificacion_de_gastos_personales cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            gastos = list(planificacion_de_gastos_personales.objects.filter(id=id).all())
            gastos_json = serializers.serialize('json', gastos)

            if len(gastos) > 0:
                data = {'message': "Cargado 1 gastos personales", 'gastos personales de los trabajadores': gastos_json}
            else:
                data = {'message': "Gastos personales de los trabajadores no encontrados..."}
            return JsonResponse(data)
        else:
            gastos = planificacion_de_gastos_personales.objects.all()
            gastos_json = serializers.serialize('json', gastos)

            if len(gastos) > 0:
                data = {'message': "Todos los gastos personales cargados",
                        'gastos personales de los trabajadores': gastos_json}
            else:
                data = {'message': "Gastos personales de los trabajadores no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        ejecucion_fuera_de_provincia = data.get('ejecucion_fuera_de_provincia')
        lista_trabajador = data.get('lista_trabajador')

        if ejecucion_fuera_de_provincia is None:
            ejecucion_fuera_de_provincia = False


        # Crear una nueva objeto de planificacion de gastos
        planificacion_de_gastos = planificacion_de_gastos_personales(
            ejecucion_fuera_de_provincia=ejecucion_fuera_de_provincia)

        # Guardar el objeto en la base de datos
        planificacion_de_gastos.save()

        # Asignar los trabajadores a la lista de gastos
        for id_trabajador in lista_trabajador:
            try:
                trabajador_obj = trabajador.objects.get(id_trabajador=id_trabajador)
                planificacion_de_gastos.lista_trabajador.add(trabajador_obj)
            except plazo.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Planificación creada exitosamente'
        }
        return JsonResponse(response_data)

    # hay que revisarlo (Arreglado)
    def put(self, request, id):
        jd = json.loads(request.body)
        ejecucion_fuera_de_provincia = jd.get('ejecucion_fuera_de_provincia')
        lista_trabajador = jd.get('lista_trabajador')

        gastos = list(planificacion_de_gastos_personales.objects.filter(id=id))

        if len(gastos) > 0:
            gastos_obj = planificacion_de_gastos_personales.objects.get(id=id)
            gastos_obj.ejecucion_fuera_de_provincia = ejecucion_fuera_de_provincia
            gastos_obj.lista_trabajador.clear()

            for id_trabajador in lista_trabajador:
                try:
                    trabajador_obj = trabajador.objects.get(id_trabajador=id_trabajador)
                    gastos_obj.lista_trabajador.add(trabajador_obj)
                except plazo.DoesNotExist:
                    pass

            gastos_obj.save()
            data = {'message': "Planificación de Gastos personales actualizado"}
        else:
            data = {'message': "Planificación de Gastos personales no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        gastos = list(planificacion_de_gastos_personales.objects.filter(id=id).values())

        if len(gastos) > 0:
            planificacion_de_gastos_personales.objects.filter(id=id).delete()
            data = {'message': "Planificación de gastos personales eliminado"}
        else:
            data = {'message': "Planificación de gastos personales no encontrado"}
        return JsonResponse(data)


# clase categoria_profesor (nuevo)

class categoria_profesor_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los servicios, si id!=0 entonces va a devolver el servicio cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            categoria_profesor = list(categoria_del_profesor_del_servicio.objects.filter(id=id).values())
            categoria_profesor_json = serializers.serialize('json', categoria_profesor)

            if len(categoria_profesor) > 0:
                data = {'message': "Cargado 1 categoria del profesor", 'categoria_profesor': categoria_profesor_json}
            else:
                data = {'message': "Categoría del profesor no encontrada..."}
            return JsonResponse(data)
        else:
            categoria_profesor = categoria_del_profesor_del_servicio.objects.all()
            categoria_profesor_json = serializers.serialize('json', categoria_profesor)

            if len(categoria_profesor) > 0:
                data = {'message': "Todos las categoría de profesores cargados",
                        'categoria_profesor': categoria_profesor_json}
            else:
                data = {'message': "Categoría de profesores no encontradas..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_categoria = jd.get('nombre_categoria')
        tarifa_por_hora = jd.get('tarifa_por_hora')
        total_de_horas = jd.get('total_de_horas')

        # Crear un nuevo objeto de categoria
        nueva_categoria = categoria_del_profesor_del_servicio(nombre_categoria=nombre_categoria,
                                                              tarifa_por_hora=tarifa_por_hora,
                                                              total_de_horas=total_de_horas)

        # Guardar el objeto en la base de datos
        nueva_categoria.save()
        data = {'message': "Categoría de profesor creada"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)

        nombre_categoria = jd.get('nombre_categoria')
        tarifa_por_hora = jd.get('tarifa_por_hora')
        total_de_horas = jd.get('total_de_horas')

        categoria_profesor = list(categoria_del_profesor_del_servicio.objects.filter(id=id).values())

        print(nombre_categoria)
        if len(categoria_profesor) > 0:
            categoria_profesor_aux = categoria_del_profesor_del_servicio.objects.get(id=id)
            categoria_profesor_aux.nombre_categoria = nombre_categoria
            categoria_profesor_aux.tarifa_por_hora = tarifa_por_hora
            categoria_profesor_aux.total_de_horas = total_de_horas

            categoria_profesor_aux.save()
            data = {'message': "Categoría de profesor actualizada"}
        else:
            data = {'message': "Categoría de profesor no encontrada..."}
        return JsonResponse(data)

    def delete(self, request, id):

        categoria_profesor = list(categoria_del_profesor_del_servicio.objects.filter(id=id).values())
        print(categoria_profesor)

        if len(categoria_profesor) > 0:
            categoria_del_profesor_del_servicio.objects.filter(id=id).delete()
            data = {'message': "Categoría de profesor eliminada"}
        else:
            data = {'message': "Categoría de profesor no encontrada..."}
        return JsonResponse(data)
