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

class examenes(models.Model):
    codiexamen = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class agenda(models.Model):
    rut_paciente = models.ForeignKey('paciente', on_delete=models.CASCADE)
    codiexamen = models.ForeignKey('examenes', on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.datetime.now())
    hora = models.TimeField(auto_now=False)

    def __str__(self):
        return str(self.fecha)
