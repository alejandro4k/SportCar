from django.urls import path, include
from rest_framework import routers
from home.models import *
from webservice.views import *

router = routers.DefaultRouter()
router.register(r'auto', auto_viewset)
router.register(r'marca', marca_viewset)
router.register(r'categoria', categoria_viewset)
router.register(r'concesionario', concesionario_viewset)
router.register(r'combustible', combustible_viewset)
router.register(r'perfil', perfil_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
