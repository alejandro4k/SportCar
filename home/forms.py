from django import forms
from .models import *
from django.contrib.auth.models import User

class contacto_form(forms.Form):
    nombre = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    cedula = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(widget = forms.TextInput(attrs={"class":"form-control"}))
    telefono = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}))
    ciudades = (
                ("CAL", "Cali"),
                ("Pop", "Popayán"),
                ("Bog", "Bogota"),
                ("Med", "Medellin"),
                )
    ciudad = forms.MultipleChoiceField(widget=forms.Select,choices=ciudades)
    autos = (
        ("R8", "Audi R8"),
        ("Mst", "Ford Mustang GTR"),
        ("ACA", "Honda Acura"),
        ("STG", "Kia Stinger"),
        ("PFMT", "Lamborgini Performante"),
    )
    auto = forms.MultipleChoiceField(widget=forms.Select,choices=autos)
    mensaje = forms.CharField(widget= forms.Textarea(attrs={"class":"form-control"}))
    check = (
        ("1", "Acepta Terminos y condiciones"),
        ("2","Recibir Notificaciones")
    )
    condiciones = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=check)

class agregar_autos_form(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

class agregar_marcas_form(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class agregar_concesionario_form(forms.ModelForm):
    class Meta:
        model = Concesionario
        fields = '__all__'

class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    clave = forms.CharField(widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control"}))

class register_form (forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control"}))
    password_2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput(render_value=False,attrs={"class":"form-control"}))
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya registrado')
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('correo electronico no existe')

    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2  = self.cleaned_data['password_2']

        if password_1==password_2:
            pass
        else:
            raise forms.ValidationError('Passwords no coinciden')

class perfil_form(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'identificacion', 'edad', 'foto', 'user']
        exclude =['user']
        widgets = {
            'nombre':forms.TextInput(attrs={"class":"form-control"}),
            'identificacion': forms.TextInput(attrs={"class":"form-control"}),
            'edad': forms.TextInput(attrs={"class":"form-control"}),
            'foto': forms.FileInput()
        
        }