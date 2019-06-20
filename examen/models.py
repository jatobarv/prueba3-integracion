from django.db import models
import datetime


class paciente(models.Model):
    rut_paciente = models.CharField(max_length=12)
    nombres = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=10)
    apellido_mat = models.CharField(max_length=10)
    fecha_nac = models.DateTimeField(default=datetime.datetime.now())
    ocupacion = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=10)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    prevision = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres
