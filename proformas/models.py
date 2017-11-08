from __future__ import unicode_literals
from django.contrib.auth.models import User
from productos.models import Producto
from django.db import models


# Create your models here.

class Proforma(models.Model):
    """En esta clase  se realizo el registro de la proforma  con sus respectivos atributos las entidades""" 
    numero=models.IntegerField(default=1)
    cliente = models.ForeignKey(User,blank=True,null=True)
    fecha= models.DateField()
    iva=models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    total=models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)

    def __str__(self):
        return "%s - %s - %s" %(self.id, self.numero, self.cliente)

class DetalleProforma(models.Model):
    """En esta clase  se realizo el registro de los detalles de la  proforma  con sus respectivos atributos las entidades""" 
    proforma = models.ForeignKey(Proforma)
    producto = models.ForeignKey(Producto)
    cantidad=models.IntegerField()
    precio=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s - %s" % (self.id, self.proforma) 
