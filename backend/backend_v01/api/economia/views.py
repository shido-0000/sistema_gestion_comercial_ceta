from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from django.views.decorators.csrf import csrf_exempt
import json

from django.core import serializers
from api.economia.models import contrato, pagos_al_cliente, facturacion_pagos
from api.recursos_humanos.models import trabajador, programa_de_cobro
from api.servicios.models import servicio, area_participante, resultados_obtenidos_para_ficha_tecnica


# Create your views here.

# clase contrato

class contratos_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los contrato, si id!=0 entonces va a devolver el contrato cuyo id es igual al valor

    def get(self, request, id=0):
        if id > 0:
            contratos = list(contrato.objects.filter(codigo=id).all())
            contratos_json = serializers.serialize('json', contratos)

            if len(contratos) > 0:
                data = {'message': "Cargada 1 contrato", 'contrato': contratos_json}
            else:
                data = {'message': "Contrato no encontrado..."}
            return JsonResponse(data)
        else:
            contratos = contrato.objects.all()
            contratos_json = serializers.serialize('json', contratos)

            if len(contratos) > 0:
                data = {'message': "Todos los contratos cargados", 'contratos': contratos_json}
            else:
                data = {'message': "Contratos no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        # id_area = data.get('id')
        version = data.get('version')
        CES = data.get('CES')
        titulo = data.get('titulo')
        numero = data.get('numero')
        grupo_ejecutor_del_contrato = data.get('grupo_ejecutor_del_contrato')
        cliente = data.get('cliente')
        gestor = data.get('gestor')
        producto = data.get('producto')
        codigo = data.get('codigo')
        id_servicio = data.get('id_servicio')
        localizacion_del_cliente = data.get('localizacion_del_cliente')
        coordinador_del_contrato = data.get('coordinador_del_contrato')
        cantidad_de_participantes = data.get('cantidad_de_participantes')
        fecha_de_inicio = data.get('fecha_de_inicio')
        terminacion = data.get('terminacion')
        valor_del_contrato = data.get('valor_del_contrato')
        margen_comercial = data.get('margen_comercial')
        ingreso_bruto = data.get('ingreso_bruto')
        observaciones = data.get('observaciones')
        gastos_de_operacion_desde_CETA = data.get('gastos_de_operacion_desde_CETA')
        ingreso_neto_planificado = data.get('ingreso_neto_planificado')
        remuneracion = data.get('remuneracion')
        norma_maxima = data.get('norma_maxima')
        norma_asignada = data.get('norma_asignada')
        propuesto_por = data.get('propuesto_por')
        aprobado_por = data.get('aprobado_por')

        lista_programa_de_cobro = data.get('lista_programa_de_cobro')
        lista_area_participante = data.get('lista_area_participante')

        servicio_obj = servicio.objects.get(id=id_servicio)

        # Crear un nuevo objeto de contrato
        contrato_nuevo = contrato(
            version=version,
            CES=CES,
            titulo=titulo,
            numero=numero,
            grupo_ejecutor_del_contrato=grupo_ejecutor_del_contrato,
            cliente=cliente,
            gestor=gestor,
            producto=producto,
            codigo=codigo,
            id_servicio=servicio_obj,
            localizacion_del_cliente=localizacion_del_cliente,
            coordinador_del_contrato=coordinador_del_contrato,
            cantidad_de_participantes=cantidad_de_participantes,
            fecha_de_inicio=fecha_de_inicio,
            terminacion=terminacion,
            valor_del_contrato=valor_del_contrato,
            margen_comercial=margen_comercial,
            ingreso_bruto=ingreso_bruto,
            observaciones=observaciones,
            gastos_de_operacion_desde_CETA=gastos_de_operacion_desde_CETA,
            ingreso_neto_planificado=ingreso_neto_planificado,
            remuneracion=remuneracion,
            norma_maxima=norma_maxima,
            norma_asignada=norma_asignada,
            propuesto_por=propuesto_por,
            aprobado_por=aprobado_por
        )

        # Guardar el objeto en la base de datos
        contrato_nuevo.save()

        # Asignar los programas de cobro al contrato
        for id_programa in lista_programa_de_cobro:
            try:
                programa_de_cobro_obj = programa_de_cobro.objects.get(id=id_programa)
                contrato_nuevo.lista_programa_de_cobro.add(programa_de_cobro_obj)
            except trabajador.DoesNotExist:
                pass

        # Asignar las areas de participantes al contrato
        for id_area in lista_area_participante:
            try:
                areas_obj = area_participante.objects.get(id=id_area)
                contrato_nuevo.lista_area_participante.add(areas_obj)
            except area_participante.DoesNotExist:
                pass

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Contrato creado exitosamente'
        }
        return JsonResponse(response_data)

    def put(self, request, id):

        jd = json.loads(request.body)
        contratos = list(contrato.objects.filter(id=id).values())
        lista_areas = jd['lista_area_participante']
        lista_programas_de_cobro = jd['lista_programa_de_cobro']
        id_servicio = jd.get('id_servicio')
        # id_servicio = jd['id_servicio']

        servicio_obj = servicio.objects.get(id=id_servicio)

        if len(contratos) > 0:
            contrato_aux = contrato.objects.get(id=id)
            contrato_aux.version = jd['version']
            contrato_aux.CES = jd['CES']
            contrato_aux.titulo = jd['titulo']
            contrato_aux.numero = jd['numero']
            contrato_aux.grupo_ejecutor_del_contrato = jd['grupo_ejecutor_del_contrato']
            contrato_aux.cliente = jd['cliente']
            contrato_aux.gestor = jd['gestor']
            contrato_aux.producto = jd['producto']
            contrato_aux.codigo = jd['codigo']
            # contrato_aux.id_servicio = jd['id_servicio']
            contrato_aux.id_servicio = servicio_obj
            # contrato_aux.id_servicio = id_servicio
            contrato_aux.localizacion_del_cliente = jd['localizacion_del_cliente']
            contrato_aux.coordinador_del_contrato = jd['coordinador_del_contrato']
            contrato_aux.cantidad_de_participantes = jd['cantidad_de_participantes']
            contrato_aux.fecha_de_inicio = jd['fecha_de_inicio']
            contrato_aux.terminacion = jd['terminacion']
            contrato_aux.valor_del_contrato = jd['valor_del_contrato']
            contrato_aux.margen_comercial = jd['margen_comercial']
            contrato_aux.ingreso_bruto = jd['ingreso_bruto']
            contrato_aux.observaciones = jd['observaciones']
            contrato_aux.gastos_de_operacion_desde_CETA = jd['gastos_de_operacion_desde_CETA']
            contrato_aux.ingreso_neto_planificado = jd['ingreso_neto_planificado']
            contrato_aux.remuneracion = jd['remuneracion']
            contrato_aux.norma_maxima = jd['norma_maxima']
            contrato_aux.norma_asignada = jd['norma_asignada']
            contrato_aux.propuesto_por = jd['propuesto_por']
            contrato_aux.aprobado_por = jd['aprobado_por']

            for id_area in lista_areas:
                try:
                    area_aux = area_participante.objects.get(id=id_area)
                    contrato_aux.lista_area_participante.add(area_aux)
                except area_participante.DoesNotExist:
                    pass

            for id_programa_cobro in lista_programas_de_cobro:
                try:
                    programa_aux = programa_de_cobro.objects.get(id=id_programa_cobro)
                    contrato_aux.lista_programa_de_cobro.add(programa_aux)
                except programa_de_cobro.DoesNotExist:
                    pass

            contrato_aux.save()
            data = {'message': "Contrato actualizado"}
        else:
            data = {'message': "Contrato no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        contratos = list(contrato.objects.filter(id=id).values())

        if len(contratos) > 0:
            contrato.objects.filter(id=id).delete()
            data = {'message': "Contrato eliminado"}
        else:
            data = {'message': "Contrato no encontrado"}
        return JsonResponse(data)


# jonathan

# clase pagos_al_cliente


class pagos_al_cliente_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los area_participante, si id!=0 entonces va a devolver el area_participante cuyo id es igual al valor

    def get(self, request, id=0):

        if id > 0:
            pagos = list(pagos_al_cliente.objects.filter(id=id).all())
            pagos_json = serializers.serialize('json', pagos)

            if len(pagos) > 0:
                data = {'message': "Cargada 1 pago", 'pago': pagos_json}
            else:
                data = {'message': "Pago no encontrado..."}
            return JsonResponse(data)
        else:
            pagos = pagos_al_cliente.objects.all()
            pagos_json = serializers.serialize('json', pagos)

            if len(pagos) > 0:
                data = {'message': "Todas los pagos cargados", 'pago': pagos_json}
            else:
                data = {'message': "Pagos no encontradas..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        fecha = data['fecha']
        valor = data['valor']
        detalles = data['detalles']

        # Crear un nuevo objeto
        nueva_pago = pagos_al_cliente(fecha=fecha, valor=valor, detalles=detalles)

        # Guardar el objeto en la base de datos
        nueva_pago.save()

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Pago creado exitosamente'
        }
        return JsonResponse(response_data)

    # Arreglado
    def put(self, request, id):
        jd = json.loads(request.body)
        fecha = jd['fecha']
        valor = jd['valor']
        detalles = jd['detalles']

        pagos = list(pagos_al_cliente.objects.filter(id=id))

        if len(pagos) > 0:

            pagos_obj = pagos_al_cliente.objects.get(id=id)
            pagos_obj.fecha = fecha
            pagos_obj.valor = valor
            pagos_obj.detalles = detalles

            pagos_obj.save()
            data = {'message': "Pago actualizado"}
        else:
            data = {'message': "Pago no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):
        pagos = list(pagos_al_cliente.objects.filter(id=id).values())

        if len(pagos) > 0:
            pagos_al_cliente.objects.filter(id=id).delete()
            data = {'message': "Pago eliminado"}
        else:
            data = {'message': "Pago no encontrado"}
        return JsonResponse(data)


# facturacion de pagos

class facturacion_pagos_view(GenericAPIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los usuarios, si id!=0 entonces va a devolver el usuario cuyo id es igual al valor
    def get(self, request, id=0):

        if id > 0:
            facturacion = list(facturacion_pagos.objects.filter(id=id).values())

            if len(facturacion) > 0:
                data = {'message': "Cargado 1 facturacion pagos", 'facturacion_pagos': facturacion}
            else:
                data = {'message': "facturacion de pagos no encontrado..."}
            return JsonResponse(data)
        else:
            facturacion = list(facturacion_pagos.objects.values())

            if len(facturacion) > 0:
                data = {'message': "Todos las facturaciones cargados", 'facturacion_pagos': facturacion}
            else:
                data = {'message': "facturacion pagos no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        fecha = jd['fecha']
        valor = jd['valor']
        id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']


        try:
            resultados_obtenidos_para_ficha_tecnica_obj = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)  # Obtener una instancia válida del modelo rol
            # Cifrar la contraseña antes de guardarla

            facturacion_pagos.objects.create(fecha=fecha, valor=valor,
                                                                   id_resultados_obtenidos_para_ficha_tecnica=resultados_obtenidos_para_ficha_tecnica_obj)
            data = {'message': "Facturacion creado"}
        except resultados_obtenidos_para_ficha_tecnica.DoesNotExist:
            data = {'message': "Los resultados_obtenidos_para_ficha_tecnica especificado no existe"}

        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        facturacion = list(facturacion_pagos.objects.filter(id=id).values())

        if len(facturacion) > 0:
            facturacion_pagos_aux = facturacion_pagos.objects.get(id=id)
            facturacion_pagos_aux.fecha = jd['fecha']
            facturacion_pagos_aux.valor = jd['valor']

            # Obtener la instancia de resultados_obtenidos_para_ficha_tecnica basada en el ID
            id_resultados_obtenidos_para_ficha_tecnica = jd['id_resultados_obtenidos_para_ficha_tecnica']
            resultados_obtenidos_para_ficha_tecnica_instancia = resultados_obtenidos_para_ficha_tecnica.objects.get(
                id=id_resultados_obtenidos_para_ficha_tecnica)

            # Asignar la instancia del rol
            facturacion_pagos_aux.id_resultados_obtenidos_para_ficha_tecnica = resultados_obtenidos_para_ficha_tecnica_instancia

            facturacion_pagos_aux.save()
            data = {'message': "facturacion_pagos actualizado"}
        else:
            data = {'message': "Usuario no encontrado..."}
        return JsonResponse(data)

    def delete(self, request, id):

        facturacion = list(facturacion_pagos.objects.filter(id=id).values())

        if len(facturacion) > 0:
            facturacion_pagos.objects.filter(id=id).delete()
            data = {'message': "facturacion_pagos eliminado"}
        else:
            data = {'message': "facturacion_pagos no encontrado..."}
        return JsonResponse(data)
