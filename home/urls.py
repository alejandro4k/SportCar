from django.urls import path
from .views import *


urlpatterns =[
    path("", vista_inicio , name='vista_inicio'),
    path ('contacto/',vista_contacto),
    path('lista_auto/', vista_lista_auto ,  name='vista_lista_auto'),
    path('lista_marca/', vista_lista_marca, name='vista_lista_marca'),
    path('lista_concesionario/', vista_lista_concesionario, name='vista_lista_concesionario'),
    path('agregar_auto/', vista_agregar_auto, name = 'vista_agregar_auto'),
    path('agregar_marca/', vista_agregar_marca, name = 'vista_agregar_marca'),
    path('agregar_concesionario/', vista_agregar_concesionario, name= 'vista_agregar_concesionario'),
    path('ver_auto/<int:id_auto>/', vista_ver_auto, name = 'ver_auto' ),
    path('ver_concesionario/<int:id_concesionario>/', vista_ver_concesionario, name = 'vista_ver_concesionario'),
    path('ver_marca/<int:id_marca>/', vista_ver_marca, name = 'ver_marca'),
    path('editar_auto/<int:id_auto>/', vista_editar_auto, name = 'vista_editar_auto'),
    path('editar_marca/<int:id_marca>/', vista_editar_marca, name = 'vista_editar_marca'),
     path('editar_concesionario/<int:id_concesionario>/', vista_editar_concesionario, name = 'vista_editar_concesionario'),
    path('eliminar_auto/<int:id_auto>/', vista_eliminar_auto, name = 'vista_eliminar_auto'),
    path('eliminar_marca/<int:id_marca>/', vista_eliminar_marca, name = 'vista_eliminar_marca'),
    path('eliminar_perfil/<int:id_perfil>/', vista_eliminar_perfil, name = 'vista_eliminar_perfil'),
    path('eliminar_concesionario/<int:id_concesionario>/', vista_eliminar_cocesionario, name = 'vista_eliminar_concesionario'),
    path('busqueda_marca/<str:marca_auto>/', vista_busqueda_marca, name = 'vista_busqueda_marca'),
    path('login/', vista_login, name='vita_login'),
    path('logout/', vista_logout, name='vista_logout'),
    path('register/', vista_register, name='vista_register'),
    path('vista_crear_perfil/', vista_crear_perfil, name='vista_crear_perfil'),
    path('lista_perfil/', lista_perfil, name='lista_perfil'),
    path('ws/auto/', ws_auto_vista, name='ws_auto_vista')

]