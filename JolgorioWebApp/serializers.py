from rest_framework import serializers
from JolgorioWebApp.models import Usuario, Actividad, Logro, Material

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idusuario', 'nombre', 'apellido1', 'apellido2', 'iddistrito', 'email', 'fechanac', 'numero', 'sexo']


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['idactividad', 'tipo', 'titulo', 'descripcion', 'enlace', 'descripcion_tmp', 'estado']

class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro
        fields = ['idlogro', 'tipo', 'descripcion']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['idmaterial', 'nombre']


