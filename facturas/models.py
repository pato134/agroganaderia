from __future__ import unicode_literals
from django.contrib.auth.models import User
from productos.models import Producto
from django.db import models

# Create your models here.
class Factura(models.Model):
	"""En esta clase  se realizo el registro de la factura  con los datos de los clientes   con sus respectivos atributos""" 
	numero=models.IntegerField(default=1)
	cliente = models.ForeignKey(User)
	fecha= models.DateField()
	iva=models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
	total=models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)

	def __str__(self):
		return "%s - %s - %s" %(self.id, self.numero, self.cliente)


class Detalle(models.Model):
	"""En esta clase  se realizo el registro de la factura  con los datos de los clientes   con sus respectivos atributos""" 
	factura = models.ForeignKey(Factura)
	producto = models.ForeignKey(Producto)
	cantidad=models.IntegerField()
	precio=models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return "%s - %s" % (self.id, self.factura)

class Pago(models.Model):
	"""En esta clase  se realizo el registro de la factura  con los datos de los clientes   con sus respectivos atributos""" 
	factura = models.ForeignKey(Factura)
	comprobante=models.ImageField()
	sugerencia=models.TextField()

	def __str__(self):
		return "%s - %s - %s" % (self.comprobante, self.sugerencia)