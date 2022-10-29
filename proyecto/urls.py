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
from cgitb import handler
from logging import exception
from re import template
from urllib import request
from django.contrib import admin
from django.urls import path
from coder.views import (NuevoPaciente, PacienteDetalle, PacientesList, index, mi_charts, mi_error_404, mi_error_500,
                        mi_layout_sidenav_ligth, mi_layout_static, mi_login, mi_recovery_password)
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('coder/charts/', mi_charts),
    path('coder/layout-sidenav-light.html/', mi_layout_sidenav_ligth),
    path('coder/layout-static/', mi_layout_static),
    path('coder/login/', mi_login),
    path('coder/password/', mi_recovery_password),
    path('coder/lista-pacientes/', PacientesList.as_view(), name='lista_pacientes'),
    path('index/nuevo-paciente/', NuevoPaciente.as_view(), name='nuevo_paciente'),
    path('coder/paciente-detalle/<int:pk>/', PacienteDetalle.as_view()),
]


handler404 = 'coder.views.mi_error_404'
handler500 = 'coder.views.mi_error_500'


