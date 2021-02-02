import datetime

from rest_framework import status, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from JolgorioWebApp.models import Actividad, Usuario, Logro, Material, UsuarioHasActividad
from JolgorioWebApp.serializers import ActividadSerializer, UsuarioSerializer, LogroSerializer, MaterialSerializer

@api_view(['GET'])
def listar_actividades(request):
    if request.method == 'GET':
        actividades = Actividad.objects.filter(estado=1).order_by('tipo')
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listar_materiales(request, id):
    if request.method == 'GET':
        materiales = Material.objects.filter(actividadhasmaterial__actividad_idactividad=id)
        serializer = MaterialSerializer(materiales, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listar_actividades_completadas(request, id):
    if request.method == 'GET':
        actividades = Actividad.objects.filter(usuariohasactividad__usuario_idusuario=id)
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def listar_actividades_ultimo_mes(request, id):
    if request.method == 'GET':
        actividades = Actividad.objects.filter(usuariohasactividad__usuario_idusuario= id,
                                               usuariohasactividad__fechacompletado__month=datetime.date.today().month,
                                               usuariohasactividad__fechacompletado__year=datetime.date.today().year)
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def usuario_por_id(request, id):
    if request.method == 'GET':
        usuario = Usuario.objects.get(idusuario=id);
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)



@api_view(['GET'])
def usuario_por_telefono(request, numero):
    if request.method == 'GET':
        usuario = Usuario.objects.get(numero=numero);
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def usuario_por_correo(request, correo):
    if request.method == 'GET':
        usuario = Usuario.objects.get(email=correo);
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def listar_logros(request, tipo):
    if request.method == 'GET':
       logros = Logro.objects.filter(tipo=tipo)
       serializer = LogroSerializer(logros, many=True)
       return Response(serializer.data)

@api_view(['POST'])
def actividad_completada(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        idusuario = json_data["idusuario"]
        idactividad = json_data["idactividad"]
        fecha = datetime.date.today()
        query = UsuarioHasActividad(idusuario, idactividad, fecha)
        query.save()
        response = {"status": "success"}
        return Response(response)

