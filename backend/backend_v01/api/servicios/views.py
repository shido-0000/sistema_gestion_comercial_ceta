from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

from api.economia.models import pagos_al_cliente, facturacion_pagos
from api.recursos_humanos.models import categoria_del_profesor_del_servicio, trabajador, plazo
from api.servicios.models import servicio, area_participante, tareas_detalladas, recursos_necesarios, \
    productos_necesarios, encuetros_por_semana, cronograma_para_ficha_tecnica, resultados_para_ficha_tecnica, \
    resultados_obtenidos_para_ficha_tecnica, \
    tiempo_dedicado_en_horas_mensuales, registros_de_derechos_y_propiedad, control_de_documentos_del_contrato, \
    consideraciones_para_la_ficha_tecnica, valor_del_contrato_por_los_servicios_comercializados, ficha_tecnica


# Create your views here.


# clase servicio (actualizado)


class servicio_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los servicios, si id!=0 entonces va a devolver el servicio cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            servicios = list(servicio.objects.filter(id=id).values())
            servicios_json = serializers.serialize('json', servicios)

            if len(servicios) > 0:
                data = {'message': "Cargado 1 servicio", 'servicio': servicios_json}
            else:
                data = {'message': "Servicio no encontrado..."}
            return JsonResponse(data)
        else:
            servicios = servicio.objects.all()
            servicios_json = serializers.serialize('json', servicios)

            if len(servicios) > 0:
                data = {'message': "Todos los servicios cargados", 'servicio': servicios_json}
            else:
                data = {'message': "Servicios no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_servicio = jd.get('nombre_servicio')
        #lista_categorias = jd.get('lista_categorias')
        lista_trabajadores = jd.get('lista_trabajadores')
        capacidad_de_matricula = jd.get('capacidad_de_matricula')

        # Crear un nuevo objeto de servicio
        nuevo_servicio = servicio(nombre_servicio=nombre_servicio, capacidad_de_matricula=capacidad_de_matricula)

        # Guardar el objeto en la base de datos
        nuevo_servicio.save()

        # Asignar las categorias a la lista de categorias del servicio
        #for id_categoria in lista_categorias:
        #    try:
         #       categoria_obj = categoria_del_profesor_del_servicio.objects.get(id=id_categoria)
         #       nuevo_servicio.lista_categorias.add(categoria_obj)
         #   except categoria_del_profesor_del_servicio.DoesNotExist:
          #      pass
        for id in lista_trabajadores:
            try:
                trabajador_obj = trabajador.objects.get(id_trabajador=id)
                nuevo_servicio.lista_trabajadores.add(trabajador_obj)
            except trabajador.DoesNotExist:
                pass
        data = {'message': "Servicio creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        nombre_servicio = jd.get('nombre_servicio')
        #lista_categorias = jd.get('lista_categorias')
        lista_trabajadores = jd.get('lista_trabajadores')
        capacidad_de_matricula = jd.get('capacidad_de_matricula')

        servicios = list(servicio.objects.filter(id=id).values())

        if len(servicios) > 0:
            servicio_aux = servicio.objects.get(id=id)
            servicio_aux.nombre_servicio = nombre_servicio
            servicio_aux.capacidad_de_matricula = capacidad_de_matricula

            servicio_aux.lista_trabajadores.clear()

            #for id_categoria in lista_categorias:
            #    try:
            #        categoria_obj = categoria_del_profesor_del_servicio.objects.get(id=id_categoria)
              #      servicio_aux.lista_categorias.add(categoria_obj)
            #    except categoria_del_profesor_del_servicio.DoesNotExist:
             #       pass

            for id in lista_trabajadores:
                try:
                    trabajador_obj = trabajador.objects.get(id_trabajador=id)
                    servicio_aux.lista_trabajadores.add(trabajador_obj)
                except trabajador.DoesNotExist:
                    pass

            servicio_aux.save()
            data = {'message': "Servicio actualizado"}
        else:
            data = {'message': "Servicio no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        servicios = list(servicio.objects.filter(id=id).values())

        if len(servicios) > 0:
            servicio.objects.filter(id=id).delete()
            data = {'message': "Servicio eliminado"}
        else:
            data = {'message': "Servicio no encontrado"}
        return JsonResponse(data)


# clase area_participante


class area_participante_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los area_participante, si id!=0 entonces va a devolver el area_participante cuyo id es igual al valor

    def get(self, request, id=0):

        if id > 0:
            areas = list(area_participante.objects.filter(id=id).all())
            areas_json = serializers.serialize('json', areas)

            if len(areas) > 0:
                data = {'message': "Cargada 1 área", 'área': areas_json}
            else:
                data = {'message': "Trabajador no encontrado..."}
            return JsonResponse(data)
        else:
            areas = area_participante.objects.all()
            areas_json = serializers.serialize('json', areas)

            if len(areas) > 0:
                data = {'message': "Todas las áreas cargadas", 'áreas': areas_json}
            else:
                data = {'message': "Áreas no encontradas..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        nombre = data.get('nombre')
        porcentaje = data.get('porcentaje')
        lista_trabajador = data.get('lista_trabajador')

        # Crear un nuevo objeto de Trabajador
        nueva_area = area_participante(nombre=nombre, porcentaje=porcentaje)

        # Guardar el objeto en la base de datos
        nueva_area.save()

        # Asignar los trabajadores a la lista de trabajadores del area
        for id in lista_trabajador:
            try:
                trabajador_obj = trabajador.objects.get(id_trabajador=id)
                nueva_area.lista_trabajador.add(trabajador_obj)
            except trabajador.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Area de participantes creada exitosamente'
        }
        return JsonResponse(response_data)

    # Arreglado
    def put(self, request, id):
        jd = json.loads(request.body)
        nombre = jd.get('nombre')
        porcentaje = jd.get('porcentaje')
        lista_trabajador = jd.get('lista_trabajador')

        areas = list(area_participante.objects.filter(id=id))

        if len(areas) > 0:

            areas_obj = area_participante.objects.get(id=id)
            areas_obj.nombre = nombre
            areas_obj.porcentaje = porcentaje
            areas_obj.lista_trabajador.clear()

            for id_trabajador in lista_trabajador:
                try:
                    trabajador_obj = trabajador.objects.get(id_trabajador=id_trabajador)
                    areas_obj.lista_trabajador.add(trabajador_obj)
                except plazo.DoesNotExist:
                    pass

            areas_obj.save()
            data = {'message': "Área de participantes actualizada"}
        else:
            data = {'message': "Área de participantes no encontrada..."}
        return JsonResponse(data)

    def delete(self, request, id):
        areas = list(area_participante.objects.filter(id=id).values())

        if len(areas) > 0:
            area_participante.objects.filter(id=id).delete()
            data = {'message': "Área participante eliminada"}
        else:
            data = {'message': "Área participante no encontrada"}
        return JsonResponse(data)


# Jonathan

# clase tareas_detalladas


class tareas_detalladas_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            tareas = list(tareas_detalladas.objects.filter(id=id).values())

            if len(tareas) > 0:
                data = {'message': "Cargado 1 tarea", 'tareas_detalladas': tareas}
            else:
                data = {'message': "Tarea no encontrado..."}
            return JsonResponse(data)
        else:
            tareas = list(tareas_detalladas.objects.values())
            if len(tareas) > 0:
                data = {'message': "Todos las tareas cargado", 'tareas_detalladas': tareas}
            else:
                data = {'message': "Tareas no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_completo = jd['nombre_completo']

        if nombre_completo == "":
            data = {'message': "Error, faltan campos por llenar"}
        else:
            tareas_detalladas.objects.create(nombre_completo=jd['nombre_completo'])
            data = {'message': "Tarea creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        tareas = list(tareas_detalladas.objects.filter(id=id).values())

        if len(tareas) > 0:
            tareas_aux = tareas_detalladas.objects.get(id=id)
            tareas_aux.nombre_completo = jd['nombre_completo']

            tareas_aux.save()
            data = {'message': "Tarea actualizado"}
        else:
            data = {'message': "Tarea no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        tareas = list(tareas_detalladas.objects.filter(id=id).values())

        if len(tareas) > 0:
            tareas_detalladas.objects.filter(id=id).delete()
            data = {'message': "Tarea eliminado"}
        else:
            data = {'message': "Tarea no encontrado..."}
        return JsonResponse(data)


# clase recursos_necesarios


class recursos_necesarios_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            recursos = list(recursos_necesarios.objects.filter(id=id).values())

            if len(recursos) > 0:
                data = {'message': "Cargado 1 recurso", 'recursos_necesarios': recursos}
            else:
                data = {'message': "Recurso no encontrado..."}
            return JsonResponse(data)
        else:
            recursos = list(recursos_necesarios.objects.values())
            if len(recursos) > 0:
                data = {'message': "Todos las recursos cargado", 'recursos_necesarios': recursos}
            else:
                data = {'message': "recursos no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_completo = jd['nombre_completo']
        descripcion = jd['descripcion']
        cantidad = jd['cantidad']
        caracteristicas_especiales = jd['caracteristicas_especiales']
        justificacion = jd['justificacion']
        valor_unitario = jd['valor_unitario']
        total = jd['total']

        recursos_necesarios.objects.create(nombre_completo=jd['nombre_completo'], descripcion=descripcion,
                                           cantidad=cantidad, caracteristicas_especiales=caracteristicas_especiales,
                                           justificacion=justificacion, valor_unitario=valor_unitario, total=total)
        data = {'message': "Recurso creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        recursos = list(recursos_necesarios.objects.filter(id=id).values())

        if len(recursos) > 0:
            recursos_aux = recursos_necesarios.objects.get(id=id)
            recursos_aux.nombre_completo = jd['nombre_completo']
            recursos_aux.descripcion = jd['descripcion']
            recursos_aux.cantidad = jd['cantidad']
            recursos_aux.caracteristicas_especiales = jd['caracteristicas_especiales']
            recursos_aux.justificacion = jd['justificacion']
            recursos_aux.valor_unitario = jd['valor_unitario']
            recursos_aux.total = jd['total']

            recursos_aux.save()
            data = {'message': "Recursos actualizado"}
        else:
            data = {'message': "Recursos no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        recursos = list(recursos_necesarios.objects.filter(id=id).values())

        if len(recursos) > 0:
            recursos_necesarios.objects.filter(id=id).delete()
            data = {'message': "Recurso eliminado"}
        else:
            data = {'message': "Recurso no encontrado..."}
        return JsonResponse(data)


# clase productos_necesarios


class productos_necesarios_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            productos_necesarios_o = list(productos_necesarios.objects.filter(id=id).values())

            if len(productos_necesarios_o) > 0:
                data = {'message': "Cargado 1 productos necesarios", 'productos_necesarios': productos_necesarios_o}
            else:
                data = {'message': "productos necesarios no encontrado..."}
            return JsonResponse(data)
        else:
            productos_necesarios_o = list(productos_necesarios.objects.values())
            if len(productos_necesarios_o) > 0:
                data = {'message': "Todos las productos necesarios cargado",
                        'productos_necesarios': productos_necesarios_o}
            else:
                data = {'message': "productos necesarios no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_completo = jd['nombre_completo']
        descripcion = jd['descripcion']

        productos_necesarios.objects.create(nombre_completo=jd['nombre_completo'], descripcion=descripcion)
        data = {'message': "productos_necesarios creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        productos_necesarios_o = list(productos_necesarios.objects.filter(id=id).values())

        if len(productos_necesarios_o) > 0:
            productos_necesarios_o_aux = productos_necesarios.objects.get(id=id)
            productos_necesarios_o_aux.nombre_completo = jd['nombre_completo']
            productos_necesarios_o_aux.descripcion = jd['descripcion']

            productos_necesarios_o_aux.save()
            data = {'message': "productos_necesarios actualizado"}
        else:
            data = {'message': "productos_necesarios no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        productos_necesarios_o = list(productos_necesarios.objects.filter(id=id).values())

        if len(productos_necesarios_o) > 0:
            productos_necesarios.objects.filter(id=id).delete()
            data = {'message': "productos_necesarios eliminado"}
        else:
            data = {'message': "productos_necesarios no encontrado..."}
        return JsonResponse(data)


# clase encuetros_por_semana


class encuetros_por_semana_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            encuetros = list(encuetros_por_semana.objects.filter(id=id).values())

            if len(encuetros) > 0:
                data = {'message': "Cargado 1 encuetros_por_semana", 'encuetros_por_semana': encuetros}
            else:
                data = {'message': "encuetros_por_semana no encontrado..."}
            return JsonResponse(data)
        else:
            encuentros = list(encuetros_por_semana.objects.values())
            if len(encuentros) > 0:
                data = {'message': "Todos los encuetros_por_semana cargado",
                        'encuetros_por_semana': encuentros}
            else:
                data = {'message': "encuetros_por_semana no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        cantidad = jd['cantidad']
        semana = jd['semana']

        encuetros_por_semana.objects.create(cantidad=cantidad, semana=semana)
        data = {'message': "encuetros_por_semana creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        encuentros = list(encuetros_por_semana.objects.filter(id=id).values())

        if len(encuentros) > 0:
            encuentros_aux = encuetros_por_semana.objects.get(id=id)
            encuentros_aux.cantidad = jd['cantidad']
            encuentros_aux.semana = jd['semana']

            encuentros_aux.save()
            data = {'message': "encuetros_por_semana actualizado"}
        else:
            data = {'message': "encuetros_por_semana no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        encuentros = list(encuetros_por_semana.objects.filter(id=id).values())

        if len(encuentros) > 0:
            encuetros_por_semana.objects.filter(id=id).delete()
            data = {'message': "encuetros_por_semana eliminado"}
        else:
            data = {'message': "encuetros_por_semana no encontrado..."}
        return JsonResponse(data)


# clase cronograma_para_ficha_tecnica


class cronograma_para_ficha_tecnica_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los area_participante, si id!=0 entonces va a devolver el area_participante cuyo id es igual al valor

    def get(self, request, id=0):

        if id > 0:
            cronograma = list(cronograma_para_ficha_tecnica.objects.filter(id=id).all())
            cronograma_json = serializers.serialize('json', cronograma)

            if len(cronograma) > 0:
                data = {'message': "Cargada 1 cronograma", 'cronograma_para_ficha_tecnica': cronograma_json}
            else:
                data = {'message': "Cronograma no encontrado..."}
            return JsonResponse(data)
        else:
            cronograma = cronograma_para_ficha_tecnica.objects.all()
            cronograma_json = serializers.serialize('json', cronograma)

            if len(cronograma) > 0:
                data = {'message': "Todas las cronogramas cargadas", 'cronograma_para_ficha_tecnica': cronograma_json}
            else:
                data = {'message': "Cronogramas no encontradas..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        numero_de_la_tarea = data.get('numero_de_la_tarea')
        nombre_completo_de_la_tarea = data.get('nombre_completo_de_la_tarea')
        lista_encuetros_por_semana = data.get('lista_encuetros_por_semana')

        # Crear un nuevo objeto de Trabajador
        nueva_cronograma_para_ficha_tecnica = cronograma_para_ficha_tecnica(numero_de_la_tarea=numero_de_la_tarea,
                                                                            nombre_completo_de_la_tarea=nombre_completo_de_la_tarea)

        # Guardar el objeto en la base de datos
        nueva_cronograma_para_ficha_tecnica.save()

        # Asignar los trabajadores a la lista de trabajadores del area
        for id in lista_encuetros_por_semana:
            try:
                encuetros_por_semana_obj = encuetros_por_semana.objects.get(id=id)
                nueva_cronograma_para_ficha_tecnica.lista_encuetros_por_semana.add(encuetros_por_semana_obj)
            except encuetros_por_semana.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'cronograma_para_ficha_tecnica creada exitosamente'
        }
        return JsonResponse(response_data)

    # Arreglado
    def put(self, request, id):
        jd = json.loads(request.body)
        numero_de_la_tarea = jd.get('numero_de_la_tarea')
        nombre_completo_de_la_tarea = jd.get('nombre_completo_de_la_tarea')
        lista_encuetros_por_semana = jd.get('lista_encuetros_por_semana')

        cronograma = list(cronograma_para_ficha_tecnica.objects.filter(id=id))

        if len(cronograma) > 0:

            cronograma_para_ficha_tecnica_obj = cronograma_para_ficha_tecnica.objects.get(id=id)
            cronograma_para_ficha_tecnica_obj.numero_de_la_tarea = numero_de_la_tarea
            cronograma_para_ficha_tecnica_obj.nombre_completo_de_la_tarea = nombre_completo_de_la_tarea
            cronograma_para_ficha_tecnica_obj.lista_encuetros_por_semana.clear()

            for id in lista_encuetros_por_semana:
                try:
                    encuetros_por_semana_obj = encuetros_por_semana.objects.get(id=id)
                    cronograma_para_ficha_tecnica_obj.lista_encuetros_por_semana.add(encuetros_por_semana_obj)
                except encuetros_por_semana.DoesNotExist:
                    pass

            cronograma_para_ficha_tecnica_obj.save()
            data = {'message': "cronograma_para_ficha_tecnica actualizada"}
        else:
            data = {'message': "cronograma_para_ficha_tecnica no encontrada..."}
        return JsonResponse(data)

    def delete(self, request, id):
        cronograma = list(cronograma_para_ficha_tecnica.objects.filter(id=id).values())

        if len(cronograma) > 0:
            cronograma_para_ficha_tecnica.objects.filter(id=id).delete()
            data = {'message': "cronograma_para_ficha_tecnica eliminada"}
        else:
            data = {'message': "cronograma_para_ficha_tecnica no encontrada"}
        return JsonResponse(data)


# clase resultados_para_ficha_tecnica


class resultados_para_ficha_tecnica_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            resultados = list(resultados_para_ficha_tecnica.objects.filter(id=id).values())

            if len(resultados) > 0:
                data = {'message': "Cargado 1 resultados_para_ficha_tecnica",
                        'resultados_para_ficha_tecnica': resultados}
            else:
                data = {'message': "resultados_para_ficha_tecnica no encontrado..."}
            return JsonResponse(data)
        else:
            resultados = list(resultados_para_ficha_tecnica.objects.values())
            if len(resultados) > 0:
                data = {'message': "Todos las resultados_para_ficha_tecnica cargado",
                        'resultados_para_ficha_tecnica': resultados}
            else:
                data = {'message': "resultados_para_ficha_tecnica no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        numero_de_la_tarea = jd['numero_de_la_tarea']
        nombre_completo_de_la_tarea = jd['nombre_completo_de_la_tarea']
        descripcion_del_tipo_de_entregable = jd['descripcion_del_tipo_de_entregable']
        formato_del_entregable = jd['formato_del_entregable']
        fecha_escrita_de_entrega_de_entregable = jd['fecha_escrita_de_entrega_de_entregable']

        resultados_para_ficha_tecnica.objects.create(numero_de_la_tarea=numero_de_la_tarea,
                                                     nombre_completo_de_la_tarea=nombre_completo_de_la_tarea,
                                                     descripcion_del_tipo_de_entregable=descripcion_del_tipo_de_entregable,
                                                     formato_del_entregable=formato_del_entregable,
                                                     fecha_escrita_de_entrega_de_entregable=fecha_escrita_de_entrega_de_entregable)
        data = {'message': "resultados_para_ficha_tecnica creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        resultados = list(resultados_para_ficha_tecnica.objects.filter(id=id).values())

        if len(resultados) > 0:
            resultados_para_ficha_tecnica_aux = resultados_para_ficha_tecnica.objects.get(id=id)
            resultados_para_ficha_tecnica_aux.numero_de_la_tarea = jd['numero_de_la_tarea']
            resultados_para_ficha_tecnica_aux.nombre_completo_de_la_tarea = jd['nombre_completo_de_la_tarea']
            resultados_para_ficha_tecnica_aux.descripcion_del_tipo_de_entregable = jd[
                'descripcion_del_tipo_de_entregable']
            resultados_para_ficha_tecnica_aux.formato_del_entregable = jd['formato_del_entregable']
            resultados_para_ficha_tecnica_aux.fecha_escrita_de_entrega_de_entregable = jd[
                'fecha_escrita_de_entrega_de_entregable']

            resultados_para_ficha_tecnica_aux.save()
            data = {'message': "resultados_para_ficha_tecnica actualizado"}
        else:
            data = {'message': "resultados_para_ficha_tecnica no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        resultados = list(resultados_para_ficha_tecnica.objects.filter(id=id).values())

        if len(resultados) > 0:
            resultados_para_ficha_tecnica.objects.filter(id=id).delete()
            data = {'message': "resultados_para_ficha_tecnica eliminado"}
        else:
            data = {'message': "resultados_para_ficha_tecnica no encontrado..."}
        return JsonResponse(data)


# clase resultados_obtenidos_para_ficha_tecnica


class resultados_obtenidos_para_ficha_tecnica_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            resultados = list(resultados_obtenidos_para_ficha_tecnica.objects.filter(id=id).values())

            if len(resultados) > 0:
                data = {'message': "Cargado 1 resultados_obtenidos_para_ficha_tecnica",
                        'resultados_obtenidos_para_ficha_tecnica': resultados}
            else:
                data = {'message': "resultados_para_ficha_tecnica no encontrado..."}
            return JsonResponse(data)
        else:
            resultados = list(resultados_obtenidos_para_ficha_tecnica.objects.values())
            if len(resultados) > 0:
                data = {'message': "Todos las resultados_obtenidos_para_ficha_tecnica cargado",
                        'resultados_obtenidos_para_ficha_tecnica': resultados}
            else:
                data = {'message': "resultados_obtenidos_para_ficha_tecnica no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_producto_obtenido = jd.get('nombre_producto_obtenido')
        descripcion_producto_obtenido = jd.get('descripcion_producto_obtenido')
        tipo_de_registro = jd.get('tipo_de_registro')

        resultados_obtenidos_para_ficha_tecnica.objects.create(nombre_producto_obtenido=nombre_producto_obtenido,
                                                               descripcion_producto_obtenido=descripcion_producto_obtenido,
                                                               tipo_de_registro=tipo_de_registro)
        data = {'message': "resultados_obtenidos_para_ficha_tecnica creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        resultados = list(resultados_obtenidos_para_ficha_tecnica.objects.filter(id=id).values())

        if len(resultados) > 0:
            resultados_obtenidos_para_ficha_tecnica_aux = resultados_obtenidos_para_ficha_tecnica.objects.get(id=id)
            resultados_obtenidos_para_ficha_tecnica_aux.nombre_producto_obtenido = jd['nombre_producto_obtenido']
            resultados_obtenidos_para_ficha_tecnica_aux.descripcion_producto_obtenido = jd[
                'descripcion_producto_obtenido']
            resultados_obtenidos_para_ficha_tecnica_aux.tipo_de_registro = jd['tipo_de_registro']

            resultados_obtenidos_para_ficha_tecnica_aux.save()
            data = {'message': "resultados_obtenidos_para_ficha_tecnica_aux actualizado"}
        else:
            data = {'message': "resultados_obtenidos_para_ficha_tecnica_aux no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        resultados = list(resultados_obtenidos_para_ficha_tecnica.objects.filter(id=id).values())

        if len(resultados) > 0:
            resultados_obtenidos_para_ficha_tecnica.objects.filter(id=id).delete()
            data = {'message': "resultados_obtenidos_para_ficha_tecnica eliminado"}
        else:
            data = {'message': "resultados_para_ficha_tecnica no encontrado..."}
        return JsonResponse(data)




# clase tiempo_dedicado_en_horas_mensuales


class tiempo_dedicado_en_horas_mensuales_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los usuarios, si id!=0 entonces va a devolver el usuario cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            tiempo = list(tiempo_dedicado_en_horas_mensuales.objects.filter(id=id).values())

            if len(tiempo) > 0:
                data = {'message': "Cargado 1 tiempo_dedicado_en_horas_mensuales",
                        'tiempo_dedicado_en_horas_mensuales': tiempo}
            else:
                data = {'message': "tiempo_dedicado_en_horas_mensuales no encontrado..."}
            return JsonResponse(data)
        else:
            tiempo = list(tiempo_dedicado_en_horas_mensuales.objects.values())

            if len(tiempo) > 0:
                data = {'message': "Todos los tiempo_dedicado_en_horas_mensuales cargados",
                        'tiempo_dedicado_en_horas_mensuales': tiempo}
            else:
                data = {'message': "tiempo_dedicado_en_horas_mensuales no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']
        horas_dedicadas = jd['horas_dedicadas']

        try:
            resultados_obtenidos_para_ficha_tecnica_obj = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)  # Obtener una instancia válida del modelo rol
            tiempo_dedicado_en_horas_mensuales.objects.create(horas_dedicadas=horas_dedicadas,
                                                              id_resultados_obtenidos_para_ficha_tecnica=resultados_obtenidos_para_ficha_tecnica_obj)
            data = {'message': "tiempo_dedicado_en_horas_mensuales creado"}
        except resultados_obtenidos_para_ficha_tecnica.DoesNotExist:
            data = {'message': "El resultados_obtenidos_para_ficha_tecnica especificado no existe"}

        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        tiempo = list(tiempo_dedicado_en_horas_mensuales.objects.filter(id=id).values())

        if len(tiempo) > 0:
            tiempo_dedicado_en_horas_mensuales_aux = tiempo_dedicado_en_horas_mensuales.objects.get(id=id)
            tiempo_dedicado_en_horas_mensuales_aux.horas_dedicadas = jd['horas_dedicadas']

            # Obtener la instancia basada en el ID
            id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']
            resultados_obtenidos_para_ficha_tecnica_instancia = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)

            # Asignar la instancia del rol
            tiempo_dedicado_en_horas_mensuales_aux.id_resultados_obtenidos_para_ficha_tecnica = resultados_obtenidos_para_ficha_tecnica_instancia

            tiempo_dedicado_en_horas_mensuales_aux.save()
            data = {'message': "tiempo_dedicado_en_horas_mensuales actualizado"}
        else:
            data = {'message': "tiempo_dedicado_en_horas_mensuales no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        tiempo = list(tiempo_dedicado_en_horas_mensuales.objects.filter(id=id).values())

        if len(tiempo) > 0:
            tiempo_dedicado_en_horas_mensuales.objects.filter(id=id).delete()
            data = {'message': "tiempo_dedicado_en_horas_mensuales eliminado"}
        else:
            data = {'message': "tiempo_dedicado_en_horas_mensuales no encontrado..."}
        return JsonResponse(data)


# clase registros_de_derechos_y_propiedad


class registros_de_derechos_y_propiedad_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los usuarios, si id!=0 entonces va a devolver el usuario cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            registros = list(registros_de_derechos_y_propiedad.objects.filter(id=id).values())

            if len(registros) > 0:
                data = {'message': "Cargado 1 registros_de_derechos_y_propiedad",
                        'registros_de_derechos_y_propiedad': registros}
            else:
                data = {'message': "registros_de_derechos_y_propiedad no encontrado..."}
            return JsonResponse(data)
        else:
            registros = list(registros_de_derechos_y_propiedad.objects.values())

            if len(registros) > 0:
                data = {'message': "Todos los registros_de_derechos_y_propiedad cargados",
                        'registros_de_derechos_y_propiedad': registros}
            else:
                data = {'message': "registros_de_derechos_y_propiedad no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']
        porcentaje_de_la_cujae = jd['porcentaje_de_la_cujae']
        porcentaje_del_cliente = jd['porcentaje_del_cliente']
        tipo_de_registro = jd['tipo_de_registro']

        try:
            resultados_obtenidos_para_ficha_tecnica_obj = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)  # Obtener una instancia válida del modelo
            registros_de_derechos_y_propiedad.objects.create(
                id_resultados_obtenidos_para_ficha_tecnica=resultados_obtenidos_para_ficha_tecnica_obj,
                porcentaje_de_la_cujae=porcentaje_de_la_cujae, porcentaje_del_cliente=porcentaje_del_cliente,
                tipo_de_registro=tipo_de_registro)
            data = {'message': "registros_de_derechos_y_propiedad creado"}
        except resultados_obtenidos_para_ficha_tecnica.DoesNotExist:
            data = {'message': "El resultados_obtenidos_para_ficha_tecnica especificado no existe"}

        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        registros = list(registros_de_derechos_y_propiedad.objects.filter(id=id).values())

        if len(registros) > 0:
            registros_de_derechos_y_propiedad_aux = registros_de_derechos_y_propiedad.objects.get(id=id)
            registros_de_derechos_y_propiedad_aux.porcentaje_de_la_cujae = jd['porcentaje_de_la_cujae']
            registros_de_derechos_y_propiedad_aux.porcentaje_del_cliente = jd['porcentaje_del_cliente']
            registros_de_derechos_y_propiedad_aux.tipo_de_registro = jd['tipo_de_registro']

            # Obtener la instancia basada en el ID
            id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']
            resultados_obtenidos_para_ficha_tecnica_instancia = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)

            # Asignar la instancia
            registros_de_derechos_y_propiedad_aux.id_resultados_obtenidos_para_ficha_tecnica = resultados_obtenidos_para_ficha_tecnica_instancia

            registros_de_derechos_y_propiedad_aux.save()
            data = {'message': "registros_de_derechos_y_propiedad actualizado"}
        else:
            data = {'message': "registros_de_derechos_y_propiedad no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        registros = list(registros_de_derechos_y_propiedad.objects.filter(id=id).values())

        if len(registros) > 0:
            registros_de_derechos_y_propiedad.objects.filter(id=id).delete()
            data = {'message': "registros_de_derechos_y_propiedad eliminado"}
        else:
            data = {'message': "registros_de_derechos_y_propiedad no encontrado..."}
        return JsonResponse(data)


# clase control_de_documentos_del_contrato


class control_de_documentos_del_contrato_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            control = list(control_de_documentos_del_contrato.objects.filter(id=id).values())

            if len(control) > 0:
                data = {'message': "Cargado 1 control_de_documentos_del_contrato",
                        'control_de_documentos_del_contrato': control}
            else:
                data = {'message': "control_de_documentos_del_contrato no encontrado..."}
            return JsonResponse(data)
        else:
            control = list(control_de_documentos_del_contrato.objects.values())
            if len(control) > 0:
                data = {'message': "Todos los control_de_documentos_del_contrato cargado",
                        'control_de_documentos_del_contrato': control}
            else:
                data = {'message': "control_de_documentos_del_contrato no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        nombre_del_documento = jd['nombre_del_documento']
        fecha_de_entrega = jd['fecha_de_entrega']
        responsable = jd['responsable']

        control_de_documentos_del_contrato.objects.create(nombre_del_documento=nombre_del_documento,
                                                          fecha_de_entrega=fecha_de_entrega, responsable=responsable)
        data = {'message': "control_de_documentos_del_contrato creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        controles = list(control_de_documentos_del_contrato.objects.filter(id=id).values())

        if len(controles) > 0:
            control_de_documentos_del_contrato_aux = control_de_documentos_del_contrato.objects.get(id=id)
            control_de_documentos_del_contrato_aux.nombre_del_documento = jd['nombre_del_documento']
            control_de_documentos_del_contrato_aux.fecha_de_entrega = jd['fecha_de_entrega']
            control_de_documentos_del_contrato_aux.responsable = jd['responsable']

            control_de_documentos_del_contrato_aux.save()
            data = {'message': "control_de_documentos_del_contrato actualizado"}
        else:
            data = {'message': "control_de_documentos_del_contrato no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        controles = list(control_de_documentos_del_contrato.objects.filter(id=id).values())

        if len(controles) > 0:
            control_de_documentos_del_contrato.objects.filter(id=id).delete()
            data = {'message': "control_de_documentos_del_contrato eliminado"}
        else:
            data = {'message': "control_de_documentos_del_contrato no encontrado..."}
        return JsonResponse(data)


# clase consideraciones_para_la_ficha_tecnica


class consideraciones_para_la_ficha_tecnica_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            consideraciones = list(consideraciones_para_la_ficha_tecnica.objects.filter(id=id).values())

            if len(consideraciones) > 0:
                data = {'message': "Cargado 1 consideraciones_para_la_ficha_tecnica",
                        'consideraciones_para_la_ficha_tecnica': consideraciones}
            else:
                data = {'message': "consideraciones_para_la_ficha_tecnica no encontrado..."}
            return JsonResponse(data)
        else:
            consideraciones = list(consideraciones_para_la_ficha_tecnica.objects.values())
            if len(consideraciones) > 0:
                data = {'message': "Todos los consideraciones_para_la_ficha_tecnica cargado",
                        'consideraciones_para_la_ficha_tecnica': consideraciones}
            else:
                data = {'message': "consideraciones_para_la_ficha_tecnica no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        descripcion = jd['descripcion']

        consideraciones_para_la_ficha_tecnica.objects.create(descripcion=descripcion)
        data = {'message': "consideraciones_para_la_ficha_tecnica creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        consideraciones = list(consideraciones_para_la_ficha_tecnica.objects.filter(id=id).values())

        if len(consideraciones) > 0:
            consideraciones_para_la_ficha_tecnica_aux = consideraciones_para_la_ficha_tecnica.objects.get(id=id)
            consideraciones_para_la_ficha_tecnica_aux.descripcion = jd['descripcion']

            consideraciones_para_la_ficha_tecnica_aux.save()
            data = {'message': "consideraciones_para_la_ficha_tecnica actualizado"}
        else:
            data = {'message': "consideraciones_para_la_ficha_tecnica no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        consideraciones = list(consideraciones_para_la_ficha_tecnica.objects.filter(id=id).values())

        if len(consideraciones) > 0:
            consideraciones_para_la_ficha_tecnica.objects.filter(id=id).delete()
            data = {'message': "consideraciones_para_la_ficha_tecnica eliminado"}
        else:
            data = {'message': "consideraciones_para_la_ficha_tecnica no encontrado..."}
        return JsonResponse(data)


# clase valor_del_contrato_por_los_servicios_comercializados


class valor_del_contrato_por_los_servicios_comercializados_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los roles, si id!=0 entonces va a devolver el rol cuyo id es igual al valor
    def get(self, request, id=0):
        if id > 0:
            valor = list(valor_del_contrato_por_los_servicios_comercializados.objects.filter(id=id).values())

            if len(valor) > 0:
                data = {'message': "Cargado 1 valor_del_contrato_por_los_servicios_comercializados",
                        'valor_del_contrato_por_los_servicios_comercializados': valor}
            else:
                data = {'message': "valor_del_contrato_por_los_servicios_comercializados no encontrado..."}
            return JsonResponse(data)
        else:
            valor = list(valor_del_contrato_por_los_servicios_comercializados.objects.values())
            if len(valor) > 0:
                data = {'message': "Todos los valor_del_contrato_por_los_servicios_comercializados cargado",
                        'valor_del_contrato_por_los_servicios_comercializados': valor}
            else:
                data = {'message': "valor_del_contrato_por_los_servicios_comercializados no encontrados..."}
            return JsonResponse(data)

    def post(self, request):

        jd = json.loads(request.body)
        valor = jd['valor']
        moneda = jd['moneda']

        valor_del_contrato_por_los_servicios_comercializados.objects.create(valor=valor, moneda=moneda)
        data = {'message': "valor_del_contrato_por_los_servicios_comercializados creado"}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        valor = list(valor_del_contrato_por_los_servicios_comercializados.objects.filter(id=id).values())

        if len(valor) > 0:
            valor_del_contrato_por_los_servicios_comercializados_aux = valor_del_contrato_por_los_servicios_comercializados.objects.get(
                id=id)
            valor_del_contrato_por_los_servicios_comercializados_aux.valor = jd['valor']
            valor_del_contrato_por_los_servicios_comercializados_aux.moneda = jd['moneda']

            valor_del_contrato_por_los_servicios_comercializados_aux.save()
            data = {'message': "valor_del_contrato_por_los_servicios_comercializados actualizado"}
        else:
            data = {'message': "valor_del_contrato_por_los_servicios_comercializados no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        valor = list(valor_del_contrato_por_los_servicios_comercializados.objects.filter(id=id).values())

        if len(valor) > 0:
            valor_del_contrato_por_los_servicios_comercializados.objects.filter(id=id).delete()
            data = {'message': "valor_del_contrato_por_los_servicios_comercializados eliminado"}
        else:
            data = {'message': "valor_del_contrato_por_los_servicios_comercializados no encontrado..."}
        return JsonResponse(data)


# clase ficha_tecnica

class ficha_tecnica_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los contrato, si id!=0 entonces va a devolver el contrato cuyo id es igual al valor

    def get(self, request, id=0):
        if id > 0:
            ficha = list(ficha_tecnica.objects.filter(id=id).all())
            ficha_tecnica_json = serializers.serialize('json', ficha)

            if len(ficha) > 0:
                data = {'message': "Cargada 1 ficha_tecnica", 'ficha_tecnica': ficha_tecnica_json}
            else:
                data = {'message': "ficha_tecnica no encontrado..."}
            return JsonResponse(data)
        else:
            ficha = ficha_tecnica.objects.all()
            ficha_tecnica_json = serializers.serialize('json', ficha)

            if len(ficha) > 0:
                data = {'message': "Todos los ficha_tecnica cargados", 'ficha_tecnica': ficha_tecnica_json}
            else:
                data = {'message': "ficha_tecnica no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        # id_area = data.get('id')
        descripcion = data.get('descripcion')
        fecha = data.get('fecha')
        cliente = data.get('cliente')
        objeto = data.get('objeto')
        vigencia = data.get('vigencia')
        objetivos_especificos = data.get('objetivos_especificos')
        informacion_a_entregar_por_el_cliente = data.get('informacion_a_entregar_por_el_cliente')
        id_area_ejecutora_principal = data.get('id_area_ejecutora_principal')

        id_cronograma = data.get('id_cronograma')
        coordinador_del_contrato_por_la_cujae = data.get('coordinador_del_contrato_por_la_cujae')
        cargo_del_cliente = data.get('cargo_del_cliente')
        id_valor_del_contrato_por_los_servicios_comercializados = data.get(
            'id_valor_del_contrato_por_los_servicios_comercializados')
        firmado_por_responsable_del_contrato_de_ceta = data.get('firmado_por_responsable_del_contrato_de_ceta')

        lista_tareas_detalladas = data.get('lista_tareas_detalladas')
        lista_recurso_necesarios = data.get('lista_recurso_necesarios')

        lista_de_productos_extras_para_el_contrato = data.get('lista_de_productos_extras_para_el_contrato')
        lista_area_participante = data.get('lista_area_participante')

        lista_resultados_de_tareas = data.get('lista_resultados_de_tareas')
        lista_resultados_obtenidos_para_ficha_tecnica = data.get('lista_resultados_obtenidos_para_ficha_tecnica')

        lista_areas_y_trabajdores_para_la_ficha_tecnica = data.get('lista_areas_y_trabajdores_para_la_ficha_tecnica')
        lista_tiempo_dedicado_en_horas_mensuales = data.get('lista_tiempo_dedicado_en_horas_mensuales')
        lista_pagos_al_cliente = data.get('lista_pagos_al_cliente')
        lista_facturacion_pagos = data.get('lista_facturacion_pagos')
        lista_registros_de_derechos_y_propiedad = data.get('lista_registros_de_derechos_y_propiedad')

        lista_control_de_documentos_del_contrato = data.get('lista_control_de_documentos_del_contrato')
        lista_consideraciones_para_la_ficha_tecnica = data.get('lista_consideraciones_para_la_ficha_tecnica')

        cronograma_para_ficha_tecnica_obj = cronograma_para_ficha_tecnica.objects.get(id=id_cronograma)
        valor_del_contrato_por_los_servicios_comercializados_obj = valor_del_contrato_por_los_servicios_comercializados.objects.get(
            id=id_valor_del_contrato_por_los_servicios_comercializados)

        # Crear un nuevo objeto
        ficha_tecnica_nuevo = ficha_tecnica(
            descripcion=descripcion,
            fecha=fecha,
            cliente=cliente,
            objeto=objeto,
            vigencia=vigencia,
            objetivos_especificos=objetivos_especificos,
            informacion_a_entregar_por_el_cliente=informacion_a_entregar_por_el_cliente,
            id_area_ejecutora_principal=id_area_ejecutora_principal,
            id_cronograma=cronograma_para_ficha_tecnica_obj,
            coordinador_del_contrato_por_la_cujae=coordinador_del_contrato_por_la_cujae,
            cargo_del_cliente=cargo_del_cliente,
            id_valor_del_contrato_por_los_servicios_comercializados=valor_del_contrato_por_los_servicios_comercializados_obj,
            firmado_por_responsable_del_contrato_de_ceta=firmado_por_responsable_del_contrato_de_ceta,
        )

        # Guardar el objeto en la base de datos
        ficha_tecnica_nuevo.save()

        # Asignar las tareas detalladas
        for id in lista_tareas_detalladas:
            try:
                tareas_detalladas_obj = tareas_detalladas.objects.get(id=id)
                ficha_tecnica_nuevo.lista_tareas_detalladas.add(tareas_detalladas_obj)
            except tareas_detalladas.DoesNotExist:
                pass

        # Asignar lista_recurso_necesarios
        for id in lista_recurso_necesarios:
            try:
                recurso_necesarios_obj = recursos_necesarios.objects.get(id=id)
                ficha_tecnica_nuevo.lista_recurso_necesarios.add(recurso_necesarios_obj)
            except recursos_necesarios.DoesNotExist:
                pass

        # Asignar las productos_necesarios
        for id in lista_de_productos_extras_para_el_contrato:
            try:
                productos_necesarios_obj = productos_necesarios.objects.get(id=id)
                ficha_tecnica_nuevo.lista_de_productos_extras_para_el_contrato.add(productos_necesarios_obj)
            except productos_necesarios.DoesNotExist:
                pass

        # Asignar areas_participantes
        for id in lista_area_participante:
            try:
                areas_participantes_obj = area_participante.objects.get(id=id)
                ficha_tecnica_nuevo.lista_area_participante.add(areas_participantes_obj)
            except area_participante.DoesNotExist:
                pass

        # Asignar las resultados_para_ficha_tecnica
        for id in lista_resultados_de_tareas:
            try:
                resultados_para_ficha_tecnica_obj = resultados_para_ficha_tecnica.objects.get(id=id)
                ficha_tecnica_nuevo.lista_resultados_de_tareas.add(resultados_para_ficha_tecnica_obj)
            except resultados_para_ficha_tecnica.DoesNotExist:
                pass

        # Asignar resultados_obtenidos_para_ficha_tecnica
        for id in lista_resultados_obtenidos_para_ficha_tecnica:
            try:
                resultados_obtenidos_para_ficha_tecnica_obj = resultados_obtenidos_para_ficha_tecnica.objects.get(id=id)
                ficha_tecnica_nuevo.lista_resultados_obtenidos_para_ficha_tecnica.add(
                    resultados_obtenidos_para_ficha_tecnica_obj)
            except resultados_obtenidos_para_ficha_tecnica.DoesNotExist:
                pass



            # Asignar tiempo_dedicado_en_horas_mensuales
        for id in lista_tiempo_dedicado_en_horas_mensuales:
            try:
                tiempo_dedicado_en_horas_mensuales_obj = tiempo_dedicado_en_horas_mensuales.objects.get(id=id)
                ficha_tecnica_nuevo.lista_tiempo_dedicado_en_horas_mensuales.add(
                    tiempo_dedicado_en_horas_mensuales_obj)
            except tiempo_dedicado_en_horas_mensuales.DoesNotExist:
                pass

            # Asignar las pagos_al_cliente
        for id in lista_pagos_al_cliente:
            try:
                pagos_al_cliente_obj = pagos_al_cliente.objects.get(id=id)
                ficha_tecnica_nuevo.lista_pagos_al_cliente.add(pagos_al_cliente_obj)
            except pagos_al_cliente.DoesNotExist:
                pass

            # Asignar facturacion_pagos
        for id in lista_facturacion_pagos:
            try:
                facturacion_pagos_obj = facturacion_pagos.objects.get(id=id)
                ficha_tecnica_nuevo.lista_facturacion_pagos.add(
                    facturacion_pagos_obj)
            except facturacion_pagos.DoesNotExist:
                pass

            # Asignar las registros_de_derechos_y_propiedad
        for id in lista_registros_de_derechos_y_propiedad:
            try:
                registros_de_derechos_y_propiedad_obj = registros_de_derechos_y_propiedad.objects.get(id=id)
                ficha_tecnica_nuevo.lista_registros_de_derechos_y_propiedad.add(registros_de_derechos_y_propiedad_obj)
            except registros_de_derechos_y_propiedad.DoesNotExist:
                pass

            # Asignar control_de_documentos_del_contrato
        for id in lista_control_de_documentos_del_contrato:
            try:
                control_de_documentos_del_contrato_obj = control_de_documentos_del_contrato.objects.get(id=id)
                ficha_tecnica_nuevo.lista_control_de_documentos_del_contrato.add(
                    control_de_documentos_del_contrato_obj)
            except control_de_documentos_del_contrato.DoesNotExist:
                pass

            # Asignar consideraciones_para_la_ficha_tecnica
        for id in lista_consideraciones_para_la_ficha_tecnica:
            try:
                consideraciones_para_la_ficha_tecnica_obj = consideraciones_para_la_ficha_tecnica.objects.get(id=id)
                ficha_tecnica_nuevo.lista_consideraciones_para_la_ficha_tecnica.add(
                    consideraciones_para_la_ficha_tecnica_obj)
            except consideraciones_para_la_ficha_tecnica.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Ficha tecnica creado exitosamente'
        }
        return JsonResponse(response_data)

    def put(self, request, id):

        jd = json.loads(request.body)
        ficha_tecnica_nueva = list(ficha_tecnica.objects.filter(id=id).values())

        lista_tareas_detalladas = jd['lista_tareas_detalladas']
        lista_recurso_necesarios = jd['lista_recurso_necesarios']
        lista_de_productos_extras_para_el_contrato = jd['lista_de_productos_extras_para_el_contrato']
        lista_area_participante = jd['lista_area_participante']
        lista_resultados_de_tareas = jd['lista_resultados_de_tareas']
        lista_resultados_obtenidos_para_ficha_tecnica = jd['lista_resultados_obtenidos_para_ficha_tecnica']
        lista_areas_y_trabajdores_para_la_ficha_tecnica = jd['lista_areas_y_trabajdores_para_la_ficha_tecnica']
        lista_tiempo_dedicado_en_horas_mensuales = jd['lista_tiempo_dedicado_en_horas_mensuales']
        lista_pagos_al_cliente = jd['lista_pagos_al_cliente']
        lista_facturacion_pagos = jd['lista_facturacion_pagos']
        lista_registros_de_derechos_y_propiedad = jd['lista_registros_de_derechos_y_propiedad']
        lista_control_de_documentos_del_contrato = jd['lista_control_de_documentos_del_contrato']
        lista_consideraciones_para_la_ficha_tecnica = jd['lista_consideraciones_para_la_ficha_tecnica']

        id_cronograma = jd.get('id_cronograma')
        id_valor_del_contrato_por_los_servicios_comercializados = jd.get(
            'id_valor_del_contrato_por_los_servicios_comercializados')

        cronograma_obj = cronograma_para_ficha_tecnica.objects.get(id=id_cronograma)
        valor_del_contrato_por_los_servicios_comercializados_obj = valor_del_contrato_por_los_servicios_comercializados.objects.get(
            id=id_valor_del_contrato_por_los_servicios_comercializados)

        if len(ficha_tecnica_nueva) > 0:
            ficha_tecnica_aux = ficha_tecnica.objects.get(id=id)
            ficha_tecnica_aux.descripcion = jd['descripcion']
            ficha_tecnica_aux.fecha = jd['fecha']
            ficha_tecnica_aux.cliente = jd['cliente']
            ficha_tecnica_aux.objeto = jd['objeto']
            ficha_tecnica_aux.vigencia = jd['vigencia']
            ficha_tecnica_aux.objetivos_especificos = jd['objetivos_especificos']
            ficha_tecnica_aux.informacion_a_entregar_por_el_cliente = jd['informacion_a_entregar_por_el_cliente']
            ficha_tecnica_aux.coordinador_del_contrato_por_la_cujae = jd['coordinador_del_contrato_por_la_cujae']
            ficha_tecnica_aux.cargo_del_cliente = jd['cargo_del_cliente']
            ficha_tecnica_aux.firmado_por_responsable_del_contrato_de_ceta = jd[
                'firmado_por_responsable_del_contrato_de_ceta']

            # contrato_aux.id_servicio = jd['id_servicio']
            ficha_tecnica_aux.id_cronograma = cronograma_obj
            ficha_tecnica_aux.id_valor_del_contrato_por_los_servicios_comercializados = valor_del_contrato_por_los_servicios_comercializados_obj

            # Asignar las tareas detalladas
            for id in lista_tareas_detalladas:
                try:
                    tareas_detalladas_obj = tareas_detalladas.objects.get(id=id)
                    ficha_tecnica_aux.lista_tareas_detalladas.add(tareas_detalladas_obj)
                except tareas_detalladas.DoesNotExist:
                    pass

            # Asignar lista_recurso_necesarios
            for id in lista_recurso_necesarios:
                try:
                    recurso_necesarios_obj = recursos_necesarios.objects.get(id=id)
                    ficha_tecnica_aux.lista_recurso_necesarios.add(recurso_necesarios_obj)
                except recursos_necesarios.DoesNotExist:
                    pass

            # Asignar las productos_necesarios
            for id in lista_de_productos_extras_para_el_contrato:
                try:
                    productos_necesarios_obj = productos_necesarios.objects.get(id=id)
                    ficha_tecnica_aux.lista_de_productos_extras_para_el_contrato.add(productos_necesarios_obj)
                except productos_necesarios.DoesNotExist:
                    pass

            # Asignar areas_participantes
            for id in lista_area_participante:
                try:
                    areas_participantes_obj = area_participante.objects.get(id=id)
                    ficha_tecnica_aux.lista_area_participante.add(areas_participantes_obj)
                except area_participante.DoesNotExist:
                    pass

            # Asignar las resultados_para_ficha_tecnica
            for id in lista_resultados_de_tareas:
                try:
                    resultados_para_ficha_tecnica_obj = resultados_para_ficha_tecnica.objects.get(id=id)
                    ficha_tecnica_aux.lista_resultados_de_tareas.add(resultados_para_ficha_tecnica_obj)
                except resultados_para_ficha_tecnica.DoesNotExist:
                    pass

            # Asignar resultados_obtenidos_para_ficha_tecnica
            for id in lista_resultados_obtenidos_para_ficha_tecnica:
                try:
                    resultados_obtenidos_para_ficha_tecnica_obj = resultados_obtenidos_para_ficha_tecnica.objects.get(
                        id=id)
                    ficha_tecnica_aux.lista_resultados_obtenidos_para_ficha_tecnica.add(
                        resultados_obtenidos_para_ficha_tecnica_obj)
                except resultados_obtenidos_para_ficha_tecnica.DoesNotExist:
                    pass



                # Asignar tiempo_dedicado_en_horas_mensuales
            for id in lista_tiempo_dedicado_en_horas_mensuales:
                try:
                    tiempo_dedicado_en_horas_mensuales_obj = tiempo_dedicado_en_horas_mensuales.objects.get(id=id)
                    ficha_tecnica_aux.lista_tiempo_dedicado_en_horas_mensuales.add(
                        tiempo_dedicado_en_horas_mensuales_obj)
                except tiempo_dedicado_en_horas_mensuales.DoesNotExist:
                    pass

                # Asignar las pagos_al_cliente
            for id in lista_pagos_al_cliente:
                try:
                    pagos_al_cliente_obj = pagos_al_cliente.objects.get(id=id)
                    ficha_tecnica_aux.lista_pagos_al_cliente.add(pagos_al_cliente_obj)
                except pagos_al_cliente.DoesNotExist:
                    pass

                # Asignar facturacion_pagos
            for id in lista_facturacion_pagos:
                try:
                    facturacion_pagos_obj = facturacion_pagos.objects.get(id=id)
                    ficha_tecnica_aux.lista_facturacion_pagos.add(
                        facturacion_pagos_obj)
                except facturacion_pagos.DoesNotExist:
                    pass

                # Asignar las registros_de_derechos_y_propiedad
            for id in lista_registros_de_derechos_y_propiedad:
                try:
                    registros_de_derechos_y_propiedad_obj = registros_de_derechos_y_propiedad.objects.get(id=id)
                    ficha_tecnica_aux.lista_registros_de_derechos_y_propiedad.add(
                        registros_de_derechos_y_propiedad_obj)
                except registros_de_derechos_y_propiedad.DoesNotExist:
                    pass

                # Asignar control_de_documentos_del_contrato
            for id in lista_control_de_documentos_del_contrato:
                try:
                    control_de_documentos_del_contrato_obj = control_de_documentos_del_contrato.objects.get(id=id)
                    ficha_tecnica_aux.lista_control_de_documentos_del_contrato.add(
                        control_de_documentos_del_contrato_obj)
                except control_de_documentos_del_contrato.DoesNotExist:
                    pass

                # Asignar consideraciones_para_la_ficha_tecnica
            for id in lista_consideraciones_para_la_ficha_tecnica:
                try:
                    consideraciones_para_la_ficha_tecnica_obj = consideraciones_para_la_ficha_tecnica.objects.get(id=id)
                    ficha_tecnica_aux.lista_consideraciones_para_la_ficha_tecnica.add(
                        consideraciones_para_la_ficha_tecnica_obj)
                except consideraciones_para_la_ficha_tecnica.DoesNotExist:
                    pass

            ficha_tecnica_aux.save()
            data = {'message': "Ficha tecnica actualizado"}
        else:
            data = {'message': "Ficha tecnica no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        ficha = list(ficha_tecnica.objects.filter(id=id).values())

        if len(ficha) > 0:
            ficha_tecnica.objects.filter(id=id).delete()
            data = {'message': "ficha_tecnica eliminado"}
        else:
            data = {'message': "ficha_tecnica no encontrado"}
        return JsonResponse(data)
