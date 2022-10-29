from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    numero_ci = models.IntegerField()
    numero_contacto = models.IntegerField()
    motivo_consulta = models.CharField(max_length=20)


    def __str__(self):
          return f'{self.nombre} {self.apellido} - CI:{self.numero_ci}'