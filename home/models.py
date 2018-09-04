from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length= 500)

    def __str__(self):
        return self.nombre


class Concesionario (models.Model):
    nombre = models.CharField( max_length = 100 )
    ciudad = models.CharField( max_length = 100)
    direccion = models.CharField( max_length = 100 )

    def __str__(self):
        return self.nombre
class Combustible (models.Model):
    tipo1 = (
        ("Diesel", "Diesel"),
        ("Gasolina","Gasolina")
    )
    tipo = models.CharField( max_length = 100, choices = tipo1 )

    def __str__(self):
        return self.tipo
        
class Marca (models.Model):
    nombre = models.CharField( max_length = 100)
    foto = models.ImageField(upload_to='marcas', null=True,blank=True)

    def __str__ (self):
        return self.nombre
class Auto (models.Model):
    nombre = models.CharField( max_length = 100 )
    modelo = models.IntegerField()
    status = models.BooleanField( default = True )
    stock = models.IntegerField()
    #categoria = models.ManyToManyField(Categoria, null = True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE)
    combustible = models.ForeignKey(Combustible, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='autos', null=True,blank=True, default='autos/defaul.jpg')
    
    #foto = models.ImageField()

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    nombre = models.CharField(max_length = 100)
    identificacion = models.CharField(max_length = 100)
    edad = models.CharField(max_length = 5)
    foto = models.ImageField(upload_to='perfiles', null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

