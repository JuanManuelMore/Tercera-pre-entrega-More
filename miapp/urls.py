from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name="inicio"),

    path('clientes/', clientes, name="clientes"),

    path('propuestas/', propuestas, name="propuestas"),

    path('desarrolladores/', desarrolladores, name="desarrolladores"),

    path('propuestas_form', propuestasForm, name="propuestas_form"),

    path('desarrolladores_form', desarrolladoresForm, name="desarrolladores_form"),

    path('clientes_form', clientesForm, name="clientes_Form"),

    path('buscar_propuesta/', buscarPropuesta, name="buscar_propuesta"),
    path('buscar_propuesta2/', resultadosPropuesta, name="buscar_propuesta2"),
]