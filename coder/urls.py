from django.urls import path
from coder.views import (principal, NuevoPaciente, PacienteDetalle,
                         PacientesList, mi_layout_static, UsuarioLogin, UsuarioLogout)

urlpatterns = [
    path('', principal, name='index'),
    path('coder/layout-static/', mi_layout_static),
    path('coder/lista-pacientes/', PacientesList.as_view(), name='lista_pacientes'),
    path('index/nuevo-paciente/', NuevoPaciente.as_view(), name='nuevo_paciente'),
    path('coder/paciente-detalle/<int:pk>/', PacienteDetalle.as_view()),
    path('login/', UsuarioLogin.as_view(), name="usuario-login"),
    path('logout/', UsuarioLogout.as_view(), name="usuario-logout"),
]


