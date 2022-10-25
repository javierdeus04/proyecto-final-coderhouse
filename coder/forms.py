from django import forms
from coder.models import Paciente

class PacienteForm(forms.ModelForm):

    fecha_de_nacimiento = forms.DateField(label='Fecha de nacimiento', input_formats=['%d/%m/%Y'], 
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    
    class Meta:
        model = Paciente
        fields = {'nombre', 'apellido', 'fecha_de_nacimiento', 'numero_ci', 'numero_cel'}

