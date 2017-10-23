from __future__ import unicode_literals
from django.contrib.auth.models import User
from productos.models import Producto
from django.db import models

# Create your models here.
class Factura(models.Model):
	numero=models.IntegerField
	cliente = models.ForeignKey(User)
	fecha= models.DateField()

	def __str__(self):
		return "%s-%s" %(self.numero, self.cliente)


class Detalle(models.Model):
	factura = models.ForeignKey(Factura)
	producto = models.ForeignKey(Producto)
	cantidad=models.IntegerField()
	precio=models.IntegerField()

	def __str__(self):
		return "%s-%s" % (self.id, self.factura)