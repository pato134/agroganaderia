from __future__ import unicode_literals
from django.db import models


# Create your models here.
class TipoProducto(models.Model):
	image = models.FileField(null=True, blank=True)
	nombre = models.CharField(max_length=200)


	def __str__(self):
		return self.nombre

class Producto(models.Model):
	image = models.FileField(null=True, blank=True)
	nombre= models.CharField(max_length=200)
	tipo_producto = models.ForeignKey (TipoProducto)
	valor_producto = models.DecimalField(max_digits=5, decimal_places=2)
	fecha_vencimiento = models.DateField()
	stock= models.IntegerField()
	def __str__(self):
		return self.nombre