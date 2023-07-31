from django import forms 
from django.utils import timezone

class PropuestasForm(forms.Form):
    titulo = forms.CharField(label="Título",max_length=50,required=True)
    descripcion= forms.CharField(label="Descripción",max_length=500,required=True)
    fechaSolicitud = forms.DateField(label="Fecha de la Solicitud", required=False)

class DesarrolladoresForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    apellido = forms.CharField(label="Apellido",max_length=50,required=True)
    email = forms.EmailField(label="Email")
    especialidades = forms.CharField(label="Especialidades",max_length=500,required=True)

class ClientesForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=50,required=True)
    apellido = forms.CharField(label="Apellido",max_length=50,required=True)
    email = forms.EmailField(label="Email")
