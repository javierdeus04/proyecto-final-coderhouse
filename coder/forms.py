from django import forms
from coder.models import ConsultaMedica, Funcionario, Paciente

class PacienteForm(forms.ModelForm):

    fecha_de_nacimiento = forms.DateField()
    
    class Meta:
        model = Paciente
        fields = {'nombre', 'apellido', 'fecha_de_nacimiento', 'numero_ci', 'numero_cel'}

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = {'nombre', 'apellido', 'cargo', 'numero_func'}

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = ConsultaMedica
        fields = {'medico', 'especialidad', 'dias_consulta'}


class BuscarPorNombrePac(forms.Form):
    nombre = forms.CharField(max_length=100)

class BuscarPorNumFunc(forms.Form):    
    numero_func = forms.IntegerField()

class BuscarPorEsp(forms.Form):
    especialidad = forms.CharField(max_length=100)


