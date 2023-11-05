from django.db import models


class Reporte(models.Model):
    nombre = models.CharField(max_length=255)
    matricula = models.CharField(max_length=9)
    habitacion = models.CharField(max_length=4)
    problema = models.CharField(max_length=1024)
    estatus = models.CharField(max_length=20, default='No resuelto')
    fecha_reporte = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.habitacion
# Create your models here.
