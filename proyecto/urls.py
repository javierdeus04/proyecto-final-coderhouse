"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coder.views import (AgregarConsulta, BuscarConsulta, ListarConsultas, 
                        AgregarFuncionarios, BuscarFuncionario, BuscarPaciente, 
                        ListarPacientes, AgregarPacientes, ListarFuncionarios, PaginaPpal)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ppal/', PaginaPpal.as_view(), name='principal'),
    path('pacientes/', ListarPacientes.as_view(), name='pacientes-list'),
    path('pacientes/agregar', AgregarPacientes.as_view(), name='nuevo-paciente'),
    path('pacientes/buscar', BuscarPaciente.as_view(), name='buscar-paciente'),
    path('funcionarios/', ListarFuncionarios.as_view(), name='funcionarios-list'),
    path('funcionarios/agregar', AgregarFuncionarios.as_view(), name='nuevo-funcionario'),
    path('funcionarios/buscar', BuscarFuncionario.as_view(), name='buscar-funcionario'),
    path('consultas/', ListarConsultas.as_view(), name='conultas-list'),
    path('consultas/agregar', AgregarConsulta.as_view(), name='agregar-consulta'),
    path('consultas/buscar', BuscarConsulta.as_view(), name='buscar-consulta'),
]
