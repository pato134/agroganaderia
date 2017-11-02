# from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.


class Proveedor(models.Model):
	nombres=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=200)
	cedula=models.CharField(max_length=200)
	telefono = models.CharField(max_length=10)
	direccion = models.CharField(max_length=200)
	nombre_empresa = models.CharField(max_length=200)
	direccion_empresa = models.CharField(max_length=200)
	telefono_empresa = models.CharField(max_length=200)
	 

	def __str__(self):
		return " %s - %s - %s - %s - %s - %s" %(self.cedula ,self.telefono, self.direccion, self.nombre_empresa, self.direccion_empresa, self.telefono_empresa)
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Proveedor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Proveedor.save()
    """