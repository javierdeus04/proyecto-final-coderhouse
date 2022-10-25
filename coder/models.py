from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    numero_ci = models.IntegerField(max_length=8)
    numero_cel = models.IntegerField(max_length=9)

    def __str__(self):
        return f'ID: {self.id}, Nombre:{self.nombre}, Apellido:{self.apellido}, CI:{self.numero_ci}'

class Funcionario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    numero_ci = models.IntegerField(max_length=8)
    numero_cel = models.IntegerField(max_length=9)
    numero_func = models.IntegerField(max_length=5)

    def __str__(self):
        return f'ID: {self.id}, Nombre:{self.nombre}, Apellido:{self.apellido}, Número de funcionario:{self.numero_func}'

