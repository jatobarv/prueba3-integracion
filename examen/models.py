from django.db import models
from django.utils import timezone


class usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=10)
    apellido_mat = models.CharField(max_length=10)
    fecha_nac = models.DateTimeField(default=timezone.now)
    ocupacion = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=10)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return self.nombres

class producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class servicio(models.Model):
    rut = models.ForeignKey('usuario', on_delete=models.CASCADE)
    idproducto = models.ForeignKey('producto', on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(auto_now=False)

    def __str__(self):
        return str(self.fecha)
