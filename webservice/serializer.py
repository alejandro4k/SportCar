from rest_framework import serializers
from home.models import *

class auto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ('url','nombre','modelo', 'status', 'stock', 'categoria','marca','concesionario','combustible', 'foto',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url','nombre','foto',)

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre', 'descripcion',)

class concesionario_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concesionario
        fields = ('url', 'nombre', 'ciudad', 'direccion',)

class combustible_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combustible
        fields = ('url','tipo')

class perfil_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ('url', 'nombre', 'nombre', 'identificacion', 'edad', 'foto', 'user',)