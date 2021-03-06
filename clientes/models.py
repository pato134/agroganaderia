from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class Cliente(models.Model):
	"""En esta clase  se realizo el registro de los clientes  con sus respectivos atributos"""
	GENEROS=(
		("M","MASCULINO"), 
		("F","FEMENINO"), 
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cedula =models.CharField(max_length= 200, blank=True, null=True)
	direccion =models.CharField(max_length= 200)
	telefono=models.CharField(max_length=200)
	genero = models.CharField(max_length=1,choices=GENEROS)
	lugar=models.CharField(max_length=200)
	edad = models.IntegerField(blank=True, null=True)
	 

	def __str__(self):
		return " %s -%s %s -%s"%(self.cedula, self.direccion ,self.telefono, self.lugar)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.cliente.save()
