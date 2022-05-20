from django.db import models

# Create your models here.
class Datos(models.Model):

    dni = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    agno = models.DateField()
