from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cliente(models.Model):
	direccion = models.CharField(max_length=500)
	telefono = models.CharField(max_length=14)
	genero = models.CharField(max_length=1)
	edad = models.CharField(max_length=200)

	def __str__(self):
		return " %s - %s - %s - %s"%(self.direccion, self.telefono, self.genero, self.edad)
