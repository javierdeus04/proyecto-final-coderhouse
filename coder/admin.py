from django.contrib import admin
from coder.models import Funcionario, Paciente, ConsultaMedica

admin.site.register(Paciente)
admin.site.register(Funcionario)
admin.site.register(ConsultaMedica)