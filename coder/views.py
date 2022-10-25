from django.shortcuts import render, get_object_or_404
from django.views import View
from coder.models import Paciente
from coder.forms import PacienteForm

class ListarPacientes(View):
    template_name = 'coder/lista_de_pacientes.html'

    def get(self, request):
        pacientes = Paciente.objects.all()
        return render(request, self.template_name, {'pacientes': pacientes})

class AgregarPacientes(View):
    template_name = 'coder/agregar_pacientes.html'
    form_class = PacienteForm
    initial = {'nombre':'', 'apellido':'', 'fecha_de_nacimiento':'', 'numero_ci':'', 'numero_cel':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.template_name, {'form': form})

class ActualizarPacientes(View):
    template_name = 'coder/actualizar_paciente.html'
    success_template = 'coder/exito.html'
    form_class = PacienteForm
    initial = {'nombre':'', 'apellido':'', 'fecha_de_nacimiento':'', 'numero_ci':'', 'numero_cel':''}

    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = self.form_class(instance=paciente)
        return render(request, self.template_name, {'form': form, 'pk': pk})

    def post(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        form = self.form_class(request.POST, instance=paciente)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.success_template)
        



