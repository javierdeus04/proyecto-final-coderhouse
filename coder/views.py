from django.shortcuts import render, get_object_or_404
from django.views import View
from coder.models import ConsultaMedica, Funcionario, Paciente
from coder.forms import Buscar, PacienteForm, FuncionarioForm, ConsultaForm, BuscarConsulta

class ListarPacientes(View):
    template_name = 'coder/lista_de_pacientes.html'

    def get(self, request):
        pacientes = Paciente.objects.all()
        return render(request, self.template_name, {'pacientes': pacientes})

class ListarFuncionarios(View):
    template_name = 'coder/lista_de_funcionarios.html'

    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, self.template_name, {'funcionarios': funcionarios})

class ListarConsultas(View):
    template_name = 'coder/lista_de_consultas.html'

    def get(self, request):
        consultas_medicas = ConsultaMedica.objects.all()
        return render(request, self.template_name, {'consultas_medicas': consultas_medicas})

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

class AgregarFuncionarios(View):
    template_name = 'coder/agregar_funcionarios.html'
    form_class = FuncionarioForm
    initial = {'nombre':'', 'apellido':'', 'cargo':'', 'numero_func':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.template_name, {'form': form})

class AgregarConsulta(View):
    template_name = 'coder/agregar_consulta_medica.html'
    form_class = ConsultaForm
    initial = {'medico':'', 'especialidad':'', 'dias':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.template_name, {'form': form})


class BuscarPaciente(View):

    form_class = Buscar
    template_name = 'coder/buscar_paciente.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_pacientes = Paciente.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_pacientes':lista_pacientes})

        return render(request, self.template_name, {"form": form})

class BuscarFuncionario(View):

    form_class = Buscar
    template_name = 'coder/buscar_funcionario.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_funcionarios = Funcionario.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_funcionarios':lista_funcionarios})

        return render(request, self.template_name, {"form": form})

class BuscarConsulta(View):

    form_class = BuscarConsulta
    template_name = 'coder/buscar_consultas_medicas.html'
    initial = {"especialidad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            especialidad = form.cleaned_data.get("especialidad")
            consultas_medicas = ConsultaMedica.objects.filter(especialidad__icontains=especialidad).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'consultas_medicas':consultas_medicas})

        return render(request, self.template_name, {"form": form})
        



