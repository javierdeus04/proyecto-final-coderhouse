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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

@login_required
def principal(request):    
    return render(request, 'coder/principal.html')





def mi_layout_static(request):
    return render(request, 'coder/layout-static.html')
def mi_login(request):
    return render(request, 'coder/login.html')
def mi_recovery_password(request):
    return render(request, 'coder/password.html')

class NuevoPaciente(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'numero_ci', 'numero_cel', 'motivo_consulta']
    success_url = 'index.html'

class PacientesList(LoginRequiredMixin, ListView):
    model = Paciente

class PacienteDetalle(DetailView):
    model = Paciente

class UsuarioLogin(LoginView):
    template_name = 'coder/login.html'
    next_page = reverse_lazy("index")

class UsuarioLogout(LogoutView):
    template_name = 'coder/logout.html'


