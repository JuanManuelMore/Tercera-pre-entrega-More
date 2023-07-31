from django.db import models
from django.utils import timezone


# Create your models here.
class Desarrolladores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    especialidades = models.TextField(default=None)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Propuestas(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion= models.TextField(default=None)
    fechaSolicitud = models.DateField(default=timezone.now)


