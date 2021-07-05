from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Aportes(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=255)
    aporte = models.IntegerField()
    fecha = models.DateField(default=datetime.now)

class Ingresos(models.Model):
    fechaIngreso = models.DateField()
    ingresos = models.IntegerField(default=0)
    
class Ficha(models.Model):
    idFicha = models.AutoField(primary_key=True)
    Medicamentos = models.CharField(max_length=30)
    Cuidados_especiales = models.CharField(max_length=300)
    Situación_salud = models.CharField(max_length= 300)
    NombreApe = models.CharField(max_length= 200)
    NombreCom_fam = models.CharField(max_length=200)
    rutFam = models.CharField(max_length= 20,null=True)
    sexoFam = models.CharField(max_length=1)
    fechaNa_fam = models.DateField(default=datetime.now)
    Domicilio_fam = models.CharField(max_length= 40)
    Ocupacion_fam = models.CharField(max_length= 30)