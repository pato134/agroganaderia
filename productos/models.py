from __future__ import unicode_literals

from django.db import models




# Create your models here.
class TipoProducto(models.Model):
	image = models.FileField(null=True, blank=True)
	nombre = models.CharField(max_length=200)
	valor_tipo_producto = models.CharField(max_length=200)
	fecha_vencimiento = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	image = models.FileField(null=True, blank=True)
	nombre= models.CharField(max_length=200)
	tipo_producto = models.ForeignKey (TipoProducto)
	valor_producto = models.CharField(max_length=200)
	fecha_vencimiento = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre