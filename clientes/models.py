from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	direccion = models.CharField(max_length=500)
	telefono = models.CharField(max_length=14)
	genero = models.CharField(max_length=1)
	edad = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre	