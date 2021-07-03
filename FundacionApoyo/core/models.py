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
    