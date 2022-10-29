from pipes import Template
from urllib import request
from django.shortcuts import render
from django.views import View
from django.views.defaults import page_not_found, server_error
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from coder.models import Paciente

def index(request):    
    return render(request, 'coder/index.html')
def mi_error_404(request, exception=None):
    return render(request, '404.html')
def mi_error_500(request):
    return render(request, '500.html')
def mi_charts(request):
    return render(request, 'coder/charts.html')
def mi_layout_sidenav_ligth(request):
    return render(request, 'coder/layout-sidenav-light.html')
def mi_layout_static(request):
    return render(request, 'coder/layout-static.html')
def mi_login(request):
    return render(request, 'coder/login.html')
def mi_recovery_password(request):
    return render(request, 'coder/password.html')

class NuevoPaciente(CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'numero_ci', 'numero_cel', 'motivo_consulta']
    success_url = 'coder/litsa-pacientes.html'

class PacientesList(ListView):
    model = Paciente

class PacienteDetalle(DetailView):
    model = Paciente


