from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    numero_ci = models.IntegerField()
    numero_cel = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id}, Nombre:{self.nombre}, Apellido:{self.apellido}, CI:{self.numero_ci}'

class Funcionario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20)
    numero_func = models.IntegerField()    

    def __str__(self):
        return f'ID: {self.id}, Nombre:{self.nombre}, Apellido:{self.apellido}, Número de funcionario:{self.numero_func}'

class ConsultaMedica(models.Model):
    medico = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)    
    dias_consulta = models.CharField(max_length=20)

    def __str__(self):
        return f'ID: {self.id}, Especialidad:{self.especialidad}, Médico:{self.medico}, Dias de consulta:{self.dias_consulta}'