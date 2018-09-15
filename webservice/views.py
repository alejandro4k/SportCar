from django.shortcuts import render
from home.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.

class auto_viewset(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = auto_serializer

class marca_viewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = categoria_serializer

class concesionario_viewset(viewsets.ModelViewSet):
    queryset = Concesionario.objects.all()
    serializer_class = concesionario_serializer

class combustible_viewset(viewsets.ModelViewSet):
    queryset = Combustible.objects.all()
    serializer_class = combustible_serializer

class perfil_viewset(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = perfil_serializer
    
