from django.db import models

# Create your models here.
class Trabajadores(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.CharField(max_length=40)
    cargo=models.CharField(max_length=40)
    fechaInicio=models.DateField(max_length=40)
    fechatermino=models.DateField(max_length=10)
    saldo=models.CharField(max_length=40)
    casado=models.CharField(max_length=40)
