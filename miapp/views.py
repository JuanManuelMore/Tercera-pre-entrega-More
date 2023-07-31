from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView



def index(request):
    return render(request, "miapp/base.html")

def clientes(request):
    return render(request, "miapp/clientes.html")

def desarrolladores(request):
    return render(request, "miapp/desarrolladores.html")

def propuestas(request):
    ctx={"propuestas": Propuestas.objects.all()}
    return render(request, "miapp/propuestas.html",ctx)

def propuestasForm(request):
    if request.method == "POST": 
       miForm = PropuestasForm(request.POST)
       if miForm.is_valid():
           titulo_p=miForm.cleaned_data.get('titulo')
           descripcion_p=miForm.cleaned_data.get('descripcion')
           fechaSolicitud_p=miForm.cleaned_data.get('fechaSolicitud')
           propuesta=Propuestas(titulo=titulo_p, descripcion=descripcion_p,fechaSolicitud=fechaSolicitud_p)
           propuesta.save()
           return render(request, "miapp/base.html")
    else:
      miForm = PropuestasForm()
    return render(request,"miapp/propuestasForm.html", {"form":miForm})

def desarrolladoresForm(request):
    if request.method == "POST": 
       miForm = DesarrolladoresForm(request.POST)
       if miForm.is_valid():
           nombre_d=miForm.cleaned_data.get('nombre')
           apellido_d=miForm.cleaned_data.get('apellido')
           email_d=miForm.cleaned_data.get('email')
           especialidades_d=miForm.cleaned_data.get('especialidades')
           desarrollador=Desarrolladores(nombre=nombre_d, apellido=apellido_d,email=email_d,especialidades=especialidades_d)
           desarrollador.save()
           return render(request, "miapp/base.html")
    else:
      miForm = DesarrolladoresForm()
    return render(request,"miapp/desarrolladoresForm.html", {"form":miForm})

def clientesForm(request):
    if request.method == "POST": 
       miForm = ClientesForm(request.POST)
       if miForm.is_valid():
           nombre_c=miForm.cleaned_data.get('nombre')
           apellido_c=miForm.cleaned_data.get('apellido')
           email_c=miForm.cleaned_data.get('email')
           cliente=Clientes(nombre=nombre_c, apellido=apellido_c,email=email_c)
           cliente.save()
           return render(request, "miapp/base.html")
    else:
      miForm = ClientesForm()
    return render(request,"miapp/clientesForm.html", {"form":miForm})

def buscarPropuesta(request):
   return render(request,"miapp/buscarPropuesta.html")

def resultadosPropuesta(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        propuesta = Propuestas.objects.filter(titulo__icontains=titulo)
        return render(request, 
                      "miapp/resultadosPropuesta.html", 
                      {"titulo": titulo, "propuestas":propuesta})
    return HttpResponse("No se ingresaron datos a buscar!")
