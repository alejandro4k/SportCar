from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def vista_contacto(request):
    formulario = contacto_form()
    return render(request,'contacto.html', locals())

def vista_lista_auto(request):
    lista = Auto.objects.filter().order_by('-id')
    return render(request, 'lista_auto.html', locals())

def vista_lista_marca(request):
    listam =Marca.objects.filter()
    return render(request, 'lista_marca.html', locals())


    
def vista_lista_concesionario(request):
    listacon = Concesionario.objects.filter()
    return render(request, "lista_concesionario.html", locals())

def lista_perfil(request):
    listap = Perfil.objects.filter()
    return render(request,"lista_perfil.html", locals())

def vista_agregar_auto(request):
    if request.method == 'POST':
        formulario= agregar_autos_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit = False)
            prod.status = True
            prod.save()
            formulario.save()
        return redirect ('/lista_auto/')
    else: 
        formulario = agregar_autos_form()
    return render(request, 'vista_agregar_auto.html', locals())

def vista_agregar_marca(request):
    if request.method == 'POST':
        formulario = agregar_marcas_form(request.POST, request.FILES)
        if formulario.is_valid():
            marc = formulario.save(commit = False)
            marc.status = True
            marc.save()
            formulario.save()
        return redirect ('/lista_marca/')
    else:
        formulario = agregar_marcas_form()
    return render(request, 'vista_agregar_marca.html', locals())

def vista_agregar_concesionario(request):
    if request.method == 'POST':
        formulario = agregar_concesionario_form(request.POST, request.FILES)
        if formulario.is_valid():
            conc = formulario.save(commit = False)
            conc.status = True
            conc.save()
            formulario.save()
        return redirect('/lista_concesionario/')
    else:
        formulario = agregar_concesionario_form()
    return render(request, 'vista_agregar_concesionario.html', locals())

def vista_ver_auto(request, id_auto):
    p = Auto.objects.get(id = id_auto)
    return render (request,'ver_auto.html', locals())

def vista_ver_marca(request, id_marca):
    p = Marca.objects.get(id = id_marca)
    return render (request,"ver_marca.html", locals())

def vista_ver_concesionario(request, id_concesionario):
    p = Concesionario.objects.get(id = id_concesionario)
    return render (request,"ver_concesionario.html", locals())

def vista_editar_auto(request, id_auto):
    aut = Auto.objects.get(id = id_auto)
    if request.method =='POST':
        formulario = agregar_autos_form(request.POST, request.FILES, instance = aut)
        if formulario.is_valid():
            aut = formulario.save()
            return redirect('/lista_auto/')
    else:
        formulario = agregar_autos_form(instance = aut)
    return render(request, 'vista_agregar_auto.html', locals())

def vista_editar_marca(request, id_marca):
    marc = Marca.objects.get(id= id_marca)
    if request.method == 'POST':
        formulario = agregar_marcas_form(request.POST, request.FILES, instance = marc)
        if formulario.is_valid():
            marc = formulario.save()
            return redirect('/lista_marca/')
    else:
        formulario = agregar_marcas_form(instance = marc)
    return render(request, 'vista_agregar_marca.html', locals())

def vista_editar_concesionario(request, id_concesionario):
    conc = Concesionario.objects.get(id= id_concesionario)
    if request.method == 'POST':
        formulario = agregar_concesionario_form(request.POST, request.FILES, instance = conc)
        if formulario.is_valid():
            conc = formulario.save()
            return redirect('/lista_concesionario/')
    else:
        formulario = agregar_concesionario_form(instance = conc)
    return render(request, 'vista_agregar_concesionario.html', locals())

def vista_eliminar_auto(request, id_auto):
    aut = Auto.objects.get(id = id_auto)
    aut.delete()
    return redirect('/lista_auto/')

def vista_eliminar_perfil(request, id_perfil):
    perfil = Perfil.objects.get(id = id_perfil)
    u = User.objects.get(id = perfil.user.id)
    u.delete()
    return redirect('/lista_perfil')

def vista_eliminar_cocesionario(request, id_concesionario):
    conc = Concesionario.objects.get(id = id_concesionario)
    conc.delete()
    return redirect('/lista_concesionario/')

def vista_eliminar_marca(request, id_marca):
    marc = Marca.objects.get(id = id_marca)
    marc.delete()
    return redirect('/lista_marca')

def vista_login(request):
    usu=''
    cla=''
    if request.method =="POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                msj = "usuario o clave incorrectos"
    formulario = login_form()
    return render(request, 'login.html', locals())

def vista_logout(request):
    logout(request)
    return redirect('/login/')

def vista_inicio(request):
    listam = Marca.objects.filter()

    return render(request,"inicio.html", locals())

    


def vista_register (request):
    formulario = register_form()
    if request.method=='POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password_1 = formulario.cleaned_data['password_1']
            password_2 = formulario.cleaned_data['password_2']
            u =User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()
            return redirect ('/login/')
        else:
            return render(request, 'register.html', locals())
    return render(request, 'register.html', locals())

def vista_crear_perfil(request):
    form_1 = register_form()
    form_2 = perfil_form()
    if request.method=='POST':
        form_1 = register_form(request.POST)
        form_2 = perfil_form(request.POST, request.FILES)
        if form_1.is_valid() and form_2.is_valid():
            usuario = form_1.cleaned_data['username']
            correo = form_1.cleaned_data['email']
            password_1 = form_1.cleaned_data['password_1']
            password_2 = form_1.cleaned_data['password_2']
            u =User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()

            z = form_2.save(commit=False)
            z.user = u
            z.save()
            form_1 = register_form()
            form_2 = perfil_form()

    return render(request, 'perfil.html', locals())
'''
def vista_buscar_auto_marca(request,marca_auto):
    busqueda = Auto.objects.filter(marca = marca_auto)
    return render (request,"lista_marca_auto.html", locals())
'''
def vista_busqueda_marca(request, marca_auto):
    busqueda = Auto.objects.filter(marca__nombre__iexact = marca_auto)
    return render (request, 'lista_marca_auto.html', locals())    

    
