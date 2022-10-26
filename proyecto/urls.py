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
from coder.views import AgregarConsulta, BuscarConsulta, ListarConsultas, AgregarFuncionarios, BuscarFuncionario, BuscarPaciente, ListarPacientes, AgregarPacientes, ListarFuncionarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', ListarPacientes.as_view()),
    path('pacientes/agregar', AgregarPacientes.as_view()),
    path('pacientes/buscar', BuscarPaciente.as_view()),
    path('funcionarios/', ListarFuncionarios.as_view()),
    path('funcionarios/agregar', AgregarFuncionarios.as_view()),
    path('funcionarios/buscar', BuscarFuncionario.as_view()),
    path('consultas/', ListarConsultas.as_view()),
    path('consultas/agregar', AgregarConsulta.as_view()),
    path('consultas/buscar', BuscarConsulta.as_view()),
]
